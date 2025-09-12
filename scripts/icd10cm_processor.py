import pandas as pd
import logging
from datetime import datetime

def save_to_csv(df, filename):
    df.to_csv(filename, index=False)

def load_icd10cm_data(filepath):
    df = pd.read_csv(filepath, sep=";", dtype=str)
    return df

def clean_icd10cm_data(raw_data):
    df = raw_data[["A00", "Cholera"]]
    df.columns = ["code", "description"]

    # Do NOT remove duplicates – keep all rows
    duplicate_count = df["code"].duplicated().sum()
    print("Number of duplicate codes found (kept in dataset):", duplicate_count)

    df["last_updated"] = datetime.now().isoformat()
    return df

def main():
    logging.basicConfig(level=logging.INFO)
    
    # Load raw data
    raw_data = load_icd10cm_data("input/icd102019syst_codes.txt")
    print("Rows in raw data:", len(raw_data))
    print("First 5 rows of raw data:")
    print(raw_data.head().to_string())
    
    # Clean and process
    clean_data = clean_icd10cm_data(raw_data)
    print("Rows in cleaned data:", len(clean_data))
    print("First 5 rows of cleaned data:")
    print(clean_data.head().to_string())

    # Save outputs
    save_to_csv(clean_data, "output/csv/icd10cm_clean.csv")
    
    logging.info("ICD-10-CM processing completed")

if __name__ == "__main__":
    main()

