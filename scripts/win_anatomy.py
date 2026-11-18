#!/usr/bin/env python3
"""
UFC ADVERSARIAL JUDGE - WIN ANATOMY ("what is a true win?")
===========================================================
The prediction model answers "who should win?" before a fight. This module
answers "who actually earned it, and how?" after a fight, using what happened
in the cage.

1. A judge model
   A logistic regression trained on every UFC decision with full stats. It
   learns how much each in-fight stat moves the judges: significant strikes,
   knockdowns, takedowns, control time, submission attempts and rounds won on
   the feet. Its coefficients give "exchange rates", e.g. how many significant
   strikes a knockdown is worth on the scorecards.

2. A verdict for every fight
   Using that judge model (with out-of-fold predictions, so a fight never
   grades itself), each win is graded:

   Decisions
     Clear win            the stats back the winner with >= 85% judge probability
     Competitive win      60-85%: the right person won, but it was a fight
     Coin-flip decision   40-60%: the numbers could support either fighter
     Contested decision   < 40%: the stats favoured the loser ("robbery" territory)
   Finishes
     Dominant finish      the winner was also ahead on the fight's stats
     Comeback finish      the loser was ahead on the stats; one moment changed it
     Quick finish         over in under 90 seconds; too short to judge by stats
   Other
     Technical result     DQ, overturned, could not continue

3. A route for every win: striking, grappling or mixed, based on which stats
   carried the judge-model score (or the method, for finishes).
"""

import os
import sys

import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_predict
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROCESSED_DIR = os.path.join(ROOT, 'data', 'processed')

# In-fight differentials (fighter A minus fighter B)
JUDGE_FEATURES = {
    'sig_diff': 'Significant strikes landed',
    'kd_diff': 'Knockdowns',
    'td_diff': 'Takedowns landed',
    'ctrl_min_diff': 'Control time (minutes)',
    'sub_diff': 'Submission attempts',
    'rounds_diff': 'Rounds won on significant strikes',
    'head_diff': 'Head strikes landed',
}
STRIKING = ['sig_diff', 'kd_diff', 'rounds_diff', 'head_diff']
GRAPPLING = ['td_diff', 'ctrl_min_diff', 'sub_diff']
GROUND_POSITIONS = ('Mount', 'Side Control', 'Back Control', 'Half Guard', 'Guard', 'Ground', 'North-South', 'Crucifix')


def _n(x):
    return x.fillna(0.0).astype(float)


def in_fight_diffs(bouts):
    d = pd.DataFrame(index=bouts.index)
    d['sig_diff'] = _n(bouts['a_sig_l']) - _n(bouts['b_sig_l'])
    d['kd_diff'] = _n(bouts['a_kd']) - _n(bouts['b_kd'])
    d['td_diff'] = _n(bouts['a_td_l']) - _n(bouts['b_td_l'])
    d['ctrl_min_diff'] = (_n(bouts['a_ctrl']) - _n(bouts['b_ctrl'])) / 60.0
    d['sub_diff'] = _n(bouts['a_sub']) - _n(bouts['b_sub'])
    d['rounds_diff'] = _n(bouts['a_rounds_won_strikes']) - _n(bouts['b_rounds_won_strikes'])
    d['head_diff'] = _n(bouts['a_head_l']) - _n(bouts['b_head_l'])
    return d


def is_decision(method):
    return method.fillna('').str.startswith('Decision')


def fit_judge_model(bouts):
    """Train on all decisions with stats; return (model, out-of-fold P(A won) for those decisions)."""
    mask = is_decision(bouts['method']) & bouts['result'].isin(['A', 'B']) & bouts['has_stats']
    X = in_fight_diffs(bouts[mask])
    y = (bouts.loc[mask, 'result'] == 'A').astype(int)
    # Mirror so the judge model has no corner bias
    Xm = pd.concat([X, -X]); ym = pd.concat([y, 1 - y])
    model = make_pipeline(StandardScaler(), LogisticRegression(C=1.0, max_iter=2000))
    model.fit(Xm, ym)
    oof = cross_val_predict(make_pipeline(StandardScaler(), LogisticRegression(C=1.0, max_iter=2000)),
                            X, y, cv=10, method='predict_proba')[:, 1]
    return model, pd.Series(oof, index=X.index), X, y


def exchange_rates(model):
    """Judge-model weight of each stat, expressed in 'significant strikes' of value."""
    scaler, lr = model.named_steps['standardscaler'], model.named_steps['logisticregression']
    raw = lr.coef_[0] / scaler.scale_  # log-odds per one unit of each stat
    w = dict(zip(JUDGE_FEATURES, raw))
    return pd.DataFrame([{'stat': JUDGE_FEATURES[k], 'feature': k, 'logodds_per_unit': v,
                          'worth_in_sig_strikes': v / w['sig_diff']} for k, v in w.items()])


def judge_contributions(model, X):
    scaler, lr = model.named_steps['standardscaler'], model.named_steps['logisticregression']
    Z = (X.to_numpy(dtype=float) - scaler.mean_) / scaler.scale_
    return pd.DataFrame(Z * lr.coef_[0], columns=X.columns, index=X.index)


def classify_wins(bouts):
    """Add judge probability, win type and win route to every decided fight."""
    model, oof, _, _ = fit_judge_model(bouts)
    b = bouts[bouts['result'].isin(['A', 'B'])].copy()
    X = in_fight_diffs(b)
    p_a = pd.Series(model.predict_proba(X)[:, 1], index=b.index)
    p_a.loc[oof.index.intersection(b.index)] = oof  # decisions: out-of-fold
    winner_is_a = b['result'] == 'A'
    b['stats_support_winner'] = np.where(winner_is_a, p_a, 1 - p_a)

    contrib = judge_contributions(model, X)
    sign = np.where(winner_is_a, 1.0, -1.0)[:, None]
    toward_winner = contrib * sign
    strike_push = toward_winner[STRIKING].clip(lower=0).sum(axis=1)
    grapple_push = toward_winner[GRAPPLING].clip(lower=0).sum(axis=1)

    method = b['method'].fillna('')
    types, routes = [], []
    for i in b.index:
        m, sup, secs = method[i], b.at[i, 'stats_support_winner'], b.at[i, 'fight_sec']
        s, g = strike_push[i], grapple_push[i]
        if m.startswith('Decision'):
            types.append('Clear win' if sup >= 0.85 else 'Competitive win' if sup >= 0.60
                         else 'Coin-flip decision' if sup >= 0.40 else 'Contested decision')
            total = s + g
            routes.append('striking' if total and s / total >= 0.65 else
                          'grappling' if total and g / total >= 0.65 else 'mixed')
        elif ('KO' in m) or ('Submission' in m) or ('Doctor' in m):
            if pd.notna(secs) and secs < 90:
                types.append('Quick finish')
            else:
                types.append('Dominant finish' if sup >= 0.5 else 'Comeback finish')
            detail = str(b.at[i, 'method_detail'])
            on_ground = any(k in detail for k in GROUND_POSITIONS) and 'Bottom' not in detail
            if 'Submission' in m:
                routes.append('grappling')
            elif on_ground:
                # ground-and-pound: the takedown/control game created the finish
                routes.append('grappling' if g > s else 'mixed')
            else:
                routes.append('striking')
        else:
            types.append('Technical result')
            routes.append('n/a')
    b['win_type'] = types
    b['win_route'] = routes
    return b, model


def describe_fighter(row, side):
    """Plain-English summary of one fighter's in-fight numbers."""
    o = 'b' if side == 'a' else 'a'
    def g(k, s=side):
        v = row.get(f'{s}_{k}')
        return 0 if pd.isna(v) else int(v)
    parts = [f"{g('sig_l')} of {g('sig_a')} sig. strikes (opponent {g('sig_l', o)})"]
    if g('kd') or g('kd', o):
        parts.append(f"{g('kd')} knockdown(s) scored, {g('kd', o)} suffered")
    if g('td_a') or g('td_a', o):
        parts.append(f"{g('td_l')}/{g('td_a')} takedowns")
    ctrl = row.get(f'{side}_ctrl')
    if pd.notna(ctrl) and ctrl > 0:
        parts.append(f"{int(ctrl // 60)}:{int(ctrl % 60):02d} control")
    if g('sub'):
        parts.append(f"{g('sub')} submission attempt(s)")
    rw = row.get(f'{side}_rounds_won_strikes')
    if pd.notna(rw):
        parts.append(f"out-landed opponent in {int(rw)} round(s)")
    return '; '.join(parts)


def why_won_and_lost(row):
    """Return (why the winner won, what the loser did / where it went wrong)."""
    w_side = 'a' if row['result'] == 'A' else 'b'
    l_side = 'b' if w_side == 'a' else 'a'
    W, L = row[f'fighter_{w_side}'], row[f'fighter_{l_side}']
    m = str(row['method'])
    def v(k, s):
        x = row.get(f'{s}_{k}')
        return 0.0 if pd.isna(x) else float(x)

    sig_w, sig_l = v('sig_l', w_side), v('sig_l', l_side)
    kd_w, kd_l = v('kd', w_side), v('kd', l_side)
    td_w, td_l = v('td_l', w_side), v('td_l', l_side)
    ct_w, ct_l = v('ctrl', w_side), v('ctrl', l_side)

    edges_w, edges_l = [], []
    for label, a, b_, fmt in [('significant strikes', sig_w, sig_l, '{:.0f}-{:.0f}'),
                              ('knockdowns', kd_w, kd_l, '{:.0f}-{:.0f}'),
                              ('takedowns', td_w, td_l, '{:.0f}-{:.0f}'),
                              ('control time (min)', ct_w / 60, ct_l / 60, '{:.1f}-{:.1f}')]:
        if a > b_:
            edges_w.append(f"{label} {fmt.format(a, b_)}")
        elif b_ > a:
            edges_l.append(f"{label} {fmt.format(b_, a)}")

    how = f"{m}" + (f" ({row['method_detail']})" if pd.notna(row.get('method_detail')) and
                    not m.startswith('Decision') else '')
    when = f"R{int(row['end_round'])} {row['end_time']}" if pd.notna(row.get('end_round')) else ''
    t = row['win_type']
    if t == 'Clear win':
        why_w = f"{W} won the fight on the numbers and the cards agreed: led {', '.join(edges_w) or 'the key stats'}."
    elif t == 'Competitive win':
        why_w = (f"{W} edged it: led {', '.join(edges_w) or 'the scoring stats'}"
                 + (f", while {L} took {', '.join(edges_l)}" if edges_l else '') + '.')
    elif t == 'Coin-flip decision':
        why_w = (f"{W} got the nod in a fight the stats call nearly even "
                 f"({W}: {', '.join(edges_w) or 'no clear stat edges'}; {L}: {', '.join(edges_l) or 'none'}).")
    elif t == 'Contested decision':
        why_w = (f"{W} got the decision even though {L} led {', '.join(edges_l) or 'the scoring stats'}; "
                 f"this is a contested result, not a clean win.")
    elif t == 'Dominant finish':
        why_w = f"{W} was winning the fight ({', '.join(edges_w) or 'ahead on the stats'}) and finished it: {how}, {when}."
    elif t == 'Comeback finish':
        why_w = (f"{W} was behind ({L} led {', '.join(edges_l) or 'the stats'}) but ended it with one decisive "
                 f"moment: {how}, {when}.")
    elif t == 'Quick finish':
        why_w = f"{W} ended it almost immediately: {how}, {when}. Too short for stats to tell the story."
    else:
        why_w = f"{W} won by {how}; a technical result rather than a fight that was decided in the cage."

    if edges_l:
        why_l = f"{L} had real success ({', '.join(edges_l)}) but "
        why_l += ('was finished.' if t in ('Dominant finish', 'Comeback finish', 'Quick finish')
                  else 'it was not enough on the scorecards.')
    else:
        why_l = f"{L} did not win any of the main stat battles."
        if kd_l == 0 and kd_w > 0:
            why_l += f" Was knocked down {int(kd_w)} time(s)."
    return why_w, why_l


def summary_tables(classified):
    """Headline facts about what decides UFC fights."""
    dec = classified[classified['method'].fillna('').str.startswith('Decision') & classified['has_stats']]
    w = np.where(dec['result'] == 'A', 'a', 'b')
    def won_stat(k):
        a = dec[f'a_{k}'].fillna(0).to_numpy(); b = dec[f'b_{k}'].fillna(0).to_numpy()
        wv = np.where(w == 'a', a, b); lv = np.where(w == 'a', b, a)
        return (wv > lv).mean(), (wv < lv).mean()
    facts = []
    for k, label in [('sig_l', 'landed more significant strikes'), ('kd', 'scored more knockdowns'),
                     ('td_l', 'landed more takedowns'), ('ctrl', 'had more control time'),
                     ('rounds_won_strikes', 'out-landed the opponent in more rounds')]:
        more, less = won_stat(k)
        facts.append({'In decisions, the winner...': label, 'share_of_decisions': more,
                      'loser_had_more': less})
    types = classified['win_type'].value_counts(normalize=True).rename('share').reset_index()
    return pd.DataFrame(facts), types


if __name__ == '__main__':
    bouts = pd.read_csv(os.path.join(PROCESSED_DIR, 'bouts.csv'), parse_dates=['date'], low_memory=False)
    classified, model = classify_wins(bouts)
    print(exchange_rates(model).round(3).to_string(index=False))
    facts, types = summary_tables(classified)
    print(facts.round(3).to_string(index=False))
    print(types.round(3).to_string(index=False))
