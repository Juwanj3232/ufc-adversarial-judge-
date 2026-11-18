# Backtest report: past fights, predicted honestly and explained

_Generated 2026-11-18 14:58. Every spotlight prediction below was made by a model trained only on fights before that date, using stats as they stood that morning._

## Spotlight scorecard

**72 of 116 correct (62%).**

| verdict | fights |
|---|---|
| Right, on overall profile | 39 |
| Right for the right reasons | 30 |
| Wrong: the model misread the matchup | 20 |
| Wrong on a toss-up | 12 |
| Wrong on a fight-changing moment | 7 |
| Wrong, but the result was razor-close | 5 |
| Right winner, different route | 3 |


## What actually wins a UFC fight

A judge model was trained on every UFC decision with full stats. Its weights, expressed as "how many significant strikes is this worth on the scorecards":

| stat | worth_in_sig_strikes |
|---|---|
| Significant strikes landed | 1.0 |
| Knockdowns | 15.9 |
| Takedowns landed | 3.0 |
| Control time (minutes) | 5.0 |
| Submission attempts | 5.2 |
| Rounds won on significant strikes | 3.7 |
| Head strikes landed | 0.7 |

_Head strikes are counted on top of the significant-strike total, so a landed head strike is worth about 1.7 body or leg strikes._

| In decisions, the winner... | share_of_decisions | loser_had_more |
|---|---|---|
| landed more significant strikes | 77.7% | 21.0% |
| scored more knockdowns | 12.8% | 5.2% |
| landed more takedowns | 54.1% | 24.0% |
| had more control time | 66.2% | 30.8% |
| out-landed the opponent in more rounds | 75.5% | 20.2% |

How all UFC wins break down:

| win type | share of all wins |
|---|---|
| Dominant finish | 40.1% |
| Clear win | 26.7% |
| Competitive win | 10.4% |
| Quick finish | 7.4% |
| Comeback finish | 5.8% |
| Contested decision | 5.0% |
| Coin-flip decision | 4.4% |
| Technical result | 0.3% |

## Where the model is reliable (every fight since 2012, walk-forward)

| win_type | fights | model_accuracy | avg_confidence |
|---|---|---|---|
| Dominant finish | 2733 | 64.8% | 62.1% |
| Clear win | 1921 | 69.8% | 62.3% |
| Competitive win | 795 | 61.3% | 60.7% |
| Quick finish | 462 | 61.7% | 61.7% |
| Contested decision | 391 | 43.0% | 60.2% |
| Comeback finish | 382 | 44.8% | 61.1% |
| Coin-flip decision | 347 | 46.4% | 60.3% |
| Technical result | 18 | 33.3% | 59.5% |

By model confidence:

| conf_band | fights | model_accuracy |
|---|---|---|
| 50-55% | 1863 | 55.4% |
| 55-60% | 1596 | 56.9% |
| 60-65% | 1351 | 62.7% |
| 65-70% | 992 | 68.3% |
| 70%+ | 1247 | 74.1% |

## Fight by fight

### 2018-02-10 · Rob Wilkinson vs Israel Adesanya
_UFC 221: Romero vs. Rockhold · Middleweight Bout_

- **Result:** Israel Adesanya by KO/TKO (R2 3:37). **Win type:** Dominant finish via striking; stats support for the winner 83%.
- **Model before the fight** (trained on 4,436 earlier fights): Rob Wilkinson 41% / Israel Adesanya 59%. Picked Israel Adesanya ✅
- **Pushing toward Rob Wilkinson** (their number first): Recent results (last ~3 fights) (25% vs 50%, ≈4.7 pts); Age (26.0 vs 28.6, ≈3.6 pts); Takedowns landed / 15 min (2.34 vs 1.62, ≈2.7 pts); Recent strength of schedule (last ~3 opponents) (1516.59 vs 1500.00, ≈1.8 pts)
- **Pushing toward Israel Adesanya** (their number first): Chin risk (KD absorbed / 15 min) (0.32 vs 2.15, ≈9.3 pts); Recent striking form (last ~3 fights) (0.00 vs -0.82, ≈4.6 pts); Striking defense (57% vs 51%, ≈2.4 pts); UFC win percentage (50% vs 33%, ≈1.7 pts)
- **In the cage, Rob Wilkinson:** 22 of 46 sig. strikes (opponent 52); 0 knockdown(s) scored, 1 suffered; 3/15 takedowns; 4:07 control; out-landed opponent in 1 round(s)
- **In the cage, Israel Adesanya:** 52 of 75 sig. strikes (opponent 22); 1 knockdown(s) scored, 0 suffered; 0/0 takedowns; out-landed opponent in 1 round(s)
- **Why Israel Adesanya won:** Israel Adesanya was winning the fight (significant strikes 52-22, knockdowns 1-0) and finished it: KO/TKO (Punches to Head At Distance), R2 3:37.
- **Rob Wilkinson:** Rob Wilkinson had real success (takedowns 3-0, control time (min) 4.1-0.0) but was finished.
- **Verdict: Right for the right reasons.** The model expected Israel Adesanya to have the striking edge, and that is how the fight was won (striking).

### 2018-04-14 · Israel Adesanya vs Marvin Vettori
_UFC Fight Night: Poirier vs. Gaethje · Middleweight Bout_

- **Result:** Israel Adesanya by Decision - Split (R3 5:00). **Win type:** Coin-flip decision via striking; stats support for the winner 59%.
- **Model before the fight** (trained on 4,503 earlier fights): Israel Adesanya 34% / Marvin Vettori 66%. Picked Marvin Vettori ❌
- **Pushing toward Israel Adesanya** (their number first): Reach (203 cm vs 188 cm, ≈2.6 pts); Recent striking form (last ~3 fights) (1.27 vs 0.61, ≈2.5 pts); Finishing rate (65% vs 26%, ≈1.5 pts); Striking accuracy (57% vs 43%, ≈1.2 pts)
- **Pushing toward Marvin Vettori** (their number first): Recent strength of schedule (last ~3 opponents) (1525.71 vs 1482.63, ≈7.5 pts); Age (24.6 vs 28.7, ≈4.7 pts); Striking defense (67% vs 55%, ≈4.2 pts); Recent results (last ~3 fights) (58% vs 75%, ≈2.9 pts)
- **In the cage, Israel Adesanya:** 57 of 123 sig. strikes (opponent 46); 0/1 takedowns; out-landed opponent in 2 round(s)
- **In the cage, Marvin Vettori:** 46 of 154 sig. strikes (opponent 57); 2/6 takedowns; 3:19 control; out-landed opponent in 1 round(s)
- **Why Israel Adesanya won:** Israel Adesanya got the nod in a fight the stats call nearly even (Israel Adesanya: significant strikes 57-46; Marvin Vettori: takedowns 2-0, control time (min) 3.3-0.0).
- **Marvin Vettori:** Marvin Vettori had real success (takedowns 2-0, control time (min) 3.3-0.0) but it was not enough on the scorecards.
- **Verdict: Wrong, but the result was razor-close.** The in-fight stats only gave Israel Adesanya a 59% case for the decision. The model's pick was arguably as deserving as the official winner.

### 2018-07-06 · Brad Tavares vs Israel Adesanya
_The Ultimate Fighter: Undefeated Finale · Middleweight Bout_

- **Result:** Israel Adesanya by Decision - Unanimous (R5 5:00). **Win type:** Clear win via striking; stats support for the winner 99%.
- **Model before the fight** (trained on 4,602 earlier fights): Brad Tavares 57% / Israel Adesanya 43%. Picked Brad Tavares ❌
- **Pushing toward Brad Tavares** (their number first): Recent strength of schedule (last ~3 opponents) (1574.21 vs 1504.54, ≈9.3 pts); Elo rating (quality of wins) (1697 vs 1567, ≈4.5 pts); UFC experience (fights) (16 vs 2, ≈3.6 pts); Takedowns landed / 15 min (1.13 vs 0.63, ≈2.6 pts)
- **Pushing toward Israel Adesanya** (their number first): Reach (203 cm vs 188 cm, ≈3.4 pts); Striking defense (64% vs 57%, ≈2.3 pts); UFC cage time (minutes) (24 vs 206, ≈2.0 pts); Chin risk (KD absorbed / 15 min) (0.12 vs 0.29, ≈2.0 pts)
- **In the cage, Brad Tavares:** 40 of 174 sig. strikes (opponent 119); 1/12 takedowns; 2:05 control; out-landed opponent in 0 round(s)
- **In the cage, Israel Adesanya:** 119 of 215 sig. strikes (opponent 40); 0/2 takedowns; 1:46 control; 1 submission attempt(s); out-landed opponent in 5 round(s)
- **Why Israel Adesanya won:** Israel Adesanya won the fight on the numbers and the cards agreed: led significant strikes 119-40.
- **Brad Tavares:** Brad Tavares had real success (takedowns 1-0, control time (min) 2.1-1.8) but it was not enough on the scorecards.
- **Verdict: Wrong: the model misread the matchup.** The model's main reasons pointed to Brad Tavares, but Israel Adesanya won a clear win via striking (stats support 99%), so this was a genuine miss rather than bad luck.

### 2018-11-03 · Derek Brunson vs Israel Adesanya
_UFC 230: Cormier vs. Lewis · Middleweight Bout_

- **Result:** Israel Adesanya by KO/TKO (R1 4:51). **Win type:** Dominant finish via striking; stats support for the winner 93%.
- **Model before the fight** (trained on 4,752 earlier fights): Derek Brunson 37% / Israel Adesanya 63%. Picked Israel Adesanya ✅
- **Pushing toward Derek Brunson** (their number first): Recent strength of schedule (last ~3 opponents) (1623.20 vs 1560.56, ≈8.4 pts); Recent results (last ~3 fights) (55% vs 85%, ≈5.8 pts); Recent grappling control (74% vs 30%, ≈5.0 pts); Takedowns landed / 15 min (2.35 vs 0.38, ≈4.5 pts)
- **Pushing toward Israel Adesanya** (their number first): Striking defense (69% vs 51%, ≈6.9 pts); Age (29.3 vs 34.8, ≈6.1 pts); Recent striking form (last ~3 fights) (1.86 vs 0.51, ≈5.0 pts); Chin risk (KD absorbed / 15 min) (0.07 vs 0.37, ≈4.5 pts)
- **In the cage, Derek Brunson:** 3 of 14 sig. strikes (opponent 13); 0 knockdown(s) scored, 3 suffered; 0/7 takedowns; 1:34 control; out-landed opponent in 0 round(s)
- **In the cage, Israel Adesanya:** 13 of 23 sig. strikes (opponent 3); 3 knockdown(s) scored, 0 suffered; 0/0 takedowns; 0:10 control; out-landed opponent in 1 round(s)
- **Why Israel Adesanya won:** Israel Adesanya was winning the fight (significant strikes 13-3, knockdowns 3-0) and finished it: KO/TKO (Punches to Head At Distance), R1 4:51.
- **Derek Brunson:** Derek Brunson had real success (control time (min) 1.6-0.2) but was finished.
- **Verdict: Right for the right reasons.** The model expected Israel Adesanya to have the striking edge, and that is how the fight was won (striking).

### 2019-02-09 · Israel Adesanya vs Anderson Silva
_UFC 234: Adesanya vs. Silva · Middleweight Bout_

- **Result:** Israel Adesanya by Decision - Unanimous (R3 5:00). **Win type:** Clear win via striking; stats support for the winner 93%.
- **Model before the fight** (trained on 4,886 earlier fights): Israel Adesanya 76% / Anderson Silva 24%. Picked Israel Adesanya ✅
- **Pushing toward Israel Adesanya** (their number first): Age (29.6 vs 43.8, ≈12.9 pts); Age past 32 (decline years) (0.0 vs 11.8, ≈6.3 pts); Recent striking form (last ~3 fights) (1.77 vs -0.29, ≈5.1 pts); Recent results vs expectation (opponent-adjusted) (0.43 vs -0.13, ≈3.5 pts)
- **Pushing toward Anderson Silva** (their number first): Recent strength of schedule (last ~3 opponents) (1648.02 vs 1585.48, ≈7.3 pts); Title fight experience (13 vs 0, ≈5.2 pts); Recent results (last ~3 fights) (51% vs 87%, ≈4.9 pts); Elo rating (quality of wins) (1757 vs 1656, ≈3.3 pts)
- **In the cage, Israel Adesanya:** 65 of 132 sig. strikes (opponent 31); out-landed opponent in 2 round(s)
- **In the cage, Anderson Silva:** 31 of 72 sig. strikes (opponent 65); out-landed opponent in 0 round(s)
- **Why Israel Adesanya won:** Israel Adesanya won the fight on the numbers and the cards agreed: led significant strikes 65-31.
- **Anderson Silva:** Anderson Silva did not win any of the main stat battles.
- **Verdict: Right, on overall profile.** The model backed Israel Adesanya mainly on overall profile (quality of opposition, age, experience, form) rather than a specific matchup edge, and Israel Adesanya won via striking.

### 2019-04-13 · Kelvin Gastelum vs Israel Adesanya
_UFC 236: Holloway vs. Poirier 2 · UFC Interim Middleweight Title Bout_

- **Result:** Israel Adesanya by Decision - Unanimous (R5 5:00). **Win type:** Clear win via striking; stats support for the winner 97%.
- **Model before the fight** (trained on 4,984 earlier fights): Kelvin Gastelum 43% / Israel Adesanya 57%. Picked Israel Adesanya ✅
- **Pushing toward Kelvin Gastelum** (their number first): Recent strength of schedule (last ~3 opponents) (1655.35 vs 1621.01, ≈5.3 pts); UFC experience (fights) (13 vs 5, ≈4.1 pts); Age (27.5 vs 29.7, ≈3.3 pts); Recent results (last ~3 fights) (71% vs 88%, ≈3.3 pts)
- **Pushing toward Israel Adesanya** (their number first): Recent striking form (last ~3 fights) (1.80 vs 0.50, ≈5.6 pts); Reach (203 cm vs 180 cm, ≈3.9 pts); Days since last fight (63 vs 336, ≈2.8 pts); Takedown accuracy (26% vs 47%, ≈2.7 pts)
- **In the cage, Kelvin Gastelum:** 91 of 220 sig. strikes (opponent 109); 0 knockdown(s) scored, 4 suffered; 1/9 takedowns; 1:21 control; out-landed opponent in 2 round(s)
- **In the cage, Israel Adesanya:** 109 of 237 sig. strikes (opponent 91); 4 knockdown(s) scored, 0 suffered; 0/0 takedowns; 0:42 control; 2 submission attempt(s); out-landed opponent in 3 round(s)
- **Why Israel Adesanya won:** Israel Adesanya won the fight on the numbers and the cards agreed: led significant strikes 109-91, knockdowns 4-0.
- **Kelvin Gastelum:** Kelvin Gastelum had real success (takedowns 1-0, control time (min) 1.4-0.7) but it was not enough on the scorecards.
- **Verdict: Right for the right reasons.** The model expected Israel Adesanya to have the striking edge, and that is how the fight was won (striking).

### 2019-10-05 · Robert Whittaker vs Israel Adesanya
_UFC 243: Whittaker vs. Adesanya · UFC Middleweight Title Bout_

- **Result:** Israel Adesanya by KO/TKO (R2 3:33). **Win type:** Dominant finish via striking; stats support for the winner 91%.
- **Model before the fight** (trained on 5,247 earlier fights): Robert Whittaker 45% / Israel Adesanya 55%. Picked Israel Adesanya ✅
- **Pushing toward Robert Whittaker** (their number first): UFC experience (fights) (13 vs 6, ≈4.4 pts); Recent strength of schedule (last ~3 opponents) (1668.02 vs 1644.19, ≈4.1 pts); Elo rating (quality of wins) (1831 vs 1734, ≈2.2 pts); Title fight experience (2 vs 1, ≈1.8 pts)
- **Pushing toward Israel Adesanya** (their number first): Reach (203 cm vs 185 cm, ≈3.6 pts); Days since last fight (175 vs 483, ≈3.1 pts); Takedown accuracy (25% vs 48%, ≈2.6 pts); Chin risk (KD absorbed / 15 min) (0.04 vs 0.37, ≈2.5 pts)
- **In the cage, Robert Whittaker:** 32 of 116 sig. strikes (opponent 40); 0 knockdown(s) scored, 2 suffered; out-landed opponent in 0 round(s)
- **In the cage, Israel Adesanya:** 40 of 95 sig. strikes (opponent 32); 2 knockdown(s) scored, 0 suffered; 0:04 control; out-landed opponent in 2 round(s)
- **Why Israel Adesanya won:** Israel Adesanya was winning the fight (significant strikes 40-32, knockdowns 2-0, control time (min) 0.1-0.0) and finished it: KO/TKO (Punch to Head At Distance), R2 3:33.
- **Robert Whittaker:** Robert Whittaker did not win any of the main stat battles. Was knocked down 2 time(s).
- **Verdict: Right for the right reasons.** The model expected Israel Adesanya to have the striking edge, and that is how the fight was won (striking).

### 2020-03-07 · Israel Adesanya vs Yoel Romero
_UFC 248: Adesanya vs. Romero · UFC Middleweight Title Bout_

- **Result:** Israel Adesanya by Decision - Unanimous (R5 5:00). **Win type:** Competitive win via striking; stats support for the winner 68%.
- **Model before the fight** (trained on 5,437 earlier fights): Israel Adesanya 81% / Yoel Romero 19%. Picked Israel Adesanya ✅
- **Pushing toward Israel Adesanya** (their number first): Age (30.6 vs 42.9, ≈6.8 pts); Age past 32 (decline years) (0.0 vs 10.9, ≈5.6 pts); Recent striking form (last ~3 fights) (1.26 vs 0.01, ≈3.8 pts); Recent results vs expectation (opponent-adjusted) (0.48 vs -0.04, ≈3.7 pts)
- **Pushing toward Yoel Romero** (their number first): Recent results (last ~3 fights) (50% vs 90%, ≈5.0 pts); Takedowns landed / 15 min (1.87 vs 0.20, ≈2.5 pts); UFC experience (fights) (12 vs 7, ≈1.8 pts); Recent grappling control (69% vs 35%, ≈1.7 pts)
- **In the cage, Israel Adesanya:** 48 of 132 sig. strikes (opponent 40); 0/0 takedowns; out-landed opponent in 3 round(s)
- **In the cage, Yoel Romero:** 40 of 89 sig. strikes (opponent 48); 0/3 takedowns; out-landed opponent in 2 round(s)
- **Why Israel Adesanya won:** Israel Adesanya edged it: led significant strikes 48-40.
- **Yoel Romero:** Yoel Romero did not win any of the main stat battles.
- **Verdict: Right, on overall profile.** The model backed Israel Adesanya mainly on overall profile (quality of opposition, age, experience, form) rather than a specific matchup edge, and Israel Adesanya won via striking.

### 2020-09-26 · Israel Adesanya vs Paulo Costa
_UFC 253: Adesanya vs. Costa · UFC Middleweight Title Bout_

- **Result:** Israel Adesanya by KO/TKO (R2 3:59). **Win type:** Dominant finish via striking; stats support for the winner 97%.
- **Model before the fight** (trained on 5,673 earlier fights): Israel Adesanya 80% / Paulo Costa 20%. Picked Israel Adesanya ✅
- **Pushing toward Israel Adesanya** (their number first): Recent strength of schedule (last ~3 opponents) (1678.73 vs 1586.26, ≈7.1 pts); Reach (203 cm vs 183 cm, ≈3.7 pts); Striking defense (65% vs 54%, ≈3.0 pts); Elo rating (quality of wins) (1809 vs 1687, ≈2.4 pts)
- **Pushing toward Paulo Costa** (their number first): Finishing rate (72% vs 37%, ≈1.5 pts); UFC cage time (minutes) (36 vs 127, ≈1.3 pts); Age (29.4 vs 31.2, ≈0.8 pts); Takedowns landed / 15 min (0.45 vs 0.16, ≈0.8 pts)
- **In the cage, Israel Adesanya:** 55 of 84 sig. strikes (opponent 12); 1 knockdown(s) scored, 0 suffered; 0:09 control; out-landed opponent in 2 round(s)
- **In the cage, Paulo Costa:** 12 of 26 sig. strikes (opponent 55); 0 knockdown(s) scored, 1 suffered; 0:01 control; out-landed opponent in 0 round(s)
- **Why Israel Adesanya won:** Israel Adesanya was winning the fight (significant strikes 55-12, knockdowns 1-0, control time (min) 0.1-0.0) and finished it: KO/TKO (Punch to Head At Distance), R2 3:59.
- **Paulo Costa:** Paulo Costa did not win any of the main stat battles. Was knocked down 1 time(s).
- **Verdict: Right, on overall profile.** The model backed Israel Adesanya mainly on overall profile (quality of opposition, age, experience, form) rather than a specific matchup edge, and Israel Adesanya won via striking.

### 2021-03-06 · Jan Blachowicz vs Israel Adesanya
_UFC 259: Blachowicz vs. Adesanya · UFC Light Heavyweight Title Bout_

- **Result:** Jan Blachowicz by Decision - Unanimous (R5 5:00). **Win type:** Clear win via mixed; stats support for the winner 100%.
- **Model before the fight** (trained on 5,887 earlier fights): Jan Blachowicz 18% / Israel Adesanya 82%. Picked Israel Adesanya ❌
- **Pushing toward Jan Blachowicz** (their number first): Takedowns landed / 15 min (1.13 vs 0.15, ≈1.6 pts); UFC experience (fights) (15 vs 9, ≈1.6 pts); Recent results (last ~3 fights) (78% vs 90%, ≈1.4 pts); Knockdown power (KD / 15 min) (0.49 vs 1.12, ≈0.1 pts)
- **Pushing toward Israel Adesanya** (their number first): Age (31.6 vs 38.0, ≈3.7 pts); Recent strength of schedule (last ~3 opponents) (1673.31 vs 1632.07, ≈3.6 pts); Age past 32 (decline years) (0.0 vs 6.0, ≈3.6 pts); Striking defense (65% vs 54%, ≈2.8 pts)
- **In the cage, Jan Blachowicz:** 107 of 193 sig. strikes (opponent 78); 3/5 takedowns; 7:06 control; out-landed opponent in 5 round(s)
- **In the cage, Israel Adesanya:** 78 of 161 sig. strikes (opponent 107); 0/0 takedowns; 0:01 control; out-landed opponent in 0 round(s)
- **Why Jan Blachowicz won:** Jan Blachowicz won the fight on the numbers and the cards agreed: led significant strikes 107-78, takedowns 3-0, control time (min) 7.1-0.0.
- **Israel Adesanya:** Israel Adesanya did not win any of the main stat battles.
- **Verdict: Wrong: the model misread the matchup.** The model's main reasons pointed to Israel Adesanya, but Jan Blachowicz won a clear win via mixed (stats support 100%), so this was a genuine miss rather than bad luck.

### 2021-06-12 · Israel Adesanya vs Marvin Vettori
_UFC 263: Adesanya vs. Vettori 2 · UFC Middleweight Title Bout_

- **Result:** Israel Adesanya by Decision - Unanimous (R5 5:00). **Win type:** Competitive win via striking; stats support for the winner 75%.
- **Model before the fight** (trained on 6,023 earlier fights): Israel Adesanya 55% / Marvin Vettori 45%. Picked Israel Adesanya ✅
- **Pushing toward Israel Adesanya** (their number first): Recent strength of schedule (last ~3 opponents) (1682.01 vs 1584.42, ≈8.8 pts); Elo rating (quality of wins) (1796 vs 1688, ≈4.0 pts); Reach (203 cm vs 188 cm, ≈3.8 pts); Takedown accuracy (25% vs 52%, ≈3.1 pts)
- **Pushing toward Marvin Vettori** (their number first): Takedowns landed / 15 min (2.16 vs 0.13, ≈5.7 pts); Recent grappling control (87% vs 22%, ≈5.0 pts); Age (27.7 vs 31.9, ≈4.6 pts); Recent striking form (last ~3 fights) (0.99 vs 0.61, ≈2.3 pts)
- **In the cage, Israel Adesanya:** 96 of 181 sig. strikes (opponent 58); 0/0 takedowns; 0:36 control; out-landed opponent in 5 round(s)
- **In the cage, Marvin Vettori:** 58 of 176 sig. strikes (opponent 96); 4/14 takedowns; 6:55 control; out-landed opponent in 0 round(s)
- **Why Israel Adesanya won:** Israel Adesanya edged it: led significant strikes 96-58, while Marvin Vettori took takedowns 4-0, control time (min) 6.9-0.6.
- **Marvin Vettori:** Marvin Vettori had real success (takedowns 4-0, control time (min) 6.9-0.6) but it was not enough on the scorecards.
- **Verdict: Right, on overall profile.** The model backed Israel Adesanya mainly on overall profile (quality of opposition, age, experience, form) rather than a specific matchup edge, and Israel Adesanya won via striking.

### 2022-02-12 · Israel Adesanya vs Robert Whittaker
_UFC 271: Adesanya vs. Whittaker 2 · UFC Middleweight Title Bout_

- **Result:** Israel Adesanya by Decision - Unanimous (R5 5:00). **Win type:** Competitive win via striking; stats support for the winner 74%.
- **Model before the fight** (trained on 6,341 earlier fights): Israel Adesanya 56% / Robert Whittaker 44%. Picked Israel Adesanya ✅
- **Pushing toward Israel Adesanya** (their number first): Reach (203 cm vs 185 cm, ≈4.7 pts); Chin risk (KD absorbed / 15 min) (0.02 vs 0.38, ≈3.1 pts); Recent strength of schedule (last ~3 opponents) (1676.21 vs 1651.18, ≈2.7 pts); Title fight experience (6 vs 3, ≈2.3 pts)
- **Pushing toward Robert Whittaker** (their number first): Recent grappling control (60% vs 18%, ≈2.8 pts); UFC experience (fights) (17 vs 11, ≈2.7 pts); Recent striking form (last ~3 fights) (1.53 vs 0.82, ≈2.4 pts); Takedowns landed / 15 min (0.69 vs 0.11, ≈2.1 pts)
- **In the cage, Israel Adesanya:** 79 of 169 sig. strikes (opponent 59); 1 knockdown(s) scored, 0 suffered; 0/0 takedowns; 0:01 control; out-landed opponent in 4 round(s)
- **In the cage, Robert Whittaker:** 59 of 136 sig. strikes (opponent 79); 0 knockdown(s) scored, 1 suffered; 4/10 takedowns; 3:40 control; out-landed opponent in 1 round(s)
- **Why Israel Adesanya won:** Israel Adesanya edged it: led significant strikes 79-59, knockdowns 1-0, while Robert Whittaker took takedowns 4-0, control time (min) 3.7-0.0.
- **Robert Whittaker:** Robert Whittaker had real success (takedowns 4-0, control time (min) 3.7-0.0) but it was not enough on the scorecards.
- **Verdict: Right for the right reasons.** The model expected Israel Adesanya to have the striking edge, and that is how the fight was won (striking).

### 2022-07-02 · Israel Adesanya vs Jared Cannonier
_UFC 276: Adesanya vs. Cannonier · UFC Middleweight Title Bout_

- **Result:** Israel Adesanya by Decision - Unanimous (R5 5:00). **Win type:** Clear win via striking; stats support for the winner 89%.
- **Model before the fight** (trained on 6,563 earlier fights): Israel Adesanya 81% / Jared Cannonier 19%. Picked Israel Adesanya ✅
- **Pushing toward Israel Adesanya** (their number first): Recent strength of schedule (last ~3 opponents) (1699.22 vs 1650.12, ≈4.0 pts); Age past 32 (decline years) (0.9 vs 6.3, ≈3.7 pts); Elo rating (quality of wins) (1852 vs 1710, ≈3.6 pts); Age (32.9 vs 38.3, ≈3.4 pts)
- **Pushing toward Jared Cannonier** (their number first): Recent results (last ~3 fights) (69% vs 80%, ≈1.4 pts); Takedowns landed / 15 min (0.36 vs 0.10, ≈0.8 pts); UFC cage time (minutes) (131 vs 211, ≈0.6 pts); UFC experience (fights) (13 vs 12, ≈0.4 pts)
- **In the cage, Israel Adesanya:** 116 of 230 sig. strikes (opponent 90); 0/0 takedowns; out-landed opponent in 4 round(s)
- **In the cage, Jared Cannonier:** 90 of 157 sig. strikes (opponent 116); 0/4 takedowns; 4:14 control; out-landed opponent in 0 round(s)
- **Why Israel Adesanya won:** Israel Adesanya won the fight on the numbers and the cards agreed: led significant strikes 116-90.
- **Jared Cannonier:** Jared Cannonier had real success (control time (min) 4.2-0.0) but it was not enough on the scorecards.
- **Verdict: Right, on overall profile.** The model backed Israel Adesanya mainly on overall profile (quality of opposition, age, experience, form) rather than a specific matchup edge, and Israel Adesanya won via striking.

### 2022-11-12 · Israel Adesanya vs Alex Pereira
_UFC 281: Adesanya vs. Pereira · UFC Middleweight Title Bout_

- **Result:** Alex Pereira by KO/TKO (R5 2:01). **Win type:** Comeback finish via striking; stats support for the winner 20%.
- **Model before the fight** (trained on 6,750 earlier fights): Israel Adesanya 69% / Alex Pereira 31%. Picked Israel Adesanya ❌
- **Pushing toward Israel Adesanya** (their number first): Elo rating (quality of wins) (1872 vs 1633, ≈7.3 pts); Recent strength of schedule (last ~3 opponents) (1693.83 vs 1600.60, ≈7.0 pts); UFC experience (fights) (13 vs 3, ≈3.4 pts); Title fight experience (8 vs 0, ≈3.0 pts)
- **Pushing toward Alex Pereira** (their number first): UFC cage time (minutes) (23 vs 236, ≈3.4 pts); Recent striking form (last ~3 fights) (1.64 vs 0.82, ≈3.1 pts); Recent results vs expectation (opponent-adjusted) (0.45 vs 0.27, ≈2.2 pts); Takedowns landed / 15 min (0.60 vs 0.09, ≈1.8 pts)
- **In the cage, Israel Adesanya:** 86 of 162 sig. strikes (opponent 91); 1/4 takedowns; 6:34 control; out-landed opponent in 3 round(s)
- **In the cage, Alex Pereira:** 91 of 157 sig. strikes (opponent 86); 1/1 takedowns; 0:31 control; out-landed opponent in 1 round(s)
- **Why Alex Pereira won:** Alex Pereira was behind (Israel Adesanya led control time (min) 6.6-0.5) but ended it with one decisive moment: KO/TKO (Punches to Head At Distance), R5 2:01.
- **Israel Adesanya:** Israel Adesanya had real success (control time (min) 6.6-0.5) but was finished.
- **Verdict: Wrong on a fight-changing moment.** Alex Pereira won with a comeback finish — a single moment that pre-fight averages cannot see coming.

### 2023-04-08 · Alex Pereira vs Israel Adesanya
_UFC 287: Pereira vs. Adesanya 2 · UFC Middleweight Title Bout_

- **Result:** Israel Adesanya by KO/TKO (R2 4:21). **Win type:** Dominant finish via striking; stats support for the winner 58%.
- **Model before the fight** (trained on 6,933 earlier fights): Alex Pereira 39% / Israel Adesanya 61%. Picked Israel Adesanya ✅
- **Pushing toward Alex Pereira** (their number first): Recent results vs expectation (opponent-adjusted) (0.51 vs 0.07, ≈6.5 pts); UFC cage time (minutes) (45 vs 258, ≈3.8 pts); Win / loss streak (+4 vs -1, ≈1.7 pts); Finishing rate (66% vs 29%, ≈1.7 pts)
- **Pushing toward Israel Adesanya** (their number first): Elo rating (quality of wins) (1810 vs 1695, ≈4.8 pts); UFC experience (fights) (14 vs 4, ≈4.2 pts); Recent results (last ~3 fights) (66% vs 87%, ≈3.9 pts); Title fight experience (9 vs 1, ≈2.9 pts)
- **In the cage, Alex Pereira:** 49 of 85 sig. strikes (opponent 41); 0 knockdown(s) scored, 1 suffered; out-landed opponent in 2 round(s)
- **In the cage, Israel Adesanya:** 41 of 96 sig. strikes (opponent 49); 1 knockdown(s) scored, 0 suffered; 0:03 control; out-landed opponent in 0 round(s)
- **Why Israel Adesanya won:** Israel Adesanya was winning the fight (knockdowns 1-0, control time (min) 0.1-0.0) and finished it: KO/TKO (Punch to Head At Distance), R2 4:21.
- **Alex Pereira:** Alex Pereira had real success (significant strikes 49-41) but was finished.
- **Verdict: Right, on overall profile.** The model backed Israel Adesanya mainly on overall profile (quality of opposition, age, experience, form) rather than a specific matchup edge, and Israel Adesanya won via striking.

### 2023-09-09 · Israel Adesanya vs Sean Strickland
_UFC 293: Adesanya vs. Strickland · UFC Middleweight Title Bout_

- **Result:** Sean Strickland by Decision - Unanimous (R5 5:00). **Win type:** Clear win via striking; stats support for the winner 99%.
- **Model before the fight** (trained on 7,185 earlier fights): Israel Adesanya 64% / Sean Strickland 36%. Picked Israel Adesanya ❌
- **Pushing toward Israel Adesanya** (their number first): Recent strength of schedule (last ~3 opponents) (1672.94 vs 1587.85, ≈7.0 pts); Elo rating (quality of wins) (1836 vs 1722, ≈4.6 pts); Takedown accuracy (25% vs 60%, ≈3.0 pts); Title fight experience (10 vs 0, ≈2.7 pts)
- **Pushing toward Sean Strickland** (their number first): Recent striking form (last ~3 fights) (1.59 vs 0.45, ≈3.4 pts); Takedowns landed / 15 min (1.03 vs 0.13, ≈2.4 pts); Recent grappling control (70% vs 39%, ≈2.2 pts); Striking defense (63% vs 57%, ≈1.9 pts)
- **In the cage, Israel Adesanya:** 94 of 271 sig. strikes (opponent 137); 0 knockdown(s) scored, 1 suffered; out-landed opponent in 2 round(s)
- **In the cage, Sean Strickland:** 137 of 259 sig. strikes (opponent 94); 1 knockdown(s) scored, 0 suffered; 0:14 control; out-landed opponent in 3 round(s)
- **Why Sean Strickland won:** Sean Strickland won the fight on the numbers and the cards agreed: led significant strikes 137-94, knockdowns 1-0, control time (min) 0.2-0.0.
- **Israel Adesanya:** Israel Adesanya did not win any of the main stat battles. Was knocked down 1 time(s).
- **Verdict: Wrong: the model misread the matchup.** The model's main reasons pointed to Israel Adesanya, but Sean Strickland won a clear win via striking (stats support 99%), so this was a genuine miss rather than bad luck.

### 2023-10-21 · Shara Magomedov vs Bruno Silva
_UFC 294: Makhachev vs. Volkanovski 2 · Middleweight Bout_

- **Result:** Shara Magomedov by Decision - Unanimous (R3 5:00). **Win type:** Competitive win via striking; stats support for the winner 78%.
- **Model before the fight** (trained on 7,237 earlier fights): Shara Magomedov 49% / Bruno Silva 51%. Picked Bruno Silva ❌
- **Pushing toward Shara Magomedov** (their number first): Age (29.4 vs 34.3, ≈5.1 pts); Striking defense (56% vs 49%, ≈2.8 pts); Age past 32 (decline years) (0.0 vs 2.3, ≈2.6 pts); Takedowns landed / 15 min (1.51 vs 0.77, ≈2.4 pts)
- **Pushing toward Bruno Silva** (their number first): Recent strength of schedule (last ~3 opponents) (1581.07 vs 1500.00, ≈7.9 pts); UFC experience (fights) (7 vs 0, ≈3.0 pts); Elo rating (quality of wins) (1555 vs 1500, ≈2.7 pts); Strength of schedule (avg opponent Elo) (1552 vs 1500, ≈1.7 pts)
- **In the cage, Shara Magomedov:** 113 of 154 sig. strikes (opponent 65); 0/0 takedowns; out-landed opponent in 3 round(s)
- **In the cage, Bruno Silva:** 65 of 91 sig. strikes (opponent 113); 3/7 takedowns; 6:44 control; out-landed opponent in 0 round(s)
- **Why Shara Magomedov won:** Shara Magomedov edged it: led significant strikes 113-65, while Bruno Silva took takedowns 3-0, control time (min) 6.7-0.0.
- **Bruno Silva:** Bruno Silva had real success (takedowns 3-0, control time (min) 6.7-0.0) but it was not enough on the scorecards.
- **Verdict: Wrong on a toss-up.** The model saw this as close to 50/50 and leaned the wrong way.

### 2024-06-22 · Shara Magomedov vs Antonio Trocoli
_UFC Fight Night: Whittaker vs. Aliskerov · Middleweight Bout_

- **Result:** Shara Magomedov by KO/TKO (R3 2:27). **Win type:** Dominant finish via striking; stats support for the winner 98%.
- **Model before the fight** (trained on 7,564 earlier fights): Shara Magomedov 60% / Antonio Trocoli 40%. Picked Shara Magomedov ✅
- **Pushing toward Shara Magomedov** (their number first): Recent results vs expectation (opponent-adjusted) (0.29 vs 0.00, ≈4.1 pts); Age (30.1 vs 33.5, ≈3.5 pts); Recent striking form (last ~3 fights) (1.60 vs 0.00, ≈3.2 pts); Recent strength of schedule (last ~3 opponents) (1527.31 vs 1500.00, ≈2.8 pts)
- **Pushing toward Antonio Trocoli** (their number first): Striking defense (56% vs 39%, ≈5.3 pts); Recent results (last ~3 fights) (50% vs 75%, ≈4.8 pts); Reach (201 cm vs 185 cm, ≈3.3 pts); Recent grappling control (50% vs 21%, ≈2.1 pts)
- **In the cage, Shara Magomedov:** 82 of 108 sig. strikes (opponent 16); 1 knockdown(s) scored, 0 suffered; 0/0 takedowns; 0:17 control; out-landed opponent in 3 round(s)
- **In the cage, Antonio Trocoli:** 16 of 34 sig. strikes (opponent 82); 0 knockdown(s) scored, 1 suffered; 0/7 takedowns; 4:42 control; out-landed opponent in 0 round(s)
- **Why Shara Magomedov won:** Shara Magomedov was winning the fight (significant strikes 82-16, knockdowns 1-0) and finished it: KO/TKO (Punches to Head At Distance), R3 2:27.
- **Antonio Trocoli:** Antonio Trocoli had real success (control time (min) 4.7-0.3) but was finished.
- **Verdict: Right for the right reasons.** The model expected Shara Magomedov to have the striking edge, and that is how the fight was won (striking).

### 2024-08-03 · Shara Magomedov vs Michal Oleksiejczuk
_UFC Fight Night: Sandhagen vs. Nurmagomedov · Middleweight Bout_

- **Result:** Shara Magomedov by Decision - Unanimous (R3 5:00). **Win type:** Competitive win via striking; stats support for the winner 73%.
- **Model before the fight** (trained on 7,624 earlier fights): Shara Magomedov 51% / Michal Oleksiejczuk 49%. Picked Shara Magomedov ✅
- **Pushing toward Shara Magomedov** (their number first): Times finished (0 vs 5, ≈5.7 pts); Recent results vs expectation (opponent-adjusted) (0.32 vs -0.07, ≈5.6 pts); Recent striking form (last ~3 fights) (2.65 vs 0.28, ≈4.0 pts); Net striking margin (landed - absorbed / min) (2.69 vs 0.67, ≈3.3 pts)
- **Pushing toward Michal Oleksiejczuk** (their number first): Recent results (last ~3 fights) (42% vs 82%, ≈7.9 pts); Striking defense (61% vs 42%, ≈5.8 pts); Recent strength of schedule (last ~3 opponents) (1563.04 vs 1515.52, ≈5.2 pts); UFC experience (fights) (13 vs 2, ≈3.9 pts)
- **In the cage, Shara Magomedov:** 97 of 178 sig. strikes (opponent 77); 0/0 takedowns; out-landed opponent in 3 round(s)
- **In the cage, Michal Oleksiejczuk:** 77 of 146 sig. strikes (opponent 97); 3/7 takedowns; 2:39 control; out-landed opponent in 0 round(s)
- **Why Shara Magomedov won:** Shara Magomedov edged it: led significant strikes 97-77, while Michal Oleksiejczuk took takedowns 3-0, control time (min) 2.6-0.0.
- **Michal Oleksiejczuk:** Michal Oleksiejczuk had real success (takedowns 3-0, control time (min) 2.6-0.0) but it was not enough on the scorecards.
- **Verdict: Right for the right reasons.** The model expected Shara Magomedov to have the striking edge, and that is how the fight was won (striking).

### 2024-08-17 · Dricus Du Plessis vs Israel Adesanya
_UFC 305: Du Plessis vs. Adesanya · UFC Middleweight Title Bout_

- **Result:** Dricus Du Plessis by Submission (R4 3:38). **Win type:** Dominant finish via grappling; stats support for the winner 77%.
- **Model before the fight** (trained on 7,647 earlier fights): Dricus Du Plessis 66% / Israel Adesanya 34%. Picked Dricus Du Plessis ✅
- **Pushing toward Dricus Du Plessis** (their number first): Win / loss streak (+7 vs -1, ≈6.1 pts); Recent results vs expectation (opponent-adjusted) (0.45 vs -0.03, ≈6.1 pts); Takedowns landed / 15 min (2.76 vs 0.12, ≈6.1 pts); Age (30.6 vs 35.1, ≈4.0 pts)
- **Pushing toward Israel Adesanya** (their number first): Recent results (last ~3 fights) (58% vs 90%, ≈5.4 pts); UFC experience (fights) (16 vs 7, ≈2.8 pts); Title fight experience (11 vs 1, ≈2.4 pts); Takedown accuracy (25% vs 49%, ≈2.3 pts)
- **In the cage, Dricus Du Plessis:** 90 of 197 sig. strikes (opponent 97); 4/9 takedowns; 3:39 control; 2 submission attempt(s); out-landed opponent in 1 round(s)
- **In the cage, Israel Adesanya:** 97 of 203 sig. strikes (opponent 90); 0/1 takedowns; 0:09 control; out-landed opponent in 2 round(s)
- **Why Dricus Du Plessis won:** Dricus Du Plessis was winning the fight (takedowns 4-0, control time (min) 3.6-0.1) and finished it: Submission (Rear Naked Choke), R4 3:38.
- **Israel Adesanya:** Israel Adesanya had real success (significant strikes 97-90) but was finished.
- **Verdict: Right, on overall profile.** The model backed Dricus Du Plessis mainly on overall profile (quality of opposition, age, experience, form) rather than a specific matchup edge, and Dricus Du Plessis won via grappling.

### 2024-10-26 · Shara Magomedov vs Armen Petrosyan
_UFC 308: Topuria vs. Holloway · Middleweight Bout_

- **Result:** Shara Magomedov by KO/TKO (R2 4:52). **Win type:** Dominant finish via striking; stats support for the winner 54%.
- **Model before the fight** (trained on 7,741 earlier fights): Shara Magomedov 62% / Armen Petrosyan 38%. Picked Shara Magomedov ✅
- **Pushing toward Shara Magomedov** (their number first): Recent results vs expectation (opponent-adjusted) (0.34 vs 0.04, ≈4.4 pts); Age (30.4 vs 34.0, ≈3.6 pts); Elo rating (quality of wins) (1600 vs 1528, ≈2.6 pts); Takedown defense (69% vs 38%, ≈2.1 pts)
- **Pushing toward Armen Petrosyan** (their number first): Recent results (last ~3 fights) (54% vs 85%, ≈6.2 pts); Striking defense (56% vs 44%, ≈3.4 pts); Recent grappling control (32% vs 17%, ≈1.0 pts); UFC experience (fights) (5 vs 3, ≈0.7 pts)
- **In the cage, Shara Magomedov:** 65 of 106 sig. strikes (opponent 77); 1 knockdown(s) scored, 0 suffered; 0:02 control; out-landed opponent in 1 round(s)
- **In the cage, Armen Petrosyan:** 77 of 140 sig. strikes (opponent 65); 0 knockdown(s) scored, 1 suffered; 0:21 control; out-landed opponent in 1 round(s)
- **Why Shara Magomedov won:** Shara Magomedov was winning the fight (knockdowns 1-0) and finished it: KO/TKO (Spinning Back Fist Head), R2 4:52.
- **Armen Petrosyan:** Armen Petrosyan had real success (significant strikes 77-65, control time (min) 0.3-0.0) but was finished.
- **Verdict: Right, on overall profile.** The model backed Shara Magomedov mainly on overall profile (quality of opposition, age, experience, form) rather than a specific matchup edge, and Shara Magomedov won via striking.

### 2025-01-11 · Mackenzie Dern vs Amanda Ribas
_UFC Fight Night: Dern vs. Ribas 2 · Women's Strawweight Bout_

- **Result:** Mackenzie Dern by Submission (R3 4:56). **Win type:** Dominant finish via grappling; stats support for the winner 67%.
- **Model before the fight** (trained on 7,830 earlier fights): Mackenzie Dern 35% / Amanda Ribas 65%. Picked Amanda Ribas ❌
- **Pushing toward Mackenzie Dern** (their number first): Takedown accuracy (19% vs 49%, ≈2.6 pts); UFC experience (fights) (14 vs 11, ≈1.3 pts); Win / loss streak (+1 vs -1, ≈1.0 pts); Times finished (1 vs 2, ≈0.9 pts)
- **Pushing toward Amanda Ribas** (their number first): Striking defense (61% vs 52%, ≈3.2 pts); Takedowns landed / 15 min (2.01 vs 0.93, ≈2.7 pts); Takedown defense (81% vs 42%, ≈2.3 pts); Recent striking form (last ~3 fights) (0.44 vs -0.39, ≈2.3 pts)
- **In the cage, Mackenzie Dern:** 27 of 46 sig. strikes (opponent 17); 1/3 takedowns; 4:34 control; 1 submission attempt(s); out-landed opponent in 2 round(s)
- **In the cage, Amanda Ribas:** 17 of 56 sig. strikes (opponent 27); 2/2 takedowns; 5:47 control; out-landed opponent in 0 round(s)
- **Why Mackenzie Dern won:** Mackenzie Dern was winning the fight (significant strikes 27-17) and finished it: Submission (Armbar From Mount), R3 4:56.
- **Amanda Ribas:** Amanda Ribas had real success (takedowns 2-1, control time (min) 5.8-4.6) but was finished.
- **Verdict: Wrong: the model misread the matchup.** The model's main reasons pointed to Amanda Ribas, but Mackenzie Dern won a dominant finish via grappling (stats support 67%), so this was a genuine miss rather than bad luck.

### 2025-01-18 · Islam Makhachev vs Renato Moicano
_UFC 311: Makhachev vs. Moicano · UFC Lightweight Title Bout_

- **Result:** Islam Makhachev by Submission (R1 4:05). **Win type:** Dominant finish via grappling; stats support for the winner 62%.
- **Model before the fight** (trained on 7,844 earlier fights): Islam Makhachev 88% / Renato Moicano 12%. Picked Islam Makhachev ✅
- **Pushing toward Islam Makhachev** (their number first): Recent strength of schedule (last ~3 opponents) (1729.26 vs 1600.63, ≈4.4 pts); Win / loss streak (+14 vs +4, ≈3.7 pts); Elo rating (quality of wins) (1963 vs 1741, ≈2.8 pts); Takedowns landed / 15 min (3.05 vs 1.84, ≈1.6 pts)
- **Pushing toward Renato Moicano** (their number first): Recent results (last ~3 fights) (76% vs 91%, ≈1.5 pts); Grappling control share (66% vs 82%, ≈0.4 pts); Takedown accuracy (44% vs 52%, ≈0.4 pts); Days since last fight (112 vs 231, ≈0.4 pts)
- **In the cage, Islam Makhachev:** 6 of 19 sig. strikes (opponent 9); 1/2 takedowns; 1:27 control; 1 submission attempt(s); out-landed opponent in 0 round(s)
- **In the cage, Renato Moicano:** 9 of 27 sig. strikes (opponent 6); 0/0 takedowns; out-landed opponent in 1 round(s)
- **Why Islam Makhachev won:** Islam Makhachev was winning the fight (takedowns 1-0, control time (min) 1.4-0.0) and finished it: Submission (D'Arce Choke On Ground), R1 4:05.
- **Renato Moicano:** Renato Moicano had real success (significant strikes 9-6) but was finished.
- **Verdict: Right, on overall profile.** The model backed Islam Makhachev mainly on overall profile (quality of opposition, age, experience, form) rather than a specific matchup edge, and Islam Makhachev won via grappling.

### 2025-01-18 · Merab Dvalishvili vs Umar Nurmagomedov
_UFC 311: Makhachev vs. Moicano · UFC Bantamweight Title Bout_

- **Result:** Merab Dvalishvili by Decision - Unanimous (R5 5:00). **Win type:** Competitive win via grappling; stats support for the winner 78%.
- **Model before the fight** (trained on 7,844 earlier fights): Merab Dvalishvili 56% / Umar Nurmagomedov 44%. Picked Merab Dvalishvili ✅
- **Pushing toward Merab Dvalishvili** (their number first): Recent strength of schedule (last ~3 opponents) (1656.41 vs 1593.67, ≈6.2 pts); Takedowns landed / 15 min (5.78 vs 3.55, ≈5.9 pts); UFC experience (fights) (13 vs 6, ≈2.9 pts); Elo rating (quality of wins) (1811 vs 1714, ≈2.9 pts)
- **Pushing toward Umar Nurmagomedov** (their number first): Age (29.0 vs 34.0, ≈5.0 pts); Striking accuracy (61% vs 42%, ≈3.1 pts); UFC cage time (minutes) (72 vs 209, ≈2.0 pts); Finishing rate (47% vs 9%, ≈2.0 pts)
- **In the cage, Merab Dvalishvili:** 111 of 259 sig. strikes (opponent 104); 7/30 takedowns; 2:22 control; out-landed opponent in 2 round(s)
- **In the cage, Umar Nurmagomedov:** 104 of 237 sig. strikes (opponent 111); 2/15 takedowns; 1:37 control; out-landed opponent in 3 round(s)
- **Why Merab Dvalishvili won:** Merab Dvalishvili edged it: led significant strikes 111-104, takedowns 7-2, control time (min) 2.4-1.6.
- **Umar Nurmagomedov:** Umar Nurmagomedov did not win any of the main stat battles.
- **Verdict: Right, on overall profile.** The model backed Merab Dvalishvili mainly on overall profile (quality of opposition, age, experience, form) rather than a specific matchup edge, and Merab Dvalishvili won via grappling.

### 2025-02-01 · Israel Adesanya vs Nassourdine Imavov
_UFC Fight Night: Adesanya vs. Imavov · Middleweight Bout_

- **Result:** Nassourdine Imavov by KO/TKO (R2 0:30). **Win type:** Dominant finish via striking; stats support for the winner 59%.
- **Model before the fight** (trained on 7,857 earlier fights): Israel Adesanya 39% / Nassourdine Imavov 61%. Picked Nassourdine Imavov ✅
- **Pushing toward Israel Adesanya** (their number first): Recent results (last ~3 fights) (48% vs 77%, ≈6.4 pts); Recent strength of schedule (last ~3 opponents) (1688.97 vs 1643.73, ≈4.2 pts); Strength of schedule (avg opponent Elo) (1682 vs 1603, ≈3.0 pts); UFC experience (fights) (17 vs 9, ≈3.0 pts)
- **Pushing toward Nassourdine Imavov** (their number first): Recent results vs expectation (opponent-adjusted) (0.35 vs -0.11, ≈7.0 pts); Age (28.9 vs 35.5, ≈6.5 pts); Age past 32 (decline years) (0.0 vs 3.5, ≈3.5 pts); Recent striking form (last ~3 fights) (1.17 vs 0.02, ≈3.3 pts)
- **In the cage, Israel Adesanya:** 26 of 50 sig. strikes (opponent 15); 0 knockdown(s) scored, 1 suffered; 0/1 takedowns; out-landed opponent in 1 round(s)
- **In the cage, Nassourdine Imavov:** 15 of 31 sig. strikes (opponent 26); 1 knockdown(s) scored, 0 suffered; 0/3 takedowns; 0:44 control; out-landed opponent in 1 round(s)
- **Why Nassourdine Imavov won:** Nassourdine Imavov was winning the fight (knockdowns 1-0, control time (min) 0.7-0.0) and finished it: KO/TKO (Punch to Head At Distance), R2 0:30.
- **Israel Adesanya:** Israel Adesanya had real success (significant strikes 26-15) but was finished.
- **Verdict: Right, on overall profile.** The model backed Nassourdine Imavov mainly on overall profile (quality of opposition, age, experience, form) rather than a specific matchup edge, and Nassourdine Imavov won via striking.

### 2025-02-01 · Shara Magomedov vs Michael Page
_UFC Fight Night: Adesanya vs. Imavov · Middleweight Bout_

- **Result:** Michael Page by Decision - Unanimous (R3 5:00). **Win type:** Competitive win via striking; stats support for the winner 61%.
- **Model before the fight** (trained on 7,857 earlier fights): Shara Magomedov 56% / Michael Page 44%. Picked Shara Magomedov ❌
- **Pushing toward Shara Magomedov** (their number first): Age (30.7 vs 37.8, ≈7.0 pts); Age past 32 (decline years) (0.0 vs 5.8, ≈5.5 pts); Recent results vs expectation (opponent-adjusted) (0.34 vs 0.11, ≈3.5 pts); UFC win percentage (83% vs 50%, ≈3.3 pts)
- **Pushing toward Michael Page** (their number first): Recent results (last ~3 fights) (46% vs 87%, ≈9.5 pts); Recent strength of schedule (last ~3 opponents) (1631.35 vs 1520.94, ≈8.2 pts); Reach (201 cm vs 185 cm, ≈4.0 pts); Strength of schedule (avg opponent Elo) (1600 vs 1519, ≈3.0 pts)
- **In the cage, Shara Magomedov:** 38 of 87 sig. strikes (opponent 43); 0/0 takedowns; 0:40 control; out-landed opponent in 1 round(s)
- **In the cage, Michael Page:** 43 of 75 sig. strikes (opponent 38); 0/1 takedowns; 0:50 control; out-landed opponent in 2 round(s)
- **Why Michael Page won:** Michael Page edged it: led significant strikes 43-38, control time (min) 0.8-0.7.
- **Shara Magomedov:** Shara Magomedov did not win any of the main stat battles.
- **Verdict: Wrong: the model misread the matchup.** The model's main reasons pointed to Shara Magomedov, but Michael Page won a competitive win via striking (stats support 61%), so this was a genuine miss rather than bad luck.

### 2025-02-08 · Zhang Weili vs Tatiana Suarez
_UFC 312: Du Plessis vs. Strickland 2 · UFC Women's Strawweight Title Bout_

- **Result:** Zhang Weili by Decision - Unanimous (R5 5:00). **Win type:** Clear win via striking; stats support for the winner 99%.
- **Model before the fight** (trained on 7,868 earlier fights): Zhang Weili 45% / Tatiana Suarez 55%. Picked Tatiana Suarez ❌
- **Pushing toward Zhang Weili** (their number first): Recent strength of schedule (last ~3 opponents) (1635.59 vs 1558.16, ≈6.9 pts); Recent results (last ~3 fights) (78% vs 90%, ≈2.9 pts); Strength of schedule (avg opponent Elo) (1616 vs 1545, ≈2.5 pts); Recent striking form (last ~3 fights) (2.48 vs 1.78, ≈1.9 pts)
- **Pushing toward Tatiana Suarez** (their number first): Takedowns landed / 15 min (5.32 vs 2.42, ≈8.4 pts); Age (34.1 vs 35.5, ≈2.2 pts); Finishing rate (66% vs 36%, ≈1.9 pts); UFC win percentage (89% vs 77%, ≈1.8 pts)
- **In the cage, Zhang Weili:** 53 of 87 sig. strikes (opponent 12); 1/3 takedowns; 10:54 control; 1 submission attempt(s); out-landed opponent in 5 round(s)
- **In the cage, Tatiana Suarez:** 12 of 36 sig. strikes (opponent 53); 1/15 takedowns; 5:56 control; out-landed opponent in 0 round(s)
- **Why Zhang Weili won:** Zhang Weili won the fight on the numbers and the cards agreed: led significant strikes 53-12, control time (min) 10.9-5.9.
- **Tatiana Suarez:** Tatiana Suarez did not win any of the main stat battles.
- **Verdict: Wrong: the model misread the matchup.** The model's main reasons pointed to Tatiana Suarez, but Zhang Weili won a clear win via striking (stats support 99%), so this was a genuine miss rather than bad luck.

### 2025-02-08 · Dricus Du Plessis vs Sean Strickland
_UFC 312: Du Plessis vs. Strickland 2 · UFC Middleweight Title Bout_

- **Result:** Dricus Du Plessis by Decision - Unanimous (R5 5:00). **Win type:** Competitive win via striking; stats support for the winner 64%.
- **Model before the fight** (trained on 7,868 earlier fights): Dricus Du Plessis 77% / Sean Strickland 23%. Picked Dricus Du Plessis ✅
- **Pushing toward Dricus Du Plessis** (their number first): Win / loss streak (+8 vs +1, ≈4.1 pts); Recent results vs expectation (opponent-adjusted) (0.45 vs 0.11, ≈3.9 pts); Takedowns landed / 15 min (2.84 vs 0.81, ≈3.8 pts); Recent strength of schedule (last ~3 opponents) (1686.44 vs 1639.50, ≈3.5 pts)
- **Pushing toward Sean Strickland** (their number first): Recent results (last ~3 fights) (66% vs 90%, ≈3.9 pts); UFC experience (fights) (22 vs 8, ≈3.3 pts); Recent striking form (last ~3 fights) (1.34 vs 0.49, ≈1.9 pts); Striking defense (61% vs 55%, ≈1.6 pts)
- **In the cage, Dricus Du Plessis:** 147 of 314 sig. strikes (opponent 128); 1/2 takedowns; 0:05 control; out-landed opponent in 4 round(s)
- **In the cage, Sean Strickland:** 128 of 263 sig. strikes (opponent 147); 0/0 takedowns; out-landed opponent in 1 round(s)
- **Why Dricus Du Plessis won:** Dricus Du Plessis edged it: led significant strikes 147-128, takedowns 1-0, control time (min) 0.1-0.0.
- **Sean Strickland:** Sean Strickland did not win any of the main stat battles.
- **Verdict: Right, on overall profile.** The model backed Dricus Du Plessis mainly on overall profile (quality of opposition, age, experience, form) rather than a specific matchup edge, and Dricus Du Plessis won via striking.

### 2025-02-15 · Jared Cannonier vs Gregory Rodrigues
_UFC Fight Night: Cannonier vs. Rodrigues · Middleweight Bout_

- **Result:** Jared Cannonier by KO/TKO (R4 0:21). **Win type:** Dominant finish via striking; stats support for the winner 64%.
- **Model before the fight** (trained on 7,879 earlier fights): Jared Cannonier 32% / Gregory Rodrigues 68%. Picked Gregory Rodrigues ❌
- **Pushing toward Jared Cannonier** (their number first): Recent strength of schedule (last ~3 opponents) (1661.25 vs 1538.51, ≈8.5 pts); Recent results (last ~3 fights) (46% vs 76%, ≈6.1 pts); Strength of schedule (avg opponent Elo) (1633 vs 1530, ≈3.0 pts); UFC experience (fights) (18 vs 9, ≈2.9 pts)
- **Pushing toward Gregory Rodrigues** (their number first): Age (33.0 vs 40.9, ≈6.5 pts); Age past 32 (decline years) (1.0 vs 8.9, ≈5.9 pts); Takedowns landed / 15 min (2.61 vs 0.49, ≈4.8 pts); Recent results vs expectation (opponent-adjusted) (0.22 vs -0.02, ≈3.4 pts)
- **In the cage, Jared Cannonier:** 98 of 201 sig. strikes (opponent 93); 2 knockdown(s) scored, 2 suffered; 1/3 takedowns; 2:09 control; out-landed opponent in 2 round(s)
- **In the cage, Gregory Rodrigues:** 93 of 221 sig. strikes (opponent 98); 2 knockdown(s) scored, 2 suffered; 0/3 takedowns; 0:17 control; out-landed opponent in 2 round(s)
- **Why Jared Cannonier won:** Jared Cannonier was winning the fight (significant strikes 98-93, takedowns 1-0, control time (min) 2.1-0.3) and finished it: KO/TKO (Punches to Head At Distance), R4 0:21.
- **Gregory Rodrigues:** Gregory Rodrigues did not win any of the main stat battles.
- **Verdict: Wrong: the model misread the matchup.** The model's main reasons pointed to Gregory Rodrigues, but Jared Cannonier won a dominant finish via striking (stats support 64%), so this was a genuine miss rather than bad luck.

### 2025-03-01 · Manel Kape vs Asu Almabayev
_UFC Fight Night: Kape vs. Almabayev · Flyweight Bout_

- **Result:** Manel Kape by KO/TKO (R3 2:16). **Win type:** Dominant finish via striking; stats support for the winner 88%.
- **Model before the fight** (trained on 7,903 earlier fights): Manel Kape 41% / Asu Almabayev 59%. Picked Asu Almabayev ❌
- **Pushing toward Manel Kape** (their number first): Recent results (last ~3 fights) (66% vs 87%, ≈4.9 pts); Recent strength of schedule (last ~3 opponents) (1558.53 vs 1527.95, ≈3.1 pts); UFC experience (fights) (8 vs 4, ≈1.5 pts); Takedown accuracy (35% vs 48%, ≈1.4 pts)
- **Pushing toward Asu Almabayev** (their number first): Takedowns landed / 15 min (4.29 vs 0.61, ≈9.3 pts); Recent grappling control (87% vs 37%, ≈6.1 pts); Recent results vs expectation (opponent-adjusted) (0.35 vs 0.19, ≈2.4 pts); Sig. strikes absorbed / min (1.55 vs 4.05, ≈2.4 pts)
- **In the cage, Manel Kape:** 61 of 115 sig. strikes (opponent 40); 0/1 takedowns; 0:29 control; out-landed opponent in 2 round(s)
- **In the cage, Asu Almabayev:** 40 of 80 sig. strikes (opponent 61); 0/6 takedowns; out-landed opponent in 1 round(s)
- **Why Manel Kape won:** Manel Kape was winning the fight (significant strikes 61-40, control time (min) 0.5-0.0) and finished it: KO/TKO (Punches to Head At Distance), R3 2:16.
- **Asu Almabayev:** Asu Almabayev did not win any of the main stat battles.
- **Verdict: Wrong: the model misread the matchup.** The model's main reasons pointed to Asu Almabayev, but Manel Kape won a dominant finish via striking (stats support 88%), so this was a genuine miss rather than bad luck.

### 2025-03-08 · Alex Pereira vs Magomed Ankalaev
_UFC 313: Pereira vs. Ankalaev · UFC Light Heavyweight Title Bout_

- **Result:** Magomed Ankalaev by Decision - Unanimous (R5 5:00). **Win type:** Clear win via mixed; stats support for the winner 92%.
- **Model before the fight** (trained on 7,913 earlier fights): Alex Pereira 49% / Magomed Ankalaev 51%. Picked Magomed Ankalaev ✅
- **Pushing toward Alex Pereira** (their number first): Recent strength of schedule (last ~3 opponents) (1664.83 vs 1620.42, ≈4.6 pts); Recent striking form (last ~3 fights) (1.96 vs 0.75, ≈3.5 pts); Strength of schedule (avg opponent Elo) (1670 vs 1583, ≈3.4 pts); Reach (201 cm vs 190 cm, ≈2.8 pts)
- **Pushing toward Magomed Ankalaev** (their number first): Recent grappling control (78% vs 23%, ≈6.0 pts); Age past 32 (decline years) (0.8 vs 5.7, ≈5.5 pts); Age (32.8 vs 37.7, ≈4.7 pts); Takedowns landed / 15 min (0.97 vs 0.31, ≈2.7 pts)
- **In the cage, Alex Pereira:** 76 of 137 sig. strikes (opponent 94); 0/1 takedowns; out-landed opponent in 2 round(s)
- **In the cage, Magomed Ankalaev:** 94 of 180 sig. strikes (opponent 76); 0/12 takedowns; 5:42 control; out-landed opponent in 3 round(s)
- **Why Magomed Ankalaev won:** Magomed Ankalaev won the fight on the numbers and the cards agreed: led significant strikes 94-76, control time (min) 5.7-0.0.
- **Alex Pereira:** Alex Pereira did not win any of the main stat battles.
- **Verdict: Right for the right reasons.** The model expected Magomed Ankalaev to have the grappling edge, and that is how the fight was won (mixed).

### 2025-03-15 · Marvin Vettori vs Roman Dolidze
_UFC Fight Night: Vettori vs. Dolidze 2 · Middleweight Bout_

- **Result:** Roman Dolidze by Decision - Unanimous (R5 5:00). **Win type:** Competitive win via striking; stats support for the winner 82%.
- **Model before the fight** (trained on 7,923 earlier fights): Marvin Vettori 65% / Roman Dolidze 35%. Picked Marvin Vettori ❌
- **Pushing toward Marvin Vettori** (their number first): Recent strength of schedule (last ~3 opponents) (1657.41 vs 1600.24, ≈5.5 pts); Age (31.5 vs 36.7, ≈5.0 pts); Age past 32 (decline years) (0.0 vs 4.7, ≈3.9 pts); Recent results (last ~3 fights) (52% vs 67%, ≈3.3 pts)
- **Pushing toward Roman Dolidze** (their number first): Days since last fight (161 vs 637, ≈4.4 pts); UFC cage time (minutes) (124 vs 254, ≈1.7 pts); Recent results vs expectation (opponent-adjusted) (0.18 vs 0.06, ≈1.7 pts); Finishing rate (44% vs 14%, ≈1.6 pts)
- **In the cage, Marvin Vettori:** 111 of 220 sig. strikes (opponent 141); 0/0 takedowns; out-landed opponent in 2 round(s)
- **In the cage, Roman Dolidze:** 141 of 338 sig. strikes (opponent 111); 0/1 takedowns; 0:15 control; out-landed opponent in 3 round(s)
- **Why Roman Dolidze won:** Roman Dolidze edged it: led significant strikes 141-111, control time (min) 0.2-0.0.
- **Marvin Vettori:** Marvin Vettori did not win any of the main stat battles.
- **Verdict: Wrong: the model misread the matchup.** The model's main reasons pointed to Marvin Vettori, but Roman Dolidze won a competitive win via striking (stats support 82%), so this was a genuine miss rather than bad luck.

### 2025-03-22 · Leon Edwards vs Sean Brady
_UFC Fight Night: Edwards vs. Brady · Welterweight Bout_

- **Result:** Sean Brady by Submission (R4 1:39). **Win type:** Dominant finish via grappling; stats support for the winner 100%.
- **Model before the fight** (trained on 7,936 earlier fights): Leon Edwards 50% / Sean Brady 50%. Picked Leon Edwards ❌
- **Pushing toward Leon Edwards** (their number first): Recent strength of schedule (last ~3 opponents) (1736.87 vs 1642.48, ≈7.9 pts); Elo rating (quality of wins) (1878 vs 1730, ≈5.4 pts); UFC experience (fights) (17 vs 8, ≈3.2 pts); Grappling control share (46% vs 86%, ≈2.1 pts)
- **Pushing toward Sean Brady** (their number first): Takedowns landed / 15 min (3.25 vs 1.26, ≈5.0 pts); Recent grappling control (83% vs 39%, ≈4.6 pts); Recent striking form (last ~3 fights) (1.00 vs 0.12, ≈3.4 pts); UFC cage time (minutes) (112 vs 312, ≈3.3 pts)
- **In the cage, Leon Edwards:** 23 of 35 sig. strikes (opponent 57); 0/1 takedowns; 0:15 control; out-landed opponent in 1 round(s)
- **In the cage, Sean Brady:** 57 of 93 sig. strikes (opponent 23); 5/7 takedowns; 11:10 control; 1 submission attempt(s); out-landed opponent in 3 round(s)
- **Why Sean Brady won:** Sean Brady was winning the fight (significant strikes 57-23, takedowns 5-0, control time (min) 11.2-0.2) and finished it: Submission (Guillotine Choke From Mount), R4 1:39.
- **Leon Edwards:** Leon Edwards did not win any of the main stat battles.
- **Verdict: Wrong on a toss-up.** The model saw this as close to 50/50 and leaned the wrong way.

### 2025-03-29 · Brandon Moreno vs Steve Erceg
_UFC Fight Night: Moreno vs. Erceg · Flyweight Bout_

- **Result:** Brandon Moreno by Decision - Unanimous (R5 5:00). **Win type:** Contested decision via grappling; stats support for the winner 11%.
- **Model before the fight** (trained on 7,949 earlier fights): Brandon Moreno 75% / Steve Erceg 25%. Picked Brandon Moreno ✅
- **Pushing toward Brandon Moreno** (their number first): Recent strength of schedule (last ~3 opponents) (1639.28 vs 1575.51, ≈5.1 pts); Elo rating (quality of wins) (1710 vs 1543, ≈4.6 pts); UFC experience (fights) (17 vs 5, ≈2.8 pts); Recent striking form (last ~3 fights) (0.73 vs -0.04, ≈2.5 pts)
- **Pushing toward Steve Erceg** (their number first): UFC cage time (minutes) (64 vs 283, ≈2.6 pts); Recent results (last ~3 fights) (47% vs 57%, ≈1.8 pts); Age (29.7 vs 31.3, ≈1.6 pts); Takedown accuracy (29% vs 45%, ≈1.2 pts)
- **In the cage, Brandon Moreno:** 89 of 176 sig. strikes (opponent 116); 1/5 takedowns; 1:25 control; out-landed opponent in 0 round(s)
- **In the cage, Steve Erceg:** 116 of 279 sig. strikes (opponent 89); 0/0 takedowns; out-landed opponent in 5 round(s)
- **Why Brandon Moreno won:** Brandon Moreno got the decision even though Steve Erceg led significant strikes 116-89; this is a contested result, not a clean win.
- **Steve Erceg:** Steve Erceg had real success (significant strikes 116-89) but it was not enough on the scorecards.
- **Verdict: Right, on overall profile.** The model backed Brandon Moreno mainly on overall profile (quality of opposition, age, experience, form) rather than a specific matchup edge, and Brandon Moreno won via grappling.

### 2025-04-05 · Josh Emmett vs Lerone Murphy
_UFC Fight Night: Emmett vs. Murphy · Featherweight Bout_

- **Result:** Lerone Murphy by Decision - Unanimous (R5 5:00). **Win type:** Competitive win via striking; stats support for the winner 74%.
- **Model before the fight** (trained on 7,961 earlier fights): Josh Emmett 22% / Lerone Murphy 78%. Picked Lerone Murphy ✅
- **Pushing toward Josh Emmett** (their number first): Recent results (last ~3 fights) (62% vs 88%, ≈4.5 pts); Recent strength of schedule (last ~3 opponents) (1638.03 vs 1572.17, ≈3.6 pts); UFC experience (fights) (14 vs 8, ≈1.6 pts); Strength of schedule (avg opponent Elo) (1612 vs 1561, ≈1.5 pts)
- **Pushing toward Lerone Murphy** (their number first): Age (33.7 vs 40.1, ≈4.6 pts); Recent striking form (last ~3 fights) (2.06 vs -1.14, ≈4.6 pts); Age past 32 (decline years) (1.7 vs 8.1, ≈3.7 pts); Days since last fight (161 vs 476, ≈3.4 pts)
- **In the cage, Josh Emmett:** 41 of 143 sig. strikes (opponent 84); 4/11 takedowns; 3:39 control; out-landed opponent in 0 round(s)
- **In the cage, Lerone Murphy:** 84 of 157 sig. strikes (opponent 41); 0/0 takedowns; 0:06 control; out-landed opponent in 4 round(s)
- **Why Lerone Murphy won:** Lerone Murphy edged it: led significant strikes 84-41, while Josh Emmett took takedowns 4-0, control time (min) 3.6-0.1.
- **Josh Emmett:** Josh Emmett had real success (takedowns 4-0, control time (min) 3.6-0.1) but it was not enough on the scorecards.
- **Verdict: Right, on overall profile.** The model backed Lerone Murphy mainly on overall profile (quality of opposition, age, experience, form) rather than a specific matchup edge, and Lerone Murphy won via striking.

### 2025-04-12 · Alexander Volkanovski vs Diego Lopes
_UFC 314: Volkanovski vs. Lopes · UFC Featherweight Title Bout_

- **Result:** Alexander Volkanovski by Decision - Unanimous (R5 5:00). **Win type:** Clear win via striking; stats support for the winner 100%.
- **Model before the fight** (trained on 7,973 earlier fights): Alexander Volkanovski 53% / Diego Lopes 47%. Picked Alexander Volkanovski ✅
- **Pushing toward Alexander Volkanovski** (their number first): Recent strength of schedule (last ~3 opponents) (1736.61 vs 1626.57, ≈8.1 pts); Recent results (last ~3 fights) (51% vs 82%, ≈7.6 pts); Elo rating (quality of wins) (1805 vs 1697, ≈4.5 pts); UFC experience (fights) (16 vs 6, ≈3.5 pts)
- **Pushing toward Diego Lopes** (their number first): Recent results vs expectation (opponent-adjusted) (0.41 vs -0.05, ≈7.5 pts); Age (30.3 vs 36.5, ≈6.9 pts); Win / loss streak (+5 vs -2, ≈6.1 pts); Age past 32 (decline years) (0.0 vs 4.5, ≈5.1 pts)
- **In the cage, Alexander Volkanovski:** 158 of 259 sig. strikes (opponent 63); 0 knockdown(s) scored, 1 suffered; 1/11 takedowns; 1:18 control; out-landed opponent in 5 round(s)
- **In the cage, Diego Lopes:** 63 of 194 sig. strikes (opponent 158); 1 knockdown(s) scored, 0 suffered; 0/0 takedowns; 0:05 control; out-landed opponent in 0 round(s)
- **Why Alexander Volkanovski won:** Alexander Volkanovski won the fight on the numbers and the cards agreed: led significant strikes 158-63, takedowns 1-0, control time (min) 1.3-0.1.
- **Diego Lopes:** Diego Lopes had real success (knockdowns 1-0) but it was not enough on the scorecards.
- **Verdict: Right, on overall profile.** The model backed Alexander Volkanovski mainly on overall profile (quality of opposition, age, experience, form) rather than a specific matchup edge, and Alexander Volkanovski won via striking.

### 2025-04-26 · Ian Machado Garry vs Carlos Prates
_UFC Fight Night: Machado Garry vs. Prates · Welterweight Bout_

- **Result:** Ian Machado Garry by Decision - Unanimous (R5 5:00). **Win type:** Clear win via striking; stats support for the winner 100%.
- **Model before the fight** (trained on 7,986 earlier fights): Ian Machado Garry 58% / Carlos Prates 42%. Picked Ian Machado Garry ✅
- **Pushing toward Ian Machado Garry** (their number first): Age (27.4 vs 31.7, ≈4.0 pts); Recent results (last ~3 fights) (71% vs 87%, ≈3.7 pts); Recent striking form (last ~3 fights) (1.10 vs -0.05, ≈3.4 pts); Recent strength of schedule (last ~3 opponents) (1615.30 vs 1590.64, ≈3.2 pts)
- **Pushing toward Carlos Prates** (their number first): Recent results vs expectation (opponent-adjusted) (0.42 vs 0.18, ≈3.9 pts); Finishing rate (86% vs 33%, ≈2.7 pts); Win / loss streak (+4 vs -1, ≈2.6 pts); Reach (198 cm vs 188 cm, ≈2.5 pts)
- **In the cage, Ian Machado Garry:** 126 of 242 sig. strikes (opponent 63); 4/19 takedowns; 3:09 control; out-landed opponent in 5 round(s)
- **In the cage, Carlos Prates:** 63 of 129 sig. strikes (opponent 126); 0/0 takedowns; 1:46 control; out-landed opponent in 0 round(s)
- **Why Ian Machado Garry won:** Ian Machado Garry won the fight on the numbers and the cards agreed: led significant strikes 126-63, takedowns 4-0, control time (min) 3.1-1.8.
- **Carlos Prates:** Carlos Prates did not win any of the main stat battles.
- **Verdict: Right for the right reasons.** The model expected Ian Machado Garry to have the striking edge, and that is how the fight was won (striking).

### 2025-05-03 · Cory Sandhagen vs Deiveson Figueiredo
_UFC Fight Night: Sandhagen vs. Figueiredo · Bantamweight Bout_

- **Result:** Cory Sandhagen by KO/TKO (R2 4:08). **Win type:** Dominant finish via striking; stats support for the winner 99%.
- **Model before the fight** (trained on 8,000 earlier fights): Cory Sandhagen 66% / Deiveson Figueiredo 34%. Picked Cory Sandhagen ✅
- **Pushing toward Cory Sandhagen** (their number first): Age (33.0 vs 37.4, ≈4.2 pts); Age past 32 (decline years) (1.0 vs 5.4, ≈4.0 pts); Recent striking form (last ~3 fights) (0.78 vs -1.08, ≈4.0 pts); Striking defense (57% vs 50%, ≈1.8 pts)
- **Pushing toward Deiveson Figueiredo** (their number first): Striking accuracy (54% vs 44%, ≈2.1 pts); Title fight experience (6 vs 1, ≈1.7 pts); UFC experience (fights) (18 vs 14, ≈1.4 pts); UFC win percentage (74% vs 69%, ≈1.1 pts)
- **In the cage, Cory Sandhagen:** 54 of 87 sig. strikes (opponent 6); 2/2 takedowns; 5:07 control; out-landed opponent in 2 round(s)
- **In the cage, Deiveson Figueiredo:** 6 of 9 sig. strikes (opponent 54); 2/5 takedowns; 0:31 control; out-landed opponent in 0 round(s)
- **Why Cory Sandhagen won:** Cory Sandhagen was winning the fight (significant strikes 54-6, control time (min) 5.1-0.5) and finished it: KO/TKO (toKnee Injury), R2 4:08.
- **Deiveson Figueiredo:** Deiveson Figueiredo did not win any of the main stat battles.
- **Verdict: Right for the right reasons.** The model expected Cory Sandhagen to have the striking edge, and that is how the fight was won (striking).

### 2025-05-10 · Belal Muhammad vs Jack Della Maddalena
_UFC 315: Muhammad vs. Della Maddalena · UFC Welterweight Title Bout_

- **Result:** Jack Della Maddalena by Decision - Unanimous (R5 5:00). **Win type:** Competitive win via striking; stats support for the winner 77%.
- **Model before the fight** (trained on 8,012 earlier fights): Belal Muhammad 44% / Jack Della Maddalena 56%. Picked Jack Della Maddalena ✅
- **Pushing toward Belal Muhammad** (their number first): Recent strength of schedule (last ~3 opponents) (1699.15 vs 1621.63, ≈7.4 pts); Elo rating (quality of wins) (1888 vs 1763, ≈4.2 pts); Takedowns landed / 15 min (2.24 vs 0.54, ≈4.1 pts); Recent grappling control (68% vs 25%, ≈4.0 pts)
- **Pushing toward Jack Della Maddalena** (their number first): Age (28.7 vs 36.8, ≈7.8 pts); Age past 32 (decline years) (0.0 vs 4.8, ≈4.8 pts); Striking defense (66% vs 57%, ≈3.5 pts); UFC cage time (minutes) (55 vs 283, ≈3.4 pts)
- **In the cage, Belal Muhammad:** 132 of 318 sig. strikes (opponent 178); 3/9 takedowns; 3:21 control; out-landed opponent in 0 round(s)
- **In the cage, Jack Della Maddalena:** 178 of 342 sig. strikes (opponent 132); 0/3 takedowns; 0:40 control; out-landed opponent in 5 round(s)
- **Why Jack Della Maddalena won:** Jack Della Maddalena edged it: led significant strikes 178-132, while Belal Muhammad took takedowns 3-0, control time (min) 3.4-0.7.
- **Belal Muhammad:** Belal Muhammad had real success (takedowns 3-0, control time (min) 3.4-0.7) but it was not enough on the scorecards.
- **Verdict: Right for the right reasons.** The model expected Jack Della Maddalena to have the striking edge, and that is how the fight was won (striking).

### 2025-05-10 · Valentina Shevchenko vs Manon Fiorot
_UFC 315: Muhammad vs. Della Maddalena · UFC Women's Flyweight Title Bout_

- **Result:** Valentina Shevchenko by Decision - Unanimous (R5 5:00). **Win type:** Competitive win via striking; stats support for the winner 69%.
- **Model before the fight** (trained on 8,012 earlier fights): Valentina Shevchenko 47% / Manon Fiorot 53%. Picked Manon Fiorot ❌
- **Pushing toward Valentina Shevchenko** (their number first): Recent results (last ~3 fights) (72% vs 90%, ≈4.4 pts); Takedowns landed / 15 min (2.68 vs 1.22, ≈4.0 pts); UFC experience (fights) (17 vs 7, ≈3.3 pts); Title fight experience (12 vs 0, ≈2.9 pts)
- **Pushing toward Manon Fiorot** (their number first): Recent results vs expectation (opponent-adjusted) (0.41 vs 0.11, ≈4.9 pts); Win / loss streak (+7 vs +1, ≈3.5 pts); UFC cage time (minutes) (102 vs 312, ≈3.4 pts); Age (35.2 vs 37.2, ≈2.5 pts)
- **In the cage, Valentina Shevchenko:** 72 of 149 sig. strikes (opponent 71); 1 knockdown(s) scored, 0 suffered; 2/9 takedowns; 1:52 control; out-landed opponent in 2 round(s)
- **In the cage, Manon Fiorot:** 71 of 160 sig. strikes (opponent 72); 0 knockdown(s) scored, 1 suffered; 1/12 takedowns; 7:07 control; out-landed opponent in 2 round(s)
- **Why Valentina Shevchenko won:** Valentina Shevchenko edged it: led significant strikes 72-71, knockdowns 1-0, takedowns 2-1, while Manon Fiorot took control time (min) 7.1-1.9.
- **Manon Fiorot:** Manon Fiorot had real success (control time (min) 7.1-1.9) but it was not enough on the scorecards.
- **Verdict: Wrong on a toss-up.** The model saw this as close to 50/50 and leaned the wrong way.

### 2025-05-17 · Gilbert Burns vs Michael Morales
_UFC Fight Night: Burns vs. Morales · Welterweight Bout_

- **Result:** Michael Morales by KO/TKO (R1 3:39). **Win type:** Dominant finish via striking; stats support for the winner 97%.
- **Model before the fight** (trained on 8,024 earlier fights): Gilbert Burns 21% / Michael Morales 79%. Picked Michael Morales ✅
- **Pushing toward Gilbert Burns** (their number first): Recent results (last ~3 fights) (40% vs 88%, ≈8.0 pts); Recent strength of schedule (last ~3 opponents) (1682.04 vs 1598.41, ≈4.5 pts); UFC experience (fights) (23 vs 5, ≈3.4 pts); Takedowns landed / 15 min (2.07 vs 0.58, ≈2.7 pts)
- **Pushing toward Michael Morales** (their number first): Age (25.9 vs 38.8, ≈8.7 pts); Recent results vs expectation (opponent-adjusted) (0.42 vs -0.14, ≈6.2 pts); Recent striking form (last ~3 fights) (1.86 vs -1.39, ≈4.9 pts); Win / loss streak (+5 vs -3, ≈4.6 pts)
- **In the cage, Gilbert Burns:** 5 of 18 sig. strikes (opponent 33); 0 knockdown(s) scored, 2 suffered; 1/2 takedowns; 0:30 control; out-landed opponent in 0 round(s)
- **In the cage, Michael Morales:** 33 of 56 sig. strikes (opponent 5); 2 knockdown(s) scored, 0 suffered; 0/0 takedowns; 0:10 control; out-landed opponent in 1 round(s)
- **Why Michael Morales won:** Michael Morales was winning the fight (significant strikes 33-5, knockdowns 2-0) and finished it: KO/TKO (Punches to Head At Distance), R1 3:39.
- **Gilbert Burns:** Gilbert Burns had real success (takedowns 1-0, control time (min) 0.5-0.2) but was finished.
- **Verdict: Right, on overall profile.** The model backed Michael Morales mainly on overall profile (quality of opposition, age, experience, form) rather than a specific matchup edge, and Michael Morales won via striking.

### 2025-06-07 · Merab Dvalishvili vs Sean O'Malley
_UFC 316: Dvalishvili vs. O'Malley 2 · UFC Bantamweight Title Bout_

- **Result:** Merab Dvalishvili by Submission (R3 4:42). **Win type:** Dominant finish via grappling; stats support for the winner 99%.
- **Model before the fight** (trained on 8,044 earlier fights): Merab Dvalishvili 63% / Sean O'Malley 37%. Picked Merab Dvalishvili ✅
- **Pushing toward Merab Dvalishvili** (their number first): Takedowns landed / 15 min (5.62 vs 0.41, ≈14.3 pts); Win / loss streak (+12 vs -1, ≈8.6 pts); Recent grappling control (79% vs 15%, ≈5.6 pts); Recent results vs expectation (opponent-adjusted) (0.38 vs 0.19, ≈3.2 pts)
- **Pushing toward Sean O'Malley** (their number first): Recent results (last ~3 fights) (69% vs 89%, ≈4.6 pts); Age (30.6 vs 34.4, ≈3.9 pts); Striking accuracy (61% vs 42%, ≈3.3 pts); Age past 32 (decline years) (0.0 vs 2.4, ≈2.7 pts)
- **In the cage, Merab Dvalishvili:** 52 of 115 sig. strikes (opponent 31); 5/12 takedowns; 6:29 control; 1 submission attempt(s); out-landed opponent in 3 round(s)
- **In the cage, Sean O'Malley:** 31 of 57 sig. strikes (opponent 52); 0/0 takedowns; out-landed opponent in 0 round(s)
- **Why Merab Dvalishvili won:** Merab Dvalishvili was winning the fight (significant strikes 52-31, takedowns 5-0, control time (min) 6.5-0.0) and finished it: Submission (Guillotine Choke On Ground), R3 4:42.
- **Sean O'Malley:** Sean O'Malley did not win any of the main stat battles.
- **Verdict: Right for the right reasons.** The model expected Merab Dvalishvili to have the grappling edge, and that is how the fight was won (grappling).

### 2025-06-07 · Julianna Pena vs Kayla Harrison
_UFC 316: Dvalishvili vs. O'Malley 2 · UFC Women's Bantamweight Title Bout_

- **Result:** Kayla Harrison by Submission (R2 4:55). **Win type:** Dominant finish via grappling; stats support for the winner 97%.
- **Model before the fight** (trained on 8,044 earlier fights): Julianna Pena 41% / Kayla Harrison 59%. Picked Kayla Harrison ✅
- **Pushing toward Julianna Pena** (their number first): Recent strength of schedule (last ~3 opponents) (1640.99 vs 1578.65, ≈6.0 pts); Recent results (last ~3 fights) (64% vs 82%, ≈4.2 pts); Elo rating (quality of wins) (1685 vs 1589, ≈3.4 pts); UFC experience (fights) (11 vs 2, ≈2.9 pts)
- **Pushing toward Kayla Harrison** (their number first): Recent striking form (last ~3 fights) (1.98 vs 0.22, ≈4.5 pts); Recent grappling control (84% vs 43%, ≈4.0 pts); Recent results vs expectation (opponent-adjusted) (0.41 vs 0.21, ≈3.3 pts); Striking accuracy (59% vs 45%, ≈2.5 pts)
- **In the cage, Julianna Pena:** 9 of 30 sig. strikes (opponent 30); 0/1 takedowns; out-landed opponent in 0 round(s)
- **In the cage, Kayla Harrison:** 30 of 54 sig. strikes (opponent 9); 2/3 takedowns; 6:05 control; 1 submission attempt(s); out-landed opponent in 2 round(s)
- **Why Kayla Harrison won:** Kayla Harrison was winning the fight (significant strikes 30-9, takedowns 2-0, control time (min) 6.1-0.0) and finished it: Submission (Kimura From Side Control), R2 4:55.
- **Julianna Pena:** Julianna Pena did not win any of the main stat battles.
- **Verdict: Right winner, different route.** The model expected a striking edge for Kayla Harrison, but the fight was actually won by grappling.

### 2025-06-14 · Kamaru Usman vs Joaquin Buckley
_UFC Fight Night: Usman vs. Buckley · Welterweight Bout_

- **Result:** Kamaru Usman by Decision - Unanimous (R5 5:00). **Win type:** Clear win via grappling; stats support for the winner 97%.
- **Model before the fight** (trained on 8,057 earlier fights): Kamaru Usman 46% / Joaquin Buckley 54%. Picked Joaquin Buckley ❌
- **Pushing toward Kamaru Usman** (their number first): Recent strength of schedule (last ~3 opponents) (1724.42 vs 1625.31, ≈8.9 pts); Recent results (last ~3 fights) (49% vs 81%, ≈7.6 pts); Takedowns landed / 15 min (2.76 vs 1.76, ≈4.3 pts); Strength of schedule (avg opponent Elo) (1682 vs 1572, ≈3.3 pts)
- **Pushing toward Joaquin Buckley** (their number first): Win / loss streak (+6 vs -3, ≈8.0 pts); Age (31.1 vs 38.1, ≈7.8 pts); Recent results vs expectation (opponent-adjusted) (0.33 vs -0.12, ≈7.5 pts); Age past 32 (decline years) (0.0 vs 6.1, ≈6.1 pts)
- **In the cage, Kamaru Usman:** 41 of 99 sig. strikes (opponent 44); 4/13 takedowns; 12:57 control; out-landed opponent in 2 round(s)
- **In the cage, Joaquin Buckley:** 44 of 148 sig. strikes (opponent 41); 0/0 takedowns; out-landed opponent in 3 round(s)
- **Why Kamaru Usman won:** Kamaru Usman won the fight on the numbers and the cards agreed: led takedowns 4-0, control time (min) 12.9-0.0.
- **Joaquin Buckley:** Joaquin Buckley had real success (significant strikes 44-41) but it was not enough on the scorecards.
- **Verdict: Wrong on a toss-up.** The model saw this as close to 50/50 and leaned the wrong way.

### 2025-06-21 · Jamahal Hill vs Khalil Rountree Jr.
_UFC Fight Night: Hill vs. Rountree Jr. · Light Heavyweight Bout_

- **Result:** Khalil Rountree Jr. by Decision - Unanimous (R5 5:00). **Win type:** Clear win via striking; stats support for the winner 86%.
- **Model before the fight** (trained on 8,068 earlier fights): Jamahal Hill 72% / Khalil Rountree Jr. 28%. Picked Jamahal Hill ❌
- **Pushing toward Jamahal Hill** (their number first): Recent striking form (last ~3 fights) (1.63 vs -1.11, ≈6.2 pts); Recent strength of schedule (last ~3 opponents) (1631.79 vs 1595.09, ≈3.4 pts); Strength of schedule (avg opponent Elo) (1606 vs 1537, ≈2.3 pts); Net striking margin (landed - absorbed / min) (2.34 vs -0.70, ≈2.2 pts)
- **Pushing toward Khalil Rountree Jr.** (their number first): UFC experience (fights) (15 vs 9, ≈1.7 pts); Recent results vs expectation (opponent-adjusted) (0.17 vs 0.05, ≈1.6 pts); Chin risk (KD absorbed / 15 min) (0.23 vs 0.47, ≈1.5 pts); Elo rating (quality of wins) (1641 vs 1630, ≈0.8 pts)
- **In the cage, Jamahal Hill:** 69 of 172 sig. strikes (opponent 102); 0 knockdown(s) scored, 1 suffered; out-landed opponent in 0 round(s)
- **In the cage, Khalil Rountree Jr.:** 102 of 181 sig. strikes (opponent 69); 1 knockdown(s) scored, 0 suffered; out-landed opponent in 4 round(s)
- **Why Khalil Rountree Jr. won:** Khalil Rountree Jr. won the fight on the numbers and the cards agreed: led significant strikes 102-69, knockdowns 1-0.
- **Jamahal Hill:** Jamahal Hill did not win any of the main stat battles. Was knocked down 1 time(s).
- **Verdict: Wrong: the model misread the matchup.** The model's main reasons pointed to Jamahal Hill, but Khalil Rountree Jr. won a clear win via striking (stats support 86%), so this was a genuine miss rather than bad luck.

### 2025-06-28 · Alexandre Pantoja vs Kai Kara-France
_UFC 317: Topuria vs. Oliveira · UFC Flyweight Title Bout_

- **Result:** Alexandre Pantoja by Submission (R3 1:55). **Win type:** Dominant finish via grappling; stats support for the winner 92%.
- **Model before the fight** (trained on 8,080 earlier fights): Alexandre Pantoja 58% / Kai Kara-France 42%. Picked Alexandre Pantoja ✅
- **Pushing toward Alexandre Pantoja** (their number first): Recent grappling control (79% vs 28%, ≈5.9 pts); Elo rating (quality of wins) (1783 vs 1620, ≈4.9 pts); Takedowns landed / 15 min (2.66 vs 0.69, ≈4.9 pts); Win / loss streak (+7 vs +1, ≈3.4 pts)
- **Pushing toward Kai Kara-France** (their number first): Recent results (last ~3 fights) (58% vs 85%, ≈6.2 pts); Striking defense (65% vs 50%, ≈4.8 pts); Age (32.3 vs 35.2, ≈3.5 pts); Age past 32 (decline years) (0.3 vs 3.2, ≈3.3 pts)
- **In the cage, Alexandre Pantoja:** 42 of 76 sig. strikes (opponent 38); 3/6 takedowns; 7:20 control; 2 submission attempt(s); out-landed opponent in 1 round(s)
- **In the cage, Kai Kara-France:** 38 of 67 sig. strikes (opponent 42); 0/2 takedowns; 0:10 control; out-landed opponent in 2 round(s)
- **Why Alexandre Pantoja won:** Alexandre Pantoja was winning the fight (significant strikes 42-38, takedowns 3-0, control time (min) 7.3-0.2) and finished it: Submission (Rear Naked Choke), R3 1:55.
- **Kai Kara-France:** Kai Kara-France did not win any of the main stat battles.
- **Verdict: Right for the right reasons.** The model expected Alexandre Pantoja to have the grappling edge, and that is how the fight was won (grappling).

### 2025-06-28 · Ilia Topuria vs Charles Oliveira
_UFC 317: Topuria vs. Oliveira · UFC Lightweight Title Bout_

- **Result:** Ilia Topuria by KO/TKO (R1 2:27). **Win type:** Dominant finish via striking; stats support for the winner 88%.
- **Model before the fight** (trained on 8,080 earlier fights): Ilia Topuria 74% / Charles Oliveira 26%. Picked Ilia Topuria ✅
- **Pushing toward Ilia Topuria** (their number first): Times finished (0 vs 8, ≈6.4 pts); Age (28.4 vs 35.7, ≈5.4 pts); Recent results vs expectation (opponent-adjusted) (0.47 vs 0.04, ≈5.0 pts); Win / loss streak (+8 vs +1, ≈4.5 pts)
- **Pushing toward Charles Oliveira** (their number first): UFC experience (fights) (33 vs 8, ≈5.6 pts); Recent results (last ~3 fights) (68% vs 90%, ≈4.2 pts); Reach (188 cm vs 175 cm, ≈1.8 pts); Takedown accuracy (40% vs 55%, ≈1.5 pts)
- **In the cage, Ilia Topuria:** 21 of 29 sig. strikes (opponent 9); 1 knockdown(s) scored, 0 suffered; 0/0 takedowns; 1:01 control; out-landed opponent in 1 round(s)
- **In the cage, Charles Oliveira:** 9 of 16 sig. strikes (opponent 21); 0 knockdown(s) scored, 1 suffered; 0/2 takedowns; 0:21 control; out-landed opponent in 0 round(s)
- **Why Ilia Topuria won:** Ilia Topuria was winning the fight (significant strikes 21-9, knockdowns 1-0, control time (min) 1.0-0.3) and finished it: KO/TKO (Punch to Head At Distance), R1 2:27.
- **Charles Oliveira:** Charles Oliveira did not win any of the main stat battles. Was knocked down 1 time(s).
- **Verdict: Right for the right reasons.** The model expected Ilia Topuria to have the striking edge, and that is how the fight was won (striking).

### 2025-07-12 · Derrick Lewis vs Tallison Teixeira
_UFC Fight Night: Lewis vs. Teixeira · Heavyweight Bout_

- **Result:** Derrick Lewis by KO/TKO (R1 0:35). **Win type:** Quick finish via mixed; stats support for the winner 79%.
- **Model before the fight** (trained on 8,091 earlier fights): Derrick Lewis 21% / Tallison Teixeira 79%. Picked Tallison Teixeira ❌
- **Pushing toward Derrick Lewis** (their number first): Recent strength of schedule (last ~3 opponents) (1613.91 vs 1511.54, ≈5.4 pts); UFC experience (fights) (29 vs 1, ≈5.4 pts); Recent results (last ~3 fights) (51% vs 75%, ≈3.9 pts); Elo rating (quality of wins) (1671 vs 1541, ≈2.9 pts)
- **Pushing toward Tallison Teixeira** (their number first): Age (25.6 vs 40.4, ≈11.9 pts); Times finished (0 vs 9, ≈6.2 pts); Age past 32 (decline years) (0.0 vs 8.4, ≈4.3 pts); Striking defense (56% vs 41%, ≈3.3 pts)
- **In the cage, Derrick Lewis:** 9 of 17 sig. strikes (opponent 3); 1 knockdown(s) scored, 0 suffered; 0:12 control; out-landed opponent in 1 round(s)
- **In the cage, Tallison Teixeira:** 3 of 5 sig. strikes (opponent 9); 0 knockdown(s) scored, 1 suffered; out-landed opponent in 0 round(s)
- **Why Derrick Lewis won:** Derrick Lewis ended it almost immediately: KO/TKO (Punches to Head On Ground), R1 0:35. Too short for stats to tell the story.
- **Tallison Teixeira:** Tallison Teixeira did not win any of the main stat battles. Was knocked down 1 time(s).
- **Verdict: Wrong on a fight-changing moment.** Derrick Lewis won with a quick finish — a single moment that pre-fight averages cannot see coming.

### 2025-07-19 · Max Holloway vs Dustin Poirier
_UFC 318: Holloway vs. Poirier 3 · Lightweight Bout_

- **Result:** Max Holloway by Decision - Unanimous (R5 5:00). **Win type:** Clear win via striking; stats support for the winner 99%.
- **Model before the fight** (trained on 8,103 earlier fights): Max Holloway 70% / Dustin Poirier 30%. Picked Max Holloway ✅
- **Pushing toward Max Holloway** (their number first): Recent striking form (last ~3 fights) (2.01 vs -0.40, ≈5.2 pts); Times finished (2 vs 7, ≈4.6 pts); Age (33.6 vs 36.5, ≈2.8 pts); Age past 32 (decline years) (1.6 vs 4.5, ≈2.6 pts)
- **Pushing toward Dustin Poirier** (their number first): Takedowns landed / 15 min (1.31 vs 0.29, ≈2.6 pts); UFC cage time (minutes) (323 vs 483, ≈1.7 pts); Recent results (last ~3 fights) (53% vs 60%, ≈1.4 pts); Reach (183 cm vs 175 cm, ≈1.3 pts)
- **In the cage, Max Holloway:** 198 of 375 sig. strikes (opponent 109); 1 knockdown(s) scored, 1 suffered; 0/0 takedowns; 1:32 control; out-landed opponent in 5 round(s)
- **In the cage, Dustin Poirier:** 109 of 255 sig. strikes (opponent 198); 1 knockdown(s) scored, 1 suffered; 0/1 takedowns; 0:12 control; 1 submission attempt(s); out-landed opponent in 0 round(s)
- **Why Max Holloway won:** Max Holloway won the fight on the numbers and the cards agreed: led significant strikes 198-109, control time (min) 1.5-0.2.
- **Dustin Poirier:** Dustin Poirier did not win any of the main stat battles.
- **Verdict: Right for the right reasons.** The model expected Max Holloway to have the striking edge, and that is how the fight was won (striking).

### 2025-07-26 · Shara Magomedov vs Marc-Andre Barriault
_UFC Fight Night: Whittaker vs. De Ridder · Middleweight Bout_

- **Result:** Shara Magomedov by Decision - Unanimous (R3 5:00). **Win type:** Clear win via striking; stats support for the winner 94%.
- **Model before the fight** (trained on 8,117 earlier fights): Shara Magomedov 68% / Marc-Andre Barriault 32%. Picked Shara Magomedov ✅
- **Pushing toward Shara Magomedov** (their number first): Times finished (0 vs 4, ≈3.6 pts); Age (31.2 vs 35.4, ≈3.6 pts); Elo rating (quality of wins) (1589 vs 1486, ≈3.4 pts); Age past 32 (decline years) (0.0 vs 3.4, ≈3.0 pts)
- **Pushing toward Marc-Andre Barriault** (their number first): Recent results (last ~3 fights) (47% vs 65%, ≈4.1 pts); UFC experience (fights) (14 vs 5, ≈2.3 pts); Striking defense (52% vs 44%, ≈2.2 pts); Win / loss streak (+1 vs -1, ≈1.0 pts)
- **In the cage, Shara Magomedov:** 93 of 142 sig. strikes (opponent 39); 0/1 takedowns; 0:57 control; out-landed opponent in 3 round(s)
- **In the cage, Marc-Andre Barriault:** 39 of 77 sig. strikes (opponent 93); 2/6 takedowns; 4:30 control; out-landed opponent in 0 round(s)
- **Why Shara Magomedov won:** Shara Magomedov won the fight on the numbers and the cards agreed: led significant strikes 93-39.
- **Marc-Andre Barriault:** Marc-Andre Barriault had real success (takedowns 2-0, control time (min) 4.5-0.9) but it was not enough on the scorecards.
- **Verdict: Right for the right reasons.** The model expected Shara Magomedov to have the striking edge, and that is how the fight was won (striking).

### 2025-07-26 · Robert Whittaker vs Reinier de Ridder
_UFC Fight Night: Whittaker vs. De Ridder · Middleweight Bout_

- **Result:** Reinier de Ridder by Decision - Split (R5 5:00). **Win type:** Coin-flip decision via grappling; stats support for the winner 54%.
- **Model before the fight** (trained on 8,117 earlier fights): Robert Whittaker 48% / Reinier de Ridder 52%. Picked Reinier de Ridder ✅
- **Pushing toward Robert Whittaker** (their number first): Recent results (last ~3 fights) (58% vs 85%, ≈7.0 pts); Recent strength of schedule (last ~3 opponents) (1661.57 vs 1584.61, ≈6.5 pts); Elo rating (quality of wins) (1773 vs 1638, ≈5.5 pts); UFC experience (fights) (23 vs 3, ≈5.3 pts)
- **Pushing toward Reinier de Ridder** (their number first): Recent results vs expectation (opponent-adjusted) (0.42 vs -0.04, ≈7.0 pts); Takedowns landed / 15 min (3.43 vs 0.83, ≈6.7 pts); Finishing rate (82% vs 26%, ≈4.3 pts); Times finished (0 vs 4, ≈4.1 pts)
- **In the cage, Robert Whittaker:** 66 of 142 sig. strikes (opponent 67); 1 knockdown(s) scored, 0 suffered; 0/0 takedowns; 0:36 control; out-landed opponent in 3 round(s)
- **In the cage, Reinier de Ridder:** 67 of 145 sig. strikes (opponent 66); 0 knockdown(s) scored, 1 suffered; 2/15 takedowns; 9:06 control; out-landed opponent in 2 round(s)
- **Why Reinier de Ridder won:** Reinier de Ridder got the nod in a fight the stats call nearly even (Reinier de Ridder: significant strikes 67-66, takedowns 2-0, control time (min) 9.1-0.6; Robert Whittaker: knockdowns 1-0).
- **Robert Whittaker:** Robert Whittaker had real success (knockdowns 1-0) but it was not enough on the scorecards.
- **Verdict: Right winner, different route.** The model expected a striking edge for Reinier de Ridder, but the fight was actually won by grappling.

### 2025-08-02 · Tatsuro Taira vs HyunSung Park
_UFC Fight Night: Taira vs. Park · Flyweight Bout_

- **Result:** Tatsuro Taira by Submission (R2 1:06). **Win type:** Dominant finish via grappling; stats support for the winner 95%.
- **Model before the fight** (trained on 8,129 earlier fights): Tatsuro Taira 60% / HyunSung Park 40%. Picked Tatsuro Taira ✅
- **Pushing toward Tatsuro Taira** (their number first): Recent strength of schedule (last ~3 opponents) (1552.25 vs 1480.55, ≈6.3 pts); Age (25.5 vs 29.7, ≈4.1 pts); Recent results (last ~3 fights) (69% vs 85%, ≈3.9 pts); Takedowns landed / 15 min (2.54 vs 1.32, ≈3.3 pts)
- **Pushing toward HyunSung Park** (their number first): Striking defense (63% vs 48%, ≈5.1 pts); Recent striking form (last ~3 fights) (0.72 vs -0.60, ≈4.5 pts); Recent results vs expectation (opponent-adjusted) (0.29 vs 0.13, ≈2.3 pts); Win / loss streak (+3 vs -1, ≈2.2 pts)
- **In the cage, Tatsuro Taira:** 7 of 11 sig. strikes (opponent 3); 1 knockdown(s) scored, 0 suffered; 4/5 takedowns; 4:41 control; 1 submission attempt(s); out-landed opponent in 1 round(s)
- **In the cage, HyunSung Park:** 3 of 9 sig. strikes (opponent 7); 0 knockdown(s) scored, 1 suffered; 0/0 takedowns; out-landed opponent in 0 round(s)
- **Why Tatsuro Taira won:** Tatsuro Taira was winning the fight (significant strikes 7-3, knockdowns 1-0, takedowns 4-0, control time (min) 4.7-0.0) and finished it: Submission (Neck Crank From Back Control), R2 1:06.
- **HyunSung Park:** HyunSung Park did not win any of the main stat battles. Was knocked down 1 time(s).
- **Verdict: Right, on overall profile.** The model backed Tatsuro Taira mainly on overall profile (quality of opposition, age, experience, form) rather than a specific matchup edge, and Tatsuro Taira won via grappling.

### 2025-08-09 · Roman Dolidze vs Anthony Hernandez
_UFC Fight Night: Dolidze vs. Hernandez · Middleweight Bout_

- **Result:** Anthony Hernandez by Submission (R4 2:45). **Win type:** Dominant finish via grappling; stats support for the winner 100%.
- **Model before the fight** (trained on 8,141 earlier fights): Roman Dolidze 23% / Anthony Hernandez 77%. Picked Anthony Hernandez ✅
- **Pushing toward Roman Dolidze** (their number first): Recent results (last ~3 fights) (73% vs 85%, ≈2.3 pts); Times finished (0 vs 2, ≈1.7 pts); Strength of schedule (avg opponent Elo) (1577 vs 1560, ≈0.8 pts); Recent strength of schedule (last ~3 opponents) (1610.26 vs 1601.80, ≈0.8 pts)
- **Pushing toward Anthony Hernandez** (their number first): Takedowns landed / 15 min (5.72 vs 1.14, ≈9.3 pts); Recent striking form (last ~3 fights) (2.00 vs 0.11, ≈3.7 pts); Age (31.8 vs 37.1, ≈3.6 pts); Age past 32 (decline years) (0.0 vs 5.1, ≈3.1 pts)
- **In the cage, Roman Dolidze:** 36 of 107 sig. strikes (opponent 91); 0/1 takedowns; 0:45 control; out-landed opponent in 0 round(s)
- **In the cage, Anthony Hernandez:** 91 of 152 sig. strikes (opponent 36); 9/11 takedowns; 7:48 control; 1 submission attempt(s); out-landed opponent in 4 round(s)
- **Why Anthony Hernandez won:** Anthony Hernandez was winning the fight (significant strikes 91-36, takedowns 9-0, control time (min) 7.8-0.8) and finished it: Submission (Rear Naked Choke), R4 2:45.
- **Roman Dolidze:** Roman Dolidze did not win any of the main stat battles.
- **Verdict: Right for the right reasons.** The model expected Anthony Hernandez to have the grappling edge, and that is how the fight was won (grappling).

### 2025-08-16 · Alibi Idiris vs Joseph Morales
_UFC 319: Du Plessis vs. Chimaev · Ultimate Fighter 33 Flyweight Tournament Title Bout_

- **Result:** Joseph Morales by Submission (R2 3:04). **Win type:** Dominant finish via grappling; stats support for the winner 82%.
- **Model before the fight** (trained on 8,153 earlier fights): Alibi Idiris 58% / Joseph Morales 42%. Picked Alibi Idiris ❌
- **Pushing toward Alibi Idiris** (their number first): Recent results vs expectation (opponent-adjusted) (0.00 vs -0.18, ≈2.8 pts); Recent grappling control (50% vs 20%, ≈2.3 pts); Takedowns landed / 15 min (1.50 vs 0.86, ≈2.0 pts); Takedown defense (62% vs 36%, ≈1.9 pts)
- **Pushing toward Joseph Morales** (their number first): Recent results (last ~3 fights) (33% vs 50%, ≈4.3 pts); Grappling control share (20% vs 50%, ≈1.5 pts); Striking defense (59% vs 55%, ≈1.2 pts); UFC experience (fights) (3 vs 0, ≈1.0 pts)
- **In the cage, Alibi Idiris:** 28 of 56 sig. strikes (opponent 29); 0/1 takedowns; 1:04 control; out-landed opponent in 1 round(s)
- **In the cage, Joseph Morales:** 29 of 63 sig. strikes (opponent 28); 2/5 takedowns; 3:38 control; 2 submission attempt(s); out-landed opponent in 1 round(s)
- **Why Joseph Morales won:** Joseph Morales was winning the fight (significant strikes 29-28, takedowns 2-0, control time (min) 3.6-1.1) and finished it: Submission (Triangle Choke From Bottom Guard), R2 3:04.
- **Alibi Idiris:** Alibi Idiris did not win any of the main stat battles.
- **Verdict: Wrong: the model misread the matchup.** The model's main reasons pointed to Alibi Idiris, but Joseph Morales won a dominant finish via grappling (stats support 82%), so this was a genuine miss rather than bad luck.

### 2025-08-16 · Dricus Du Plessis vs Khamzat Chimaev
_UFC 319: Du Plessis vs. Chimaev · UFC Middleweight Title Bout_

- **Result:** Khamzat Chimaev by Decision - Unanimous (R5 5:00). **Win type:** Clear win via grappling; stats support for the winner 100%.
- **Model before the fight** (trained on 8,153 earlier fights): Dricus Du Plessis 50% / Khamzat Chimaev 50%. Picked Khamzat Chimaev ✅
- **Pushing toward Dricus Du Plessis** (their number first): Striking defense (54% vs 44%, ≈3.7 pts); Elo rating (quality of wins) (1854 vs 1818, ≈1.7 pts); Title fight experience (3 vs 0, ≈1.5 pts); Strength of schedule (avg opponent Elo) (1659 vs 1632, ≈1.4 pts)
- **Pushing toward Khamzat Chimaev** (their number first): Takedowns landed / 15 min (3.65 vs 2.43, ≈3.4 pts); Takedown defense (81% vs 56%, ≈2.1 pts); Striking accuracy (57% vs 49%, ≈1.8 pts); Recent grappling control (87% vs 70%, ≈1.4 pts)
- **In the cage, Dricus Du Plessis:** 13 of 29 sig. strikes (opponent 37); 1/1 takedowns; 0:53 control; 1 submission attempt(s); out-landed opponent in 1 round(s)
- **In the cage, Khamzat Chimaev:** 37 of 47 sig. strikes (opponent 13); 12/17 takedowns; 21:40 control; out-landed opponent in 4 round(s)
- **Why Khamzat Chimaev won:** Khamzat Chimaev won the fight on the numbers and the cards agreed: led significant strikes 37-13, takedowns 12-1, control time (min) 21.7-0.9.
- **Dricus Du Plessis:** Dricus Du Plessis did not win any of the main stat battles.
- **Verdict: Right for the right reasons.** The model expected Khamzat Chimaev to have the grappling edge, and that is how the fight was won (grappling).

### 2025-09-06 · Nassourdine Imavov vs Caio Borralho
_UFC Fight Night: Imavov vs. Borralho · Middleweight Bout_

- **Result:** Nassourdine Imavov by Decision - Unanimous (R5 5:00). **Win type:** Competitive win via striking; stats support for the winner 81%.
- **Model before the fight** (trained on 8,177 earlier fights): Nassourdine Imavov 65% / Caio Borralho 35%. Picked Nassourdine Imavov ✅
- **Pushing toward Nassourdine Imavov** (their number first): Recent strength of schedule (last ~3 opponents) (1659.02 vs 1577.48, ≈6.4 pts); Age (29.5 vs 32.6, ≈3.4 pts); Strength of schedule (avg opponent Elo) (1616 vs 1557, ≈2.4 pts); Elo rating (quality of wins) (1765 vs 1722, ≈2.4 pts)
- **Pushing toward Caio Borralho** (their number first): Recent grappling control (74% vs 41%, ≈2.6 pts); Recent striking form (last ~3 fights) (1.26 vs 0.90, ≈1.6 pts); UFC win percentage (89% vs 75%, ≈1.6 pts); Takedowns landed / 15 min (1.38 vs 0.91, ≈1.5 pts)
- **In the cage, Nassourdine Imavov:** 81 of 162 sig. strikes (opponent 66); 0/0 takedowns; 0:29 control; out-landed opponent in 3 round(s)
- **In the cage, Caio Borralho:** 66 of 166 sig. strikes (opponent 81); 0/5 takedowns; 1:20 control; out-landed opponent in 2 round(s)
- **Why Nassourdine Imavov won:** Nassourdine Imavov edged it: led significant strikes 81-66, while Caio Borralho took control time (min) 1.3-0.5.
- **Caio Borralho:** Caio Borralho had real success (control time (min) 1.3-0.5) but it was not enough on the scorecards.
- **Verdict: Right, on overall profile.** The model backed Nassourdine Imavov mainly on overall profile (quality of opposition, age, experience, form) rather than a specific matchup edge, and Nassourdine Imavov won via striking.

### 2025-09-13 · Diego Lopes vs Jean Silva
_Noche UFC: Lopes vs. Silva · Featherweight Bout_

- **Result:** Diego Lopes by KO/TKO (R2 4:48). **Win type:** Dominant finish via mixed; stats support for the winner 98%.
- **Model before the fight** (trained on 8,190 earlier fights): Diego Lopes 51% / Jean Silva 49%. Picked Diego Lopes ✅
- **Pushing toward Diego Lopes** (their number first): Recent strength of schedule (last ~3 opponents) (1657.79 vs 1553.34, ≈7.4 pts); Recent results (last ~3 fights) (64% vs 87%, ≈6.2 pts); Strength of schedule (avg opponent Elo) (1633 vs 1537, ≈4.1 pts); Recent grappling control (52% vs 38%, ≈1.3 pts)
- **Pushing toward Jean Silva** (their number first): Recent striking form (last ~3 fights) (0.41 vs -0.82, ≈4.4 pts); Age (28.7 vs 30.7, ≈2.9 pts); Win / loss streak (+4 vs -1, ≈2.6 pts); Striking defense (55% vs 48%, ≈2.4 pts)
- **In the cage, Diego Lopes:** 74 of 135 sig. strikes (opponent 43); 1 knockdown(s) scored, 0 suffered; 3/4 takedowns; 2:40 control; out-landed opponent in 1 round(s)
- **In the cage, Jean Silva:** 43 of 91 sig. strikes (opponent 74); 0 knockdown(s) scored, 1 suffered; 0/0 takedowns; 0:03 control; out-landed opponent in 1 round(s)
- **Why Diego Lopes won:** Diego Lopes was winning the fight (significant strikes 74-43, knockdowns 1-0, takedowns 3-0, control time (min) 2.7-0.1) and finished it: KO/TKO (Punches to Head On Ground), R2 4:48.
- **Jean Silva:** Jean Silva did not win any of the main stat battles. Was knocked down 1 time(s).
- **Verdict: Right, on overall profile.** The model backed Diego Lopes mainly on overall profile (quality of opposition, age, experience, form) rather than a specific matchup edge, and Diego Lopes won via mixed.

### 2025-09-13 · Rodrigo Sezinando vs Daniil Donchenko
_Noche UFC: Lopes vs. Silva · Ultimate Fighter 33 Welterweight Tournament Title Bout_

- **Result:** Daniil Donchenko by KO/TKO (R1 4:27). **Win type:** Dominant finish via striking; stats support for the winner 94%.
- **Model before the fight** (trained on 8,190 earlier fights): Rodrigo Sezinando 46% / Daniil Donchenko 54%. Picked Daniil Donchenko ✅
- **Pushing toward Rodrigo Sezinando** (their number first): Recent strength of schedule (last ~3 opponents) (1500.00 vs 1500.00, ≈0.1 pts); Net striking margin (landed - absorbed / min) (0.00 vs 0.00, ≈0.1 pts); Age past 32 (decline years) (0.0 vs 0.0, ≈0.1 pts); Striking defense (55% vs 55%, ≈0.0 pts)
- **Pushing toward Daniil Donchenko** (their number first): Age (24.1 vs 27.8, ≈3.9 pts); Height (180 cm vs 175 cm, ≈0.3 pts); Recent striking form (last ~3 fights) (0.00 vs 0.00, ≈0.1 pts); Strength of schedule (avg opponent Elo) (1500 vs 1500, ≈0.1 pts)
- **In the cage, Rodrigo Sezinando:** 10 of 36 sig. strikes (opponent 39); 0 knockdown(s) scored, 1 suffered; 1/4 takedowns; 1:02 control; out-landed opponent in 0 round(s)
- **In the cage, Daniil Donchenko:** 39 of 68 sig. strikes (opponent 10); 1 knockdown(s) scored, 0 suffered; 1/3 takedowns; 1:03 control; out-landed opponent in 1 round(s)
- **Why Daniil Donchenko won:** Daniil Donchenko was winning the fight (significant strikes 39-10, knockdowns 1-0, control time (min) 1.1-1.0) and finished it: KO/TKO (Punches to Head At Distance), R1 4:27.
- **Rodrigo Sezinando:** Rodrigo Sezinando did not win any of the main stat battles. Was knocked down 1 time(s).
- **Verdict: Right, on overall profile.** The model backed Daniil Donchenko mainly on overall profile (quality of opposition, age, experience, form) rather than a specific matchup edge, and Daniil Donchenko won via striking.

### 2025-09-27 · Carlos Ulberg vs Dominick Reyes
_UFC Fight Night: Ulberg vs. Reyes · Light Heavyweight Bout_

- **Result:** Carlos Ulberg by KO/TKO (R1 4:27). **Win type:** Dominant finish via striking; stats support for the winner 79%.
- **Model before the fight** (trained on 8,203 earlier fights): Carlos Ulberg 49% / Dominick Reyes 51%. Picked Dominick Reyes ❌
- **Pushing toward Carlos Ulberg** (their number first): Recent results vs expectation (opponent-adjusted) (0.37 vs 0.17, ≈3.7 pts); Elo rating (quality of wins) (1743 vs 1696, ≈2.8 pts); Times finished (1 vs 3, ≈2.6 pts); Win / loss streak (+8 vs +3, ≈2.4 pts)
- **Pushing toward Dominick Reyes** (their number first): Recent results (last ~3 fights) (65% vs 87%, ≈6.2 pts); Recent striking form (last ~3 fights) (2.08 vs 1.13, ≈3.4 pts); Recent strength of schedule (last ~3 opponents) (1621.84 vs 1595.08, ≈3.2 pts); Strength of schedule (avg opponent Elo) (1614 vs 1555, ≈2.4 pts)
- **In the cage, Carlos Ulberg:** 11 of 17 sig. strikes (opponent 5); 1 knockdown(s) scored, 0 suffered; 0:03 control; out-landed opponent in 1 round(s)
- **In the cage, Dominick Reyes:** 5 of 11 sig. strikes (opponent 11); 0 knockdown(s) scored, 1 suffered; out-landed opponent in 0 round(s)
- **Why Carlos Ulberg won:** Carlos Ulberg was winning the fight (significant strikes 11-5, knockdowns 1-0, control time (min) 0.1-0.0) and finished it: KO/TKO (Punches to Head At Distance), R1 4:27.
- **Dominick Reyes:** Dominick Reyes did not win any of the main stat battles. Was knocked down 1 time(s).
- **Verdict: Wrong on a toss-up.** The model saw this as close to 50/50 and leaned the wrong way.

### 2025-10-04 · Merab Dvalishvili vs Cory Sandhagen
_UFC 320: Ankalaev vs. Pereira 2 · UFC Bantamweight Title Bout_

- **Result:** Merab Dvalishvili by Decision - Unanimous (R5 5:00). **Win type:** Clear win via mixed; stats support for the winner 100%.
- **Model before the fight** (trained on 8,215 earlier fights): Merab Dvalishvili 69% / Cory Sandhagen 31%. Picked Merab Dvalishvili ✅
- **Pushing toward Merab Dvalishvili** (their number first): Takedowns landed / 15 min (5.59 vs 1.30, ≈11.9 pts); Win / loss streak (+13 vs +1, ≈7.6 pts); Recent results vs expectation (opponent-adjusted) (0.37 vs 0.14, ≈3.4 pts); Elo rating (quality of wins) (1865 vs 1782, ≈3.0 pts)
- **Pushing toward Cory Sandhagen** (their number first): Recent results (last ~3 fights) (65% vs 90%, ≈5.6 pts); Strength of schedule (avg opponent Elo) (1662 vs 1610, ≈2.0 pts); Age (33.5 vs 34.7, ≈1.7 pts); Finishing rate (46% vs 14%, ≈1.5 pts)
- **In the cage, Merab Dvalishvili:** 114 of 265 sig. strikes (opponent 80); 20/37 takedowns; 10:02 control; out-landed opponent in 4 round(s)
- **In the cage, Cory Sandhagen:** 80 of 184 sig. strikes (opponent 114); 0/0 takedowns; out-landed opponent in 1 round(s)
- **Why Merab Dvalishvili won:** Merab Dvalishvili won the fight on the numbers and the cards agreed: led significant strikes 114-80, takedowns 20-0, control time (min) 10.0-0.0.
- **Cory Sandhagen:** Cory Sandhagen did not win any of the main stat battles.
- **Verdict: Right for the right reasons.** The model expected Merab Dvalishvili to have the grappling edge, and that is how the fight was won (mixed).

### 2025-10-04 · Magomed Ankalaev vs Alex Pereira
_UFC 320: Ankalaev vs. Pereira 2 · UFC Light Heavyweight Title Bout_

- **Result:** Alex Pereira by KO/TKO (R1 1:20). **Win type:** Quick finish via mixed; stats support for the winner 87%.
- **Model before the fight** (trained on 8,215 earlier fights): Magomed Ankalaev 62% / Alex Pereira 38%. Picked Magomed Ankalaev ❌
- **Pushing toward Magomed Ankalaev** (their number first): Recent grappling control (82% vs 17%, ≈6.5 pts); Age past 32 (decline years) (1.3 vs 6.2, ≈5.0 pts); Age (33.3 vs 38.2, ≈5.0 pts); Elo rating (quality of wins) (1842 vs 1795, ≈2.9 pts)
- **Pushing toward Alex Pereira** (their number first): Recent results (last ~3 fights) (68% vs 86%, ≈4.5 pts); Strength of schedule (avg opponent Elo) (1680 vs 1599, ≈3.3 pts); Recent strength of schedule (last ~3 opponents) (1684.92 vs 1652.88, ≈2.7 pts); Reach (201 cm vs 190 cm, ≈2.4 pts)
- **In the cage, Magomed Ankalaev:** 4 of 9 sig. strikes (opponent 28); 0/1 takedowns; out-landed opponent in 0 round(s)
- **In the cage, Alex Pereira:** 28 of 45 sig. strikes (opponent 4); 0/0 takedowns; 0:17 control; out-landed opponent in 1 round(s)
- **Why Alex Pereira won:** Alex Pereira ended it almost immediately: KO/TKO (Elbows to Head From Half Guard), R1 1:20. Too short for stats to tell the story.
- **Magomed Ankalaev:** Magomed Ankalaev did not win any of the main stat battles.
- **Verdict: Wrong on a fight-changing moment.** Alex Pereira won with a quick finish — a single moment that pre-fight averages cannot see coming.

### 2025-10-11 · Charles Oliveira vs Mateusz Gamrot
_UFC Fight Night: Oliveira vs. Gamrot · Lightweight Bout_

- **Result:** Charles Oliveira by Submission (R2 2:48). **Win type:** Comeback finish via grappling; stats support for the winner 45%.
- **Model before the fight** (trained on 8,229 earlier fights): Charles Oliveira 39% / Mateusz Gamrot 61%. Picked Mateusz Gamrot ❌
- **Pushing toward Charles Oliveira** (their number first): UFC experience (fights) (34 vs 11, ≈5.2 pts); Recent strength of schedule (last ~3 opponents) (1692.11 vs 1639.37, ≈4.6 pts); Recent results (last ~3 fights) (56% vs 69%, ≈3.6 pts); Elo rating (quality of wins) (1818 vs 1726, ≈3.5 pts)
- **Pushing toward Mateusz Gamrot** (their number first): Times finished (0 vs 9, ≈8.3 pts); Takedowns landed / 15 min (4.95 vs 2.19, ≈7.9 pts); Recent results vs expectation (opponent-adjusted) (0.19 vs -0.06, ≈4.2 pts); Recent striking form (last ~3 fights) (0.52 vs -0.22, ≈3.6 pts)
- **In the cage, Charles Oliveira:** 11 of 33 sig. strikes (opponent 18); 1/1 takedowns; 3:35 control; 1 submission attempt(s); out-landed opponent in 0 round(s)
- **In the cage, Mateusz Gamrot:** 18 of 42 sig. strikes (opponent 11); 1/1 takedowns; 1:00 control; out-landed opponent in 2 round(s)
- **Why Charles Oliveira won:** Charles Oliveira was behind (Mateusz Gamrot led significant strikes 18-11) but ended it with one decisive moment: Submission (Rear Naked Choke), R2 2:48.
- **Mateusz Gamrot:** Mateusz Gamrot had real success (significant strikes 18-11) but was finished.
- **Verdict: Wrong on a fight-changing moment.** Charles Oliveira won with a comeback finish — a single moment that pre-fight averages cannot see coming.

### 2025-10-18 · Reinier de Ridder vs Brendan Allen
_UFC Fight Night: De Ridder vs. Allen · Middleweight Bout_

- **Result:** Brendan Allen by KO/TKO (R4 5:00). **Win type:** Dominant finish via striking; stats support for the winner 89%.
- **Model before the fight** (trained on 8,241 earlier fights): Reinier de Ridder 53% / Brendan Allen 47%. Picked Reinier de Ridder ❌
- **Pushing toward Reinier de Ridder** (their number first): Recent results vs expectation (opponent-adjusted) (0.46 vs 0.05, ≈6.9 pts); Times finished (0 vs 2, ≈2.6 pts); Takedowns landed / 15 min (2.53 vs 1.59, ≈2.5 pts); UFC cage time (minutes) (47 vs 188, ≈2.0 pts)
- **Pushing toward Brendan Allen** (their number first): Recent results (last ~3 fights) (64% vs 87%, ≈6.1 pts); Age (29.8 vs 35.1, ≈6.1 pts); Age past 32 (decline years) (0.0 vs 3.1, ≈4.0 pts); UFC experience (fights) (17 vs 4, ≈3.7 pts)
- **In the cage, Reinier de Ridder:** 9 of 13 sig. strikes (opponent 22); 3/7 takedowns; 7:05 control; 1 submission attempt(s); out-landed opponent in 1 round(s)
- **In the cage, Brendan Allen:** 22 of 37 sig. strikes (opponent 9); 1/1 takedowns; 11:39 control; 1 submission attempt(s); out-landed opponent in 3 round(s)
- **Why Brendan Allen won:** Brendan Allen was winning the fight (significant strikes 22-9, control time (min) 11.7-7.1) and finished it: KO/TKO (toCorner stoppage between rounds), R4 5:00.
- **Reinier de Ridder:** Reinier de Ridder had real success (takedowns 3-1) but was finished.
- **Verdict: Wrong on a toss-up.** The model saw this as close to 50/50 and leaned the wrong way.

### 2025-10-25 · Virna Jandiroba vs Mackenzie Dern
_UFC 321: Aspinall vs. Gane · UFC Women's Strawweight Title Bout_

- **Result:** Mackenzie Dern by Decision - Unanimous (R5 5:00). **Win type:** Contested decision via striking; stats support for the winner 18%.
- **Model before the fight** (trained on 8,254 earlier fights): Virna Jandiroba 57% / Mackenzie Dern 43%. Picked Virna Jandiroba ❌
- **Pushing toward Virna Jandiroba** (their number first): Recent results vs expectation (opponent-adjusted) (0.32 vs 0.10, ≈3.8 pts); Takedowns landed / 15 min (2.28 vs 0.93, ≈3.5 pts); Chin risk (KD absorbed / 15 min) (0.03 vs 0.44, ≈2.9 pts); Elo rating (quality of wins) (1708 vs 1637, ≈2.9 pts)
- **Pushing toward Mackenzie Dern** (their number first): Age past 32 (decline years) (0.6 vs 5.4, ≈5.0 pts); Recent results (last ~3 fights) (61% vs 80%, ≈5.0 pts); Age (32.6 vs 37.4, ≈4.8 pts); Recent striking form (last ~3 fights) (-0.19 vs -0.41, ≈1.9 pts)
- **In the cage, Virna Jandiroba:** 106 of 217 sig. strikes (opponent 118); 9/17 takedowns; 9:07 control; out-landed opponent in 2 round(s)
- **In the cage, Mackenzie Dern:** 118 of 231 sig. strikes (opponent 106); 2/8 takedowns; 3:45 control; out-landed opponent in 3 round(s)
- **Why Mackenzie Dern won:** Mackenzie Dern got the decision even though Virna Jandiroba led takedowns 9-2, control time (min) 9.1-3.8; this is a contested result, not a clean win.
- **Virna Jandiroba:** Virna Jandiroba had real success (takedowns 9-2, control time (min) 9.1-3.8) but it was not enough on the scorecards.
- **Verdict: Wrong, but the result was razor-close.** The in-fight stats only gave Mackenzie Dern a 18% case for the decision. The model's pick was arguably as deserving as the official winner.

### 2025-11-01 · Steve Garcia vs David Onama
_UFC Fight Night: Garcia vs. Onama · Featherweight Bout_

- **Result:** Steve Garcia by KO/TKO (R1 3:34). **Win type:** Dominant finish via mixed; stats support for the winner 96%.
- **Model before the fight** (trained on 8,266 earlier fights): Steve Garcia 52% / David Onama 48%. Picked Steve Garcia ✅
- **Pushing toward Steve Garcia** (their number first): Recent striking form (last ~3 fights) (2.30 vs 0.64, ≈5.3 pts); Striking defense (61% vs 52%, ≈2.6 pts); Takedown defense (74% vs 54%, ≈1.7 pts); Finishing rate (63% vs 37%, ≈1.7 pts)
- **Pushing toward David Onama** (their number first): Chin risk (KD absorbed / 15 min) (0.17 vs 1.11, ≈4.3 pts); Age (31.4 vs 33.4, ≈2.6 pts); Recent grappling control (59% vs 37%, ≈1.6 pts); Recent strength of schedule (last ~3 opponents) (1545.16 vs 1528.05, ≈1.6 pts)
- **In the cage, Steve Garcia:** 33 of 62 sig. strikes (opponent 2); 1 knockdown(s) scored, 0 suffered; 0:04 control; out-landed opponent in 1 round(s)
- **In the cage, David Onama:** 2 of 16 sig. strikes (opponent 33); 0 knockdown(s) scored, 1 suffered; out-landed opponent in 0 round(s)
- **Why Steve Garcia won:** Steve Garcia was winning the fight (significant strikes 33-2, knockdowns 1-0, control time (min) 0.1-0.0) and finished it: KO/TKO (Punches to Head On Ground), R1 3:34.
- **David Onama:** David Onama did not win any of the main stat battles. Was knocked down 1 time(s).
- **Verdict: Right for the right reasons.** The model expected Steve Garcia to have the striking edge, and that is how the fight was won (mixed).

### 2025-11-08 · Gabriel Bonfim vs Randy Brown
_UFC Fight Night: Bonfim vs. Brown · Welterweight Bout_

- **Result:** Gabriel Bonfim by KO/TKO (R2 1:40). **Win type:** Dominant finish via striking; stats support for the winner 69%.
- **Model before the fight** (trained on 8,279 earlier fights): Gabriel Bonfim 67% / Randy Brown 33%. Picked Gabriel Bonfim ✅
- **Pushing toward Gabriel Bonfim** (their number first): Takedowns landed / 15 min (3.49 vs 0.83, ≈7.4 pts); Age (28.2 vs 35.3, ≈5.8 pts); Age past 32 (decline years) (0.0 vs 3.3, ≈3.7 pts); Times finished (1 vs 4, ≈3.3 pts)
- **Pushing toward Randy Brown** (their number first): UFC experience (fights) (20 vs 6, ≈3.0 pts); Elo rating (quality of wins) (1732 vs 1660, ≈2.9 pts); Reach (198 cm vs 183 cm, ≈2.4 pts); Recent results (last ~3 fights) (69% vs 78%, ≈2.2 pts)
- **In the cage, Gabriel Bonfim:** 35 of 64 sig. strikes (opponent 33); 1 knockdown(s) scored, 0 suffered; out-landed opponent in 1 round(s)
- **In the cage, Randy Brown:** 33 of 87 sig. strikes (opponent 35); 0 knockdown(s) scored, 1 suffered; out-landed opponent in 1 round(s)
- **Why Gabriel Bonfim won:** Gabriel Bonfim was winning the fight (significant strikes 35-33, knockdowns 1-0) and finished it: KO/TKO (Knee to Head In Clinch), R2 1:40.
- **Randy Brown:** Randy Brown did not win any of the main stat battles. Was knocked down 1 time(s).
- **Verdict: Right winner, different route.** The model expected a grappling edge for Gabriel Bonfim, but the fight was actually won by striking.

### 2025-11-15 · Jack Della Maddalena vs Islam Makhachev
_UFC 322: Della Maddalena vs. Makhachev · UFC Welterweight Title Bout_

- **Result:** Islam Makhachev by Decision - Unanimous (R5 5:00). **Win type:** Clear win via grappling; stats support for the winner 99%.
- **Model before the fight** (trained on 8,291 earlier fights): Jack Della Maddalena 34% / Islam Makhachev 66%. Picked Islam Makhachev ✅
- **Pushing toward Jack Della Maddalena** (their number first): Age (29.2 vs 34.1, ≈4.2 pts); Recent striking form (last ~3 fights) (1.49 vs 0.55, ≈3.5 pts); Takedown accuracy (27% vs 52%, ≈2.4 pts); Age past 32 (decline years) (0.0 vs 2.1, ≈2.3 pts)
- **Pushing toward Islam Makhachev** (their number first): Win / loss streak (+15 vs +8, ≈6.7 pts); Takedowns landed / 15 min (3.07 vs 0.40, ≈6.5 pts); Elo rating (quality of wins) (1979 vs 1806, ≈6.1 pts); Recent grappling control (80% vs 24%, ≈4.4 pts)
- **In the cage, Jack Della Maddalena:** 18 of 61 sig. strikes (opponent 30); 0/1 takedowns; out-landed opponent in 2 round(s)
- **In the cage, Islam Makhachev:** 30 of 57 sig. strikes (opponent 18); 4/4 takedowns; 19:10 control; out-landed opponent in 3 round(s)
- **Why Islam Makhachev won:** Islam Makhachev won the fight on the numbers and the cards agreed: led significant strikes 30-18, takedowns 4-0, control time (min) 19.2-0.0.
- **Jack Della Maddalena:** Jack Della Maddalena did not win any of the main stat battles.
- **Verdict: Right for the right reasons.** The model expected Islam Makhachev to have the grappling edge, and that is how the fight was won (grappling).

### 2025-11-15 · Valentina Shevchenko vs Zhang Weili
_UFC 322: Della Maddalena vs. Makhachev · UFC Women's Flyweight Title Bout_

- **Result:** Valentina Shevchenko by Decision - Unanimous (R5 5:00). **Win type:** Clear win via grappling; stats support for the winner 99%.
- **Model before the fight** (trained on 8,291 earlier fights): Valentina Shevchenko 46% / Zhang Weili 54%. Picked Zhang Weili ❌
- **Pushing toward Valentina Shevchenko** (their number first): Striking defense (63% vs 54%, ≈2.8 pts); Title fight experience (13 vs 8, ≈2.5 pts); UFC experience (fights) (18 vs 12, ≈2.2 pts); Recent results (last ~3 fights) (76% vs 81%, ≈1.3 pts)
- **Pushing toward Zhang Weili** (their number first): Recent striking form (last ~3 fights) (2.19 vs 0.79, ≈4.7 pts); UFC cage time (minutes) (174 vs 337, ≈2.4 pts); Recent results vs expectation (opponent-adjusted) (0.30 vs 0.17, ≈2.3 pts); Win / loss streak (+5 vs +2, ≈1.5 pts)
- **In the cage, Valentina Shevchenko:** 41 of 68 sig. strikes (opponent 32); 5/6 takedowns; 13:24 control; out-landed opponent in 3 round(s)
- **In the cage, Zhang Weili:** 32 of 98 sig. strikes (opponent 41); 0/1 takedowns; 0:46 control; out-landed opponent in 2 round(s)
- **Why Valentina Shevchenko won:** Valentina Shevchenko won the fight on the numbers and the cards agreed: led significant strikes 41-32, takedowns 5-0, control time (min) 13.4-0.8.
- **Zhang Weili:** Zhang Weili did not win any of the main stat battles.
- **Verdict: Wrong on a toss-up.** The model saw this as close to 50/50 and leaned the wrong way.

### 2025-11-22 · Arman Tsarukyan vs Dan Hooker
_UFC Fight Night: Tsarukyan vs. Hooker · Lightweight Bout_

- **Result:** Arman Tsarukyan by Submission (R2 3:34). **Win type:** Dominant finish via grappling; stats support for the winner 98%.
- **Model before the fight** (trained on 8,305 earlier fights): Arman Tsarukyan 76% / Dan Hooker 24%. Picked Arman Tsarukyan ✅
- **Pushing toward Arman Tsarukyan** (their number first): Age (29.1 vs 35.8, ≈4.8 pts); Takedowns landed / 15 min (3.08 vs 0.78, ≈4.0 pts); Times finished (0 vs 4, ≈3.2 pts); Age past 32 (decline years) (0.0 vs 3.8, ≈3.0 pts)
- **Pushing toward Dan Hooker** (their number first): Recent results (last ~3 fights) (66% vs 82%, ≈3.2 pts); UFC experience (fights) (22 vs 11, ≈2.3 pts); Height (183 cm vs 170 cm, ≈1.2 pts); Reach (190 cm vs 183 cm, ≈0.7 pts)
- **In the cage, Arman Tsarukyan:** 42 of 60 sig. strikes (opponent 10); 2/4 takedowns; 6:02 control; 1 submission attempt(s); out-landed opponent in 2 round(s)
- **In the cage, Dan Hooker:** 10 of 33 sig. strikes (opponent 42); 0/0 takedowns; 0:10 control; 2 submission attempt(s); out-landed opponent in 0 round(s)
- **Why Arman Tsarukyan won:** Arman Tsarukyan was winning the fight (significant strikes 42-10, takedowns 2-0, control time (min) 6.0-0.2) and finished it: Submission (Arm Triangle From Mount), R2 3:34.
- **Dan Hooker:** Dan Hooker did not win any of the main stat battles.
- **Verdict: Right, on overall profile.** The model backed Arman Tsarukyan mainly on overall profile (quality of opposition, age, experience, form) rather than a specific matchup edge, and Arman Tsarukyan won via grappling.

### 2025-12-06 · Merab Dvalishvili vs Petr Yan
_UFC 323: Dvalishvili vs. Yan 2 · UFC Bantamweight Title Bout_

- **Result:** Petr Yan by Decision - Unanimous (R5 5:00). **Win type:** Coin-flip decision via striking; stats support for the winner 47%.
- **Model before the fight** (trained on 8,319 earlier fights): Merab Dvalishvili 71% / Petr Yan 29%. Picked Merab Dvalishvili ❌
- **Pushing toward Merab Dvalishvili** (their number first): Takedowns landed / 15 min (6.15 vs 1.57, ≈11.3 pts); Win / loss streak (+14 vs +3, ≈6.8 pts); Elo rating (quality of wins) (1890 vs 1756, ≈4.5 pts); Recent striking form (last ~3 fights) (1.32 vs 0.53, ≈3.2 pts)
- **Pushing toward Petr Yan** (their number first): Recent results (last ~3 fights) (66% vs 90%, ≈5.4 pts); Age past 32 (decline years) (0.8 vs 2.9, ≈2.8 pts); Age (32.8 vs 34.9, ≈2.4 pts); Striking accuracy (54% vs 43%, ≈2.2 pts)
- **In the cage, Merab Dvalishvili:** 134 of 383 sig. strikes (opponent 139); 2/29 takedowns; 5:12 control; 2 submission attempt(s); out-landed opponent in 1 round(s)
- **In the cage, Petr Yan:** 139 of 230 sig. strikes (opponent 134); 5/9 takedowns; 2:55 control; out-landed opponent in 4 round(s)
- **Why Petr Yan won:** Petr Yan got the nod in a fight the stats call nearly even (Petr Yan: significant strikes 139-134, takedowns 5-2; Merab Dvalishvili: control time (min) 5.2-2.9).
- **Merab Dvalishvili:** Merab Dvalishvili had real success (control time (min) 5.2-2.9) but it was not enough on the scorecards.
- **Verdict: Wrong, but the result was razor-close.** The in-fight stats only gave Petr Yan a 47% case for the decision. The model's pick was arguably as deserving as the official winner.

### 2025-12-06 · Alexandre Pantoja vs Joshua Van
_UFC 323: Dvalishvili vs. Yan 2 · UFC Flyweight Title Bout_

- **Result:** Joshua Van by KO/TKO (R1 0:26). **Win type:** Quick finish via mixed; stats support for the winner 40%.
- **Model before the fight** (trained on 8,319 earlier fights): Alexandre Pantoja 48% / Joshua Van 52%. Picked Joshua Van ✅
- **Pushing toward Alexandre Pantoja** (their number first): Elo rating (quality of wins) (1805 vs 1690, ≈4.9 pts); Takedowns landed / 15 min (2.71 vs 0.92, ≈4.5 pts); Recent grappling control (82% vs 46%, ≈3.1 pts); UFC experience (fights) (17 vs 9, ≈3.0 pts)
- **Pushing toward Joshua Van** (their number first): Age (24.2 vs 35.6, ≈12.0 pts); Recent striking form (last ~3 fights) (1.71 vs 0.23, ≈5.2 pts); Age past 32 (decline years) (0.0 vs 3.6, ≈4.0 pts); Striking defense (58% vs 50%, ≈2.7 pts)
- **In the cage, Alexandre Pantoja:** 6 of 11 sig. strikes (opponent 2); out-landed opponent in 1 round(s)
- **In the cage, Joshua Van:** 2 of 4 sig. strikes (opponent 6); out-landed opponent in 0 round(s)
- **Why Joshua Van won:** Joshua Van ended it almost immediately: KO/TKO (to On GroundArm injury to Pantoja), R1 0:26. Too short for stats to tell the story.
- **Alexandre Pantoja:** Alexandre Pantoja had real success (significant strikes 6-2) but was finished.
- **Verdict: Right for the right reasons.** The model expected Joshua Van to have the striking edge, and that is how the fight was won (mixed).

### 2025-12-13 · Brandon Royval vs Manel Kape
_UFC Fight Night: Royval vs. Kape · Flyweight Bout_

- **Result:** Manel Kape by KO/TKO (R1 3:18). **Win type:** Dominant finish via mixed; stats support for the winner 68%.
- **Model before the fight** (trained on 8,332 earlier fights): Brandon Royval 42% / Manel Kape 58%. Picked Manel Kape ✅
- **Pushing toward Brandon Royval** (their number first): Recent strength of schedule (last ~3 opponents) (1626.56 vs 1569.41, ≈4.1 pts); Recent results (last ~3 fights) (57% vs 72%, ≈4.1 pts); Strength of schedule (avg opponent Elo) (1599 vs 1555, ≈2.3 pts); Title fight experience (1 vs 0, ≈1.6 pts)
- **Pushing toward Manel Kape** (their number first): Striking defense (58% vs 44%, ≈4.3 pts); Recent results vs expectation (opponent-adjusted) (0.25 vs 0.11, ≈2.4 pts); Striking accuracy (55% vs 41%, ≈2.4 pts); Times finished (0 vs 2, ≈2.3 pts)
- **In the cage, Brandon Royval:** 17 of 26 sig. strikes (opponent 17); 0 knockdown(s) scored, 1 suffered; out-landed opponent in 0 round(s)
- **In the cage, Manel Kape:** 17 of 23 sig. strikes (opponent 17); 1 knockdown(s) scored, 0 suffered; 0:04 control; out-landed opponent in 0 round(s)
- **Why Manel Kape won:** Manel Kape was winning the fight (knockdowns 1-0, control time (min) 0.1-0.0) and finished it: KO/TKO (Punches to Head On Ground), R1 3:18.
- **Brandon Royval:** Brandon Royval did not win any of the main stat battles. Was knocked down 1 time(s).
- **Verdict: Right for the right reasons.** The model expected Manel Kape to have the striking edge, and that is how the fight was won (mixed).

### 2026-01-24 · Justin Gaethje vs Paddy Pimblett
_UFC 324: Gaethje vs. Pimblett · UFC Interim Lightweight Title Bout_

- **Result:** Justin Gaethje by Decision - Unanimous (R5 5:00). **Win type:** Clear win via mixed; stats support for the winner 98%.
- **Model before the fight** (trained on 8,343 earlier fights): Justin Gaethje 41% / Paddy Pimblett 59%. Picked Paddy Pimblett ❌
- **Pushing toward Justin Gaethje** (their number first): Recent strength of schedule (last ~3 opponents) (1713.54 vs 1567.17, ≈7.4 pts); Recent results (last ~3 fights) (63% vs 90%, ≈7.2 pts); Strength of schedule (avg opponent Elo) (1715 vs 1552, ≈6.2 pts); Striking defense (52% vs 44%, ≈2.9 pts)
- **Pushing toward Paddy Pimblett** (their number first): Recent striking form (last ~3 fights) (1.83 vs -0.59, ≈6.4 pts); Age (31.1 vs 37.2, ≈6.4 pts); Times finished (0 vs 5, ≈5.5 pts); Age past 32 (decline years) (0.0 vs 5.2, ≈4.3 pts)
- **In the cage, Justin Gaethje:** 144 of 254 sig. strikes (opponent 156); 2 knockdown(s) scored, 0 suffered; 3/3 takedowns; 5:55 control; out-landed opponent in 2 round(s)
- **In the cage, Paddy Pimblett:** 156 of 311 sig. strikes (opponent 144); 0 knockdown(s) scored, 2 suffered; 0/5 takedowns; 0:48 control; out-landed opponent in 3 round(s)
- **Why Justin Gaethje won:** Justin Gaethje won the fight on the numbers and the cards agreed: led knockdowns 2-0, takedowns 3-0, control time (min) 5.9-0.8.
- **Paddy Pimblett:** Paddy Pimblett had real success (significant strikes 156-144) but it was not enough on the scorecards.
- **Verdict: Wrong: the model misread the matchup.** The model's main reasons pointed to Paddy Pimblett, but Justin Gaethje won a clear win via mixed (stats support 98%), so this was a genuine miss rather than bad luck.

### 2026-01-31 · Alexander Volkanovski vs Diego Lopes
_UFC 325: Volkanovski vs. Lopes 2 · UFC Featherweight Title Bout_

- **Result:** Alexander Volkanovski by Decision - Unanimous (R5 5:00). **Win type:** Clear win via striking; stats support for the winner 98%.
- **Model before the fight** (trained on 8,354 earlier fights): Alexander Volkanovski 64% / Diego Lopes 36%. Picked Alexander Volkanovski ✅
- **Pushing toward Alexander Volkanovski** (their number first): Recent striking form (last ~3 fights) (2.18 vs -0.19, ≈6.3 pts); Recent strength of schedule (last ~3 opponents) (1721.26 vs 1650.59, ≈5.8 pts); Elo rating (quality of wins) (1828 vs 1711, ≈4.9 pts); Striking defense (59% vs 48%, ≈3.4 pts)
- **Pushing toward Diego Lopes** (their number first): Age (31.1 vs 37.3, ≈6.8 pts); Age past 32 (decline years) (0.0 vs 5.3, ≈5.3 pts); Recent results vs expectation (opponent-adjusted) (0.27 vs 0.02, ≈4.4 pts); UFC cage time (minutes) (84 vs 278, ≈3.4 pts)
- **In the cage, Alexander Volkanovski:** 98 of 160 sig. strikes (opponent 70); 2/7 takedowns; 2:49 control; 1 submission attempt(s); out-landed opponent in 4 round(s)
- **In the cage, Diego Lopes:** 70 of 158 sig. strikes (opponent 98); 2/5 takedowns; 1:50 control; out-landed opponent in 0 round(s)
- **Why Alexander Volkanovski won:** Alexander Volkanovski won the fight on the numbers and the cards agreed: led significant strikes 98-70, control time (min) 2.8-1.8.
- **Diego Lopes:** Diego Lopes did not win any of the main stat battles.
- **Verdict: Right for the right reasons.** The model expected Alexander Volkanovski to have the striking edge, and that is how the fight was won (striking).

### 2026-02-07 · Mario Bautista vs Vinicius Oliveira
_UFC Fight Night: Bautista vs. Oliveira · Bantamweight Bout_

- **Result:** Mario Bautista by Submission (R2 4:46). **Win type:** Dominant finish via grappling; stats support for the winner 90%.
- **Model before the fight** (trained on 8,367 earlier fights): Mario Bautista 36% / Vinicius Oliveira 64%. Picked Vinicius Oliveira ❌
- **Pushing toward Mario Bautista** (their number first): Recent results (last ~3 fights) (70% vs 87%, ≈4.7 pts); UFC experience (fights) (13 vs 4, ≈2.7 pts); Elo rating (quality of wins) (1704 vs 1651, ≈2.6 pts); Takedown accuracy (33% vs 46%, ≈1.1 pts)
- **Pushing toward Vinicius Oliveira** (their number first): Recent results vs expectation (opponent-adjusted) (0.42 vs 0.14, ≈4.9 pts); Age (30.2 vs 32.6, ≈2.9 pts); Times finished (0 vs 2, ≈2.3 pts); Win / loss streak (+4 vs -1, ≈2.1 pts)
- **In the cage, Mario Bautista:** 15 of 27 sig. strikes (opponent 12); 5/7 takedowns; 5:47 control; 1 submission attempt(s); out-landed opponent in 1 round(s)
- **In the cage, Vinicius Oliveira:** 12 of 21 sig. strikes (opponent 15); 0/1 takedowns; 1:39 control; out-landed opponent in 1 round(s)
- **Why Mario Bautista won:** Mario Bautista was winning the fight (significant strikes 15-12, takedowns 5-0, control time (min) 5.8-1.6) and finished it: Submission (Rear Naked Choke), R2 4:46.
- **Vinicius Oliveira:** Vinicius Oliveira did not win any of the main stat battles.
- **Verdict: Wrong: the model misread the matchup.** The model's main reasons pointed to Vinicius Oliveira, but Mario Bautista won a dominant finish via grappling (stats support 90%), so this was a genuine miss rather than bad luck.

### 2026-02-21 · Sean Strickland vs Anthony Hernandez
_UFC Fight Night: Strickland vs. Hernandez · Middleweight Bout_

- **Result:** Sean Strickland by KO/TKO (R3 2:23). **Win type:** Dominant finish via mixed; stats support for the winner 100%.
- **Model before the fight** (trained on 8,380 earlier fights): Sean Strickland 18% / Anthony Hernandez 82%. Picked Anthony Hernandez ❌
- **Pushing toward Sean Strickland** (their number first): Recent results (last ~3 fights) (54% vs 86%, ≈5.3 pts); UFC experience (fights) (23 vs 11, ≈2.3 pts); Recent strength of schedule (last ~3 opponents) (1667.07 vs 1618.71, ≈2.2 pts); Striking defense (61% vs 50%, ≈1.9 pts)
- **Pushing toward Anthony Hernandez** (their number first): Takedowns landed / 15 min (5.96 vs 0.76, ≈9.4 pts); Win / loss streak (+8 vs -1, ≈5.0 pts); Recent results vs expectation (opponent-adjusted) (0.38 vs 0.02, ≈4.0 pts); UFC cage time (minutes) (125 vs 369, ≈3.0 pts)
- **In the cage, Sean Strickland:** 110 of 241 sig. strikes (opponent 55); 1 knockdown(s) scored, 0 suffered; 0/0 takedowns; 0:18 control; out-landed opponent in 3 round(s)
- **In the cage, Anthony Hernandez:** 55 of 122 sig. strikes (opponent 110); 0 knockdown(s) scored, 1 suffered; 0/1 takedowns; 0:32 control; out-landed opponent in 0 round(s)
- **Why Sean Strickland won:** Sean Strickland was winning the fight (significant strikes 110-55, knockdowns 1-0) and finished it: KO/TKO (Punches to Head On Ground), R3 2:23.
- **Anthony Hernandez:** Anthony Hernandez had real success (control time (min) 0.5-0.3) but was finished.
- **Verdict: Wrong: the model misread the matchup.** The model's main reasons pointed to Anthony Hernandez, but Sean Strickland won a dominant finish via mixed (stats support 100%), so this was a genuine miss rather than bad luck.

### 2026-02-28 · Brandon Moreno vs Lone'er Kavanagh
_UFC Fight Night: Moreno vs. Kavanagh · Flyweight Bout_

- **Result:** Lone'er Kavanagh by Decision - Unanimous (R5 5:00). **Win type:** Contested decision via striking; stats support for the winner 30%.
- **Model before the fight** (trained on 8,394 earlier fights): Brandon Moreno 60% / Lone'er Kavanagh 40%. Picked Brandon Moreno ❌
- **Pushing toward Brandon Moreno** (their number first): Elo rating (quality of wins) (1684 vs 1520, ≈6.4 pts); Recent strength of schedule (last ~3 opponents) (1624.43 vs 1510.77, ≈6.4 pts); Strength of schedule (avg opponent Elo) (1621 vs 1507, ≈5.0 pts); UFC experience (fights) (19 vs 3, ≈3.7 pts)
- **Pushing toward Lone'er Kavanagh** (their number first): Age (26.7 vs 32.2, ≈5.7 pts); UFC cage time (minutes) (40 vs 316, ≈5.1 pts); Recent striking form (last ~3 fights) (0.46 vs 0.11, ≈2.0 pts); Recent grappling control (68% vs 48%, ≈1.5 pts)
- **In the cage, Brandon Moreno:** 79 of 168 sig. strikes (opponent 97); 0/8 takedowns; 7:20 control; out-landed opponent in 2 round(s)
- **In the cage, Lone'er Kavanagh:** 97 of 205 sig. strikes (opponent 79); 0/1 takedowns; out-landed opponent in 3 round(s)
- **Why Lone'er Kavanagh won:** Lone'er Kavanagh got the decision even though Brandon Moreno led control time (min) 7.3-0.0; this is a contested result, not a clean win.
- **Brandon Moreno:** Brandon Moreno had real success (control time (min) 7.3-0.0) but it was not enough on the scorecards.
- **Verdict: Wrong, but the result was razor-close.** The in-fight stats only gave Lone'er Kavanagh a 30% case for the decision. The model's pick was arguably as deserving as the official winner.

### 2026-03-07 · Max Holloway vs Charles Oliveira
_UFC 326: Holloway vs. Oliveira 2 · Lightweight Bout_

- **Result:** Charles Oliveira by Decision - Unanimous (R5 5:00). **Win type:** Clear win via grappling; stats support for the winner 100%.
- **Model before the fight** (trained on 8,407 earlier fights): Max Holloway 71% / Charles Oliveira 29%. Picked Max Holloway ❌
- **Pushing toward Max Holloway** (their number first): Times finished (2 vs 9, ≈6.1 pts); Recent striking form (last ~3 fights) (2.29 vs -0.30, ≈5.6 pts); Striking defense (59% vs 49%, ≈3.5 pts); Recent strength of schedule (last ~3 opponents) (1719.60 vs 1691.09, ≈2.3 pts)
- **Pushing toward Charles Oliveira** (their number first): UFC cage time (minutes) (270 vs 508, ≈3.9 pts); Takedowns landed / 15 min (2.18 vs 0.27, ≈3.6 pts); Reach (188 cm vs 175 cm, ≈1.4 pts); UFC experience (fights) (35 vs 31, ≈1.2 pts)
- **In the cage, Max Holloway:** 26 of 45 sig. strikes (opponent 50); 0/0 takedowns; 1:36 control; out-landed opponent in 0 round(s)
- **In the cage, Charles Oliveira:** 50 of 66 sig. strikes (opponent 26); 5/13 takedowns; 20:49 control; 4 submission attempt(s); out-landed opponent in 5 round(s)
- **Why Charles Oliveira won:** Charles Oliveira won the fight on the numbers and the cards agreed: led significant strikes 50-26, takedowns 5-0, control time (min) 20.8-1.6.
- **Max Holloway:** Max Holloway did not win any of the main stat battles.
- **Verdict: Wrong: the model misread the matchup.** The model's main reasons pointed to Max Holloway, but Charles Oliveira won a clear win via grappling (stats support 100%), so this was a genuine miss rather than bad luck.

### 2026-03-14 · Josh Emmett vs Kevin Vallejos
_UFC Fight Night: Emmett vs. Vallejos · Featherweight Bout_

- **Result:** Kevin Vallejos by KO/TKO (R1 3:33). **Win type:** Dominant finish via striking; stats support for the winner 98%.
- **Model before the fight** (trained on 8,419 earlier fights): Josh Emmett 22% / Kevin Vallejos 78%. Picked Kevin Vallejos ✅
- **Pushing toward Josh Emmett** (their number first): Recent results (last ~3 fights) (42% vs 85%, ≈8.4 pts); Recent strength of schedule (last ~3 opponents) (1640.40 vs 1546.04, ≈3.9 pts); Strength of schedule (avg opponent Elo) (1619 vs 1530, ≈3.0 pts); UFC experience (fights) (16 vs 3, ≈2.5 pts)
- **Pushing toward Kevin Vallejos** (their number first): Age (24.3 vs 41.0, ≈12.1 pts); Recent results vs expectation (opponent-adjusted) (0.38 vs -0.10, ≈6.2 pts); Age past 32 (decline years) (0.0 vs 9.0, ≈5.2 pts); Recent striking form (last ~3 fights) (0.66 vs -1.18, ≈3.5 pts)
- **In the cage, Josh Emmett:** 3 of 12 sig. strikes (opponent 36); 0 knockdown(s) scored, 2 suffered; 0/1 takedowns; out-landed opponent in 0 round(s)
- **In the cage, Kevin Vallejos:** 36 of 55 sig. strikes (opponent 3); 2 knockdown(s) scored, 0 suffered; 0/0 takedowns; 0:38 control; out-landed opponent in 1 round(s)
- **Why Kevin Vallejos won:** Kevin Vallejos was winning the fight (significant strikes 36-3, knockdowns 2-0, control time (min) 0.6-0.0) and finished it: KO/TKO (Punches to Head At Distance), R1 3:33.
- **Josh Emmett:** Josh Emmett did not win any of the main stat battles. Was knocked down 2 time(s).
- **Verdict: Right, on overall profile.** The model backed Kevin Vallejos mainly on overall profile (quality of opposition, age, experience, form) rather than a specific matchup edge, and Kevin Vallejos won via striking.

### 2026-03-21 · Movsar Evloev vs Lerone Murphy
_UFC Fight Night: Evloev vs. Murphy · Featherweight Bout_

- **Result:** Movsar Evloev by Decision - Majority (R5 5:00). **Win type:** Clear win via grappling; stats support for the winner 92%.
- **Model before the fight** (trained on 8,433 earlier fights): Movsar Evloev 64% / Lerone Murphy 36%. Picked Movsar Evloev ✅
- **Pushing toward Movsar Evloev** (their number first): Takedowns landed / 15 min (4.35 vs 1.42, ≈6.8 pts); Recent strength of schedule (last ~3 opponents) (1634.72 vs 1574.67, ≈4.3 pts); Age (32.1 vs 34.7, ≈3.5 pts); Age past 32 (decline years) (0.1 vs 2.7, ≈2.6 pts)
- **Pushing toward Lerone Murphy** (their number first): Recent striking form (last ~3 fights) (1.67 vs 0.82, ≈3.8 pts); Days since last fight (217 vs 469, ≈2.1 pts); Grappling control share (41% vs 79%, ≈1.6 pts); Finishing rate (30% vs 3%, ≈1.4 pts)
- **In the cage, Movsar Evloev:** 86 of 189 sig. strikes (opponent 89); 9/10 takedowns; 3:54 control; out-landed opponent in 2 round(s)
- **In the cage, Lerone Murphy:** 89 of 239 sig. strikes (opponent 86); 0/0 takedowns; out-landed opponent in 2 round(s)
- **Why Movsar Evloev won:** Movsar Evloev won the fight on the numbers and the cards agreed: led takedowns 9-0, control time (min) 3.9-0.0.
- **Lerone Murphy:** Lerone Murphy had real success (significant strikes 89-86) but it was not enough on the scorecards.
- **Verdict: Right for the right reasons.** The model expected Movsar Evloev to have the grappling edge, and that is how the fight was won (grappling).

### 2026-03-28 · Israel Adesanya vs Joe Pyfer
_UFC Fight Night: Adesanya vs. Pyfer · Middleweight Bout_

- **Result:** Joe Pyfer by KO/TKO (R2 4:18). **Win type:** Dominant finish via grappling; stats support for the winner 72%.
- **Model before the fight** (trained on 8,446 earlier fights): Israel Adesanya 45% / Joe Pyfer 55%. Picked Joe Pyfer ✅
- **Pushing toward Israel Adesanya** (their number first): Recent results (last ~3 fights) (40% vs 80%, ≈10.9 pts); Recent strength of schedule (last ~3 opponents) (1688.08 vs 1566.68, ≈7.0 pts); Strength of schedule (avg opponent Elo) (1684 vs 1550, ≈5.9 pts); UFC experience (fights) (18 vs 7, ≈3.5 pts)
- **Pushing toward Joe Pyfer** (their number first): Recent results vs expectation (opponent-adjusted) (0.28 vs -0.18, ≈8.7 pts); Age (29.5 vs 36.7, ≈7.4 pts); UFC cage time (minutes) (62 vs 316, ≈5.7 pts); Age past 32 (decline years) (0.0 vs 4.7, ≈4.4 pts)
- **In the cage, Israel Adesanya:** 42 of 75 sig. strikes (opponent 36); 0/2 takedowns; out-landed opponent in 1 round(s)
- **In the cage, Joe Pyfer:** 36 of 70 sig. strikes (opponent 42); 2/8 takedowns; 2:44 control; out-landed opponent in 1 round(s)
- **Why Joe Pyfer won:** Joe Pyfer was winning the fight (takedowns 2-0, control time (min) 2.7-0.0) and finished it: KO/TKO (Punches to Head From Mount), R2 4:18.
- **Israel Adesanya:** Israel Adesanya had real success (significant strikes 42-36) but was finished.
- **Verdict: Right, on overall profile.** The model backed Joe Pyfer mainly on overall profile (quality of opposition, age, experience, form) rather than a specific matchup edge, and Joe Pyfer won via grappling.

### 2026-04-04 · Renato Moicano vs Chris Duncan
_UFC Fight Night: Moicano vs. Duncan · Lightweight Bout_

- **Result:** Renato Moicano by Submission (R2 3:14). **Win type:** Dominant finish via grappling; stats support for the winner 67%.
- **Model before the fight** (trained on 8,458 earlier fights): Renato Moicano 52% / Chris Duncan 48%. Picked Renato Moicano ✅
- **Pushing toward Renato Moicano** (their number first): Recent results (last ~3 fights) (51% vs 82%, ≈8.6 pts); Recent strength of schedule (last ~3 opponents) (1668.60 vs 1538.44, ≈8.5 pts); UFC experience (fights) (19 vs 7, ≈3.9 pts); Strength of schedule (avg opponent Elo) (1615 vs 1529, ≈3.7 pts)
- **Pushing toward Chris Duncan** (their number first): Recent results vs expectation (opponent-adjusted) (0.29 vs 0.04, ≈4.8 pts); Age past 32 (decline years) (0.9 vs 4.9, ≈4.5 pts); Times finished (1 vs 5, ≈4.3 pts); Age (32.9 vs 36.9, ≈4.2 pts)
- **In the cage, Renato Moicano:** 21 of 36 sig. strikes (opponent 27); 1/4 takedowns; 3:16 control; 1 submission attempt(s); out-landed opponent in 0 round(s)
- **In the cage, Chris Duncan:** 27 of 62 sig. strikes (opponent 21); 0/2 takedowns; 0:01 control; out-landed opponent in 2 round(s)
- **Why Renato Moicano won:** Renato Moicano was winning the fight (takedowns 1-0, control time (min) 3.3-0.0) and finished it: Submission (Rear Naked Choke), R2 3:14.
- **Chris Duncan:** Chris Duncan had real success (significant strikes 27-21) but was finished.
- **Verdict: Right, on overall profile.** The model backed Renato Moicano mainly on overall profile (quality of opposition, age, experience, form) rather than a specific matchup edge, and Renato Moicano won via grappling.

### 2026-04-11 · Jiri Prochazka vs Carlos Ulberg
_UFC 327: Prochazka vs. Ulberg · UFC Light Heavyweight Title Bout_

- **Result:** Carlos Ulberg by KO/TKO (R1 3:45). **Win type:** Dominant finish via striking; stats support for the winner 87%.
- **Model before the fight** (trained on 8,471 earlier fights): Jiri Prochazka 47% / Carlos Ulberg 53%. Picked Carlos Ulberg ✅
- **Pushing toward Jiri Prochazka** (their number first): Recent results (last ~3 fights) (70% vs 88%, ≈5.2 pts); Recent strength of schedule (last ~3 opponents) (1660.75 vs 1610.26, ≈4.9 pts); Strength of schedule (avg opponent Elo) (1662 vs 1567, ≈4.2 pts); Age past 32 (decline years) (1.5 vs 3.4, ≈2.9 pts)
- **Pushing toward Carlos Ulberg** (their number first): Win / loss streak (+9 vs +2, ≈6.4 pts); Recent striking form (last ~3 fights) (1.08 vs 0.09, ≈4.0 pts); Elo rating (quality of wins) (1776 vs 1723, ≈2.5 pts); Chin risk (KD absorbed / 15 min) (0.21 vs 0.48, ≈2.0 pts)
- **In the cage, Jiri Prochazka:** 14 of 20 sig. strikes (opponent 27); 0 knockdown(s) scored, 1 suffered; out-landed opponent in 0 round(s)
- **In the cage, Carlos Ulberg:** 27 of 42 sig. strikes (opponent 14); 1 knockdown(s) scored, 0 suffered; 0:04 control; out-landed opponent in 1 round(s)
- **Why Carlos Ulberg won:** Carlos Ulberg was winning the fight (significant strikes 27-14, knockdowns 1-0, control time (min) 0.1-0.0) and finished it: KO/TKO (Punch to Head At Distance), R1 3:45.
- **Jiri Prochazka:** Jiri Prochazka did not win any of the main stat battles. Was knocked down 1 time(s).
- **Verdict: Right for the right reasons.** The model expected Carlos Ulberg to have the striking edge, and that is how the fight was won (striking).

### 2026-04-18 · Gilbert Burns vs Mike Malott
_UFC Fight Night: Burns vs. Malott · Welterweight Bout_

- **Result:** Mike Malott by KO/TKO (R3 2:08). **Win type:** Dominant finish via mixed; stats support for the winner 97%.
- **Model before the fight** (trained on 8,482 earlier fights): Gilbert Burns 32% / Mike Malott 68%. Picked Mike Malott ✅
- **Pushing toward Gilbert Burns** (their number first): Recent results (last ~3 fights) (33% vs 80%, ≈11.6 pts); Recent strength of schedule (last ~3 opponents) (1677.68 vs 1557.83, ≈6.8 pts); UFC experience (fights) (24 vs 7, ≈5.3 pts); Strength of schedule (avg opponent Elo) (1630 vs 1547, ≈3.3 pts)
- **Pushing toward Mike Malott** (their number first): Recent results vs expectation (opponent-adjusted) (0.27 vs -0.20, ≈7.7 pts); Win / loss streak (+3 vs -4, ≈5.1 pts); UFC cage time (minutes) (64 vs 296, ≈5.1 pts); Recent striking form (last ~3 fights) (0.67 vs -1.61, ≈5.0 pts)
- **In the cage, Gilbert Burns:** 40 of 92 sig. strikes (opponent 56); 0 knockdown(s) scored, 2 suffered; 0/7 takedowns; 0:01 control; out-landed opponent in 1 round(s)
- **In the cage, Mike Malott:** 56 of 121 sig. strikes (opponent 40); 2 knockdown(s) scored, 0 suffered; 0/0 takedowns; 0:14 control; out-landed opponent in 2 round(s)
- **Why Mike Malott won:** Mike Malott was winning the fight (significant strikes 56-40, knockdowns 2-0, control time (min) 0.2-0.0) and finished it: KO/TKO (Punches to Head On Ground), R3 2:08.
- **Gilbert Burns:** Gilbert Burns did not win any of the main stat battles. Was knocked down 2 time(s).
- **Verdict: Right, on overall profile.** The model backed Mike Malott mainly on overall profile (quality of opposition, age, experience, form) rather than a specific matchup edge, and Mike Malott won via mixed.

### 2026-04-25 · Aljamain Sterling vs Youssef Zalal
_UFC Fight Night: Sterling vs. Zalal · Featherweight Bout_

- **Result:** Aljamain Sterling by Decision - Unanimous (R5 5:00). **Win type:** Clear win via grappling; stats support for the winner 98%.
- **Model before the fight** (trained on 8,493 earlier fights): Aljamain Sterling 52% / Youssef Zalal 48%. Picked Aljamain Sterling ✅
- **Pushing toward Aljamain Sterling** (their number first): Recent strength of schedule (last ~3 opponents) (1672.17 vs 1562.50, ≈8.2 pts); Elo rating (quality of wins) (1823 vs 1679, ≈6.6 pts); Strength of schedule (avg opponent Elo) (1636 vs 1529, ≈4.3 pts); UFC experience (fights) (22 vs 12, ≈3.8 pts)
- **Pushing toward Youssef Zalal** (their number first): Age (29.6 vs 36.7, ≈7.2 pts); Age past 32 (decline years) (0.0 vs 4.7, ≈5.1 pts); Recent results vs expectation (opponent-adjusted) (0.29 vs 0.07, ≈4.2 pts); UFC cage time (minutes) (138 vs 306, ≈3.9 pts)
- **In the cage, Aljamain Sterling:** 46 of 89 sig. strikes (opponent 35); 6/11 takedowns; 13:49 control; 1 submission attempt(s); out-landed opponent in 2 round(s)
- **In the cage, Youssef Zalal:** 35 of 65 sig. strikes (opponent 46); 0/0 takedowns; 3:59 control; 1 submission attempt(s); out-landed opponent in 2 round(s)
- **Why Aljamain Sterling won:** Aljamain Sterling won the fight on the numbers and the cards agreed: led significant strikes 46-35, takedowns 6-0, control time (min) 13.8-4.0.
- **Youssef Zalal:** Youssef Zalal did not win any of the main stat battles.
- **Verdict: Right, on overall profile.** The model backed Aljamain Sterling mainly on overall profile (quality of opposition, age, experience, form) rather than a specific matchup edge, and Aljamain Sterling won via grappling.

### 2026-05-02 · Jack Della Maddalena vs Carlos Prates
_UFC Fight Night: Della Maddalena vs. Prates · Welterweight Bout_

- **Result:** Carlos Prates by KO/TKO (R3 3:17). **Win type:** Dominant finish via mixed; stats support for the winner 100%.
- **Model before the fight** (trained on 8,506 earlier fights): Jack Della Maddalena 70% / Carlos Prates 30%. Picked Jack Della Maddalena ❌
- **Pushing toward Jack Della Maddalena** (their number first): Recent strength of schedule (last ~3 opponents) (1721.67 vs 1660.88, ≈4.7 pts); Recent striking form (last ~3 fights) (0.85 vs -0.51, ≈4.1 pts); Striking defense (63% vs 49%, ≈3.8 pts); Age (29.6 vs 32.7, ≈3.4 pts)
- **Pushing toward Carlos Prates** (their number first): Reach (198 cm vs 185 cm, ≈2.8 pts); Takedown defense (79% vs 63%, ≈1.6 pts); Finishing rate (79% vs 53%, ≈1.4 pts); Recent grappling control (32% vs 12%, ≈1.4 pts)
- **In the cage, Jack Della Maddalena:** 41 of 76 sig. strikes (opponent 104); 0 knockdown(s) scored, 3 suffered; 2/5 takedowns; 1:13 control; out-landed opponent in 0 round(s)
- **In the cage, Carlos Prates:** 104 of 193 sig. strikes (opponent 41); 3 knockdown(s) scored, 0 suffered; 0/0 takedowns; 0:42 control; out-landed opponent in 3 round(s)
- **Why Carlos Prates won:** Carlos Prates was winning the fight (significant strikes 104-41, knockdowns 3-0) and finished it: KO/TKO (Elbows to Body From Half Guard), R3 3:17.
- **Jack Della Maddalena:** Jack Della Maddalena had real success (takedowns 2-0, control time (min) 1.2-0.7) but was finished.
- **Verdict: Wrong: the model misread the matchup.** The model's main reasons pointed to Jack Della Maddalena, but Carlos Prates won a dominant finish via mixed (stats support 100%), so this was a genuine miss rather than bad luck.

### 2026-05-09 · Joshua Van vs Tatsuro Taira
_UFC 328: Chimaev vs. Strickland · UFC Flyweight Title Bout_

- **Result:** Joshua Van by KO/TKO (R5 1:32). **Win type:** Dominant finish via striking; stats support for the winner 99%.
- **Model before the fight** (trained on 8,519 earlier fights): Joshua Van 56% / Tatsuro Taira 44%. Picked Joshua Van ✅
- **Pushing toward Joshua Van** (their number first): Recent striking form (last ~3 fights) (1.55 vs -0.05, ≈4.8 pts); Striking defense (58% vs 48%, ≈3.8 pts); Takedown defense (79% vs 51%, ≈2.5 pts); Age (24.6 vs 26.3, ≈1.9 pts)
- **Pushing toward Tatsuro Taira** (their number first): Takedowns landed / 15 min (2.90 vs 0.92, ≈5.0 pts); Recent grappling control (83% vs 46%, ≈3.1 pts); Reach (178 cm vs 165 cm, ≈3.0 pts); Recent results (last ~3 fights) (78% vs 86%, ≈2.1 pts)
- **In the cage, Joshua Van:** 131 of 209 sig. strikes (opponent 55); 2 knockdown(s) scored, 0 suffered; 1/2 takedowns; 1:21 control; 2 submission attempt(s); out-landed opponent in 4 round(s)
- **In the cage, Tatsuro Taira:** 55 of 151 sig. strikes (opponent 131); 0 knockdown(s) scored, 2 suffered; 8/21 takedowns; 10:38 control; out-landed opponent in 1 round(s)
- **Why Joshua Van won:** Joshua Van was winning the fight (significant strikes 131-55, knockdowns 2-0) and finished it: KO/TKO (Punches to Head At Distance), R5 1:32.
- **Tatsuro Taira:** Tatsuro Taira had real success (takedowns 8-1, control time (min) 10.6-1.4) but was finished.
- **Verdict: Right for the right reasons.** The model expected Joshua Van to have the striking edge, and that is how the fight was won (striking).

### 2026-05-09 · Khamzat Chimaev vs Sean Strickland
_UFC 328: Chimaev vs. Strickland · UFC Middleweight Title Bout_

- **Result:** Sean Strickland by Decision - Split (R5 5:00). **Win type:** Competitive win via striking; stats support for the winner 71%.
- **Model before the fight** (trained on 8,519 earlier fights): Khamzat Chimaev 87% / Sean Strickland 13%. Picked Khamzat Chimaev ❌
- **Pushing toward Khamzat Chimaev** (their number first): Takedowns landed / 15 min (4.65 vs 0.74, ≈6.0 pts); Win / loss streak (+9 vs +1, ≈3.4 pts); UFC cage time (minutes) (74 vs 382, ≈3.3 pts); Recent results vs expectation (opponent-adjusted) (0.46 vs 0.11, ≈2.9 pts)
- **Pushing toward Sean Strickland** (their number first): Recent results (last ~3 fights) (62% vs 90%, ≈3.6 pts); Striking defense (61% vs 45%, ≈2.4 pts); UFC experience (fights) (24 vs 9, ≈1.8 pts); Recent striking form (last ~3 fights) (1.24 vs 0.73, ≈0.9 pts)
- **In the cage, Khamzat Chimaev:** 98 of 240 sig. strikes (opponent 123); 9/13 takedowns; 7:16 control; out-landed opponent in 1 round(s)
- **In the cage, Sean Strickland:** 123 of 312 sig. strikes (opponent 98); 0/1 takedowns; 3:01 control; out-landed opponent in 3 round(s)
- **Why Sean Strickland won:** Sean Strickland edged it: led significant strikes 123-98, while Khamzat Chimaev took takedowns 9-0, control time (min) 7.3-3.0.
- **Khamzat Chimaev:** Khamzat Chimaev had real success (takedowns 9-0, control time (min) 7.3-3.0) but it was not enough on the scorecards.
- **Verdict: Wrong: the model misread the matchup.** The model's main reasons pointed to Khamzat Chimaev, but Sean Strickland won a competitive win via striking (stats support 71%), so this was a genuine miss rather than bad luck.

### 2026-05-16 · Arnold Allen vs Melquizael Costa
_UFC Fight Night: Allen vs. Costa · Featherweight Bout_

- **Result:** Arnold Allen by Decision - Unanimous (R5 5:00). **Win type:** Clear win via mixed; stats support for the winner 99%.
- **Model before the fight** (trained on 8,532 earlier fights): Arnold Allen 45% / Melquizael Costa 55%. Picked Melquizael Costa ❌
- **Pushing toward Arnold Allen** (their number first): Recent results (last ~3 fights) (54% vs 83%, ≈8.1 pts); Recent strength of schedule (last ~3 opponents) (1630.28 vs 1563.40, ≈5.2 pts); UFC experience (fights) (14 vs 9, ≈2.4 pts); Striking defense (60% vs 55%, ≈2.3 pts)
- **Pushing toward Melquizael Costa** (their number first): Recent results vs expectation (opponent-adjusted) (0.32 vs -0.03, ≈6.4 pts); Win / loss streak (+6 vs -1, ≈5.6 pts); Recent striking form (last ~3 fights) (1.06 vs -0.03, ≈4.8 pts); Age (29.7 vs 32.3, ≈3.8 pts)
- **In the cage, Arnold Allen:** 98 of 152 sig. strikes (opponent 100); 1 knockdown(s) scored, 0 suffered; 7/7 takedowns; 9:28 control; out-landed opponent in 1 round(s)
- **In the cage, Melquizael Costa:** 100 of 254 sig. strikes (opponent 98); 0 knockdown(s) scored, 1 suffered; 0/4 takedowns; 1:45 control; out-landed opponent in 2 round(s)
- **Why Arnold Allen won:** Arnold Allen won the fight on the numbers and the cards agreed: led knockdowns 1-0, takedowns 7-0, control time (min) 9.5-1.8.
- **Melquizael Costa:** Melquizael Costa had real success (significant strikes 100-98) but it was not enough on the scorecards.
- **Verdict: Wrong on a toss-up.** The model saw this as close to 50/50 and leaned the wrong way.

### 2026-06-06 · Belal Muhammad vs Gabriel Bonfim
_UFC Fight Night: Muhammad vs. Bonfim · Welterweight Bout_

- **Result:** Gabriel Bonfim by Decision - Unanimous (R5 5:00). **Win type:** Clear win via striking; stats support for the winner 96%.
- **Model before the fight** (trained on 8,557 earlier fights): Belal Muhammad 32% / Gabriel Bonfim 68%. Picked Gabriel Bonfim ✅
- **Pushing toward Belal Muhammad** (their number first): Recent results (last ~3 fights) (59% vs 82%, ≈5.7 pts); Recent strength of schedule (last ~3 opponents) (1703.29 vs 1609.92, ≈5.5 pts); Elo rating (quality of wins) (1804 vs 1707, ≈3.4 pts); UFC experience (fights) (20 vs 7, ≈3.2 pts)
- **Pushing toward Gabriel Bonfim** (their number first): Age (28.8 vs 37.9, ≈9.7 pts); Recent results vs expectation (opponent-adjusted) (0.36 vs 0.04, ≈5.5 pts); UFC cage time (minutes) (58 vs 323, ≈5.1 pts); Age past 32 (decline years) (0.0 vs 5.9, ≈4.7 pts)
- **In the cage, Belal Muhammad:** 86 of 275 sig. strikes (opponent 128); 0/2 takedowns; 0:08 control; out-landed opponent in 0 round(s)
- **In the cage, Gabriel Bonfim:** 128 of 260 sig. strikes (opponent 86); 0/1 takedowns; out-landed opponent in 5 round(s)
- **Why Gabriel Bonfim won:** Gabriel Bonfim won the fight on the numbers and the cards agreed: led significant strikes 128-86.
- **Belal Muhammad:** Belal Muhammad had real success (control time (min) 0.1-0.0) but it was not enough on the scorecards.
- **Verdict: Right, on overall profile.** The model backed Gabriel Bonfim mainly on overall profile (quality of opposition, age, experience, form) rather than a specific matchup edge, and Gabriel Bonfim won via striking.

### 2026-06-14 · Alex Pereira vs Ciryl Gane
_UFC Freedom 250 · UFC Interim Heavyweight Title Bout_

- **Result:** Ciryl Gane by KO/TKO (R2 1:27). **Win type:** Dominant finish via striking; stats support for the winner 98%.
- **Model before the fight** (trained on 8,569 earlier fights): Alex Pereira 40% / Ciryl Gane 60%. Picked Ciryl Gane ✅
- **Pushing toward Alex Pereira** (their number first): Takedown defense (77% vs 51%, ≈2.1 pts); Title fight experience (8 vs 4, ≈2.0 pts); Grappling control share (13% vs 53%, ≈1.6 pts); Strength of schedule (avg opponent Elo) (1692 vs 1667, ≈1.4 pts)
- **Pushing toward Ciryl Gane** (their number first): Age (36.2 vs 38.9, ≈3.5 pts); Recent striking form (last ~3 fights) (2.29 vs 1.32, ≈3.1 pts); Age past 32 (decline years) (4.2 vs 6.9, ≈2.9 pts); Striking defense (60% vs 54%, ≈2.1 pts)
- **In the cage, Alex Pereira:** 12 of 33 sig. strikes (opponent 54); 0 knockdown(s) scored, 1 suffered; 0/0 takedowns; out-landed opponent in 0 round(s)
- **In the cage, Ciryl Gane:** 54 of 86 sig. strikes (opponent 12); 1 knockdown(s) scored, 0 suffered; 0/2 takedowns; 0:12 control; out-landed opponent in 2 round(s)
- **Why Ciryl Gane won:** Ciryl Gane was winning the fight (significant strikes 54-12, knockdowns 1-0, control time (min) 0.2-0.0) and finished it: KO/TKO (Punches to Head At Distance), R2 1:27.
- **Alex Pereira:** Alex Pereira did not win any of the main stat battles. Was knocked down 1 time(s).
- **Verdict: Right for the right reasons.** The model expected Ciryl Gane to have the striking edge, and that is how the fight was won (striking).

### 2026-06-14 · Ilia Topuria vs Justin Gaethje
_UFC Freedom 250 · UFC Lightweight Title Bout_

- **Result:** Justin Gaethje by KO/TKO (R4 5:00). **Win type:** Comeback finish via striking; stats support for the winner 43%.
- **Model before the fight** (trained on 8,569 earlier fights): Ilia Topuria 83% / Justin Gaethje 17%. Picked Ilia Topuria ❌
- **Pushing toward Ilia Topuria** (their number first): Age (29.4 vs 37.6, ≈4.8 pts); Win / loss streak (+9 vs +2, ≈3.4 pts); Age past 32 (decline years) (0.0 vs 5.6, ≈3.1 pts); Times finished (0 vs 5, ≈2.9 pts)
- **Pushing toward Justin Gaethje** (their number first): Recent results (last ~3 fights) (69% vs 90%, ≈3.4 pts); Strength of schedule (avg opponent Elo) (1716 vs 1658, ≈1.7 pts); Striking accuracy (58% vs 48%, ≈1.6 pts); UFC experience (fights) (15 vs 9, ≈1.5 pts)
- **In the cage, Ilia Topuria:** 97 of 162 sig. strikes (opponent 91); 1 knockdown(s) scored, 0 suffered; 1/3 takedowns; 2:32 control; out-landed opponent in 1 round(s)
- **In the cage, Justin Gaethje:** 91 of 192 sig. strikes (opponent 97); 0 knockdown(s) scored, 1 suffered; 0/5 takedowns; 1:32 control; out-landed opponent in 3 round(s)
- **Why Justin Gaethje won:** Justin Gaethje was behind (Ilia Topuria led significant strikes 97-91, knockdowns 1-0, takedowns 1-0, control time (min) 2.5-1.5) but ended it with one decisive moment: KO/TKO (toCorner Stoppage), R4 5:00.
- **Ilia Topuria:** Ilia Topuria had real success (significant strikes 97-91, knockdowns 1-0, takedowns 1-0, control time (min) 2.5-1.5) but was finished.
- **Verdict: Wrong on a fight-changing moment.** Justin Gaethje won with a comeback finish — a single moment that pre-fight averages cannot see coming.

### 2026-06-20 · Manel Kape vs Kyoji Horiguchi
_UFC Fight Night: Kape vs. Horiguchi · Flyweight Bout_

- **Result:** Manel Kape by KO/TKO (R3 2:42). **Win type:** Comeback finish via mixed; stats support for the winner 23%.
- **Model before the fight** (trained on 8,576 earlier fights): Manel Kape 58% / Kyoji Horiguchi 42%. Picked Manel Kape ✅
- **Pushing toward Manel Kape** (their number first): Age past 32 (decline years) (0.6 vs 3.7, ≈4.9 pts); Age (32.6 vs 35.7, ≈3.8 pts); Recent results (last ~3 fights) (76% vs 85%, ≈2.4 pts); Striking accuracy (56% vs 47%, ≈2.1 pts)
- **Pushing toward Kyoji Horiguchi** (their number first): Takedowns landed / 15 min (1.60 vs 0.53, ≈2.9 pts); Striking defense (63% vs 57%, ≈2.1 pts); Title fight experience (1 vs 0, ≈1.8 pts); Recent striking form (last ~3 fights) (1.68 vs 1.04, ≈1.5 pts)
- **In the cage, Manel Kape:** 19 of 56 sig. strikes (opponent 27); 1 knockdown(s) scored, 0 suffered; 0/0 takedowns; 0:10 control; out-landed opponent in 1 round(s)
- **In the cage, Kyoji Horiguchi:** 27 of 53 sig. strikes (opponent 19); 0 knockdown(s) scored, 1 suffered; 2/5 takedowns; 4:00 control; out-landed opponent in 2 round(s)
- **Why Manel Kape won:** Manel Kape was behind (Kyoji Horiguchi led significant strikes 27-19, takedowns 2-0, control time (min) 4.0-0.2) but ended it with one decisive moment: KO/TKO (Punches to Head On Ground), R3 2:42.
- **Kyoji Horiguchi:** Kyoji Horiguchi had real success (significant strikes 27-19, takedowns 2-0, control time (min) 4.0-0.2) but was finished.
- **Verdict: Right, on overall profile.** The model backed Manel Kape mainly on overall profile (quality of opposition, age, experience, form) rather than a specific matchup edge, and Manel Kape won via mixed.

### 2026-06-27 · Rafael Fiziev vs Manuel Torres
_UFC Fight Night: Fiziev vs. Torres · Lightweight Bout_

- **Result:** Rafael Fiziev by KO/TKO (R2 0:15). **Win type:** Dominant finish via mixed; stats support for the winner 76%.
- **Model before the fight** (trained on 8,588 earlier fights): Rafael Fiziev 36% / Manuel Torres 64%. Picked Manuel Torres ❌
- **Pushing toward Rafael Fiziev** (their number first): Recent results (last ~3 fights) (44% vs 76%, ≈8.0 pts); Chin risk (KD absorbed / 15 min) (0.31 vs 1.14, ≈4.0 pts); Recent strength of schedule (last ~3 opponents) (1621.84 vs 1584.16, ≈2.9 pts); Strength of schedule (avg opponent Elo) (1607 vs 1553, ≈2.5 pts)
- **Pushing toward Manuel Torres** (their number first): Recent results vs expectation (opponent-adjusted) (0.29 vs -0.04, ≈5.6 pts); Recent striking form (last ~3 fights) (0.79 vs -0.19, ≈3.5 pts); Finishing rate (76% vs 25%, ≈2.9 pts); Takedowns landed / 15 min (1.73 vs 0.89, ≈2.6 pts)
- **In the cage, Rafael Fiziev:** 25 of 39 sig. strikes (opponent 22); 1 knockdown(s) scored, 0 suffered; 2/2 takedowns; 0:42 control; out-landed opponent in 1 round(s)
- **In the cage, Manuel Torres:** 22 of 52 sig. strikes (opponent 25); 0 knockdown(s) scored, 1 suffered; 0/0 takedowns; 0:06 control; out-landed opponent in 1 round(s)
- **Why Rafael Fiziev won:** Rafael Fiziev was winning the fight (significant strikes 25-22, knockdowns 1-0, takedowns 2-0, control time (min) 0.7-0.1) and finished it: KO/TKO (Punches to Head On Ground), R2 0:15.
- **Manuel Torres:** Manuel Torres did not win any of the main stat battles. Was knocked down 1 time(s).
- **Verdict: Wrong: the model misread the matchup.** The model's main reasons pointed to Manuel Torres, but Rafael Fiziev won a dominant finish via mixed (stats support 76%), so this was a genuine miss rather than bad luck.

### 2026-06-27 · Shara Magomedov vs Michel Pereira
_UFC Fight Night: Fiziev vs. Torres · Middleweight Bout_

- **Result:** Shara Magomedov by Decision - Unanimous (R3 5:00). **Win type:** Coin-flip decision via striking; stats support for the winner 42%.
- **Model before the fight** (trained on 8,588 earlier fights): Shara Magomedov 53% / Michel Pereira 47%. Picked Shara Magomedov ✅
- **Pushing toward Shara Magomedov** (their number first): Recent striking form (last ~3 fights) (1.44 vs -0.90, ≈6.1 pts); Recent results vs expectation (opponent-adjusted) (0.15 vs -0.04, ≈3.5 pts); Times finished (0 vs 2, ≈2.3 pts); Striking accuracy (62% vs 52%, ≈2.1 pts)
- **Pushing toward Michel Pereira** (their number first): Recent results (last ~3 fights) (55% vs 72%, ≈4.5 pts); UFC experience (fights) (15 vs 6, ≈3.6 pts); Takedowns landed / 15 min (1.24 vs 0.23, ≈2.9 pts); Recent strength of schedule (last ~3 opponents) (1543.94 vs 1513.30, ≈2.6 pts)
- **In the cage, Shara Magomedov:** 52 of 85 sig. strikes (opponent 35); 0 knockdown(s) scored, 1 suffered; 0/0 takedowns; 0:53 control; out-landed opponent in 2 round(s)
- **In the cage, Michel Pereira:** 35 of 82 sig. strikes (opponent 52); 1 knockdown(s) scored, 0 suffered; 0/2 takedowns; 4:04 control; out-landed opponent in 1 round(s)
- **Why Shara Magomedov won:** Shara Magomedov got the nod in a fight the stats call nearly even (Shara Magomedov: significant strikes 52-35; Michel Pereira: knockdowns 1-0, control time (min) 4.1-0.9).
- **Michel Pereira:** Michel Pereira had real success (knockdowns 1-0, control time (min) 4.1-0.9) but it was not enough on the scorecards.
- **Verdict: Right for the right reasons.** The model expected Shara Magomedov to have the striking edge, and that is how the fight was won (striking).

### 2026-07-11 · Conor McGregor vs Max Holloway
_UFC 329: McGregor vs. Holloway 2 · Welterweight Bout_

- **Result:** Max Holloway by KO/TKO (R1 1:09). **Win type:** Quick finish via striking; stats support for the winner 74%.
- **Model before the fight** (trained on 8,601 earlier fights): Conor McGregor 26% / Max Holloway 74%. Picked Max Holloway ✅
- **Pushing toward Conor McGregor** (their number first): UFC cage time (minutes) (113 vs 533, ≈6.5 pts); Reach (188 cm vs 175 cm, ≈1.8 pts); Recent results (last ~3 fights) (46% vs 54%, ≈1.7 pts); Takedowns landed / 15 min (0.76 vs 0.26, ≈1.7 pts)
- **Pushing toward Max Holloway** (their number first): Days since last fight (126 vs 1500, ≈4.4 pts); Elo rating (quality of wins) (1836 vs 1720, ≈3.7 pts); Recent striking form (last ~3 fights) (1.55 vs -0.13, ≈3.5 pts); Age past 32 (decline years) (2.6 vs 6.0, ≈3.5 pts)
- **In the cage, Conor McGregor:** 0 of 6 sig. strikes (opponent 12); out-landed opponent in 0 round(s)
- **In the cage, Max Holloway:** 12 of 19 sig. strikes (opponent 0); 0:37 control; out-landed opponent in 1 round(s)
- **Why Max Holloway won:** Max Holloway ended it almost immediately: KO/TKO (toMcGregor knee injury), R1 1:09. Too short for stats to tell the story.
- **Conor McGregor:** Conor McGregor did not win any of the main stat battles.
- **Verdict: Right, on overall profile.** The model backed Max Holloway mainly on overall profile (quality of opposition, age, experience, form) rather than a specific matchup edge, and Max Holloway won via striking.

### 2026-07-18 · Dricus Du Plessis vs Kamaru Usman
_UFC Fight Night: Du Plessis vs. Usman · Middleweight Bout_

- **Result:** Dricus Du Plessis by Decision - Unanimous (R5 5:00). **Win type:** Clear win via striking; stats support for the winner 99%.
- **Model before the fight** (trained on 8,615 earlier fights): Dricus Du Plessis 48% / Kamaru Usman 52%. Picked Kamaru Usman ❌
- **Pushing toward Dricus Du Plessis** (their number first): Age past 32 (decline years) (0.5 vs 7.2, ≈7.3 pts); Age (32.5 vs 39.2, ≈7.1 pts); Recent results vs expectation (opponent-adjusted) (0.22 vs -0.02, ≈4.2 pts); UFC cage time (minutes) (149 vs 339, ≈3.9 pts)
- **Pushing toward Kamaru Usman** (their number first): Recent grappling control (77% vs 27%, ≈5.0 pts); Recent results (last ~3 fights) (58% vs 72%, ≈3.7 pts); UFC experience (fights) (19 vs 10, ≈3.3 pts); Takedown defense (87% vs 41%, ≈3.0 pts)
- **In the cage, Dricus Du Plessis:** 136 of 273 sig. strikes (opponent 92); 0/2 takedowns; 0:06 control; out-landed opponent in 4 round(s)
- **In the cage, Kamaru Usman:** 92 of 234 sig. strikes (opponent 136); 0/7 takedowns; 0:24 control; out-landed opponent in 1 round(s)
- **Why Dricus Du Plessis won:** Dricus Du Plessis won the fight on the numbers and the cards agreed: led significant strikes 136-92.
- **Kamaru Usman:** Kamaru Usman had real success (control time (min) 0.4-0.1) but it was not enough on the scorecards.
- **Verdict: Wrong on a toss-up.** The model saw this as close to 50/50 and leaned the wrong way.

### 2026-07-25 · Magomed Ankalaev vs Bogdan Guskov
_UFC Fight Night: Ankalaev vs. Guskov · Light Heavyweight Bout_

- **Result:** Magomed Ankalaev by KO/TKO (R5 2:41). **Win type:** Dominant finish via grappling; stats support for the winner 99%.
- **Model before the fight** (trained on 8,627 earlier fights): Magomed Ankalaev 78% / Bogdan Guskov 22%. Picked Magomed Ankalaev ✅
- **Pushing toward Magomed Ankalaev** (their number first): Elo rating (quality of wins) (1799 vs 1637, ≈5.1 pts); Recent strength of schedule (last ~3 opponents) (1672.31 vs 1579.29, ≈4.4 pts); Striking defense (56% vs 46%, ≈2.8 pts); UFC experience (fights) (15 vs 6, ≈2.5 pts)
- **Pushing toward Bogdan Guskov** (their number first): UFC cage time (minutes) (44 vs 189, ≈1.9 pts); Recent results vs expectation (opponent-adjusted) (0.26 vs 0.14, ≈1.6 pts); Finishing rate (61% vs 39%, ≈0.8 pts); Times finished (1 vs 2, ≈0.6 pts)
- **In the cage, Magomed Ankalaev:** 54 of 113 sig. strikes (opponent 39); 2/4 takedowns; 8:26 control; 3 submission attempt(s); out-landed opponent in 4 round(s)
- **In the cage, Bogdan Guskov:** 39 of 63 sig. strikes (opponent 54); 0/0 takedowns; 1 submission attempt(s); out-landed opponent in 0 round(s)
- **Why Magomed Ankalaev won:** Magomed Ankalaev was winning the fight (significant strikes 54-39, takedowns 2-0, control time (min) 8.4-0.0) and finished it: KO/TKO (Punches to Head On Ground), R5 2:41.
- **Bogdan Guskov:** Bogdan Guskov did not win any of the main stat battles.
- **Verdict: Right, on overall profile.** The model backed Magomed Ankalaev mainly on overall profile (quality of opposition, age, experience, form) rather than a specific matchup edge, and Magomed Ankalaev won via grappling.

### 2026-08-01 · Uros Medic vs Daniel Rodriguez
_UFC Fight Night: Medic vs. Rodriguez · Welterweight Bout_

- **Result:** Uros Medic by KO/TKO (R1 0:30). **Win type:** Quick finish via striking; stats support for the winner 83%.
- **Model before the fight** (trained on 8,639 earlier fights): Uros Medic 51% / Daniel Rodriguez 49%. Picked Uros Medic ✅
- **Pushing toward Uros Medic** (their number first): Age (33.3 vs 39.6, ≈7.0 pts); Age past 32 (decline years) (1.3 vs 7.6, ≈6.0 pts); Finishing rate (66% vs 29%, ≈2.2 pts); UFC cage time (minutes) (42 vs 162, ≈2.2 pts)
- **Pushing toward Daniel Rodriguez** (their number first): Recent strength of schedule (last ~3 opponents) (1607.82 vs 1557.23, ≈5.0 pts); Chin risk (KD absorbed / 15 min) (0.28 vs 0.88, ≈3.1 pts); Strength of schedule (avg opponent Elo) (1589 vs 1537, ≈2.5 pts); Elo rating (quality of wins) (1693 vs 1652, ≈2.0 pts)
- **In the cage, Uros Medic:** 11 of 14 sig. strikes (opponent 1); 1 knockdown(s) scored, 0 suffered; 0:04 control; out-landed opponent in 1 round(s)
- **In the cage, Daniel Rodriguez:** 1 of 3 sig. strikes (opponent 11); 0 knockdown(s) scored, 1 suffered; out-landed opponent in 0 round(s)
- **Why Uros Medic won:** Uros Medic ended it almost immediately: KO/TKO (Punches to Head At Distance), R1 0:30. Too short for stats to tell the story.
- **Daniel Rodriguez:** Daniel Rodriguez did not win any of the main stat battles. Was knocked down 1 time(s).
- **Verdict: Right, on overall profile.** The model backed Uros Medic mainly on overall profile (quality of opposition, age, experience, form) rather than a specific matchup edge, and Uros Medic won via striking.

### 2026-08-08 · Mateusz Gamrot vs Quillan Salkilld
_UFC Fight Night: Gamrot vs. Salkilld · Lightweight Bout_

- **Result:** Quillan Salkilld by Submission (R1 4:25). **Win type:** Dominant finish via grappling; stats support for the winner 71%.
- **Model before the fight** (trained on 8,653 earlier fights): Mateusz Gamrot 41% / Quillan Salkilld 59%. Picked Quillan Salkilld ✅
- **Pushing toward Mateusz Gamrot** (their number first): Recent results (last ~3 fights) (63% vs 88%, ≈6.5 pts); Recent strength of schedule (last ~3 opponents) (1646.10 vs 1583.04, ≈5.4 pts); Strength of schedule (avg opponent Elo) (1636 vs 1563, ≈4.2 pts); Striking defense (60% vs 50%, ≈3.2 pts)
- **Pushing toward Quillan Salkilld** (their number first): Age (26.6 vs 35.7, ≈8.9 pts); Recent results vs expectation (opponent-adjusted) (0.40 vs 0.13, ≈5.1 pts); Age past 32 (decline years) (0.0 vs 3.7, ≈4.1 pts); Reach (190 cm vs 178 cm, ≈2.7 pts)
- **In the cage, Mateusz Gamrot:** 3 of 10 sig. strikes (opponent 10); 0/1 takedowns; 0:20 control; 2 submission attempt(s); out-landed opponent in 0 round(s)
- **In the cage, Quillan Salkilld:** 10 of 24 sig. strikes (opponent 3); 1/1 takedowns; 2:02 control; 1 submission attempt(s); out-landed opponent in 1 round(s)
- **Why Quillan Salkilld won:** Quillan Salkilld was winning the fight (significant strikes 10-3, takedowns 1-0, control time (min) 2.0-0.3) and finished it: Submission (Rear Naked Choke), R1 4:25.
- **Mateusz Gamrot:** Mateusz Gamrot did not win any of the main stat battles.
- **Verdict: Right, on overall profile.** The model backed Quillan Salkilld mainly on overall profile (quality of opposition, age, experience, form) rather than a specific matchup edge, and Quillan Salkilld won via grappling.

### 2026-08-15 · Mackenzie Dern vs Gillian Robertson
_UFC 330: Makhachev vs. Machado Garry · UFC Women's Strawweight Title Bout_

- **Result:** Mackenzie Dern by Decision - Unanimous (R5 5:00). **Win type:** Clear win via mixed; stats support for the winner 95%.
- **Model before the fight** (trained on 8,665 earlier fights): Mackenzie Dern 42% / Gillian Robertson 58%. Picked Gillian Robertson ❌
- **Pushing toward Mackenzie Dern** (their number first): Recent strength of schedule (last ~3 opponents) (1593.23 vs 1535.22, ≈4.1 pts); Recent results (last ~3 fights) (68% vs 79%, ≈3.0 pts); Title fight experience (1 vs 0, ≈1.7 pts); Strength of schedule (avg opponent Elo) (1557 vs 1519, ≈1.7 pts)
- **Pushing toward Gillian Robertson** (their number first): Takedowns landed / 15 min (2.67 vs 0.96, ≈4.2 pts); Age (31.2 vs 33.4, ≈2.7 pts); Recent grappling control (82% vs 50%, ≈2.4 pts); Chin risk (KD absorbed / 15 min) (0.02 vs 0.39, ≈2.2 pts)
- **In the cage, Mackenzie Dern:** 65 of 168 sig. strikes (opponent 49); 4/6 takedowns; 10:48 control; 1 submission attempt(s); out-landed opponent in 3 round(s)
- **In the cage, Gillian Robertson:** 49 of 131 sig. strikes (opponent 65); 1/3 takedowns; 6:47 control; out-landed opponent in 2 round(s)
- **Why Mackenzie Dern won:** Mackenzie Dern won the fight on the numbers and the cards agreed: led significant strikes 65-49, takedowns 4-1, control time (min) 10.8-6.8.
- **Gillian Robertson:** Gillian Robertson did not win any of the main stat battles.
- **Verdict: Wrong: the model misread the matchup.** The model's main reasons pointed to Gillian Robertson, but Mackenzie Dern won a clear win via mixed (stats support 95%), so this was a genuine miss rather than bad luck.

### 2026-08-15 · Islam Makhachev vs Ian Machado Garry
_UFC 330: Makhachev vs. Machado Garry · UFC Welterweight Title Bout_

- **Result:** Islam Makhachev by Decision - Unanimous (R5 5:00). **Win type:** Clear win via grappling; stats support for the winner 99%.
- **Model before the fight** (trained on 8,665 earlier fights): Islam Makhachev 74% / Ian Machado Garry 26%. Picked Islam Makhachev ✅
- **Pushing toward Islam Makhachev** (their number first): Elo rating (quality of wins) (1997 vs 1787, ≈6.4 pts); Win / loss streak (+16 vs +2, ≈6.1 pts); Recent strength of schedule (last ~3 opponents) (1729.47 vs 1657.88, ≈4.0 pts); Recent grappling control (88% vs 40%, ≈4.0 pts)
- **Pushing toward Ian Machado Garry** (their number first): Age (28.7 vs 34.8, ≈5.2 pts); Age past 32 (decline years) (0.0 vs 2.8, ≈2.6 pts); Recent results (last ~3 fights) (79% vs 91%, ≈2.4 pts); Reach (188 cm vs 178 cm, ≈2.3 pts)
- **In the cage, Islam Makhachev:** 22 of 44 sig. strikes (opponent 29); 1 knockdown(s) scored, 0 suffered; 7/15 takedowns; 12:30 control; out-landed opponent in 2 round(s)
- **In the cage, Ian Machado Garry:** 29 of 65 sig. strikes (opponent 22); 0 knockdown(s) scored, 1 suffered; 0/0 takedowns; 0:34 control; out-landed opponent in 3 round(s)
- **Why Islam Makhachev won:** Islam Makhachev won the fight on the numbers and the cards agreed: led knockdowns 1-0, takedowns 7-0, control time (min) 12.5-0.6.
- **Ian Machado Garry:** Ian Machado Garry had real success (significant strikes 29-22) but it was not enough on the scorecards.
- **Verdict: Right, on overall profile.** The model backed Islam Makhachev mainly on overall profile (quality of opposition, age, experience, form) rather than a specific matchup edge, and Islam Makhachev won via grappling.

### 2026-08-22 · Anthony Hernandez vs Gregory Rodrigues
_UFC Fight Night: Hernandez vs. Rodrigues · Middleweight Bout_

- **Result:** Gregory Rodrigues by Decision - Unanimous (R5 5:00). **Win type:** Clear win via striking; stats support for the winner 99%.
- **Model before the fight** (trained on 8,677 earlier fights): Anthony Hernandez 70% / Gregory Rodrigues 30%. Picked Anthony Hernandez ❌
- **Pushing toward Anthony Hernandez** (their number first): Takedowns landed / 15 min (5.47 vs 1.89, ≈5.8 pts); Recent strength of schedule (last ~3 opponents) (1634.42 vs 1584.65, ≈4.3 pts); Age (32.8 vs 34.5, ≈2.1 pts); Recent results (last ~3 fights) (69% vs 77%, ≈1.8 pts)
- **Pushing toward Gregory Rodrigues** (their number first): Win / loss streak (+3 vs -1, ≈1.4 pts); Takedown accuracy (36% vs 48%, ≈0.7 pts); Times finished (2 vs 3, ≈0.7 pts); Recent results vs expectation (opponent-adjusted) (0.23 vs 0.19, ≈0.6 pts)
- **In the cage, Anthony Hernandez:** 90 of 159 sig. strikes (opponent 174); 0 knockdown(s) scored, 3 suffered; 3/29 takedowns; 10:40 control; out-landed opponent in 0 round(s)
- **In the cage, Gregory Rodrigues:** 174 of 283 sig. strikes (opponent 90); 3 knockdown(s) scored, 0 suffered; 0/0 takedowns; 2:40 control; out-landed opponent in 4 round(s)
- **Why Gregory Rodrigues won:** Gregory Rodrigues won the fight on the numbers and the cards agreed: led significant strikes 174-90, knockdowns 3-0.
- **Anthony Hernandez:** Anthony Hernandez had real success (takedowns 3-0, control time (min) 10.7-2.7) but it was not enough on the scorecards.
- **Verdict: Wrong: the model misread the matchup.** The model's main reasons pointed to Anthony Hernandez, but Gregory Rodrigues won a clear win via striking (stats support 99%), so this was a genuine miss rather than bad luck.

### 2026-09-05 · Dan Hooker vs Salahdine Parnasse
_UFC Fight Night: Hooker vs. Parnasse · Lightweight Bout_

- **Result:** Salahdine Parnasse by KO/TKO (R1 2:35). **Win type:** Dominant finish via striking; stats support for the winner 66%.
- **Model before the fight** (trained on 8,703 earlier fights): Dan Hooker 51% / Salahdine Parnasse 49%. Picked Dan Hooker ❌
- **Pushing toward Dan Hooker** (their number first): Recent strength of schedule (last ~3 opponents) (1663.57 vs 1500.00, ≈9.1 pts); UFC experience (fights) (24 vs 0, ≈7.4 pts); Elo rating (quality of wins) (1653 vs 1500, ≈5.7 pts); Strength of schedule (avg opponent Elo) (1609 vs 1500, ≈5.0 pts)
- **Pushing toward Salahdine Parnasse** (their number first): Age (28.8 vs 36.6, ≈7.7 pts); Times finished (0 vs 6, ≈5.5 pts); UFC cage time (minutes) (0 vs 243, ≈4.2 pts); Age past 32 (decline years) (0.0 vs 4.6, ≈4.1 pts)
- **In the cage, Dan Hooker:** 14 of 31 sig. strikes (opponent 12); 0 knockdown(s) scored, 1 suffered; out-landed opponent in 1 round(s)
- **In the cage, Salahdine Parnasse:** 12 of 17 sig. strikes (opponent 14); 1 knockdown(s) scored, 0 suffered; 0:02 control; out-landed opponent in 0 round(s)
- **Why Salahdine Parnasse won:** Salahdine Parnasse was winning the fight (knockdowns 1-0, control time (min) 0.0-0.0) and finished it: KO/TKO (Punch to Head At Distance), R1 2:35.
- **Dan Hooker:** Dan Hooker had real success (significant strikes 14-12) but was finished.
- **Verdict: Wrong on a toss-up.** The model saw this as close to 50/50 and leaned the wrong way.

### 2026-09-12 · Jean Silva vs Jose Delgado
_Noche UFC: Silva vs. Delgado · Featherweight Bout_

- **Result:** Jean Silva by Submission (R3 2:57). **Win type:** Dominant finish via grappling; stats support for the winner 85%.
- **Model before the fight** (trained on 8,717 earlier fights): Jean Silva 51% / Jose Delgado 49%. Picked Jean Silva ✅
- **Pushing toward Jean Silva** (their number first): Recent strength of schedule (last ~3 opponents) (1611.19 vs 1545.71, ≈4.9 pts); Elo rating (quality of wins) (1661 vs 1613, ≈2.6 pts); Takedowns landed / 15 min (1.54 vs 0.83, ≈2.2 pts); Strength of schedule (avg opponent Elo) (1580 vs 1542, ≈1.7 pts)
- **Pushing toward Jose Delgado** (their number first): Recent striking form (last ~3 fights) (1.13 vs 0.04, ≈3.9 pts); Reach (188 cm vs 175 cm, ≈3.3 pts); Takedown accuracy (28% vs 56%, ≈1.9 pts); Age (28.4 vs 29.7, ≈1.6 pts)
- **In the cage, Jean Silva:** 39 of 77 sig. strikes (opponent 40); 1 knockdown(s) scored, 0 suffered; 1/2 takedowns; 1:37 control; 1 submission attempt(s); out-landed opponent in 2 round(s)
- **In the cage, Jose Delgado:** 40 of 108 sig. strikes (opponent 39); 0 knockdown(s) scored, 1 suffered; 0/1 takedowns; 0:21 control; out-landed opponent in 1 round(s)
- **Why Jean Silva won:** Jean Silva was winning the fight (knockdowns 1-0, takedowns 1-0, control time (min) 1.6-0.3) and finished it: Submission (Rear Naked ChokeOne-arm RNC), R3 2:57.
- **Jose Delgado:** Jose Delgado had real success (significant strikes 40-39) but was finished.
- **Verdict: Right, on overall profile.** The model backed Jean Silva mainly on overall profile (quality of opposition, age, experience, form) rather than a specific matchup edge, and Jean Silva won via grappling.

### 2026-09-19 · Joshua Van vs Alexandre Pantoja
_UFC 331: Van vs. Pantoja 2 · UFC Flyweight Title Bout_

- **Result:** Joshua Van by Decision - Unanimous (R5 5:00). **Win type:** Clear win via striking; stats support for the winner 96%.
- **Model before the fight** (trained on 8,730 earlier fights): Joshua Van 75% / Alexandre Pantoja 25%. Picked Joshua Van ✅
- **Pushing toward Joshua Van** (their number first): Age (24.9 vs 36.4, ≈9.6 pts); Win / loss streak (+7 vs -1, ≈5.5 pts); Recent results vs expectation (opponent-adjusted) (0.37 vs 0.07, ≈4.2 pts); Recent striking form (last ~3 fights) (2.06 vs 0.27, ≈4.1 pts)
- **Pushing toward Alexandre Pantoja** (their number first): Recent grappling control (81% vs 28%, ≈3.8 pts); Recent results (last ~3 fights) (70% vs 87%, ≈3.5 pts); Takedowns landed / 15 min (2.71 vs 0.89, ≈3.0 pts); UFC experience (fights) (18 vs 11, ≈1.8 pts)
- **In the cage, Joshua Van:** 181 of 305 sig. strikes (opponent 147); 1 knockdown(s) scored, 0 suffered; 0/0 takedowns; 2:13 control; 1 submission attempt(s); out-landed opponent in 3 round(s)
- **In the cage, Alexandre Pantoja:** 147 of 284 sig. strikes (opponent 181); 0 knockdown(s) scored, 1 suffered; 5/18 takedowns; 9:11 control; out-landed opponent in 1 round(s)
- **Why Joshua Van won:** Joshua Van won the fight on the numbers and the cards agreed: led significant strikes 181-147, knockdowns 1-0.
- **Alexandre Pantoja:** Alexandre Pantoja had real success (takedowns 5-0, control time (min) 9.2-2.2) but it was not enough on the scorecards.
- **Verdict: Right, on overall profile.** The model backed Joshua Van mainly on overall profile (quality of opposition, age, experience, form) rather than a specific matchup edge, and Joshua Van won via striking.

### 2026-09-26 · Raul Rosas Jr. vs Raoni Barcelos
_UFC Fight Night: Rosas Jr. vs. Barcelos · Bantamweight Bout_

- **Result:** Raul Rosas Jr. by KO/TKO (R5 1:38). **Win type:** Comeback finish via mixed; stats support for the winner 2%.
- **Model before the fight** (trained on 8,742 earlier fights): Raul Rosas Jr. 66% / Raoni Barcelos 34%. Picked Raul Rosas Jr. ✅
- **Pushing toward Raul Rosas Jr.** (their number first): Age (22.0 vs 39.4, ≈15.5 pts); Takedowns landed / 15 min (5.84 vs 2.44, ≈7.0 pts); Age past 32 (decline years) (0.0 vs 7.4, ≈5.9 pts); UFC cage time (minutes) (71 vs 197, ≈1.8 pts)
- **Pushing toward Raoni Barcelos** (their number first): Recent strength of schedule (last ~3 opponents) (1585.76 vs 1515.72, ≈5.0 pts); Elo rating (quality of wins) (1699 vs 1649, ≈2.5 pts); UFC experience (fights) (15 vs 7, ≈2.5 pts); Takedown defense (85% vs 53%, ≈2.1 pts)
- **In the cage, Raul Rosas Jr.:** 113 of 251 sig. strikes (opponent 127); 1/3 takedowns; 0:54 control; out-landed opponent in 2 round(s)
- **In the cage, Raoni Barcelos:** 127 of 223 sig. strikes (opponent 113); 9/22 takedowns; 6:21 control; 5 submission attempt(s); out-landed opponent in 2 round(s)
- **Why Raul Rosas Jr. won:** Raul Rosas Jr. was behind (Raoni Barcelos led significant strikes 127-113, takedowns 9-1, control time (min) 6.3-0.9) but ended it with one decisive moment: KO/TKO (to From Half GuardBarcelos injury), R5 1:38.
- **Raoni Barcelos:** Raoni Barcelos had real success (significant strikes 127-113, takedowns 9-1, control time (min) 6.3-0.9) but was finished.
- **Verdict: Right, on overall profile.** The model backed Raul Rosas Jr. mainly on overall profile (quality of opposition, age, experience, form) rather than a specific matchup edge, and Raul Rosas Jr. won via mixed.

### 2026-10-03 · Natalia Silva vs Wang Cong
_UFC 332: Silva vs. Wang · UFC Women's Flyweight Title Bout_

- **Result:** Natalia Silva by Decision - Unanimous (R5 5:00). **Win type:** Clear win via striking; stats support for the winner 96%.
- **Model before the fight** (trained on 8,754 earlier fights): Natalia Silva 70% / Wang Cong 30%. Picked Natalia Silva ✅
- **Pushing toward Natalia Silva** (their number first): Elo rating (quality of wins) (1746 vs 1620, ≈4.5 pts); Recent strength of schedule (last ~3 opponents) (1597.74 vs 1532.89, ≈4.4 pts); Age (29.7 vs 34.4, ≈4.4 pts); Age past 32 (decline years) (0.0 vs 2.4, ≈2.5 pts)
- **Pushing toward Wang Cong** (their number first): Recent striking form (last ~3 fights) (2.98 vs 1.73, ≈3.6 pts); Recent results (last ~3 fights) (81% vs 90%, ≈2.3 pts); Striking accuracy (57% vs 45%, ≈1.9 pts); Net striking margin (landed - absorbed / min) (3.31 vs 2.14, ≈0.9 pts)
- **In the cage, Natalia Silva:** 109 of 216 sig. strikes (opponent 98); 1 knockdown(s) scored, 0 suffered; 3/5 takedowns; 4:12 control; out-landed opponent in 3 round(s)
- **In the cage, Wang Cong:** 98 of 206 sig. strikes (opponent 109); 0 knockdown(s) scored, 1 suffered; 0/0 takedowns; 2:39 control; out-landed opponent in 1 round(s)
- **Why Natalia Silva won:** Natalia Silva won the fight on the numbers and the cards agreed: led significant strikes 109-98, knockdowns 1-0, takedowns 3-0, control time (min) 4.2-2.6.
- **Wang Cong:** Wang Cong did not win any of the main stat battles. Was knocked down 1 time(s).
- **Verdict: Right, on overall profile.** The model backed Natalia Silva mainly on overall profile (quality of opposition, age, experience, form) rather than a specific matchup edge, and Natalia Silva won via striking.

### 2026-10-10 · Brendan Allen vs Christian Leroy Duncan
_UFC Fight Night: Allen vs. Duncan · Middleweight Bout_

- **Result:** Brendan Allen by Submission (R5 2:46). **Win type:** Comeback finish via grappling; stats support for the winner 12%.
- **Model before the fight** (trained on 8,768 earlier fights): Brendan Allen 45% / Christian Leroy Duncan 55%. Picked Christian Leroy Duncan ❌
- **Pushing toward Brendan Allen** (their number first): Elo rating (quality of wins) (1789 vs 1708, ≈4.6 pts); Recent strength of schedule (last ~3 opponents) (1618.72 vs 1576.52, ≈3.8 pts); UFC experience (fights) (19 vs 10, ≈2.9 pts); Takedowns landed / 15 min (1.48 vs 0.56, ≈2.5 pts)
- **Pushing toward Christian Leroy Duncan** (their number first): Recent striking form (last ~3 fights) (1.95 vs -0.02, ≈6.2 pts); Recent results vs expectation (opponent-adjusted) (0.31 vs 0.14, ≈3.1 pts); Reach (201 cm vs 190 cm, ≈2.9 pts); Times finished (0 vs 2, ≈2.3 pts)
- **In the cage, Brendan Allen:** 51 of 107 sig. strikes (opponent 106); 4/11 takedowns; 8:39 control; 2 submission attempt(s); out-landed opponent in 0 round(s)
- **In the cage, Christian Leroy Duncan:** 106 of 189 sig. strikes (opponent 51); 0/0 takedowns; 3:51 control; out-landed opponent in 4 round(s)
- **Why Brendan Allen won:** Brendan Allen was behind (Christian Leroy Duncan led significant strikes 106-51) but ended it with one decisive moment: Submission (Rear Naked Choke), R5 2:46.
- **Christian Leroy Duncan:** Christian Leroy Duncan had real success (significant strikes 106-51) but was finished.
- **Verdict: Wrong on a fight-changing moment.** Brendan Allen won with a comeback finish — a single moment that pre-fight averages cannot see coming.

### 2026-10-17 · Joaquin Buckley vs Mike Malott
_UFC Fight Night: Buckley vs. Malott · Welterweight Bout_

- **Result:** Mike Malott by KO/TKO (R2 2:32). **Win type:** Dominant finish via striking; stats support for the winner 93%.
- **Model before the fight** (trained on 8,779 earlier fights): Joaquin Buckley 48% / Mike Malott 52%. Picked Mike Malott ✅
- **Pushing toward Joaquin Buckley** (their number first): Recent results (last ~3 fights) (54% vs 82%, ≈7.7 pts); Recent strength of schedule (last ~3 opponents) (1663.71 vs 1575.02, ≈5.9 pts); Age (32.5 vs 34.9, ≈3.9 pts); UFC experience (fights) (17 vs 8, ≈3.1 pts)
- **Pushing toward Mike Malott** (their number first): Recent grappling control (69% vs 24%, ≈6.1 pts); Recent results vs expectation (opponent-adjusted) (0.30 vs 0.06, ≈4.4 pts); Recent striking form (last ~3 fights) (0.77 vs -0.10, ≈3.6 pts); Times finished (1 vs 3, ≈2.7 pts)
- **In the cage, Joaquin Buckley:** 14 of 53 sig. strikes (opponent 37); 0 knockdown(s) scored, 1 suffered; 0:08 control; out-landed opponent in 0 round(s)
- **In the cage, Mike Malott:** 37 of 50 sig. strikes (opponent 14); 1 knockdown(s) scored, 0 suffered; 1:25 control; out-landed opponent in 2 round(s)
- **Why Mike Malott won:** Mike Malott was winning the fight (significant strikes 37-14, knockdowns 1-0, control time (min) 1.4-0.1) and finished it: KO/TKO (Knee to Head At Distance), R2 2:32.
- **Joaquin Buckley:** Joaquin Buckley did not win any of the main stat battles. Was knocked down 1 time(s).
- **Verdict: Right for the right reasons.** The model expected Mike Malott to have the striking edge, and that is how the fight was won (striking).

### 2026-10-24 · Petr Yan vs Merab Dvalishvili
_UFC 333: Volkanovski vs. Evloev · UFC Bantamweight Title Bout_

- **Result:** Petr Yan by Decision - Unanimous (R5 5:00). **Win type:** Contested decision via mixed; stats support for the winner 23%.
- **Model before the fight** (trained on 8,792 earlier fights): Petr Yan 49% / Merab Dvalishvili 51%. Picked Merab Dvalishvili ❌
- **Pushing toward Petr Yan** (their number first): Age (33.7 vs 35.8, ≈3.3 pts); Age past 32 (decline years) (1.7 vs 3.8, ≈2.8 pts); Striking accuracy (55% vs 42%, ≈2.2 pts); Win / loss streak (+4 vs -1, ≈2.0 pts)
- **Pushing toward Merab Dvalishvili** (their number first): Takedowns landed / 15 min (5.75 vs 1.69, ≈11.1 pts); Recent grappling control (81% vs 51%, ≈2.4 pts); Elo rating (quality of wins) (1846 vs 1799, ≈2.4 pts); Recent striking form (last ~3 fights) (0.96 vs 0.44, ≈1.7 pts)
- **In the cage, Petr Yan:** 128 of 228 sig. strikes (opponent 131); 0/1 takedowns; 0:23 control; out-landed opponent in 1 round(s)
- **In the cage, Merab Dvalishvili:** 131 of 363 sig. strikes (opponent 128); 5/58 takedowns; 1:54 control; out-landed opponent in 3 round(s)
- **Why Petr Yan won:** Petr Yan got the decision even though Merab Dvalishvili led significant strikes 131-128, takedowns 5-0, control time (min) 1.9-0.4; this is a contested result, not a clean win.
- **Merab Dvalishvili:** Merab Dvalishvili had real success (significant strikes 131-128, takedowns 5-0, control time (min) 1.9-0.4) but it was not enough on the scorecards.
- **Verdict: Wrong, but the result was razor-close.** The in-fight stats only gave Petr Yan a 23% case for the decision. The model's pick was arguably as deserving as the official winner.

### 2026-10-24 · Alexander Volkanovski vs Movsar Evloev
_UFC 333: Volkanovski vs. Evloev · UFC Featherweight Title Bout_

- **Result:** Alexander Volkanovski by KO/TKO (R2 4:54). **Win type:** Dominant finish via mixed; stats support for the winner 83%.
- **Model before the fight** (trained on 8,792 earlier fights): Alexander Volkanovski 47% / Movsar Evloev 53%. Picked Movsar Evloev ❌
- **Pushing toward Alexander Volkanovski** (their number first): Recent results (last ~3 fights) (66% vs 91%, ≈6.6 pts); Recent strength of schedule (last ~3 opponents) (1711.56 vs 1654.53, ≈4.4 pts); Recent striking form (last ~3 fights) (1.86 vs 0.53, ≈4.4 pts); Title fight experience (11 vs 0, ≈3.9 pts)
- **Pushing toward Movsar Evloev** (their number first): Takedowns landed / 15 min (4.50 vs 1.63, ≈6.9 pts); Recent results vs expectation (opponent-adjusted) (0.40 vs 0.08, ≈6.1 pts); Age (32.7 vs 38.1, ≈5.7 pts); Age past 32 (decline years) (0.7 vs 6.1, ≈4.9 pts)
- **In the cage, Alexander Volkanovski:** 56 of 110 sig. strikes (opponent 40); 1/2 takedowns; 1:44 control; out-landed opponent in 2 round(s)
- **In the cage, Movsar Evloev:** 40 of 65 sig. strikes (opponent 56); 3/7 takedowns; 0:46 control; out-landed opponent in 0 round(s)
- **Why Alexander Volkanovski won:** Alexander Volkanovski was winning the fight (significant strikes 56-40, control time (min) 1.7-0.8) and finished it: KO/TKO (Punches to Head From Half Guard), R2 4:54.
- **Movsar Evloev:** Movsar Evloev had real success (takedowns 3-1) but was finished.
- **Verdict: Wrong on a toss-up.** The model saw this as close to 50/50 and leaned the wrong way.

### 2026-10-31 · Renato Moicano vs Tom Nolan
_UFC Fight Night: Moicano vs. Nolan · Lightweight Bout_

- **Result:** Tom Nolan by KO/TKO (R3 1:28). **Win type:** Dominant finish via mixed; stats support for the winner 97%.
- **Model before the fight** (trained on 8,806 earlier fights): Renato Moicano 51% / Tom Nolan 49%. Picked Renato Moicano ❌
- **Pushing toward Renato Moicano** (their number first): Recent strength of schedule (last ~3 opponents) (1660.80 vs 1543.95, ≈7.4 pts); Recent results (last ~3 fights) (59% vs 82%, ≈6.1 pts); Striking defense (60% vs 49%, ≈4.2 pts); Elo rating (quality of wins) (1729 vs 1636, ≈4.0 pts)
- **Pushing toward Tom Nolan** (their number first): Age (26.6 vs 37.4, ≈11.7 pts); Age past 32 (decline years) (0.0 vs 5.4, ≈4.7 pts); Recent results vs expectation (opponent-adjusted) (0.34 vs 0.11, ≈4.2 pts); Times finished (1 vs 5, ≈3.8 pts)
- **In the cage, Renato Moicano:** 9 of 12 sig. strikes (opponent 69); 0 knockdown(s) scored, 1 suffered; 3/5 takedowns; 7:17 control; 1 submission attempt(s); out-landed opponent in 0 round(s)
- **In the cage, Tom Nolan:** 69 of 92 sig. strikes (opponent 9); 1 knockdown(s) scored, 0 suffered; 1/1 takedowns; 1:10 control; out-landed opponent in 3 round(s)
- **Why Tom Nolan won:** Tom Nolan was winning the fight (significant strikes 69-9, knockdowns 1-0) and finished it: KO/TKO (Elbows to Head From Half Guard), R3 1:28.
- **Renato Moicano:** Renato Moicano had real success (takedowns 3-1, control time (min) 7.3-1.2) but was finished.
- **Verdict: Wrong on a toss-up.** The model saw this as close to 50/50 and leaned the wrong way.

### 2026-11-07 · Waldo Cortes Acosta vs Johnny Walker
_UFC Fight Night: Cortes Acosta vs. Walker · Heavyweight Bout_

- **Result:** Johnny Walker by KO/TKO (R3 2:27). **Win type:** Comeback finish via striking; stats support for the winner 30%.
- **Model before the fight** (trained on 8,818 earlier fights): Waldo Cortes Acosta 61% / Johnny Walker 39%. Picked Waldo Cortes Acosta ❌
- **Pushing toward Waldo Cortes Acosta** (their number first): Chin risk (KD absorbed / 15 min) (0.03 vs 0.86, ≈4.0 pts); Times finished (0 vs 4, ≈3.3 pts); Striking defense (55% vs 49%, ≈3.1 pts); Recent strength of schedule (last ~3 opponents) (1630.16 vs 1607.17, ≈2.6 pts)
- **Pushing toward Johnny Walker** (their number first): Recent striking form (last ~3 fights) (0.77 vs 0.44, ≈1.7 pts); Strength of schedule (avg opponent Elo) (1605 vs 1572, ≈1.5 pts); UFC experience (fights) (16 vs 14, ≈1.3 pts); Recent results vs expectation (opponent-adjusted) (0.07 vs 0.01, ≈1.2 pts)
- **In the cage, Waldo Cortes Acosta:** 40 of 89 sig. strikes (opponent 51); 1 knockdown(s) scored, 1 suffered; 4:24 control; out-landed opponent in 1 round(s)
- **In the cage, Johnny Walker:** 51 of 77 sig. strikes (opponent 40); 1 knockdown(s) scored, 1 suffered; 0:09 control; out-landed opponent in 2 round(s)
- **Why Johnny Walker won:** Johnny Walker was behind (Waldo Cortes Acosta led control time (min) 4.4-0.1) but ended it with one decisive moment: KO/TKO (Punch to Head At Distance), R3 2:27.
- **Waldo Cortes Acosta:** Waldo Cortes Acosta had real success (control time (min) 4.4-0.1) but was finished.
- **Verdict: Wrong on a fight-changing moment.** Johnny Walker won with a comeback finish — a single moment that pre-fight averages cannot see coming.

### 2026-11-14 · Ciryl Gane vs Josh Hokit
_UFC 334: Gane vs. Hokit · UFC Heavyweight Title Bout_

- **Result:** Ciryl Gane by Decision - Unanimous (R5 5:00). **Win type:** Clear win via striking; stats support for the winner 99%.
- **Model before the fight** (trained on 8,832 earlier fights): Ciryl Gane 65% / Josh Hokit 35%. Picked Ciryl Gane ✅
- **Pushing toward Ciryl Gane** (their number first): Elo rating (quality of wins) (1856 vs 1666, ≈6.9 pts); Recent strength of schedule (last ~3 opponents) (1724.70 vs 1597.39, ≈6.8 pts); Reach (206 cm vs 185 cm, ≈4.8 pts); Strength of schedule (avg opponent Elo) (1679 vs 1575, ≈4.3 pts)
- **Pushing toward Josh Hokit** (their number first): Age (29.0 vs 36.6, ≈7.4 pts); Age past 32 (decline years) (0.0 vs 4.6, ≈3.9 pts); Recent results vs expectation (opponent-adjusted) (0.43 vs 0.29, ≈2.4 pts); UFC cage time (minutes) (30 vs 182, ≈2.0 pts)
- **In the cage, Ciryl Gane:** 237 of 343 sig. strikes (opponent 146); 0/0 takedowns; 0:04 control; out-landed opponent in 5 round(s)
- **In the cage, Josh Hokit:** 146 of 283 sig. strikes (opponent 237); 3/30 takedowns; 4:37 control; out-landed opponent in 0 round(s)
- **Why Ciryl Gane won:** Ciryl Gane won the fight on the numbers and the cards agreed: led significant strikes 237-146.
- **Josh Hokit:** Josh Hokit had real success (takedowns 3-0, control time (min) 4.6-0.1) but it was not enough on the scorecards.
- **Verdict: Right, on overall profile.** The model backed Ciryl Gane mainly on overall profile (quality of opposition, age, experience, form) rather than a specific matchup edge, and Ciryl Gane won via striking.

### 2026-11-14 · Kayla Harrison vs Amanda Nunes
_UFC 334: Gane vs. Hokit · UFC Women's Bantamweight Title Bout_

- **Result:** Kayla Harrison by Submission (R4 1:29). **Win type:** Dominant finish via grappling; stats support for the winner 65%.
- **Model before the fight** (trained on 8,832 earlier fights): Kayla Harrison 60% / Amanda Nunes 40%. Picked Kayla Harrison ✅
- **Pushing toward Kayla Harrison** (their number first): Recent results vs expectation (opponent-adjusted) (0.45 vs 0.12, ≈5.6 pts); Days since last fight (525 vs 1253, ≈3.9 pts); Age (36.4 vs 38.5, ≈3.2 pts); UFC cage time (minutes) (32 vs 204, ≈3.0 pts)
- **Pushing toward Amanda Nunes** (their number first): Elo rating (quality of wins) (1817 vs 1638, ≈6.4 pts); Title fight experience (12 vs 1, ≈2.5 pts); UFC experience (fights) (18 vs 3, ≈2.5 pts); Takedowns landed / 15 min (2.70 vs 2.41, ≈1.8 pts)
- **In the cage, Kayla Harrison:** 25 of 41 sig. strikes (opponent 31); 3/9 takedowns; 5:41 control; 2 submission attempt(s); out-landed opponent in 2 round(s)
- **In the cage, Amanda Nunes:** 31 of 62 sig. strikes (opponent 25); 2/7 takedowns; 4:28 control; out-landed opponent in 2 round(s)
- **Why Kayla Harrison won:** Kayla Harrison was winning the fight (takedowns 3-2, control time (min) 5.7-4.5) and finished it: Submission (Rear Naked Choke), R4 1:29.
- **Amanda Nunes:** Amanda Nunes had real success (significant strikes 31-25) but was finished.
- **Verdict: Right, on overall profile.** The model backed Kayla Harrison mainly on overall profile (quality of opposition, age, experience, form) rather than a specific matchup edge, and Kayla Harrison won via grappling.
