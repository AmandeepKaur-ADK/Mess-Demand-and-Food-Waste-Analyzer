from pathlib import Path
import pandas as pd

REQUIRED_COLUMNS = {
    "date", "day", "students_served_est", "rice_used_kg",
    "wheat_flour_used_kg", "dal_pulses_used_kg", "vegetables_used_kg",
    "potatoes_used_kg", "breakfast_grains_used_kg", "milk_used_litres",
    "bread_used_kg", "eggs_used_pieces", "bananas_used_pieces",
}

NUMERIC_COLUMNS = sorted(REQUIRED_COLUMNS - {"date", "day"})


def load_mess_data(path: str | Path) -> pd.DataFrame:
    """Load and validate the original daily mess records without altering raw values."""
    df = pd.read_csv(path)
    missing = REQUIRED_COLUMNS - set(df.columns)
    if missing:
        raise ValueError(f"CSV is missing required columns: {sorted(missing)}")

    # The source uses M/D/YYYY dates. Parse explicitly to avoid day/month ambiguity.
    df["date"] = pd.to_datetime(df["date"], format="%m/%d/%Y", errors="coerce")
    if df["date"].isna().any():
        bad_rows = (df.index[df["date"].isna()] + 2).tolist()
        raise ValueError(f"Invalid dates in CSV row(s): {bad_rows}")

    for col in NUMERIC_COLUMNS:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    invalid_numeric = df[NUMERIC_COLUMNS].isna().any(axis=1)
    if invalid_numeric.any():
        bad_rows = (df.index[invalid_numeric] + 2).tolist()
        raise ValueError(f"Missing or non-numeric values in CSV row(s): {bad_rows}")

    df["day"] = df["day"].astype(str).str.strip().str.title()
    df["actual_day"] = df["date"].dt.day_name()
    df["day_matches_date"] = df["day"].eq(df["actual_day"])
    return df.sort_values("date").reset_index(drop=True)


def data_quality_report(df: pd.DataFrame) -> dict:
    quantity_cols = [c for c in NUMERIC_COLUMNS if c != "students_served_est"]
    return {
        "rows": int(len(df)),
        "columns": int(len(df.columns)),
        "date_start": df["date"].min().date().isoformat(),
        "date_end": df["date"].max().date().isoformat(),
        "unique_dates": int(df["date"].nunique()),
        "duplicate_dates": int(df["date"].duplicated().sum()),
        "weekday_mismatches": int((~df["day_matches_date"]).sum()),
        "missing_values": int(df.isna().sum().sum()),
        "non_positive_student_days": int((df["students_served_est"] <= 0).sum()),
        "negative_quantity_cells": int((df[quantity_cols] < 0).sum().sum()),
        "zero_quantity_cells": int((df[quantity_cols] == 0).sum().sum()),
    }
