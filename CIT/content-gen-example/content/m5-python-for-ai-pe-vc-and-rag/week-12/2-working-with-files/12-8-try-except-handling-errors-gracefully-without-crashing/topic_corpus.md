---
topic_id: "12.8"
title: "try / except — handling errors gracefully without crashing"
position_in_module: 3
generated_at: "2026-06-14T00:00:00Z"
resource_count: 3
---

# 1. try / except — Handling Errors Gracefully Without Crashing — Topic Corpus

## 2. Prerequisites

This topic builds directly on the file-handling skills from the previous two topics. You need:

- **12.6 — Reading from and writing to a file:** you know how to call `open()`, read lines with `.read()` / `.readlines()`, and use a `with` block to handle files safely.
- **12.7 — Write mode, append mode, `.write()`, `.writelines()`:** you know how to create or update files from Python code.

These two topics are the motivation for `try / except`: the most common error a beginner encounters when working with files is trying to open a file that does not exist. This topic teaches you exactly what to do when that happens — and how the same technique applies anywhere in Python where something might go wrong.

## 3. Learning Objectives

By the end of this topic you will be able to:

1. Explain what a Python **exception** is and how it differs from a program that simply stops with a cryptic error message.
2. Write a `try` block that wraps code which might fail, and an `except` block that handles the failure without crashing the program.
3. Catch a **specific exception** (such as `FileNotFoundError`, `ValueError`, or `TypeError`) rather than silencing every possible error.
4. Use the `else` clause to write code that runs only when the `try` block succeeded.
5. Wrap file `open()` calls in a `try / except` block to gracefully handle missing or unreadable files.
6. Identify at least two common beginner mistakes — bare `except` and swallowing errors silently — and explain why they make programs harder to debug.

## 4. Introduction

You have spent the last two topics writing code that opens, reads, and writes files. That code looks clean and works perfectly — as long as the file actually exists, the path is spelled correctly, and you have permission to access it.

But what happens when none of those things are true?

Run this in Python:

```python
f = open("marks.csv", "r")
```

If `marks.csv` does not exist, Python immediately prints something like:

```
FileNotFoundError: [Errno 2] No such file or directory: 'marks.csv'
```

...and the entire program stops. Any code below that line never runs. If this was part of a larger script — say, a script that also sends results to an API and writes a summary — none of that happens either. The program just dies.

This kind of abrupt stop is called a **crash**. Crashes are unpleasant for users, hard to diagnose, and sometimes dangerous when they leave files half-written or network connections open.

Python's answer to this problem is **exception handling**: a built-in mechanism that lets you say, "I know this piece of code might fail — here is what I want to do if it does." The tool that implements this is `try / except` [1].

Learning `try / except` unlocks two important abilities: (1) you can write programs that stay alive and give helpful messages even when something unexpected happens; (2) you can distinguish between the errors you anticipated and the ones you did not, so debugging is faster.

## 5. Core Concepts

### 5.1 What Is an Exception?

An **exception** is Python's way of saying "something went wrong while this line was running." When Python encounters a problem it cannot resolve — a missing file, a number divided by zero, a function receiving the wrong type of argument — it **raises** an exception [1].

"Raising" means Python creates a special object that describes the problem, then immediately stops the current block of code and looks for instructions about what to do. If there are no such instructions, the program crashes and Python prints the error message you see in the terminal.

Exceptions are not the same as **syntax errors**. A syntax error means your code is written incorrectly (missing a colon, mismatched brackets). Python catches syntax errors before the program even starts running. Exceptions, by contrast, happen at **runtime** — while the code is actually executing. That is why you cannot always see them before you run your program.

Every exception has a **name** (also called its **type**). The name tells you what kind of problem occurred:

| Exception name | When it occurs |
|---|---|
| `FileNotFoundError` | You tried to open a file that does not exist at the given path [1] |
| `ValueError` | A function received an argument of the right type but a bad value (e.g., `int("hello")`) [2] |
| `TypeError` | A function received an argument of the completely wrong type (e.g., adding a number to a string) [2] |
| `ZeroDivisionError` | You tried to divide a number by zero |
| `PermissionError` | You tried to open a file but the operating system denied access |

Knowing the name matters because you handle each type differently.

### 5.2 The `try` Block

The `try` block contains the code that **might** fail [1]. You are effectively telling Python: "I am not 100% certain this will work — keep an eye on it."

```python
try:
    f = open("marks.csv", "r")
    content = f.read()
    f.close()
```

Syntax rules:
- The keyword is `try` (all lowercase).
- A colon follows immediately: `try:`.
- Every line inside the block is indented by four spaces (the same rule as `for`, `if`, and `def`).

If every line inside the `try` block runs without raising an exception, Python exits the block normally and continues with whatever comes next. The `except` block is skipped entirely.

If any line inside the `try` block raises an exception, Python immediately stops at that line — the remaining lines in the `try` block do not run — and jumps to the `except` block.

### 5.3 The `except` Block

The `except` block contains the code that runs **only when the `try` block raised an exception** [1]. It is where you handle the problem gracefully.

```python
try:
    f = open("marks.csv", "r")
    content = f.read()
    f.close()
except FileNotFoundError:
    print("Error: marks.csv was not found. Please check the file name and try again.")
```

What happens here:

1. Python tries to open `marks.csv`.
2. If the file does not exist, Python raises `FileNotFoundError`.
3. Instead of crashing, Python runs the `except` block and prints the helpful message.
4. The program then continues with whatever line comes after the entire `try / except` structure.

The program does not crash. The user sees a clear message. Downstream code still runs.

**The exception name after `except`** is the filter. `except FileNotFoundError:` catches only that specific exception — nothing else. This is intentional and correct [1][3].

### 5.4 Catching Specific Exceptions

The most important rule in exception handling is: **catch what you expect, and nothing more** [1][3].

Python allows you to write `except` without naming an exception type — this is called a **bare except**:

```python
# DO NOT DO THIS
try:
    f = open("marks.csv", "r")
except:
    print("Something went wrong.")
```

A bare `except` catches **every** possible exception, including ones you did not anticipate: typos in variable names (`NameError`), keyboard interrupts (when the user presses Ctrl+C), memory failures, and more. By hiding all of them under "something went wrong" you make debugging nearly impossible. The Python community strongly discourages bare `except` [1][3].

The better approach is to name the specific exception you are guarding against:

```python
try:
    f = open("marks.csv", "r")
    content = f.read()
    f.close()
except FileNotFoundError:
    print("The file 'marks.csv' does not exist.")
```

If you want to handle more than one known exception type, write multiple `except` clauses:

```python
try:
    raw = input("Enter a number: ")
    number = int(raw)
except ValueError:
    print("That was not a valid number.")
except TypeError:
    print("A type mismatch occurred.")
```

Each `except` clause is checked in order, top to bottom. The first one whose type matches the raised exception runs; the rest are skipped [2].

**Getting the error message into your code.** You can capture the exception object itself with `as e`. This gives you access to Python's own description of the problem:

```python
try:
    f = open("marks.csv", "r")
except FileNotFoundError as e:
    print(f"File error: {e}")
```

The variable `e` holds the exception object. When you convert it to a string (which `print` and f-strings do automatically), you get the same message Python would have shown if the program had crashed. Showing this to a developer — while still letting the program continue — is often the right balance [3].

### 5.5 The `else` Clause

Python's `try / except` has an optional third piece: the `else` block [2].

```python
try:
    f = open("marks.csv", "r")
    content = f.read()
    f.close()
except FileNotFoundError:
    print("File not found.")
else:
    print("File read successfully.")
    print(content)
```

The `else` block runs **only if the `try` block completed without raising any exception** [2]. Think of it as "the happy path" — code that should only run when things went well.

Why use `else` instead of simply putting those lines at the bottom of the `try` block?

Clarity and correctness: code inside the `try` block is code you are actively protecting from exceptions. Code in `else` runs after that protection ends, so any exception it raises is **not** caught by the `except` clause above it. This makes it easier to see exactly which lines are under exception-handling protection and which are not [2][3].

For beginners, `else` is optional — your code will work without it. But it is a clean, readable signal of intent: "this is what I do when everything worked."

### 5.6 Wrapping File Operations in `try / except`

The direct connection to 12.6 and 12.7: every time you call `open()`, there is a chance the file does not exist, the path is wrong, or you lack permission. Without `try / except`, any of these failures crashes the program. With it, you can give the user a helpful message and keep going [1][3].

**Pattern: reading a file safely**

```python
def read_marks(filename):
    try:
        with open(filename, "r") as f:
            lines = f.readlines()
        return lines
    except FileNotFoundError:
        print(f"Error: '{filename}' was not found.")
        return []
```

Notice:
- The `with open(...)` block from 12.6 is still used — it ensures the file is closed when the block exits.
- The `try` wraps the entire `with open(...)` call. If the file does not exist, `FileNotFoundError` is raised before the `with` block even starts.
- The `except` block returns an empty list `[]` so the calling code can continue without a crash.

**Pattern: writing a file safely**

```python
def write_summary(filename, text):
    try:
        with open(filename, "w") as f:
            f.write(text)
        print(f"Summary written to '{filename}'.")
    except PermissionError:
        print(f"Error: Could not write to '{filename}'. Check file permissions.")
```

`PermissionError` is the most common exception when writing — it means the operating system blocked the write (for example, the file is read-only or you are writing to a protected directory).

**When `try` is outside `with`:** the `with` statement guarantees the file is closed when the block exits, even if an exception was raised inside it. The `except` clause catches the exception after the `with` block has already cleaned up [1].

## 6. Implementation

### Step-by-step: Wrapping a file read

**Step 1 — Identify the risky call.** The call to `open()` is where `FileNotFoundError` can appear. That line, and anything that depends on the file being open, goes inside `try`.

**Step 2 — Write the `try` block.**

```python
try:
    with open("marks.csv", "r") as f:
        lines = f.readlines()
```

**Step 3 — Write the `except` block naming the specific exception.**

```python
except FileNotFoundError:
    print("marks.csv was not found. Please add the file and re-run.")
    lines = []
```

Setting `lines = []` inside `except` means the variable still exists after the block, so code further down that uses `lines` does not raise a `NameError`.

**Step 4 — Add `else` (optional) for the success path.**

```python
else:
    print(f"Read {len(lines)} lines from marks.csv.")
```

**Combined:**

```python
try:
    with open("marks.csv", "r") as f:
        lines = f.readlines()
except FileNotFoundError:
    print("marks.csv was not found. Please add the file and re-run.")
    lines = []
else:
    print(f"Read {len(lines)} lines from marks.csv.")

# This code runs whether the file was found or not
print(f"Processing {len(lines)} lines...")
```

### Step-by-step: Validating user input

`try / except` is not just for files. It is the standard way to validate that user input can be converted to a number [2]:

```python
raw = input("Enter a mark (0-100): ")
try:
    mark = int(raw)
except ValueError:
    print(f"'{raw}' is not a valid integer. Defaulting to 0.")
    mark = 0

print(f"Mark recorded: {mark}")
```

`int("85")` works and returns `85`. `int("eighty-five")` raises `ValueError`. The `except ValueError` block catches that specific failure, sets a safe default, and the program continues.

## 7. Real-World Patterns

### File I/O in data pipelines

In data pipelines — including the kind of AI pipelines you will build in upcoming topics — reading CSV files or JSON files is one of the first things a script does. A missing input file is one of the most common reasons a pipeline fails at startup. Wrapping the initial `open()` in `try / except FileNotFoundError` and printing a clear diagnostic message is standard practice [3].

```python
def load_data(path):
    try:
        with open(path, "r") as f:
            return f.read()
    except FileNotFoundError:
        print(f"[ERROR] Input file not found: {path}")
        return None
```

The function returns `None` when the file is absent. Callers check `if data is None` before doing anything with the result.

### Input validation in interactive scripts

Any script that prompts a user for a number should protect `int()` or `float()` conversion with `try / except ValueError`. The user will eventually type something that is not a number. Catching it keeps the program running and lets you ask again or use a safe default [2][3].

### API calls (preview, covered in 12.10+)

When you make API calls to services like the Anthropic API (covered in upcoming topics), the connection can fail: no internet, invalid key, server timeout. Those failures also raise exceptions. The same `try / except` pattern you learn here for files applies directly to API calls — the exception types differ, but the structure is identical. This will be covered in detail in topic 12.12.

## 8. Best Practices

**Do** catch specific exception types, not bare `except` [1][3].

```python
# Good
except FileNotFoundError:

# Bad — catches everything including bugs you need to see
except:
```

**Do** give users a clear, actionable error message [1].

```python
# Good
print(f"Could not open '{filename}'. Check that the file exists in the current folder.")

# Bad — gives the user nothing to act on
print("Error.")
```

**Do** set safe defaults for variables inside the `except` block when downstream code depends on those variables.

```python
except FileNotFoundError:
    lines = []   # downstream code can still call len(lines) safely
```

**Do not** put more code inside `try` than necessary. The `try` block should cover only the one or two lines that can actually raise the exception you are catching [3]. Putting many lines inside `try` masks which line is the actual source of the problem.

```python
# Too broad — which line failed?
try:
    with open("marks.csv") as f:
        lines = f.readlines()
    total = sum(float(line.strip()) for line in lines)
    average = total / len(lines)
    print(f"Average: {average}")
except Exception:
    print("Something went wrong.")

# Better — separate try/except blocks, each protecting one concern
try:
    with open("marks.csv") as f:
        lines = f.readlines()
except FileNotFoundError:
    print("marks.csv not found.")
    lines = []

try:
    total = sum(float(line.strip()) for line in lines)
    average = total / len(lines)
    print(f"Average: {average}")
except ValueError:
    print("One or more lines could not be converted to a number.")
except ZeroDivisionError:
    print("The file was empty — no marks to average.")
```

**Do not** silently swallow exceptions with an empty `except` block [3].

```python
# Silent swallow — the error disappears, bugs become invisible
try:
    f = open("marks.csv")
except FileNotFoundError:
    pass   # avoid this unless you have a very specific documented reason
```

If you genuinely want to ignore an exception, add a comment explaining why so future readers understand the intent.

**A brief note on `finally`:** Python's `try` structure has a fourth clause, `finally`, which runs regardless of whether an exception occurred. It is used for cleanup tasks such as closing network connections. It is mentioned here for awareness; the `with` block already handles file cleanup for the operations in this module, so `finally` is an advanced pattern you do not need yet [2].

## 9. Hands-On Exercise

**Exercise — Safe CSV reader for the lab**

You have a file called `student_marks.csv`. Each line contains one integer mark (a number from 0 to 100).

1. Write a function `load_marks(filename)` that:
   - Tries to open the file and read every line.
   - Returns a list of integer marks if the file exists.
   - Catches `FileNotFoundError` and prints a clear message, returning an empty list instead of crashing.
   - Catches `ValueError` (in case a line cannot be converted to an integer) and prints which line caused the problem, skipping that line.

2. Call `load_marks("student_marks.csv")` and print the number of marks loaded.

3. Test two edge cases:
   - Run the script when `student_marks.csv` does not exist.
   - Add a non-numeric line (such as "N/A") inside the file and check that the rest of the marks still load.

This exercise directly mirrors Lab Part 1 (reading a CSV of student marks), adding the error-handling layer on top of the file-reading skills from 12.6.

## 10. Key Takeaways

- An **exception** is Python's way of signalling a runtime error. Without `try / except`, any unhandled exception crashes the program immediately.
- The **`try` block** wraps code that might fail. The **`except` block** runs only when a specific failure occurs — the program keeps running instead of crashing.
- Always catch **specific exception types** (e.g., `FileNotFoundError`, `ValueError`). Bare `except:` hides bugs and is strongly discouraged by the Python community.
- The **`else` clause** runs only when no exception occurred — it cleanly separates "what to do on success" from "what to do on failure."
- For file operations from 12.6 and 12.7, wrapping `open()` in `try / except FileNotFoundError` is the standard, professional pattern — it gives users a meaningful message and lets the rest of the script continue.

## 11. Next Steps

_System-derived from the next entry in curriculum/sequence.md._
