# Mess Analyser Interview Plan

**User:** Anonymous  
**Created:** 11/18/2026 3:49:55  
**Updated:** 11/18/2026 3:49:56  
**Exported:** 11/18/2026 3:55:49  
**Link:** [https://chatgpt.com/share/6afcd30b-4720-83ee-aa8b-8ef6cd193f59](https://chatgpt.com/share/6afcd30b-4720-83ee-aa8b-8ef6cd193f59)  

## Prompt:
11/17/2026, 10:41:43 AM

# 1-Day Take-Home Assignment for B.Tech Graduates

## The task

In 24 hours, find one small real problem you have seen near you in the last week, build a simple tool that helps one real person with it, and push it to a public Git repo.

Use AI as much as you like for research and code. Two parts cannot be done by AI: going to the place and talking to the person (Step 2), and the reflection (Step 4). Those are what we are judging most.

**Rules**

•         The problem must be one you saw yourself, within walking distance of home or college. Not from a tutorial or the internet.

•         The tool must help a real person you can name (a shopkeeper, warden, guard, canteen staff, a family member) who is not you.

•         The tool must run on data you collected yourself: at least 20 real entries (counts, prices, timings). No downloaded or generated data.

•         Rejected automatically: to-do app, weather app, chatbot, portfolio, anything with Kaggle or API data.

**Example of the right size:** the chai stall outside college runs out of milk some days and wastes it on others. You count sales for a day, ask the owner how he decides the order, and write a small script that suggests tomorrow's milk quantity.

## The four steps

| &#x20;&#x20;&#x20;&#x20; |
| ------------------------ |

Step

| &#x20;&#x20;&#x20;&#x20; |
| ------------------------ |

Time

| &#x20;&#x20;&#x20;&#x20; |
| ------------------------ |

What    you hand in

| &#x20;&#x20;&#x20; |
| ------------------ |

1\. Find and research

| &#x20;&#x20;&#x20; |
| ------------------ |

1.5 h

| &#x20;&#x20;&#x20; |
| ------------------ |

research.md: the problem in 5 lines, 2 existing solutions and why they do not   fit your person, 2 sources you actually read with a 3-line note each

| &#x20;&#x20;&#x20; |
| ------------------ |

2\. Go outside

| &#x20;&#x20;&#x20; |
| ------------------ |

1.5 h

| &#x20;&#x20;&#x20; |
| ------------------ |

fieldwork.md: 20 minutes at the place with 2 timestamped photos; one   conversation with your person (name, role, 3 things they said, 1 thing that   surprised you); your raw data in data.csv with a note on how you   collected it

| &#x20;&#x20;&#x20; |
| ------------------ |

3\. Build

| &#x20;&#x20;&#x20; |
| ------------------ |

4 h

| &#x20;&#x20;&#x20; |
| ------------------ |

Working code that reads data.csv   and gives one useful output; a README with how to run it, the real output,   and what it gets wrong

| &#x20;&#x20;&#x20; |
| ------------------ |

4\. Reflect

| &#x20;&#x20;&#x20; |
| ------------------ |

1 h

| &#x20;&#x20;&#x20; |
| ------------------ |

reflection.md, written without AI, half a page: what you got wrong at the   start, what you would cut, where AI helped and where it wasted time. Plus a   3-minute screen recording of the tool running, linked in the README

## Git and submission

•         Your first commit, within the first hour, is research.md with your problem and your person. This locks your choice.

•         At least 5 commits spread across the day, with messages in your own words.

•         Export the AI chats you used into an ai-chats/ folder. We read them; it is fine, we expect them.

•         Email the repo link within 24 hours. A 10-minute call follows, where we will ask you to open a row of your data and say where you were when you recorded it, feed the tool a bad row, and change one thing in the code live.

## Scoring (for the panel, remove before sending)

Four parts, 25 points each: research depth, uniqueness of the problem, fieldwork evidence, build and call. Fieldwork below 10 is a reject regardless of total.

Red flags: README with no place, person or date; data.csv with round numbers and no gaps; a conversation with nothing surprising in it; one big commit at the end; a reflection that could fit any project; model-written code with an empty ai-chats/ folder.

Call questions: pick one data row and ask where they were; ask what the person said that changed the plan; ask them to change a threshold live; ask what the tool should not be trusted for.

Mess Demand & Food Waste Analyser

use one chat we have analyze it as welll and first tell me one by one what to do and what questions to ask

## Response:
11/17/2026, 10:41:43 AM · gpt-6

> **Starting the fieldwork**
>
> I’m treating the project as provisional until interviews validate it. First, I’m visiting the mess, introducing the idea without pitching, and asking: “How do you currently plan meals, record attendance, and track leftovers?”
>
> ****
>
> 
>
> **Reviewed take-home assignment, mess plans, location, and access**
>
> 
>
> Worked for 8s

# Mess Demand &amp; Food Waste Analyser - Assignment Execution Plan

We will treat this as a real field-research project, not a coding assignment.

From our previous discussion, we have three important facts\:

- **Location\:** College mess.
- **Access\:** You can directly speak with the mess owner/manager or staff.
- **Data access\:** You can collect actual daily records.

Our provisional project is **Mess Demand &amp; Food Waste Analyser**\.

However, we will NOT assume that food wastage is the actual problem. We need to discover what the mess staff genuinely struggle with, validate it, and then build a tool around that problem.

## 1\. Understand what we are trying to build

## Mess Demand &amp; Food Waste Analyser
[![Services | Shri Sai Food Solutions](https://images.openai.com/static-rsc-4/xJncfcfswsQvWiH0D0lQ28Koc8O_zTqGTgo27ipjr9q5GvKgJqnlAhTAR2d3aHRXUU2dv2UI5Vaq2q8F9t1du-IrBoM-Cpmy351uEjEQTIyzlmyRRWMLEmhWDsGvuuIBa9MeLkvqUkE0xcrlFzMBnJ9ZbQvKFjDNu4daTGSJhysjiPcs6Jr5UZYptfOM6IBo?purpose=fullsize)](https://shrisaifoods.com/services)

**Our initial hypothesis**

Mess staff may have difficulty estimating how much food to prepare for each meal.

This could lead to\:

- Excess food preparation and wastage.
- Insufficient food during peak demand.
- Difficulty estimating the next day's requirements.

**Potential solution**

A simple tool that reads actual mess records and helps staff estimate food preparation quantities for upcoming meals.

(Hypothesis - requires field validation)

## 2\. Exactly what to do, step by step

1. **Step 1 - Visit the mess (first 15-20 minutes)**
   
   Don't start by telling the manager that you are building a food-waste analyser.
   
   Observe the actual operations\:
   
   - How food is prepared.
   - How students are served.
   - How staff estimate quantities.
   - Whether leftovers are measured.
   - Whether shortages occur.
   - Whether any records are maintained.
   
   **Your objective\:** Find one operational difficulty.
2. **Step 2 - Talk to the mess manager/owner (20-30 minutes)**
   
   Introduce your assignment\:
   
   "I am working on a small college project where I need to understand one real problem faced by someone working here. I want to understand how mess operations work, especially food preparation, quantity estimation and leftover management. I would also like to collect some actual records, with your permission."
   
   Then ask the questions below in order.
3. **Step 3 - Validate the problem (15 minutes)**
   
   Determine whether the problem is\:
   
   - Frequent.
   - Actually troublesome.
   - Something the person wants improved.
   - Solvable with a small software tool.
   
   Don't force the food-waste idea if the manager identifies a different, more important problem.
4. **Step 4 - Collect actual data (20-30 minutes)**
   
   Ask permission to inspect existing records.
   
   Collect at least 20 genuine entries. These could be historical daily meal records, provided you can verify their source.
   
   Take two timestamped photos showing the actual environment or records, with permission.
5. **Step 5 - Document and commit**
   
   Prepare `research.md`, `fieldwork.md` and `data.csv`\.
   
   Push the first commit within the first hour. Update the documents as your research progresses; don't invent interview findings or observations.
6. **Step 6 - Build the tool**
   
   Build only after understanding the actual problem and the available data.
   
   The tool must read your real CSV and produce an output useful to the person you interviewed.
7. **Step 7 - Test, reflect and submit**
   
   Test with actual data and deliberately malformed data. Record a three-minute demonstration, write your own reflection, export your AI chats and push everything to a public GitHub repository.

---

## 3\. Questions to ask the mess manager

This is the most important part of the assignment.

Do not ask all questions mechanically. Let the conversation flow, and ask follow-up questions based on their answers.

### A. Understand the mess operations

Start with these questions.

| No. | Question | What we want to discover |
|--------|--------|--------|
| 1 | Can you explain how food preparation is planned every day? | Planning process |
| 2 | How do you decide how much food to prepare? | Quantity estimation |
| 3 | Do you have a fixed number of students eating every day? | Demand variability |
| 4 | Does the number of students change between breakfast, lunch and dinner? | Meal-wise demand |
| 5 | Who makes the decision about food quantities? | Responsible person |

### B. Discover actual problems

These are more important than the first set.

| No. | Question | What we want to discover |
|--------|--------|--------|
| 6 | What is the most difficult part of managing the mess daily? | Primary pain point |
| 7 | Does food sometimes remain unused after meals? | Food wastage |
| 8 | How do you decide what to do with leftover food? | Waste management |
| 9 | Does food ever finish before everyone has eaten? | Food shortages |
| 10 | Which food items are most frequently left over? | Item-level waste |
| 11 | Are there particular days when more food is wasted? | Patterns |
| 12 | What happens when the number of students suddenly increases or decreases? | Unexpected demand |

**Important follow-up\:**

If they say food is wasted, ask\:

- How frequently does this happen?
- Approximately how much food remains?
- How do you currently measure it?
- Does it create a financial loss?
- What do you currently do to prevent it?

Don't accept vague answers like "sometimes a lot". Ask for a real example from the last few days.

### C. Understand their existing data

| No. | Question |
|--------|--------|
| 13 | Do you maintain daily records of food prepared? |
| 14 | Do you record how many students eat each meal? |
| 15 | Do you record leftover food quantities? |
| 16 | Are these records maintained in a notebook, Excel or somewhere else? |
| 17 | Can I examine some previous records for my assignment? |
| 18 | Would you be comfortable sharing at least 20 actual entries? |

### D. Understand what would actually help them

| No. | Question |
|--------|--------|
| 19 | If you could improve one thing in the mess management process, what would it be? |
| 20 | Would knowing tomorrow's approximate food requirements be useful? |
| 21 | What information would you need before trusting such an estimate? |
| 22 | What would make a software tool inconvenient for you? |

### E. Ask these three questions before leaving

These are particularly important for the assignment's evaluation.

1. Can you tell me about one recent incident when food preparation or management did not go as planned?
2. What did you do to solve that problem?
3. If I build a small tool to help with this, what is the one output that would genuinely save you time or money?

---

## 4\. How to represent the evidence

Create this folder structure\:

```text
mess-demand-analyser/
│
├── research.md
├── fieldwork.md
├── data.csv
├── reflection.md
│
├── src/
│   └── ...
│
├── screenshots/
│   ├── mess_observation_1.jpg
│   └── mess_observation_2.jpg
│
├── ai-chats/
│
└── README.md
```

### Example of the data we might collect

This is a proposed schema, NOT data to submit. We must collect actual values.

`data.csv`

```csv
date,meal,food_item,prepared_kg,served_students,leftover_kg
```

If the manager has data only at meal level, don't force item-level collection. Adapt the schema to what is genuinely available.

For example, your actual records might contain\:

- Date
- Meal type
- Number of students served
- Quantity prepared
- Quantity remaining

We need at least 20 actual entries, with missing values preserved rather than fabricated.

### Evidence requirements

**What the evaluator should be able to verify**

Two timestamped photos

---

Actual person's name and role

---

Three statements and one surprising observation

---

20+ genuine data entries

---

Notes describing how the data was collected

---

## 5\. What goes into research.md?

Initially, this is a working document.

```markdown
# Research: Mess Demand & Food Waste Analyser

## 1. Problem Statement
[What problem did I personally observe?]
[Who experiences this problem?]
[How frequently does it occur?]
[What is its impact?]
[Why does it need a solution?]

## 2. Person Affected
Name:
Role:
Location:
How I accessed this person:

## 3. Existing Solutions

### Solution 1
Name:
How it works:
Why it does not fit this person:

### Solution 2
Name:
How it works:
Why it does not fit this person:

## 4. Research Sources

### Source 1
Title:
URL:
What I learned:
What is relevant to my problem:

### Source 2
Title:
URL:
What I learned:
What is relevant to my problem:
```

The two existing solutions must be real solutions you investigate, not two invented alternatives. Read two actual sources and document what you learned from them.

---

## 6\. Our immediate execution: start with the interview

Don't start coding. Don't design the interface. Don't decide the algorithm.

First, get the facts.

**Current milestone** (Field research)

of  completed %

### Before we proceed, I need one thing from you\:

**Have you already spoken to the mess manager, or are you going to meet them now?**

If you haven't, take the questions above with you. Come back with their actual answers, even if they are incomplete.

We will then work through their answers one by one, identify the strongest problem, decide exactly what data to collect, and finalize the project scope before writing the code.

The objective is to build something that a real mess employee would actually use, not merely something that looks impressive in a GitHub repository.

## Prompt:
11/17/2026, 10:53:41 AM

lets do our first commit and do first step by telling what our idea is

## Response:
11/17/2026, 10:53:40 AM · gpt-6

> **Drafting initial research**
>
> I’m framing the mess kitchen as a provisional setting, with the manager as the intended interviewee. I’ll compare manual tracking with Mealiez, while clearly marking assumptions until direct observation confirms the problem.
>
> **Drafted initial research**
>
> 
>
> **Searched 10 websites**
>
> 
>
> Worked for 15s

# Step 1 - First Git commit: `research.md`

Our first commit must establish the project idea, the problem we intend to investigate, and the person we want to help.

We are choosing\:

(Provisional project idea)

# Mess Demand &amp; Food Waste Analyser

**Problem we want to investigate**

College mess staff must decide how much food to prepare for each meal. Changes in student attendance and meal demand may cause excess food preparation, wastage, or food shortages.

**Our proposed solution**

A simple data-driven tool that analyses actual mess records to help staff understand food consumption, identify wastage patterns, and estimate appropriate food preparation quantities.

## 1\. Define the idea correctly

We need to distinguish between what we currently believe and what we have actually verified.

| Category | Current position |
|--------|--------|
| Location | College mess, NIT Jamshedpur |
| Potential user | Mess manager / responsible staff member |
| Suspected problem | Difficulty estimating meal demand |
| Possible impact | Food wastage, shortages, financial loss |
| Proposed tool | Demand and food-waste analysis |
| Data required | Actual preparation, consumption, attendance and leftover records |
| Validation | Pending direct observation and interview |

**Important\:** We are not claiming that the mess currently suffers from these problems. These are hypotheses to validate during fieldwork.

## 2\. Create the first `research.md`

Use the following as the initial research document. We will update it after visiting the mess and interviewing the staff member.

**document: **

# Research: Mess Demand & Food Waste Analyser

## 1. Initial Problem Statement

College mess kitchens need to prepare food for a changing number of students across breakfast, lunch and dinner.

1. The quantity of food required may vary from one meal to another.
2. Staff may rely on experience or manual estimates when deciding preparation quantities.
3. Incorrect estimates could result in excess preparation, leftover food or food shortages.
4. We want to investigate whether the mess currently faces this problem and how it affects daily operations.
5. Our goal is to build a small data-driven tool that helps one mess staff member make better food preparation decisions using actual records.

**Status:** Initial hypothesis. Not yet validated through field observation or an interview.

## 2. Person Affected

- **Location:** College mess, NIT Jamshedpur, Jharkhand.
- **Intended user:** Mess manager or staff member responsible for food preparation.
- **Person's name:** To be confirmed during fieldwork.
- **Access:** We can visit the mess, speak directly with the staff and request access to actual operational records.

## 3. Proposed Solution

Mess Demand & Food Waste Analyser will be a simple tool that:

- Reads actual mess data from a CSV file.
- Analyses food preparation, student consumption and leftover quantities.
- Identifies meals or food items with recurring excess or insufficient preparation.
- Provides a practical preparation estimate based on historical records, if the available data supports it.

The tool will be designed around the staff member's actual workflow and data availability.

## 4. Existing Solutions

### Solution 1: Mealiez - Mess Management Software

Website: https://www.mealiez.in/

**How it works:**
Mealiez provides mess management features such as meal booking, attendance tracking, billing, inventory management and analytics.

**Why it may not fit our intended user:**
It is a broader management platform rather than a small, focused tool for analysing the particular preparation and leftover records of one mess. We still need to verify the staff member's current workflow, requirements and willingness to use such software.

### Solution 2: Manual registers and spreadsheets

**How they work:**
Mess staff can maintain daily records of meal counts, food quantities and leftover measurements in notebooks or spreadsheets.

**Why they may not fit our intended user:**
Recording information alone may not make it easy to identify recurring demand patterns or calculate preparation recommendations. We need to investigate whether the mess already uses these methods and what difficulties staff experience with them.

## 5. Research Sources

### Source 1: Food Waste Management Practices and Barriers to Progress in U.S. University Foodservice

URL: https://www.mdpi.com/1660-4601/19/11/6512

**What I learned:**
- The study surveyed 57 university foodservice representatives.
- Common waste reduction strategies included forecasting demand and preparing smaller batches.
- It also identified practical barriers to food donation and composting.

**Relevance to our project:**
This research supports investigating demand estimation and food preparation practices in institutional kitchens. However, its findings concern U.S. universities and cannot automatically be applied to our college mess.

### Source 2: Mealiez - Mess Management Software

URL: https://www.mealiez.in/

**What I learned:**
- Mealiez offers digital meal booking and attendance management.
- It also provides inventory management and analytics features.
- Its product is designed for mess operators, hostels and canteens in India.

**Relevance to our project:**
It gives us an existing commercial solution to compare against. Our project should avoid rebuilding an entire mess management platform and instead solve one specific problem identified by our intended user.

## 6. Validation Pending

During fieldwork, we will establish:

- Whether food overproduction or shortages actually occur.
- How staff currently estimate food preparation quantities.
- Whether leftover food is measured and recorded.
- What historical records are available.
- Which single operational problem the staff member wants us to address.

**Final problem statement and project scope will be updated after the field interview.**

## 3\. Make your first commit

Open your project folder in VS Code.

Create `research.md`, paste the document above, and open the VS Code terminal.

Run\:

```bash
git init
git add research.md
git commit -m "Add initial research and project idea"
```

If Git is already initialized, skip `git init`\.

Then verify\:

```bash
git status
git log --oneline -1
```

## 4\. What this first commit establishes

- The project direction.
- The person we intend to help.
- The problem hypothesis.
- Two existing solutions.
- Initial research and sources.

**Do not add fabricated interview details or sample data.**

Our next step is fieldwork: observe the mess and interview the responsible staff member. That is where we turn this initial idea into a validated problem.

**Your immediate task\:** Create `research.md` and make the first commit. Then tell me whether it was pushed to GitHub or is currently only on your local machine.

## Prompt:
11/17/2026, 11:13:50 AM

How to show the evidence of conversation with the person

## Response:
11/17/2026, 11:13:51 AM · gpt-6

You should document the conversation in `fieldwork.md` as a **timestamped interview record**, supported by photographs and actual observations.

The evaluator should be able to verify that you visited the mess and spoke to a real person.

## 1\. Evidence to collect during the conversation

Collect these four things\:

| Evidence | What to capture |
|--------|--------|
| Person's details | Name and role (with permission) |
| Interview notes | Three actual statements made by the person |
| Surprising finding | One thing you didn't expect to discover |
| Photographs | Two timestamped photos of the mess/operations |

You do not need to record the person's face or voice. Written notes are acceptable if they accurately document the conversation.

## 2\. How to document the conversation

Create `fieldwork.md` in your repository.

Use this structure\:

**document: **

# Fieldwork Documentation

## 1. Visit Details

- **Location:** College Mess, NIT Jamshedpur
- **Date:** [Actual date]
- **Visit start time:** [Actual time]
- **Visit end time:** [Actual time]
- **Observation duration:** [Actual duration]

## 2. Person Interviewed

- **Name:** [Name, with permission]
- **Role:** [Mess manager / cook / staff member]
- **Interview time:** [Actual time]
- **Permission for interview:** Yes
- **Permission for photographs:** [Yes/No]

## 3. Conversation Record

### Question 1
**Question asked:** How do you decide how much food to prepare every day?

**Person's response:** [Write their actual response]

### Question 2
**Question asked:** What happens when more or fewer students arrive than expected?

**Person's response:** [Write their actual response]

### Question 3
**Question asked:** What happens to leftover food after each meal?

**Person's response:** [Write their actual response]

## 4. Three Important Things I Learned

1. [Actual statement or finding]
2. [Actual statement or finding]
3. [Actual statement or finding]

## 5. One Surprising Observation

[Something unexpected that changed my understanding of the problem.]

## 6. Direct Observations

- [What I observed about food preparation]
- [What I observed about serving]
- [What I observed about leftover management]

## 7. Photographic Evidence

- `screenshots/mess_observation_1.jpg` - [Description and timestamp]
- `screenshots/mess_observation_2.jpg` - [Description and timestamp]

## 8. Data Collection Method

[Explain which records were inspected, how the 20+ entries were collected, and whether quantities were measured, recorded by staff or taken from historical registers.]

## 9. Impact on Initial Project Idea

[Explain whether the conversation confirmed, changed or rejected the initial hypothesis.]

## 3\. How to capture photographic evidence

[![Hostel | International Institute for Population Sciences (IIPS)](https://images.openai.com/static-rsc-4/imMkgWK8kMrHIsExLTmLj_MkKl6gzn1x7BLtRK4EGaY6qL0aMBsx0l0r1i0fyGWMgZfUVTjL9OHRx4CXaeteSuPO3s_RTj6bSlW184W7SWjhl7m7zuDUi_JiBTRImQ4vefl4On-9hdwLXpF2PucszJIin-VMCLwzehIGdCGDA4Q9IYWkJo_yKGbQ5NPoARYC?purpose=fullsize)](https://iipsindia.ac.in/content/hostel-old)

**Photo 1: Mess operations**

Show the actual kitchen or food preparation process.

[![Nourishing Minds and Bodies at SRI VISWA](https://images.openai.com/static-rsc-4/baW-7UUmFG7-pvYagRxTfKQHgJjat7hccxkQgIg0F3YFNk5X0EslKwPpstRDFqujYi51BKgMPdd4cYH3B5n9ukkpp6QlAtWL89hRBEP35EYlQYiqYcpOXhq7gyPO_rhwGxqGxHW9Di5ZfSF5BS-Oxdpd48lwzgwjTbMD--Y9Gc27WogW6QlB733-ULubskU4?purpose=fullsize)](https://sriviswa.com/food-dining-and-health)

**Photo 2: Food serving or records**

Show serving arrangements or the actual register/data collection process.

These are examples of what to photograph, not evidence to submit. Take your own photographs with permission.

## 4\. Should you record the conversation?

My recommendation\:

- Take written notes during the interview.
- Ask permission before recording audio.
- If permitted, record audio as supplementary evidence.
- Never fabricate quotes or recreate a conversation afterward as if it were recorded live.

You can also include a short anonymized interview transcript if the person prefers not to have their identity published.

## 5\. How the evidence will appear in GitHub

```text
mess-demand-analyser/
│
├── research.md
├── fieldwork.md
├── data.csv
│
├── screenshots/
│   ├── mess_observation_1.jpg
│   └── mess_observation_2.jpg
│
└── README.md
```

**One important point\:** The strongest evidence is not simply a photograph of the mess. It is a specific statement from the staff member that changes your initial understanding of the problem, backed by an actual observation or record.

For example, perhaps you initially assume food wastage is caused by inaccurate student counts, but the manager explains that students frequently take unpredictable quantities of particular dishes. That discovery could change the entire tool we build.

## Prompt:
11/17/2026, 6:50:50 PM

this is my transcipt for conversation it will be added as well and with this we will make 
fieldwork.md and readme.md and i am also sharing research.md 
readme.md will contain more information when our tool or model will be ready but it should contain the mentioned infor 1-Day Take-Home Assignment for B.Tech Graduates
The task
In 24 hours, find one small real problem you have seen near you in the last week, build a simple tool that
helps one real person with it, and push it to a public Git repo.
Use AI as much as you like for research and code. Two parts cannot be done by AI: going to the place
and talking to the person (Step 2), and the reflection (Step 4). Those are what we are judging most.
Rules
• The problem must be one you saw yourself, within walking distance of home or college. Not
from a tutorial or the internet.
• The tool must help a real person you can name (a shopkeeper, warden, guard, canteen staff, a
family member) who is not you.
• The tool must run on data you collected yourself: at least 20 real entries (counts, prices,
timings). No downloaded or generated data.
• Rejected automatically: to-do app, weather app, chatbot, portfolio, anything with Kaggle or API
data.
Example of the right size: the chai stall outside college runs out of milk some days and wastes it on
others. You count sales for a day, ask the owner how he decides the order, and write a small script that
suggests tomorrow&#39;s milk quantity.
The four steps
Step Time What you hand in
1. Find and research 1.5 h research.md: the problem in 5 lines, 2 existing solutions and
why they do not fit your person, 2 sources you actually read
with a 3-line note each

2. Go outside 1.5 h fieldwork.md: 20 minutes at the place with 2 timestamped
photos; one conversation with your person (name, role, 3
things they said, 1 thing that surprised you); your raw data in
data.csv with a note on how you collected it
3. Build 4 h Working code that reads data.csv and gives one useful
output; a README with how to run it, the real output, and
what it gets wrong

4. Reflect 1 h reflection.md, written without AI, half a page: what you
got wrong at the start, what you would cut, where AI helped
and where it wasted time. Plus a 3-minute screen recording
of the tool running, linked in the README

Git and submission
• Your first commit, within the first hour, is research.md with your problem and your person. This
locks your choice.
• At least 5 commits spread across the day, with messages in your own words.
• Export the AI chats you used into an ai-chats/ folder. We read them; it is fine, we expect
them.
• Email the repo link within 24 hours. A 10-minute call follows, where we will ask you to open a
row of your data and say where you were when you recorded it, feed the tool a bad row, and
change one thing in the code live.
Scoring (for the panel, remove before sending)
Four parts, 25 points each: research depth, uniqueness of the problem, fieldwork evidence, build and
call. Fieldwork below 10 is a reject regardless of total.
Red flags: README with no place, person or date; data.csv with round numbers and no gaps; a
conversation with nothing surprising in it; one big commit at the end; a reflection that could fit any
project; model-written code with an empty ai-chats/ folder.
Call questions: pick one data row and ask where they were; ask what the person said that changed the
plan; ask them to change a threshold live; ask what the tool should not be trusted for.

[Attachment: Pasted markdown(5).md]

[Attachment: research.md]

## Response:
11/17/2026, 6:50:51 PM · gpt-6

> **Preparing fieldwork files**
>
> I’m organizing the transcript into `fieldwork.md` and `README.md`, while separating confirmed observations from unverified details. I’ll preserve uncertainties about dates, participant attribution, photos, and unrecorded measurements rather than inventing them.
>
> **Prepared fieldwork files**
>
> 
>
> Worked for 38s

# Fieldwork and README - Based on Your Actual Interview

I have reviewed both uploaded files\:

1. Your conversation transcript.
2. Your existing `research.md`\.

We now have enough information to move beyond the initial hypothesis and document the actual problem discovered during fieldwork.

The important change is that **food wastage is not simply a matter of preparing too much food. The mess relies on the cook's experience and multiple contextual factors to estimate preparation quantities, without a dedicated tool for analysing those patterns.**

## 1\. What we actually discovered

These are the findings supported by your interview transcript and research document. fileciteturn0file0 fileciteturn0file1

| Area | Actual finding |
|--------|--------|
| People served | Approximately 400-450 girls across two hostels |
| Planning | Food quantities are estimated by the cook |
| Decision factors | Day, meal, menu, holidays, events and examination schedules |
| Meal demand | Lunch is reported as having the highest demand |
| Food combinations | Egg curry and dry vegetables increase roti requirements; gravy dishes increase rice consumption |
| Leftover tracking | Leftover quantities are not systematically measured |
| Current evidence | Staff photograph leftover food at the end of the day and share it in a group |
| Existing records | Bookkeeper maintains handwritten records; the manager prepares Excel sheets |
| Main difficulty | Estimating appropriate food quantities and minimizing leftovers without causing shortages |
| Desired improvement | A tool that helps estimate future food requirements |

### The most important discovery

The cook already uses an informal decision-making system based on experience.

For example\:

- Egg curry days require more wheat/rotis.
- Sambar and rajma meals require more rice.
- Holidays and examinations affect attendance.
- Lunch and dinner have different demand patterns.

This means our tool should not simply calculate average food consumption.

It should investigate the relationship between **menu, meal, day, events, student attendance and preparation quantity**\.

### One issue we must clarify

Your transcript contains slightly conflicting observations\:

- Lunch is described as the meal with the highest demand.
- Another observation says most food is prepared in the afternoon because of dinner demand.
- Dinner is also described as having more leftovers.

We should clarify this before building our analysis. We must not silently choose one interpretation.

---

## 2\. `fieldwork.md` - Final working draft

This document should communicate what happened during the visit, what the staff explained, and how that changed our project direction.

I have deliberately kept unverified details as placeholders rather than inventing them.

**document: **

# Fieldwork Report: Mess Demand & Food Waste Analyser

## 1. Visit Information

- **Location:** Hostel A Mess, NIT Jamshedpur, Jharkhand
- **Date:** [Enter actual visit date]
- **Observation start time:** [Enter time]
- **Observation end time:** [Enter time]
- **Total observation duration:** [Enter actual duration]
- **Person interviewed:** [Confirm which person participated]
- **People involved in mess operations:** Bhusan Kumar (Mess Manager), Sandeep (Mess Supervisor), cook and bookkeeper.

## 2. Purpose of the Visit

The purpose of this visit was to understand how food preparation quantities are decided in the college mess, how staff handle changing meal demand, and whether food wastage or shortages create operational difficulties.

Our initial hypothesis was that inaccurate food preparation estimates could result in excess food and unnecessary wastage.

We wanted to understand the actual workflow before deciding what kind of tool would be useful.

## 3. Mess Operations Observed and Explained

### 3.1 Scale of Operations

The mess kitchen serves approximately 400-450 female students across two hostels that share the same kitchen.

The number of students eating varies between breakfast, lunch and dinner.

### 3.2 Food Preparation Process

Food quantities are primarily estimated by the cook using experience and knowledge of previous meal patterns.

The estimation considers:

- Day of the week and its menu.
- Meal timing (breakfast, lunch and dinner).
- Holidays and vacations.
- College events.
- Examination schedules.
- The dishes being prepared and their combinations.
- Expected student attendance.

### 3.3 Relationship Between Menu and Food Consumption

An important operational detail discovered during the conversation was that food quantities depend on the dishes served together.

Examples explained by the staff:

- Egg curry and dry vegetables generally require more rotis.
- Sambar and rajma meals generally require more rice.
- Gravy-based dishes influence the quantity of rice required.

This suggests that food preparation cannot be estimated using student count alone.

### 3.4 Leftover Management

The staff attempts to minimize leftover food as much as possible.

However, leftover quantities are not systematically measured.

Instead, staff members take photographs of leftover food after the day's operations and share them in a group containing relevant authorities, mess managers and staff.

The transcript indicates that leftover food is generally discarded.

### 3.5 Food Shortages

Complete food shortages are described as relatively uncommon because the cook estimates quantities using previous experience.

However, individual dishes can sometimes finish before the meal ends, even when other dishes remain available.

## 4. Interview Record

**Interviewee:** [Confirm name]  
**Role:** [Mess Manager / Mess Supervisor / other]  
**Interview date and time:** [Enter actual details]

The following are paraphrased findings from the conversation, not verbatim quotations.

### Three Important Things Learned

**1. Food preparation is based on experience and multiple contextual factors.**

The cook considers the menu, day, meal timing, holidays, events and examinations before deciding preparation quantities.

**2. Food combinations affect preparation requirements.**

The quantity of rice or rotis required depends on the dishes being served together. Different menus require different preparation estimates.

**3. Leftover food is not measured quantitatively.**

Staff photograph leftover food at the end of the day and share the photographs with relevant personnel instead of maintaining item-wise leftover measurements.

## 5. One Surprising Discovery

The most surprising discovery was that food preparation estimates consider much more than the number of students or the meal timing.

The staff also considers college events, holidays, examinations and the relationship between dishes when deciding how much food to prepare.

Despite considering all these factors, the process is still dependent on the cook's personal experience rather than a dedicated analytical tool.

This changed our understanding of the problem. A simple average-based prediction would not adequately represent the actual decision-making process.

## 6. Existing Record-Keeping Process

The mess already maintains operational records.

The process explained during the conversation:

1. The bookkeeper maintains daily handwritten records.
2. These records are shared with the mess manager.
3. The manager prepares Excel sheets to compare financial performance and track food usage.

However, leftover food quantities are not systematically recorded.

We need to inspect these records to determine which variables can actually be used by our tool.

## 7. Problem Identified After Fieldwork

The initial assumption was that the mess primarily needed a food-waste tracking tool.

After the conversation, we identified a more specific operational problem:

**The mess relies on experience-based estimation to decide food preparation quantities. Although staff considers several factors such as menu, meal, day, events and examinations, these factors are not analysed through a dedicated data-driven tool. This can make it difficult to consistently estimate appropriate quantities and minimize leftover food without creating shortages.**

## 8. Proposed Direction

We will investigate a small demand-analysis tool that:

- Reads historical mess records from a CSV file.
- Analyses preparation quantities across meals and days.
- Considers menu-related information where available.
- Identifies recurring preparation patterns.
- Produces a practical estimate or recommendation for upcoming meals.

The final functionality will depend on the actual data available.

We will not claim to measure or predict food waste directly if leftover quantities are not recorded.

## 9. Evidence Collected

| Evidence | File | Status |
|---|---|---|
| Conversation transcript | `evidence/interview-transcript.md` | Transcript provided |
| First timestamped photograph | `evidence/mess_observation_1.jpg` | To add |
| Second timestamped photograph | `evidence/mess_observation_2.jpg` | To add |
| Raw operational records | `data.csv` | To collect |
| Interview details | This document | Name and time to confirm |

## 10. Data Collection Method

The intended data source is the actual handwritten daily mess records and/or the corresponding Excel sheets maintained by the mess staff.

We will request permission to inspect the records and manually extract at least 20 genuine entries.

For every entry, we will preserve the original recorded values and document the meaning and source of each field.

No generated, downloaded or fabricated operational records will be used.

## 11. Pending Validation

Before implementation, we still need to:

- Confirm the exact person interviewed and their role.
- Record the actual visit date, times and observation duration.
- Add two timestamped photographs.
- Inspect the handwritten and Excel records.
- Collect at least 20 genuine entries.
- Clarify the differences between lunch and dinner demand observations.
- Determine whether the available records support meal-wise or item-wise analysis.

---

## 3\. `README.md` - Initial project documentation

The README should be more comprehensive than the research document.

It should tell an evaluator\:

1. What real problem we discovered.
2. Who experiences it.
3. What we learned through fieldwork.
4. What we intend to build.
5. What actual data supports it.
6. How to run the tool.
7. What the tool produces and where it may fail.

For now, sections related to implementation will remain pending. We will complete them after the tool works.

**document: **

# Mess Demand & Food Waste Analyser

A small data-driven tool to help college mess staff understand meal preparation patterns and make better food quantity estimates using actual historical mess records.

## 1. Project Overview

College mess kitchens prepare food for hundreds of students across multiple meals every day.

The quantity of food required changes depending on several factors, including the day, meal timing, menu, holidays, college events and examination schedules.

At Hostel A Mess, NIT Jamshedpur, food preparation quantities are primarily estimated by the cook using experience and knowledge of previous meal patterns.

Although staff considers these factors, there is no dedicated analytical tool to study the historical patterns and support food preparation decisions.

This project aims to explore whether a simple data-driven tool can help improve this process.

## 2. The Real-World Problem

**Location:** Hostel A Mess, NIT Jamshedpur, Jharkhand, India.

**People involved:**
- Bhusan Kumar - Mess Manager.
- Sandeep - Mess Supervisor.
- Cook and bookkeeper involved in daily operations.

**Operational context:**

- Approximately 400-450 female students are served across two hostels.
- Lunch, dinner and breakfast have different demand patterns.
- Preparation quantities depend on the menu and dishes served together.
- Holidays, events and examination schedules influence expected attendance.
- Leftover quantities are not systematically measured.
- Food preparation estimates depend primarily on staff experience.

The problem identified through fieldwork is the lack of a dedicated data-driven approach to analyse historical preparation patterns and support quantity estimation.

## 3. Field Research

The project began with a visit to the college mess and a conversation with the staff responsible for its operations.

Important findings:

1. Food preparation is based on experience and multiple contextual factors.
2. Different food combinations affect the quantities of rice and rotis required.
3. Leftover quantities are not systematically recorded; photographs are shared with relevant staff and management.
4. The bookkeeper maintains handwritten records, which are subsequently used by the mess manager to prepare Excel sheets.
5. The staff expressed interest in having assistance with estimating future food requirements.

**Surprising discovery:**

Food preparation decisions consider not only student numbers and meal timing but also examination schedules, holidays, college events and the dishes served together.

See [Fieldwork Documentation](fieldwork.md) and [Interview Transcript](evidence/interview-transcript.md).

## 4. Proposed Solution

Mess Demand & Food Waste Analyser will be a lightweight analytical tool designed around the existing mess workflow.

Its intended responsibilities are:

- Read actual historical records from `data.csv`.
- Analyse food preparation patterns across different meals and days.
- Identify recurring patterns in food preparation.
- Consider menu and contextual factors wherever the collected data supports them.
- Generate a useful preparation recommendation for upcoming meals, if sufficient historical data is available.

The implementation will prioritize simplicity so that staff can understand and use its output without needing technical knowledge.

## 5. Data Source

The project will use actual operational records collected with permission from the college mess.

**Expected sources:**
- Handwritten daily records maintained by the bookkeeper.
- Excel sheets maintained by the mess manager.

**Minimum requirement:** 20 genuine data entries.

No Kaggle datasets, generated records, downloaded datasets or external APIs will be used.

The final CSV structure will be documented after inspecting the available records.

## 6. Project Architecture

The planned workflow is:

```text
Actual Mess Records
        |
        v
    data.csv
        |
        v
 Data Loading & Validation
        |
        v
  Data Analysis
        |
        v
 Demand Pattern Analysis
        |
        v
 Preparation Recommendation
        |
        v
  Useful Output for Staff
```

The implementation will remain small and focused on solving the identified operational problem.

## 7. Technology Stack

To be finalized based on the implementation.

## 8. Project Structure

```text
mess-demand-analyser/
│
├── research.md
├── fieldwork.md
├── data.csv
├── reflection.md
├── README.md
│
├── evidence/
│   ├── interview-transcript.md
│   ├── mess_observation_1.jpg
│   └── mess_observation_2.jpg
│
├── src/
│
├── screenshots/
│
└── ai-chats/
```

## 9. How to Run

Implementation pending.

Run instructions, dependencies and setup commands will be added after development.

## 10. Actual Output

To be added after running the completed tool against the collected operational data.

The README will include a genuine example of the output generated from the actual CSV records.

## 11. Limitations

Known limitations based on field research:

- Leftover quantities are not systematically measured, so direct quantitative food-waste analysis may not be possible.
- Historical records may not contain all the factors used by the cook.
- Unexpected events and sudden changes in attendance may affect estimates.
- Food preferences and individual consumption patterns may vary.
- Recommendations should support staff decisions rather than replace their experience.

Further limitations will be documented after implementation and testing.

## 12. Demonstration

A three-minute screen recording demonstrating the tool with actual data will be linked here after development.

**Demo:** Pending.

## 13. Project Documentation

- [Research](research.md)
- [Fieldwork](fieldwork.md)
- [Interview Transcript](evidence/interview-transcript.md)
- [Raw Data](data.csv)
- [Reflection](reflection.md) - To be written independently.

## 14. Assignment Context

This project was developed as part of a one-day take-home assignment for B.Tech graduates.

The assignment emphasizes identifying a real local problem, interacting with an actual person affected by it, collecting original data, building a useful tool and reflecting on the development process.

The project uses AI assistance for research and development while keeping fieldwork and personal reflection grounded in the candidate's own work.

---

## 4\. Important corrections before committing

There are five things we need to resolve.

| Item | Current status | Required action |
|--------|--------|--------|
| Interviewee identity | Two names in research.md, but transcript doesn't attribute answers | Confirm who answered |
| Visit date/time | Not present in transcript | Add actual details |
| Two photographs | Not uploaded | Add original timestamped photos |
| 20+ data entries | Not collected yet | Obtain actual records |
| Lunch vs dinner demand | Some conflicting observations | Clarify with staff |

**One important project decision\:** We should not promise a food-waste prediction model yet. Since leftovers aren't measured, our strongest initial direction is historical meal-demand and preparation analysis. We can add quantitative waste analysis only if reliable leftover data becomes available.

## 5\. Recommended repository structure

I recommend keeping the original interview transcript separately from the fieldwork report.

```text
mess-demand-analyser/
│
├── research.md
├── fieldwork.md
├── README.md
├── data.csv
├── reflection.md
│
├── evidence/
│   ├── interview-transcript.md
│   ├── mess_observation_1.jpg
│   └── mess_observation_2.jpg
│
├── src/
├── screenshots/
└── ai-chats/
```

## 6\. Your next actions

**Fieldwork completion checklist**

/ completed %

**Do not make the next implementation commit yet.** First, let's establish the actual data available from the bookkeeper.

The next thing I want to examine is the handwritten register or Excel sheet. That will determine our CSV structure, what analysis is possible, and ultimately what tool we should build.

## Prompt:
11/18/2026, 1:16:52 AM

we have now all the aspects data csv and i will be sharing the vacations during the time period and mess menu and now lets work on our tool

## Response:
11/18/2026, 1:16:53 AM · gpt-6

> **Searched conversations and library for CSV files**
>
> 
>
> Worked for 12s

# Phase 3 — Build: Mess Demand &amp; Food Waste Analyser

We are moving from field research to implementation.

Based on your interview, I recommend that we build a **data-driven mess food preparation recommendation tool**, rather than a generic food-waste dashboard.

The key insight from your fieldwork is that the cook already considers several factors when estimating quantities\:

- Day of the week.
- Meal (breakfast, lunch, dinner).
- Menu and food combinations.
- Vacations and holidays.
- College events and examination schedules.
- Historical preparation experience.

Our tool should use these factors to support the cook's existing decision-making process.

## 1\. What exactly are we building?

# Mess Demand Analyser

(Proposed MVP)

**Input**

Historical mess records + menu + vacation calendar.

**Historical Data Analysis**

Meal, day, menu, quantities and attendance

**Demand Pattern Analysis**

Identify similar days and meal patterns

**Preparation Recommendation**

**Output**

- Estimated preparation quantity for each meal/item.
- Historical comparison with similar meals.
- Factors influencing the recommendation.
- Warnings when data is insufficient.

## 2\. How we will approach development

We will follow this sequence. No model training or UI development before understanding the data.

| Phase | Work | Deliverable |
|--------|--------|--------|
| 1 | Inspect CSV | Understand available columns |
| 2 | Inspect menu and vacation calendar | Build contextual features |
| 3 | Data cleaning | Reliable dataset |
| 4 | Exploratory analysis | Demand patterns |
| 5 | Recommendation logic | Preparation estimates |
| 6 | Validation | Compare predictions against historical records |
| 7 | Interface | Usable tool for mess staff |
| 8 | Testing | Real output and failure cases |

## 3\. Recommended technology

For this assignment, I recommend Python because the core problem is data analysis and numerical recommendations.

| Component | Technology |
|--------|--------|
| Data processing | Python, Pandas |
| Analysis | NumPy |
| Visualization | Matplotlib |
| Recommendation logic | Statistical / rule-based approach initially |
| Interface | Streamlit |
| Data storage | CSV |

We should start with an explainable statistical baseline, not jump directly to machine learning. If the data supports a more advanced model, we can evaluate it later.

## 4\. What I need from you now

I searched the available conversation files but haven't found the actual operational CSV, vacation calendar or mess menu yet.

Please share these three things\:

1. **`data.csv`** — the actual records collected from the mess.
2. **Vacation and holiday details** — dates covering the same period as the CSV.
3. **Mess menu** — the actual menu for the corresponding dates.

**Our first development milestone**

(Data understanding)

Once you upload the files, we will\:

- Inspect every column and its meaning.
- Check missing values and inconsistent entries.
- Understand quantities and their units.
- Match dates with the menu and vacation calendar.
- Identify which variables can actually influence preparation estimates.

**Deliverable\:** A documented dataset and a finalized recommendation approach.

**One rule\:** We will not fabricate missing values, assume attendance figures, or claim to predict food waste when actual leftover quantities aren't measured.

Let's first understand your actual data. Then we will build the tool around what the mess really records and what the cook actually needs.

## Prompt:
11/18/2026, 1:31:38 AM

![image(20261117-194742).png](https://sdmntprcentralindia.oaiusercontent.com/files/00000000-2c14-8208-857a-937d19b28b29/raw?se=2026-11-17T22%3A30%3A08Z&sp=r&sv=2026-06-06&sr=b&scid=79aa5a99-676e-42db-836a-842198d3413b&skoid=3cb6de21-012a-49c9-9402-a1ebf8d0bd06&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2026-11-17T03%3A40%3A10Z&ske=2026-11-18T03%3A40%3A10Z&sks=b&skv=2026-06-06&sig=T6cD8SPBKjbYx7%2BxM4YjMMvO/bcrKLpU2YBLwI3yD7M%3D)

![image(20261117-195436).png](https://sdmntprcentralindia.oaiusercontent.com/files/00000000-8a6c-8208-908f-969560265396/raw?se=2026-11-17T22%3A30%3A08Z&sp=r&sv=2026-06-06&sr=b&scid=dbe93f88-e60b-46ae-9cbd-c0fd6b5fc0ae&skoid=3cb6de21-012a-49c9-9402-a1ebf8d0bd06&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2026-11-17T03%3A51%3A27Z&ske=2026-11-18T03%3A51%3A27Z&sks=b&skv=2026-06-06&sig=B3yy0pBREzs0aveVb%2BR8W4HjVONdMdA0TC7YgeXFUEE%3D)

[Attachment: data(2).csv]

mess menu
acadmic calendar among that time period and data so now we are ready to wrok on our tool

## Response:
11/18/2026, 1:31:39 AM · gpt-6

> **Inspecting dataset schema and contents**
>
>
> ****
>
> 
>
> **Assessing the dataset**
>
> I’m checking the CSV’s structure and spotting repeated consumption values, missing meal-level details, and possible calendar inconsistencies. I’ll avoid assuming patterns are genuine and separate reliable planning inputs from questionable records.
>
> **Assessed the dataset**
>
> 
>
> **Calculating weekday and per-student food usage patterns**
>
>
> **Clarifying data reliability**
>
> I’m seeing repeated weekday attendance, zero values for some ingredients, mixed kilograms and litres in one total, and no leftovers or meal-level fields. I’m treating this as a preparation-planning baseline, not yet a food-waste model.
>
> **Clarified data reliability**
>
> 
>
> **Inspected menu data and calculated weekday food usage patterns**
>
> 
>
> Worked for 48s

# Phase 3 - Data audit and problem definition

I have inspected all three uploads\:

1. `data(2).csv` - mess operational records.
2. Revised mess menu photograph.
3. Academic calendar photograph.

We can begin implementation. However, the first step is to understand exactly what our dataset can support.

## 1\. What is in our CSV?

(23 records loaded)

# 23

Daily records

# 14

Columns

# 23

Distinct dates

# 0

Missing cells

---

**Date coverage**

25 October 2026 - 16 November 2026

### Available variables

| Category | Columns |
|--------|--------|
| Date information | `date`, `day` |
| Demand | `students_served_est` |
| Grain usage | `rice_used_kg`, `wheat_flour_used_kg`, `breakfast_grains_used_kg` |
| Other ingredients | `dal_pulses_used_kg`, `vegetables_used_kg`, `potatoes_used_kg` |
| Dairy and bread | `milk_used_litres`, `bread_used_kg` |
| Count-based items | `eggs_used_pieces`, `bananas_used_pieces` |
| Combined quantity | `total_food_mass_kg_approx` |

We have enough variables to begin studying daily ingredient consumption relative to student demand.

## 2\. What patterns can we investigate?

The first useful analysis is ingredient consumption per student.

For example\:

$$
\text{Rice per student} =
\frac{\text{Rice used (kg)}}{\text{Students served}}
$$

We can calculate this for every day and investigate whether the quantity changes with\:

- Weekday.
- Number of students.
- Vacation periods.
- College events.
- Menu combinations.

This is more meaningful than simply comparing total rice consumption across days.

## 3\. Academic calendar: important context

I extracted the following events from your uploaded calendar\:

| Date | Event |
|--------|--------|
| 17-25 Oct | Mid-semester break |
| 20 Oct | Dussehra holiday |
| 29 Oct | Mid-semester marks activity |
| 30 Oct - 1 Nov | Annual Sports Meet (URJA) |
| 8 Nov | Diwali holiday |

These dates overlap with our CSV coverage.

We can create contextual features\:

```python
is_vacation
is_holiday
is_sports_event
is_exam_period
```

We must distinguish actual holidays, student vacations and college events rather than treating all of them as the same category.

## 4\. Data quality issues we need to address

I found four important things.

(Important) **No leftover measurements**

We cannot calculate actual food waste or waste percentage from this CSV. It records ingredient usage, not leftovers.

---

(Important) **Daily aggregation only**

We don't have separate breakfast, lunch and dinner records. We cannot directly predict meal-wise quantities using this CSV.

---

(Check) **Combined food mass**

`total_food_mass_kg_approx` adds kilograms and litres together. This is not a physically valid total mass measurement. We should not use it as a prediction target.

---

(Check) **Repeated patterns**

Student counts repeat exactly for several weekdays, and egg and banana counts have repeated values and zeros. These may reflect genuine schedules or recording conventions, but we should verify their provenance.

There are no missing cells, and all recorded weekday labels match their calendar dates.

## 5\. What should our first version actually do?

I recommend three core features.

**Feature 1 - Historical consumption analysis**

[![Coconut — Food Waste Reduction & ESG Solution](https://images.openai.com/static-rsc-4/cxHR98XwzM-zm5lbKhpDU0Q5KDjrEo2HycvAfJP4SCKpPJtdMWh9CIyvkcIlzjFpv7IlIOmIBxaLRwvW9VEY5hfhwAlyD5k6DOck4U74oa9NCL-vLVmPlvcxebDWZB2H7cllFJhLf_TJn43peujZGLreoDm614UfmXUhpXxkLFsuvEeASPI-7ZyTBKGtyTbl?purpose=fullsize)](https://www.nuvilab.com/en/coconut)

- Ingredient usage per student.
- Daily and weekday comparisons.
- Consumption trends.
  
  ---
  
  **Feature 2 - Context-aware demand analysis**

[![Image](https://images.openai.com/static-rsc-4/Zro3f3ZRJcjNsEflICYxcrUVG4n0K7gZ_fxsz6UVSW62Mfj08ounfwCOsVhE1dCtqUPcII9YVFXPaIdfAFJAiFlvEwUfBL0IFUmI5-NwoPcGSdRnMKVeSKbEIj_XFIuETuiYdAbrhyfb20vKNL7vKakW-TDrUQNdoBchb27ne9Mok8KKoAHZH2GGasASrdql?purpose=fullsize)](https://public.tableau.com/app/profile/lisa.hitch/viz/CorporateAccessCalendar/Dashboard)

- Normal days versus vacation periods.
- Event and holiday comparisons.
- Menu-based consumption patterns.
  
  ---
  
  **Feature 3 - Preparation recommendation**

[![Voyance | Devpost](https://images.openai.com/static-rsc-4/CcxcjILrBKBYTPELag4My96Chj43Kh20zzTMgieKer96AaqydJHTxNBKmBMf9L5tP0XzI3qU9FC4hNtUoRahHrbHvaeHxSZzrxkgXPsUN6ntDLRB9p4OB1GYbXE-dz7ny8yG0SCj5mUx2nVn7EWxEQQANPlcdmUtkH7-0O9KgwoRX5JkynUSNqIF5gpbMDHS?purpose=fullsize)](https://devpost.com/software/voyance)

- Recommended ingredient quantities.
- Historical comparison.
- Explanation of how the estimate was calculated.

### Proposed recommendation logic

Our initial baseline can be\:

$$
\text{Recommended Quantity}
=
\text{Historical Quantity per Student}
\times
\text{Expected Students}
$$

We can improve this by comparing similar weekdays and menu combinations.

For example, if the cook expects 420 students tomorrow, the tool can use historical ingredient consumption per student from comparable days to estimate the required quantities.

This is a baseline, not yet a validated prediction model.

## 6\. Technology and project structure

I suggest Python + Pandas + Streamlit.

```text
mess-demand-analyser/
│
├── data/
│   ├── raw/
│   │   └── data.csv
│   └── processed/
│
├── config/
│   ├── academic_calendar.csv
│   └── mess_menu.csv
│
├── src/
│   ├── data_loader.py
│   ├── preprocessing.py
│   ├── feature_engineering.py
│   ├── analysis.py
│   └── recommendation.py
│
├── app.py
├── requirements.txt
├── research.md
├── fieldwork.md
├── README.md
└── reflection.md
```

We will keep the implementation simple and modular.

---

## 7\. Before writing code: one confirmation

I need to establish the reliability of our input data.

**Is `data(2).csv` transcribed from the actual bookkeeper's handwritten records or manager's Excel sheets, or have the quantities been reconstructed/estimated from your observations?**

This distinction determines whether we can honestly evaluate historical predictions against actual recorded consumption.

Also, I noticed the printed menu heading says September 2025, while the handwritten revision appears dated 27/09/26. We should confirm that this revised menu was applicable to the October-November 2026 data period.

Once the data provenance is established, our first coding task will be `data_loader.py` and `preprocessing.py`\. We will inspect the data programmatically before building the dashboard.

## Prompt:
11/18/2026, 1:33:59 AM

**Is&#x20;**`data(2).csv`**&#x20;transcribed from the actual bookkeeper's handwritten records or manager's Excel sheets, or have the quantities been reconstructed/estimated from your observations?** &#x20;
yes and we have to make sure to include other factors liek academic vacations and mess menu so now lets start

## Response:
11/18/2026, 1:34:00 AM · gpt-6

> **Parsing CSV Dates and Summarizing Values**
>
>
> **Rotating Menu Image For OCR**
>
>
> **Building the scaffold**
>
> I’m preparing a starter project with CSV loaders, configuration, feature-building utilities, and a weekday-based menu schema. I’m avoiding uncertain handwritten transcriptions and leaving calendar and menu records ready for confirmation.
>
> **Planning the first coding step**
>
> I’m starting with a small, auditable project: loaders, schema checks, date-based event expansion, and menu feature aggregation. I’ll keep uncertain menu details as placeholders rather than inventing values.
>
> **Built scaffold and planned initial coding step**
>
> 
>
> **Building Mess Demand Dashboard Project**
>
>
> **Analyzed images, parsed CSV data, rotated menu OCR, and built demand dashboard**
>
> 
>
> Worked for 1m 22s

We will now start implementation using the actual bookkeeper/manager records as our data source.

The project will account for three important inputs\:

1. **Historical mess data\:** Actual ingredient quantities and student counts.
2. **Academic calendar\:** Vacations, holidays, examinations and college events.
3. **Mess menu\:** Dishes served on each date and their influence on ingredient requirements.

Our objective is to reproduce part of the cook's existing decision-making process in a simple, explainable tool.

We will build this incrementally. First, data ingestion and validation; then contextual analysis; finally, preparation recommendations.

# Step 1 - Set up the project and inspect the data

## 2\. Starter project created

**mess-demand-analyser-starter.zip**

Python project · CSV · Calendar · Streamlit

[Download starter project](sandbox:/mnt/data/mess-demand-analyser-starter.zip)

The starter includes\:

| File | Responsibility |
|--------|--------|
| `data_loader.py` | Load and validate actual records |
| `preprocessing.py` | Add weekday, calendar and per-student features |
| `academic_calendar.csv` | Academic events and vacations |
| `mess_menu.csv` | Menu data template |
| `app.py` | Initial Streamlit dashboard |
| `requirements.txt` | Dependencies |

## 3\. Initial validation results

(Validation executed successfully)

| Check | Result |
|--------|--------|
| Records | 23 |
| Unique dates | 23 |
| Missing values | 0 |
| Duplicate dates | 0 |
| Incorrect weekday labels | 0 |
| Negative quantities | 0 |
| Zero quantity cells | 10 |

The 10 zero values have been preserved. We need to determine whether they mean no consumption, a menu-related absence, or a recording convention.

### Academic calendar matching

Matches within the available dataset, 25 October-16 November 2026.

| Date | Context | Students |
|--------|--------|--------|
| 25 Oct | Last day of mid-semester break | 372 |
| 29 Oct | Mid-semester marks activity | 438 |
| 30 Oct | Sports Meet | 408 |
| 31 Oct | Sports Meet | 396 |
| 1 Nov | Sports Meet | 372 |
| 8 Nov | Diwali holiday | 300 |

Notice that the academic vacation from 17-25 October overlaps our dataset only on 25 October. Dussehra on 20 October falls outside the dataset.

We must not assume that the effects of an entire vacation period can be learned from one overlapping record.

## 4\. Run the project

After downloading and extracting the ZIP, open the folder in VS Code.

```bash
python -m venv .venv
```

Windows\:

```bash
.venv\Scripts\activate
```

Install dependencies\:

```bash
pip install -r requirements.txt
```

Start the application\:

```bash
streamlit run app.py
```

You should see the initial dashboard with student counts, ingredient usage and academic-calendar matches.

---

## 5\. What we will implement next

Our next task is to integrate the mess menu properly.

The menu photograph contains a weekly schedule with separate breakfast, lunch, snacks and dinner sections. It also has handwritten revisions dated 27/09/26.

We should transcribe the revised menu rather than assume the printed September 2025 heading represents the applicable menu period.

**Next development milestone**

(Data integration)

1. Transcribe the Monday-Sunday menu.
2. Map dishes to rice, roti, eggs and other ingredients.
3. Match menu days with historical CSV dates.
4. Combine menu features with academic-calendar features.
5. Analyse consumption per student across comparable days.

**One clarification before we proceed\:**

Is the revised menu dated 27 September 2026 the menu that was followed throughout 25 October-16 November 2026?

This will determine whether we can confidently join the weekly menu to all 23 historical records.

## Prompt:
11/18/2026, 1:46:07 AM

yes we will use this menu only

## Response:
11/18/2026, 1:46:08 AM · gpt-6

> **Inspecting Container Files for Menu Integration**
>
>
> ****
>
> 
>
> **Planning menu integration**
>
> I’m treating the confirmed menu as structured data and preserving uncertain text rather than guessing. I’m planning daily menu summaries and explicit signals—such as rice, roti, egg, and gravy—to support the MVP’s usage recommendations.
>
> **Planned menu integration**
>
> 
>
> **Creating mess menu demand analysis configuration**
>
>
> **Implemented and tested the mess menu demand analysis application package**
>
> 
>
> Worked for 2m 44s

## 4\. Menu integration completed

(28 menu entries integrated)

I have created `config/mess_menu.csv` containing\:

- Monday–Sunday.
- Breakfast, lunch, snacks and dinner.
- Dish names transcribed from the revised menu.
- Notes identifying unclear handwritten corrections.

The menu is matched to all 23 historical records using weekdays.

**Important\:** Some handwritten menu corrections are difficult to read in the photograph. Those entries are flagged with lower transcription confidence and should be checked against the original menu.

## 5\. Current project status

**Historical CSV loading** (Complete)

**Academic calendar integration** (Complete)

**Weekly menu integration** (Complete)

**Per-student consumption** (Complete)

**Preparation baseline** (Implemented)

**Automated tests** (4 passed)

**Streamlit interface** (Needs local testing)

**Updated project ZIP**
[Download mess-demand-analyser-updated.zip](sandbox:/mnt/data/mess-demand-analyser-updated.zip)

The automated data-processing tests passed. Streamlit itself still needs to be installed and tested in your local environment.

## 6\. What we do next

Before introducing machine learning, I want us to investigate three questions\:

1. Does rice consumption increase on days with gravy-based dishes?
2. Does wheat consumption increase on egg curry or dry vegetable days?
3. How do student counts and ingredient consumption change during vacations and college events?

These are directly connected to what the cook told you during fieldwork.

**Our next milestone is exploratory data analysis (EDA).** We will produce actual graphs, comparisons and findings from the 23 records, then decide which factors deserve to influence the recommendation algorithm.

We should not introduce arbitrary menu-based adjustment percentages. The data must support them.

## Prompt:
11/18/2026, 2:04:24 AM

we will be changing the file ourselves now just tell me what we have to do according to the achanges

1. Does rice consumption increase on days with gravy-based dishes? yes&#x20;
2. Does wheat consumption increase on egg curry or dry vegetable days? yes
3. How do student counts and ingredient consumption change during vacations and college events? ususally decreases as people goes to home

## Response:
11/18/2026, 2:04:28 AM · gpt-6

Based on these findings, we need to modify our project from a basic consumption analyser into a **context-aware food preparation recommendation system**\.

We now have three domain rules from your fieldwork\:

1. Gravy-based dishes increase rice requirements.
2. Egg curry and dry vegetables increase wheat/roti requirements.
3. Vacations and college events generally reduce student attendance because students go home.

These should influence our data processing and recommendation logic.

# 1\. Changes required in the project

## Change 1 - Update `mess_menu.csv`

Currently, we have menu names mapped to weekdays. We need to add ingredient-related categories.

Add these columns\:

| Column | Purpose |
|--------|--------|
| `day` | Monday-Sunday |
| `meal` | Breakfast, lunch, snacks, dinner |
| `dishes` | Actual dishes |
| `has_gravy` | Whether gravy-based dishes are served |
| `has_egg_curry` | Whether egg curry is served |
| `has_dry_vegetables` | Whether dry vegetables are served |
| `menu_category` | Optional category for analysis |

Example\:

```csv
day,meal,dishes,has_gravy,has_egg_curry,has_dry_vegetables
Monday,Lunch,Rajma Rice,1,0,0
Tuesday,Lunch,Egg Curry Roti,0,1,0
Wednesday,Lunch,Dry Vegetables Roti,0,0,1
```

These are illustrative rows. Use your actual menu.

**Why?**

We want the system to understand the relationship between dishes and ingredient requirements instead of treating every Monday or Tuesday as identical.

## Change 2 - Update `academic_calendar.csv`

We need to distinguish different types of academic events.

Recommended columns\:

```csv
date,event_name,event_type,is_vacation,is_holiday
```

Possible event types\:

- Vacation
- Examination
- College event
- Holiday
- Normal academic day

For example\:

| Event | Classification |
|--------|--------|
| Mid-semester break | Vacation |
| Dussehra | Holiday |
| URJA | College event |
| Diwali | Holiday |

Do not combine vacations, examinations and events into one generic category. Their effects may differ.

## Change 3 - Update `preprocessing.py`

This is where we combine all three datasets.

Our final processed dataframe should contain\:

| Feature | Source |
|--------|--------|
| Date | Mess CSV |
| Day | Mess CSV |
| Students served | Mess CSV |
| Rice used | Mess CSV |
| Wheat used | Mess CSV |
| Rice per student | Calculated |
| Wheat per student | Calculated |
| Has gravy | Menu |
| Has egg curry | Menu |
| Has dry vegetables | Menu |
| Is vacation | Academic calendar |
| Is holiday | Academic calendar |
| Is college event | Academic calendar |

Add these calculations\:

```python
df["rice_per_student"] = (
    df["rice_used_kg"] / df["students_served_est"]
)

df["wheat_per_student"] = (
    df["wheat_flour_used_kg"] / df["students_served_est"]
)
```

Handle zero student counts before division.

# 2\. Changes to the recommendation algorithm

This is the most important modification.

We should not use a simple overall average.

Instead, our recommendation should consider the following\:

**Rice recommendation**

Historical rice consumption per student

Gravy-based menu information

Expected student attendance

**Estimated rice quantity**

---

**Wheat recommendation**

Historical wheat consumption per student

Egg curry / dry vegetable information

Expected student attendance

**Estimated wheat quantity**

---

**Attendance adjustment**

Normal expected attendance

Vacation / holiday / event context

**Expected students**

A useful baseline\:

$$
Q_{\text{rice}} =
R_{\text{per student}} \times N_{\text{expected}}
$$

$$
Q_{\text{wheat}} =
W_{\text{per student}} \times N_{\text{expected}}
$$

Here, historical consumption per student should be calculated using comparable days and menus.

For the first version, use historical median consumption per student rather than inventing adjustment percentages.

# 3\. Changes to the Python files

Here is exactly what each file should now do.

| File | Changes |
|--------|--------|
| `data_loader.py` | Load all three CSV files and validate their schemas |
| `preprocessing.py` | Merge dates, menu features and academic events |
| `feature_engineering.py` | Calculate ingredient consumption per student and menu indicators |
| `analysis.py` | Compare consumption across menu categories and academic periods |
| `recommendation.py` | Estimate preparation quantities using comparable historical records |
| `app.py` | Display historical patterns and recommendations |

# 4\. What the dashboard should display

Our interface should have four sections.

**1\. Mess overview**

- Total students served.
- Daily ingredient consumption.
- Historical consumption trends.
  
  ---
  
  **2\. Menu impact analysis**
- Rice consumption on gravy days versus other days.
- Wheat consumption on egg curry days versus other days.
- Wheat consumption on dry vegetable days versus other days.
  
  ---
  
  **3\. Academic calendar impact**
- Normal days versus vacation days.
- Holiday attendance patterns.
- College event attendance patterns.
  
  ---
  
  **4\. Preparation recommendation**

User selects a future date and expected student count.

The tool displays\:

- Expected rice quantity.
- Expected wheat quantity.
- Other ingredient estimates where sufficient historical evidence exists.
- Historical records used for the recommendation.
- Confidence or insufficient-data warnings.

# 5\. Important limitations

There are three things we must not overlook\:

1. Our CSV contains daily aggregated consumption, whereas the menu contains individual meals. We cannot claim meal-specific predictions from daily totals.
2. We have only 23 historical records. We should use explainable statistical rules, not train a complex ML model.
3. We do not have measured leftover quantities. Therefore, we can recommend preparation quantities, but cannot claim that we have calculated actual food waste reduction.

---

## 6\. Your implementation order

Follow this exact order. Don't jump between files.

**Development checklist** /

**Start with `mess_menu.csv`\.** Once you have added the ingredient categories, we can move to `academic_calendar.csv` and then implement the data-processing pipeline.

The central idea is to make the tool understand the same factors the cook considers mentally, while using historical records to quantify their impact.

## Prompt:
11/18/2026, 2:10:30 AM

day,meal,menu_items,menu_source_note,transcription_confidence\
Monday,Breakfast,"Bread; butter; jam; milk; tea; banana/boiled egg; aloo paratha; tomato chutney",Revised weekly menu photograph dated 27/09/2026; printed item text transcribed where legible,medium\
Monday,Lunch,"Rice; roti; salad; moong dal; aloo parwal; mixed vegetable curry; achar",Revised weekly menu photograph dated 27/09/2026; some lower-row text is faint,medium\
Monday,Snacks,"Bread pakoda; tea",Revised weekly menu photograph dated 27/09/2026,high\
Monday,Dinner,"Roti; rice; chana dal; soya aloo; gulab jamun",Revised weekly menu photograph dated 27/09/2026,medium\
Tuesday,Breakfast,"Bread; butter; jam; milk; tea; banana/omelette; aloo poha; coconut chutney",Revised weekly menu photograph dated 27/09/2026; handwritten edits are partly unclear,medium\
Tuesday,Lunch,"Rice; roti; salad; sambar; aloo kundru; dahi vada; achar",Revised weekly menu photograph dated 27/09/2026,medium\
Tuesday,Snacks,"Gol gappa; coffee",Revised weekly menu photograph dated 27/09/2026,high\
Tuesday,Dinner,"Roti; rice; paneer aloo; sevai; masoor dal",Revised weekly menu photograph dated 27/09/2026; one item partly unclear,medium\
Wednesday,Breakfast,"Bread; butter; jam; milk; tea; banana/boiled egg; uttapam; coconut chutney sambar",Revised weekly menu photograph dated 27/09/2026,medium\
Wednesday,Lunch,"Rice; roti; salad; masoor dal; chana dal pakoda; dahi; achar",Revised weekly menu photograph dated 27/09/2026; handwritten correction near dal row,medium\
Wednesday,Snacks,"Noodles; tea",Revised weekly menu photograph dated 27/09/2026,high\
Wednesday,Dinner,"Roti; rice; dal; seasonal vegetable; omelette curry",Revised weekly menu photograph dated 27/09/2026; some dinner text is faint,low\
Thursday,Breakfast,"Bread; butter; jam; milk; tea; banana/boiled egg; idli; sambar; aloo sabzi",Revised weekly menu photograph dated 27/09/2026,medium\
Thursday,Lunch,"Jeera rice; roti; salad; moong dal; kabuli chana masala; aloo fry; achar",Revised weekly menu photograph dated 27/09/2026,medium\
Thursday,Snacks,"Chana chaat; coffee",Revised weekly menu photograph dated 27/09/2026; handwritten correction near snack row,medium\
Thursday,Dinner,"Roti; rice; masoor dal; mixed vegetable; ice cream",Revised weekly menu photograph dated 27/09/2026,medium\
Friday,Breakfast,"Bread; butter; jam; milk; tea; banana/boiled egg; steamed idli/fried idli; sambar; coconut chutney",Revised weekly menu photograph dated 27/09/2026,medium\
Friday,Lunch,"Rice; roti; salad; mixed vegetable; fish curry; masoor dal; achar",Revised weekly menu photograph dated 27/09/2026,medium\
Friday,Snacks,"Pani chat; tea",Revised weekly menu photograph dated 27/09/2026,high\
Friday,Dinner,"Roti; rice; paneer-based curry; dal; ice cream",Revised weekly menu photograph dated 27/09/2026; handwritten item correction is unclear,low\
Saturday,Breakfast,"Bread; butter; jam; milk; tea; banana/boiled egg; chole bhature",Revised weekly menu photograph dated 27/09/2026,medium\
Saturday,Lunch,"Rice; roti; salad; masoor dal; paneer masala; fish fry; mixed vegetable; achar",Revised weekly menu photograph dated 27/09/2026,medium\
Saturday,Snacks,"Samosa; coffee",Revised weekly menu photograph dated 27/09/2026,high\
Saturday,Dinner,"Paratha; chole; aloo matar; dahi",Revised weekly menu photograph dated 27/09/2026; text partly unclear,medium\
Sunday,Breakfast,"Bread; butter; jam; milk; tea; banana/boiled egg; dosa; sambar; onion chutney",Revised weekly menu photograph dated 27/09/2026,medium\
Sunday,Lunch,"Ghee rice; puri; salad; aloo dum; chana masala; achar",Revised weekly menu photograph dated 27/09/2026,medium\
Sunday,Snacks,"No snacks listed / unclear in photograph",Revised weekly menu photograph dated 27/09/2026,low\
Sunday,Dinner,"Puri; roti; baingan choka; mixed dal; aloo matar; suji halwa with dry fruits",Revised weekly menu photograph dated 27/09/2026,medium\
thsi si the mess_menu.csv how to update this
event_name,start_date,end_date,event_type,source_note\
Mid-Semester Break,2026-10-17,2026-10-25,vacation,Academic calendar image supplied by user\
Submission of Class Attendance (2nd Report),2026-10-19,2026-10-19,academic_deadline,Academic calendar image supplied by user\
Dussehra Holiday,2026-10-20,2026-10-20,holiday,Academic calendar image supplied by user\
Showing of Answer Books and Last Date to Enter Mid Semester Marks,2026-10-29,2026-10-29,academic_activity,Academic calendar image supplied by user\
Annual Sports Meet (URJA),2026-10-30,2026-11-01,college_event,Academic calendar image supplied by user\
Diwali Holiday,2026-11-08,2026-11-08,holiday,Academic calendar image supplied by user\
this si the academic_calendar.csv&#x20;
adn&#x20;
from pathlib import Path
import pandas as pd

INGREDIENT_COLUMNS = {
    "rice_used_kg"*:* "rice_kg_per_student"*,*
    "wheat_flour_used_kg"*:* "wheat_flour_kg_per_student"*,*
    "dal_pulses_used_kg"*:* "dal_pulses_kg_per_student"*,*
    "vegetables_used_kg"*:* "vegetables_kg_per_student"*,*
    "potatoes_used_kg"*:* "potatoes_kg_per_student"*,*
    "breakfast_grains_used_kg"*:* "breakfast_grains_kg_per_student"*,*
    "milk_used_litres"*:* "milk_litres_per_student"*,*
    "bread_used_kg"*:* "bread_kg_per_student"*,*
    "eggs_used_pieces"*:* "eggs_pieces_per_student"*,*
    "bananas_used_pieces"*:* "bananas_pieces_per_student"*,*
}

def load_calenda&#x72;*(*&#x70;at&#x68;*:* str | Pat&#x68;*)* *->* p&#x64;*.*&#x44;ataFrame:
    calendar = p&#x64;*.*&#x72;ead_csv(path)
    required = {"event_name"*,* "start_date"*,* "end_date"*,* "event_type"}
    missing = required - set(calenda&#x72;*.*&#x63;olumns)
    if missin&#x67;*:*
        raise ValueError(f"Academic calendar is missing columns: {sorted(missing)}")
    calendar["start_date"] = p&#x64;*.*&#x74;o_datetime(calendar["start_date"]*,* errors="raise")
    calendar["end_date"] = p&#x64;*.*&#x74;o_datetime(calendar["end_date"]*,* errors="raise")
    if (calendar["end_date"] < calendar["start_date"])*.*&#x61;ny()*:*
        raise ValueError("An academic calendar event ends before it starts.")
    return calendar

def add_context_feature&#x73;*(*&#x64;&#x66;*:* p&#x64;*.*&#x44;ataFram&#x65;*,* calenda&#x72;*:* p&#x64;*.*&#x44;ataFram&#x65;*)* *->* p&#x64;*.*&#x44;ataFrame:
    """Attach calendar context; retain multiple events on a date as separate labels."""
    out = d&#x66;*.*&#x63;opy()
    out["weekday"] = out["date"]*.*&#x64;&#x74;*.*&#x64;ay_name()
    out["is_weekend"] = out["date"]*.*&#x64;&#x74;*.*&#x64;ayofweek >= 5
    out["calendar_events"] = ""
    out["is_vacation"] = False
    out["is_holiday"] = False
    out["is_college_event"] = False
    out["is_academic_activity"] = False

    type_to_flag = {
        "vacation"*:* "is_vacation"*,*
        "holiday"*:* "is_holiday"*,*
        "college_event"*:* "is_college_event"*,*
        "academic_activity"*:* "is_academic_activity"*,*
    }
    for \_*,* event in calenda&#x72;*.*&#x69;terrows()*:*
        mask = out["date"]*.*&#x62;etween(event["start_date"]*,* event["end_date"])
        ou&#x74;*.*&#x6C;oc[mas&#x6B;*,* "calendar_events"] = ou&#x74;*.*&#x6C;oc[mas&#x6B;*,* "calendar_events"]*.*&#x61;pply(
            lambda existing: "; "*.*&#x6A;oin(x for x in [existin&#x67;*,* event["event_name"]] if x)
        )
        flag = type_to_fla&#x67;*.*&#x67;et(event["event_type"])
        if fla&#x67;*:*
            ou&#x74;*.*&#x6C;oc[mas&#x6B;*,* flag] = True
    return out

def add_per_student_feature&#x73;*(*&#x64;&#x66;*:* p&#x64;*.*&#x44;ataFram&#x65;*)* *->* p&#x64;*.*&#x44;ataFrame:
    out = d&#x66;*.*&#x63;opy()
    denominator = out["students_served_est"]*.*&#x77;here(out["students_served_est"] > 0)
    for sourc&#x65;*,* target in INGREDIENT_COLUMN&#x53;*.*&#x69;tems()*:*
        out[target] = out[source] / denominator
    *# Do not use total_food_mass_kg_approx: it combines kg, litres and item counts.*
    return out

def prepare_analysis_dat&#x61;*(*
    d&#x66;*:* p&#x64;*.*&#x44;ataFram&#x65;*,* calenda&#x72;*:* p&#x64;*.*&#x44;ataFram&#x65;*,* men&#x75;*:* p&#x64;*.*&#x44;ataFrame | None = None
*)* *->* p&#x64;*.*&#x44;ataFrame:
    out = add_context_features(d&#x66;*,* calendar)
    if menu is not Non&#x65;*:*
        out = attach_menu_context(ou&#x74;*,* menu)
    return add_per_student_features(out)

df["rice_per_student"] = (
    df["rice_used_kg"] / df["students_served_est"]
)

df["wheat_per_student"] = (
    df["wheat_flour_used_kg"] / df["students_served_est"]
)
preprocessing.py

## Response:
11/18/2026, 2:10:31 AM · gpt-6

> **Updating menu features**
>
> I’m treating your menu file as a feature source and your consumption file as the daily target. I’d clean the CSV first, add explicit dish-category flags, then merge daily menu indicators by date before training.
>
> **Structuring menu tags**
>
> I’m adding verified per-meal flags such as `has_gravy`, `has_egg_curry`, and `has_dry_vegetables`, then aggregating them by date. I’m also correcting calendar mappings and preserving uncertain menu classifications as missing rather than guessing.
>
> **Updated menu features and structured menu tags**
>
> 
>
> ****
>
> 
>
> Worked for 24s

We should make one important improvement to the data structure before proceeding.

Your existing `mess_menu.csv` and `academic_calendar.csv` are good starting points. We do not need to redesign either file completely. We need to add menu-related features and correct the preprocessing logic so all three datasets work together.

The objective is\:

- Identify gravy-based dishes for rice demand.
- Identify egg curry and dry vegetables for wheat demand.
- Identify vacations, holidays and college events for attendance context.
- Calculate ingredient consumption per student.
- Preserve the original menu descriptions and academic event information.

# 1\. Update `mess_menu.csv`

Your current file has 28 rows (7 days × 4 meals). Keep all existing rows and columns.

Add three columns\:

| New column | Meaning |
|--------|--------|
| `has_gravy` | 1 if the meal contains a gravy-based dish |
| `has_egg_curry` | 1 if the meal contains egg curry |
| `has_dry_vegetables` | 1 if the meal contains dry vegetables |

Your new header should be\:

```csv
day,meal,menu_items,menu_source_note,transcription_confidence,has_gravy,has_egg_curry,has_dry_vegetables
```

### Example of how to update the rows

These are illustrative classifications, not verified labels for your complete menu.

```csv
Monday,Lunch,"Rice; roti; salad; moong dal; aloo parwal; mixed vegetable curry; achar",Source note,medium,1,0,0
Tuesday,Lunch,"Rice; roti; salad; sambar; aloo kundru; dahi vada; achar",Source note,medium,0,0,0
Wednesday,Dinner,"Roti; rice; dal; seasonal vegetable; omelette curry",Source note,low,1,0,0
```

**Important classification rules\:**

- Don't mark every dish containing the word `curry` as gravy. Check the actual preparation.
- Don't classify omelette curry as egg curry unless the cook confirms that it belongs to the same preparation category.
- Mark dry vegetables only when they are actually prepared as dry dishes.
- Preserve uncertain menu transcriptions. Do not turn uncertainty into a confirmed classification.

Use `1` for yes and `0` for no.

For your project, these are manual domain labels based on the menu and cook's knowledge, not labels generated by an AI model.

# 2\. `academic_calendar.csv` - Keep the existing structure

Your current structure is appropriate\:

```csv
event_name,start_date,end_date,event_type,source_note
```

Keep all six existing events.

There is one correction needed in the Python code: your calendar contains `academic_deadline`, but your current `type_to_flag` dictionary does not handle it.

We should support these event types\:

| Event type | Feature |
|--------|--------|
| `vacation` | `is_vacation` |
| `holiday` | `is_holiday` |
| `college_event` | `is_college_event` |
| `academic_activity` | `is_academic_activity` |
| `academic_deadline` | `is_academic_deadline` |

We should also retain the actual event names in `calendar_events`\.

Do not automatically assume every college event reduces attendance. Our initial observation is that vacations and events can reduce attendance, but the magnitude must be learned from the actual records.

# 3\. Replace your `preprocessing.py`

Your pasted code contains formatting corruption and references `attach_menu_context()` without showing its implementation.

Replace it with the following clean implementation.

```python

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

    menu["day"] = menu["day"].str.strip().str.title()
    menu["meal"] = menu["meal"].str.strip().str.title()

    if menu.duplicated(["day", "meal"]).any():
        raise ValueError("Duplicate day and meal entries found.")

    for column in MENU_FLAGS:
        menu[column] = pd.to_numeric(
            menu[column], errors="raise"
        )

        if not menu[column].isin([0, 1]).all():
            raise ValueError(
                f"{column} must contain only 0 or 1."
            )

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

    # Daily ingredient records are aggregated across meals.
    # Therefore retain both daily and lunch-specific menu flags.

    daily_flags = (
        menu.groupby("day")[MENU_FLAGS]
        .max()
        .add_prefix("any_meal_")
        .reset_index()
    )

    lunch_menu = menu[
        menu["meal"].str.lower() == "lunch"
    ][["day", *MENU_FLAGS]].copy()

    lunch_menu = lunch_menu.rename(
        columns={
            column: f"lunch_{column}"
            for column in MENU_FLAGS
        }
    )

    out = out.merge(
        daily_flags,
        left_on="weekday",
        right_on="day",
        how="left",
        validate="many_to_one",
    )

    out = out.drop(columns=["day"])

    out = out.merge(
        lunch_menu,
        left_on="weekday",
        right_on="day",
        how="left",
        validate="many_to_one",
    )

    out = out.drop(columns=["day"])

    menu_columns = [
        f"any_meal_{column}" for column in MENU_FLAGS
    ] + [
        f"lunch_{column}" for column in MENU_FLAGS
    ]

    if out[menu_columns].isna().any().any():
        raise ValueError(
            "Some weekdays do not have complete menu classifications."
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

    # Do not use total_food_mass_kg_approx:
    # it combines different measurement units.

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
```

# 4\. Update the main data-loading pipeline

In your main application or wherever you load the datasets, use\:

```python
import pandas as pd

from src.preprocessing import (
    load_calendar,
    load_menu,
    prepare_analysis_data,
)

mess_data = pd.read_csv("data/raw/data.csv")

calendar = load_calendar(
    "config/academic_calendar.csv"
)

menu = load_menu(
    "config/mess_menu.csv"
)

processed_data = prepare_analysis_data(
    mess_data,
    calendar,
    menu,
)

print(processed_data.head())
```

Adjust the import path if your `src` folder is not a Python package yet. You can add an empty `src/__init__.py`\.

# 5\. What output should we expect?

After preprocessing, your original daily records will have additional columns.

| New column | Meaning |
|--------|--------|
| `weekday` | Day of the week |
| `is_vacation` | Whether date falls during vacation |
| `is_holiday` | Whether date is a holiday |
| `is_college_event` | Whether a college event occurs |
| `is_academic_activity` | Academic activity indicator |
| `is_academic_deadline` | Academic deadline indicator |
| `calendar_events` | Names of overlapping events |
| `any_meal_has_gravy` | Gravy dish appears in any meal |
| `any_meal_has_egg_curry` | Egg curry appears in any meal |
| `any_meal_has_dry_vegetables` | Dry vegetables appear in any meal |
| `lunch_has_gravy` | Gravy dish at lunch |
| `lunch_has_egg_curry` | Egg curry at lunch |
| `lunch_has_dry_vegetables` | Dry vegetables at lunch |
| `rice_kg_per_student` | Rice consumption per student |
| `wheat_flour_kg_per_student` | Wheat consumption per student |

**Why keep both daily and lunch-specific features?**

Your historical data contains daily ingredient totals, not meal-wise consumption. We can investigate whether lunch menu categories correlate with total daily usage, but we cannot claim that the daily rice quantity was consumed specifically at lunch.

# 6\. One additional file we should create: `feature_engineering.py`

Keep preprocessing and feature engineering separate.

- `preprocessing.py`\: clean and combine datasets.
- `feature_engineering.py`\: derive analytical variables.
- `analysis.py`\: investigate relationships.
- `recommendation.py`\: estimate preparation quantities.

This separation will make your project easier to explain during the technical evaluation.

# 7\. Your next tasks

Follow this order\:

**Implementation checklist** /7

**Our next milestone is EDA, not model training.** We will establish whether the three findings from the cook are visible in the actual historical records, quantify the relationships where possible, and then build the recommendation algorithm.

One final methodological point: because the menu repeats weekly, menu categories can be strongly associated with weekdays. We must account for that when interpreting comparisons, rather than assuming a difference is caused by gravy or egg curry alone.

## Prompt:
11/18/2026, 2:21:15 AM

done now lets move ahead and fast to conclude we have most patterns and data connected

## Response:
11/18/2026, 2:21:16 AM · gpt-6

> **Inspecting Available Data Files**
>
>
> ****
>
> 
>
> **Inspected project data, loaders, menus, calendars, and tests**
>
> 
>
> **Advancing the analysis**
>
> I’m moving from validation into EDA and recommendation logic. The data shows repeated weekday patterns, but the sample is small, so I’ll prioritize robust summaries, menu associations, and clear next code steps without overclaiming.
>
> **Finalizing the pipeline**
>
> I’m treating menus as fixed weekday context, not independent statistical effects. I’ll use them to explain recommendations, while relying on per-student weekday baselines and explicit attendance inputs rather than unsupported multipliers.
>
> **Advanced analysis and finalized the pipeline**
>
> 
>
> **Used python tool**
>
> 
>
> Worked for 47s

# Phase 4 - EDA, pattern validation and recommendation engine

We are close to the actual tool. We should now stop adding more features and concentrate on producing a reliable recommendation.

I checked the available project files and ran the existing tests using `python -m pytest -q`\.

(4 existing tests passed)

## 1\. What the actual data tells us

Our 23 daily records cover 25 October-16 November 2026.

Some useful findings\:

| Metric | Finding |
|--------|--------|
| Average students served | 411 |
| Normal-day average | 416 |
| Sports Meet average | 392 |
| Diwali attendance | 300 |
| Average rice per student | Approximately 0.126 kg |
| Average wheat per student | Approximately 0.086 kg |

### Academic calendar findings

Interpretation\:

- Diwali attendance was 300, compared with 372 on the other recorded Sundays: approximately 19.4% lower.
- The mid-semester break observation was also a Sunday, with 372 students.
- Sports Meet attendance averaged 392, but the recorded counts match the usual Friday, Saturday and Sunday weekday patterns.

**Important\:** We cannot conclude that every college event reduces attendance. The evidence supports a particularly clear reduction on Diwali, but the other categories have very few observations.

### Ingredient consumption

These values are descriptive, not proof that a particular dish caused a change.

## 2\. Important modelling decision

There is one limitation we need to handle carefully.

Your menu repeats every week, so Monday's menu is the same across the available Monday records. The menu category and weekday are therefore closely linked.

Also, your operational data contains daily ingredient totals, not separate meal-wise quantities.

Consequently\:

- We can analyse daily rice and wheat usage against menu categories.
- We can use the cook's menu knowledge in our recommendation explanation.
- We cannot independently quantify the causal effect of gravy or egg curry from these 23 records.
- We cannot calculate meal-wise consumption from daily totals.

Our first model will therefore use historical weekday patterns as its statistical baseline, with menu and academic information as contextual explanations.

This is more defensible than inventing adjustment percentages.

## 3\. Implement `src/analysis.py`

Create this file. It will calculate the patterns we need for the final dashboard.

```python

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
```

## 4\. Final recommendation engine

Keep your existing `recommendation.py` baseline. It already has an important safeguard: it only uses historical records before the target date.

The recommendation should work like this\:

1. User selects a future date.
2. User enters expected student attendance.
3. The system identifies the weekday and its associated menu.
4. It selects previous records from the same weekday.
5. It calculates the median ingredient consumption per student.
6. It multiplies that rate by expected attendance.
7. It displays the relevant academic event and menu information.

For example\:

**Illustrative recommendation**

Example only; not a calculated result from a specific target date.

Expected attendance

# 420

Historical rice rate

# 0.126 kg

---

**Estimated rice requirement**

# 52.9 kg

420 × 0.126 kg per student

The result should also display the historical records used and the target day's menu and academic context.

Do not automatically reduce the expected attendance because of a holiday. Let the manager enter the expected count, with historical attendance and calendar information available to support that decision.

## 5\. Final dashboard structure

Your completed Streamlit application should have four sections\:

| Section | Contents |
|--------|--------|
| Overview | Student attendance, ingredient usage and historical trends |
| Menu analysis | Rice and wheat consumption by menu category |
| Academic analysis | Attendance during normal days, vacations and events |
| Preparation planner | Date selection, expected attendance and quantity recommendations |

## 6\. Final testing

Run\:

```bash
python -m pytest -q
```

Then\:

```bash
streamlit run app.py
```

Test these cases\:

- Normal weekday.
- Vacation or holiday.
- College event.
- Missing menu classification.
- Zero expected students.
- Invalid CSV quantity.
- A target date with insufficient historical data.

The tool must explain when it does not have enough information rather than generating an arbitrary estimate.

## 7\. Finish the assignment

Once the dashboard works, update the README with\:

- Project overview and real problem.
- Mess location and intended user.
- Fieldwork findings.
- Actual dataset description.
- Technologies used.
- Installation and execution instructions.
- Actual output and screenshots.
- Limitations.
- Three-minute demonstration recording.

Also update `ai-chats/` with the relevant exported conversations.

**My recommended final scope\:** a context-aware daily ingredient preparation planner, not a machine-learning food-waste prediction system. It is smaller, explainable, grounded in the actual mess records and directly addresses the cook's estimation problem.

One final requirement: test the generated recommendation with the mess cook or manager before describing it as useful in practice.

## Prompt:
11/18/2026, 2:30:51 AM

2026-11-18 02:28:00.446 Uncaught app execution
Traceback (most recent call last):
  File "C:\Users\acer\AppData\Local\Programs\Python\Python312\Lib\site-packages\streamlit\runtime\scriptrunner\exec_code.py", line 136, in exec_func_with_error_handling
    result = func()
             ^^^^^^
  File "C:\Users\acer\AppData\Local\Programs\Python\Python312\Lib\site-packages\streamlit\runtime\scriptrunner\script_runner.py", line 936, in code_to_exec
    exec(code, module.__dict__)  # noqa: S102
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\acer\OneDrive\Documents\Development\AI ML\Take Home Assignment\Mess Demand and Food Waste Analyzer\app.py", line 5, in <module>
    from src.data_loader import load_mess_data, data_quality_report
  File "C:\Users\acer\OneDrive\Documents\Development\AI ML\Take Home Assignment\Mess Demand and Food Waste Analyzer\src\__init__.py", line 15, in <module>
    menu = load_menu(
           ^^^^^^^^^^
  File "C:\Users\acer\OneDrive\Documents\Development\AI ML\Take Home Assignment\Mess Demand and Food Waste Analyzer\src\preprocessing.py", line 87, in load_menu
    raise ValueError(
ValueError: has_gravy must contain only 0 or 1.
2026-11-18 02:29:25.114 Uncaught app execution
Traceback (most recent call last):
  File "C:\Users\acer\AppData\Local\Programs\Python\Python312\Lib\site-packages\streamlit\runtime\scriptrunner\exec_code.py", line 136, in exec_func_with_error_handling
    result = func()
             ^^^^^^
  File "C:\Users\acer\AppData\Local\Programs\Python\Python312\Lib\site-packages\streamlit\runtime\scriptrunner\script_runner.py", line 936, in code_to_exec
    exec(code, module.__dict__)  # noqa: S102
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\acer\OneDrive\Documents\Development\AI ML\Take Home Assignment\Mess Demand and Food Waste Analyzer\app.py", line 5, in <module>
    from src.data_loader import load_mess_data, data_quality_report
  File "C:\Users\acer\OneDrive\Documents\Development\AI ML\Take Home Assignment\Mess Demand and Food Waste Analyzer\src\__init__.py", line 19, in <module>
    processed_data = prepare_analysis_data(
                     ^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\acer\OneDrive\Documents\Development\AI ML\Take Home Assignment\Mess Demand and Food Waste Analyzer\src\preprocessing.py", line 235, in prepare_analysis_data
    out = attach_menu_context(out, menu)
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\acer\OneDrive\Documents\Development\AI ML\Take Home Assignment\Mess Demand and Food Waste Analyzer\src\preprocessing.py", line 180, in attach_menu_context
    out = out.drop(columns=["day"])
          ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\acer\AppData\Local\Programs\Python\Python312\Lib\site-packages\pandas\core\frame.py", line 5603, in drop
    return super().drop(
           ^^^^^^^^^^^^^
  File "C:\Users\acer\AppData\Local\Programs\Python\Python312\Lib\site-packages\pandas\core\generic.py", line 4810, in drop
    obj = obj._drop_axis(labels, axis, level=level, errors=errors)
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\acer\AppData\Local\Programs\Python\Python312\Lib\site-packages\pandas\core\generic.py", line 4852, in _drop_axis
    new_axis = axis.drop(labels, errors=errors)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\acer\AppData\Local\Programs\Python\Python312\Lib\site-packages\pandas\core\indexes\base.py", line 7136, in drop
    raise KeyError(f"{labels[mask].tolist()} not found in axis")
KeyError: "['day'] not found in axis"
debugging now

## Response:
11/18/2026, 2:30:52 AM · gpt-6

The errors are coming from three separate issues. We can fix them without changing your project architecture.

**Do not change `app.py` yet.** Fix the import and preprocessing issues first.

# 1\. Fix `src/__init__.py` - most important

Your traceback shows\:

```text
src/__init__.py, line 15
menu = load_menu(...)
```

This means your `__init__.py` is executing the entire data-loading pipeline whenever Python imports anything from `src`\.

That is incorrect for our project structure.

**Open `src/__init__.py` and remove everything inside it.**

Keep only\:

```python
"""Mess Demand & Food Waste Analyser package."""
```

Why?

When you write\:

```python
from src.data_loader import load_mess_data
```

Python executes `src/__init__.py` first.

That file should not load CSVs, initialize dataframes, or run the application. Those operations belong in `app.py` or dedicated functions.

This also explains why your errors appear during imports.

---

# 2\. Fix `has_gravy must contain only 0 or 1`

Your current `load_menu()` expects\:

```python
0
1
```

But your CSV probably contains blank cells, `Yes`/`No`, or another representation.

We should make the validation explicit rather than silently converting unknown values.

Replace the menu flag validation inside `load_menu()` with\:

```python
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
```

**Also check your CSV header.** It must contain\:

```csv
day,meal,menu_items,menu_source_note,transcription_confidence,has_gravy,has_egg_curry,has_dry_vegetables
```

Every row must have three valid classification values.

For example\:

```csv
Monday,Lunch,"Rice; roti; moong dal; mixed vegetable curry",source,medium,1,0,0
```

Do not leave a classification blank. If you cannot confidently classify a dish, investigate it rather than guessing.

---

# 3\. Fix `KeyError: ['day'] not found in axis`

This is a merge issue.

Your historical CSV may already contain a `day` column.

When Pandas merges two dataframes that both contain `day`, it can create\:

```text
day_x
day_y
```

Consequently, this fails\:

```python
out = out.drop(columns=["day"])
```

We can avoid the issue entirely by replacing your `attach_menu_context()` function with a mapping-based implementation.

Replace the entire function with\:

```python

def attach_menu_context(
    df: pd.DataFrame,
    menu: pd.DataFrame,
) -> pd.DataFrame:

    out = df.copy()

    # Aggregate menu indicators across all meals for each weekday.
    daily_menu = (
        menu.groupby("day")[MENU_FLAGS]
        .max()
    )

    # Create daily menu features using weekday mapping.
    for column in MENU_FLAGS:
        out[f"any_meal_{column}"] = (
            out["weekday"].map(daily_menu[column])
        )

    # Extract lunch-specific menu indicators.
    lunch_menu = (
        menu[menu["meal"].str.lower() == "lunch"]
        .set_index("day")[MENU_FLAGS]
    )

    for column in MENU_FLAGS:
        out[f"lunch_{column}"] = (
            out["weekday"].map(lunch_menu[column])
        )

    # Ensure every weekday has a corresponding menu.
    menu_columns = [
        f"any_meal_{column}" for column in MENU_FLAGS
    ] + [
        f"lunch_{column}" for column in MENU_FLAGS
    ]

    if out[menu_columns].isna().any().any():
        raise ValueError(
            "Missing menu classification for one or more weekdays."
        )

    return out
```

This approach\:

- Preserves your original `day` column.
- Avoids duplicate merge columns.
- Maps menu information directly using weekdays.
- Keeps daily and lunch-specific indicators separate.

---

## 4\. Restart Streamlit

Stop the currently running application using `Ctrl + C`\.

Then execute\:

```bash
streamlit run app.py
```

If the same error persists, clear the Streamlit cache\:

```bash
streamlit cache clear
```

Then restart.

## 5\. Verify the fixes

Run these commands\:

```bash
python -c "from src.preprocessing import load_menu, load_calendar, prepare_analysis_data; print('Imports successful')"
```

Then\:

```bash
python -m pytest -q
```

Finally\:

```bash
streamlit run app.py
```

**Expected result**

`src` imports without executing the application.

Menu flags are validated and converted to integers.

Menu context is attached without duplicate-column errors.

Streamlit starts successfully.

**Do these three fixes first.** If another traceback appears, share the complete traceback and the relevant function. We will fix the actual cause rather than making random changes elsewhere.

## Prompt:
11/18/2026, 2:37:55 AM

![image(20261117-210753).png](https://sdmntprcentralindia.oaiusercontent.com/files/00000000-bf6c-8208-b302-9daf6bc4deae/raw?se=2026-11-17T22%3A30%3A08Z&sp=r&sv=2026-06-06&sr=b&scid=aaefbf3e-e32b-40c9-97ef-4fcb185a45bd&skoid=3cb6de21-012a-49c9-9402-a1ebf8d0bd06&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2026-11-17T03%3A59%3A21Z&ske=2026-11-18T03%3A59%3A21Z&sks=b&skv=2026-06-06&sig=ha5Z%2BCRaopaydWjUVbA6VL3i04/XeMjCL59cu/yVGnk%3D)

menu is missing

## Response:
11/18/2026, 2:37:57 AM · gpt-6

The screenshot shows that the menu file is not necessarily missing. The actual problem is that **`prepare_analysis_data()` is being called without the `menu` argument.**

We need to pass all three datasets to the preprocessing function.

## 1\. Fix `app.py`

Find this code\:

```python
processed_data = prepare_analysis_data(
    mess_data,
    calendar
)
```

Replace it with\:

```python
# Load academic calendar
calendar = load_calendar(
    "config/academic_calendar.csv"
)

# Load mess menu
menu = load_menu(
    "config/mess_menu.csv"
)

# Prepare combined analysis data
processed_data = prepare_analysis_data(
    mess_data,
    calendar,
    menu
)
```

## 2\. Check your imports

At the top of `app.py`, ensure you have\:

```python
from src.preprocessing import (
    load_calendar,
    load_menu,
    prepare_analysis_data
)
```

## 3\. Verify your project structure

Your menu file should be here\:

```text
Mess Demand and Food Waste Analyzer/
│
├── app.py
│
├── config/
│   ├── academic_calendar.csv
│   └── mess_menu.csv
│
├── data/
│   └── raw/
│       └── data.csv
│
└── src/
    ├── __init__.py
    ├── data_loader.py
    └── preprocessing.py
```

## 4\. Restart

```bash
streamlit run app.py
```

(Expected fix)

The preprocessing function now receives\:

- `mess_data`
- `calendar`
- `menu`

**If it still fails\:** Share your current `app.py` and `src/preprocessing.py`\. I can identify the exact line to change rather than guessing.

## Prompt:
11/18/2026, 2:42:58 AM

![image(20261117-211253).png](https://sdmntprcentralindia.oaiusercontent.com/files/00000000-b6f0-8208-aadc-96ad07994f73/raw?se=2026-11-17T22%3A30%3A08Z&sp=r&sv=2026-06-06&sr=b&scid=d392e71e-4327-4059-abd3-68d8f474c271&skoid=3cb6de21-012a-49c9-9402-a1ebf8d0bd06&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2026-11-17T03%3A34%3A53Z&ske=2026-11-18T03%3A34%3A53Z&sks=b&skv=2026-06-06&sig=Nx4GZAebfACoznOETKCYfTwvh3f/uCDcCjQTUu/2ZEU%3D)

what is the error now?

## Response:
11/18/2026, 2:43:00 AM · gpt-6

> **Diagnosing schema mismatch**
>
> I’m seeing a column-name mismatch: the display code expects older `menu_*` fields, while preprocessing now creates `any_meal_*` and meal-specific fields. I’ll recommend updating the display list or adding backward-compatible aliases.
>
> Worked for 4s

This is a **column name mismatch between `preprocessing.py` and `app.py`**\. Your data is loading, but the dashboard is requesting columns that your updated preprocessing function does not create.

### 1\. Why this error occurs

Your `app.py` expects these old column names\:

```python
menu_cols = [
    "menu_summary",
    "menu_has_egg",
    "menu_has_gravy_or_curry",
    "menu_has_roti_or_paratha",
    "menu_has_rice"
]
```

But our updated `preprocessing.py` creates these columns instead\:

```python
any_meal_has_gravy
any_meal_has_egg_curry
any_meal_has_dry_vegetables

lunch_has_gravy
lunch_has_egg_curry
lunch_has_dry_vegetables
```

Pandas raises `KeyError` because the requested columns don't exist.

### 2\. Fix it in `app.py`

Find the section titled\:

**3\. Weekly menu matched to each record**

Replace its existing `menu_cols` definition and dataframe display with\:

```python
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
```

### 3\. Restart Streamlit

```bash
Ctrl + C
streamlit run app.py
```

(Expected fix)

The weekly menu section should now display the menu-related features for each historical date.

### 4\. One additional improvement

We should eventually display the actual dish names (`menu_items`\) alongside these classifications, not just binary indicators.

That will make the dashboard easier to understand during your interview demonstration.

**For now, make this change and share the next screen or traceback if another error appears.**

## Prompt:
11/18/2026, 2:44:25 AM

from pathlib import Path
import streamlit as st
import pandas as pd

from sr&#x63;*.*&#x64;ata_loader import load_mess_dat&#x61;*,* data_quality_report
from sr&#x63;*.*&#x70;reprocessing import (
    load_calenda&#x72;*,*
    load_men&#x75;*,*
    prepare_analysis_dat&#x61;*,*
    INGREDIENT_COLUMN&#x53;*,*
)
from sr&#x63;*.*&#x72;ecommendation import make_daily_baseline

ROOT = Path(\_\_file\_\_)*.*&#x70;arent

DATA_PATH = ROOT / "data" / "raw" / "data.csv"
CALENDAR_PATH = ROOT / "config" / "academic_calendar.csv"
MENU_PATH = ROOT / "config" / "mess_menu.csv"

s&#x74;*.*&#x73;et_page_config(
    page_title="Mess Demand Analyser"*,*
    page_icon="🍽️"*,*
    layout="wide"
)

s&#x74;*.*&#x74;itle("Mess Demand Analyser")
s&#x74;*.*&#x63;aption(
    "Historical ingredient usage and academic-calendar context"
)

tr&#x79;*:*
    raw = load_mess_data(DATA_PATH)
    calendar = load_calendar(CALENDAR_PATH)
    menu = load_menu(MENU_PATH)

    data = prepare_analysis_data(
        ra&#x77;*,*
        calenda&#x72;*,*
        menu
    )

except Exception as ex&#x63;*:*
    s&#x74;*.*&#x65;rror(f"Could not load project data: {exc}")
    s&#x74;*.*&#x73;top()

report = data_quality_report(raw)
col&#x31;*,* col&#x32;*,* col&#x33;*,* col4 = s&#x74;*.*&#x63;olumns(4)
col&#x31;*.*&#x6D;etric("Daily records"*,* report["rows"])
col&#x32;*.*&#x6D;etric("Distinct dates"*,* report["unique_dates"])
col&#x33;*.*&#x6D;etric("Students (average)"*,* f"{raw['students_served_est']*.*&#x6D;ean():.0f}")
col&#x34;*.*&#x6D;etric("Weekday mismatches"*,* report["weekday_mismatches"])

s&#x74;*.*&#x73;ubheader("1. Historical consumption")
s&#x74;*.*&#x6C;ine_chart(dat&#x61;*.*&#x73;et_index("date")["students_served_est"])
selected = s&#x74;*.*&#x73;electbox("Ingredient usage per student"*,* list(INGREDIENT_COLUMN&#x53;*.*&#x6B;eys()))
s&#x74;*.*&#x6C;ine_chart(dat&#x61;*.*&#x73;et_index("date")[INGREDIENT_COLUMNS[selected]])
s&#x74;*.*&#x63;aption("Per-student values are daily recorded quantities divided by the recorded estimated student count.")

s&#x74;*.*&#x73;ubheader("2. Academic calendar context")
context_cols = ["date"*,* "weekday"*,* "students_served_est"*,* "calendar_events"*,* "is_vacation"*,* "is_holiday"*,* "is_college_event"*,* "is_academic_activity"]
s&#x74;*.*&#x64;ataframe(data[context_cols]*,* use_container_width=Tru&#x65;*,* hide_index=True)

s&#x74;*.*&#x73;ubheader("3. Weekly menu matched to each record")
menu_cols = ["date"*,* "weekday"*,* "menu_summary"*,* "menu_has_egg"*,* "menu_has_gravy_or_curry"*,* "menu_has_roti_or_paratha"*,* "menu_has_rice"]
s&#x74;*.*&#x64;ataframe(data[menu_cols]*,* use_container_width=Tru&#x65;*,* hide_index=True)
s&#x74;*.*&#x63;aption("Menu text is transcribed from the revised menu photograph. Some handwritten/blurred items are uncertain; see config/mess_menu.csv.")

s&#x74;*.*&#x73;ubheader("4. Daily preparation estimate")
s&#x74;*.*&#x77;rite("A transparent baseline using the median historical ingredient use per student from previous records. Same-weekday history is used when at least two prior records exist.")
min_date = raw["date"]*.*&#x6D;in()*.*&#x64;ate()
max_date = raw["date"]*.*&#x6D;ax()*.*&#x64;ate()
target_date = s&#x74;*.*&#x64;ate_input("Date to estimate"*,* value=max_date + p&#x64;*.*&#x54;imedelta(days=1)*,* min_value=min_date)
expected_students = s&#x74;*.*&#x6E;umber_input("Expected students"*,* min_value=&#x31;*,* max_value=100&#x30;*,* value=int(raw["students_served_est"]*.*&#x6D;edian())*,* step=1)
if s&#x74;*.*&#x62;utton("Generate preparation estimate")*:*
    estimate = make_daily_baseline(ra&#x77;*,* p&#x64;*.*&#x54;imestamp(target_date)*,* int(expected_students))
    s&#x74;*.*&#x64;ataframe(estimat&#x65;*,* use_container_width=Tru&#x65;*,* hide_index=True)
    s&#x74;*.*&#x77;arning("This is a historical baseline, not a validated forecast. Academic events and menu are displayed as context but are not yet used as numerical adjustment factors. Leftover quantities are not recorded, so this tool does not calculate food waste.")

with s&#x74;*.*&#x65;xpander("Data quality report")*:*
    s&#x74;*.*&#x6A;son(report)
with s&#x74;*.*&#x65;xpander("Original historical records")*:*
    s&#x74;*.*&#x64;ataframe(ra&#x77;*,* use_container_width=Tru&#x65;*,* hide_index=True)comapre

## Response:
11/18/2026, 2:44:25 AM · gpt-6

> **Comparing the implementation**
>
> I’m checking the app against the updated preprocessing flow. The main mismatch is the menu display: `attach_menu_context()` currently creates flags, not the descriptive menu columns your UI expects.
>
> **Compared the implementation**
>
> 
>
> Worked for 5s

I compared your current `app.py` with the updated `preprocessing.py` structure we implemented.

Your main data-loading pipeline is correct. You are loading all three datasets and passing them to `prepare_analysis_data()` correctly.

There are **three changes required**\.

## 1\. Fix the weekly menu section - primary error

Your current code expects these columns\:

```python
menu_cols = [
    "date",
    "weekday",
    "menu_summary",
    "menu_has_egg",
    "menu_has_gravy_or_curry",
    "menu_has_roti_or_paratha",
    "menu_has_rice"
]
```

These are old column names.

Your current `attach_menu_context()` generates\:

- `any_meal_has_gravy`
- `any_meal_has_egg_curry`
- `any_meal_has_dry_vegetables`
- `lunch_has_gravy`
- `lunch_has_egg_curry`
- `lunch_has_dry_vegetables`

**Replace your entire menu section with\:**

```python
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
```

## 2\. Include academic deadlines

Your current section is\:

```python
context_cols = [
    "date",
    "weekday",
    "students_served_est",
    "calendar_events",
    "is_vacation",
    "is_holiday",
    "is_college_event",
    "is_academic_activity"
]
```

Add `is_academic_deadline`\:

```python
context_cols = [
    "date",
    "weekday",
    "students_served_est",
    "calendar_events",
    "is_vacation",
    "is_holiday",
    "is_college_event",
    "is_academic_activity",
    "is_academic_deadline"
]
```

This assumes your `preprocessing.py` contains the corresponding flag, as in our previous update.

## 3\. Display actual menu items instead of only indicators

This is an improvement I recommend.

Currently, the dashboard displays whether a dish category exists, but not which dishes are actually served.

In `attach_menu_context()` in `preprocessing.py`, add this before `return out`\:

```python
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
```

Then include this in your dashboard's menu columns\:

```python
menu_cols = [
    "date",
    "weekday",
    "menu_summary",
    "lunch_has_gravy",
    "lunch_has_egg_curry",
    "lunch_has_dry_vegetables",
]
```

This will make the dashboard much more informative during your demonstration.

---

## 4\. Everything else in your `app.py`

| Section | Status |
|--------|--------|
| Imports | Correct, assuming names match your modules |
| File paths | Correct, assuming the folder structure matches |
| Load historical CSV | Correct |
| Load academic calendar | Correct |
| Load mess menu | Correct |
| `prepare_analysis_data()` | Correct |
| Data quality metrics | Correct |
| Historical consumption charts | Correct |
| Academic context | Add deadline column |
| Weekly menu | Replace outdated column names |
| Preparation estimate | Correct as a historical baseline |
| Data quality expanders | Correct |

## 5\. Final verification

Save both files and restart\:

```bash
streamlit run app.py
```

If the application loads, verify these four sections\:

1. Historical consumption charts.
2. Academic calendar records.
3. Weekly menu matched to all 23 dates.
4. Daily preparation estimate.

**One important distinction\:** Your recommendation currently uses historical ingredient consumption. Although menu and calendar context are displayed, they are not yet numerical adjustment factors. Keep that limitation visible in the dashboard until we validate a context-aware recommendation method.

---

If you want, I can:

- Fix menu columns and display in app.py
- Add missing datasets to preprocessing call
- Refactor src/__init__.py to avoid side effects



---
Powered by [ChatGPT Exporter](https://www.chatgptexporter.com)