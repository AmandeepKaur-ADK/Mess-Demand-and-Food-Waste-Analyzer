
from pathlib import Path
import streamlit as st
import pandas as pd

from src.data_loader import load_mess_data, data_quality_report
from src.preprocessing import (
    load_calendar,
    load_menu,
    prepare_analysis_data,
    INGREDIENT_COLUMNS,
)
from src.recommendation import make_daily_baseline


ROOT = Path(__file__).parent

DATA_PATH = ROOT / "data" / "raw" / "data.csv"
CALENDAR_PATH = ROOT / "config" / "academic_calendar.csv"
MENU_PATH = ROOT / "config" / "mess_menu.csv"


st.set_page_config(
    page_title="Mess Demand Analyser",
    page_icon="🍽️",
    layout="wide"
)

st.title("Mess Demand Analyser")
st.caption(
    "Historical ingredient usage and academic-calendar context"
)


try:
    raw = load_mess_data(DATA_PATH)
    calendar = load_calendar(CALENDAR_PATH)
    menu = load_menu(MENU_PATH)

    data = prepare_analysis_data(
        raw,
        calendar,
        menu
    )

except Exception as exc:
    st.error(f"Could not load project data: {exc}")
    st.stop()


report = data_quality_report(raw)
col1, col2, col3, col4 = st.columns(4)
col1.metric("Daily records", report["rows"])
col2.metric("Distinct dates", report["unique_dates"])
col3.metric("Students (average)", f"{raw['students_served_est'].mean():.0f}")
col4.metric("Weekday mismatches", report["weekday_mismatches"])

st.subheader("1. Historical consumption")
st.line_chart(data.set_index("date")["students_served_est"])
selected = st.selectbox("Ingredient usage per student", list(INGREDIENT_COLUMNS.keys()))
st.line_chart(data.set_index("date")[INGREDIENT_COLUMNS[selected]])
st.caption("Per-student values are daily recorded quantities divided by the recorded estimated student count.")

st.subheader("2. Academic calendar context")
context_cols = ["date", "weekday", "students_served_est", "calendar_events", "is_vacation", "is_holiday", "is_college_event", "is_academic_activity", "is_academic_deadline"]
st.dataframe(data[context_cols], use_container_width=True, hide_index=True)

st.subheader("3. Weekly menu matched to each record")

menu_cols = [
    "date",
    "weekday",
    "lunch_has_gravy",
    "lunch_has_egg_curry",
    "lunch_has_dry_vegetables",
    "any_meal_has_gravy",
    "any_meal_has_egg_curry",
    "any_meal_has_dry_vegetables",
]

st.dataframe(
    data[menu_cols],
    use_container_width=True,
    hide_index=True
)

st.caption(
    "Menu indicators are derived from the revised weekly menu. "
    "Daily ingredient totals cannot establish meal-specific consumption."
)

st.subheader("4. Daily preparation estimate")
st.write("A transparent baseline using the median historical ingredient use per student from previous records. Same-weekday history is used when at least two prior records exist.")
min_date = raw["date"].min().date()
max_date = raw["date"].max().date()
target_date = st.date_input("Date to estimate", value=max_date + pd.Timedelta(days=1), min_value=min_date)
expected_students = st.number_input("Expected students", min_value=1, max_value=1000, value=int(raw["students_served_est"].median()), step=1)
if st.button("Generate preparation estimate"):
    estimate = make_daily_baseline(raw, pd.Timestamp(target_date), int(expected_students))
    st.dataframe(estimate, use_container_width=True, hide_index=True)
    st.warning("This is a historical baseline, not a validated forecast. Academic events and menu are displayed as context but are not yet used as numerical adjustment factors. Leftover quantities are not recorded, so this tool does not calculate food waste.")

with st.expander("Data quality report"):
    st.json(report)
with st.expander("Original historical records"):
    st.dataframe(raw, use_container_width=True, hide_index=True)