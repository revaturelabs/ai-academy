<!-- nav:top:start -->
[⬅ Previous: 11.3 — Variables](../../11-3-variables-naming-and-storing-values/artifacts/reading.md)&emsp;·&emsp;[⬆ Table of Contents](../../../../../../../README.md#curriculum-topic-index)&emsp;·&emsp;[Next: 11.5 — If / else ➡](../../11-5-if-else-writing-decision-logic-in-code/artifacts/reading.md)
<!-- nav:top:end -->

---

# Data types — string, integer, float, boolean

## Overview

In the previous topic, you learned that every value in Python carries a type. You stored values in variables and used `type()` to inspect them. But storing values is only half the picture — you also need to **do things** with them: display results on screen, add numbers together, join text, and decide whether a condition is true or false.

This topic equips you with the operations each type supports. You will meet `print()` — the function that makes any value visible in the output area — and learn the specific things you can do with strings, integers, floats, and booleans. You will also learn how to convert values between types when an operation requires it. By the end, you will have every tool needed to build the grade-average script that is the focus of this week's lab [3].

## Key Concepts

### The `print()` function

A variable stores a value in memory, but that value stays invisible until you explicitly ask Python to show it [5]. In a Colab code cell, only the last expression is displayed automatically — `print()` is how you display any value, anywhere, at any point in your code.

```python
student_name = "Alice"
average_mark = 84.0
print("Student:", student_name, "Average:", average_mark)
# Student: Alice Average: 84.0

<!-- nav:top:start -->
[⬅ Previous: 11.3 — Variables](../../11-3-variables-naming-and-storing-values/artifacts/reading.md)&emsp;·&emsp;[⬆ Table of Contents](../../../../../../../README.md#curriculum-topic-index)&emsp;·&emsp;[Next: 11.5 — If / else ➡](../../11-5-if-else-writing-decision-logic-in-code/artifacts/reading.md)
<!-- nav:top:end -->

---
```

Passing multiple arguments separated by commas causes `print()` to display them with a space between each [5].

### Strings

A **string** (`str`) is a sequence of characters enclosed in single or double quotes [1][4].

**Concatenation** joins two strings with `+`:

```python
first_name = "Alice"
greeting = "Hello, " + first_name
print(greeting)   # Hello, Alice
```

`+` only works between two strings — if one side is a number, Python raises a `TypeError`. The fix is type conversion, covered below.

**`len()`** returns the number of characters as an integer [1][4]:

```python
print(len("Alice"))   # 5
```

**Indexing** accesses a single character by its zero-based position [1][4]:

```python
name = "Alice"
print(name[0])   # A   (first character)
print(name[4])   # e   (fifth character)
```

Position 0 is always the first character — Python counts from zero throughout.

### Integer arithmetic

Python's `int` supports six arithmetic operators [2][3]:

| Operator | Meaning | Example | Result |
|---|---|---|---|
| `+` | Addition | `88 + 72` | `160` |
| `-` | Subtraction | `91 - 10` | `81` |
| `*` | Multiplication | `3 * 30` | `90` |
| `//` | Floor division | `251 // 3` | `83` |
| `%` | Modulo (remainder) | `251 % 3` | `2` |
| `**` | Exponentiation | `2 ** 8` | `256` |

**Floor division** (`//`) divides and discards the remainder, giving a whole number [2]. **Modulo** (`%`) gives only the remainder. These two operators are used together whenever you need to split a total into groups.

### Float precision

A `float` is a number with a decimal point. One surprising behaviour catches every new programmer [3]:

```python
print(0.1 + 0.2)   # 0.30000000000000004
```

This is not a Python bug. Computers store numbers in binary, and `0.1` has no exact binary representation — the stored value is very slightly off. When you add two approximate values, the tiny errors accumulate [2][3]. Use `round()` to control precision before display:

```python
average = (88 + 72 + 91) / 3   # 83.666...
print(round(average, 1))        # 83.7
```

### Booleans and logical operators

A **boolean** (`bool`) holds `True` or `False`. Three operators let you combine boolean values [1][3]:

- **`and`** — `True` only when both sides are `True`
- **`or`** — `True` when at least one side is `True`
- **`not`** — flips a boolean: `True` becomes `False`, `False` becomes `True`

```python
passed_exam = True
attendance_ok = True
eligible = passed_exam and attendance_ok
print(eligible)   # True
```

Connecting booleans to calculated results — checking whether a mark is above a threshold — is introduced in topic 11.5.

### Type conversion

The four conversion functions convert values between types [1][3]:

| Function | Converts to | Most common use |
|---|---|---|
| `str(x)` | `str` | Turn a number into text before using `+` |
| `int(x)` | `int` | Drop decimals; parse a digit string |
| `float(x)` | `float` | Make a whole number decimal-aware |
| `bool(x)` | `bool` | Test whether a value is "truthy" |

`str()` is the one you will reach for most often — if you try `"Average: " + 83.7`, Python raises a `TypeError`. Wrap the number in `str()` first.

`bool()` follows a simple rule: `0`, `0.0`, and `""` (empty string) are `False`; everything else is `True` [1][3].

## Worked Example

The snippet below assembles everything from this topic into a single grade-average calculation:

```python
# Inputs (user input is covered in 11.5)

<!-- nav:top:start -->
[⬅ Previous: 11.3 — Variables](../../11-3-variables-naming-and-storing-values/artifacts/reading.md)&emsp;·&emsp;[⬆ Table of Contents](../../../../../../../README.md#curriculum-topic-index)&emsp;·&emsp;[Next: 11.5 — If / else ➡](../../11-5-if-else-writing-decision-logic-in-code/artifacts/reading.md)
<!-- nav:top:end -->

---
student_name = "Alice"
mark1 = 88
mark2 = 72
mark3 = 91

# Integer arithmetic

<!-- nav:top:start -->
[⬅ Previous: 11.3 — Variables](../../11-3-variables-naming-and-storing-values/artifacts/reading.md)&emsp;·&emsp;[⬆ Table of Contents](../../../../../../../README.md#curriculum-topic-index)&emsp;·&emsp;[Next: 11.5 — If / else ➡](../../11-5-if-else-writing-decision-logic-in-code/artifacts/reading.md)
<!-- nav:top:end -->

---
total = mark1 + mark2 + mark3       # 251
average = total / 3                 # 83.666... (int ÷ int gives float in Python 3)
average_rounded = round(average, 1) # 83.7

# Type conversion for the output string

<!-- nav:top:start -->
[⬅ Previous: 11.3 — Variables](../../11-3-variables-naming-and-storing-values/artifacts/reading.md)&emsp;·&emsp;[⬆ Table of Contents](../../../../../../../README.md#curriculum-topic-index)&emsp;·&emsp;[Next: 11.5 — If / else ➡](../../11-5-if-else-writing-decision-logic-in-code/artifacts/reading.md)
<!-- nav:top:end -->

---
result_message = student_name + " scored an average of " + str(average_rounded)

# print() to display

<!-- nav:top:start -->
[⬅ Previous: 11.3 — Variables](../../11-3-variables-naming-and-storing-values/artifacts/reading.md)&emsp;·&emsp;[⬆ Table of Contents](../../../../../../../README.md#curriculum-topic-index)&emsp;·&emsp;[Next: 11.5 — If / else ➡](../../11-5-if-else-writing-decision-logic-in-code/artifacts/reading.md)
<!-- nav:top:end -->

---
print(result_message)
# Alice scored an average of 83.7

<!-- nav:top:start -->
[⬅ Previous: 11.3 — Variables](../../11-3-variables-naming-and-storing-values/artifacts/reading.md)&emsp;·&emsp;[⬆ Table of Contents](../../../../../../../README.md#curriculum-topic-index)&emsp;·&emsp;[Next: 11.5 — If / else ➡](../../11-5-if-else-writing-decision-logic-in-code/artifacts/reading.md)
<!-- nav:top:end -->

---

# Boolean flag (comparison covered in 11.5)

<!-- nav:top:start -->
[⬅ Previous: 11.3 — Variables](../../11-3-variables-naming-and-storing-values/artifacts/reading.md)&emsp;·&emsp;[⬆ Table of Contents](../../../../../../../README.md#curriculum-topic-index)&emsp;·&emsp;[Next: 11.5 — If / else ➡](../../11-5-if-else-writing-decision-logic-in-code/artifacts/reading.md)
<!-- nav:top:end -->

---
passed = True
print("Passed:", passed)
# Passed: True

<!-- nav:top:start -->
[⬅ Previous: 11.3 — Variables](../../11-3-variables-naming-and-storing-values/artifacts/reading.md)&emsp;·&emsp;[⬆ Table of Contents](../../../../../../../README.md#curriculum-topic-index)&emsp;·&emsp;[Next: 11.5 — If / else ➡](../../11-5-if-else-writing-decision-logic-in-code/artifacts/reading.md)
<!-- nav:top:end -->

---
```

Line by line:

1. `total / 3` — regular division (`/`) of two `int` values produces a `float` in Python 3 [2].
2. `round(average, 1)` — rounds the float to one decimal place, giving `83.7`.
3. `str(average_rounded)` — converts `83.7` to `"83.7"` so it can be concatenated with the surrounding strings.
4. `print(result_message)` — displays the assembled sentence.
5. `passed = True` — a boolean flag; connecting it to the calculated average via comparison is introduced in topic 11.5.

**Common errors:**
- `TypeError: can only concatenate str (not "float") to str` → wrap the number in `str()`.
- `TypeError: unsupported operand type(s) for +: 'int' and 'str'` → call `int()` or `float()` on the string first.
- `NameError: name 'true' is not defined` → use `True` with a capital T.

## In Practice

**Floats in AI systems.** When your code calls an AI model, confidence scores and similarity scores are floats between 0.0 and 1.0 [3]. The float precision issue is why these scores are compared against thresholds rather than tested for exact equality — a pattern that appears in the RAG pipeline module later in this course.

**Strings in data pipelines.** Student records arriving from a CSV file or an API begin their life as strings. Every numeric field must be converted with `int()` or `float()` before arithmetic can happen [3][4]. Building that habit now means you will not be surprised when a "number" in a real dataset turns out to be text.

**Boolean flags.** Variables like `is_active`, `has_passed`, and `needs_review` are called **flags** in professional code [3]. They appear throughout AI systems to record whether a document was retrieved, whether a pipeline step completed, and whether a threshold was exceeded.

## Key Takeaways

- `print()` makes a value visible in the output area; a variable can exist in memory without ever appearing on screen until you print it [5].
- Strings support concatenation (`+`), length (`len()`), and zero-based character indexing (`s[0]`) [1][4].
- Python's six integer arithmetic operators include floor division (`//`) for whole-number results and modulo (`%`) for remainders [2].
- The result `0.1 + 0.2` is not exactly `0.3` — binary floating-point storage causes a tiny error; use `round()` to control precision before display [2][3].
- `str()`, `int()`, `float()`, and `bool()` convert values between types; `str()` is the fix when a `TypeError` blocks you from concatenating a number into a string [1][3].

## References

1. Python Software Foundation. *Built-in Types*. https://docs.python.org/3/library/stdtypes.html
2. Python Software Foundation. *An Informal Introduction to Python*. https://docs.python.org/3/tutorial/introduction.html
3. Real Python. *Basic Data Types in Python*. https://realpython.com/python-data-types/
4. Real Python. *Strings and Character Data in Python*. https://realpython.com/python-strings/
5. Python Software Foundation. *print() — Built-in Functions*. https://docs.python.org/3/library/functions.html#print

---
<!-- nav:bottom:start -->
[⬅ Previous: 11.3 — Variables](../../11-3-variables-naming-and-storing-values/artifacts/reading.md)&emsp;·&emsp;[⬆ Table of Contents](../../../../../../../README.md#curriculum-topic-index)&emsp;·&emsp;[Next: 11.5 — If / else ➡](../../11-5-if-else-writing-decision-logic-in-code/artifacts/reading.md)
<!-- nav:bottom:end -->
