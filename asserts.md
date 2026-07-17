# Asserts — The Whole Skill

**Last updated:** 2026-06-11

The syntax is one line. The skill is choosing what to test. This is what failed at Millennium — not the algorithm, the verification.

## Syntax (memorise this, it's all there is)

```python
assert two_sum([3, 9, 12, 7], 19) == [2, 3], f"got {two_sum([3, 9, 12, 7], 19)}"
```

- `assert <expression that should be True>, <message shown if it isn't>`
- Passing = silence. Failing = `AssertionError` with your message.
- The f-string message is what makes failures debuggable — always include the actual output.
- Cleaner form when you'd otherwise call the function twice:

```python
result = two_sum([3, 9, 12, 7], 19)
assert result == [2, 3], f"got {result}"
print("all tests passed")   # so silence is distinguishable from 'didn't run'
```

## The three-case minimum (every problem, every time)

1. **The example case** — straight from the problem statement. Proves the happy path.
2. **The degenerate case** — empty input, single element, or both. Most index errors live here.
3. **The "no" case** — input where the answer is False/empty/None. Solutions that always return something true-ish pass cases 1–2 and fail this.

```python
assert is_valid("({[]})") == True
assert is_valid("") == True          # degenerate: empty string IS valid
assert is_valid("(]") == False       # the "no" case
```

Then add problem-specific traps: duplicates, all-identical elements, negatives, target at the boundary, already-sorted/reverse-sorted.

## Gotchas that waste interview minutes

- `[0, 1] != (0, 1)` — list vs tuple comparison fails. Match the expected type.
- If order is unspecified, compare sorted: `assert sorted(result) == sorted(expected)`.
- Floats: `assert abs(result - 0.3) < 1e-9`, never `==`.
- If your function mutates its input, a reused test list carries state between asserts. Fresh literal per assert.

## Drill (do this until it's reflex)

In every problem from now on, **write the three asserts before the function body** — signature first, asserts second, implementation third. Run them, watch all three fail, then implement until silence + "all tests passed". This is the habit: tests are part of writing the function, not something you bolt on if there's time. In a live interview, saying "let me write a couple of quick asserts" while doing this is a strong signal — it's what they wanted to see at Millennium.
