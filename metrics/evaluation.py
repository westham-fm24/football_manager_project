# metrics/evaluation.py
import pandas as pd
import numpy as np
from .thresholds import ideal_performance_metrics

# ─── Helper: evaluate a single metric quality ───────────────────────────────
def evaluate_metric_quality(value, thresholds):
    """Check if a given numeric value falls into Elite/Good/Average bands."""
    if pd.isna(value):
        return None
    for quality, thr_str in thresholds.items():
        thr = thr_str.replace('–', '-').replace('%', '').strip()
        if thr.startswith('≥'):
            try:
                return quality if value >= float(thr.lstrip('≥').strip()) else None
            except:
                continue
        if thr.startswith('≤'):
            try:
                return quality if value <= float(thr.lstrip('≤').strip()) else None
            except:
                continue
        if '-' in thr:
            try:
                low, high = [float(x.strip()) for x in thr.split('-', 1)]
                if low <= value <= high:
                    return quality
            except:
                continue
    return None

# ─── Role → Metrics Mapping ─────────────────────────────────────────────────
role_performance_metrics = {
    "STR": ['xG/90', 'Shot/90', 'ShT/90', 'NP-xG/90', 'Sprints/90', 'Poss Lost/90'],
    "W":   ['xG/90', 'xA/90', 'Pas %', 'ShT/90', 'K Ps/90', 'Poss Lost/90'],
    "CM":  ['Pr passes/90', 'Pas %', 'xA/90', 'Drb/90', 'Tck/90', 'Poss Lost/90'],
    "DM":  ['Tck/90', 'Int/90', 'Blk/90', 'Pas %', 'Pr passes/90', 'Poss Lost/90'],
    "CD":  ['Tck/90', 'Int/90', 'Pas %', 'Poss Lost/90','Poss Won/90','Hdrs W/90'],
    "FB":  ['Pr passes/90', 'Drb/90', 'Tck/90', 'CR C/A', 'Sprints/90','Poss Lost/90'],
    "GK":  ['xSv %', 'Pr passes/90', 'Pas %', 'Poss Lost/90']
}

# ─── Adjust player scores by metric quality ─────────────────────────────────
def adjust_player_scores(df, performance_thresholds=None, role_metrics=None, quality_factors=None):
    if performance_thresholds is None:
        performance_thresholds = ideal_performance_metrics
    if role_metrics is None:
        role_metrics = role_performance_metrics
    if quality_factors is None:
        quality_factors = {
            'Elite': 1.4,
            'Good': 1.15,
            'Average': 0.95,
            None: 0.0
        }

    for role, metrics in role_metrics.items():
        def compute_adj(row):
            total_f = 0.0
            for m in metrics:
                val = row.get(m, np.nan)
                band = evaluate_metric_quality(val, performance_thresholds.get(m, {}))
                total_f += quality_factors.get(band, 1.0)
            avg_f = total_f / len(metrics)
            return round(row[role] * avg_f, 1)
        df[f"{role}_adj"] = df.apply(compute_adj, axis=1)

    return df
