# Progress Tracker

## Phase 1 Summary (as of 5 April)

**Syntax drills (`01_syntax_drills.ipynb`):** All exercises completed — Lists, Dicts, Sets, Strings, Two Pointers. Cold rewrites of Two Sum, Valid Anagram, and Contains Duplicate done from memory at the end of the notebook. Contains Duplicate rewrite correctly used a set (improvement on the original dict approach).

**Data structures (`02_data_structures.ipynb`):** Stack, Queue, and LinkedList exercises completed from scratch. Binary Tree exercise (inorder traversal, max depth, invert) still to do.

**Gap before Phase 2:** Complete the Binary Tree exercise in `02_data_structures.ipynb` — that's the last stub remaining.

---

## Week 1

### Day 1 — Sunday 30 March
**Completed:**
- [x] Lists syntax drills
- [x] Stack class from scratch
- [x] MinStack with inheritance and super()
- [x] Dunder methods (__len__, __str__, __repr__)
- [x] Two Sum (#1)
- [x] Valid Anagram (#242)
- [x] Contains Duplicate (#217)

**Struggled with:**
- Dict syntax — adding and incrementing keys
- Which end of array is stack top ([-1] not [0])
- seen[complement] vs complement in Two Sum return value

**Confidence scores (1-10):**
- Syntax fluency: 4
- Data structures: 4
- Problem solving: 5
- System design: 3

---

### Day 2 — Monday 31 March
_No session — rest day._

---

### Day 3 — Tuesday 1 April
_No session — rest day._

---

> ### 🔁 Restart Point — Thursday 2 April
> Two days off, no big deal. Day 1 was strong. Pick up exactly where you left off below.

---

### Day 4 — Thursday 2 April ← **RESTART HERE**
**Focus:** Linked Lists + Two Pointers
**Morning drill:** Complete the stub exercises in `02_data_structures.ipynb` (Stack, Queue, LinkedList, Binary Tree) cold before anything else — this is unfinished from Phase 1. Then run through `01_syntax_drills.ipynb` lists/dict section as a warmup.

**Problems to complete:**
- [ ] Reverse Linked List (#206)
- [ ] Valid Palindrome (#125)

**Approach:**
- 15 min minimum per problem before looking at anything
- After attempting, check `phase1_foundations/02_data_structures.ipynb` for linked list patterns if stuck

**Completed:**
- [x] Stack exercise (`02_data_structures.ipynb`)
- [x] Queue exercise (`02_data_structures.ipynb`)
- [x] LinkedList exercise (`02_data_structures.ipynb`)

**Struggled with:**
-

---

### Day 5 — Friday 3 April
**Focus:** Sliding Window
**Problems:** Best Time to Buy and Sell Stock (#121), Maximum Subarray (#53)

**Completed:**
-

**Struggled with:**
-

---

### Day 6 — Saturday 4 April
**Focus:** Hashmaps deep dive
**Problems:** Group Anagrams (#49), Top K Frequent Elements (#347)

**Completed:**
-

**Struggled with:**
-

---

### Day 7 — Sunday 5 April (Review Day)
**Cold rewrites — did these from memory with no notes:**
-

**What still needs work:**
-

---

## Week 2

### Day 8 — Monday 6 April
**Focus:** Stacks + Queues
**Problems:** Valid Parentheses (#20), Min Stack (#155)

**Completed:**
-

### Day 9 — Tuesday 7 April
**Focus:** Binary Search
**Problems:** Binary Search (#704), Search in Rotated Sorted Array (#33)

**Completed:**
-

### Day 10 — Wednesday 8 April
**Focus:** Trees BFS/DFS
**Problems:** Invert Binary Tree (#226), Max Depth of Binary Tree (#104), Level Order Traversal (#102)

**Completed:**
-

### Day 11 — Thursday 9 April
**Focus:** Dynamic Programming intro
**Problems:** Climbing Stairs (#70), House Robber (#198)

**Completed:**
-

### Day 12 — Friday 10 April
**Focus:** Timed sessions (30 min each)
**Problems:** 3x medium problems of your choice

**Completed:**
-

### Day 13 — Saturday 11 April
**Focus:** Timed sessions + SQL/Pandas
**Problems:** 2x medium + window functions

**Completed:**
-

### Day 14 — Sunday 12 April — Full Mock + Point72 Prep
**Focus:** Full mock interview simulation + Cap IQ walkthrough
**Problems:** 2 problems, 45 mins each

**Completed:**
-

---

## BofA Round 2 Prep — 2026-05-15 to 2026-05-21

**Format:** Two live coding interviews with IDE. Cristina (FX Pre-Trade) Wed 14:30, Laura (Commodities Pre-Trade) Thu 13:00.

**Goal:** Pattern recognition + clean reasoning out loud. Not memorised solutions — understood patterns you can reconstruct and explain.

**How to use this plan:**
1. Watch the Neetcode video first (neetcode.io — each problem has a video)
2. Close the video and attempt the problem cold
3. If stuck after 15 minutes, re-watch, then attempt again
4. Log confidence honestly below

---

### Saturday 2026-05-17 — Warm up + Arrays & Hashing

**First — drill the scaffold and testing pattern (do this once before anything else):**

Before touching any problem, practice writing this from muscle memory in under 60 seconds. This is your interview boilerplate — scaffold first, logic second.

```python
class Solution:
    def method_name(self, input):
        pass


if __name__ == "__main__":
    solution = Solution()

    # test 1 — basic happy path
    assert solution.method_name(...) == ..., "basic case failed"

    # test 2 — edge case (empty, single element, duplicates, negatives)
    assert solution.method_name(...) == ..., "edge case failed"

    # test 3 — boundary (answer at first/last position, zero result)
    assert solution.method_name(...) == ..., "boundary case failed"

    print("all tests passed")
```

**Why asserts over prints:** if a test fails, it tells you exactly which case broke and why. Prints just dump output you have to manually verify — same habit you've had at work. Break it here.

**What to say out loud in the interview:** "Before I start I'll write a few test cases so I know what I'm building toward." Write them first. It reframes the whole thing — you're engineering toward a known target, not scrambling to a solution.

**Three cases every time:**
1. Basic happy path — normal input, expected output
2. Edge case — empty list, single element, duplicates, negative numbers
3. Boundary — answer at index 0 or last index, result is zero or None

**In a Jupyter notebook:** use the same assert pattern in a cell. Run the cell after implementing — if it executes silently, all tests passed. If it throws an AssertionError, you see exactly which case failed.

---

**Morning — cold rewrites first (already done, no notes):**
- [ ] **Two Sum** (#1) — cold rewrite, target <10 min ✅
- [ ] **Contains Duplicate** (#217) — cold rewrite using a set, target <5 min ✅
- [ ] **Valid Parentheses** (#20) — cold rewrite, target <10 min ✅

**Then new problems:**

Pattern: use a hashmap to trade O(n²) brute force for O(n). Watch video → attempt cold → log.

- [ ] **Group Anagrams** (#49) [Medium] — neetcode.io/problems/anagram-groups
  - Pattern: Hashmap — sort each word as a key, group words with matching keys
  - Why it matters: classic "group by computed property" pattern, comes up constantly ✅

- [ ] **Top K Frequent Elements** (#347) [Medium] — neetcode.io/problems/top-k-elements-in-list
  - Pattern: Hashmap + bucket sort (or heap)
  - Why it matters: frequency counting is a core pattern, the bucket sort approach is elegant 

---

### Sunday 2026-05-18 — Two Pointers

Pattern: two pointers moving toward each other or at different speeds to avoid nested loops.

- [ ] **Valid Palindrome** (#125) [Easy] — neetcode.io/problems/is-palindrome
  - Pattern: Two Pointers — left and right moving inward, skip non-alphanumeric
  - Why it matters: simple intro to the pattern, tests string handling in Python

- [ ] **3Sum** (#15) [Medium] — neetcode.io/problems/three-integer-sum
  - Pattern: Sort + Two Pointers — fix one element, use two pointers for the rest
  - Why it matters: harder two-pointer, tests whether you can reason about duplicates

---

### Monday 2026-05-19 — Sliding Window

Pattern: maintain a window over a sequence, expand/shrink it to track a condition. Avoids O(n²) nested loops.

- [ ] **Best Time to Buy and Sell Stock** (#121) [Easy] — neetcode.io/problems/buy-and-sell-crypto
  - Pattern: Sliding Window — track min price seen so far, compute max profit
  - Why it matters: simplest sliding window, good for getting the pattern in your head

- [ ] **Longest Substring Without Repeating Characters** (#3) [Medium] — neetcode.io/problems/longest-substring-without-duplicates
  - Pattern: Sliding Window + Hashset — shrink window when duplicate found
  - Why it matters: combines sliding window with a set, very common interview problem

---

### Tuesday 2026-05-20 — Stack + revision

Morning: one new problem. Evening: cold rewrites of everything from the week.

- [ ] **Min Stack** (#155) [Medium] — neetcode.io/problems/minimum-stack
  - Pattern: Stack — maintain a second stack tracking current minimum
  - Why it matters: tests whether you can think about auxiliary data structures

**Evening — cold rewrites (pick any 3 from the week, no notes):**
- [ ] Pick 3, reconstruct from scratch, log time

---

### Wednesday 2026-05-21 morning — Light review only

No new problems. Read through your solutions from the week. Make sure you can say out loud for each one: what pattern is this, why does it work, what's the time and space complexity.

Interview at 14:30. Stop all prep by 13:00. Eat something.

---

### Interview approach — live coding

1. **Read the problem twice** before touching the keyboard
2. **Say the pattern out loud** — "I think this is a sliding window because..."
3. **Write pseudocode first** — talk through it before coding
4. **State complexity** when you finish — time and space
5. **Test with an example** — walk through your code with a simple input

If you're stuck: "Can I take a moment to think?" is fine. Silence while thinking is fine. Bluffing a wrong approach wastes more time.

---

<!-- DB_GENERATED_BELOW -->

# Problems Log — Last updated: 2026-04-23

## Summary
- **Total problems logged:** 4
- **Patterns covered:** Hashmap, Stack
- **Average confidence:** 5.8/10
- **Last session:** 2026-04-23

---

### 2026-03-30
- [x] **Two Sum** (#1) [Easy] — Hashmap — Confidence: 5/10
  - 🟡 Reasoned
  - Notes: Tripped up on seen[complement] vs complement in return value. Recalled dict pattern but got the return wrong first.
- [x] **Valid Anagram** (#242) [Easy] — Hashmap — Confidence: 5/10
  - 🟡 Reasoned
  - Notes: Dict syntax issues — adding and incrementing keys. Got there through reasoning.
- [x] **Contains Duplicate** (#217) [Easy] — Hashmap — Confidence: 6/10
  - 🟡 Reasoned
  - Notes: Cold rewrite used a set (improvement on original dict approach). Cleaner solution.

### 2026-04-23
- [x] **Valid Parentheses** (#20) [Easy] — Stack — Confidence: 7/10
  - 🟡 Reasoned | Time: 18 min
