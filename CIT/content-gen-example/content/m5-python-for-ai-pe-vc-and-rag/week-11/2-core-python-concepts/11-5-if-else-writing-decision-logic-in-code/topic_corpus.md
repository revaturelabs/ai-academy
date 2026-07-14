---
topic_id: "11.5"
title: "If / else — writing decision logic in code"
position_in_module: 3
generated_at: "2026-06-12T01:00:00Z"
resource_count: 5
---

# 1. If / else — writing decision logic in code — Topic Corpus

## 2. Prerequisites

This topic builds on all four topics that came before it in this module. From 11.3 you have variables and the four basic types (`str`, `int`, `float`, `bool`). From 11.4 you have `print()`, arithmetic operators, `round()`, `str()` for type conversion, and boolean `and`/`or`/`not`. One concept was explicitly deferred from 11.4: **comparison operators** — the symbols that compare two values and produce a `True` or `False` result. That deferral is resolved here.

You also need the Colab environment (11.2) and an understanding of what a program is (11.1). If you can write multi-line code cells in Colab and are comfortable with variables and the four basic types, you are ready.

## 3. Learning Objectives

By the end of this topic you will be able to:

- Write a comparison expression using `==`, `!=`, `<`, `>`, `<=`, or `>=` and explain what boolean value it produces.
- Write an `if` / `else` block in Python, following the indentation rule, and predict its output for a given input.
- Write an `elif` chain to test multiple mutually exclusive conditions — for example, assigning a letter grade to a numeric average.
- Combine comparison expressions with `and`, `or`, and `not` to express compound conditions.
- Use `input()` to read a value from the user and convert it with `int()` or `float()` before using it in arithmetic or comparisons.

## 4. Introduction

In Week 1 you drew flowcharts with decision diamonds — a shape that asked a yes/no question and directed the flow down different paths. `if`/`else` is how you express that decision diamond in Python code [1][2].

Look at the grade-average script you have been building across this week. In 11.4 you hard-coded the inputs (`student_name = "Alice"`, `mark1 = 88`, ...) and used a hard-coded boolean flag (`passed = True`) because comparison operators had not been introduced yet. This topic removes both of those limitations:

- Comparison operators let you write `average >= 60.0` and get `True` or `False` automatically.
- `input()` replaces hard-coded values with values the user types at runtime.
- `if`/`elif`/`else` branches the program: print one message when the average is >= 90, a different message when it is >= 80, and so on.

By the end of this topic you will have every piece needed to write the complete grade-average script for this week's lab [1].

## 5. Core Concepts

### 5.1 Comparison operators

A **comparison operator** compares two values and produces a `bool` — either `True` or `False` [3][5]. Python has six [1][3]:

| Operator | Meaning | Example | Result |
|----------|---------|---------|--------|
| `==` | Equal to | `5 == 5` | `True` |
| `!=` | Not equal to | `5 != 3` | `True` |
| `<` | Less than | `3 < 5` | `True` |
| `>` | Greater than | `5 > 3` | `True` |
| `<=` | Less than or equal to | `5 <= 5` | `True` |
| `>=` | Greater than or equal to | `6 >= 5` | `True` |

```python
average = 83.7
passed = average >= 60.0
print(passed)           # True
print(type(passed))     # <class 'bool'>
```

**Critical distinction: `==` vs `=`**

This is the most common error beginners make with conditions [1][2]:

- `=` is the **assignment** operator: `mark = 88` stores 88 in `mark`.
- `==` is the **equality test**: `mark == 88` asks "is mark equal to 88?" and produces `True` or `False`.

Writing `if mark = 88:` is a **SyntaxError** — always use `==` inside conditions.

### 5.2 The `if` statement — single-path decision

The `if` statement tells Python: run these lines only if the condition is True [1][2][4]:

```python
average = 83.7
if average >= 60.0:
    print("Pass")
```

Three things to notice:

1. **The condition** (`average >= 60.0`) is any expression that evaluates to `True` or `False`.
2. **The colon** (`:`) at the end of the `if` line is required — Python raises a `SyntaxError` without it.
3. **Indentation** — the body of the `if` block is indented by 4 spaces [1][2]. Python uses indentation to define blocks; it does not use curly braces. Every line inside the block must be indented consistently.

```python
# Both print() calls are inside the if block
if average >= 60.0:
    print("Pass")
    print("Well done!")

# This print() is outside — runs regardless
print("Processing complete")
```

#### The `else` clause

`else:` provides the path to take when the condition is `False` [1][2][4]:

```python
average = 45.0
if average >= 60.0:
    print("Pass")
else:
    print("Fail — please resubmit")
```

Python evaluates the condition and runs exactly one of the two branches — never both.

### 5.3 `elif` — multiple mutually exclusive conditions

`elif` (short for "else if") extends the chain to handle more than two paths [1][2][4]. Python evaluates conditions **top to bottom** and runs only the first branch whose condition is `True`, then skips all remaining branches:

```python
average = 83.7

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

print("Grade:", grade)    # Grade: B
```

Tracing through for `average = 83.7`:

- `83.7 >= 90` → `False` — skip.
- `83.7 >= 80` → `True` — assign `"B"`, skip all remaining branches.

**Order matters.** If you place `average >= 60` first, every student with a passing average would receive `"D"` and no higher grade could be reached. Always write the most restrictive condition at the top [2].

### 5.4 Compound conditions

Comparison expressions can be combined with `and`, `or`, and `not` (introduced in 11.4) to form **compound conditions** [1][3][5]:

```python
average = 72.0
attendance = 85

if average >= 60 and attendance >= 80:
    print("Eligible for certificate")
else:
    print("Requirement not met")
```

`and` requires both conditions to be `True`. `or` requires at least one. `not` inverts a boolean. These are the same operators from 11.4 — the only new element is that the operands are now comparison expressions rather than pre-assigned boolean variables.

### 5.5 `input()` — reading values from the user

`input(prompt)` pauses the program, displays `prompt`, waits for the user to type something and press Enter, and returns what they typed as a **string** [1][2]:

```python
student_name = input("Enter student name: ")
print("Hello,", student_name)
```

**The return value is always a `str`.** Convert before arithmetic:

```python
mark = int(input("Enter mark (0-100): "))   # str → int in one step
```

If the user types something that cannot be converted — typing `"abc"` when you call `int()` — Python raises a `ValueError`. Validating user input (retrying until a valid value is entered) uses loops, introduced in 11.6. For now, assume the user types valid numbers.

## 6. Implementation

### Complete grade-average script

The snippet below combines every concept from topics 11.3 to 11.5 into the script the lab asks you to build:

```python
# --- Inputs from the user ---
student_name = input("Student name: ")
mark1 = int(input("Mark 1 (0-100): "))
mark2 = int(input("Mark 2 (0-100): "))
mark3 = int(input("Mark 3 (0-100): "))

# --- Compute average ---
total = mark1 + mark2 + mark3
average = total / 3
average_rounded = round(average, 1)

# --- Assign letter grade ---
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

# --- Display result ---
result = student_name + " averaged " + str(average_rounded) + " — Grade: " + grade
print(result)
```

Sample run (user input shown after each prompt):
```
Student name: Alice
Mark 1 (0-100): 88
Mark 2 (0-100): 72
Mark 3 (0-100): 91
Alice averaged 83.7 — Grade: B
```

### Common errors

**`SyntaxError: invalid syntax` on the `if` line** — you wrote `=` (assignment) instead of `==` (comparison) inside the condition.

**`IndentationError: expected an indented block`** — the body of the `if` is not indented, or tabs and spaces are mixed.

**`ValueError: invalid literal for int() with base 10`** — the user typed text that cannot be parsed as an integer. Re-run and type a valid number.

**Unexpected grade assignment** — every mark above 60 is being graded "D": check that your most restrictive condition (`>= 90`) is at the top of the elif chain.

## 7. Real-World Patterns

### if/elif in AI scoring pipelines

AI pipelines route items based on a score [2][5]. A sentiment classifier outputs a float between 0 and 1, and an if/elif chain labels it: `positive` if >= 0.7, `neutral` if >= 0.4, `negative` otherwise. This is structurally identical to the grade-assignment pattern. The threshold values and branch actions differ; the if/elif/else logic is the same.

### Range checking in data validation

Before doing arithmetic on user-supplied values, production code checks that the value is in a valid range [2]:

```python
if mark < 0 or mark > 100:
    print("Mark must be between 0 and 100.")
```

You have all the tools to write this check now. Retrying until the user enters a valid value uses a loop — introduced in 11.6.

### Connecting flowcharts to code

Every if/elif/else block maps directly to a decision diamond in a flowchart [1]. Drawing the flowchart first — labelling each branch — and then translating each diamond into an `if`/`elif`/`else` block line by line is the core of the spec-first approach introduced in 11.7.

## 8. Best Practices

- **Use `elif` (not chained `if`) for mutually exclusive cases.** Three separate `if` statements run all three checks regardless of which one matched — you could assign `grade` multiple times and end up with the last matching value [2].
- **Put the most restrictive condition first in any elif chain.** A less restrictive condition placed earlier catches cases that should have gone to a more specific branch.
- **`==` inside conditions, `=` for assignment.** A quick rule: `=` gives a value to a variable; `==` asks a yes/no question about values.
- **Name intermediate comparison results for clarity.** `eligible = average >= 60 and attendance >= 80` followed by `if eligible:` is more readable than a long compound condition on one line.
- **Convert `input()` immediately.** `mark = int(input("..."))` makes the type obvious at a glance — cleaner than storing as a string and converting later.

## 9. Hands-On Exercise

Open a new code cell in Colab and write a grade classifier without looking at Section 6:

1. Use `input()` to read a student's name.
2. Use `input()` + `int()` to read one exam mark (0–100).
3. Write an `if`/`elif`/`else` chain:
   - `"Distinction"` for marks >= 75
   - `"Credit"` for marks >= 60
   - `"Pass"` for marks >= 50
   - `"Fail"` for anything below 50
4. Print `"<name>: <grade>"` using string concatenation.

Expected output (for "Bob" with mark 67):
```
Bob: Credit
```

## 10. Key Takeaways

- The six comparison operators (`==`, `!=`, `<`, `>`, `<=`, `>=`) compare two values and produce a `bool`; `==` tests equality while `=` assigns a value — mixing them up is a `SyntaxError` [1][3].
- `if condition:` followed by an indented block runs that block only when the condition is `True`; Python defines code blocks by indentation, not curly braces [1][2].
- `elif` chains test conditions top to bottom and execute only the first `True` branch — write the most restrictive condition first [1][2].
- Comparison expressions combine with `and`, `or`, and `not` to form compound conditions [3][5].
- `input()` always returns a `str`; convert immediately with `int()` or `float()` before arithmetic or comparison [1][2].

## 11. Next Steps

_System-derived from the next entry in curriculum/sequence.md._
