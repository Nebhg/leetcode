# Coding & Data Engineering Study Plan

**Goal:** Build the ability to write clean Python, work with data tools, and solve realistic engineering problems cold — no AI assistance.

**Daily commitment:** 1.5–2 hours  
**Started:** 2026-05-29  
**Rule:** No AI autocomplete, no Copilot, no Claude during sessions. The whole point is building muscle memory you can rely on in an interview room.

---

## Daily Structure

Split your session into three blocks:

| Block | Time | Focus |
|---|---|---|
| A | 20–25 min | Syntax / language / tool drill (book exercises, cold rewrites) |
| B | 50–60 min | Main problem — algorithm (LeetCode) or data problem (StrataScratch), alternating days |
| C | 20–30 min | Framework/tool study — one topic at a time, rotating through the stack |

Block A is non-negotiable. Even on days you're tired, do it. It's the block that builds fluency.

---

## Resources

**Books**
- *Python for Data Analysis* — Wes McKinney (core book — Python, pandas, NumPy)
- *Effective Python* — Brett Slatkin (language idioms, read selectively — don't grind it cover to cover)

**Algorithm practice**
- neetcode.io — watch the video for a problem, then close it and attempt cold
- leetcode.com — submit there to confirm correctness

**Realistic DE problems**
- StrataScratch (stratascratch.com) — real company interview questions, Python + SQL, filter by difficulty
- Focus on: data cleaning, groupby/aggregation, joins, window functions, outlier detection

**Framework courses (all free)**
- pandas/NumPy: exercises embedded in *Python for Data Analysis* — do them in a notebook, no autocomplete
- AWS: AWS Skill Builder — "AWS Cloud Practitioner Essentials" + "Data Engineering on AWS" path
- dbt: courses.getdbt.com — official free course, "dbt Fundamentals" then "Jinja, Macros, Packages"
- Airflow: Astronomer Academy (academy.astronomer.io) — "Airflow Fundamentals" certification course (free)

---

## Phase 1 — Python Core + Algorithm Foundations
### Duration: Weeks 1–4

**Goal:** Get Python syntax fluent, close the LeetCode Phase 1 gap, start moving on patterns.

**Where you are:** Binary Tree exercise unfinished, 4 problems logged. Real confidence ~5/10.

### What to do

**Block A — Syntax drills:**
Read *Python for Data Analysis* Part I (chapters 1–4). Do every code example by typing it yourself, not copy-pasting. Covers NumPy fundamentals, Python built-ins, and file handling. By the end of week 4 you should be able to write `np.array`, `np.reshape`, `np.where`, list comprehensions, generators, and context managers without hesitation.

**Block B — Algorithms (Mon/Wed/Fri) and Data problems (Tue/Thu/Sat):**

Algorithm days — complete remaining Phase 1 problems, then start Phase 2 patterns:
- Finish Binary Tree exercise in `02_data_structures.ipynb` (Day 1, Block A)
- Complete any unchecked BofA prep problems that weren't logged
- Work through: Two Pointers, Sliding Window, Hashmaps, Stack — one pattern per week

Data days — StrataScratch easy problems only:
- Filter: Python, Easy, topics = "Pandas Basics", "Data Manipulation"
- Target: 3 problems per week, no hints, write the full solution cold
- Good starting problems: "Find the most profitable city", "Count the number of user events made in 2020", "Workers with the highest salaries"

**Block C — Tool rotation:**
Week 1–2: NumPy (chapters 4–5 of *Python for Data Analysis*)
Week 3–4: pandas Series and DataFrame basics (chapters 5–6)

### Week-by-week focus

**Week 1:** Binary Tree completion + Two Pointers pattern + NumPy intro
**Week 2:** Sliding Window pattern + NumPy continued + first StrataScratch problems
**Week 3:** Hashmap deep dive + pandas intro + StrataScratch easy
**Week 4:** Stack pattern + pandas continued + cold rewrite day Sunday

### Sunday review ritual
Every Sunday, do cold rewrites of 3 problems from the week — no notes, no looking back. Log honestly. If you can't reconstruct it in 15 minutes, you don't own it yet.

---

## Phase 2 — Data Engineering Stack + Medium Problems
### Duration: Weeks 5–10

**Goal:** Get comfortable with the real DE toolkit (pandas, AWS, dbt, Airflow) and move into medium-difficulty problems.

**Block A — Book + exercises:**
*Python for Data Analysis* chapters 7–12: data cleaning, merging, groupby, time series, string manipulation. These chapters are directly relevant to what you'd be asked in a DE interview. Do all the exercises.

In parallel, start reading *Effective Python* selectively — read items 1–10 (Pythonic thinking), items 16–21 (comprehensions and generators), items 26–35 (functions). These fix the habits that trip you up under pressure.

**Block B — Algorithms (Mon/Wed/Fri):**
Medium LeetCode problems. One per session, 45 minutes max then check neetcode video if stuck.

Patterns to cover in order:
1. Trees BFS/DFS — Level Order Traversal (#102), Binary Tree Right Side View (#199)
2. Binary Search — Search in Rotated Array (#33), Find Minimum in Rotated Sorted Array (#153)
3. Linked List — Merge Two Sorted Lists (#21), Reorder List (#143)
4. Dynamic Programming intro — Climbing Stairs (#70), House Robber (#198), Coin Change (#322)
5. Graphs — Number of Islands (#200), Clone Graph (#133)

**Block B — Data problems (Tue/Thu/Sat):**
StrataScratch medium difficulty. Move toward more realistic problems:
- "Highest Energy Consumption" (Facebook)
- "Spotify Listening History" (Spotify)
- "Activity Rank" (Google)
- Any problem tagged "window functions" or "data cleaning"

Target: 3 per week. Log what you struggled with.

**Block C — Framework rotation (one per two weeks):**
- Weeks 5–6: AWS — complete "AWS Cloud Practitioner Essentials" on Skill Builder. Understand S3, IAM, Lambda, EC2, VPC. Don't just watch — take notes in your own words.
- Weeks 7–8: dbt — complete "dbt Fundamentals" on courses.getdbt.com. Build the Jaffle Shop project from scratch (they walk you through it). Understand models, refs, sources, tests, documentation.
- Weeks 9–10: Airflow — complete "Airflow Fundamentals" on Astronomer Academy. Understand DAGs, operators, sensors, task dependencies, XComs. Build one DAG from scratch.

---

## Phase 3 — Realistic DE Problems + Interview Simulation
### Duration: Weeks 11–16

**Goal:** Replicate interview conditions. Timed, cold, no help.

**Block A — Cold rewrites only:**
No new book content. Each morning, pick one problem from the previous week and rewrite it cold in under 15 minutes. Track time.

**Block B — Timed problem sessions:**
Algorithm days: 45 minutes per problem, hard stop. Simulate an interview — state the pattern out loud (or in comments), write tests first, then implement.

Data days: 30-minute StrataScratch medium/hard problems. No hints. These should feel like realistic work — cleaning messy data, computing metrics, joining tables, handling nulls.

**Block C — AWS deep dive:**
- "Data Engineering on AWS" path on Skill Builder
- Understand: Glue (ETL), Redshift (data warehouse), Athena (S3 querying), Kinesis (streaming), Lake Formation
- Draw your own architecture diagrams for common patterns: batch ingestion, streaming, ELT pipeline

### End-to-end project (Week 14–16)
Build one small DE project completely cold, no AI:
- Ingest data from a public API (e.g. FRED, OpenWeather, or a financial data API)
- Clean and transform it with pandas
- Load it somewhere (SQLite or S3 if you have an AWS account)
- Orchestrate with Airflow (simple 3-task DAG)
- If possible, add a dbt model on top

This is the thing you talk about in interviews. "I built this" is worth more than "I studied this."

---

## Phase 4 — Interview Readiness
### Duration: Weeks 17–20

**Goal:** Sharpen, not learn. You should know everything by now — this phase is about execution under pressure.

- 3x timed LeetCode sessions per week (45 min each, medium/hard)
- 2x StrataScratch sessions per week (real DE problems)
- 1x mock interview per week — either with a friend or record yourself solving a problem out loud
- AWS: review your architecture diagrams, make sure you can explain tradeoffs
- dbt + Airflow: make sure you can answer "walk me through how you'd build a pipeline" without hesitating

**Problems to have cold by the end:**
Algorithms: Two Sum, Valid Parentheses, Reverse Linked List, Binary Search, Invert Binary Tree, Level Order Traversal, Climbing Stairs, Number of Islands, Top K Frequent Elements, 3Sum, Longest Substring Without Repeating Characters

Data manipulation (pandas): groupby + agg, merge/join, pivot_table, apply with lambda, rolling windows, handling nulls, date arithmetic, string extraction with str accessor

---

## Tracking

Log sessions in `PROGRESS.md` using the existing format. After every StrataScratch problem, add a line:

```
- YYYY-MM-DD — [Problem name] ([Platform]) — [Easy/Medium/Hard] — [Pattern] — Confidence: X/10 — Notes: ...
```

Review the log every Sunday. If a pattern keeps showing up in "struggled with", prioritise it next week.

---

## Checkpoints

| Week | Milestone |
|---|---|
| 4 | All Phase 1 LeetCode patterns solid (can reconstruct cold) |
| 6 | AWS Cloud Practitioner knowledge solid, can explain S3/Lambda/Glue |
| 8 | dbt fundamentals complete, Jaffle Shop project built |
| 10 | Airflow fundamentals complete, one DAG built from scratch |
| 12 | Comfortable with medium LeetCode — solving most within 45 min |
| 14 | Comfortable with StrataScratch medium — solving without hints |
| 16 | End-to-end DE project complete |
| 20 | Interview ready across all dimensions |
