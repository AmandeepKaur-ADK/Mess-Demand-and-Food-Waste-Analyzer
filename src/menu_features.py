from pathlib import Path
import pandas as pd

MEALS = ["Breakfast", "Lunch", "Snacks", "Dinner"]


def load_menu(path: str | Path) -> pd.DataFrame:
    menu = pd.read_csv(path)
    required = {"day", "meal", "menu_items"}
    missing = required - set(menu.columns)
    if missing:
        raise ValueError(f"Mess menu is missing required columns: {sorted(missing)}")
    menu["day"] = menu["day"].astype(str).str.strip().str.title()
    menu["meal"] = menu["meal"].astype(str).str.strip().str.title()
    menu["menu_items"] = menu["menu_items"].fillna("").astype(str)
    if menu.duplicated(["day", "meal"]).any():
        duplicates = menu.loc[menu.duplicated(["day", "meal"], keep=False), ["day", "meal"]]
        raise ValueError(f"Duplicate day/meal menu entries: {duplicates.to_dict('records')}")
    invalid_days = set(menu["day"]) - set(pd.Series(pd.date_range("2026-01-05", periods=7, freq="D").day_name()))
    if invalid_days:
        raise ValueError(f"Unrecognized weekdays in menu: {sorted(invalid_days)}")
    return menu


def attach_menu_context(df: pd.DataFrame, menu: pd.DataFrame) -> pd.DataFrame:
    """Attach the weekly menu for each date. Daily records remain daily aggregates."""
    out = df.copy()
    out["weekday"] = out["date"].dt.day_name()
    # The raw CSV also has a `day` column; use the date-derived weekday for joining.
    out = out.drop(columns=["day"], errors="ignore")
    menu_by_day = (
        menu.groupby("day").apply(
            lambda g: " | ".join(f"{r.meal}: {r.menu_items}" for r in g.itertuples()),
            include_groups=False,
        ).rename("menu_summary").reset_index()
    )
    out = out.merge(menu_by_day, left_on="weekday", right_on="day", how="left", validate="many_to_one")
    out = out.drop(columns=["day"], errors="ignore")
    out["menu_available"] = out["menu_summary"].notna()
    text = out["menu_summary"].fillna("").str.lower()
    # These are transparent keyword indicators, not measured ingredient quantities.
    out["menu_has_egg"] = text.str.contains(r"egg|omelette", regex=True)
    out["menu_has_gravy_or_curry"] = text.str.contains(r"curry|masala|sambar|dal|chana", regex=True)
    out["menu_has_roti_or_paratha"] = text.str.contains(r"roti|paratha|puri|bhature", regex=True)
    out["menu_has_rice"] = text.str.contains(r"rice", regex=True)
    return out
