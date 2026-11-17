# Fieldwork Report: Mess Demand & Food Waste Analyser

## 1. Visit Information

- **Location:** Hostel A Mess, NIT Jamshedpur, Jharkhand
- **Date:** 17 November 2026
- **Observation start time:** 12 40 PM
- **Observation end time:** 1 15 PM
- **Total observation duration:** 35 minutes+
- **Person interviewed:** Mess Supervisor - Sandeep and staff - Anubhav
- **People involved in mess operations:** Bhusan Kumar (Mess Manager), Sandeep (Mess Supervisor), cook and bookkeeper.

## 2. Purpose of the Visit

The purpose of this visit was to understand how food preparation quantities are decided in the hostel mess, how staff handle changing meal demand, and whether food wastage or shortages create operational difficulties.

Our initial hypothesis was that inaccurate food preparation estimates could result in excess food and unnecessary wastage.

We wanted to understand the actual workflow before deciding what kind of tool would be useful.

## 3. Mess Operations Observed and Explained

### 3.1 Scale of Operations

The mess kitchen serves approximately 400–450 female students across two hostels that share the same kitchen.

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

**Interviewee:** Sandeep (Mess supervisor), Anubhav (Staff)
**Role:** Mess Supervisor and Mess staff  
**Interview date and time:** 17 November 2026 12 45 PM

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

| Evidence                      | File                               | Status              |
| ----------------------------- | ---------------------------------- | ------------------- |
| Conversation transcript       | `evidence/interview-transcript.md` | Transcript provided |
| First timestamped photograph  | `evidence/mess_observation1.jpg`   | Images Provided     |
| Second timestamped photograph | `evidence/mess_observation2.jpg`   | Images Provided     |
| Third timestamped photograph  | `evidence/mess_observation3.jpg`   | Images Provided     |
| Raw operational records       | `data.csv`                         | Collected           |
| Interview details             | This document                      | 17 November 2026    |

## 10. Data Collection Method

The intended data source is the actual handwritten daily mess records and/or the corresponding Excel sheets maintained by the mess staff.

We will request permission to inspect the records and manually extract at least 20 genuine entries.

For every entry, we will preserve the original recorded values and document the meaning and source of each field.
