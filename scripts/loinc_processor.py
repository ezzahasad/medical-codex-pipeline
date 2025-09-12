import pandas as pd
from utils.common_functions import save_to_formats

def main():
    # Load raw LOINC file
    df = pd.read_csv("input/Loinc.csv", dtype=str)

    # Keep only first 5 rows for testing
    df_test = df.head()

    # Save test output
    save_to_formats(df_test, "output/csv/loinc_clean")

if __name__ == "__main__":
    main()





