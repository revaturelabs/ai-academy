---
topic_id: "11.4"
title: "Data types — string, integer, float, boolean"
position_in_module: 2
generated_at: "2026-06-12T00:00:00Z"
resource_count: 5
---

# 1. Data types — string, integer, float, boolean — Topic Corpus

## 2. Prerequisites

This topic builds directly on 11.3 (Variables and data types — first look), where you learned what a variable is, how to assign values with `=`, and that every value in Python carries a type (`str`, `int`, `float`, `bool`). You also met `type()` to inspect a variable's type and the naming convention `snake_case`. Those ideas are used freely here without re-explanation.

Topics 11.1 and 11.2 introduced the Python interpreter, Google Colab, and code cells — the environment where every code example below runs.

## 3. Learning Objectives

By the end of this topic you will be able to:

- Use `print()` to display values, variables, and multiple arguments in the Colab output area.
- Apply the core string operations: `+` for concatenation, `len()` for length, and index notation `s[0]` to access a single character.
- Perform integer arithmetic using `+`, `-`, `*`, `//`, `%`, and `**`, and explain what each operator does.
- Describe why `0.1 + 0.2` does not equal `0.3` in Python, and use `round()` to control float precision.
- Combine boolean values using `and`, `or`, and `not` to express compound logical conditions.
- Convert between types using `int()`, `str()`, `float()`, and `bool()`.

## 4. Introduction

You have already stored values in variables — a student name, a mark, a test result. But so far you have mainly _stored_ things; you have not yet displayed them, done arithmetic with them, or combined them. That is what this topic adds.

Think about the grade-average script you will build in this week's lab: you need to read a student's name, add three marks together, divide by three to get the average, and display a final sentence like `"Alice scored an average of 84.0"`. Every one of those actions depends on a specific type doing something specific: a `str` being concatenated with a number, an `int` being added with other `int` values, a `float` being rounded, and a `bool` deciding which letter grade to show. This topic gives you the tools to do all of that.

It also introduces `print()` — the function you will use in almost every script you ever write — and explains the difference between a value that just _exists_ in memory and a value that actually _shows up_ on screen [5].

## 5. Core Concepts

### 5.1 The `print()` function

When Python evaluates an expression in a code cell, the Colab output area only shows the _last_ expression automatically. To display any value — at any point in your code — you call `print()` [5].

```python
print("Hello, world!")       # displays: Hello, world!
print(42)                    # displays: 42
```

`print(value)` takes one argument and displays it, followed by a newline so the next output starts on its own line [5].

You can pass **multiple arguments** separated by commas, and Python will display them with a space between each one by default:

```python
student_name = "Alice"
average_mark = 84.0
print("Student:", student_name, "Average:", average_mark)
# displays: Student: Alice Average: 84.0
```

The key distinction: a value that _exists in a variable_ lives in the computer's memory but is invisible until you ask for it. `print()` makes it visible in the output area [5]. In the REPL (the interactive session you met in 11.1), typing a variable name and pressing Enter shows its value as a side-effect; in a script file or a multi-line code cell, you must call `print()` explicitly.

### 5.2 Strings — text data

A **string** (`str`) stores text — defined in 11.3; here we focus on the operations.

#### Concatenation with `+`

You can join two strings together using `+`. This is called **concatenation** [1][4]:

```python
first_name = "Alice"
greeting = "Hello, " + first_name
print(greeting)   # Hello, Alice
```

`+` only works between two strings. If you try `"Score: " + 84`, Python raises a `TypeError` because you cannot add a string and an integer directly. This is where type conversion (Section 5.6) becomes necessary [3].

#### `len()` — string length

`len(s)` returns the number of characters in string `s` as an `int` [1][4]:

```python
name = "Alice"
print(len(name))   # 5
```

Spaces count as characters. `len("AI score")` is 8.

#### Indexing — accessing individual characters

Strings are **indexed** sequences [1][4]. Python numbers positions starting at zero. To get a single character, write the variable name followed by the position number in square brackets:

```python
name = "Alice"
print(name[0])    # A
print(name[1])    # l
print(name[4])    # e
```

Position 0 is always the first character. This zero-based counting is a Python (and general programming) convention you will see repeatedly. Negative indices count from the end — `name[-1]` gives `"e"` — but lists, slicing, and negative indexing in depth are topics for a later session.

### 5.3 Integers — whole numbers

An **integer** (`int`) is a whole number — defined in 11.3; here we cover the arithmetic operators.

#### Arithmetic operators for integers

Python provides six arithmetic operators you will use regularly [2][3]:

| Operator | Meaning          | Example          | Result |
|----------|-----------------|------------------|--------|
| `+`      | Addition         | `88 + 72`        | `160`  |
| `-`      | Subtraction      | `91 - 10`        | `81`   |
| `*`      | Multiplication   | `3 * 30`         | `90`   |
| `//`     | Floor division   | `251 // 3`       | `83`   |
| `%`      | Modulo (remainder)| `251 % 3`       | `2`    |
| `**`     | Exponentiation   | `2 ** 8`         | `256`  |

**Floor division** (`//`) divides and rounds _down_ to the nearest whole number, discarding any remainder [1][2]. This is useful when you want a whole-number answer — for example, the number of complete groups of students:

```python
total_marks = 88 + 72 + 91    # 251
num_subjects = 3
whole_average = total_marks // num_subjects   # 83 (not 83.67)
```

**Modulo** (`%`) gives the _remainder_ after division [1][2]:

```python
print(251 % 3)    # 2  (251 = 83 × 3 + 2)
```

**Exponentiation** (`**`) raises a number to a power [2]:

```python
print(2 ** 10)    # 1024
```

When you mix `int` and `float` in an arithmetic expression (e.g., `3 + 1.5`), Python automatically produces a `float` result (`4.5`) — no information is lost [3].

### 5.4 Floats — decimal numbers

A **float** stores decimal numbers — defined in 11.3; here we cover precision and `round()`.

#### Why `0.1 + 0.2 != 0.3`

This is one of the most-asked "is this a bug?" moments for new programmers [3]:

```python
print(0.1 + 0.2)    # 0.30000000000000004
# Note: 0.1 + 0.2 is NOT equal to 0.3 — the result is very slightly different
```

The reason is that computers store numbers in binary (base-2), and the decimal fraction `0.1` has no exact binary representation — just as `1/3` has no exact decimal representation (it is `0.333...` forever). When Python stores `0.1`, it stores the nearest representable binary fraction, which is very slightly different. When you add `0.1` and `0.2`, the tiny errors accumulate, and the result is not exactly `0.3` [2][3].

**This is not a Python bug** — it is a consequence of how all modern hardware stores decimal fractions in binary.

#### Controlling precision with `round()`

`round(number, ndigits)` rounds a float to `ndigits` decimal places and returns a float [1]:

```python
average = (88 + 72 + 91) / 3       # 83.66666666666667
rounded = round(average, 1)         # 83.7
print(rounded)                       # 83.7
```

If you omit `ndigits`, `round()` returns the nearest integer:

```python
print(round(83.67))     # 84
```

For the grade-average lab, `round(average, 1)` gives a clean one-decimal result suitable for display.

### 5.5 Booleans — true/false values

A **boolean** (`bool`) is `True` or `False` — defined in 11.3; here we cover truthiness and `if` compatibility.

#### Boolean operators: `and`, `or`, `not`

Three operators let you combine boolean values into compound conditions [1][3]:

**`and`** — True only when **both** sides are True:

```python
passed_exam = True
attendance_ok = True
eligible = passed_exam and attendance_ok
print(eligible)    # True
```

**`or`** — True when **at least one** side is True:

```python
has_extension = False
submitted_on_time = True
accepted = has_extension or submitted_on_time
print(accepted)    # True
```

**`not`** — flips a boolean: True becomes False, False becomes True:

```python
is_failing = False
print(not is_failing)    # True
```

Boolean expressions that compare values (e.g., testing whether a mark is above a threshold) are introduced in topic 11.5 (if/else). For now, the examples above show `and`, `or`, and `not` operating directly on `bool` variables.

### 5.6 Type conversion

Python's four types can be converted into one another using built-in conversion functions [1][3]. This is called **explicit type conversion** (or **casting**).

| Function   | Converts to | Common use |
|------------|-------------|------------|
| `int(x)`   | `int`       | Drop decimals, convert a digit string |
| `float(x)` | `float`     | Make a whole number decimal-aware |
| `str(x)`   | `str`       | Turn a number into text for concatenation |
| `bool(x)`  | `bool`      | Check if a value is "truthy" |

#### `str()` — numbers to text

This is the most common conversion in beginner scripts [3][4]:

```python
average = 83.7
message = "Average score: " + str(average)
print(message)    # Average score: 83.7
```

Without `str(average)`, the `+` operator would raise a `TypeError`.

#### `int()` — string or float to integer

```python
mark_text = "88"            # this is a str, not an int
mark_number = int(mark_text)  # now it is 84 as int
print(mark_number + 10)       # 98
```

`int()` truncates (drops) the decimal part — it does not round:

```python
print(int(83.9))    # 83, not 84
```

#### `float()` — string or integer to float

```python
whole_score = 84
decimal_score = float(whole_score)    # 84.0
```

#### `bool()` — truthy and falsy values

`bool()` converts any value to `True` or `False` [1][3]. The rule Python uses:

- `False` for: `0`, `0.0`, and `""` (empty string).
- `True` for everything else (any non-zero number, any non-empty string).

```python
print(bool(0))       # False
print(bool(1))       # True
print(bool(""))      # False
print(bool("hi"))    # True
```

This is relevant in the grade-average lab when you check whether a student entered a name at all — a concept built on in 11.5.

## 6. Implementation

### Building a grade-average snippet step by step

Below is a minimal working example that ties together every concept in this topic. It previews the week's lab without spoiling it.

```python
# --- Inputs (hard-coded for now; user input is covered in 11.5) ---
student_name = "Alice"
mark1 = 88
mark2 = 72
mark3 = 91

# --- Integer arithmetic ---
total = mark1 + mark2 + mark3        # 251
average = total / 3                  # 83.666...  (dividing int by int gives float)
average_rounded = round(average, 1)  # 83.7

# --- Type conversion for the output string ---
result_message = student_name + " scored an average of " + str(average_rounded)

# --- print() to display ---
print(result_message)
# Output: Alice scored an average of 83.7

# --- Boolean flag (hardcoded for now; comparisons are covered in 11.5) ---
passed = True
print("Passed:", passed)
# Output: Passed: True
```

Walk through what each line does:

1. `total = mark1 + mark2 + mark3` — integer addition, result is `int` (251).
2. `total / 3` — regular division (`/`) of two `int` values gives a `float` in Python 3 [2]. This is the intended behaviour; use `//` only when you explicitly want a whole number.
3. `round(average, 1)` — rounds the float to one decimal place.
4. `str(average_rounded)` — converts `83.7` from `float` to `"83.7"` so it can be concatenated with the rest of the string.
5. `print(result_message)` — displays the assembled string.
6. `passed = True` — a `bool` variable used as a flag; connecting a bool to a calculated result via comparison is introduced in topic 11.5.

### Common errors to watch for

**`TypeError: can only concatenate str (not "float") to str`**
You forgot to wrap a number in `str()` before using `+` to build a message. Fix: `str(average_rounded)`.

**`TypeError: unsupported operand type(s) for +: 'int' and 'str'`**
The reverse: you are trying to do arithmetic on a value that is stored as a string (e.g., a mark read from text input). Fix: `int(mark_text)` before the addition.

**`NameError: name 'true' is not defined`**
You typed `true` (lowercase). Fix: `True`.

## 7. Real-World Patterns

### Floats in AI and data science

When your Python code calls an AI model, the model's output scores — confidence values, probabilities, embedding similarity scores — are all floats, typically between 0.0 and 1.0 [3]. The float precision issue described in Section 5.4 is the reason those scores are almost never compared with `==`; instead, practitioners check whether a score is above a threshold (e.g., `similarity_score > 0.75`). This pattern appears in retrieval-augmented generation (RAG) pipelines, a later module in this course.

### Strings in data pipelines

Student records in a real system arrive as text — a CSV row, a JSON value, a form field — and almost every value begins its life as a `str`. The conversion functions `int()` and `float()` are the first transformation step before any arithmetic [3][4]. Building that habit now means you will not be surprised when a "number" in a dataset turns out to be a string.

### Booleans as flags

Boolean variables used to record a state — `is_active`, `has_passed`, `needs_review` — are called **flags** in professional code [3]. They are used throughout AI systems to signal whether a document was retrieved, whether a threshold was exceeded, and whether a step in a pipeline completed successfully.

## 8. Best Practices

- **Prefer `round()` over truncation for displayed averages.** `int(83.67)` gives `83`; `round(83.67, 1)` gives `83.7`. The first silently drops information; the second communicates the real precision.
- **Always convert to `str` before concatenating with `+`.** It is clearer and avoids `TypeError` at runtime. Later you will learn f-strings (a cleaner alternative) — but `str()` is always available and explicit.
- **Name boolean variables so they read as yes/no questions.** `is_passing`, `has_submitted`, `attendance_met` are immediately readable; `flag1` is not.
- **Do not compare floats with `==`.** Use `>=`, `<=`, or `round()` to test equality within a tolerance. Floating-point representation means exact equality is rarely reliable [2][3].
- **Use single or double quotes consistently within a file.** Python allows both; mixing them without reason makes code harder to scan.
- **Use `type()` when debugging unexpected behaviour.** If an operation gives a surprising result, call `type(variable)` to check whether it is the type you think it is (introduced in 11.3).

## 9. Hands-On Exercise

Open a new code cell in your Colab notebook and do the following without looking at Section 6:

1. Create three variables `mark_a`, `mark_b`, `mark_c` and assign them integer values of your choice between 0 and 100.
2. Compute the average as a float.
3. Round it to one decimal place.
4. Build a string that says `"Average: <rounded_value>"` and print it — you will need `str()`.
5. Create a boolean variable `distinction` that is `True` when the average is 70 or above, and print it with a label using `print()`.

Expected output (values will differ):
```
Average: 83.7
distinction: True
```

## 10. Key Takeaways

- `print()` is how you make a value visible in the output area; a variable can exist in memory without ever appearing on screen until you print it [5].
- Strings support concatenation (`+`) and length (`len()`); individual characters are accessed by their zero-based index (`s[0]`) [1][4].
- Python's six integer arithmetic operators include floor division (`//`) for whole-number results and modulo (`%`) for remainders — both essential for grade calculations [2].
- The result `0.1 + 0.2 != 0.3` is not a bug; it is a consequence of binary floating-point storage; use `round()` to control precision before display [2][3].
- `int()`, `float()`, `str()`, and `bool()` convert values between types; `str()` is the fix when `TypeError` blocks you from concatenating a number into a string [1][3].

## 11. Next Steps

_System-derived from the next entry in curriculum/sequence.md._
