"""
UFC ADVERSARIAL JUDGE - MODEL + EXPLANATION LIBRARY
===================================================
Shared by train_model.py, backtest.py and predict_fight.py so all three build,
run and explain the model the same way.

Explanations
------------
The production model is a blend of a logistic regression and boosted trees.
For one matchup we compute, for each feature, how far it moved the prediction:
  * logistic part: coefficient x standardized value (exact for a linear model)
  * boosted part:  SHAP values from shap.TreeExplainer
Both are in log-odds, so they are averaged and then converted into approximate
percentage points of win probability. Each explanation is computed for A-vs-B and
B-vs-A and averaged, so it never depends on which corner a fighter is listed in.
"""

import numpy as np
import pandas as pd
from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

from features import FEATURE_COLUMNS, FEATURE_GROUP, FRIENDLY_NAMES


def make_logistic():
    return make_pipeline(SimpleImputer(strategy='constant', fill_value=0.0), StandardScaler(),
                         LogisticRegression(C=0.05, max_iter=2000))


def make_boosting():
    return HistGradientBoostingClassifier(max_iter=300, learning_rate=0.03, max_depth=4,
                                          min_samples_leaf=60, l2_regularization=1.0, random_state=42)


class BlendModel:
    """Average of a logistic regression and a boosted-tree model."""

    def __init__(self):
        self.logistic = make_logistic()
        self.boosting = make_boosting()
        self._tree_explainer = None

    def fit(self, X, y):
        self.logistic.fit(X, y)
        self.boosting.fit(X, y)
        self._tree_explainer = None
        return self

    def predict_proba(self, X):
        return (self.logistic.predict_proba(X) + self.boosting.predict_proba(X)) / 2.0

    # ── explanation ──
    def _linear_contrib(self, X):
        imp, scaler, lr = (self.logistic.named_steps[k] for k in
                           ('simpleimputer', 'standardscaler', 'logisticregression'))
        Z = scaler.transform(imp.transform(X))
        return Z * lr.coef_[0]

    def _tree_contrib(self, X):
        import shap
        if self._tree_explainer is None:
            self._tree_explainer = shap.TreeExplainer(self.boosting)
        sv = self._tree_explainer.shap_values(X)
        if isinstance(sv, list):
            sv = sv[1]
        sv = np.asarray(sv)
        return sv[:, :, 1] if sv.ndim == 3 else sv

    def contributions(self, X):
        """Per-feature push in log-odds toward fighter A, symmetric in corner order."""
        X = np.asarray(X, dtype=float)
        lin = (self._linear_contrib(X) - self._linear_contrib(-X)) / 2.0
        tree = (self._tree_contrib(X) - self._tree_contrib(-X)) / 2.0
        return (lin + tree) / 2.0

    def __getstate__(self):
        state = self.__dict__.copy()
        state['_tree_explainer'] = None
        return state


def make_model(kind):
    if kind == 'elo_only':
        return make_pipeline(StandardScaler(), LogisticRegression())
    if kind == 'logistic':
        return make_logistic()
    if kind == 'boosting':
        return make_boosting()
    if kind == 'blend':
        return BlendModel()
    raise ValueError(kind)


def columns_for(kind, feature_columns=FEATURE_COLUMNS):
    return ['elo_diff'] if kind == 'elo_only' else list(feature_columns)


def mirrored(df, cols):
    """Each fight from both corners: features flip sign, label flips."""
    X = df[cols].to_numpy(dtype=float)
    y = df['label'].to_numpy(dtype=int)
    return np.vstack([X, -X]), np.concatenate([y, 1 - y])


def fit(kind, train_df, feature_columns=FEATURE_COLUMNS):
    X, y = mirrored(train_df, columns_for(kind, feature_columns))
    return make_model(kind).fit(X, y)


def predict_sym(model, df, cols=FEATURE_COLUMNS):
    """P(fighter A wins), averaged over both corner orders."""
    X = df[cols].to_numpy(dtype=float)
    return (model.predict_proba(X)[:, 1] + 1.0 - model.predict_proba(-X)[:, 1]) / 2.0


def explain(model, row, name_a, name_b, prob_a=None):
    """
    Table of every feature's push for one matchup. `row` holds the *_diff columns
    plus a_<field>/b_<field> values. Positive push favours fighter A.
    """
    x = np.array([[float(row[c]) if pd.notna(row[c]) else np.nan for c in FEATURE_COLUMNS]])
    contrib = model.contributions(x)[0]
    if prob_a is None:
        prob_a = float(predict_sym(model, pd.DataFrame(x, columns=FEATURE_COLUMNS))[0])
    slope = max(prob_a * (1 - prob_a), 0.05)  # d(prob)/d(log-odds) at the prediction
    out = []
    for col, c in zip(FEATURE_COLUMNS, contrib):
        field = col[:-5]
        out.append({
            'feature': col, 'factor': FRIENDLY_NAMES.get(col, col), 'group': FEATURE_GROUP.get(col, 'other'),
            'value_a': row.get(f'a_{field}', np.nan), 'value_b': row.get(f'b_{field}', np.nan),
            'push_logodds': c, 'push_pts': c * slope * 100,
            'favours': name_a if c > 0 else name_b,
        })
    df = pd.DataFrame(out)
    df['abs'] = df['push_logodds'].abs()
    return df.sort_values('abs', ascending=False).drop(columns='abs').reset_index(drop=True)


def format_value(feature, v):
    """Human-readable stat value for reports."""
    if v is None or (isinstance(v, float) and np.isnan(v)):
        return 'n/a'
    f = feature[:-5] if feature.endswith('_diff') else feature
    if f in ('str_acc', 'str_def', 'td_acc', 'td_def', 'ctrl_share', 'recent_ctrl_share',
             'recent_win', 'win_pct', 'finish_rate'):
        return f'{v:.0%}'
    if f in ('elo', 'opp_elo_avg', 'recent_opp_elo', 'layoff_days', 'ufc_minutes'):
        return f'{v:.0f}'
    if f in ('ufc_fights', 'streak', 'ko_losses', 'finished_losses', 'title_fights'):
        return f'{v:+.0f}' if f == 'streak' else f'{v:.0f}'
    if f in ('height_cm', 'reach_cm'):
        return f'{v:.0f} cm'
    if f in ('age', 'age_decline'):
        return f'{v:.1f}'
    return f'{v:.2f}'
