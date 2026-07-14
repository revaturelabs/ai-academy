<!-- nav:top:start -->
[⬅ Previous: 11.4 — Data types](../../11-4-data-types-string-integer-float-boolean/artifacts/reading.md)&emsp;·&emsp;[⬆ Table of Contents](../../../../../../../README.md#curriculum-topic-index)&emsp;·&emsp;[Next: 11.6 — For loops ➡](../../11-6-for-loops-repeating-an-action-across-a-list/artifacts/reading.md)
<!-- nav:top:end -->

---

# If / else — writing decision logic in code

## Overview

In Week 1 you drew flowcharts with decision diamonds — shapes that asked a yes/no question and directed the flow down different paths. This topic shows you how to express that diamond in Python code, using `if`, `elif`, and `else`. You will also meet `input()`, which lets your program pause and collect a value the user types at the keyboard [1][2].

Two limitations from topic 11.4 are resolved here. The hard-coded boolean flag (`passed = True`) and the hard-coded input values (`student_name = "Alice"`) were workarounds because comparison operators and if/else had not yet been introduced. By the end of this topic you will replace both workarounds with real conditional logic — completing the grade-average script that is the week's lab goal.

## Key Concepts

### Comparison operators

A **comparison operator** compares two values and returns a `bool` — either `True` or `False` [3][5]. Python has six comparison operators:

| Operator | Meaning | Example | Result |
|---|---|---|---|
| `==` | Equal to | `5 == 5` | `True` |
| `!=` | Not equal to | `5 != 3` | `True` |
| `<` | Less than | `3 < 5` | `True` |
| `>` | Greater than | `5 > 3` | `True` |
| `<=` | Less than or equal | `5 <= 5` | `True` |
| `>=` | Greater than or equal | `6 >= 5` | `True` |

The most important rule to remember: `=` is the **assignment** operator (it stores a value in a variable), while `==` is the **equality test** (it asks whether two values are the same) [1][2]. Writing `if mark = 88:` is a syntax error — always use `==` inside a condition.

```python
average = 83.7
passed = average >= 60.0    # comparison produces True
print(passed)               # True
```

### The `if` / `else` structure

![if / elif / else — Grade Assignment](artifacts/diagram.png)

The `if` statement tells Python: run the indented block only when the condition is `True`. Add `else:` for the path to take when the condition is `False` [1][2][4]:

```python
average = 83.7
if average >= 60.0:
    print("Pass")
else:
    print("Fail — please resubmit")
```

Three syntax rules apply to every `if` statement:

1. **Colon required** — the `if` line (and each `elif`/`else` line) must end with `:`.
2. **Indentation** — the body of each branch must be indented by 4 spaces [1][2]. Python uses indentation to define code blocks rather than curly braces like many other languages. Every line inside a block must be indented consistently; mixing tabs and spaces causes an `IndentationError`.
3. **One branch runs** — Python evaluates the condition and runs exactly one branch, never both.

### `elif` — multiple mutually exclusive paths

`elif` (short for "else if") extends the decision chain beyond two paths [1][2][4]. Python evaluates conditions **top to bottom** and runs only the first branch whose condition is `True`, then skips all remaining branches:

```python
if average >= 90:
    grade = "A"
elif average >= 80:
    grade = "B"
elif average >= 70:
    grade = "C"
elif average >= 60:
    grade = "D"
else:
    grade = "F"
```

**Order is critical.** If you put `average >= 60` at the top, every student with a passing mark would receive "D" — the program would never reach the higher-grade branches. Always write the most restrictive condition first [2]. You can have as many `elif` branches as needed; the final `else` catches every case that was not caught above.

### Compound conditions

Comparison expressions combine with `and`, `or`, and `not` (introduced in 11.4) to express compound conditions [1][3][5]. The operands are now comparison results rather than pre-assigned boolean variables — everything else works the same way:

```python
average = 72.0
attendance = 85
if average >= 60 and attendance >= 80:
    print("Eligible for certificate")
else:
    print("Requirement not met")
```

### `input()` — reading values from the user

`input(prompt)` pauses the program, displays the prompt text, waits for the user to type something and press Enter, and returns what they typed as a **string** [1][2]. Because the return type is always `str`, you must convert immediately before doing any arithmetic:

```python
student_name = input("Enter student name: ")
mark = int(input("Enter mark (0-100): "))   # convert str → int in one step
```

If the user types text that cannot be converted — for example, "abc" when you call `int()` — Python raises an error. For now, assume the user types valid numbers; handling invalid input requires loops, introduced in 11.6.

## Worked Example

The complete grade-average script assembles every concept from topics 11.3–11.5:

```python
# Inputs from the user

<!-- nav:top:start -->
[⬅ Previous: 11.4 — Data types](../../11-4-data-types-string-integer-float-boolean/artifacts/reading.md)&emsp;·&emsp;[⬆ Table of Contents](../../../../../../../README.md#curriculum-topic-index)&emsp;·&emsp;[Next: 11.6 — For loops ➡](../../11-6-for-loops-repeating-an-action-across-a-list/artifacts/reading.md)
<!-- nav:top:end -->

---
student_name = input("Student name: ")
mark1 = int(input("Mark 1 (0-100): "))
mark2 = int(input("Mark 2 (0-100): "))
mark3 = int(input("Mark 3 (0-100): "))

# Compute average

<!-- nav:top:start -->
[⬅ Previous: 11.4 — Data types](../../11-4-data-types-string-integer-float-boolean/artifacts/reading.md)&emsp;·&emsp;[⬆ Table of Contents](../../../../../../../README.md#curriculum-topic-index)&emsp;·&emsp;[Next: 11.6 — For loops ➡](../../11-6-for-loops-repeating-an-action-across-a-list/artifacts/reading.md)
<!-- nav:top:end -->

---
total = mark1 + mark2 + mark3
average = total / 3
average_rounded = round(average, 1)

# Assign letter grade

<!-- nav:top:start -->
[⬅ Previous: 11.4 — Data types](../../11-4-data-types-string-integer-float-boolean/artifacts/reading.md)&emsp;·&emsp;[⬆ Table of Contents](../../../../../../../README.md#curriculum-topic-index)&emsp;·&emsp;[Next: 11.6 — For loops ➡](../../11-6-for-loops-repeating-an-action-across-a-list/artifacts/reading.md)
<!-- nav:top:end -->

---
if average_rounded >= 90:
    grade = "A"
elif average_rounded >= 80:
    grade = "B"
elif average_rounded >= 70:
    grade = "C"
elif average_rounded >= 60:
    grade = "D"
else:
    grade = "F"

# Display result

<!-- nav:top:start -->
[⬅ Previous: 11.4 — Data types](../../11-4-data-types-string-integer-float-boolean/artifacts/reading.md)&emsp;·&emsp;[⬆ Table of Contents](../../../../../../../README.md#curriculum-topic-index)&emsp;·&emsp;[Next: 11.6 — For loops ➡](../../11-6-for-loops-repeating-an-action-across-a-list/artifacts/reading.md)
<!-- nav:top:end -->

---
print(student_name + " averaged " + str(average_rounded) + " — Grade: " + grade)
```

Sample run (user input appears after each prompt):
```
Student name: Alice
Mark 1 (0-100): 88
Mark 2 (0-100): 72
Mark 3 (0-100): 91
Alice averaged 83.7 — Grade: B
```

Line-by-line notes:
- `int(input(...))` — the user types a string; `int()` converts it to an integer before addition (from 11.4).
- `total / 3` — integer divided by integer gives a float in Python 3 (from 11.4).
- `elif average_rounded >= 80` fires because `83.7 >= 90` is `False` and `83.7 >= 80` is `True`.
- `str(average_rounded)` — converts `83.7` to `"83.7"` for the concatenation (from 11.4) [1][3].

Common errors:
- **`SyntaxError` on the `if` line** — you wrote `=` instead of `==` inside the condition.
- **`IndentationError`** — the block body is not indented, or tabs and spaces are mixed.
- **Every mark gets grade "D"** — the `>= 60` branch is above `>= 80` in the chain.

## In Practice

**AI scoring pipelines.** Sentiment classifiers output a float confidence score between 0.0 and 1.0. An if/elif chain labels the result: `positive` if ≥ 0.7, `neutral` if ≥ 0.4, `negative` otherwise [2][5]. This is structurally identical to the grade-assignment pattern above — the thresholds and labels change, the if/elif/else logic does not.

**Range validation.** Before using a user-supplied number in arithmetic, production code verifies it is within the expected range. A range check looks like `if mark < 0 or mark > 100: print("Invalid.")`. Retrying until the user enters a valid value requires a loop, introduced in 11.6 [2].

**Flowchart to code.** The discipline of sketching the decision diamond on paper first — labelling each branch with the condition and the action — and then translating each diamond into an `if`/`elif` line is the core of the spec-first approach introduced in 11.7. Drawing before coding catches logical errors (wrong order, missing branches) before you write a single line [1].

## Key Takeaways

- The six comparison operators produce a `bool`; `==` tests equality while `=` assigns — mixing them up is a syntax error [1][3].
- `if condition:` runs an indented block when the condition is `True`; Python uses 4-space indentation, not curly braces [1][2].
- `elif` chains evaluate top to bottom; put the most restrictive condition first [1][2].
- Comparison expressions combine with `and`, `or`, and `not` to form compound conditions [3][5].
- `input()` always returns a `str`; convert with `int()` or `float()` before arithmetic or comparison [1][2].

## References

1. Python Software Foundation. *Control Flow Tools*. https://docs.python.org/3/tutorial/controlflow.html
2. Real Python. *Conditional Statements in Python*. https://realpython.com/python-conditional-statements/
3. Python Software Foundation. *Comparisons — Built-in Types*. https://docs.python.org/3/library/stdtypes.html#comparisons
4. W3Schools. *Python Conditions*. https://www.w3schools.com/python/python_conditions.asp
5. Real Python. *Operators and Expressions in Python*. https://realpython.com/python-operators-expressions/

---
<!-- nav:bottom:start -->
[⬅ Previous: 11.4 — Data types](../../11-4-data-types-string-integer-float-boolean/artifacts/reading.md)&emsp;·&emsp;[⬆ Table of Contents](../../../../../../../README.md#curriculum-topic-index)&emsp;·&emsp;[Next: 11.6 — For loops ➡](../../11-6-for-loops-repeating-an-action-across-a-list/artifacts/reading.md)
<!-- nav:bottom:end -->
