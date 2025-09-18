# NFL ETL Pipeline

This project contains a data preprocessing pipeline for the NFL Play-by-Play dataset (2009–2018).

## Steps
1. Load dataset from CSV.
2. Remove duplicates.
3. Handle null values (median/mode).
4. Handle outliers (IQR method).

## Files
- `utils.py` → helper functions (load data, clean data, etc.)
- `preprocessing.py` → pipeline that uses `utils.py`

## How to Run
```bash
python preprocessing.py
