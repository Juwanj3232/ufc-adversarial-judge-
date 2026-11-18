import argparse
import os
from collections import defaultdict
import numpy as np
import pandas as pd
from icecream import ic

# ==============================================================================
# UFC ADVERSARIAL JUDGE - MATCHUP GENERATION PIPELINE
# ==============================================================================
# Why Real Bouts > Synthetic Matchups:
# - The original script generated 20,000 random fighter pairings and labeled
#   the winner based on who had a higher overall career win_ratio.
# - Problem 1: It wasn't predicting who wins a fight; it was predicting who has
#   a prettier record on paper across different eras and weight divisions!
# - Problem 2: An unranked prospect (15-0) against regional fighters would be
#   favored over a battle-tested UFC champion (15-6) against elite top contenders.
#
# This upgraded generator builds matchups from ACTUAL UFC BOUTS (8,551 bouts),
# with dynamic chronological pre-fight features (zero data leakage) and symmetrical
# mirroring (F1 vs F2 and F2 vs F1) so corner color or listing order has 0 bias.
# ==============================================================================

# Core skill and physical feature differences used by the Adversarial Judge
FEATURE_COLUMNS = [
    'height_diff',
    'reach_diff',
    'ape_index_diff',
    'slpm_diff',
    'sapm_diff',
    'strike_diff_edge',
    'strike_acc_diff',
    'strike_def_diff',
    'strike_eff_diff',
    'td_avg_diff',
    'td_acc_diff',
    'td_def_diff',
    'td_threat_diff',
    'sub_avg_diff',
    'age_diff',
    'ufc_fights_diff',
    'win_streak_diff',
    'ufc_win_rate_diff'
]


def generate_real_bout_matchups(cleaned_fighters_path='data/processed/cleaned_fighters.csv',
                                gold_bouts_path='data/raw/ufc_gold_dataset_final.csv',
                                output_path='data/processed/matchups.csv'):
    """Extracts pre-fight differentials from real historical UFC bouts with zero future leakage."""
    ic("Loading cleaned fighters and real UFC bout history...")
    fighters = pd.read_csv(cleaned_fighters_path)
    gold = pd.read_csv(gold_bouts_path)

    fighters['dob'] = pd.to_datetime(fighters['dob'], errors='coerce')
    f_dict = fighters.set_index('name').to_dict('index')

    gold['Event_Date'] = pd.to_datetime(gold['Event_Date'], errors='coerce')
    gold = gold.sort_values('Event_Date').reset_index(drop=True)

    # Dynamic pre-fight tracker: updates fight-by-fight to prevent chronological data leakage
    history_tracker = defaultdict(lambda: {
        'ufc_wins': 0,
        'ufc_losses': 0,
        'ufc_fights': 0,
        'win_streak': 0,
        'last_fight_date': None
    })

    matchup_rows = []

    for _, row in gold.iterrows():
        f1 = row['Fighter_1']
        f2 = row['Fighter_2']
        winner = row['Winner']
        fight_date = row['Event_Date']

        # Skip draws or no contests for binary outcome modeling
        if winner not in [f1, f2]:
            continue

        # Fighter must exist in the cleaned database
        if f1 not in f_dict or f2 not in f_dict:
            continue

        s1 = f_dict[f1]
        s2 = f_dict[f2]
        h1 = history_tracker[f1]
        h2 = history_tracker[f2]

        # Calculate exact age at fight date (fallback to 30.0 if DOB unavailable)
        age1 = (fight_date - s1['dob']).days / 365.25 if pd.notna(s1['dob']) else 30.0
        age2 = (fight_date - s2['dob']).days / 365.25 if pd.notna(s2['dob']) else 30.0

        # Pre-fight UFC win rates
        rate1 = h1['ufc_wins'] / (h1['ufc_fights'] + 0.001) if h1['ufc_fights'] > 0 else 0.50
        rate2 = h2['ufc_wins'] / (h2['ufc_fights'] + 0.001) if h2['ufc_fights'] > 0 else 0.50

        # Construct primary matchup row (F1 - F2)
        matchup_f1 = {
            'event_date': fight_date,
            'fighter_a': f1,
            'fighter_b': f2,
            'height_diff': s1['height_cm'] - s2['height_cm'],
            'reach_diff': s1['reach_cm'] - s2['reach_cm'],
            'ape_index_diff': s1['ape_index'] - s2['ape_index'],
            'slpm_diff': s1['SLpM'] - s2['SLpM'],
            'sapm_diff': s1['SApM'] - s2['SApM'],
            'strike_diff_edge': s1['strike_differential'] - s2['strike_differential'],
            'strike_acc_diff': s1['strike_accuracy'] - s2['strike_accuracy'],
            'strike_def_diff': s1['strike_defense'] - s2['strike_defense'],
            'strike_eff_diff': s1['striking_efficiency'] - s2['striking_efficiency'],
            'td_avg_diff': s1['takedown_avg'] - s2['takedown_avg'],
            'td_acc_diff': s1['takedown_accuracy'] - s2['takedown_accuracy'],
            'td_def_diff': s1['takedown_defense'] - s2['takedown_defense'],
            'td_threat_diff': s1['takedown_threat'] - s2['takedown_threat'],
            'sub_avg_diff': s1['sub_avg'] - s2['sub_avg'],
            'age_diff': age1 - age2,
            'ufc_fights_diff': h1['ufc_fights'] - h2['ufc_fights'],
            'win_streak_diff': h1['win_streak'] - h2['win_streak'],
            'ufc_win_rate_diff': rate1 - rate2,
            'winner': 1 if winner == f1 else 0
        }
        matchup_rows.append(matchup_f1)

        # Symmetrical Mirror: (F2 - F1) with inverted label
        # Guarantees the model has ZERO bias towards whoever is listed in Slot 1
        matchup_f2 = {
            'event_date': fight_date,
            'fighter_a': f2,
            'fighter_b': f1,
            'height_diff': -matchup_f1['height_diff'],
            'reach_diff': -matchup_f1['reach_diff'],
            'ape_index_diff': -matchup_f1['ape_index_diff'],
            'slpm_diff': -matchup_f1['slpm_diff'],
            'sapm_diff': -matchup_f1['sapm_diff'],
            'strike_diff_edge': -matchup_f1['strike_diff_edge'],
            'strike_acc_diff': -matchup_f1['strike_acc_diff'],
            'strike_def_diff': -matchup_f1['strike_def_diff'],
            'strike_eff_diff': -matchup_f1['strike_eff_diff'],
            'td_avg_diff': -matchup_f1['td_avg_diff'],
            'td_acc_diff': -matchup_f1['td_acc_diff'],
            'td_def_diff': -matchup_f1['td_def_diff'],
            'td_threat_diff': -matchup_f1['td_threat_diff'],
            'sub_avg_diff': -matchup_f1['sub_avg_diff'],
            'age_diff': -matchup_f1['age_diff'],
            'ufc_fights_diff': -matchup_f1['ufc_fights_diff'],
            'win_streak_diff': -matchup_f1['win_streak_diff'],
            'ufc_win_rate_diff': -matchup_f1['ufc_win_rate_diff'],
            'winner': 1 - matchup_f1['winner']
        }
        matchup_rows.append(matchup_f2)

        # Update historical tracker AFTER recording pre-fight features (no lookahead!)
        if winner == f1:
            h1['ufc_wins'] += 1
            h1['win_streak'] = max(1, h1['win_streak'] + 1)
            h2['ufc_losses'] += 1
            h2['win_streak'] = min(-1, h2['win_streak'] - 1)
        elif winner == f2:
            h2['ufc_wins'] += 1
            h2['win_streak'] = max(1, h2['win_streak'] + 1)
            h1['ufc_losses'] += 1
            h1['win_streak'] = min(-1, h1['win_streak'] - 1)

        h1['ufc_fights'] += 1
        h2['ufc_fights'] += 1
        h1['last_fight_date'] = fight_date
        h2['last_fight_date'] = fight_date

    matchups_df = pd.DataFrame(matchup_rows)
    matchups_df = matchups_df.sort_values(by='event_date').reset_index(drop=True)

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    matchups_df.to_csv(output_path, index=False)
    ic(f"Generated {len(matchups_df)} real-bout matchup examples saved to {output_path}")
    return matchups_df


def generate_synthetic_matchups(cleaned_fighters_path='data/processed/cleaned_fighters.csv',
                                output_path='data/processed/matchups.csv',
                                n_matchups=20000,
                                seed=42):
    """Generates synthetic matchups between random fighter pairs based on skill stats."""
    ic("Generating synthetic random matchups (legacy mode)...")
    df = pd.read_csv(cleaned_fighters_path)
    df = df.dropna(subset=['height_cm', 'reach_cm', 'SLpM', 'SApM', 'win_ratio']).reset_index(drop=True)

    rng = np.random.default_rng(seed)
    idx = df.index.to_numpy()

    matchup_rows = []
    for _ in range(n_matchups):
        a, b = rng.choice(idx, size=2, replace=False)
        fa = df.loc[a]
        fb = df.loc[b]

        label = 1 if fa['win_ratio'] > fb['win_ratio'] else 0
        row_a = {
            'height_diff': fa['height_cm'] - fb['height_cm'],
            'reach_diff': fa['reach_cm'] - fb['reach_cm'],
            'ape_index_diff': fa['ape_index'] - fb['ape_index'],
            'slpm_diff': fa['SLpM'] - fb['SLpM'],
            'sapm_diff': fa['SApM'] - fb['SApM'],
            'strike_diff_edge': fa['strike_differential'] - fb['strike_differential'],
            'strike_acc_diff': fa['strike_accuracy'] - fb['strike_accuracy'],
            'strike_def_diff': fa['strike_defense'] - fb['strike_defense'],
            'strike_eff_diff': fa['striking_efficiency'] - fb['striking_efficiency'],
            'td_avg_diff': fa['takedown_avg'] - fb['takedown_avg'],
            'td_acc_diff': fa['takedown_accuracy'] - fb['takedown_accuracy'],
            'td_def_diff': fa['takedown_defense'] - fb['takedown_defense'],
            'td_threat_diff': fa['takedown_threat'] - fb['takedown_threat'],
            'sub_avg_diff': fa['sub_avg'] - fb['sub_avg'],
            'age_diff': 0.0,
            'ufc_fights_diff': fa['total_fights'] - fb['total_fights'],
            'win_streak_diff': 0,
            'ufc_win_rate_diff': fa['win_ratio'] - fb['win_ratio'],
            'winner': label
        }
        matchup_rows.append(row_a)
        # Mirror
        row_b = {k: (-v if k != 'winner' else 1 - v) for k, v in row_a.items()}
        matchup_rows.append(row_b)

    matchups_df = pd.DataFrame(matchup_rows)
    matchups_df.to_csv(output_path, index=False)
    ic(f"Generated {len(matchups_df)} synthetic matchup examples saved to {output_path}")
    return matchups_df


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate UFC matchups dataset")
    parser.add_argument('--mode', choices=['real', 'synthetic'], default='real',
                        help="Generate matchups from 'real' historical UFC bouts or 'synthetic' pairs.")
    args = parser.parse_args()

    if args.mode == 'real':
        generate_real_bout_matchups()
    else:
        generate_synthetic_matchups()