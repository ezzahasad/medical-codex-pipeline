import pandas as pd
from datetime import datetime

def main():
    icd10who = pd.read_csv("input/icd102019syst_codes.txt", sep=";", dtype=str)

    icd10who_small = icd10who[["A00", "Cholera"]]
    icd10who_small = icd10who_small.rename(columns={
        "A00": "code",
        "Cholera": "description"
    })

    # Count rows before dropping empties
    before_count = len(icd10who_small)

    # Remove empty rows
    icd10who_small = icd10who_small.dropna(subset=["code", "description"])

    # Count rows after dropping empties
    after_count = len(icd10who_small)

    # Add last_updated
    icd10who_small["last_updated"] = datetime.now().date().isoformat()

    # Save
    file_output_path = "output/csv/icd10who_clean.csv"
    icd10who_small.to_csv(file_output_path, index=False)

    print(f"✅ ICD-10 WHO saved to {file_output_path}")
    print(f"Rows before removing empty rows: {before_count}")
    print(f"Rows after removing empty rows: {after_count}")

if __name__ == "__main__":
    main()




