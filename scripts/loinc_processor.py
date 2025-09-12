import pandas as pd
from datetime import datetime
from utils.common_functions import save_to_formats

def main():
    loinc = pd.read_csv("input/Loinc.csv")

    loinc_small = loinc[["LOINC_NUM", "LONG_COMMON_NAME"]]
    loinc_small = loinc_small.rename(columns={
        "LOINC_NUM": "code",
        "LONG_COMMON_NAME": "description"
    })

    loinc_small = loinc_small.drop_duplicates(subset=["code"])
    loinc_small = loinc_small.dropna(subset=["code"])

    loinc_small["code"] = loinc_small["code"].str.strip()
    loinc_small["description"] = loinc_small["description"].str.strip()

    loinc_small["last_updated"] = datetime.now().isoformat()

    save_to_formats(loinc_small, "output/csv/loinc_clean.csv")

if __name__ == "__main__":
    main()





