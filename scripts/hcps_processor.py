import pandas as pd
from datetime import datetime
import os

def main():
    # Make sure output folder exists
    os.makedirs("output/csv", exist_ok=True)

    # Load the HCPCS file as fixed-width
    hcps = pd.read_fwf(
        "input/HCPC2025_OCT_ANWEB_v3.txt",
        dtype=str
    )

    # Show structure for debugging
    print("Detected columns:", hcps.shape[1])
    print("First 10 rows of raw data:")
    print(hcps.head(10).to_string())

    # Rename the first two columns to "code" and "description"
    hcps = hcps.rename(columns={hcps.columns[0]: "code", hcps.columns[1]: "description"})

    # Keep only code + description, drop empties
    hcps_small = hcps[["code", "description"]].dropna()

    # Add last_updated column
    hcps_small["last_updated"] = datetime.now().date()

    # Save cleaned file
    hcps_small.to_csv("output/csv/hcps_clean.csv", index=False)

    # Print summary
    print("✅ Cleaned HCPCS file saved to output/csv/hcps_clean.csv")
    print("Rows before cleanup:", len(hcps))
    print("Rows after cleanup:", len(hcps_small))
    print(hcps_small.head(10).to_string())

    print("All columns detected:", hcps.columns.tolist())


if __name__ == "__main__":
    main()









