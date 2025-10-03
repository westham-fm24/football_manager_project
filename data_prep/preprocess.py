# data_prep/preprocess.py
def handle_range(value):
    """Convert strings like '45%', '1,234', '-' into floats."""
    if isinstance(value, str):
        value = value.strip().replace(',', '')
        if value in ['-', '']:
            return 0.0
        if value.endswith('%'):
            try:
                return float(value[:-1])
            except ValueError:
                return 0.0
        try:
            return float(value)
        except ValueError:
            return 0.0
    try:
        return float(value)
    except (ValueError, TypeError):
        return 0.0

def preprocess_columns(df, cols):
    """Apply handle_range() to given columns in DataFrame."""
    for c in cols:
        if c in df.columns:
            df[c] = df[c].apply(handle_range)
