import shap as sh
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
from icecream import ic

# shap | Explains WHY the model made a specific prediction — per-feature push values.
# matplotlib | Plotting library; will be used for SHAP visual plots (force plots) later.
# pandas | Loads the matchups CSV into a DataFrame and builds our results tables.
# train_test_split | Shuffles and splits the data: the model learns on one set, gets graded on another.
# RandomForestClassifier | 100 decision trees that vote on a binary outcome: does Fighter A win?
# accuracy_score / confusion_matrix | Grading tools for a classifier (replaced MAE/R2 from the old regressor).
# icecream | Debug printing that auto-labels variables (ic| prefix).


def train_fighter_model():
    # 1. LOAD THE MATCHUP DATA
    # Each row = one synthetic matchup: 8 stat DIFFERENCES (A minus B) + the winner label.
    # Built by generate_matchups.py — 40,000 rows (20k pairs + their mirrored versions).
    data_path = 'data/processed/matchups.csv'
    df = pd.read_csv(data_path)

    # 2. SEPARATE FEATURES (X) FROM THE ANSWER KEY (y)
    # .drop returns everything EXCEPT 'winner' — the 8 difference columns the model learns from.
    # y holds only the answers: 1 = Fighter A won, 0 = Fighter B won.
    # Keeping these separate is the anti-cheating wall: the model never sees the answer as an input.
    X = df.drop(columns=['winner'])
    y = df['winner']

    # Drop any row with a missing value — the forest can't do math on NaN and would crash.
    # y[X.index] then keeps ONLY the same surviving row labels, so every feature row
    # stays paired with ITS OWN answer. Without this realignment, answers would silently
    # shift onto the wrong matchups — no crash, just a model learning garbage.
    X = X.dropna()
    y = y[X.index]

    # 3. THE SPLIT
    # 80% of rows train the model; 20% are hidden away as the final exam.
    # random_state=42 makes the "random" shuffle identical every run — reproducible results.
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # 4. TRAIN THE MODEL
    # n_estimators=100 builds a forest of 100 trees, each trained on a random subset of
    # rows AND features. Each tree overfits in its own random direction; when all 100 vote,
    # the quirks cancel out and the shared signal survives (this is why it's an "ensemble").
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    ic("Training the Random Forest model...")
    model.fit(X_train, y_train)

    # 5. EVALUATE (THE FINAL EXAM)
    # The model predicts winners for the 8,000 test rows it has never seen.
    # accuracy = fraction it got right (0.62 = 62%). Baseline for coin-flip guessing is 0.50.
    # The confusion matrix breaks results into a 2x2 grid:
    #   [[correct-B   wrong-said-A],
    #    [wrong-said-B   correct-A]] — balanced off-diagonals mean no bias toward either slot.
    predictions = model.predict(X_test)
    acc = accuracy_score(y_test, predictions)
    cm = confusion_matrix(y_test, predictions)
    print(f"Accuracy: {acc:.4f}")
    print(f"Confusion matrix:\n{cm}")

    # 6. SHAP — EXPLAIN ONE SPECIFIC PREDICTION (the "Judge" logic)
    # TreeExplainer wraps the trained forest so it can decompose any single prediction.
    # .iloc[[0]] grabs the first test row BY POSITION; double brackets keep it as a
    # one-row DataFrame (SHAP's expected shape) instead of collapsing to a Series.
    explainer = sh.TreeExplainer(model)
    one_matchup = X_test.iloc[[0]]
    shap_values = explainer.shap_values(one_matchup)

    # predict_proba gives confidence instead of a hard 1/0 answer.
    # [0] = the first (only) matchup passed in; [1] = probability of class 1 ("A wins").
    # :.1% formats 0.59 as "59.0%" automatically.
    prob = model.predict_proba(one_matchup)[0][1]
    print(f"Model predicts A wins with {prob:.1%} confidence")

    # shap_values has shape (1 matchup, 8 features, 2 classes). The two class columns are
    # mirror images (+x / -x), so we only need class 1: shap_values[0, :, 1] reads as
    # "matchup 0, all 8 features, the A-wins class."
    # Positive value = pushed the prediction toward A; negative = toward B.
    # key=abs sorts by SIZE of the push regardless of direction — biggest factors first.
    explanation = pd.DataFrame({
        'feature': X.columns,
        'shap_value': shap_values[0, :, 1]
    }).sort_values(by='shap_value', key=abs, ascending=False)
    ic(explanation)

    # 7. GLOBAL FEATURE IMPORTANCE (what the Judge values ON AVERAGE)
    # Unlike SHAP (one specific matchup), this ranks features across ALL 40,000 matchups.
    # feature_importances_ has no parentheses — it's a stored property computed during .fit(),
    # not a function being called.
    importances = pd.DataFrame({
        'feature': X.columns,
        'importance': model.feature_importances_
    }).sort_values(by='importance', ascending=False)
    ic("Feature Importances (What the AI Judge values most):")
    ic(importances)


if __name__ == "__main__":
    # This guard means "only auto-run when executed directly (python3 train_model.py)."
    # If another script IMPORTS this file to borrow the function, __name__ won't equal
    # "__main__" and training won't fire off accidentally during the import.
    train_fighter_model()