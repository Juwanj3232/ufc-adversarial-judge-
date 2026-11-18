# Data refresh, honest testing, and "what is a true win"

_Written 2026-11-18. Data through UFC 334 (2026-11-14)._

## The short version

1. **The data is now current and rebuilt from the fight level up.** The project had 8,551 fights ending 2026-03-07. It now has 9,001 fights ending 2026-11-14, including Adesanya's loss to Joe Pyfer. Every stat is recomputed from round-by-round numbers.
2. **One command refreshes everything**, and there are three ways to make it run on its own. The recommended one is a weekly Mac background job plus a freshness check built into the predictor.
3. **The old accuracy numbers were inflated.** The old pipeline gave every past fight each fighter's *final career* stats, so the model was partly reading the answer. Tested honestly, the model picks about **62% of winners overall and 64% since 2024**, and its confidence levels are trustworthy.
4. **A "true win" is now measurable.** A judge model trained on every UFC decision shows what actually wins fights. Every past win is graded from "clear" to "contested", and the predictor is about **66% accurate on genuine wins**. It is no better than a coin flip on contested decisions and comeback finishes, which no pre-fight model can call.
5. **Adesanya and Shara backtest:** the model called 14 of Adesanya's 19 UFC fights and 5 of Shara's 7, each made with only the information available before the fight.

---

## Part 1: Updating the dataset

### Options for where the data comes from

| Option | How fresh | Effort to run | Reliability | Cost | Verdict |
|---|---|---|---|---|---|
| **A. Public UFCStats mirror** (github.com/Greco1899/scrape_ufc_stats) | Re-scraped daily, about 1 day behind events | One download of about 12 MB, under 30 s | Good. Maintained since 2023 with daily refresh commits. One upstream dependency. | Free | **Chosen** |
| B. Our own scraper against UFCStats.com | Real time | Hours for a full scrape | **Currently blocked.** UFCStats now shows a JavaScript "checking your browser" wall to scripts. Getting past it means driving a real browser, which is slow and fragile, and it works around the site's bot protection. | Free | Fallback only, if the mirror disappears |
| C. Kaggle UFC datasets | Weeks to months behind; many are abandoned | Manual download or API key | Varies; column formats change between authors | Free | Not recommended |
| D. Paid sports-data APIs (e.g. SportsDataIO, API-Sports MMA) | Real time | API integration work | High | Paid subscription; stat definitions differ from UFCStats | Overkill for this project |

**Why A wins:** it is the same UFCStats numbers the project already used, in a stable CSV format. It refreshes daily, costs nothing, and does not require us to hit UFCStats at all. It also includes **round-by-round stats for every fight**, which made the accuracy fix below possible. The old fighter-profile scrape only had career totals.

### What "accurately reflects the fighters' statistics" now means

The old pipeline used the career summary line from each fighter's UFCStats profile (SLpM, Str. Acc, and so on). The new pipeline rebuilds those numbers from every round of every fight, so it can produce a fighter's stats **as of any date**.

**Accuracy check:** I rebuilt every fighter's career numbers as of the date of the old profile scrape (March 2026). I then compared them with what UFCStats printed on the profile pages. For the 1,200 established fighters (5+ UFC fights, active since 2005):

| Stat | Within 0.25 per minute, or 5 percentage points | Exact match to UFCStats' rounding |
|---|---|---|
| Sig. strikes landed per min | 89.0% | 74.1% |
| Sig. strikes absorbed per min | 88.6% | 73.2% |
| Striking accuracy | 97.7% | 82.7% |
| Striking defense | 98.2% | 84.5% |
| Takedowns per 15 min | 90.8% | 75.9% |

The remaining differences come from fights UFCStats counts on profile pages but does not list as UFC events. The main examples are Dana White's Contender Series and some TUF exhibition bouts, plus early-1990s fights that have no stats. Our numbers are **UFC-only**, which is the consistent choice for comparing fighters.

Other data fixes:
- **Duplicate fights removed.** UFCStats renamed some events (for example "UFC Fight Night" to "Noche UFC"), which listed 25 fights twice.
- **Fighters who share a name are kept apart.** There are two Bruno Silvas, two Jean Silvas, and others. Each bout is matched to the right profile by weight class, so their records don't merge.
- **Fight time is exact.** It is computed from the round format, round and clock (for example 3 Rnd (5-5-5), R3 2:10), across all 20 formats used since 1994.

---

## Part 2: Keeping it updated

Everything runs from one command:

```bash
python3 scripts/update_data.py            # download, rebuild data, refit model (~30 s)
python3 scripts/update_data.py --full     # also rerun the honest evaluation and backtest (~1 min)
python3 scripts/update_data.py --check    # how old is my data?
```

Before replacing anything, the refresh checks the new download. All files must arrive with the expected columns. No file may shrink by more than 1%, and the newest event cannot be older than what we already have. If any check fails, nothing is replaced. The previous copy is kept in `data/raw/ufcstats/_previous/` for rollback, and `data/raw/ufcstats/manifest.json` records exactly which mirror commit you have.

### Options for running it automatically

| Option | Runs when your Mac is off? | Setup | Best for |
|---|---|---|---|
| **1. Freshness check in the predictor** (already built in) | n/a | None | Never predicting on stale data. It warns when data is more than 7 days old, and `--refresh` updates first. |
| **2. Weekly Mac background job (launchd)** | No, but it catches up when the Mac wakes | `bash scheduling/install_launchd.sh` | **Recommended.** Keeps your local data, model and reports fresh every Monday at 09:00. |
| 3. GitHub Actions weekly workflow | Yes | Push `.github/workflows/refresh-data.yml` | Keeping the reports and model *in the GitHub repo* fresh. Your `data/` folder is git-ignored, so this does not update your laptop's data. |
| 4. Manual | n/a | None | Running it before a fight you care about |

**Recommendation: options 1 and 2 together.** The predictions run on your machine from local data, so the local job is what actually matters. The built-in check guarantees you never predict on stale data even if the job missed a week. Add option 3 only if you want the GitHub repo to show up-to-date reports. Monday is chosen because Saturday's event reaches the mirror on Sunday.

Nothing has been installed or pushed yet. Those are your calls. To uninstall the Mac job, run `bash scheduling/install_launchd.sh --remove`.

---

## Part 3: Testing honestly

### The leak in the old pipeline

The old training data attached each fighter's **current** career averages to every past fight. Take a 2019 fight: the model saw striking numbers that included everything the fighter did from 2019 to 2026, *including that fight*. For a newcomer with three UFC fights, a third of their "career stats" is the fight being predicted. That is why the old model scored 67–75%.

### The fix: point-in-time features

`scripts/features.py` replays every UFC fight in date order. Before each fight it freezes both fighters' stats as they stood that morning. Only afterwards does it add the result. Each fighter gets 32 measurements, and the model sees fighter A's value minus fighter B's:

- **Quality:** Elo rating (rises more for beating strong opponents), average opponent Elo over the whole career (strength of schedule), recent strength of schedule (weighted toward the last ~3 opponents), opponent-adjusted recent results (how much better or worse than Elo expected a fighter did lately), and win percentage.
- **Striking:** landed and absorbed per minute, accuracy, defense, net margin, and recent form weighted toward the last ~3 fights.
- **Grappling:** takedowns per 15 minutes, takedown accuracy and defense, submission attempts, and share of control time, both career and recent.
- **Power and durability:** knockdowns scored and absorbed per 15 minutes, finishing rate, KO/TKO losses, and times finished.
- **Context:** age, years past 32, height, reach, layoff in days, UFC fights, cage minutes, and title-fight experience.

Small samples are pulled toward the UFC average. A debut fighter who landed 9 strikes in a 1-minute win is not treated as a 9.0 SLpM fighter.

### Walk-forward results

For each year from 2012 to 2026, a model was trained only on fights before that year and then predicted the whole year. That gives 7,049 fights, all predicted without seeing the future.

| Model | Accuracy | Log loss (lower is better) | Brier (lower is better) |
|---|---|---|---|
| Elo rating alone | 56.6% | 0.681 | 0.244 |
| Logistic regression | 61.4% | 0.654 | 0.231 |
| Boosted trees | 61.3% | 0.655 | 0.232 |
| **Blend of both (production model)** | **62.3%** | **0.652** | **0.230** |
| _Old career-stats method (leaky)_ | _66.2%_ | _0.607_ | _0.210_ |

| Subset | Blend accuracy | Old leaky method |
|---|---|---|
| All fights 2012–2026 | 62.3% | 66.2% |
| Both fighters with 3+ UFC fights | 63.7% | 63.1% |
| 2024 to today | 64.4% | 69.7% |

The leaky method's advantage disappears for experienced fighters, where the honest model is now slightly better. Their career totals are barely affected by any single fight. That pattern is the fingerprint of leakage rather than real skill.

For context, published research and betting-market favourites typically land in the 60–70% range on UFC fights. A data-only model at about 62% honest is in the normal range.

### Can you trust the percentages? (calibration)

| Model says the favourite has | Fights | Favourite actually won |
|---|---|---|
| 50–55% | 1,863 | 55.4% |
| 55–60% | 1,596 | 56.9% |
| 60–65% | 1,351 | 62.7% |
| 65–70% | 992 | 68.3% |
| 70–75% | 666 | 71.5% |
| 75–80% | 350 | 74.3% |
| 80%+ | 231 | 81.4% |

When the model says 65%, it means 65%. The only drift is in the 75–80% band, where it is about 3 points overconfident.

---

## Part 4: What a "true win" is

### What decides a UFC decision

A judge model (`scripts/win_anatomy.py`) was trained on every UFC decision that has full stats. It learns how much each in-fight stat moves the judges. Its weights translate into "significant strikes of value" on the scorecards:

| In-fight event | Worth about this many significant strikes |
|---|---|
| 1 knockdown | 16 |
| 1 submission attempt | 5 |
| 1 minute of control time | 5 |
| 1 round won on strikes (out-landing that round) | 4 |
| 1 takedown | 3 |
| 1 landed head strike | 1.7 (counts on top of the strike itself) |

In UFC decisions:
- The winner landed more significant strikes **78%** of the time, and the loser out-landed the winner 21% of the time.
- The winner out-landed the opponent in more rounds **76%** of the time.
- The winner had more control time **66%** of the time.
- The winner landed more takedowns **54%** of the time.

### Grading every win

Using that judge model, every UFC win is graded. Decisions are graded out-of-fold, so a fight never grades itself.

| Win type | Meaning | Share of all UFC wins |
|---|---|---|
| Dominant finish | Finished while also ahead on the stats | 40.1% |
| Clear win | Decision; stats back the winner 85%+ | 26.7% |
| Competitive win | Decision; stats back the winner 60–85% | 10.4% |
| Quick finish | Over in under 90 seconds, too short to judge | 7.4% |
| Comeback finish | Finished while *behind* on the stats | 5.8% |
| Contested decision | Stats favoured the loser (under 40%) | 5.0% |
| Coin-flip decision | Stats nearly even (40–60%) | 4.4% |
| Technical | DQ, overturned, could not continue | 0.3% |

Each win also gets a **route**: striking, grappling, or mixed. Ground-and-pound finishes count toward grappling when takedowns and control created them.

### Where the predictor is reliable

These are honest walk-forward predictions for every fight since 2012, split by how the fight was actually won:

| How the fight was won | Fights | Model accuracy |
|---|---|---|
| Clear win | 1,921 | **69.8%** |
| Dominant finish | 2,733 | 64.8% |
| Quick finish | 462 | 61.7% |
| Competitive win | 795 | 61.3% |
| Coin-flip decision | 347 | 46.4% |
| Comeback finish | 382 | 44.8% |
| Contested decision | 391 | 43.0% |

About **15% of UFC results** (coin-flips, contested decisions and comebacks) are below 50% for any pre-fight model. In those fights, the fighter who was "supposed to" win often did win the fight on the numbers, and the official result went the other way. On genuine wins, the model is right about **66%** of the time.

**Experiment:** I also tried training on "true wins" instead of official results. One version dropped contested decisions, and another used the judge model's probability as a soft label. Accuracy was unchanged (61.6–61.8%), so the production model keeps official results as the target. The useful output is the grading itself, which explains each miss.

---

## Part 5: Backtest on past fights

`scripts/backtest.py` retrains the model separately before every spotlight fight date, using only earlier fights. It covers all 116 of: every Adesanya and Shara Magomedov UFC fight, plus every main event and title fight since January 2025.

**Spotlight record: 72 of 116 (62%)**

| Verdict | Fights | What it means |
|---|---|---|
| Right for the right reasons | 30 | Model expected a striking or grappling edge, and that is how the fight was won |
| Right, on overall profile | 39 | Model backed the winner on quality, age, experience and form rather than a specific style edge |
| Right winner, different route | 3 | Correct pick, but the fight was won another way |
| Wrong: misread the matchup | 20 | A genuine miss; the winner won clearly |
| Wrong on a toss-up | 12 | Model said about 50/50 and leaned the wrong way |
| Wrong on a fight-changing moment | 7 | Comeback or quick finish |
| Wrong, but razor-close | 5 | Decision the stats call even or contested |

### Israel Adesanya: 14 of 19 called correctly

"Model" is Adesanya's pre-fight win probability. ✅ means the model's pick won.

| Date | Opponent | Result | Model | Win type | Verdict |
|---|---|---|---|---|---|
| 2018-02 | Rob Wilkinson | W KO/TKO | 59% ✅ | Dominant finish | Right for the right reasons |
| 2018-04 | Marvin Vettori | W Split dec. | 34% ❌ | Coin-flip decision | Wrong, but razor-close |
| 2018-07 | Brad Tavares | W Unanimous | 43% ❌ | Clear win | Misread (debut-era data was thin) |
| 2018-11 | Derek Brunson | W KO/TKO | 63% ✅ | Dominant finish | Right for the right reasons |
| 2019-02 | Anderson Silva | W Unanimous | 76% ✅ | Clear win | Right, on profile |
| 2019-04 | Kelvin Gastelum | W Unanimous | 57% ✅ | Clear win | Right for the right reasons |
| 2019-10 | Robert Whittaker | W KO/TKO | 55% ✅ | Dominant finish | Right for the right reasons |
| 2020-03 | Yoel Romero | W Unanimous | 81% ✅ | Competitive win | Right, on profile |
| 2020-09 | Paulo Costa | W KO/TKO | 80% ✅ | Dominant finish | Right, on profile |
| 2021-03 | Jan Blachowicz | L Unanimous | 82% ❌ | Clear win (mixed) | Misread; a move up to light heavyweight is not in the features |
| 2021-06 | Marvin Vettori | W Unanimous | 55% ✅ | Competitive win | Right, on profile |
| 2022-02 | Robert Whittaker | W Unanimous | 56% ✅ | Competitive win | Right for the right reasons |
| 2022-07 | Jared Cannonier | W Unanimous | 81% ✅ | Clear win | Right, on profile |
| 2022-11 | Alex Pereira | L KO/TKO | 69% ❌ | Comeback finish | Wrong on a fight-changing moment |
| 2023-04 | Alex Pereira | W KO/TKO | 61% ✅ | Dominant finish | Right, on profile |
| 2023-09 | Sean Strickland | L Unanimous | 64% ❌ | Clear win | Misread |
| 2024-08 | Dricus Du Plessis | L Submission | 34% ✅ | Dominant finish (grappling) | Right, on profile |
| 2025-02 | Nassourdine Imavov | L KO/TKO | 39% ✅ | Dominant finish | Right, on profile |
| 2026-03 | Joe Pyfer | L KO/TKO | 45% ✅ | Dominant finish (grappling) | Right, on profile |

**What this shows about Adesanya:** during his title run the model favoured him on strength of schedule, Elo, his 203 cm reach, a sturdy chin, striking defense, and often older opponents (Silva, Romero, Cannonier). From 2024 on, it turned against him in every fight, and it was right each time.

The factors that flipped it were his age past 32 and his accumulated cage time. The model treats 300+ UFC minutes as wear, not as an asset. His long layoffs, fading recent striking form, and opponents with wrestling (Du Plessis) or momentum added to that.

His one big edge never went away. He has faced tougher opposition than almost anyone, and that stayed one of his largest factors, but it was no longer enough. The Pyfer loss shows the pattern clearly. Adesanya out-landed Pyfer 42–36, but Pyfer won through 2 takedowns and 2:44 of control, then finished him with punches from mount.

The model's misses on Adesanya are also instructive. Against Strickland, it saw Strickland's better recent form and wrestling but let Adesanya's strength of schedule win out. Against Blachowicz, a move up to light heavyweight is not something the features capture.

### Shara Magomedov: 5 of 7 called correctly

| Date | Opponent | Result | Model | Win type | Verdict |
|---|---|---|---|---|---|
| 2023-10 | Bruno Silva | W Unanimous | 49% ❌ | Competitive win | Wrong on a toss-up |
| 2024-06 | Antonio Trocoli | W KO/TKO | 60% ✅ | Dominant finish | Right for the right reasons |
| 2024-08 | Michal Oleksiejczuk | W Unanimous | 51% ✅ | Competitive win | Right for the right reasons |
| 2024-10 | Armen Petrosyan | W KO/TKO | 62% ✅ | Dominant finish | Right, on profile |
| 2025-02 | Michael Page | L Unanimous | 56% ❌ | Competitive win | Misread; Page's reach and strength of schedule were real |
| 2025-07 | Marc-Andre Barriault | W Unanimous | 68% ✅ | Clear win | Right for the right reasons |
| 2026-06 | Michel Pereira | W Unanimous | 53% ✅ | Coin-flip decision | Right, though the stats call it nearly even |

**What this shows about Shara:** his wins come from striking volume and pressure. He has attempted one takedown in his whole UFC career. His one loss came against an older, longer, elusive striker with a stronger schedule, which is a profile with obvious parallels to Adesanya.

The full fight-by-fight write-ups are in `reports/backtest_report.md`. For each fight they list the factors that pushed toward each fighter (with numbers), each fighter's stat line in the cage, why the winner won, what the loser did, and the verdict.

---

## Update: recent schedule and opponent-adjusted results

**Why:** fighters aged 35+ on a 2+ fight losing streak, with a 100+ Elo schedule edge over their opponent, won less often than the model predicted. Adesanya fits that profile. The suspected cause was that strength of schedule averaged a whole career, so old title-run opponents kept full weight.

**What was added:**
- **Recent strength of schedule:** the average Elo of recent opponents, weighted so a fight three bouts ago counts half.
- **Opponent-adjusted recent results:** each fight scores the result minus what Elo expected, with the same weighting. Losing to a champion costs little; losing to a much lower-rated opponent costs a lot.

**Test:** each version was run through the same 2012–2026 walk-forward test and kept only if accuracy rose or held.

| Version | Accuracy | Since 2024 | Log loss |
|---|---|---|---|
| Model before the update | 61.63% | 63.3% | 0.6521 |
| + recent schedule | 62.12% | 64.4% | 0.6517 |
| + opponent-adjusted results | 61.92% | 64.0% | 0.6515 |
| **+ both (now live)** | **62.28%** | **64.4%** | **0.6515** |
| + both, career schedule removed | 62.01% | 64.1% | 0.6519 |
| + both, older "recent results" removed | 61.99% | 64.4% | 0.6518 |

Both features are live. The spotlight set moved from 73 to 72 of 116. Nine of its fights flipped, four to right and five to wrong, and all nine sat between 49% and 56%. That is coin-flip noise inside the larger test, which gained 0.65 points.

**What it did not fix:** the 30 fights matching the Adesanya profile are still overrated. The model now predicts 44% for them against 30% actual, almost the same as before. His recent opponents (Strickland, Du Plessis, Imavov, Pyfer) were strong too, so recent schedule stays high for him. Adesanya vs Shara moved only from 56.9% to 56.4%. Letting age shrink the schedule credit is the remaining idea for that group.

**Reading the explanations:** the model's "recent results", "opponent-adjusted results" and "win/loss streak" factors overlap heavily. The model splits credit between them, so one can show a push in an unexpected direction while another offsets it. For Adesanya vs Shara, "recent results" shows about +12 points for Adesanya and opponent-adjusted results about −8.5. Read related factors together. Here the results factors net out near zero and the two schedule factors give him about +14.

## How to use it

```bash
pip install -r requirements.txt
python3 scripts/update_data.py --full                      # refresh everything
python3 scripts/backtest.py --fighter "Israel Adesanya"    # backtest any fighter(s)
python3 scripts/predict_fight.py "Israel Adesanya" "Shara Magomedov" --date 2026-12-05
bash scheduling/install_launchd.sh                         # weekly auto-refresh on this Mac
```

## Known limits

- **What the model can't see:** injuries, camp changes, weight cuts, short-notice replacements and betting odds. Adding historical odds would be the biggest single accuracy upgrade available.
- **Weight-class moves:** they are not modelled directly. This explains the Adesanya vs Blachowicz miss.
- **One data dependency:** everything relies on the mirror. If it stops updating, `update_data.py --check` will show the data going stale, and option B in Part 1 is the fallback.
- **Mirror licence:** the mirror's code is GPL-3.0. We only download its published data files and do not copy its code.
- **Legacy scripts:** `data_cleaning.py`, `generate_matchups.py` and `scraper.py` are no longer used, and the old career-stats files in `data/processed/` are not read anymore.
