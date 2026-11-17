# Mess Demand Analyser

A small, explainable tool to analyse actual daily mess ingredient records alongside the academic calendar and weekly mess menu. The intended user is mess staff responsible for estimating food preparation quantities.

## Current implementation status

- [x] Load the supplied daily CSV records.
- [x] Validate required fields, dates, duplicate dates, weekday consistency and quantity anomalies.
- [x] Attach academic-calendar events to matching dates.
- [x] Calculate ingredient usage per recorded student.
- [ ] Transcribe and validate the revised weekly mess menu.
- [ ] Analyse menu and academic-context effects.
- [ ] Implement and validate preparation recommendations.

## Data provenance

`data/raw/data.csv` contains records transcribed from the mess's actual bookkeeper/manager records, as confirmed by the project researcher. Preserve the source file and do not fabricate missing values. The `students_served_est` field is explicitly an estimate.

The academic calendar in `config/academic_calendar.csv` is transcribed from the calendar image supplied for this project. The weekly menu in `config/mess_menu.csv` is a schema template pending careful transcription and confirmation that the revised menu applies to the dataset period.

## Setup

```bash
python -m venv .venv
# Windows PowerShell:
.venv\Scripts\Activate.ps1
# macOS/Linux:
# source .venv/bin/activate
pip install -r requirements.txt
```

## Run

```bash
streamlit run app.py
```

## Important measurement limitation

`total_food_mass_kg_approx` is excluded from analysis because the source combines kilograms, litres and piece counts. The CSV records ingredient usage, not measured leftovers. Therefore this version does not calculate actual food waste.

## Project layout

```text
config/academic_calendar.csv
config/mess_menu.csv
data/raw/data.csv
src/data_loader.py
src/preprocessing.py
app.py
```
