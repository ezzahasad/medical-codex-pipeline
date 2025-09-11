import pandas as pd
import logging

def save_to_csv(df, filename):
    df.to_csv(filename, index=False)

def load_icd10cm_data(filepath):
    df = pd.read_csv(filepath, sep=";", dtype=str)
    return df

from datetime import datetime

def clean_icd10cm_data(raw_data):
    df = raw_data[["A00", "Cholera"]]
    df.columns = ["code", "description"]

    df = df.drop_duplicates(subset=["code"], keep="first")

    df["last_updated"] = datetime.now().isoformat()
    print("Duplicate codes after cleaning:", df["code"].duplicated().sum())

    return df

def main():
    logging.basicConfig(level=logging.INFO)
    
    raw_data = load_icd10cm_data("input/icd102019syst_codes.txt")
    print("First 5 rows of raw data:")
    print(raw_data.head().to_string())
    print("Column names in raw data:")
    print(list(raw_data.columns))
    
    clean_data = clean_icd10cm_data(raw_data)
    save_to_csv(clean_data, "output/csv/icd10cm_clean.csv")
    
    logging.info("ICD-10-CM processing completed")

if __name__ == "__main__":
    main()
