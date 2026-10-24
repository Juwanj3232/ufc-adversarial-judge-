import pandas as pd
import numpy as np

# line 1 | Pandas loads the cleaned fighter table and writes the final matchups CSV.
# line 2 | NumPy gives us a fast, seedable random number generator for picking fighter pairs.

# These are the 8 stats we compare between two fighters.
# IMPORTANT: none of these are derived from wins/losses, so the model can't "cheat" by back-calculating the win_ratio label from them.
FEATURES = [
    'strike_defense',
    'SApM',
    'takedown_defense',
    'SLpM',
    'strike_accuracy',
    'takedown_avg',
    'reach_cm',
    'height_cm'
]


def generate_matchups(input_path, output_path, n_matchups = 20000, seed = 42):
    # 1. LOAD THE CLEANED FIGHTERS
    df = pd.read_csv(input_path)

    # Drop any fighter missing one of our feature stats or the win_ratio label.
    # A matchup is only valid if BOTH fighters have every number we need.
    df = df.dropna(subset=FEATURES + ['win_ratio']).reset_index(drop=True)
    print(f"Usable fighters: {len(df)}")

    # line 30 | reset_index gives us clean 0,1,2... row numbers so random picking is simple.

    # 2. SET UP THE RANDOM GENERATOR
    rng = np.random.default_rng(seed) # <- python version of random number seed 
    idx = df.index.to_numpy()

    # line 36 | A fixed seed (42) means the "random" pairs are the SAME every run — reproducible.

    X = []  # will hold the difference vectors (the model's input)
    y = []  # will hold the labels: 1 = fighter A wins, 0 = fighter B wins

    # 3. BUILD THE MATCHUPS
    for _ in range(n_matchups):
        # Pick two DIFFERENT fighters at random (replace=False stops A vs A).
        a, b = rng.choice(idx, size=2, replace=False)
        fighter_a = df.loc[a]
        fighter_b = df.loc[b]

        # The difference vector: A's stat minus B's stat, for every feature.
        # Positive number = A has the edge in that stat; negative = B does.
    
        diff = [fighter_a[f] - fighter_b[f] for f in FEATURES]

        # The label: whoever has the higher career win ratio is the "winner".
        # win_ratio is NOT in FEATURES, so this is a real fact the model must infer. || ternary expression
        label = 1 if fighter_a['win_ratio'] > fighter_b['win_ratio'] else 0

        # Store the matchup as written: A vs B.
        X.append(diff)
        y.append(label)

        # 4. ADD THE MIRROR (B vs A)
        # Flip every difference sign and flip the label. This stops the model
        # from learning "fighter listed first always wins" — it forces the model
        # to learn that the DIRECTION of the advantage is what matters.
        X.append([-d for d in diff])
        y.append(1 - label)

    # line 64 | Each loop adds TWO rows (A-B and B-A), so we get 2 x n_matchups total.

    # 5. SAVE TO CSV
    # Build a DataFrame: one column per feature difference, plus the winner label.
    matchups = pd.DataFrame(X, columns=FEATURES)
    matchups['winner'] = y
    matchups.to_csv(output_path, index=False)
    print(f"Saved {len(matchups)} matchup rows to {output_path}")


if __name__ == "__main__":
   generate_matchups(
        "data/processed/cleaned_fighters.csv",
        "data/processed/matchups.csv"
    )