# Coding & DE Skills — Progress Tracker

**Last updated:** 2026-06-11
**Daily commitment:** 1 hour weekdays (extra optional), 2–3 hours weekends

> **Reset 2026-06-11 after Millennium rejection.** Diagnosis: the gap is not algorithm knowledge — it's *production*. Ben knows the solutions to Two Sum and Valid Parentheses but cannot type them from a blank file under pressure, and couldn't write asserts to test code in the interview. Every rule below targets that gap. Squarepoint technical interview is the live deadline.

---

## DAILY STRUCTURE (60 min weekdays)

| Block | Time | What |
|---|---|---|
| Syntax warm-up | 10 min | Type 5 idioms from the Syntax Drill List below, cold, from memory. No reference. |
| One problem, full protocol | 45 min | Visual trace → blank-file code → asserts → log (see protocol) |
| Wrap | 5 min | Log it honestly. Schedule the cold rewrite. |

**Weekends (2–3 hrs):** cold rewrites that are due → 1–2 new problems → 30 min DE tooling or MOOC.

---

## THE PROBLEM PROTOCOL

Every problem, every time, in this order:

1. **Trace first, code second.** Before writing any code, step through one example by hand — use `visualiser.html` for the pattern, or draw the state (pointers, stack, hashmap) yourself. You must be able to say what the state looks like at each step before you type anything.
2. **Blank file.** No skeleton, no snippets. Write the function signature yourself.
3. **Asserts are part of the solution — written BEFORE the function body.** Signature first, three asserts second (example case, degenerate input, "no" case), implementation third. See `asserts.md` for the full method. A solution without passing asserts is not done. This is the exact skill that failed at Millennium.
4. **15 min minimum stuck-time.** No AI ever during practice. Neetcode video only if genuinely stuck after 15 min — then close it and write from the trace, not from memory of the video.
5. **State the pattern and time/space complexity out loud before logging.**

**Cold rewrite schedule:** every solved problem gets rewritten from a blank file at **+1 day, +3 days, +7 days**. Under 10 minutes each, asserts included. If a rewrite fails, the problem goes back to day 0. Recognition without reconstruction is worthless — this schedule is the whole game.

---

## SYNTAX DRILL LIST

Rotate 5 per day in the warm-up. Type each from memory, run it, fix it without looking anything up.

1. Dict: `d.get(k, default)`, `k in d`, iterate `d.items()`
2. `defaultdict(list)` and `Counter` from collections
3. Stack via list: `append` / `pop` / `stack[-1]` / truthiness check
4. `enumerate(arr)` and `zip(a, b)`
5. Two-pointer skeleton: `l, r = 0, len(a)-1` + `while l < r:`
6. Slicing: `a[::-1]`, `a[1:]`, `s[i:j]`
7. List comprehension with condition; set comprehension
8. Sort: `sorted(arr, key=lambda x: ...)`, reverse, in-place `.sort()`
9. String build: `"".join(parts)`; `s.isalnum()`, `.lower()`
10. `deque` from collections: `popleft` / `append` (BFS skeleton)
11. Swap: `a[i], a[j] = a[j], a[i]`
12. `range(len(a)-1, -1, -1)` — iterate backwards
13. Set ops: `add`, `in`, `remove`; dedupe with `set(arr)`
14. `float("inf")` / `float("-inf")` as initial best values
15. Assert template: `assert f(x) == y, f"got {f(x)}"` — three cases minimum

---

## VISUAL REFERENCE

`visualiser.html` in this folder — interactive step-through of pointer/stack/hashmap state for core patterns. Use it in step 1 of the protocol until you can draw the traces unaided. New problems get added via the visualiser skill ("add X to the visualiser").

---

## FOUNDATIONS — JUST-IN-TIME PRIMERS

The uni gap is real: grades without the underlying material. But the fix is not watching lectures now — passive material didn't stick then and won't stick now. Each primer below is done by **implementing the structure from scratch once** and then explaining it out loud, the evening before starting that Blind 75 section. 20–30 min each, in the optional-extra slot.

- [ ] **Big-O reading skills** — read complexity straight off loop structure; why hashmap lookup is O(1) average and what "average" hides
- [ ] **Hash tables** (before Arrays & Hashing) — implement a toy hashmap: hash function, buckets as lists, collision handling. After this, `dict` stops being magic.
- [ ] **Stacks & queues** (before Stack section) — implement both with list/deque; connect to the call stack (why recursion IS a stack)
- [ ] **Binary search invariants** (before Binary Search) — implement it, then break it: off-by-one on `r = mid` vs `r = mid - 1`, when `while l < r` vs `l <= r`
- [ ] **Linked lists** (before Linked Lists) — node/pointer model on paper, then implement insert, delete, reverse from scratch
- [ ] **Trees & traversals** (before Trees) — implement pre/in/post-order recursively and BFS with a deque; trace the call stack by hand for one small tree
- [ ] **Heaps** (before Heap section) — heap property, why push/pop is O(log n); use `heapq` on a toy problem
- [ ] **Graphs** (before Graphs) — adjacency list representation; write BFS and DFS templates from scratch
- [ ] **Recursion → memoisation → DP** (before DP) — fibonacci naive, then memoised, then bottom-up. Same problem three ways is the whole DP intuition.

Log each one when done: name, date, and one sentence you'd use to explain it to someone else. If you can't write the sentence, it isn't done.

---

## MOOC PROGRESS

**Course:** [programming-25.mooc.fi](https://programming-25.mooc.fi)
**Current position:** Part 2 — near the end

| Part | Status | Notes |
|---|---|---|
| Part 1 | ✅ Done | |
| Part 2 | 🔄 In progress | Near the end |
| Part 3 | ⬜ | |
| Part 4 | ⬜ | Start Blind 75 when you reach here |
| Part 5 | ⬜ | |
| Part 6 | ⬜ | |
| Part 7 | ⬜ | |
| Part 8–14 | ⬜ | Advanced — read Fluent Python alongside from here |

**Rules for MOOC:** Skip the explanatory text. Go straight to exercises. If you know the concept, just implement it. Move fast.

---

## BLIND 75 — MAIN FOCUS

Work through in order by pattern. Each problem: Neetcode video → close → attempt cold → log.

### 1. Arrays & Hashing
- [ ] Contains Duplicate (#217)
- [ ] Valid Anagram (#242)
- [ ] Two Sum (#1)
- [ ] Group Anagrams (#49)
- [ ] Top K Frequent Elements (#347)
- [ ] Product of Array Except Self (#238)
- [ ] Valid Sudoku (#36)
- [ ] Encode and Decode Strings (#271)
- [ ] Longest Consecutive Sequence (#128)

### 2. Two Pointers
- [ ] Valid Palindrome (#125)
- [ ] Two Sum II (#167)
- [ ] 3Sum (#15)
- [ ] Container with Most Water (#11)
- [ ] Trapping Rain Water (#42)

### 3. Sliding Window
- [ ] Best Time to Buy and Sell Stock (#121)
- [ ] Longest Substring Without Repeating Characters (#3)
- [ ] Longest Repeating Character Replacement (#424)
- [ ] Permutation in String (#567)
- [ ] Minimum Window Substring (#76)
- [ ] Sliding Window Maximum (#239)

### 4. Stack
- [ ] Valid Parentheses (#20)
- [ ] Min Stack (#155)
- [ ] Evaluate Reverse Polish Notation (#150)
- [ ] Generate Parentheses (#22)
- [ ] Daily Temperatures (#739)
- [ ] Car Fleet (#853)
- [ ] Largest Rectangle in Histogram (#84)

### 5. Binary Search
- [ ] Binary Search (#704)
- [ ] Search a 2D Matrix (#74)
- [ ] Koko Eating Bananas (#875)
- [ ] Find Minimum in Rotated Sorted Array (#153)
- [ ] Search in Rotated Sorted Array (#33)
- [ ] Time Based Key-Value Store (#981)
- [ ] Median of Two Sorted Arrays (#4)

### 6. Linked Lists
- [ ] Reverse Linked List (#206)
- [ ] Merge Two Sorted Lists (#21)
- [ ] Reorder List (#143)
- [ ] Remove Nth Node from End of List (#19)
- [ ] Copy List with Random Pointer (#138)
- [ ] Add Two Numbers (#2)
- [ ] Linked List Cycle (#141)
- [ ] Find the Duplicate Number (#287)
- [ ] LRU Cache (#146)

### 7. Trees
- [ ] Invert Binary Tree (#226)
- [ ] Maximum Depth of Binary Tree (#104)
- [ ] Diameter of Binary Tree (#543)
- [ ] Balanced Binary Tree (#110)
- [ ] Same Tree (#100)
- [ ] Subtree of Another Tree (#572)
- [ ] Lowest Common Ancestor of BST (#235)
- [ ] Binary Tree Level Order Traversal (#102)
- [ ] Binary Tree Right Side View (#199)
- [ ] Count Good Nodes in Binary Tree (#1448)
- [ ] Validate Binary Search Tree (#98)
- [ ] Kth Smallest Element in BST (#230)
- [ ] Construct Binary Tree from Preorder and Inorder (#105)
- [ ] Binary Tree Maximum Path Sum (#124)
- [ ] Serialize and Deserialize Binary Tree (#297)

### 8. Heap / Priority Queue
- [ ] Kth Largest Element in a Stream (#703)
- [ ] Last Stone Weight (#1046)
- [ ] K Closest Points to Origin (#973)
- [ ] Kth Largest Element in an Array (#215)
- [ ] Task Scheduler (#621)
- [ ] Design Twitter (#355)
- [ ] Find Median from Data Stream (#295)

### 9. Graphs
- [ ] Number of Islands (#200)
- [ ] Clone Graph (#133)
- [ ] Max Area of Island (#695)
- [ ] Pacific Atlantic Water Flow (#417)
- [ ] Surrounded Regions (#130)
- [ ] Rotting Oranges (#994)
- [ ] Course Schedule (#207)
- [ ] Course Schedule II (#210)
- [ ] Number of Connected Components (#323)
- [ ] Graph Valid Tree (#261)
- [ ] Word Ladder (#127)

### 10. Dynamic Programming
- [ ] Climbing Stairs (#70)
- [ ] Min Cost Climbing Stairs (#746)
- [ ] House Robber (#198)
- [ ] House Robber II (#213)
- [ ] Longest Palindromic Substring (#5)
- [ ] Palindromic Substrings (#647)
- [ ] Decode Ways (#91)
- [ ] Coin Change (#322)
- [ ] Maximum Product Subarray (#152)
- [ ] Word Break (#139)
- [ ] Longest Increasing Subsequence (#300)
- [ ] Partition Equal Subset Sum (#416)

### 11. Intervals
- [ ] Insert Interval (#57)
- [ ] Merge Intervals (#56)
- [ ] Non-overlapping Intervals (#435)
- [ ] Meeting Rooms (#252)
- [ ] Meeting Rooms II (#253)
- [ ] Minimum Interval to Include Each Query (#2080)

---

## DE TOOLING TRACK

30 min/day, rotating through these topics. Do exercises, not reading. Each exercise: write from scratch in a notebook or script, no AI.

### Numpy — do these first
- [ ] Create arrays from lists, ranges, and random — know `np.array`, `np.arange`, `np.zeros`, `np.random.rand`
- [ ] Indexing and slicing — 1D and 2D arrays, boolean masks
- [ ] Vectorised operations — add, multiply, compare arrays without loops
- [ ] Broadcasting — understand why `arr + 1` works and when shapes conflict
- [ ] Aggregations — `mean`, `sum`, `std`, `argmax` along axes
- [ ] Reshape and transpose — `reshape`, `.T`, `flatten`

### Pandas — core
- [ ] Load a CSV with `read_csv` specifying dtypes, parse_dates, index_col
- [ ] Inspect a DataFrame — `head`, `info`, `describe`, `dtypes`, `value_counts`
- [ ] Filter rows — boolean indexing, `.query()`, `.isin()`
- [ ] Select columns — single, multiple, `.loc`, `.iloc`
- [ ] Handle nulls — `isna`, `dropna`, `fillna`
- [ ] Add and transform columns — `assign`, `apply`, vectorised string ops
- [ ] Sort — `sort_values`, `sort_index`, ascending/descending
- [ ] GroupBy — `groupby` + `agg` with multiple functions, `transform`, `filter`
- [ ] Merge and join — `merge` (inner/left/right/outer), `concat` axis 0 and 1
- [ ] Pivot and reshape — `pivot_table`, `melt`, wide ↔ long
- [ ] Window functions — `rolling`, `expanding`, `shift`, `diff`
- [ ] Time series — `resample`, `DatetimeIndex`, `pd.date_range`

### SQL — window functions focus
- [ ] Write a "top N per group" query using ROW_NUMBER
- [ ] Write a running total using SUM OVER with ROWS BETWEEN
- [ ] Write a day-over-day change query using LAG
- [ ] Write a query using a CTE to break it into readable steps
- [ ] Write a self-join to compare rows within the same table
- [ ] Explain the difference between WHERE and HAVING
- [ ] Read a query plan — understand what a sequential scan vs index scan means

**Practice resource:** [sqlzoo.net](https://sqlzoo.net) or [mode.com/sql-tutorial](https://mode.com/sql-tutorial)

### PySpark — basics
- [ ] Create a SparkSession, load a CSV into a DataFrame
- [ ] Use `select`, `filter`, `withColumn`, `groupBy`, `agg`
- [ ] Write a window function using `Window.partitionBy`
- [ ] Write output to parquet — understand why parquet vs CSV
- [ ] Understand lazy evaluation — what's the difference between a transformation and an action

### DE system design — one topic per week
- [ ] Batch vs streaming — tradeoffs, when to use each
- [ ] Idempotency — how to design pipelines that are safe to rerun
- [ ] Partitioning — by date, by key, why it matters for query performance
- [ ] Schema evolution — backward/forward compatibility, Avro vs Parquet
- [ ] Data modelling — star schema, snowflake, one big table, when to denormalise
- [ ] Pipeline reliability — dead letter queues, retry logic, exactly-once semantics
- [ ] Medallion architecture — raw / staged / curated layers and why
- [ ] Orchestration — Airflow DAG design, backfill, SLAs
- [ ] Data quality — validation in pipelines, dbt tests, what to alert on

---

## BOOKS

- **DDIA** (Designing Data-Intensive Applications) — Kleppmann. Read alongside DE system design topics.
- **Fluent Python** — Ramalho. Start when you reach MOOC Part 8.
- **Fundamentals of Data Engineering** — Reis & Housley. Pipeline thinking and tooling tradeoffs.

---

## PROBLEM LOG

### Previously completed (pre-reset)

- [x] **Two Sum** (#1) [Easy] — Hashmap — Confidence: 5/10 — Reasoned
- [x] **Valid Anagram** (#242) [Easy] — Hashmap — Confidence: 5/10 — Reasoned
- [x] **Contains Duplicate** (#217) [Easy] — Hashmap — Confidence: 6/10 — Reasoned
- [x] **Valid Parentheses** (#20) [Easy] — Stack — Confidence: 7/10 — Reasoned. 18 min.

---

## LOG

<!-- Append new sessions below -->
