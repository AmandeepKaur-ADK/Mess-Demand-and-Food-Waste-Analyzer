
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


MENU_FLAGS = [
    "has_gravy",
    "has_egg_curry",
    "has_dry_vegetables",
]


def load_calendar(path: str | Path) -> pd.DataFrame:
    calendar = pd.read_csv(path)

    required = {
        "event_name",
        "start_date",
        "end_date",
        "event_type",
    }

    missing = required - set(calendar.columns)

    if missing:
        raise ValueError(
            f"Academic calendar missing columns: {sorted(missing)}"
        )

    calendar["start_date"] = pd.to_datetime(
        calendar["start_date"], errors="raise"
    )
    calendar["end_date"] = pd.to_datetime(
        calendar["end_date"], errors="raise"
    )

    if (calendar["end_date"] < calendar["start_date"]).any():
        raise ValueError("An event ends before its start date.")

    return calendar


def load_menu(path: str | Path) -> pd.DataFrame:
    menu = pd.read_csv(path)

    required = {
        "day",
        "meal",
        "menu_items",
        *MENU_FLAGS,
    }

    missing = required - set(menu.columns)

    if missing:
        raise ValueError(
            f"Mess menu missing columns: {sorted(missing)}"
        )

    menu["day"] = menu["day"].astype("string").str.strip().str.title()
    menu["meal"] = menu["meal"].astype("string").str.strip().str.title()

    if menu.duplicated(["day", "meal"]).any():
        raise ValueError("Duplicate day and meal entries found.")

    for column in MENU_FLAGS:
        normalized = (
            menu[column]
            .astype("string")
            .str.strip()
            .str.lower()
        )

        normalized = normalized.replace({
            "yes": "1",
            "no": "0",
            "true": "1",
            "false": "0",
        })

        invalid = ~normalized.isin(["0", "1"])

        if invalid.any():
            bad_values = menu.loc[invalid, column].unique().tolist()

            raise ValueError(
                f"{column} contains invalid values: {bad_values}. "
                "Use 1 for yes and 0 for no."
            )

        menu[column] = normalized.astype(int)

    return menu


def add_context_features(
    df: pd.DataFrame,
    calendar: pd.DataFrame,
) -> pd.DataFrame:

    out = df.copy()

    out["date"] = pd.to_datetime(out["date"], errors="raise")
    out["weekday"] = out["date"].dt.day_name()
    out["is_weekend"] = out["date"].dt.dayofweek >= 5

    out["calendar_events"] = ""

    flags = {
        "vacation": "is_vacation",
        "holiday": "is_holiday",
        "college_event": "is_college_event",
        "academic_activity": "is_academic_activity",
        "academic_deadline": "is_academic_deadline",
    }

    for flag in flags.values():
        out[flag] = False

    for _, event in calendar.iterrows():
        mask = out["date"].between(
            event["start_date"],
            event["end_date"],
        )

        out.loc[mask, "calendar_events"] = (
            out.loc[mask, "calendar_events"]
            .apply(
                lambda existing: "; ".join(
                    x for x in [
                        existing,
                        event["event_name"],
                    ] if x
                )
            )
        )

        flag = flags.get(event["event_type"])

        if flag:
            out.loc[mask, flag] = True

    return out


def attach_menu_context(
    df: pd.DataFrame,
    menu: pd.DataFrame,
) -> pd.DataFrame:

    out = df.copy()

    daily_menu = menu.groupby("day")[MENU_FLAGS].max()

    for column in MENU_FLAGS:
        out[f"any_meal_{column}"] = (
            out["weekday"].map(daily_menu[column])
        )

    lunch_menu = (
        menu[menu["meal"].str.lower() == "lunch"]
        .set_index("day")[MENU_FLAGS]
    )

    for column in MENU_FLAGS:
        out[f"lunch_{column}"] = (
            out["weekday"].map(lunch_menu[column])
        )

    menu_columns = [
        f"any_meal_{column}" for column in MENU_FLAGS
    ] + [
        f"lunch_{column}" for column in MENU_FLAGS
    ]

    if out[menu_columns].isna().any().any():
        raise ValueError(
            "Missing menu classification for one or more weekdays."
        )
    daily_menu_summary = (
    menu.groupby("day")["menu_items"]
    .apply(
        lambda items: " | ".join(
            f"{meal}: {dish}"
            for meal, dish in zip(
                menu.loc[items.index, "meal"],
                items
            )
        )
        )
    )

    out["menu_summary"] = out["weekday"].map(
        daily_menu_summary
    )
    return out


def add_per_student_features(
    df: pd.DataFrame,
) -> pd.DataFrame:

    out = df.copy()

    denominator = out["students_served_est"].where(
        out["students_served_est"] > 0
    )

    for source, target in INGREDIENT_COLUMNS.items():
        if source not in out.columns:
            continue

        out[target] = out[source] / denominator

    return out


def prepare_analysis_data(
    df: pd.DataFrame,
    calendar: pd.DataFrame,
    menu: pd.DataFrame,
) -> pd.DataFrame:

    out = add_context_features(df, calendar)
    out = attach_menu_context(out, menu)
    out = add_per_student_features(out)

    return out
