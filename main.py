# main.py

import os
from config import (
    source_directory,
    destination_directory,
    new_directory,
    cols_to_prep,
    html_output_cols
)

from data_prep.file_ops import move_files, load_latest_file, delete_files
from data_prep.preprocess import preprocess_columns
from data_prep.scoring import calculate_player_scores
from metrics.evaluation import adjust_player_scores, role_performance_metrics
from metrics.thresholds import ideal_performance_metrics
from html_report.generate import generate_html, save_and_open_html
from metrics.explain import generate_explain_html
explain_dir = os.path.join(os.getcwd(), "html_report", "output_explain")
generate_explain_html(squad, explain_dir)

def main():
    # Step 1: move new export files into working directory
    move_files(source_directory, destination_directory)

    # Step 2: load the latest HTML file into DataFrame
    squad = load_latest_file(destination_directory)

    # Step 3: preprocess numeric columns
    preprocess_columns(squad, cols_to_prep)

    # Step 4: calculate raw FM role scores
    squad = calculate_player_scores(squad)

    # Step 5: adjust scores based on performance thresholds
    squad = adjust_player_scores(squad, ideal_performance_metrics, role_performance_metrics)

    # Step 6: generate and save HTML
    html = generate_html(squad[html_output_cols])
    save_and_open_html(html, new_directory)

    # Step 7: cleanup old files
    delete_files(destination_directory)


if __name__ == "__main__":
    main()
