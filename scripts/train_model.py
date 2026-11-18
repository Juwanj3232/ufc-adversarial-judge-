#!/usr/bin/env python3
"""
UFC ADVERSARIAL JUDGE - MODEL TRAINING & HONEST EVALUATION
==========================================================
    python3 scripts/train_model.py            # walk-forward evaluation + final model
    python3 scripts/train_model.py --quick    # final model only (used by scheduled refreshes)

How the model is tested (walk-forward)
--------------------------------------
For every year from 2012 to today, a fresh model is trained only on fights that
happened before 1 January of that year, then asked to predict every fight in that
year. Every prediction is therefore made exactly as it would have been in real
life, with no knowledge of the future. The yearly results are pooled into one
honest scorecard.

Candidates compared
-------------------
  elo_only   the Elo rating gap alone (a strong, simple baseline)
  logistic   logistic regression on all 32 difference features
  boosting   gradient-boosted trees on all 32 difference features
  blend      the average of logistic and boosting probabilities

Also measured: the "career-stats" method the project used before, where every
fight was given each fighter's final career averages. This shows how much of
the old 67-75% accuracy came from information the model should not have had.

Every fight is used twice in training (A vs B and B vs A, with the label flipped)
and predictions average both orientations, so corner order can never matter.
"""

import argparse
import json
import os
import sys

import joblib
import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score, brier_score_loss, log_loss, roc_auc_score

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from features import FEATURE_COLUMNS, FIGHTER_FIELDS  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROCESSED_DIR = os.path.join(ROOT, 'data', 'processed')
MODEL_PATH = os.path.join(ROOT, 'models', 'ufc_judge_model.joblib')
REPORT_DIR = os.path.join(ROOT, 'reports')
FIRST_TEST_YEAR = 2012


from judge_model import columns_for, fit, make_boosting, mirrored, predict_sym  # noqa: E402

MODEL_KINDS = ['elo_only', 'logistic', 'boosting', 'blend']


def score(y, p):
    y = np.asarray(y); p = np.clip(np.asarray(p), 1e-6, 1 - 1e-6)
    return {'fights': int(len(y)), 'accuracy': accuracy_score(y, p >= 0.5),
            'log_loss': log_loss(y, p, labels=[0, 1]), 'brier': brier_score_loss(y, p),
            'roc_auc': roc_auc_score(y, p) if len(set(y)) > 1 else np.nan}


# ─── The old method, rebuilt for comparison ──────────────────────────────────

LEAKY_FIELDS = ['slpm', 'sapm', 'str_acc', 'str_def', 'td_avg', 'td_acc', 'td_def', 'sub_avg']


def add_career_stat_features(feats, processed_dir=PROCESSED_DIR):
    """Attach each fighter's FINAL career averages to every fight (what the old pipeline did)."""
    snap = pd.read_csv(os.path.join(processed_dir, 'fighter_snapshot.csv'))
    career = snap.set_index('fighter_id')[[f'raw_{f}' for f in LEAKY_FIELDS]]
    out = feats.copy()
    a = career.reindex(out['fighter_a_id']).to_numpy()
    b = career.reindex(out['fighter_b_id']).to_numpy()
    for i, f in enumerate(LEAKY_FIELDS):
        out[f'career_{f}_diff'] = a[:, i] - b[:, i]
    leaky_cols = [f'career_{f}_diff' for f in LEAKY_FIELDS] + \
        ['age_diff', 'height_cm_diff', 'reach_cm_diff', 'ufc_fights_diff', 'streak_diff', 'win_pct_diff']
    return out, leaky_cols


# ─── Walk-forward evaluation ─────────────────────────────────────────────────

def walk_forward(feats, first_year=FIRST_TEST_YEAR, kinds=MODEL_KINDS, verbose=True):
    """Train on everything before each year, predict that year. Returns per-fight predictions."""
    feats = feats.copy()
    feats['year'] = feats['date'].dt.year
    leaky_df, leaky_cols = add_career_stat_features(feats)
    preds = []
    for year in range(first_year, feats['year'].max() + 1):
        train = feats[feats['year'] < year]
        test = feats[feats['year'] == year]
        if test.empty:
            continue
        block = test[['fight_url', 'date', 'fighter_a', 'fighter_b', 'label', 'method',
                      'a_ufc_fights', 'b_ufc_fights', 'title_fight']].copy()
        for kind in kinds:
            model = fit(kind, train)
            block[f'p_{kind}'] = predict_sym(model, test, columns_for(kind))
        # the old career-stats method, same years, same model family
        lk_train = leaky_df[leaky_df['year'] < year]
        lk_test = leaky_df[leaky_df['year'] == year]
        X, y = mirrored(lk_train, leaky_cols)
        lk_model = make_boosting().fit(X, y)
        block['p_old_career_stats'] = predict_sym(lk_model, lk_test, leaky_cols)
        preds.append(block)
        if verbose:
            acc = ((block['p_blend'] >= 0.5) == block['label']).mean() if 'p_blend' in block else np.nan
            print(f"    {year}: trained on {len(train):>5,} fights, tested on {len(test):>3} -> blend accuracy {acc:.1%}")
    return pd.concat(preds, ignore_index=True)


def summarize(preds):
    rows = []
    for col in [c for c in preds.columns if c.startswith('p_')]:
        s = score(preds['label'], preds[col])
        rows.append({'model': col[2:], **s})
    return pd.DataFrame(rows)


def summarize_by_year(preds, col='p_blend'):
    out = []
    for year, g in preds.groupby(preds['date'].dt.year):
        s = score(g['label'], g[col]); s['year'] = year
        out.append(s)
    return pd.DataFrame(out)[['year', 'fights', 'accuracy', 'log_loss', 'brier', 'roc_auc']]


def calibration_table(preds, col='p_blend'):
    """When the model says 60-65%, does the favourite win about 60-65% of the time?"""
    p = preds[col].to_numpy(); y = preds['label'].to_numpy()
    fav_p = np.maximum(p, 1 - p)
    fav_won = np.where(p >= 0.5, y, 1 - y)
    bins = [0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 1.0]
    idx = np.digitize(fav_p, bins) - 1
    rows = []
    for i in range(len(bins) - 1):
        mask = idx == i
        if mask.sum():
            rows.append({'model_confidence': f'{bins[i]:.0%}-{bins[i+1]:.0%}', 'fights': int(mask.sum()),
                         'avg_predicted': fav_p[mask].mean(), 'favourite_actually_won': fav_won[mask].mean()})
    return pd.DataFrame(rows)


# ─── Final model ─────────────────────────────────────────────────────────────

def train_final(feats, kind='blend', metrics=None, model_path=MODEL_PATH):
    model = fit(kind, feats)
    bundle = {
        'kind': kind, 'model': model, 'feature_columns': columns_for(kind),
        'fighter_fields': FIGHTER_FIELDS,
        'trained_through': f"{feats['date'].max():%Y-%m-%d}", 'training_fights': int(len(feats)),
        'background': feats[FEATURE_COLUMNS].sample(min(300, len(feats)), random_state=0),
        'metrics': metrics or {},
    }
    os.makedirs(os.path.dirname(model_path), exist_ok=True)
    joblib.dump(bundle, model_path)
    return bundle


def load_features(processed_dir=PROCESSED_DIR):
    return pd.read_csv(os.path.join(processed_dir, 'features.csv'), parse_dates=['date'], low_memory=False)


def main(evaluate=True):
    feats = load_features()
    metrics = {}
    if evaluate:
        print('  Walk-forward evaluation (each year predicted by a model trained only on earlier years):')
        preds = walk_forward(feats)
        os.makedirs(REPORT_DIR, exist_ok=True)
        preds.to_csv(os.path.join(REPORT_DIR, 'walk_forward_predictions.csv'), index=False)
        summary = summarize(preds)
        veterans = preds[(preds['a_ufc_fights'] >= 3) & (preds['b_ufc_fights'] >= 3)]
        vet_summary = summarize(veterans)
        recent = preds[preds['date'] >= '2024-01-01']
        recent_summary = summarize(recent)
        by_year = summarize_by_year(preds)
        calib = calibration_table(preds)
        pd.set_option('display.width', 140)
        print('\n  ALL FIGHTS', FIRST_TEST_YEAR, '- today'); print(summary.round(4).to_string(index=False))
        print('\n  BOTH FIGHTERS WITH 3+ UFC FIGHTS'); print(vet_summary.round(4).to_string(index=False))
        print('\n  2024 - today'); print(recent_summary.round(4).to_string(index=False))
        print('\n  BLEND BY YEAR'); print(by_year.round(4).to_string(index=False))
        print('\n  CALIBRATION (blend)'); print(calib.round(3).to_string(index=False))
        metrics = {
            'walk_forward_all': summary.round(4).to_dict('records'),
            'walk_forward_veterans': vet_summary.round(4).to_dict('records'),
            'walk_forward_2024_on': recent_summary.round(4).to_dict('records'),
            'by_year_blend': by_year.round(4).to_dict('records'),
            'calibration_blend': calib.round(4).to_dict('records'),
        }
        with open(os.path.join(REPORT_DIR, 'model_metrics.json'), 'w') as fh:
            json.dump(metrics, fh, indent=2, default=str)
    else:
        metrics_path = os.path.join(REPORT_DIR, 'model_metrics.json')
        if os.path.exists(metrics_path):
            with open(metrics_path) as fh:
                metrics = json.load(fh)
    bundle = train_final(feats, metrics=metrics)
    print(f"  Final model ({bundle['kind']}) trained on {bundle['training_fights']:,} fights "
          f"through {bundle['trained_through']} -> {os.path.relpath(MODEL_PATH, ROOT)}")
    return bundle


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--quick', action='store_true', help='skip walk-forward evaluation')
    main(evaluate=not ap.parse_args().quick)
