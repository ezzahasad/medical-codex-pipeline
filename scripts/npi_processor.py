import pandas as pd
from datetime import datetime

def main():
    # Load the full NPI dataset
    npi = pd.read_csv(
        "input/npidata_pfile_200523-20250907.csv",
        dtype=str,
        low_memory=False
    )

    print("Detected columns:", npi.shape[1])
    print("Rows before cleanup:", len(npi))
    print("First 5 rows of raw data:")
    print(npi.head().to_string())

    # Keep only useful columns: NPI, last name, first name
    npi_small = npi[["NPI", "Provider Last Name (Legal Name)", "Provider First Name"]].copy()
    npi_small = npi_small.rename(columns={
        "NPI": "npi",
        "Provider Last Name (Legal Name)": "last_name",
        "Provider First Name": "first_name"
    })

    # Drop rows with missing NPI
    npi_small = npi_small.dropna(subset=["npi"])

    # Add last_updated column
    npi_small["last_updated"] = datetime.now().date()

    # --- Save full clean file ---
    npi_small.to_csv("output/csv/npi_clean.csv", index=False)
    print("\n Full cleaned NPI file saved to output/csv/npi_clean.csv")
    print(f"Total rows saved: {len(npi_small)}")

    # --- Save smaller sample file (first 100 rows) ---
    npi_sample = npi_small.head(100)
    npi_sample.to_csv("output/csv/npi_sample.csv", index=False)
    print("\n Sample NPI file saved to output/csv/npi_sample.csv")
    print(f"Sample rows saved: {len(npi_sample)}")
    print(npi_sample.head())

if __name__ == "__main__":
    main()


