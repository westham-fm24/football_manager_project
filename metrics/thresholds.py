# metrics/thresholds.py

# ─── Performance thresholds by metric ────────────────────────────────

str_metrics = {
    "xG/90": {"Elite": "≥ 0.71", "Good": "0.56 – 0.70", "Average": "< 0.56"},
    "Shot/90": {"Elite": "≥ 5.31", "Good": "3.64 – 5.30", "Average": "< 3.64"},
    "ShT/90": {"Elite": "≥ 3.02", "Good": "2.14 – 3.02", "Average": "< 2.14"},
    "NP-xG/90": {"Elite": "≥ 0.69", "Good": "0.55 – 0.68", "Average": "< 0.55"},
    "Sprints/90": {"Elite": "≥ 21.60", "Good": "16.29 – 21.59", "Average": "< 16.29"},
    "Poss Lost/90": {"Elite": "≤ 2.51", "Good": "2.52 – 4.05", "Average": "> 4.05"},
}

w_metrics = {
    "xG/90":       {"Elite": "≥ 0.53",  "Good": "0.37 – 0.52",  "Average": "< 0.37"},
    "xA/90":       {"Elite": "≥ 0.47",  "Good": "0.34 – 0.46",  "Average": "< 0.34"},
    "Drb/90":      {"Elite": "≥ 3.16",  "Good": "2.22 – 3.15",  "Average": "< 2.22"},
    "ShT/90":      {"Elite": "≥ 1.73",  "Good": "1.23 – 1.72",  "Average": "< 1.23"},
    "K Ps/90":     {"Elite": "≥ 3.98",  "Good": "2.49 – 3.97",  "Average": "< 2.49"},
    "Poss Lost/90":{"Elite": "≤ 5.74",  "Good": "5.75 – 11.88", "Average": "> 11.88"},
}

cm_metrics = {
    "Pr passes/90": {"Elite": "≥ 10.12", "Good": "6.84 – 10.11", "Average": "< 6.84"},
    "Pas %":        {"Elite": "≥ 92%",   "Good": "88% – 91%",    "Average": "< 88%"},
    "xA/90":        {"Elite": "≥ 0.41",  "Good": "0.25 – 0.40",  "Average": "< 0.25"},
    "Drb/90":       {"Elite": "≥ 2.73",  "Good": "1.45 – 2.72",  "Average": "< 1.45"},
    "Tck/90":       {"Elite": "≥ 3.38",  "Good": "2.09 – 3.37",  "Average": "< 2.09"},
    "Int/90":       {"Elite": "≥ 2.61",  "Good": "2.22 – 2.60",  "Average": "< 2.22"},
    "Blk/90":       {"Elite": "≥ 0.67",  "Good": "0.42 – 0.66",  "Average": "< 0.42"},
    "Poss Lost/90": {"Elite": "≤ 5.93",  "Good": "5.94 – 9.88",  "Average": "> 9.88"},
}

dm_metrics = {
    "Pr passes/90": {"Elite": "≥ 10.12", "Good": "6.84 – 10.11", "Average": "< 6.84"},
    "Pas %":        {"Elite": "≥ 92%",   "Good": "88% – 91%",    "Average": "< 88%"},
    "xA/90":        {"Elite": "≥ 0.41",  "Good": "0.25 – 0.40",  "Average": "< 0.25"},
    "Drb/90":       {"Elite": "≥ 2.73",  "Good": "1.45 – 2.72",  "Average": "< 1.45"},
    "Tck/90":       {"Elite": "≥ 3.38",  "Good": "2.09 – 3.37",  "Average": "< 2.09"},
    "Int/90":       {"Elite": "≥ 2.61",  "Good": "2.22 – 2.60",  "Average": "< 2.22"},
    "Blk/90":       {"Elite": "≥ 0.67",  "Good": "0.42 – 0.66",  "Average": "< 0.42"},
    "Poss Lost/90": {"Elite": "≤ 5.93",  "Good": "5.94 – 9.88",  "Average": "> 9.88"},
}

cd_metrics = {
    "Int/90":       {"Elite": "≥ 2.63",  "Good": "2.31 – 2.62",  "Average": "< 2.31"},
    "Pas %":        {"Elite": "≥ 94%",   "Good": "89% – 93%",    "Average": "< 89%"},
    "Poss Lost/90": {"Elite": "≤ 4.92",  "Good": "4.93 – 9.61",  "Average": "> 9.61"},
    "Hdrs W/90":    {"Elite": "≥ 4.28",  "Good": "3.71 – 4.27",  "Average": "< 3.71"},
    "Poss Won/90":  {"Elite": "≥ 15.04", "Good": "13.15 – 15.03","Average": "< 13.15"},
}


fb_metrics = {
    "Pr passes/90": {"Elite": "≥ 9.12", "Good": "7.64 – 9.11", "Average": "< 7.64"},
    "Drb/90":       {"Elite": "≥ 1.66", "Good": "1.08 – 1.65", "Average": "< 1.08"},
    "Tck/90":       {"Elite": "≥ 3.02", "Good": "2.51 – 3.01", "Average": "< 2.51"},
    "Cr C/A":       {"Elite": "≥ 25%",  "Good": "22% – 24%",   "Average": "< 22%"},
    "Sprints/90":   {"Elite": "≥ 25.8", "Good": "22.9 – 25.7", "Average": "< 22.9"},
    "Poss Lost/90": {"Elite": "≤ 10.3", "Good": "10.4 – 11.1", "Average": "> 11.1"},
}

gk_metrics = {
    "xSv %":         {"Elite": "≥ 0.86", "Good": "0.82 – 0.85", "Average": "< 0.82"},
    "Pas %":         {"Elite": "≥ 93%",  "Good": "90% – 92%",   "Average": "< 90%"},
    "Poss Lost/90":  {"Elite": "≤ 2.94", "Good": "2.95 – 4.12", "Average": "> 4.12"},
    "Pr passes/90":  {"Elite": "≥ 1.78", "Good": "1.52 – 1.77", "Average": "< 1.52"},
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
