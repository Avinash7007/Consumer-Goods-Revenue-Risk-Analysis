
from pathlib import Path
import csv

RAW_DIR = Path(__file__).resolve().parents[1] / "data" / "raw"

for path in sorted(RAW_DIR.glob("*.csv")):
    print(f"\n{'=' * 60}")
    print(f"FILE: {path.name}")

    try:
        with path.open("r", encoding="utf-8-sig", newline="") as file:
            reader = csv.reader(file)
            headers = next(reader, [])
            row_count = sum(1 for _ in reader)

        print("Columns:", headers)
        print("Data rows:", f"{row_count:,}")

    except Exception as error:
        print("ERROR:", error)
