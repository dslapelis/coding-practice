# LeetCode training repo

Dan uses this repo to practice coding problems. **Dan writes the solutions. You do not.**

## Workflow

When Dan asks for a problem, create a new package for it and produce three things:

1. **The problem statement** — as the module docstring at the top of `<problem>/solution.py`:
   description, examples with expected output, and constraints. If Dan pasted a problem, use
   it verbatim.
2. **The stub** — the class/function signature with a `pass` body, exactly as the problem
   (or Dan) specifies it. Type hints included, no logic, no hints in comments.
3. **The tests** — in `<problem>/test_solution.py`, written to grade the implementation.

Then stop. Dan implements. He runs `uv run pytest`; red-to-green is the grade.

## Hard rules

- **Never write the implementation**, not even a naive or partial one, and not as a comment,
  docstring, or a "here's the idea" note in the response. It spoils the exercise.
- Don't reveal the intended approach or complexity target unless Dan asks. The follow-up
  ("can you do better than O(n²)?") stays in the problem statement — that's the problem's own
  wording, not a hint from you.
- If Dan asks for a hint, give the smallest one that unblocks him. If he asks for the answer
  outright, that's his call — give it.
- When Dan says he's done, run the tests and report what passed and failed. Review the
  approach and complexity if he asks; don't rewrite his code unprompted.
- **Never edit a problem's `solution.py` below the docstring** once Dan has started. That file
  is his. Backfilling the statement or fixing the stub signature is fine; touching his code
  is not.

## Writing the tests

Tests are the grader, so they should be harder than the three examples in the prompt.

- Cover: the given examples, minimum-size input, negatives and zero, duplicates that are
  *not* the answer, the answer at both ends of the input, the stated constraint bounds, and
  a large input sized to the constraints (a naive brute force should time out or drag).
- Validate the *property*, not one blessed output, whenever the problem allows multiple valid
  answers ("return in any order", any valid path, etc.). Route those through a `check()`
  helper that asserts the answer is well-formed and correct, then normalizes it for
  comparison — see `two_sum/test_solution.py`.
- Fail loudly on the untouched stub: assert the shape of the return value before unpacking it,
  so a `None` from `pass` reports "expected two indices, got None" instead of a `TypeError`.
- Name tests after what they probe (`test_duplicates_that_are_not_the_answer`), so a failure
  tells Dan which case he broke.

## Layout

One package per problem, named in snake_case after the problem. Nothing is ever overwritten;
new problems sit alongside the old ones.

```
training/
├── CLAUDE.md
├── pyproject.toml
├── uv.lock
└── two_sum/
    ├── __init__.py          # required — makes each problem its own package
    ├── solution.py          # problem statement (docstring) + stub, then Dan's work
    └── test_solution.py     # the grader
```

The `__init__.py` matters: it makes each test module `<problem>.test_solution` rather than a
bare `test_solution`, so every problem can reuse the same two file names without pytest
colliding on them. Tests import absolutely — `from two_sum.solution import Solution` — which
resolves because pytest puts the repo root on `sys.path`. When you scaffold a new problem,
create all three files.

uv project, Python 3.14, pytest as the only dev dependency.

- `uv run pytest` — grade every problem in the repo
- `uv run pytest two_sum` — grade one problem
- `uv run pytest two_sum -q -x` — stop at the first failure
- `uv run pytest two_sum -k zeroes -l` — one test, with locals dumped on failure
- `uv run pytest two_sum -s --pdb` — see prints live; drop into pdb where it breaks
- `uv run python two_sum/solution.py` — run the `__main__` block against the examples
