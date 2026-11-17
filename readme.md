# Mess Demand Analyser

A small Streamlit tool that helps the Hostel A mess at NIT Jamshedpur look at its own historical ingredient usage, see the academic calendar and weekly menu alongside it, and get a simple, transparent preparation estimate for an upcoming day.

|                    |                                                                                                |
| ------------------ | ---------------------------------------------------------------------------------------------- |
| **Place**          | Hostel A Mess, NIT Jamshedpur, Jharkhand                                                       |
| **People**         | Bhusan Kumar (Mess Manager), Sandeep (Mess Supervisor), Anubhav (mess staff)                   |
| **Intended users** | Mess Manager / Mess Supervisor, who decide preparation quantities                              |
| **Scale**          | About 400-450 female students across two hostels sharing one kitchen                           |
| **Fieldwork**      | 17 November 2026, observation 12:40 PM-1:15 PM, interview at 12:45 PM with Sandeep and Anubhav |
| **Built with**     | Python, pandas, Streamlit                                                                      |

## The problem

Preparation quantities in the mess are decided by the cook from experience. According to the staff, the cook takes into account the day and its menu, the meal, holidays and vacations, college events, examinations, and which dishes are served together (for example, egg curry and dry vegetables need more rotis; sambar and rajma need more rice). None of this is analysed with a tool.

Two further findings from the visit shaped the scope:

- Leftover food is **not measured**. Staff photograph it and share the photos in a group, and it is generally discarded.
- Complete shortages are uncommon, but individual dishes sometimes run out before the meal ends.

Because leftovers are not recorded, this tool **does not measure or predict food waste**. It only works with what was recorded: daily ingredient usage and an estimated student count.

Full details: [`fieldwork.md`](fieldwork.md) and [`research.md`](research.md).

## What the app does

`app.py` shows five sections:

1. **Historical consumption** - line chart of estimated students served per day, and a per-student usage chart for an ingredient you select. Per-student values are the recorded daily quantity divided by the recorded estimated student count.
2. **Academic calendar context** - table of each record's date, weekday, estimated students, calendar events, and flags for vacation, holiday, college event, academic activity and academic deadline.
3. **Weekly menu matched to each record** - indicators for whether lunch (and any meal) has gravy, egg curry or dry vegetables, taken from the revised weekly menu. Daily ingredient totals cannot show which meal consumed what.
4. **Daily preparation estimate** - choose a date and an expected number of students, then click _Generate preparation estimate_. The estimate is the **median historical ingredient use per student from previous records**, scaled by the expected students. Same-weekday history is used when at least two prior records exist.
5. **Data quality report and original records** - expandable sections showing the data quality report (rows, distinct dates, weekday mismatches) and the raw records.

The top of the page also shows four metrics: daily records, distinct dates, average students, and weekday mismatches.

## Data

The data was collected by us from the mess's own operational records (the bookkeeper's handwritten daily records and the manager's Excel sheets). No downloaded or generated data is used.

| File                           | Used for                                                                    |
| ------------------------------ | --------------------------------------------------------------------------- |
| `data/raw/data.csv`            | Daily mess records (date, estimated students served, ingredient quantities) |
| `config/academic_calendar.csv` | Vacations, holidays, college events, academic activities and deadlines      |
| `config/mess_menu.csv`         | Revised weekly menu                                                         |

Known data facts:

- Records are **daily totals**, not per meal.
- The student count is an **estimate** (`students_served_est`).
- Leftover quantities are **not recorded**.

> **To complete before submission:** number of entries in `data.csv`; the dates covered; how and where each value was collected and its source (handwritten register or Excel sheet); and the column names and units. Take these from the actual file.

## How to run

Requirements: Python and pip. The dependencies are listed in `requirements.txt`:

```
pandas>=2.2,<3.0
streamlit>=1.40,<2.0
matplotlib>=3.8,<4.0
pytest>=8.0,<9.0
```

```bash
git clone <REPOSITORY_URL>
cd <REPOSITORY_FOLDER>

python -m venv .venv
# Windows:      .venv\Scripts\activate
# Linux/macOS:  source .venv/bin/activate

pip install -r requirements.txt
streamlit run app.py
```

Open the local URL that Streamlit prints in the terminal. The app expects the three data files above at exactly those paths relative to `app.py`; if any cannot be loaded it shows "Could not load project data" with the error and stops.

> **To complete:** repository URL, folder name, and the Python version you actually ran it with.

## Real output

> **To complete:** run the app on the real data and paste the actual results here: the four top metrics, one example estimate table (state the date and expected students you entered), and a screenshot. Do not enter numbers that did not come from a real run.

## What it gets wrong

- **It is a baseline, not a validated forecast.** The estimate uses only historical per-student medians. The calendar events and menu are displayed as context but are **not** used as adjustment factors, even though the staff say they matter.
- **Menu combinations are not modelled.** Staff say rice and roti needs depend on which dishes are served together. This tool does not capture that.
- **No waste calculation.** Leftovers are not recorded, so it cannot say how much was wasted or over-prepared, as we did not have any record for it to track.
- **Daily totals only.** It cannot estimate separately for breakfast, lunch and dinner.
- **Estimated headcount.** Errors in `students_served_est` flow into every per-student figure.
- **Small history.** With few records, medians (especially same-weekday ones) are based on very few days.
- **Individual dishes running out** is not addressed.

The output supports the staff's decision; it should not replace the cook's judgement.

## Repository contents

```
app.py                         Streamlit app
output/                         contains the screen recording of the tool
src/
  data_loader.py               load_mess_data, data_quality_report
  preprocessing.py             load_calendar, load_menu, prepare_analysis_data, INGREDIENT_COLUMNS
  recommendation.py            make_daily_baseline
config/
  academic_calendar.csv
  mess_menu.csv
data/raw/data.csv
requirements.txt
research.md                    Problem, existing solutions, sources
fieldwork.md                   Visit, interview, findings
.gitignore
```

Also required for the assignment and to be present in the repo: `reflection.md`, an `ai-chats/` folder with exported AI chats, and the fieldwork photographs and interview transcript referenced in `fieldwork.md`.

## Existing solutions considered

- **Mealiez** (https://www.mealiez.in/): a broader mess management platform (booking, attendance, billing, inventory, analytics). Not evaluated hands-on; this project is deliberately narrower.
- **Handwritten registers and Excel sheets**: already used by the mess to record usage and compare finances, but not set up for analysing demand patterns.

## Demo

> **To complete:** link to the 3-minute screen recording.

## Reflection and AI use

`reflection.md` is written by the author without AI. AI assistance used during development is exported in `ai-chats/`. Field observations, interview content and recorded data were gathered by the author in person.
