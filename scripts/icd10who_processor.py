import pandas as pd
from datetime import datetime

def main():
    icd10who = pd.read_csv("input/icd102019syst_codes.txt", sep=";", dtype=str)

    icd10who_small = icd10who[["A00", "Cholera"]]
    icd10who_small = icd10who_small.rename(columns={
        "A00": "code",
        "Cholera": "description"
    })

    icd10who_small["last_updated"] = datetime.now().isoformat()

    icd10who_small.to_csv("output/csv/icd10who_clean.csv", index=False)
    print("ICD-10 WHO cleaned and saved to output/csv/icd10who_clean.csv")

if __name__ == "__main__":
    main()


