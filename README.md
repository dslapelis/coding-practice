# LeetCode training

Practice repo. One package per problem: the statement lives in `solution.py`'s docstring,
`test_solution.py` is the grader. Red-to-green is the score.

```
uv run pytest              # grade everything
uv run pytest two_sum      # grade one problem
```

## Scoreboard

| Problem | Tests | Approach | Time | Space |
|---|---|---|---|---|
| [Two Sum](two_sum/) | 11 / 11 ✅ | Hash map of value → index, one pass | O(n) | O(n) |
| [Longest Substring Without Repeating Characters](longest_substring/) | 20 / 20 ✅ | Sliding window + last-seen index map | O(n) | O(min(n, charset)) |
| [Product of Array Except Self](product_except_self/) | 16 / 16 ✅ | Prefix × suffix products, two pointers in one loop | O(n) | O(1) extra |

**47 / 47 passing** as of 2026-08-29.

## Log

### Two Sum — 2026-08-28

Solved in one sitting. Two follow-up commits trimmed dead code rather than fixing anything 
— the first version was already correct.

Solves the O(n²) → O(n) step the standard way: check for the complement *before* inserting the
current value, so an element can't pair with itself.

### Longest Substring Without Repeating Characters — 2026-08-28

Committed a working but self-described "not efficient" version first, then came back and
optimized it. That's the right order.

The final version stores each character's *last seen index* rather than a set of characters in
the window, so a repeat jumps `left` straight past the previous occurrence instead of advancing
it one step at a time. The `prev >= left` guard is the subtle part: it ignores stale entries
sitting behind the window rather than dragging `left` backwards.

### Product of Array Except Self — 2026-08-29

Hardest of the three. Went in expecting sliding window; the actual shape is prefix/suffix decomposition, which is a different pattern entirely.

`answer[i] = (product left of i) × (product right of i)` — neither side contains `nums[i]`, which
is how it avoids division. Solved the O(1)-space follow-up too: instead of two sequential passes,
one loop walks index `i` from the left and `n-1-i` from the right, interleaving both traversals.

Two bugs on the way, both worth remembering:

- Assigned to a fresh `accumulator` instead of back into `left_accumulator`, so the left pass
  silently produced all `1`s.
- Merged the two passes but kept `=` for both writes. Interleaved, the writes land in an order
  you don't control, so each one clobbered the other's contribution. Both must be `*=`,
  accumulating into a `[1] * n` seed — multiplication is commutative, so arrival order stops
  mattering.

## Notes on the numbers

Timings come from git commit timestamps, so they're an upper bound on elapsed wall-clock, not
measured solve time — gaps include time away from the keyboard. Only Two Sum has a scaffold
commit separate from its solution commit, so it's the only one with a meaningful span; the other
two were committed as scaffold-plus-solution together. Nothing here is stopwatch data.
