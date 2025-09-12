import pandas as pd

def save_to_formats(df, base_filename):
    """Save DataFrame to CSV format, ensuring output directory exists"""
    import os
    if not base_filename.endswith(".csv"):
        base_filename = base_filename + ".csv"
    output_dir = os.path.dirname(base_filename)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir, exist_ok=True)
    df.to_csv(base_filename, index=False)
    print(f"✅ File saved to {base_filename}")
