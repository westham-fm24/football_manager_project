import os
import pandas as pd
from .evaluation import evaluate_metric_quality
from .thresholds import ideal_performance_metrics, role_performance_metrics

def explain_player_form(df, role):
    """Return per-metric quality table for each player of given role."""
    details = []
    for _, row in df.iterrows():
        metrics = role_performance_metrics[role]
        elite_found = False
        metric_info = []

        # Find similar players for context (by role keyword)
        same_role_df = df[df["Position"].str.contains(role, case=False, na=False)]

        for m in metrics:
            val = row.get(m)
            band = evaluate_metric_quality(val, ideal_performance_metrics.get(m, {}))
            role_avg = round(same_role_df[m].mean(), 2) if m in same_role_df.columns else None
            metric_info.append({
                "Metric": m,
                "Value": val,
                "Role Avg": role_avg,
                "Quality": band
            })
            if band == "Elite":
                elite_found = True

        base = row.get(role)
        adj = row.get(f"{role}_adj")
        if base and adj and adj > base and elite_found:
            details.append({
                "Name": row["Name"],
                "Role": role,
                "Base": base,
                "Adj": adj,
                "Delta": round(adj - base, 1),
                "Metrics": pd.DataFrame(metric_info)
            })
    return details


def generate_explain_html(df, output_dir):
    """Generate explain pages for all overperformers with at least one Elite metric."""
    os.makedirs(output_dir, exist_ok=True)
    all_explanations = []

    for role in role_performance_metrics.keys():
        expl = explain_player_form(df, role)
        for e in expl:
            # Add colored styling by Quality
            sub_df = e["Metrics"].copy()
            def colorize(val):
                if val == "Elite":
                    return 'style="background-color:#FFD700;"'
                if val == "Good":
                    return 'style="background-color:#90EE90;"'
                if val == "Average":
                    return 'style="background-color:#D3D3D3;"'
                return ''
            html_table = "<table border='1' cellspacing='0' cellpadding='5'><tr><th>Metric</th><th>Value</th><th>Role Avg</th><th>Quality</th></tr>"
            for _, r in sub_df.iterrows():
                html_table += f"<tr><td>{r['Metric']}</td><td>{r['Value']}</td><td>{r['Role Avg']}</td><td {colorize(r['Quality'])}>{r['Quality']}</td></tr>"
            html_table += "</table>"

            html = f"""
            <h2>{e['Name']} — {e['Role']} (+{e['Delta']})</h2>
            <p>Base: {e['Base']} → Adjusted: {e['Adj']}</p>
            {html_table}
            <hr>
            """
            all_explanations.append(html)

    if not all_explanations:
        html = "<h3>No players exceeded their base with Elite metrics.</h3>"
    else:
        html = "<h1>Overperformers — Driven by Elite Metrics</h1>" + "".join(all_explanations)

    filename = "explain_overperformers.html"
    path = os.path.join(output_dir, filename)
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"✅ Explanatory HTML saved to {path}")
    return path
