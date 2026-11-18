#!/usr/bin/env python3
"""
UFC ADVERSARIAL JUDGE - POINT-IN-TIME FEATURE ENGINE
====================================================
Replays every UFC fight in date order. Before each fight it freezes a snapshot
of both fighters' stats *as they were that morning*; only after recording the
snapshot does it add that fight's result and stats to their history.

This is the single most important accuracy fix in the project. A model can only
be trusted on a past fight if it was shown exactly what a fan or bettor could
have known before that fight. Anything else is the model "seeing the future".

Outputs
-------
  data/processed/features.csv          one row per decided fight, fighter A's view,
                                       with pre-fight stats for both fighters and the
                                       A-minus-B difference features used by the model
  data/processed/fighter_snapshot.csv  every fighter's stats as of today, used to
                                       predict fights that have not happened yet

How each stat is defined (matches UFCStats' own definitions)
------------------------------------------------------------
  SLpM      significant strikes landed per minute of UFC fight time
  SApM      significant strikes absorbed per minute
  Str. Acc  significant strikes landed / attempted
  Str. Def  share of the opponent's significant strike attempts that missed
  TD Avg    takedowns landed per 15 minutes
  TD Acc    takedowns landed / attempted
  TD Def    share of the opponent's takedown attempts that failed
  Sub Avg   submission attempts per 15 minutes

Extra signals this engine adds
------------------------------
  Elo rating           a chess-style strength rating; beating strong opponents
                       raises it more than beating weak ones (strength of schedule)
  Opponent Elo average the typical quality of everyone a fighter has faced
  Recent form          the same striking numbers, weighted toward the last ~3 fights
  Durability           knockdowns absorbed per 15 min and number of KO/TKO losses
  Control share        share of grappling control time a fighter owns
  Layoff               days since the fighter's previous UFC fight

Small samples are pulled toward the UFC average ("shrinkage"). A debut fighter
who landed 9 strikes in a 1-minute win does not get credited with 9.0 SLpM.
"""

import math
import os
import sys
from collections import defaultdict, deque

import numpy as np
import pandas as pd

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROCESSED_DIR = os.path.join(ROOT, 'data', 'processed')

# ─── Tunable constants ───────────────────────────────────────────────────────
ELO_START = 1500.0
ELO_K = 64.0              # how fast ratings move after each fight
ELO_FINISH_BONUS = 1.2    # finishes move ratings a bit more than decisions
EW_DECAY = 0.5 ** (1 / 3)  # recent-form weighting: a fight 3 bouts ago counts half
PRIOR_MINUTES = 15.0      # shrink per-minute rates as if 15 avg minutes were already seen
PRIOR_STRIKE_ATT = 60.0   # shrink accuracy/defense as if 60 avg attempts were already seen
PRIOR_TD_ATT = 6.0        # shrink takedown accuracy/defense as if 6 avg attempts were seen
PRIOR_CTRL_SEC = 300.0    # shrink control share toward 50% with 5 minutes of prior time
PRIME_AGE = 32.0          # age after which decline is modeled

# Per-fighter values captured before each fight (both corners get these)
FIGHTER_FIELDS = [
    'elo', 'opp_elo_avg', 'slpm', 'sapm', 'str_acc', 'str_def', 'strike_margin',
    'td_avg', 'td_acc', 'td_def', 'sub_avg', 'ctrl_share', 'kd_avg', 'kd_absorbed_avg',
    'recent_margin', 'recent_ctrl_share', 'recent_win', 'recent_opp_elo', 'recent_perf',
    'ufc_fights', 'ufc_minutes',
    'win_pct', 'streak', 'finish_rate', 'ko_losses', 'finished_losses', 'layoff_days',
    'title_fights', 'age', 'age_decline', 'height_cm', 'reach_cm',
]

# Model inputs: fighter A minus fighter B for every field above
FEATURE_COLUMNS = [f'{f}_diff' for f in FIGHTER_FIELDS]

FRIENDLY_NAMES = {
    'elo_diff': 'Elo rating (quality of wins)',
    'opp_elo_avg_diff': 'Strength of schedule (avg opponent Elo)',
    'slpm_diff': 'Sig. strikes landed / min',
    'sapm_diff': 'Sig. strikes absorbed / min',
    'str_acc_diff': 'Striking accuracy',
    'str_def_diff': 'Striking defense',
    'strike_margin_diff': 'Net striking margin (landed - absorbed / min)',
    'td_avg_diff': 'Takedowns landed / 15 min',
    'td_acc_diff': 'Takedown accuracy',
    'td_def_diff': 'Takedown defense',
    'sub_avg_diff': 'Submission attempts / 15 min',
    'ctrl_share_diff': 'Grappling control share',
    'kd_avg_diff': 'Knockdown power (KD / 15 min)',
    'kd_absorbed_avg_diff': 'Chin risk (KD absorbed / 15 min)',
    'recent_margin_diff': 'Recent striking form (last ~3 fights)',
    'recent_ctrl_share_diff': 'Recent grappling control',
    'recent_win_diff': 'Recent results (last ~3 fights)',
    'recent_opp_elo_diff': 'Recent strength of schedule (last ~3 opponents)',
    'recent_perf_diff': 'Recent results vs expectation (opponent-adjusted)',
    'ufc_fights_diff': 'UFC experience (fights)',
    'ufc_minutes_diff': 'UFC cage time (minutes)',
    'win_pct_diff': 'UFC win percentage',
    'streak_diff': 'Win / loss streak',
    'finish_rate_diff': 'Finishing rate',
    'ko_losses_diff': 'KO/TKO losses suffered',
    'finished_losses_diff': 'Times finished',
    'layoff_days_diff': 'Days since last fight',
    'title_fights_diff': 'Title fight experience',
    'age_diff': 'Age',
    'age_decline_diff': 'Age past 32 (decline years)',
    'height_cm_diff': 'Height',
    'reach_cm_diff': 'Reach',
}

# Which part of the game each feature describes (used to compare the model's
# reasoning with how a fight was actually won)
FEATURE_GROUP = {
    'elo_diff': 'quality', 'opp_elo_avg_diff': 'quality', 'win_pct_diff': 'quality',
    'streak_diff': 'momentum', 'recent_win_diff': 'momentum', 'recent_opp_elo_diff': 'quality',
    'recent_perf_diff': 'quality', 'recent_margin_diff': 'striking',
    'slpm_diff': 'striking', 'sapm_diff': 'striking', 'str_acc_diff': 'striking',
    'str_def_diff': 'striking', 'strike_margin_diff': 'striking', 'kd_avg_diff': 'power',
    'kd_absorbed_avg_diff': 'durability', 'ko_losses_diff': 'durability',
    'finished_losses_diff': 'durability', 'finish_rate_diff': 'power',
    'td_avg_diff': 'grappling', 'td_acc_diff': 'grappling', 'td_def_diff': 'grappling',
    'sub_avg_diff': 'grappling', 'ctrl_share_diff': 'grappling', 'recent_ctrl_share_diff': 'grappling',
    'ufc_fights_diff': 'experience', 'ufc_minutes_diff': 'experience', 'title_fights_diff': 'experience',
    'layoff_days_diff': 'activity', 'age_diff': 'age', 'age_decline_diff': 'age',
    'height_cm_diff': 'physical', 'reach_cm_diff': 'physical',
}


def _new_state():
    return {
        'fights': 0, 'wins': 0, 'losses': 0, 'streak': 0, 'sec': 0.0,
        'sig_l': 0.0, 'sig_a': 0.0, 'opp_sig_l': 0.0, 'opp_sig_a': 0.0,
        'td_l': 0.0, 'td_a': 0.0, 'opp_td_l': 0.0, 'opp_td_a': 0.0,
        'sub': 0.0, 'kd': 0.0, 'opp_kd': 0.0, 'ctrl': 0.0, 'opp_ctrl': 0.0,
        'ew_sec': 0.0, 'ew_sig_l': 0.0, 'ew_opp_sig_l': 0.0, 'ew_ctrl': 0.0, 'ew_opp_ctrl': 0.0,
        'ew_win': 0.0, 'ew_n': 0.0, 'ew_opp_elo': 0.0, 'ew_perf': 0.0,
        'finish_wins': 0, 'ko_losses': 0, 'finished_losses': 0, 'title_fights': 0,
        'elo': ELO_START, 'opp_elo_sum': 0.0, 'last_date': None, 'name': None,
    }


class LeagueAverages:
    """Running UFC-wide averages, also point-in-time, used as shrinkage targets."""

    def __init__(self):
        self.sec = self.sig_l = self.sig_a = self.td_l = self.td_a = self.sub = self.kd = 0.0
        # sensible starting values before any fights are seen
        self.sec, self.sig_l, self.sig_a, self.td_l, self.td_a, self.sub, self.kd = \
            600.0, 30.0, 70.0, 1.5, 4.0, 0.5, 0.2

    def add(self, sec, sig_l, sig_a, td_l, td_a, sub, kd):
        self.sec += sec; self.sig_l += sig_l; self.sig_a += sig_a
        self.td_l += td_l; self.td_a += td_a; self.sub += sub; self.kd += kd

    @property
    def per_min(self):
        mins = self.sec / 60.0
        return {'sig': self.sig_l / mins, 'td15': self.td_l / mins * 15,
                'sub15': self.sub / mins * 15, 'kd15': self.kd / mins * 15,
                'acc': self.sig_l / self.sig_a, 'td_acc': self.td_l / self.td_a}


def fighter_view(st, league, profile, as_of):
    """Turn a fighter's running totals into the stat line the model sees."""
    lg = league.per_min
    mins = st['sec'] / 60.0
    pm, ps = PRIOR_MINUTES, PRIOR_STRIKE_ATT

    slpm = (st['sig_l'] + lg['sig'] * pm) / (mins + pm)
    sapm = (st['opp_sig_l'] + lg['sig'] * pm) / (mins + pm)
    str_acc = (st['sig_l'] + lg['acc'] * ps) / (st['sig_a'] + ps)
    str_def = 1 - (st['opp_sig_l'] + lg['acc'] * ps) / (st['opp_sig_a'] + ps)
    td_avg = (st['td_l'] + lg['td15'] / 15 * pm) / (mins + pm) * 15
    td_acc = (st['td_l'] + lg['td_acc'] * PRIOR_TD_ATT) / (st['td_a'] + PRIOR_TD_ATT)
    td_def = 1 - (st['opp_td_l'] + lg['td_acc'] * PRIOR_TD_ATT) / (st['opp_td_a'] + PRIOR_TD_ATT)
    sub_avg = (st['sub'] + lg['sub15'] / 15 * pm) / (mins + pm) * 15
    kd_avg = (st['kd'] + lg['kd15'] / 15 * pm) / (mins + pm) * 15
    kd_abs = (st['opp_kd'] + lg['kd15'] / 15 * pm) / (mins + pm) * 15
    ctrl_share = (st['ctrl'] + PRIOR_CTRL_SEC / 2) / (st['ctrl'] + st['opp_ctrl'] + PRIOR_CTRL_SEC)

    ew_mins = st['ew_sec'] / 60.0
    recent_margin = (st['ew_sig_l'] - st['ew_opp_sig_l']) / (ew_mins + pm)
    recent_ctrl = (st['ew_ctrl'] + PRIOR_CTRL_SEC / 2) / (st['ew_ctrl'] + st['ew_opp_ctrl'] + PRIOR_CTRL_SEC)
    recent_win = (st['ew_win'] + 0.5) / (st['ew_n'] + 1.0)
    # who they have fought lately, and how they did versus what Elo expected against them
    recent_opp_elo = (st['ew_opp_elo'] + ELO_START) / (st['ew_n'] + 1.0)
    recent_perf = st['ew_perf'] / (st['ew_n'] + 1.0)

    dob = profile.get('dob') if profile else None
    age = (as_of - dob).days / 365.25 if dob is not None and pd.notna(dob) else np.nan
    layoff = (as_of - st['last_date']).days if st['last_date'] is not None else np.nan

    return {
        'elo': st['elo'],
        'opp_elo_avg': (st['opp_elo_sum'] + ELO_START * 2) / (st['fights'] + 2),
        'slpm': slpm, 'sapm': sapm, 'str_acc': str_acc, 'str_def': str_def,
        'strike_margin': slpm - sapm, 'td_avg': td_avg, 'td_acc': td_acc, 'td_def': td_def,
        'sub_avg': sub_avg, 'ctrl_share': ctrl_share, 'kd_avg': kd_avg, 'kd_absorbed_avg': kd_abs,
        'recent_margin': recent_margin, 'recent_ctrl_share': recent_ctrl, 'recent_win': recent_win,
        'recent_opp_elo': recent_opp_elo, 'recent_perf': recent_perf,
        'ufc_fights': st['fights'], 'ufc_minutes': mins,
        'win_pct': (st['wins'] + 1) / (st['wins'] + st['losses'] + 2),
        'streak': st['streak'],
        'finish_rate': (st['finish_wins'] + 0.3) / (st['fights'] + 1),
        'ko_losses': st['ko_losses'], 'finished_losses': st['finished_losses'],
        'layoff_days': min(layoff, 1500) if pd.notna(layoff) else np.nan,
        'title_fights': st['title_fights'],
        'age': age, 'age_decline': max(0.0, age - PRIME_AGE) if pd.notna(age) else np.nan,
        'height_cm': profile.get('height_cm', np.nan) if profile else np.nan,
        'reach_cm': profile.get('reach_cm', np.nan) if profile else np.nan,
        # raw (unshrunk) record kept for display
        'ufc_wins': st['wins'], 'ufc_losses': st['losses'],
    }


def _is_finish(method):
    m = str(method)
    return ('KO' in m) or ('Submission' in m) or ("Doctor" in m)


def _is_ko(method):
    m = str(method)
    return ('KO' in m) or ("Doctor" in m)


def _val(x):
    return 0.0 if pd.isna(x) else float(x)


def update_after_fight(st, opp, row, side, opp_elo_before):
    """Add one fight's stats and result to a fighter's running totals."""
    o = 'b' if side == 'a' else 'a'
    if row['has_stats'] and pd.notna(row['fight_sec']):
        sec = float(row['fight_sec'])
        sig_l, opp_sig_l = _val(row[f'{side}_sig_l']), _val(row[f'{o}_sig_l'])
        ctrl, opp_ctrl = _val(row[f'{side}_ctrl']), _val(row[f'{o}_ctrl'])
        st['sec'] += sec
        st['sig_l'] += sig_l; st['sig_a'] += _val(row[f'{side}_sig_a'])
        st['opp_sig_l'] += opp_sig_l; st['opp_sig_a'] += _val(row[f'{o}_sig_a'])
        st['td_l'] += _val(row[f'{side}_td_l']); st['td_a'] += _val(row[f'{side}_td_a'])
        st['opp_td_l'] += _val(row[f'{o}_td_l']); st['opp_td_a'] += _val(row[f'{o}_td_a'])
        st['sub'] += _val(row[f'{side}_sub'])
        st['kd'] += _val(row[f'{side}_kd']); st['opp_kd'] += _val(row[f'{o}_kd'])
        st['ctrl'] += ctrl; st['opp_ctrl'] += opp_ctrl
        for k in ('ew_sec', 'ew_sig_l', 'ew_opp_sig_l', 'ew_ctrl', 'ew_opp_ctrl'):
            st[k] *= EW_DECAY
        st['ew_sec'] += sec; st['ew_sig_l'] += sig_l; st['ew_opp_sig_l'] += opp_sig_l
        st['ew_ctrl'] += ctrl; st['ew_opp_ctrl'] += opp_ctrl

    result = row['result']
    won = (result == 'A' and side == 'a') or (result == 'B' and side == 'b')
    lost = (result == 'A' and side == 'b') or (result == 'B' and side == 'a')
    if result in ('A', 'B', 'draw'):
        st['fights'] += 1
        st['opp_elo_sum'] += opp_elo_before
        st['ew_win'] = st['ew_win'] * EW_DECAY + (1.0 if won else 0.5 if result == 'draw' else 0.0)
        st['ew_n'] = st['ew_n'] * EW_DECAY + 1.0
        expected = 1.0 / (1.0 + 10 ** ((opp_elo_before - st['elo']) / 400.0))  # st['elo'] is still pre-fight
        score = 1.0 if won else 0.5 if result == 'draw' else 0.0
        st['ew_opp_elo'] = st['ew_opp_elo'] * EW_DECAY + opp_elo_before
        st['ew_perf'] = st['ew_perf'] * EW_DECAY + (score - expected)
    if won:
        st['wins'] += 1
        st['streak'] = max(1, st['streak'] + 1)
        if _is_finish(row['method']):
            st['finish_wins'] += 1
    elif lost:
        st['losses'] += 1
        st['streak'] = min(-1, st['streak'] - 1)
        if _is_ko(row['method']):
            st['ko_losses'] += 1
        if _is_finish(row['method']):
            st['finished_losses'] += 1
    elif result == 'draw':
        st['streak'] = 0
    if row['title_fight']:
        st['title_fights'] += 1
    st['last_date'] = row['date']


def elo_update(ea, eb, result, method):
    """Return new (elo_a, elo_b) after a fight."""
    if result not in ('A', 'B', 'draw'):
        return ea, eb
    expected_a = 1.0 / (1.0 + 10 ** ((eb - ea) / 400.0))
    score_a = 1.0 if result == 'A' else 0.0 if result == 'B' else 0.5
    k = ELO_K * (ELO_FINISH_BONUS if _is_finish(method) and result != 'draw' else 1.0)
    delta = k * (score_a - expected_a)
    return ea + delta, eb - delta


def load_inputs(processed_dir=PROCESSED_DIR):
    bouts = pd.read_csv(os.path.join(processed_dir, 'bouts.csv'), parse_dates=['date'], low_memory=False)
    fighters = pd.read_csv(os.path.join(processed_dir, 'fighters.csv'), parse_dates=['dob'])
    profiles = fighters.set_index('fighter_url').to_dict('index')
    return bouts, fighters, profiles


def replay(bouts, profiles, until=None):
    """
    Walk through all fights in order. Returns (feature rows, final fighter states, league).
    If `until` is given, stops before fights on or after that date.
    """
    states = defaultdict(_new_state)
    league = LeagueAverages()
    rows = []

    for _, row in bouts.iterrows():
        if until is not None and row['date'] >= until:
            break
        ida, idb = row['fighter_a_id'], row['fighter_b_id']
        sa, sb = states[ida], states[idb]
        sa['name'], sb['name'] = row['fighter_a'], row['fighter_b']
        pa, pb = profiles.get(ida), profiles.get(idb)

        if row['result'] in ('A', 'B'):
            va = fighter_view(sa, league, pa, row['date'])
            vb = fighter_view(sb, league, pb, row['date'])
            rec = {
                'fight_url': row['fight_url'], 'date': row['date'], 'event': row['event'],
                'fighter_a': row['fighter_a'], 'fighter_b': row['fighter_b'],
                'fighter_a_id': ida, 'fighter_b_id': idb,
                'winner': row['winner'], 'label': 1 if row['result'] == 'A' else 0,
                'method': row['method'], 'end_round': row['end_round'],
                'weight_class': row['weight_class'], 'title_fight': row['title_fight'],
                'women': row['women'],
            }
            for f in FIGHTER_FIELDS:
                rec[f'a_{f}'] = va[f]
                rec[f'b_{f}'] = vb[f]
                rec[f'{f}_diff'] = va[f] - vb[f]
            rows.append(rec)

        ea_before, eb_before = sa['elo'], sb['elo']
        update_after_fight(sa, sb, row, 'a', eb_before)
        update_after_fight(sb, sa, row, 'b', ea_before)
        sa['elo'], sb['elo'] = elo_update(ea_before, eb_before, row['result'], row['method'])
        if row['has_stats'] and pd.notna(row['fight_sec']):
            league.add(row['fight_sec'] * 2,
                       _val(row['a_sig_l']) + _val(row['b_sig_l']),
                       _val(row['a_sig_a']) + _val(row['b_sig_a']),
                       _val(row['a_td_l']) + _val(row['b_td_l']),
                       _val(row['a_td_a']) + _val(row['b_td_a']),
                       _val(row['a_sub']) + _val(row['b_sub']),
                       _val(row['a_kd']) + _val(row['b_kd']))

    return pd.DataFrame(rows), states, league


def snapshot(states, league, profiles, as_of):
    """Every fighter's stat line as of `as_of` (for predicting upcoming fights)."""
    out = []
    for fid, st in states.items():
        view = fighter_view(st, league, profiles.get(fid), as_of)
        prof = profiles.get(fid) or {}
        mins = st['sec'] / 60.0
        out.append({
            'fighter_id': fid, 'name': st['name'], 'nickname': prof.get('nickname'),
            'weight_lbs': prof.get('weight_lbs'), 'stance': prof.get('stance'), 'dob': prof.get('dob'),
            'last_fight': st['last_date'],
            # raw career numbers, same definitions as the UFCStats profile page
            'raw_slpm': st['sig_l'] / mins if mins else np.nan,
            'raw_sapm': st['opp_sig_l'] / mins if mins else np.nan,
            'raw_str_acc': st['sig_l'] / st['sig_a'] if st['sig_a'] else np.nan,
            'raw_str_def': 1 - st['opp_sig_l'] / st['opp_sig_a'] if st['opp_sig_a'] else np.nan,
            'raw_td_avg': st['td_l'] / mins * 15 if mins else np.nan,
            'raw_td_acc': st['td_l'] / st['td_a'] if st['td_a'] else np.nan,
            'raw_td_def': 1 - st['opp_td_l'] / st['opp_td_a'] if st['opp_td_a'] else np.nan,
            'raw_sub_avg': st['sub'] / mins * 15 if mins else np.nan,
            **view,
        })
    return pd.DataFrame(out)


def build_features(processed_dir=PROCESSED_DIR, verbose=True):
    bouts, fighters, profiles = load_inputs(processed_dir)
    feats, states, league = replay(bouts, profiles)
    today = pd.Timestamp.today().normalize()
    snap = snapshot(states, league, profiles, today)
    feats.to_csv(os.path.join(processed_dir, 'features.csv'), index=False)
    snap.to_csv(os.path.join(processed_dir, 'fighter_snapshot.csv'), index=False)
    if verbose:
        print(f"  features.csv         : {len(feats):,} decided fights with pre-fight features")
        print(f"  fighter_snapshot.csv : {len(snap):,} fighters' current stat lines (as of {today:%Y-%m-%d})")
    return feats, snap


def validate_against_official(official_path, processed_dir=PROCESSED_DIR, as_of='2026-03-13'):
    """
    Accuracy check: rebuild every fighter's career numbers from fight-by-fight data
    as of the date the old profile scrape was taken, then compare with the numbers
    UFCStats printed on their profile pages at that time.
    """
    bouts, fighters, profiles = load_inputs(processed_dir)
    _, states, league = replay(bouts, profiles, until=pd.Timestamp(as_of))
    snap = snapshot(states, league, profiles, pd.Timestamp(as_of))
    off = pd.read_csv(official_path)
    off = off.rename(columns={'Fighter_URL': 'fighter_id'})

    def pct(s):
        return pd.to_numeric(s.astype(str).str.replace('%', ''), errors='coerce') / 100

    off['off_slpm'] = pd.to_numeric(off['SLpM'], errors='coerce')
    off['off_sapm'] = pd.to_numeric(off['SApM'], errors='coerce')
    off['off_str_acc'] = pct(off['Str_Acc'])
    off['off_str_def'] = pct(off['Str_Def'])
    off['off_td_avg'] = pd.to_numeric(off['TD_Avg'], errors='coerce')
    off['off_td_def'] = pct(off['TD_Def'])
    m = snap.merge(off, on='fighter_id', how='inner')
    m = m[(m['ufc_minutes'] > 5) & (m['off_slpm'] > 0)]
    report = []
    for ours, theirs, tol in [('raw_slpm', 'off_slpm', 0.06), ('raw_sapm', 'off_sapm', 0.06),
                              ('raw_str_acc', 'off_str_acc', 0.011), ('raw_str_def', 'off_str_def', 0.011),
                              ('raw_td_avg', 'off_td_avg', 0.06), ('raw_td_def', 'off_td_def', 0.011)]:
        d = (m[ours] - m[theirs]).abs().dropna()
        report.append({'stat': theirs.replace('off_', ''), 'fighters_compared': len(d),
                       'mean_abs_error': round(d.mean(), 4),
                       'within_rounding': f"{(d <= tol).mean():.1%}"})
    return pd.DataFrame(report)


if __name__ == '__main__':
    build_features()
    official = os.path.join(ROOT, 'data', 'raw', 'ufc_fighters_final.csv')
    if os.path.exists(official) and '--validate' in sys.argv:
        print(validate_against_official(official).to_string(index=False))
