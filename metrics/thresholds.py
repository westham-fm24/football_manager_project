# metrics/thresholds.py

# ─── Performance thresholds by metric ────────────────────────────────

str_metrics = {
    "xG/90": {"Elite": "≥ 1.02", "Good": "0.55 – 1.01", "Average": "< 0.55"},
    "Shot/90": {"Elite": "≥ 3.70", "Good": "2.13 – 3.69", "Average": "< 2.13"},
    "ShT/90": {"Elite": "≥ 2.08", "Good": "1.06 – 2.07", "Average": "< 1.06"},
    "NP-xG/90": {"Elite": "≥ 0.57", "Good": "0.31 – 0.56", "Average": "< 0.31"},
    "Sprints/90": {"Elite": "≥ 8.85", "Good": "6.95 – 8.84", "Average": "< 6.95"},
    "Poss Lost/90": {"Elite": "≤ 3.93", "Good": "3.94 – 8.63", "Average": "> 8.63"},
}

w_metrics = {
    "xG/90": {"Elite": "≥ 0.46", "Good": "0.33 – 0.45", "Average": "< 0.33"},
    "xA/90": {"Elite": "≥ 0.40", "Good": "0.33 – 0.39", "Average": "< 0.33"},
    "Drb/90": {"Elite": "≥ 2.78", "Good": "2.02 – 2.77", "Average": "< 2.02"},
    "ShT/90": {"Elite": "≥ 1.49", "Good": "1.18 – 1.48", "Average": "< 1.18"},
    "K Ps/90": {"Elite": "≥ 3.54", "Good": "2.23 – 3.53", "Average": "< 2.23"},
    "Poss Lost/90": {"Elite": "≤ 6.55", "Good": "6.56 – 14.01", "Average": "> 14.01"},
}

cm_metrics = {
    "Pr passes/90": {"Elite": "≥ 9.87", "Good": "6.28 – 9.86", "Average": "< 6.28"},
    "Pas %": {"Elite": "≥ 90%", "Good": "87% – 89%", "Average": "< 87%"},
    "xA/90": {"Elite": "≥ 0.32", "Good": "0.21 – 0.31", "Average": "< 0.21"},
    "Drb/90": {"Elite": "≥ 3.27", "Good": "1.24 – 3.26", "Average": "< 1.24"},
    "Tck/90": {"Elite": "≥ 3.00", "Good": "2.00 – 2.99", "Average": "< 2.00"},
    "Poss Lost/90": {"Elite": "≤ 7.20", "Good": "7.21 – 12.70", "Average": "> 12.70"},
}

dm_metrics = {
    "Tck/90": {"Elite": "≥ 3.41", "Good": "2.00 – 3.40", "Average": "< 2.00"},
    "Int/90": {"Elite": "≥ 2.47", "Good": "2.15 – 2.46", "Average": "< 2.15"},
    "Blk/90": {"Elite": "≥ 0.61", "Good": "0.40 – 0.60", "Average": "< 0.40"},
    "Pas %": {"Elite": "≥ 93%", "Good": "90% – 92%", "Average": "< 90%"},
    "Pr passes/90": {"Elite": "≥ 9.00", "Good": "6.17 – 8.99", "Average": "< 6.17"},
    "Poss Lost/90": {"Elite": "≤ 5.22", "Good": "5.23 – 7.53", "Average": "> 7.53"},
}

cd_metrics = {
    "Int/90": {"Elite": "≥ 2.47", "Good": "2.26 – 2.46", "Average": "< 2.26"},
    "Pas %": {"Elite": "≥ 93%", "Good": "87% – 92%", "Average": "< 87%"},
    "Poss Lost/90": {"Elite": "≤ 5.22", "Good": "5.23 – 10.73", "Average": "> 10.73"},
    "Hdrs W/90": {"Elite": "≥ 4", "Good": "3.5 – 3.9", "Average": "< 3.5"},
    "Poss Won/90": {"Elite": "≥ 14.38", "Good": "12.74 – 14.37", "Average": "< 12.74"},
}

fb_metrics = {
    "Pr passes/90": {"Elite": "≥ 8.5", "Good": "7.5 – 8.49", "Average": "< 7.5"},
    "Drb/90": {"Elite": "≥ 1.4", "Good": "0.9 – 1.39", "Average": "< 0.9"},
    "Tck/90": {"Elite": "≥ 2.8", "Good": "2.4 – 2.79", "Average": "< 2.4"},
    "Cr C/A": {"Elite": "≥ 23%", "Good": "21% – 22%", "Average": "< 21%"},
    "Sprints/90": {"Elite": "≥ 24.5", "Good": "22 – 24.4", "Average": "< 22"},
    "Poss Lost/90": {"Elite": "≤ 10.9", "Good": "11 – 11.5", "Average": "> 11.5"},
}

gk_metrics = {
    "xSv %": {"Elite": "≥ 0.83", "Good": "0.80 – 0.82", "Average": "< 0.80"},
    "Pas %": {"Elite": "≥ 92%", "Good": "90% – 91%", "Average": "< 90%"},
    "Poss Lost/90": {"Elite": "≤ 3.11", "Good": "3.12 – 4.15", "Average": "> 4.15"},
    "Pr passes/90": {"Elite": "≥ 1.56", "Good": "1.41 – 1.55", "Average": "< 1.41"},
}

# ─── Unified Metrics Map ──────────────────────────────
metrics_map = {
    "ST": str_metrics,
    "AM": w_metrics,
    "CM": cm_metrics,
    "DM": dm_metrics,
    "WB": fb_metrics,
    "CD": cd_metrics,
    "GK": gk_metrics,
}

# ─── Combine thresholds into one dict ──────────────────────────────
ideal_performance_metrics = {}
for d in (str_metrics, w_metrics, cm_metrics, dm_metrics, cd_metrics, fb_metrics, gk_metrics):
    ideal_performance_metrics.update(d)
