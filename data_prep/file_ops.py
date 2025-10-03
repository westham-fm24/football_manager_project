# data_prep/file_ops.py
import os, glob, shutil
import pandas as pd

def move_files(src, dest):
    """Move all .html files from src → dest, overwriting duplicates."""
    html_files = glob.glob(os.path.join(src, '*.html'))
    os.makedirs(dest, exist_ok=True)
    for file in html_files:
        dest_file = os.path.join(dest, os.path.basename(file))
        if os.path.exists(dest_file):
            os.remove(dest_file)
        shutil.move(file, dest_file)
    print(f"Moved {len(html_files)} files.")

def load_latest_file(directory):
    """Load most recent HTML file into DataFrame."""
    latest = max(glob.glob(os.path.join(directory, '*')), key=os.path.getctime)
    print(f"Latest file loaded: {latest}")

    with open(latest, 'r', encoding='utf-8', errors='replace') as f:
        html_str = f.read()

    return pd.read_html(html_str, header=0, keep_default_na=False)[0]

def delete_files(directory):
    """Delete all HTML files in a directory."""
    html_files = glob.glob(os.path.join(directory, '*.html'))
    for file in html_files:
        os.remove(file)
        print(f"Deleted file: {file}")
