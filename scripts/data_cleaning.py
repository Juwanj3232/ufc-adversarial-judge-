import pandas as pd
import numpy as np

# make a function that cleans csv files and filters out new fighters and fighters with less stats then a certain threshold 
def clean_fighter_data(input_path, output_path):
    # Load the data onto a dataframe || like Excel sheet living inside Python
    df = pd.read_csv(input_path)
    
    # 0. COLUMN MAPPING (Kaggle → our schema)
    # Renames Kaggle's column names to match what the rest of this script expects.
    df = df.rename(columns={
            'Fighter_Name': 'name',
            'Wins':         'wins',
            'Losses':       'losses',
            'Draws':        'draws',
            'Str_Acc':      'strike_accuracy',
            'Str_Def':      'strike_defense',
            'TD_Avg':       'takedown_avg',
            'TD_Acc':       'takedown_accuracy',
            'TD_Def':       'takedown_defense',   
            'Stance':       'stance'
        })

    # Convert Height from "5' 11"" string to centimeters (float)
    def height_to_cm(h):
        if pd.isna(h) or '--' in str(h): return None
        try:
            parts = str(h).replace('"','').split("'")
            return round((int(parts[0]) * 12 + int(parts[1].strip())) * 2.54, 2)
        except: return None

    # Convert Reach from "66.0"" string to centimeters (float)
    def reach_to_cm(r):
        if pd.isna(r) or '--' in str(r): return None
        try:
            return round(float(str(r).replace('"','')) * 2.54, 2)
        except: return None

    # Strip the % sign and convert to decimal (38% → 0.38)
    def pct_to_float(p):
        if pd.isna(p): return None
        try:
            return float(str(p).replace('%','').strip()) / 100
        except: return None

    df['height_cm']       = df['Height'].apply(height_to_cm)
    df['reach_cm']        = df['Reach'].apply(reach_to_cm)
    df['strike_accuracy'] = df['strike_accuracy'].apply(pct_to_float)
    df['strike_defense']  = df['strike_defense'].apply(pct_to_float)
    df['takedown_accuracy'] = df['takedown_accuracy'].apply(pct_to_float) if 'takedown_accuracy' in df.columns else 0.0
    df['takedown_defense'] = df['takedown_defense'].apply(pct_to_float)
    
    # 1. Drop non-competitors (Remove if they have 0 wins AND 0 losses)
    # This removes "Ghost" profiles that haven't actually fought.
    df = df[~((df['wins'] == 0) & (df['losses'] == 0))]

    # 2. Imputation (Replace 0.0 with the Median)
    # We use median because UFC stats often have outliers that skew the mean.
    cols_to_fix = ['strike_accuracy', 'strike_defense', 'takedown_accuracy', 'takedown_avg']
    
    for col in cols_to_fix:
        # Replace 0.0 with NaN so we can calculate the median properly
        df[col] = df[col].replace(0.0, np.nan)
        median_val = df[col].median()
        df[col] = df[col].fillna(median_val)

    # 3. Feature Engineering: Win Ratio
    # We add 1 to the denominator to avoid "Division by Zero" errors (Laplace Smoothing)
    df['win_ratio'] = df['wins'] / (df['wins'] + df['losses'] + 0.001)

    # Save the cleaned data
    df.to_csv(output_path, index=False)
    print(f"Cleaned data saved to {output_path}")

if __name__ == "__main__":
    clean_fighter_data('data/raw/ufc_fighters_final.csv', 'data/processed/cleaned_fighters.csv')