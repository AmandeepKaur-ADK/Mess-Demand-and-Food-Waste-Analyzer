import pandas as pd

# Daily aggregate ingredient quantities. Litres and pieces remain in their own units.
TARGET_COLUMNS = {
    "Rice (kg)": ("rice_used_kg", "kg"),
    "Wheat flour (kg)": ("wheat_flour_used_kg", "kg"),
    "Dal/pulses (kg)": ("dal_pulses_used_kg", "kg"),
    "Vegetables (kg)": ("vegetables_used_kg", "kg"),
    "Potatoes (kg)": ("potatoes_used_kg", "kg"),
    "Breakfast grains (kg)": ("breakfast_grains_used_kg", "kg"),
    "Milk (litres)": ("milk_used_litres", "litres"),
    "Bread (kg)": ("bread_used_kg", "kg"),
    "Eggs (pieces)": ("eggs_used_pieces", "pieces"),
    "Bananas (pieces)": ("bananas_used_pieces", "pieces"),
}


def make_daily_baseline(
    history: pd.DataFrame, target_date: pd.Timestamp, expected_students: int
) -> pd.DataFrame:
    """Estimate daily ingredient use from median per-student use on prior same weekdays.

    This is a transparent baseline, not a trained predictive model. It deliberately
    uses only dates before target_date to avoid future-data leakage.
    """
    target_date = pd.Timestamp(target_date).normalize()
    if expected_students <= 0:
        raise ValueError("Expected students must be greater than zero.")

    prior = history.loc[history["date"] < target_date].copy()
    weekday = target_date.day_name()
    comparable = prior.loc[prior["date"].dt.day_name() == weekday]
    source = comparable if len(comparable) >= 2 else prior
    source_label = f"previous {weekday} records" if len(comparable) >= 2 else "all previous records (weekday history is limited)"

    rows = []
    for label, (column, unit) in TARGET_COLUMNS.items():
        per_student = source[column] / source["students_served_est"].where(source["students_served_est"] > 0)
        per_student = per_student.dropna()
        if per_student.empty:
            estimate = None
            median_rate = None
        else:
            median_rate = float(per_student.median())
            estimate = median_rate * expected_students
        rows.append({
            "ingredient": label,
            "estimated_quantity": estimate,
            "unit": unit,
            "historical_median_per_student": median_rate,
            "comparison_records": int(len(per_student)),
            "basis": source_label,
        })
    return pd.DataFrame(rows)
