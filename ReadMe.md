# UFC Adversarial Judge

An AI system that predicts the outcome of a UFC matchup **and explains its reasoning** — not just "Fighter A wins," but "Fighter A wins, driven primarily by a strike accuracy edge and volume striking advantage, despite Fighter B's superior takedown defense."

Built with `scikit-learn` (Random Forest) and `SHAP` for per-prediction explainability.

---

## The Idea

Most "who wins this fight" predictors are black boxes. This project's goal was to build a **judge**, not just a predictor — a model that can be interrogated about *why* it favors one fighter over another for any specific matchup, using real skill statistics rather than gut-feel commentary.

## Pipeline

```
data_cleaning.py      → cleans raw fighter data, converts units, engineers win_ratio
generate_matchups.py  → builds synthetic head-to-head matchups from fighter pairs
train_model.py         → trains a classifier, evaluates it, and explains predictions with SHAP
```

Each script writes its output to `data/processed/`, which the next script consumes.

## How It Works

**1. Data.** Fighter career statistics (striking, grappling, physical measurements) sourced from a public UFC stats dataset. Cleaned and standardized: imperial units converted to metric, percentage strings parsed to decimals, missing values median-imputed.

**2. Matchup generation.** Rather than predicting a single fighter's career win total (a weak, low-signal target — see *Design Decisions* below), the model predicts **head-to-head outcomes**. For any two fighters, we compute a *difference vector* — each stat for Fighter A minus the same stat for Fighter B — and label the row by which fighter has the higher career win ratio. Every matchup is also mirrored (B − A, with the label flipped), so the model can't learn a lazy "whoever's listed first wins" shortcut.

**3. Classification.** A `RandomForestClassifier` (100 trees) is trained on ~40,000 synthetic matchups, split 80/20 for training and evaluation.

**4. Explainability.** `SHAP`'s `TreeExplainer` breaks down any single prediction into per-feature contributions — showing exactly which stat advantages pushed the model toward each fighter, and by how much.

## Results

| Metric | Score |
|---|---|
| Accuracy | 61.9% |
| Confusion matrix | Balanced — errors split ~evenly between both directions |

**Global feature importance** (what the model relies on most, across all matchups):

| Rank | Feature | Importance |
|---|---|---|
| 1 | Takedown average | 0.160 |
| 2 | Strikes landed/min | 0.150 |
| 3 | Strikes absorbed/min | 0.148 |
| 4 | Takedown defense | 0.129 |
| 5 | Strike accuracy | 0.120 |
| 6 | Strike defense | 0.113 |
| 7 | Reach | 0.092 |
| 8 | Height | 0.088 |

Global importance shows what the model values *on average* — but SHAP reveals that the deciding factor often shifts per matchup. In one tested case, `takedown_avg` (the top global feature) was nearly irrelevant, while `strike_accuracy` and `SLpM` drove the entire prediction. That's the explainability payoff: the model's *stated general priorities* and its *actual reasoning on a specific fight* aren't always the same thing.

## Design Decisions Worth Knowing

**Why predict head-to-head outcomes instead of career stats?**
Earlier iterations tried predicting a fighter's raw career win total, and separately their win ratio, directly from career-average stats. Both capped out at a low R² (0.22 and 0.12, respectively) — because a fighter's win *count* is mostly a function of matchmaking and career length, not skill alone. Reframing the problem as "who wins this specific matchup" — using *differences* between two fighters rather than absolute stats — produced a meaningfully more learnable signal.

**Why difference vectors instead of raw stats side-by-side?**
Feeding both fighters' raw stats into the model forces it to learn, from scratch, that two columns represent "the same stat for two different people." Pre-computing the difference does that comparison up front, so every input directly represents an *advantage*, not an absolute value the model has to relate on its own.

**Why exclude win/loss counts from the feature set?**
The label (who wins) is derived from win ratio. If win ratio — or wins/losses directly — were also included as *features*, the model could shortcut straight to the answer instead of learning from skill statistics. This is a data leakage trap, and earlier versions of this project fell into it before catching and fixing it.

**Why median imputation over mean?**
Athletic statistics contain real outliers (a single dominant performance, a short and unusual career). Mean is dragged by those outliers; median represents the typical fighter far more faithfully.

## What Went Wrong (and What We Learned From It)

- **The scraper is parked.** UFCStats.com serves a JavaScript proof-of-work challenge to block non-browser requests — `requests`/`BeautifulSoup` can solve HTTP but can't execute JS. Rather than stand up a full Selenium browser-automation pipeline, the project pivoted to a maintained Kaggle dataset with equivalent stats and far more coverage (4,455 fighters vs. the original 20-fighter test run).
- **The original regression approach had a data leakage bug** — `win_ratio` was included both as a feature and used to define the target, artificially inflating R². Removing it dropped the score, but produced an honest baseline.
- **Two different regression targets (win count, win ratio) were tested and both hit a low ceiling**, which is itself the finding that motivated the pivot to head-to-head classification.

## Setup

```bash
pip install pandas numpy scikit-learn shap
python3 scripts/data_cleaning.py
python3 scripts/generate_matchups.py
python3 scripts/train_model.py
```

## Roadmap

- [x] Data pipeline (cleaning, feature engineering)
- [x] Head-to-head matchup generation
- [x] Random Forest classifier (~62% accuracy)
- [x] SHAP local + global explainability
- [ ] Named-fighter explainer (query any two real fighters by name, get a live explanation)
- [ ] Re-integrate a working scraper (or scheduled Kaggle dataset refresh) for ongoing data updates

---

*Built by Juwan Johnson as a portfolio project exploring interpretable ML for sports prediction.*