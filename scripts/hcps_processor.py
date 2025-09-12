import pandas as pd
from datetime import datetime

def main():
    # Load fixed-width HCPCS file
    hcps = pd.read_fwf(
        "input/HCPC2025_OCT_ANWEB_v3.txt",
        header=None,
        dtype=str
    )

    print("Detected columns:", hcps.shape[1])
    print("First 5 rows of raw data:")
    print(hcps.head().to_string())

    # Keep only the first two columns: code + description
    hcps = hcps.iloc[:, :2]
    hcps = hcps.rename(columns={0: "code", 1: "description"})

    # Drop empty rows
    hcps_small = hcps.dropna(subset=["code", "description"])

    # Remove duplicates
    hcps_small = hcps_small.drop_duplicates(subset=["code"])

    # Add last_updated column
    hcps_small["last_updated"] = datetime.now().date()

    # Save to clean output
    hcps_small.to_csv("output/csv/hcps_clean.csv", index=False)

    print("Cleaned HCPCS file saved to output/csv/hcps_clean.csv")
    print("Rows before cleanup:", len(hcps))
    print("Rows after cleanup:", len(hcps_small))
    print("First 5 cleaned rows:")
    print(hcps_small.head().to_string())

if __name__ == "__main__":
    main()









