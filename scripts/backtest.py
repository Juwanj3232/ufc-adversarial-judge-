#!/usr/bin/env python3
"""
UFC ADVERSARIAL JUDGE - HISTORICAL BACKTEST & FIGHT-BY-FIGHT EXPLANATIONS
=========================================================================
    python3 scripts/backtest.py                       # default spotlight set
    python3 scripts/backtest.py --fighter "Israel Adesanya" --fighter "Alex Pereira"
    python3 scripts/backtest.py --since 2025-06-01    # every main event / title fight since a date

For each spotlight fight:
  1. Train the model ONLY on fights that happened before that fight's date.
  2. Predict it using each fighter's stats exactly as they stood that morning.
  3. Explain the prediction: which factors pushed toward each fighter, and how much.
  4. Grade what actually happened (win_anatomy.py): clear win, contested decision,
     comeback finish, ... and the route (striking / grappling / mixed).
  5. Judge the model: right for the right reasons, right by a different route,
     wrong on a coin-flip, wrong on a fight-changing moment, or a genuine misread.

It also scores every fight since 2012 from the walk-forward run in train_model.py,
broken down by how each fight was won, to show where the model is reliable and
where outcomes are close to unpredictable.

Output: reports/backtest_report.md and reports/backtest_fights.csv
"""

import argparse
import os
import sys
import time

import numpy as np
import pandas as pd

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import judge_model as J  # noqa: E402
import win_anatomy as W  # noqa: E402
from features import FEATURE_COLUMNS  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROCESSED_DIR = os.path.join(ROOT, 'data', 'processed')
REPORT_DIR = os.path.join(ROOT, 'reports')

DEFAULT_FIGHTERS = ['Israel Adesanya', 'Shara Magomedov']
DEFAULT_SINCE = '2025-01-01'

ROUTE_OF_GROUP = {'striking': 'striking', 'power': 'striking', 'durability': 'striking',
                  'grappling': 'grappling'}


def is_main_event(row):
    ev = str(row['event']).lower()
    last = lambda n: str(n).split()[-1].lower()
    return last(row['fighter_a']) in ev and last(row['fighter_b']) in ev


def pick_targets(bouts, fighters, since):
    mask = bouts['result'].isin(['A', 'B'])
    by_fighter = bouts['fighter_a'].isin(fighters) | bouts['fighter_b'].isin(fighters)
    marquee = (bouts['date'] >= since) & (bouts['title_fight'] | bouts.apply(is_main_event, axis=1))
    return bouts[mask & (by_fighter | marquee)].copy()


def model_route(expl, pick):
    """Which part of the game the model mainly relied on for its pick."""
    toward = expl[expl['favours'] == pick].head(8)
    totals = {'striking': 0.0, 'grappling': 0.0, 'profile': 0.0}
    for _, r in toward.iterrows():
        totals[ROUTE_OF_GROUP.get(r['group'], 'profile')] += abs(r['push_logodds'])
    total = sum(totals.values()) or 1.0
    best = max(('striking', 'grappling'), key=lambda k: totals[k])
    return best if totals[best] / total >= 0.3 else 'profile', totals


def reasoning_verdict(pick, correct, conf, m_route, fight):
    t, route, sup = fight['win_type'], fight['win_route'], fight['stats_support_winner']
    winner = fight['winner']
    if correct:
        if m_route == 'profile':
            return ('Right, on overall profile',
                    f"The model backed {pick} mainly on overall profile (quality of opposition, age, experience, "
                    f"form) rather than a specific matchup edge, and {pick} won via {route}.")
        if m_route == route or route == 'mixed':
            return ('Right for the right reasons',
                    f"The model expected {pick} to have the {m_route} edge, and that is how the fight was won ({route}).")
        return ('Right winner, different route',
                f"The model expected a {m_route} edge for {pick}, but the fight was actually won by {route}.")
    if t in ('Coin-flip decision', 'Contested decision'):
        return ('Wrong, but the result was razor-close',
                f"The in-fight stats only gave {winner} a {sup:.0%} case for the decision. The model's pick was "
                f"arguably as deserving as the official winner.")
    if t in ('Comeback finish', 'Quick finish'):
        return ('Wrong on a fight-changing moment',
                f"{winner} won with a {t.lower()} — a single moment that pre-fight averages cannot see coming.")
    if conf < 0.55:
        return ('Wrong on a toss-up', f"The model saw this as close to 50/50 and leaned the wrong way.")
    return ('Wrong: the model misread the matchup',
            f"The model's main reasons pointed to {pick}, but {winner} won a {t.lower()} via {route} "
            f"(stats support {sup:.0%}), so this was a genuine miss rather than bad luck.")


def fmt_factor_list(expl, name, is_a, n=4):
    """Top factors favouring `name`, showing that fighter's value first."""
    rows = expl[expl['favours'] == name].head(n)
    if rows.empty:
        return '_nothing significant_'
    def vals(r):
        mine, theirs = (r['value_a'], r['value_b']) if is_a else (r['value_b'], r['value_a'])
        return f"{J.format_value(r['feature'], mine)} vs {J.format_value(r['feature'], theirs)}"
    return '; '.join(f"{r['factor']} ({vals(r)}, ≈{abs(r['push_pts']):.1f} pts)" for _, r in rows.iterrows())


def run_spotlight(bouts, feats, classified, targets):
    results = []
    feats_by_url = feats.set_index('fight_url')
    cls_by_url = classified.set_index('fight_url')
    dates = sorted(targets['date'].unique())
    t0 = time.time()
    for i, d in enumerate(dates, 1):
        train = feats[feats['date'] < d]
        model = J.fit('blend', train)
        day = targets[targets['date'] == d]
        for _, b in day.iterrows():
            if b['fight_url'] not in feats_by_url.index:
                continue
            row = feats_by_url.loc[b['fight_url']]
            fa, fb = row['fighter_a'], row['fighter_b']
            p_a = float(J.predict_sym(model, row.to_frame().T.astype({c: float for c in FEATURE_COLUMNS}))[0])
            expl = J.explain(model, row, fa, fb, prob_a=p_a)
            pick = fa if p_a >= 0.5 else fb
            conf = max(p_a, 1 - p_a)
            fight = cls_by_url.loc[b['fight_url']]
            correct = pick == fight['winner']
            m_route, _ = model_route(expl, pick)
            verdict, verdict_text = reasoning_verdict(pick, correct, conf, m_route, fight)
            why_w, why_l = W.why_won_and_lost(fight)
            results.append({
                'date': d, 'event': b['event'], 'fighter_a': fa, 'fighter_b': fb,
                'weight_class': b['weight_class'], 'winner': fight['winner'],
                'method': fight['method'], 'end_round': fight['end_round'], 'end_time': fight['end_time'],
                'prob_a': p_a, 'pick': pick, 'confidence': conf, 'correct': correct,
                'training_fights': len(train), 'win_type': fight['win_type'], 'win_route': fight['win_route'],
                'stats_support_winner': fight['stats_support_winner'], 'model_route': m_route,
                'verdict': verdict, 'verdict_text': verdict_text, 'why_winner': why_w, 'why_loser': why_l,
                'factors_a': fmt_factor_list(expl, fa, True), 'factors_b': fmt_factor_list(expl, fb, False),
                'statline_a': W.describe_fighter(fight, 'a'), 'statline_b': W.describe_fighter(fight, 'b'),
            })
        print(f"    [{i}/{len(dates)}] {pd.Timestamp(d):%Y-%m-%d}: {len(day)} fight(s) "
              f"(trained on {len(train):,} earlier fights, {time.time() - t0:.0f}s)")
    return pd.DataFrame(results)


def bulk_breakdown(classified):
    """Walk-forward predictions for every fight since 2012, split by how the fight was won."""
    path = os.path.join(REPORT_DIR, 'walk_forward_predictions.csv')
    if not os.path.exists(path):
        return None, None
    wf = pd.read_csv(path, parse_dates=['date'])
    m = wf.merge(classified[['fight_url', 'win_type', 'win_route', 'stats_support_winner']], on='fight_url')
    m['correct'] = (m['p_blend'] >= 0.5) == (m['label'] == 1)
    m['confidence'] = np.maximum(m['p_blend'], 1 - m['p_blend'])
    by_type = m.groupby('win_type').agg(fights=('correct', 'size'), model_accuracy=('correct', 'mean'),
                                        avg_confidence=('confidence', 'mean')).sort_values('fights', ascending=False)
    m['conf_band'] = pd.cut(m['confidence'], [0.5, 0.55, 0.6, 0.65, 0.7, 1.0],
                            labels=['50-55%', '55-60%', '60-65%', '65-70%', '70%+'], include_lowest=True)
    by_conf = m.groupby('conf_band', observed=True).agg(fights=('correct', 'size'),
                                                        model_accuracy=('correct', 'mean'))
    return by_type, by_conf


def md_table(df, pct_cols=(), dec_cols=()):
    df = df.copy()
    for c in pct_cols:
        df[c] = df[c].map(lambda v: f'{v:.1%}')
    for c in dec_cols:
        df[c] = df[c].map(lambda v: f'{v:.2f}')
    cols = list(df.columns)
    lines = ['| ' + ' | '.join(cols) + ' |', '|' + '---|' * len(cols)]
    for _, r in df.iterrows():
        lines.append('| ' + ' | '.join(str(r[c]) for c in cols) + ' |')
    return '\n'.join(lines)


def write_report(spot, rates, facts, types, by_type, by_conf, path):
    L = []
    L.append('# Backtest report: past fights, predicted honestly and explained\n')
    L.append(f'_Generated {pd.Timestamp.now():%Y-%m-%d %H:%M}. Every spotlight prediction below was made by a '
             f'model trained only on fights before that date, using stats as they stood that morning._\n')

    n, c = len(spot), int(spot['correct'].sum())
    L.append('## Spotlight scorecard\n')
    L.append(f'**{c} of {n} correct ({c / max(n, 1):.0%}).**\n')
    L.append(md_table(spot['verdict'].value_counts().rename_axis('verdict').reset_index(name='fights')))
    L.append('')

    L.append('\n## What actually wins a UFC fight\n')
    L.append('A judge model was trained on every UFC decision with full stats. Its weights, expressed as '
             '"how many significant strikes is this worth on the scorecards":\n')
    r = rates[['stat', 'worth_in_sig_strikes']].copy()
    r['worth_in_sig_strikes'] = r['worth_in_sig_strikes'].map(lambda v: f'{v:.1f}')
    L.append(md_table(r))
    L.append('\n_Head strikes are counted on top of the significant-strike total, so a landed head strike is worth '
             'about 1.7 body or leg strikes._\n')
    L.append(md_table(facts, pct_cols=['share_of_decisions', 'loser_had_more']))
    L.append('\nHow all UFC wins break down:\n')
    t = types.copy(); t.columns = ['win type', 'share of all wins']
    L.append(md_table(t, pct_cols=['share of all wins']))

    if by_type is not None:
        L.append('\n## Where the model is reliable (every fight since 2012, walk-forward)\n')
        L.append(md_table(by_type.reset_index(), pct_cols=['model_accuracy', 'avg_confidence']))
        L.append('\nBy model confidence:\n')
        L.append(md_table(by_conf.reset_index(), pct_cols=['model_accuracy']))

    L.append('\n## Fight by fight\n')
    for _, s in spot.sort_values('date').iterrows():
        mark = '✅' if s['correct'] else '❌'
        L.append(f"### {pd.Timestamp(s['date']):%Y-%m-%d} · {s['fighter_a']} vs {s['fighter_b']}")
        L.append(f"_{s['event']} · {s['weight_class']}_\n")
        rnd = f"R{int(s['end_round'])} {s['end_time']}" if pd.notna(s['end_round']) else ''
        L.append(f"- **Result:** {s['winner']} by {s['method']} ({rnd}). "
                 f"**Win type:** {s['win_type']} via {s['win_route']}; stats support for the winner "
                 f"{s['stats_support_winner']:.0%}.")
        L.append(f"- **Model before the fight** (trained on {s['training_fights']:,} earlier fights): "
                 f"{s['fighter_a']} {s['prob_a']:.0%} / {s['fighter_b']} {1 - s['prob_a']:.0%}. "
                 f"Picked {s['pick']} {mark}")
        L.append(f"- **Pushing toward {s['fighter_a']}** (their number first): {s['factors_a']}")
        L.append(f"- **Pushing toward {s['fighter_b']}** (their number first): {s['factors_b']}")
        L.append(f"- **In the cage, {s['fighter_a']}:** {s['statline_a']}")
        L.append(f"- **In the cage, {s['fighter_b']}:** {s['statline_b']}")
        L.append(f"- **Why {s['winner']} won:** {s['why_winner']}")
        loser = s['fighter_b'] if s['winner'] == s['fighter_a'] else s['fighter_a']
        L.append(f"- **{loser}:** {s['why_loser']}")
        L.append(f"- **Verdict: {s['verdict']}.** {s['verdict_text']}\n")

    with open(path, 'w') as fh:
        fh.write('\n'.join(L))


def main(fighters=None, since=DEFAULT_SINCE):
    fighters = fighters or DEFAULT_FIGHTERS
    bouts = pd.read_csv(os.path.join(PROCESSED_DIR, 'bouts.csv'), parse_dates=['date'], low_memory=False)
    feats = pd.read_csv(os.path.join(PROCESSED_DIR, 'features.csv'), parse_dates=['date'], low_memory=False)
    print('  Grading every UFC win (win anatomy)...')
    classified, judge = W.classify_wins(bouts)
    rates = W.exchange_rates(judge)
    facts, types = W.summary_tables(classified)

    targets = pick_targets(bouts, fighters, pd.Timestamp(since))
    print(f"  Spotlight: {len(targets)} fights ({', '.join(fighters)} + main events/title fights since {since})")
    spot = run_spotlight(bouts, feats, classified, targets)
    by_type, by_conf = bulk_breakdown(classified)

    os.makedirs(REPORT_DIR, exist_ok=True)
    spot.to_csv(os.path.join(REPORT_DIR, 'backtest_fights.csv'), index=False)
    report = os.path.join(REPORT_DIR, 'backtest_report.md')
    write_report(spot, rates, facts, types, by_type, by_conf, report)

    c = int(spot['correct'].sum())
    print(f"\n  Spotlight record: {c}/{len(spot)} ({c / max(len(spot), 1):.1%})")
    print(spot['verdict'].value_counts().to_string())
    if by_type is not None:
        print('\n  Walk-forward accuracy by how the fight was won:')
        print(by_type.round(3).to_string())
    print(f"\n  Full write-up: {os.path.relpath(report, ROOT)}")
    return spot


if __name__ == '__main__':
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--fighter', action='append', help='include every UFC fight of this fighter (repeatable)')
    ap.add_argument('--since', default=DEFAULT_SINCE, help='include main events and title fights since this date')
    a = ap.parse_args()
    main(fighters=a.fighter, since=a.since)
