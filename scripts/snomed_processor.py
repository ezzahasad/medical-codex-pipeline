import pandas as pd
from datetime import datetime

def main():
    # Load the giant SNOMED file
    snomed = pd.read_csv("input/sct2_Description_Full-en_US1000124_20250901.txt", 
                         dtype=str, sep="\t")

    # Keep only id and term columns, rename them
    snomed_small = snomed[["id", "term"]].rename(columns={
        "id": "code",
        "term": "description"
    })

    # Remove empty rows
    snomed_small = snomed_small.dropna(subset=["code", "description"])

    # Add last_updated column
    snomed_small["last_updated"] = datetime.now().date()

    # Export only the first 500 rows so it’s not too big for GitHub
    snomed_sample = snomed_small.head(500)
    snomed_sample.to_csv("output/csv/snomed_sample.csv", index=False)

    print("Rows in full file:", len(snomed_small))
    print("Rows in sample file:", len(snomed_sample))

if __name__ == "__main__":
    main()

