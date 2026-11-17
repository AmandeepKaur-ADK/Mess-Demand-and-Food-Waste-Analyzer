from pathlib import Path
import streamlit as st
import pandas as pd

from src.data_loader import load_mess_data, data_quality_report
from src.preprocessing import load_calendar, prepare_analysis_data, INGREDIENT_COLUMNS

ROOT = Path(__file__).parent
DATA_PATH = ROOT / "data" / "raw" / "data.csv"
CALENDAR_PATH = ROOT / "config" / "academic_calendar.csv"

st.set_page_config(page_title="Mess Demand Analyser", page_icon="🍽️", layout="wide")
st.title("Mess Demand Analyser")
st.caption("Historical ingredient usage and academic-calendar context")

try:
    raw = load_mess_data(DATA_PATH)
    calendar = load_calendar(CALENDAR_PATH)
    data = prepare_analysis_data(raw, calendar)
except Exception as exc:
    st.error(f"Could not load project data: {exc}")
    st.stop()

report = data_quality_report(raw)
col1, col2, col3, col4 = st.columns(4)
col1.metric("Daily records", report["rows"])
col2.metric("Distinct dates", report["unique_dates"])
col3.metric("Students (average)", f"{raw['students_served_est'].mean():.0f}")
col4.metric("Weekday mismatches", report["weekday_mismatches"])

st.subheader("Data quality")
st.json(report)

st.subheader("Daily student count")
st.line_chart(data.set_index("date")["students_served_est"])

st.subheader("Ingredient use per student")
selected = st.selectbox("Choose ingredient", list(INGREDIENT_COLUMNS.keys()))
per_student_col = INGREDIENT_COLUMNS[selected]
st.line_chart(data.set_index("date")[per_student_col])

st.subheader("Academic context matched to records")
context_cols = ["date", "weekday", "students_served_est", "calendar_events", "is_vacation", "is_holiday", "is_college_event", "is_academic_activity"]
st.dataframe(data[context_cols], use_container_width=True, hide_index=True)

st.subheader("Historical records")
st.dataframe(raw, use_container_width=True, hide_index=True)
st.info("This first version describes recorded ingredient usage. It does not measure leftovers or claim to predict food waste.")
