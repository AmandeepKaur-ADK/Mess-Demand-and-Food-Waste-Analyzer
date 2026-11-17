
import pandas as pd

INGREDIENT_RATES = {
    "Rice": "rice_kg_per_student",
    "Wheat flour": "wheat_flour_kg_per_student",
    "Dal / pulses": "dal_pulses_kg_per_student",
    "Vegetables": "vegetables_kg_per_student",
    "Potatoes": "potatoes_kg_per_student",
}


def weekday_analysis(df):
    """Compare ingredient consumption across weekdays."""

    available = {
        name: column
        for name, column in INGREDIENT_RATES.items()
        if column in df.columns
    }

    return (
        df.groupby("weekday")
        .agg(
            records=("date", "count"),
            avg_students=("students_served_est", "mean"),
            **{
                f"{name.lower().replace(' ', '_')}_per_student":
                (column, "median")
                for name, column in available.items()
            }
        )
        .reset_index()
    )


def calendar_analysis(df):
    """Compare attendance and consumption by academic context."""

    categories = {
        "Vacation": "is_vacation",
        "Holiday": "is_holiday",
        "College event": "is_college_event",
        "Academic activity": "is_academic_activity",
    }

    frames = []

    for name, column in categories.items():
        if column not in df.columns:
            continue

        subset = df[df[column] == True]

        if not subset.empty:
            frames.append({
                "context": name,
                "records": len(subset),
                "avg_students": subset["students_served_est"].mean(),
                "median_students": subset["students_served_est"].median(),
                "avg_rice_per_student": subset[
                    "rice_kg_per_student"
                ].mean(),
                "avg_wheat_per_student": subset[
                    "wheat_flour_kg_per_student"
                ].mean(),
            })

    return pd.DataFrame(frames)


def menu_analysis(df):
    """Describe daily ingredient usage by lunch menu categories."""

    comparisons = {
        "Gravy": (
            "lunch_has_gravy",
            "rice_kg_per_student",
        ),
        "Egg curry": (
            "lunch_has_egg_curry",
            "wheat_flour_kg_per_student",
        ),
        "Dry vegetables": (
            "lunch_has_dry_vegetables",
            "wheat_flour_kg_per_student",
        ),
    }

    results = []

    for label, (flag, metric) in comparisons.items():
        if flag not in df.columns or metric not in df.columns:
            continue

        for value, group in df.groupby(flag):
            results.append({
                "menu_category": label,
                "present": bool(value),
                "records": len(group),
                "median_consumption_per_student": group[metric].median(),
                "mean_consumption_per_student": group[metric].mean(),
            })

    return pd.DataFrame(results)
