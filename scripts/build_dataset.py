#!/usr/bin/env python3
"""
UFC ADVERSARIAL JUDGE - DATASET BUILDER
=======================================
Turns the raw UFCStats mirror files (downloaded by update_data.py into
data/raw/ufcstats/) into two clean, analysis-ready tables:

  data/processed/bouts.csv     One row per UFC fight: date, both fighters, result,
                               method, fight time, and every in-fight stat for
                               both fighters (strikes, knockdowns, takedowns,
                               control time, strike targets and positions).

  data/processed/fighters.csv  One row per fighter profile: height, reach,
                               weight, stance, date of birth, UFCStats URL.

Why this replaces the old cleaning step
---------------------------------------
The old pipeline used each fighter's *career summary* line from their UFCStats
profile (SLpM, Str. Acc, ...). Those numbers include every fight the fighter has
ever had, so attaching them to a fight in 2019 leaks what happened in 2020-2026.
Here we keep the raw fight-by-fight numbers instead, so features.py can rebuild
any fighter's stats exactly as they stood on any date.
"""

import os
import re
import sys

import numpy as np
import pandas as pd

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW_DIR = os.path.join(ROOT, 'data', 'raw', 'ufcstats')
PROCESSED_DIR = os.path.join(ROOT, 'data', 'processed')

# Weight limit (lbs) for each division. Used to tell apart fighters who share a name.
WEIGHT_CLASS_LBS = [
    ("Women's Strawweight", 115), ("Women's Flyweight", 125), ("Women's Bantamweight", 135),
    ("Women's Featherweight", 145), ("Light Heavyweight", 205), ("Strawweight", 115),
    ("Flyweight", 125), ("Bantamweight", 135), ("Featherweight", 145), ("Lightweight", 155),
    ("Welterweight", 170), ("Middleweight", 185), ("Heavyweight", 265),
]

# In-fight stat columns that come as "X of Y" (landed of attempted)
PAIRED_STATS = {
    'SIG.STR.': 'sig', 'TOTAL STR.': 'tot', 'TD': 'td', 'HEAD': 'head', 'BODY': 'body',
    'LEG': 'leg', 'DISTANCE': 'dist', 'CLINCH': 'clinch', 'GROUND': 'ground',
}


# ─── Small parsers ───────────────────────────────────────────────────────────

def parse_of(value):
    """'41 of 65' -> (41, 65). Missing values -> (nan, nan)."""
    m = re.match(r'\s*(\d+)\s+of\s+(\d+)', str(value))
    return (int(m.group(1)), int(m.group(2))) if m else (np.nan, np.nan)


def parse_clock(value):
    """'4:32' -> 272 seconds. '--' or missing -> nan."""
    m = re.match(r'\s*(\d+):(\d+)', str(value))
    return int(m.group(1)) * 60 + int(m.group(2)) if m else np.nan


def height_to_cm(value):
    m = re.match(r"\s*(\d+)'\s*(\d+)", str(value))
    return round((int(m.group(1)) * 12 + int(m.group(2))) * 2.54, 1) if m else np.nan


def reach_to_cm(value):
    m = re.match(r'\s*([\d.]+)"', str(value))
    return round(float(m.group(1)) * 2.54, 1) if m else np.nan


def weight_to_lbs(value):
    m = re.match(r'\s*(\d+)', str(value))
    return float(m.group(1)) if m else np.nan


def division_lbs(weight_class):
    wc = str(weight_class)
    for name, lbs in WEIGHT_CLASS_LBS:
        if name in wc:
            return lbs
    return np.nan


def fight_seconds(end_round, end_time, time_format):
    """Total elapsed fight time. '3 Rnd (5-5-5)', round 3 at 2:10 -> 10 min + 130 s."""
    end_sec = parse_clock(end_time)
    if pd.isna(end_sec) or pd.isna(end_round):
        return np.nan
    lengths = [int(x) for x in re.findall(r'\d+', str(time_format).split('(')[-1])] \
        if '(' in str(time_format) else []
    completed = sum(lengths[:int(end_round) - 1]) * 60 if lengths else 0
    return completed + end_sec


def scheduled_rounds(time_format):
    m = re.match(r'\s*(\d+)\s+Rnd', str(time_format))
    return int(m.group(1)) if m else 1


# ─── Builders ────────────────────────────────────────────────────────────────

def load_raw(raw_dir=RAW_DIR):
    def read(name):
        df = pd.read_csv(os.path.join(raw_dir, f'{name}.csv'))
        for col in df.columns:
            if df[col].dtype == object or str(df[col].dtype).startswith('str'):
                df[col] = df[col].astype('string').str.strip()
        return df
    return {n: read(n) for n in ['ufc_event_details', 'ufc_fight_results',
                                 'ufc_fight_stats', 'ufc_fighter_tott', 'ufc_fighter_details']}


def build_fighters(raw):
    tott = raw['ufc_fighter_tott'].copy()
    det = raw['ufc_fighter_details'][['URL', 'NICKNAME']]
    tott = tott.merge(det, on='URL', how='left')
    fighters = pd.DataFrame({
        'name': tott['FIGHTER'],
        'nickname': tott['NICKNAME'],
        'height_cm': tott['HEIGHT'].map(height_to_cm),
        'reach_cm': tott['REACH'].map(reach_to_cm),
        'weight_lbs': tott['WEIGHT'].map(weight_to_lbs),
        'stance': tott['STANCE'].fillna('Unknown'),
        'dob': pd.to_datetime(tott['DOB'], format='%b %d, %Y', errors='coerce'),
        'fighter_url': tott['URL'],
    })
    return fighters.dropna(subset=['name']).drop_duplicates('fighter_url').reset_index(drop=True)


def aggregate_stats(stats):
    """Round-by-round rows -> one row per (event, bout, fighter) with fight totals."""
    s = stats.dropna(subset=['FIGHTER']).copy()
    out = pd.DataFrame({'EVENT': s['EVENT'], 'BOUT': s['BOUT'], 'FIGHTER': s['FIGHTER'],
                        'round_no': s['ROUND'].str.extract(r'(\d+)')[0].astype(float)})
    for col in ['KD', 'SUB.ATT', 'REV.']:
        out[col.lower().strip('.').replace('.', '_')] = pd.to_numeric(s[col], errors='coerce')
    for col, short in PAIRED_STATS.items():
        pairs = s[col].map(parse_of)
        out[f'{short}_l'] = [p[0] for p in pairs]
        out[f'{short}_a'] = [p[1] for p in pairs]
    out['ctrl'] = s['CTRL'].map(parse_clock)
    out = out.rename(columns={'sub_att': 'sub', 'rev': 'rev'})

    # Per-round sig strikes, to count "rounds won on the feet" later
    per_round = out[['EVENT', 'BOUT', 'FIGHTER', 'round_no', 'sig_l']].copy()

    value_cols = [c for c in out.columns if c not in ('EVENT', 'BOUT', 'FIGHTER', 'round_no')]
    totals = out.groupby(['EVENT', 'BOUT', 'FIGHTER'], sort=False)[value_cols].sum(min_count=1).reset_index()
    return totals, per_round


def resolve_fighter_ids(bouts, fighters):
    """Map each bout corner to a fighter profile URL; break name ties by weight class."""
    by_name = fighters.groupby('name')
    ids = {'a': [], 'b': []}
    for _, row in bouts.iterrows():
        div = division_lbs(row['weight_class'])
        for side in ('a', 'b'):
            name = row[f'fighter_{side}']
            if name not in by_name.groups:
                ids[side].append(f'name::{name}')
                continue
            cands = fighters.loc[by_name.groups[name]]
            if len(cands) == 1 or pd.isna(div):
                ids[side].append(cands.iloc[0]['fighter_url'])
            else:
                gap = (cands['weight_lbs'] - div).abs().fillna(999)
                ids[side].append(cands.loc[gap.idxmin(), 'fighter_url'])
    bouts['fighter_a_id'] = ids['a']
    bouts['fighter_b_id'] = ids['b']
    return bouts


def build_bouts(raw, fighters):
    res = raw['ufc_fight_results'].copy()
    events = raw['ufc_event_details'][['EVENT', 'DATE', 'LOCATION']].copy()
    events['date'] = pd.to_datetime(events['DATE'], format='%B %d, %Y', errors='coerce')
    res = res.merge(events[['EVENT', 'date', 'LOCATION']], on='EVENT', how='left')

    # Some events were renamed on UFCStats (e.g. "UFC Fight Night" -> "Noche UFC") so the
    # mirror lists those fights twice. Keep one copy per fight URL, preferring the dated one.
    res = res.sort_values('date', na_position='last').drop_duplicates('URL', keep='first')
    res = res.dropna(subset=['date'])

    names = res['BOUT'].str.split(' vs. ', n=1, expand=True)
    res['fighter_a'] = names[0].str.strip()
    res['fighter_b'] = names[1].str.strip()

    outcome_map = {'W/L': 'A', 'L/W': 'B', 'D/D': 'draw', 'NC/NC': 'nc'}
    res['result'] = res['OUTCOME'].map(outcome_map).fillna('nc')
    res['winner'] = np.where(res['result'] == 'A', res['fighter_a'],
                             np.where(res['result'] == 'B', res['fighter_b'], ''))

    bouts = pd.DataFrame({
        'fight_url': res['URL'], 'event': res['EVENT'], 'date': res['date'],
        'location': res['LOCATION'], 'fighter_a': res['fighter_a'], 'fighter_b': res['fighter_b'],
        'result': res['result'], 'winner': res['winner'],
        'weight_class': res['WEIGHTCLASS'], 'method': res['METHOD'],
        'method_detail': res['DETAILS'], 'end_round': pd.to_numeric(res['ROUND'], errors='coerce'),
        'end_time': res['TIME'], 'time_format': res['TIME FORMAT'], 'referee': res['REFEREE'],
    })
    bouts['title_fight'] = bouts['weight_class'].str.contains('Title', na=False)
    bouts['scheduled_rounds'] = bouts['time_format'].map(scheduled_rounds)
    bouts['fight_sec'] = [fight_seconds(r, t, f) for r, t, f in
                          zip(bouts['end_round'], bouts['end_time'], bouts['time_format'])]
    bouts['women'] = bouts['weight_class'].str.contains("Women", na=False)

    # Attach in-fight stats for each corner
    totals, per_round = aggregate_stats(raw['ufc_fight_stats'])
    stat_cols = [c for c in totals.columns if c not in ('EVENT', 'BOUT', 'FIGHTER')]
    # Event names in the stats file can be the pre-rename version, so match on bout + fighter + event
    key = res[['URL', 'EVENT', 'BOUT']].rename(columns={'URL': 'fight_url'})
    alt = raw['ufc_fight_results'][['URL', 'EVENT', 'BOUT']].rename(columns={'URL': 'fight_url'})
    key = pd.concat([key, alt]).drop_duplicates()
    totals = totals.merge(key, on=['EVENT', 'BOUT'], how='inner').drop_duplicates(['fight_url', 'FIGHTER'])

    for side in ('a', 'b'):
        side_stats = totals.rename(columns={c: f'{side}_{c}' for c in stat_cols})
        side_stats = side_stats.rename(columns={'FIGHTER': f'fighter_{side}'})
        bouts = bouts.merge(side_stats[['fight_url', f'fighter_{side}'] + [f'{side}_{c}' for c in stat_cols]],
                            on=['fight_url', f'fighter_{side}'], how='left')
    bouts['has_stats'] = bouts['a_sig_l'].notna() & bouts['b_sig_l'].notna()

    # Rounds won on significant strikes (a simple proxy for how judges see rounds)
    per_round = per_round.merge(key, on=['EVENT', 'BOUT'], how='inner')
    rw = per_round.pivot_table(index=['fight_url', 'round_no'], columns='FIGHTER', values='sig_l', aggfunc='sum')
    a_won, b_won = [], []
    rw_groups = {url: grp.droplevel(0) for url, grp in rw.groupby(level=0)}
    for url, fa, fb in zip(bouts['fight_url'], bouts['fighter_a'], bouts['fighter_b']):
        grp = rw_groups.get(url)
        if grp is None or fa not in grp.columns or fb not in grp.columns:
            a_won.append(np.nan); b_won.append(np.nan); continue
        a_won.append(int((grp[fa] > grp[fb]).sum())); b_won.append(int((grp[fb] > grp[fa]).sum()))
    bouts['a_rounds_won_strikes'] = a_won
    bouts['b_rounds_won_strikes'] = b_won

    bouts = resolve_fighter_ids(bouts, fighters)
    # Order by date, then keep the card order stable (mirror lists main event first)
    bouts = bouts.iloc[::-1].reset_index(drop=True)
    bouts = bouts.sort_values('date', kind='stable').reset_index(drop=True)
    return bouts


def build(raw_dir=RAW_DIR, out_dir=PROCESSED_DIR, verbose=True):
    os.makedirs(out_dir, exist_ok=True)
    raw = load_raw(raw_dir)
    fighters = build_fighters(raw)
    bouts = build_bouts(raw, fighters)

    fighters.to_csv(os.path.join(out_dir, 'fighters.csv'), index=False)
    bouts.to_csv(os.path.join(out_dir, 'bouts.csv'), index=False)

    if verbose:
        decided = bouts['result'].isin(['A', 'B']).sum()
        print(f"  fighters.csv : {len(fighters):,} fighter profiles")
        print(f"  bouts.csv    : {len(bouts):,} fights ({decided:,} with a winner), "
              f"{bouts['date'].min():%Y-%m-%d} to {bouts['date'].max():%Y-%m-%d}")
        print(f"                 {bouts['has_stats'].mean():.1%} of fights have full in-fight stats")
    return bouts, fighters


if __name__ == '__main__':
    raw_dir = sys.argv[1] if len(sys.argv) > 1 else RAW_DIR
    build(raw_dir)
