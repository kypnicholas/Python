from pathlib import Path
import pandas as pd

# ====================================================
# CONFIGURATION
# ====================================================

# Folder containing original CSV files
SOURCE_FOLDER = r"C:\Users\nkypri01\NK_DEV\1_Python\data_migration_VX\data\raw\test\test"

# Folder where converted files will be saved
DESTINATION_FOLDER = r"C:\Users\nkypri01\NK_DEV\1_Python\data_migration_VX\data\raw\test\testconverted"

# Current delimiter in source files
INPUT_DELIMITER = ";"

# Desired delimiter in output files
OUTPUT_DELIMITER = ","

# File encoding
ENCODING = "utf-8"

# ====================================================
# PROCESSING
# ====================================================

source_path = Path(SOURCE_FOLDER)
destination_path = Path(DESTINATION_FOLDER)

destination_path.mkdir(parents=True, exist_ok=True)

csv_files = list(source_path.glob("*.csv"))

print(f"Found {len(csv_files)} CSV files")

for file in csv_files:
    try:
        print(f"Processing: {file.name}")

        df = pd.read_csv(
            file,
            sep=INPUT_DELIMITER,
            encoding=ENCODING,
            dtype=str
        )

        output_file = destination_path / file.name

        df.to_csv(
            output_file,
            sep=OUTPUT_DELIMITER,
            index=False,
            encoding=ENCODING
        )

        print(f"Saved: {output_file}")

    except Exception as e:
        print(f"ERROR processing {file.name}: {e}")

print("Finished.")
