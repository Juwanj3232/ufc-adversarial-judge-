import os
import re
import numpy as np
import pandas as pd
from icecream import ic

# ==============================================================================
# UFC ADVERSARIAL JUDGE - DATA CLEANING PIPELINE
# ==============================================================================
# Enhancements made:
# 1. PRESERVE AUTHENTIC ZEROES: Previous code replaced 0.0 with median for
#    takedown_avg and takedown_accuracy. This falsely turned pure kickboxers
#    (e.g., Shara Magomedov, Adesanya) into wrestlers with 1.65 TD/15min!
#    We now keep authentic 0.0s for wrestling/grappling.
# 2. ANTHROPOMETRIC IMPUTATION: If reach is missing, we impute based on height
#    (ape ratio ~1.0) rather than dropping 1,900+ fighters from the roster.
# 3. ADVANCED MMA FEATURE ENGINEERING:
#    - ape_index (reach_cm - height_cm): anatomical reach advantage
#    - strike_differential (SLpM - SApM): net strikes landed vs absorbed
#    - striking_efficiency: net effective striking rate factoring accuracy & defense
#    - takedown_threat: TD_Avg * TD_Acc
#    - dynamic DOB parsing: enables precise age calculations for future fights
# 4. DE-DUPLICATION: Filters out duplicate namesake profiles by retaining the
#    profile with the most recorded fights.
# ==============================================================================


def height_to_cm(h):
    """Converts height string (e.g. 5' 11\") to centimeters."""
    if pd.isna(h) or '--' in str(h):
        return np.nan
    try:
        parts = str(h).replace('"', '').split("'")
        feet = int(parts[0])
        inches = int(parts[1].strip())
        return round((feet * 12 + inches) * 2.54, 2)
    except Exception:
        return np.nan


def reach_to_cm(r):
    """Converts reach string (e.g. 74.0\") to centimeters."""
    if pd.isna(r) or '--' in str(r):
        return np.nan
    try:
        inches = float(str(r).replace('"', '').strip())
        return round(inches * 2.54, 2)
    except Exception:
        return np.nan


def pct_to_float(p):
    """Converts percentage string (e.g. 54%) to decimal float (0.54)."""
    if pd.isna(p) or '--' in str(p):
        return np.nan
    try:
        return float(str(p).replace('%', '').strip()) / 100.0
    except Exception:
        return np.nan


def clean_fighter_data(input_path='data/raw/ufc_fighters_final.csv',
                       output_path='data/processed/cleaned_fighters.csv'):
    """Cleans raw fighter data, calculates advanced MMA metrics, and exports processed CSV."""
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df = pd.read_csv(input_path)
    ic(f"Loaded {len(df)} raw fighter records.")

    # 1. Standardize column names
    column_mapping = {
        'Fighter_Name': 'name',
        'Wins': 'wins',
        'Losses': 'losses',
        'Draws': 'draws',
        'Height': 'height_raw',
        'Weight': 'weight_raw',
        'Reach': 'reach_raw',
        'Stance': 'stance',
        'DOB': 'dob_raw',
        'SLpM': 'SLpM',
        'Str_Acc': 'strike_accuracy',
        'SApM': 'SApM',
        'Str_Def': 'strike_defense',
        'TD_Avg': 'takedown_avg',
        'TD_Acc': 'takedown_accuracy',
        'TD_Def': 'takedown_defense',
        'Sub_Avg': 'sub_avg'
    }
    df = df.rename(columns=column_mapping)

    # 2. Convert physical dimensions
    df['height_cm'] = df['height_raw'].apply(height_to_cm)
    df['reach_cm'] = df['reach_raw'].apply(reach_to_cm)

    # If reach is missing, humans typically have reach ~ height (ape index = 1.0)
    # Using height avoids dropping fighters whose reach wasn't measured on regional cards
    df['reach_cm'] = df['reach_cm'].fillna(df['height_cm'])
    df['height_cm'] = df['height_cm'].fillna(df['height_cm'].median())
    df['reach_cm'] = df['reach_cm'].fillna(df['height_cm'])
    df['ape_index'] = df['reach_cm'] - df['height_cm']

    # 3. Convert percentages and numeric stats
    df['strike_accuracy'] = df['strike_accuracy'].apply(pct_to_float)
    df['strike_defense'] = df['strike_defense'].apply(pct_to_float)
    df['takedown_accuracy'] = df['takedown_accuracy'].apply(pct_to_float)
    df['takedown_defense'] = df['takedown_defense'].apply(pct_to_float)

    for num_col in ['SLpM', 'SApM', 'takedown_avg', 'sub_avg', 'wins', 'losses', 'draws']:
        df[num_col] = pd.to_numeric(df[num_col], errors='coerce').fillna(0.0)

    # 4. Fill missing rates responsibly
    # Defense and accuracy metrics: fill missing with division/typical median (~50%)
    df['strike_accuracy'] = df['strike_accuracy'].fillna(df['strike_accuracy'].median())
    df['strike_defense'] = df['strike_defense'].fillna(df['strike_defense'].median())
    df['takedown_defense'] = df['takedown_defense'].fillna(df['takedown_defense'].median())

    # Takedown accuracy: if fighter never attempts takedowns, accuracy is 0.0, NOT median!
    df['takedown_accuracy'] = df['takedown_accuracy'].fillna(0.0)

    # 5. Advanced Feature Engineering
    df['total_fights'] = df['wins'] + df['losses'] + df['draws']
    df['win_ratio'] = df['wins'] / (df['wins'] + df['losses'] + 0.001)
    df['strike_differential'] = df['SLpM'] - df['SApM']
    
    # Net striking efficiency: offensive output times accuracy minus defensive absorption
    df['striking_efficiency'] = (df['SLpM'] * df['strike_accuracy']) - (df['SApM'] * (1.0 - df['strike_defense']))
    df['takedown_threat'] = df['takedown_avg'] * df['takedown_accuracy']

    # 6. Parse DOB for dynamic age calculation
    df['dob'] = pd.to_datetime(df['dob_raw'], errors='coerce')
    df['stance'] = df['stance'].fillna('Orthodox').str.strip()

    # 7. Drop inactive ghost profiles (0 wins, 0 losses)
    df = df[df['total_fights'] > 0].copy()

    # 8. De-duplicate fighters with identical names: keep the profile with more fights
    df = df.sort_values(by=['total_fights', 'wins'], ascending=False).drop_duplicates(subset=['name'], keep='first')
    df = df.sort_values(by='name').reset_index(drop=True)

    # Save cleaned data
    df.to_csv(output_path, index=False)
    ic(f"Successfully cleaned and saved {len(df)} fighter records to {output_path}")
    return df


if __name__ == "__main__":
    clean_fighter_data()