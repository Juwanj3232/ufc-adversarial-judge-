# 🥊 UFC Adversarial Judge

An interpretable AI fight prediction system that acts as an **Adversarial Judge** — it doesn't just predict who wins a UFC matchup, but interrogates **why** using real strike, grappling, physical, and career data, explained through per-prediction **SHAP values** and tactical fight breakdowns.

Built with `scikit-learn` (logistic regression + gradient-boosted trees blend) and `SHAP` (`TreeExplainer`), on round-by-round UFCStats data refreshed automatically.

---

## 🎯 The Vision & Intellect Companion

Most UFC prediction models are black boxes that output a single probability without context. The **UFC Adversarial Judge** is designed to pair directly with your combat sports intellect:
1. **Explainable Verdicts**: It provides a courtroom-style deliberation breakdown showing exactly which attributes pushed the decision toward Fighter A or Fighter B.
2. **Strength of Schedule Reality Checks**: Flags when raw stats (like high striking volume or accuracy) are padded against unranked newcomers vs. battle-tested against championship-level competition.
3. **Interactive Fight Simulation**: Allows you to adjust fighter gameplans (e.g., "What if Fighter A shoots 2 takedowns per round?") and watch how the judge's verdict responds in real time.

---

## 🚀 Quickstart

```bash
pip install -r requirements.txt

# 1. Pull the latest UFC data, rebuild features, retrain, evaluate and backtest (~1 min)
python3 scripts/update_data.py --full

# 2. Predict a fight (Adesanya vs Shara Magomedov, UFC Saudi Arabia, 5 Dec 2026)
python3 scripts/predict_fight.py "Israel Adesanya" "Shara Magomedov" --date 2026-12-05

# What-if sandbox, or refresh the data first
python3 scripts/predict_fight.py "Adesanya" "Shara" --simulate
python3 scripts/predict_fight.py "Adesanya" "Shara" --refresh

# 3. Backtest any fighter's past fights, predicted honestly and explained
python3 scripts/backtest.py --fighter "Israel Adesanya" --fighter "Alex Pereira"

# 4. Keep data fresh automatically (weekly macOS job, Mondays 09:00)
bash scheduling/install_launchd.sh
```

Full explanation of the data sources, update options, honest testing and the "what is a true win" analysis:
**[docs/DATA_PIPELINE_AND_BACKTEST.md](docs/DATA_PIPELINE_AND_BACKTEST.md)**.

---

## 🏗️ Architecture

```
update_data.py    → Downloads the daily UFCStats mirror (github.com/Greco1899/scrape_ufc_stats),
                    validates it, keeps the previous copy, then runs every step below.
build_dataset.py  → Builds bouts.csv (every fight + round-by-round stats for both fighters)
                    and fighters.csv (height, reach, stance, DOB).
features.py       → Replays every fight in date order and freezes each fighter's stats as they
                    stood the morning of the fight: Elo, strength of schedule, striking, grappling,
                    recent form, durability, age, layoff. No future information can leak in.
judge_model.py    → The model (logistic regression + boosted trees blend) and its per-fight
                    explanations (linear contributions + SHAP).
train_model.py    → Walk-forward evaluation (each year predicted by a model trained only on earlier
                    years) and the production model in models/ufc_judge_model.joblib.
win_anatomy.py    → Judge model of what wins UFC decisions; grades every win (clear, competitive,
                    coin-flip, contested, dominant/comeback/quick finish) and its route.
backtest.py       → Spotlight backtest: retrains before each fight, predicts, explains, grades the
                    result and says whether the model was right for the right reasons.
predict_fight.py  → Tale of the tape, win probability, the reasons, matchup breakdown, what-if mode.
```

---

## 📈 Honest Model Performance

Every number below comes from walk-forward testing on 7,049 UFC fights (2012 to Nov 2026). Each
prediction was made using only fights and stats from before that fight.

| Metric | Value |
|---|---|
| Accuracy, all fights | **62.3%** |
| Accuracy, 2024 to today | **64.4%** |
| Accuracy on clearly-won fights | **69.8%** |
| Log loss / Brier score | 0.652 / 0.230 |
| Calibration | When the model says 65-70%, the favourite has won 68.3% |

> **Why lower than the old 67-75%?** The previous pipeline gave every past fight each fighter's
> *final* career averages, which include the fight being predicted and everything after it. Rebuilt
> the old way on the same test years, that method scores 66.2%, but the edge almost vanishes for
> experienced fighters, where the honest model now does slightly better (63.7% vs 63.1%). That is the
> fingerprint of leakage rather than real skill.

### What actually wins a UFC decision (judge model, all UFC decisions)

| In-fight event | Worth about this many significant strikes on the cards |
|---|---|
| Knockdown | 16 |
| Submission attempt | 5 |
| Minute of control time | 5 |
| Takedown | 3 |

About 15% of UFC results are coin-flip decisions, contested decisions or comeback finishes. No
pre-fight model does better than a coin flip on those, and this one scores 43-46%.

---

## 🥊 Adesanya & Shara Magomedov in the Backtest

Predicted fight by fight using only information available before each bout:

- **Israel Adesanya: 14 of 19 called correctly.** The model turned against him from 2024 on, citing
  age, accumulated cage time, layoffs and opponents' momentum or wrestling, and it was right in all
  three losses (Du Plessis, Imavov, Pyfer). His remaining edge is strength of schedule.
- **Shara Magomedov: 5 of 7 called correctly.** He is a pure volume striker with one takedown
  attempt in the UFC. His only loss came against a longer, elusive striker with a stronger schedule
  (Michael Page).

Fight-by-fight reasoning: `reports/backtest_report.md` (generated by `backtest.py`).

---

## 🛠️ Repository Structure

```
├── data/                       # git-ignored; rebuilt by update_data.py
│   ├── raw/ufcstats/           # mirror CSVs + manifest.json (+ _previous/ for rollback)
│   └── processed/              # bouts, fighters, features, fighter_snapshot
├── docs/                       # DATA_PIPELINE_AND_BACKTEST.md and project documentation
├── models/ufc_judge_model.joblib
├── reports/                    # model_metrics.json, walk-forward predictions, backtest report
├── scheduling/install_launchd.sh
├── .github/workflows/refresh-data.yml   # optional weekly cloud refresh
├── scripts/                    # pipeline (see Architecture); data_cleaning.py,
│                               # generate_matchups.py and scraper.py are legacy and unused
└── requirements.txt
```

---

*Built as an interpretable machine learning system for combat sports analysis.*
