from pathlib import Path
import pandas as pd

from src.data_loader import load_mess_data
from src.menu_features import load_menu
from src.preprocessing import load_calendar, prepare_analysis_data
from src.recommendation import make_daily_baseline

ROOT = Path(__file__).resolve().parents[1]


def test_menu_and_calendar_join_to_all_daily_records():
    raw = load_mess_data(ROOT / "data/raw/data.csv")
    calendar = load_calendar(ROOT / "config/academic_calendar.csv")
    menu = load_menu(ROOT / "config/mess_menu.csv")
    prepared = prepare_analysis_data(raw, calendar, menu)
    assert len(prepared) == len(raw)
    assert prepared["menu_available"].all()


def test_menu_has_seven_days_and_four_meal_slots():
    menu = load_menu(ROOT / "config/mess_menu.csv")
    assert menu["day"].nunique() == 7
    assert len(menu) == 28
    assert set(menu["meal"]) == {"Breakfast", "Lunch", "Snacks", "Dinner"}


def test_baseline_uses_only_prior_same_weekday_records():
    raw = load_mess_data(ROOT / "data/raw/data.csv")
    result = make_daily_baseline(raw, pd.Timestamp("2026-11-17"), 420)
    assert not result.empty
    assert set(result["basis"]) == {"previous Tuesday records"}
    assert (result["estimated_quantity"] >= 0).all()


def test_baseline_rejects_nonpositive_student_count():
    raw = load_mess_data(ROOT / "data/raw/data.csv")
    try:
        make_daily_baseline(raw, pd.Timestamp("2026-11-17"), 0)
    except ValueError as exc:
        assert "greater than zero" in str(exc)
    else:
        raise AssertionError("Expected ValueError for zero students")
