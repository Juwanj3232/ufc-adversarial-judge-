#!/usr/bin/env python3
"""
UFC ADVERSARIAL JUDGE - MATCHUP PREDICTOR
=========================================
    python3 scripts/predict_fight.py "Israel Adesanya" "Shara Magomedov" --date 2026-12-05
    python3 scripts/predict_fight.py "Adesanya" "Shara" --refresh     # pull the latest data first
    python3 scripts/predict_fight.py "Adesanya" "Shara" --simulate    # what-if sandbox

What you get
  1. Tale of the tape: each fighter's UFC numbers (same definitions as UFCStats),
     Elo rating, strength of schedule, recent form and durability.
  2. Win probability from the same model that was backtested in backtest.py,
     with every fighter's stats projected to the fight date (age, layoff).
  3. The reasons: which factors push toward each fighter and by roughly how many
     percentage points.
  4. A matchup breakdown for the human analyst: range, volume vs defense,
     grappling paths, quality of opposition, age and durability.

How much to trust it
  In honest walk-forward testing the model picks about 62% of UFC winners overall
  and about 66% of fights that were genuinely won. When it says 65-70%, the
  favourite has won about 68% of the time. It cannot see injuries, camp changes,
  weight cuts or styles it has no numbers for.
"""

import argparse
import difflib
import os
import sys

import joblib
import numpy as np
import pandas as pd

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import features as F  # noqa: E402
import judge_model as J  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(ROOT, 'models', 'ufc_judge_model.joblib')


# ─── Loading ─────────────────────────────────────────────────────────────────

def check_freshness(refresh=False):
    import update_data
    age = update_data.data_age_days()
    if refresh or age is None:
        update_data.refresh()
        return
    if age > update_data.STALE_AFTER_DAYS:
        print(f"WARNING: Fight data is {age:.0f} days old. Run with --refresh (or scripts/update_data.py) "
              f"so recent results are included.")


def load_resources():
    if not os.path.exists(MODEL_PATH):
        import train_model
        train_model.main(evaluate=False)
    bundle = joblib.load(MODEL_PATH)
    bouts, fighters, profiles = F.load_inputs()
    _, states, league = F.replay(bouts, profiles)
    return bundle, states, league, profiles


def find_fighter(query, states):
    """Exact name, then whole-word / prefix match (most UFC fights wins ties), then fuzzy."""
    q = query.lower().strip()
    pool = [(fid, st['name'], st['fights']) for fid, st in states.items() if st['name']]
    exact = [p for p in pool if p[1].lower() == q]
    if exact:
        if len(exact) > 1:
            print(f"NOTE: {len(exact)} UFC fighters are named '{exact[0][1]}'; using the one with the most UFC fights.")
        return max(exact, key=lambda p: p[2])[0]
    scored = []
    for fid, name, n in pool:
        parts = name.lower().split()
        if q in parts:
            scored.append((3, n, fid))
        elif any(p.startswith(q) for p in parts):
            scored.append((2, n, fid))
        elif q in name.lower():
            scored.append((1, n, fid))
    if scored:
        return max(scored)[2]
    names = [p[1] for p in pool]
    close = difflib.get_close_matches(query, names, n=1, cutoff=0.6)
    if close:
        return max((p for p in pool if p[1] == close[0]), key=lambda p: p[2])[0]
    return None


def matchup_row(va, vb):
    row = {}
    for f in F.FIGHTER_FIELDS:
        row[f'a_{f}'] = va[f]
        row[f'b_{f}'] = vb[f]
        a, b = va[f], vb[f]
        row[f'{f}_diff'] = (a - b) if pd.notna(a) and pd.notna(b) else np.nan
    return pd.Series(row)


def predict(bundle, va, vb, name_a, name_b):
    row = matchup_row(va, vb)
    frame = row[F.FEATURE_COLUMNS].to_frame().T.astype(float)
    p_a = float(J.predict_sym(bundle['model'], frame)[0])
    expl = J.explain(bundle['model'], row, name_a, name_b, prob_a=p_a)
    return p_a, expl


# --- Printing (one double-line box) ------------------------------------------

BASE_WIDTH = 68          # inner width of the box
NAME_COL = 16            # tale-of-the-tape value columns
LABEL_COL = 28           # tale-of-the-tape centre column
FACTOR_COL = 32          # "why" table factor column
LEFT_EIGHTHS = ' ▏▎▍▌▋▊▉'

# Shorter factor labels so the "why" table fits the box
SHORT_FACTOR = {
    'opp_elo_avg_diff': 'Strength of schedule',
    'recent_opp_elo_diff': 'Recent schedule (last ~3)',
    'recent_perf_diff': 'Results vs expectation (recent)',
    'recent_margin_diff': 'Recent striking form (last ~3)',
    'recent_ctrl_share_diff': 'Recent grappling control',
    'recent_win_diff': 'Recent results (last ~3)',
    'strike_margin_diff': 'Net striking margin / min',
}


class Box:
    """Collects lines and frames them with box-drawing characters."""

    def __init__(self, width):
        self.w = width
        self.lines = ['╔' + '═' * width + '╗']

    def row(self, text=''):
        self.lines.append('║' + text[:self.w].ljust(self.w) + '║')

    def thin(self):
        self.lines.append('╟' + '─' * self.w + '╢')

    def section(self, title=None):
        if title is None:
            self.lines.append('╠' + '═' * self.w + '╣')
        else:
            head = f'══[ {title} ]'
            self.lines.append('╠' + head + '═' * (self.w - len(head)) + '╣')

    def wrapped(self, text, indent=1):
        import textwrap
        for part in textwrap.wrap(text, self.w - indent * 2):
            self.row(' ' * indent + part)

    def render(self):
        return '\n'.join(self.lines + ['╚' + '═' * self.w + '╝'])


def bar(value, max_value, width):
    """Horizontal bar with eighth-block precision, rounded down."""
    if max_value <= 0 or width <= 0:
        return ''
    eighths = int(max(0.0, min(value / max_value, 1.0)) * width * 8)
    full, part = divmod(eighths, 8)
    return '█' * full + (LEFT_EIGHTHS[part] if part else '')


def tale_rows(va, vb, sa, sb):
    def pct(x): return 'n/a' if pd.isna(x) else f'{x:.0%}'
    def num(x, d=2): return 'n/a' if pd.isna(x) else f'{x:.{d}f}'
    def raw(st, key):
        mins = st['sec'] / 60
        return {
            'slpm': st['sig_l'] / mins if mins else np.nan,
            'sapm': st['opp_sig_l'] / mins if mins else np.nan,
            'acc': st['sig_l'] / st['sig_a'] if st['sig_a'] else np.nan,
            'def': 1 - st['opp_sig_l'] / st['opp_sig_a'] if st['opp_sig_a'] else np.nan,
            'td': st['td_l'] / mins * 15 if mins else np.nan,
            'tdd': 1 - st['opp_td_l'] / st['opp_td_a'] if st['opp_td_a'] else np.nan,
            'sub': st['sub'] / mins * 15 if mins else np.nan,
        }[key]
    return [
        ('UFC record (W-L)', f"{sa['wins']}-{sa['losses']}", f"{sb['wins']}-{sb['losses']}"),
        ('Elo rating', num(va['elo'], 0), num(vb['elo'], 0)),
        ('Avg opponent Elo (schedule)', num(va['opp_elo_avg'], 0), num(vb['opp_elo_avg'], 0)),
        ('Streak', f"{va['streak']:+d}", f"{vb['streak']:+d}"),
        ('Age on fight date', num(va['age'], 1), num(vb['age'], 1)),
        ('Height / Reach (cm)', f"{num(va['height_cm'], 0)} / {num(va['reach_cm'], 0)}",
         f"{num(vb['height_cm'], 0)} / {num(vb['reach_cm'], 0)}"),
        ('Days since last fight', num(va['layoff_days'], 0), num(vb['layoff_days'], 0)),
        ('Sig. strikes landed / min', num(raw(sa, 'slpm')), num(raw(sb, 'slpm'))),
        ('Sig. strikes absorbed / min', num(raw(sa, 'sapm')), num(raw(sb, 'sapm'))),
        ('Striking accuracy', pct(raw(sa, 'acc')), pct(raw(sb, 'acc'))),
        ('Striking defense', pct(raw(sa, 'def')), pct(raw(sb, 'def'))),
        ('Recent striking margin / min', num(va['recent_margin']), num(vb['recent_margin'])),
        ('Takedowns / 15 min', num(raw(sa, 'td')), num(raw(sb, 'td'))),
        ('Takedown defense', pct(raw(sa, 'tdd')), pct(raw(sb, 'tdd'))),
        ('Control time share', pct(va['ctrl_share']), pct(vb['ctrl_share'])),
        ('Submission attempts / 15 min', num(raw(sa, 'sub')), num(raw(sb, 'sub'))),
        ('Knockdowns scored / absorbed', f"{sa['kd']:.0f} / {sa['opp_kd']:.0f}", f"{sb['kd']:.0f} / {sb['opp_kd']:.0f}"),
        ('KO/TKO losses', f"{va['ko_losses']}", f"{vb['ko_losses']}"),
    ]


def breakdown_notes(na, nb, va, vb):
    notes = []
    rd = va['reach_cm'] - vb['reach_cm'] if pd.notna(va['reach_cm']) and pd.notna(vb['reach_cm']) else 0
    if abs(rd) >= 8:
        longer, shorter = (na, nb) if rd > 0 else (nb, na)
        notes.append(('RANGE', f"{longer} has a {abs(rd) / 2.54:.1f}-inch reach advantage; {shorter} must close distance."))
    else:
        notes.append(('RANGE', 'Reach is close; neither fighter can live on distance alone.'))
    notes.append(('VOLUME', f"{na} margin {va['strike_margin']:+.2f}/min (recent {va['recent_margin']:+.2f}); "
                            f"{nb} margin {vb['strike_margin']:+.2f}/min (recent {vb['recent_margin']:+.2f})."))
    for att, dfn, an, dn in ((va, vb, na, nb), (vb, va, nb, na)):
        if att['td_avg'] >= 1.5 and dfn['td_def'] < 0.70:
            notes.append(('GRAPPLING', f"{an} lands {att['td_avg']:.1f} TD/15 min against {dn}'s "
                                       f"{dfn['td_def']:.0%} takedown defense."))
    if va['td_avg'] < 0.6 and vb['td_avg'] < 0.6:
        notes.append(('GRAPPLING', 'Neither fighter wrestles much; expect a fight on the feet.'))
    gap = va['opp_elo_avg'] - vb['opp_elo_avg']
    if abs(gap) >= 40:
        tougher, softer = (na, nb) if gap > 0 else (nb, na)
        notes.append(('OPPOSITION', f"{tougher} has faced clearly tougher opponents (avg Elo "
                                    f"{max(va['opp_elo_avg'], vb['opp_elo_avg']):.0f} vs "
                                    f"{min(va['opp_elo_avg'], vb['opp_elo_avg']):.0f}); {softer}'s numbers "
                                    f"came against weaker competition."))
    if pd.notna(va['age']) and pd.notna(vb['age']) and abs(va['age'] - vb['age']) >= 4:
        older = na if va['age'] > vb['age'] else nb
        notes.append(('AGE', f"{older} is {abs(va['age'] - vb['age']):.1f} years older"
                             + (', and past 35, where UFC win rates drop sharply.'
                                if max(va['age'], vb['age']) >= 35 else '.')))
    for v, n in ((va, na), (vb, nb)):
        if v['ko_losses'] >= 2 or v['kd_absorbed_avg'] >= 0.6:
            notes.append(('DURABILITY', f"{n} has {v['ko_losses']} KO/TKO losses and absorbs "
                                        f"{v['kd_absorbed_avg']:.2f} knockdowns per 15 min."))
    return notes


def factor_rows(expl, name, is_a, n=6):
    rows = []
    for _, r in expl[expl['favours'] == name].head(n).iterrows():
        mine, theirs = (r['value_a'], r['value_b']) if is_a else (r['value_b'], r['value_a'])
        m, t = J.format_value(r['feature'], mine), J.format_value(r['feature'], theirs)
        if m.endswith(' cm') and t.endswith(' cm'):
            values = f'{m[:-3]} v {t[:-3]} cm'
        else:
            values = f'{m} v {t}'
        label = SHORT_FACTOR.get(r['feature'], r['factor'])[:FACTOR_COL]
        rows.append((label, values, abs(r['push_pts'])))
    return rows


def verdict_lines(box, na, nb, p_a):
    winner, conf = (na, p_a) if p_a >= 0.5 else (nb, 1 - p_a)
    tier = ('Clear favourite' if conf >= 0.68 else 'Moderate favourite' if conf >= 0.60
            else 'Slight edge' if conf >= 0.54 else 'Toss-up')
    left = f'  {na.upper()}  {p_a:.1%}'
    right = f'{1 - p_a:.1%}  {nb.upper()}  '
    box.row(left + ' ' * max(1, box.w - len(left) - len(right)) + right)
    width = box.w - 4
    filled = int(round(p_a * width))
    box.row('  ' + '█' * filled + '░' * (width - filled) + '  ')
    box.row()
    box.row(f'  ▌PICK  {winner.upper()}   ·   {conf:.0%}   ·   {tier.upper()}')


def render_report(na, nb, va, vb, sa, sb, p_a, expl):
    tale = tale_rows(va, vb, sa, sb)
    name_w = max(NAME_COL, len(na), len(nb), *(len(r[1]) for r in tale), *(len(r[2]) for r in tale))
    label_w = max(LABEL_COL, *(len(r[0]) for r in tale))
    width = max(BASE_WIDTH, 1 + name_w + 3 + label_w + 3 + name_w + 1)
    box = Box(width)

    # Tale of the tape
    box.row('T A L E   O F   T H E   T A P E'.center(width))
    box.thin()
    def tape(left, mid, right):
        box.row(' ' + left.rjust(name_w) + ' │ ' + mid.center(label_w) + ' │ ' + right.ljust(name_w) + ' ')
    tape(na.upper(), 'V S', nb.upper())
    box.thin()
    for label, a, b in tale:
        tape(a, label, b)

    # Verdict
    box.section('VERDICT')
    verdict_lines(box, na, nb, p_a)

    # Why the model leans each way
    box.section('WHY THE MODEL LEANS EACH WAY')
    groups = [(na, factor_rows(expl, na, True)), (nb, factor_rows(expl, nb, False))]
    val_w = max([13] + [len(v) for _, rows in groups for _, v, _ in rows])
    bar_w = width - (1 + FACTOR_COL + 1 + val_w + 1 + 1 + 4 + 1)
    top = max([0.0] + [p for _, rows in groups for _, _, p in rows])
    box.row(' ' + 'FACTOR'.ljust(FACTOR_COL) + ' ' + 'THEM v OPP'.ljust(val_w) + ' '
            + 'IMPACT'.ljust(bar_w) + ' ' + 'PTS'.rjust(4) + ' ')
    for i, (name, rows) in enumerate(groups):
        box.thin()
        box.row(' ▌' + name.upper())
        if not rows:
            box.row(' (no meaningful factors)')
        for label, values, pts in rows:
            box.row(' ' + label.ljust(FACTOR_COL) + ' ' + values.ljust(val_w) + ' '
                    + bar(pts, top, bar_w).ljust(bar_w) + ' ' + f'{pts:.1f}'.rjust(4) + ' ')
    box.row(' Impact ≈ percentage points of win probability each factor adds.')

    # Matchup breakdown
    box.section('MATCHUP BREAKDOWN')
    import textwrap
    notes = breakdown_notes(na, nb, va, vb)
    text_w = width - (1 + 12 + 1 + 1)
    for i, (label, text) in enumerate(notes):
        if i:
            box.row()
        for j, part in enumerate(textwrap.wrap(text, text_w)):
            box.row(' ' + (label if j == 0 else '').ljust(12) + ' ' + part)

    # Footer
    box.section()
    box.wrapped('Career numbers use UFCStats definitions and count UFC fights only. '
                'The model pulls fighters with little cage time toward the UFC average.')
    return box.render()


def simulator(bundle, na, nb, va, vb):
    base_a, base_b = dict(va), dict(vb)
    editable = {'1': ('slpm', 'Sig. strikes landed / min'), '2': ('sapm', 'Sig. strikes absorbed / min'),
                '3': ('str_def', 'Striking defense (0-1)'), '4': ('td_avg', 'Takedowns / 15 min'),
                '5': ('td_def', 'Takedown defense (0-1)'), '6': ('recent_margin', 'Recent striking margin / min')}
    while True:
        print('\nWHAT-IF: change a stat and re-run the model')
        for k, (_, label) in editable.items():
            print(f"  [{k}] {label}")
        print('  [r] reset   [0] exit')
        c = input('Choice: ').strip().lower()
        if c == '0':
            return
        if c == 'r':
            va, vb = dict(base_a), dict(base_b)
        elif c in editable:
            field, label = editable[c]
            who = input(f"Fighter? [1] {na}  [2] {nb}: ").strip()
            target = va if who == '1' else vb
            try:
                target[field] = float(input(f"New {label} (now {target[field]:.2f}): ").strip())
                target['strike_margin'] = target['slpm'] - target['sapm']
            except ValueError:
                print('Not a number.')
                continue
        p_a, _ = predict(bundle, va, vb, na, nb)
        box = Box(max(BASE_WIDTH, len(na) + len(nb) + 24))
        box.row('W H A T - I F   R E S U L T'.center(box.w))
        box.thin()
        verdict_lines(box, na, nb, p_a)
        print(box.render())


def run_prediction(q1, q2, fight_date=None, simulate=False, refresh=False):
    check_freshness(refresh)
    bundle, states, league, profiles = load_resources()
    ids = [find_fighter(q, states) for q in (q1, q2)]
    for q, fid in zip((q1, q2), ids):
        if fid is None:
            print(f"ERROR: No UFC fighter found matching '{q}'.")
            return None
    date = pd.Timestamp(fight_date) if fight_date else pd.Timestamp.today().normalize()
    sa, sb = states[ids[0]], states[ids[1]]
    na, nb = sa['name'], sb['name']
    va = F.fighter_view(sa, league, profiles.get(ids[0]), date)
    vb = F.fighter_view(sb, league, profiles.get(ids[1]), date)

    print(f"\nModel trained on {bundle['training_fights']:,} UFC fights through {bundle['trained_through']}; "
          f"projecting to {date:%Y-%m-%d}.")
    p_a, expl = predict(bundle, va, vb, na, nb)
    print(render_report(na, nb, va, vb, sa, sb, p_a, expl))
    if simulate:
        simulator(bundle, na, nb, va, vb)
    return p_a, expl


if __name__ == '__main__':
    ap = argparse.ArgumentParser(description='Predict a UFC matchup with the Adversarial Judge')
    ap.add_argument('fighter1', nargs='?')
    ap.add_argument('fighter2', nargs='?')
    ap.add_argument('--date', help='fight date YYYY-MM-DD (default: today)')
    ap.add_argument('--simulate', action='store_true', help='open the what-if sandbox')
    ap.add_argument('--refresh', action='store_true', help='download the latest fight data first')
    a = ap.parse_args()
    f1 = a.fighter1 or input('Fighter 1: ').strip()
    f2 = a.fighter2 or input('Fighter 2: ').strip()
    run_prediction(f1, f2, fight_date=a.date, simulate=a.simulate, refresh=a.refresh)
