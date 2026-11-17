from pathlib import Path
import pandas as pd

INGREDIENT_COLUMNS = {
    "rice_used_kg": "rice_kg_per_student",
    "wheat_flour_used_kg": "wheat_flour_kg_per_student",
    "dal_pulses_used_kg": "dal_pulses_kg_per_student",
    "vegetables_used_kg": "vegetables_kg_per_student",
    "potatoes_used_kg": "potatoes_kg_per_student",
    "breakfast_grains_used_kg": "breakfast_grains_kg_per_student",
    "milk_used_litres": "milk_litres_per_student",
    "bread_used_kg": "bread_kg_per_student",
    "eggs_used_pieces": "eggs_pieces_per_student",
    "bananas_used_pieces": "bananas_pieces_per_student",
}


def load_calendar(path: str | Path) -> pd.DataFrame:
    calendar = pd.read_csv(path)
    required = {"event_name", "start_date", "end_date", "event_type"}
    missing = required - set(calendar.columns)
    if missing:
        raise ValueError(f"Academic calendar is missing columns: {sorted(missing)}")
    calendar["start_date"] = pd.to_datetime(calendar["start_date"], errors="raise")
    calendar["end_date"] = pd.to_datetime(calendar["end_date"], errors="raise")
    if (calendar["end_date"] < calendar["start_date"]).any():
        raise ValueError("An academic calendar event ends before it starts.")
    return calendar


def add_context_features(df: pd.DataFrame, calendar: pd.DataFrame) -> pd.DataFrame:
    """Attach calendar context; retain multiple events on a date as separate labels."""
    out = df.copy()
    out["weekday"] = out["date"].dt.day_name()
    out["is_weekend"] = out["date"].dt.dayofweek >= 5
    out["calendar_events"] = ""
    out["is_vacation"] = False
    out["is_holiday"] = False
    out["is_college_event"] = False
    out["is_academic_activity"] = False

    type_to_flag = {
        "vacation": "is_vacation",
        "holiday": "is_holiday",
        "college_event": "is_college_event",
        "academic_activity": "is_academic_activity",
    }
    for _, event in calendar.iterrows():
        mask = out["date"].between(event["start_date"], event["end_date"])
        out.loc[mask, "calendar_events"] = out.loc[mask, "calendar_events"].apply(
            lambda existing: "; ".join(x for x in [existing, event["event_name"]] if x)
        )
        flag = type_to_flag.get(event["event_type"])
        if flag:
            out.loc[mask, flag] = True
    return out


def add_per_student_features(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    denominator = out["students_served_est"].where(out["students_served_est"] > 0)
    for source, target in INGREDIENT_COLUMNS.items():
        out[target] = out[source] / denominator
    # Do not use total_food_mass_kg_approx: it combines kg, litres and item counts.
    return out


def prepare_analysis_data(df: pd.DataFrame, calendar: pd.DataFrame) -> pd.DataFrame:
    return add_per_student_features(add_context_features(df, calendar))
