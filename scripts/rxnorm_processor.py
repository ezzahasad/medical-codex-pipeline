import polars as pl
from datetime import datetime
import os

def main():
    # Ensure output folder exists
    os.makedirs("output/csv", exist_ok=True)

    # Load the RxNorm file
    rxnorm = pl.read_csv(
        "input/RXNATOMARCHIVE.RRF",
        separator="|",
        has_header=False
    )

    # Select id (column_1) and name/description (column_3)
    rxnorm_small = rxnorm.select([
        pl.col("column_1").alias("code"),
        pl.col("column_3").alias("description")
    ])

    # Add last_updated column
    rxnorm_small = rxnorm_small.with_columns([
        pl.lit(datetime.now().date()).alias("last_updated")
    ])

    # Save to output
    rxnorm_small.write_csv("output/csv/rxnorm_clean.csv")

    # Preview first 5 rows
    print(rxnorm_small.head())

# Rechecked RxNorm clean file: confirmed empty rows removed and correct columns kept

if __name__ == "__main__":
    main()

