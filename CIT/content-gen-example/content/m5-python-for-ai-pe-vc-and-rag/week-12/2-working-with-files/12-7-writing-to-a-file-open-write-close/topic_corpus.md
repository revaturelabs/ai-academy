---
topic_id: "12.7"
title: "Writing to a file — open, write, close"
position_in_module: 2
generated_at: "2026-06-14T00:00:00Z"
resource_count: 3
---

# 1. Writing to a File — open, write, close — Topic Corpus

## 2. Prerequisites

This topic continues directly from Topic 12.6 — Reading from a file. You need:

- **12.6 — Reading from a file:** you know what a file object is, how `open()` works, what read mode `'r'` means, and how the `with` block automatically closes the file.
- **12.4 — Lists:** you can create a list, loop over it, and use `append()`.
- **12.1–12.3 — Functions:** you can define a function with `def`, pass parameters, and return a value.

Background from Week 11:
- **Strings and `str()`:** you know Python strings, `+` concatenation, and how to convert a number to a string with `str()`.
- **For loops and if/else:** you can repeat a block and write conditional logic.

## 3. Learning Objectives

By the end of this topic you will be able to:

1. Open a file in **write mode (`'w'`)** and explain that it creates the file if it does not exist and **erases** it completely if it does.
2. Open a file in **append mode (`'a'`)** and explain that it creates the file if it does not exist and **adds** new content to the end if it does.
3. Use `.write(string)` to write a single string to an open file and explain why you must include `\n` manually.
4. Use `.writelines(list)` to write every string in a list to a file in a single call.
5. Convert numbers to strings with `str()` before calling `.write()`, and explain why writing a raw number raises a `TypeError`.
6. Wrap all file-writing code in a `with` block so the file is always closed and flushed, even if something goes wrong.

## 4. Introduction

In Topic 12.6 you learned to open a file and *read* data from it. Reading is only half the story. Programs that are useful in the real world need to *save* their results — write a summary to disk, log what happened, or store the output of a computation so it persists after the program finishes.

Think about the Week 12 lab. You will read student marks from a CSV file, compute averages and top scores, and then produce a summary. If you only print that summary to the screen, it disappears the moment the program stops. Writing to a file is how you make the output permanent. Another program — or a human opening the file in a text editor — can read it later [1].

This topic covers exactly that: opening a file for writing, putting content into it, and closing it safely. You will also see a second writing mode — **append mode** — that lets you add new lines to a file without erasing what is already there. The tools are simple: `open()` with a different mode letter, `.write()`, `.writelines()`, and the same `with` block you already know from reading [1][2].

One critical beginner gotcha is introduced up front and returned to repeatedly: **write mode erases the file's existing content**. This surprises almost every new programmer the first time. By the end of this topic you will know exactly when that happens and how to avoid it when you do not want it [1][3].

## 5. Core Concepts

### 5.1 Write Mode (`'w'`) — Creates or Erases

To open a file for writing, you pass the letter `'w'` as the second argument to `open()`:

```python
file_object = open("results.txt", "w")
```

This call does one of two things depending on whether the file already exists:

- **File does not exist yet:** Python creates a brand-new, empty file called `results.txt` and hands you a file object pointing to its beginning.
- **File already exists:** Python **erases all existing content** immediately — before you write a single character — and hands you a file object pointing to the (now empty) beginning.

That second behaviour is the critical gotcha [1]. The moment you call `open("results.txt", "w")`, any previous content is gone. There is no "undo" and no warning. This is intentional: write mode is designed for programs that regenerate the whole file from scratch each run (for example, re-writing a full results summary after recalculating scores). If you do not want to erase, you need append mode (§5.2).

The file object you get back works exactly like the file object from read mode — it is just a Python variable that represents the open file [2]. You call methods on it to send content to the file.

After write mode opens the file, an internal **bookmark** (the file position) sits at the very beginning. Every `.write()` call advances that bookmark forward, character by character [1].

### 5.2 Append Mode (`'a'`) — Adds to the End

Append mode uses the letter `'a'`:

```python
file_object = open("results.txt", "a")
```

The behaviour:

- **File does not exist yet:** Python creates a new, empty file — same as write mode.
- **File already exists:** Python opens it **without erasing anything**. The internal bookmark jumps straight to the very end of existing content. Every `.write()` call adds new characters after whatever was already there.

Append mode is what you use when you want to grow a file over time — for example, adding a new log entry each time a program runs, without losing the previous entries [1][3].

The two modes compared in a single mental model:

| | `'w'` Write mode | `'a'` Append mode |
|---|---|---|
| File does not exist | Creates it | Creates it |
| File already exists | **Erases content, starts from beginning** | Keeps content, starts from end |
| Typical use | Regenerate the whole file each run | Add new lines to a growing file |

Both modes let you use `.write()` and `.writelines()` — the methods are identical. Only the starting position and the treatment of existing content differ [1].

### 5.3 The `.write(string)` Method — Writing One String

Once a file is open in write or append mode, you call `.write()` to send content to it:

```python
f.write("Alice,88")
```

Three rules to remember [1][2]:

1. **The argument must be a string.** If you try to write an integer or float directly, Python raises a `TypeError` (§5.7 covers this).
2. **No automatic newline is added.** Unlike `print()`, which always ends its output with a line break, `.write()` writes exactly what you give it and nothing more. If you call `.write("Alice,88")` and then `.write("Bob,74")`, the file will contain `Alice,88Bob,74` — all on one line.
3. **The bookmark advances.** After each `.write()` call the internal position moves forward by the number of characters written. The next `.write()` continues from that point.

The method returns the number of characters written, but you almost never need that return value.

### 5.4 Newlines in `.write()` — You Must Add `\n` Yourself

Because `.write()` does not add a newline, you are responsible for including `\n` (the newline character) wherever you want a line break:

```python
f.write("Alice,88\n")
f.write("Bob,74\n")
f.write("Carol,91\n")
```

With `\n` at the end of each string, the file will contain:

```
Alice,88
Bob,74
Carol,91
```

Without `\n`, the file would contain:

```
Alice,88Bob,74Carol,91
```

That single-line result is a very common beginner mistake [1][3]. The fix is always the same: add `\n` to the end of every string that should be its own line.

You can also place `\n` in the middle of a string to force a line break at a specific point:

```python
f.write("=== Results ===\nGenerated: 2026-06-14\n")
```

This writes two lines: a header and a date, both in one `.write()` call.

### 5.5 The `.writelines(list)` Method — Writing a List of Strings

When you already have a list of strings, `.writelines()` is a convenient shorthand:

```python
lines = ["Alice,88\n", "Bob,74\n", "Carol,91\n"]
f.writelines(lines)
```

`.writelines()` loops over the list internally and calls the equivalent of `.write()` for each element. The result is identical to calling `.write()` on each string individually [2].

The same newline rule applies: `.writelines()` does **not** add `\n` between items. If your list strings do not already end with `\n`, the lines will run together just as they would with bare `.write()` calls [1]:

```python
# Wrong — no newlines in the list
lines = ["Alice,88", "Bob,74", "Carol,91"]
f.writelines(lines)
# File contains: Alice,88Bob,74Carol,91

# Correct — each string ends with \n
lines = ["Alice,88\n", "Bob,74\n", "Carol,91\n"]
f.writelines(lines)
# File contains three separate lines
```

A quick pattern for adding `\n` to every string in a list before passing it to `.writelines()`:

```python
raw = ["Alice,88", "Bob,74", "Carol,91"]
lines = [s + "\n" for s in raw]
f.writelines(lines)
```

The `[s + "\n" for s in raw]` part is a **list comprehension** — a compact way to build a new list by transforming every item. You have already used `for` loops over lists (Topic 12.4); this is the same idea compressed into one expression [2].

### 5.6 The `with` Block for Writing — Auto-Close and Auto-Flush

In Topic 12.6 you used the `with` block to open and read a file. The exact same pattern works for writing:

```python
with open("results.txt", "w") as f:
    f.write("Alice,88\n")
    f.write("Bob,74\n")
# File is automatically closed here
```

Why use `with` instead of calling `f.close()` manually? Two reasons [1][2]:

1. **Guaranteed close.** If something goes wrong inside the `with` block — for example, a variable is not defined — Python still closes the file before the error propagates. A manually placed `f.close()` that appears after the problem line would never execute.
2. **Flush on close.** When you write to a file, Python may hold the data in a temporary buffer in memory and not immediately write it to disk. When the file is closed (either by `with` or by calling `f.close()`), Python flushes the buffer — sends any buffered data to disk. If your program crashes before the file is closed, buffered data can be lost. The `with` block closes the file as soon as the indented block ends, minimising that risk.

The `with` block for writing follows the same indentation rules as for reading: all `.write()` calls must be indented inside the block. Once Python exits the indented block, the file is closed and you can no longer write to it [3].

```python
with open("results.txt", "w") as f:
    f.write("Alice,88\n")   # inside the block — file is open
# outside the block — file is closed; writing here would raise ValueError
```

### 5.7 Converting Values Before Writing — `str()` Is Required

A file holds text. `.write()` only accepts strings. If you pass a number directly, Python raises a `TypeError`:

```python
score = 88
f.write(score)        # TypeError: write() argument must be str, not int
f.write(str(score))   # Correct: writes the string "88"
```

`str()` is the function that converts any value to its string representation [2]. You used it in Week 11 for string formatting. When writing file content that mixes text and numbers — for example, a student name and their score — convert each number before concatenating:

```python
name = "Alice"
score = 88
f.write(name + "," + str(score) + "\n")
# Writes: Alice,88
```

A common pattern is to build the full string first, then write it:

```python
line = name + "," + str(score) + "\n"
f.write(line)
```

Both approaches produce the same result. The second is easier to read and debug because you can print `line` to inspect it before writing [1][3].

## 6. Implementation

This section walks through the lab use-case: saving a list of student names and scores to a file, then adding a new student without erasing the existing results.

### Step 1 — Open in Write Mode and Write Lines One at a Time

Start with a list of tuples (name, score pairs) and write each one as a line:

```python
students = [("Alice", 88), ("Bob", 74), ("Carol", 91)]

with open("results.txt", "w") as f:
    for name, score in students:
        line = name + "," + str(score) + "\n"
        f.write(line)
```

After this runs, `results.txt` contains:

```
Alice,88
Bob,74
Carol,91
```

The `for name, score in students:` loop unpacks each tuple — `name` gets the first element, `score` gets the second. This is the same `for` loop you used in Topic 12.4, extended to pairs of values [1].

### Step 2 — Confirm `\n` Is in Every Line

Before writing, print a line to verify it looks right:

```python
with open("results.txt", "w") as f:
    for name, score in students:
        line = name + "," + str(score) + "\n"
        print(repr(line))   # shows: 'Alice,88\n'
        f.write(line)
```

`repr()` is a built-in function that shows the "programmer's view" of a string — it makes invisible characters like `\n` visible as literal backslash-n. This is purely a debugging trick; remove the `print` call once you are satisfied [2].

### Step 3 — Wrap in a Function `save_results(filename, students)`

A good single-job function (Topic 12.3) handles one thing: saving data to a file. Pass the filename and the list of student tuples as parameters:

```python
def save_results(filename, students):
    """Write each student name and score to filename, one per line."""
    with open(filename, "w") as f:
        for name, score in students:
            line = name + "," + str(score) + "\n"
            f.write(line)

# Call it:
save_results("results.txt", students)
```

This function has one job: writing the results file. It takes `filename` as a parameter so it is reusable — you can call it with `"results.txt"` or `"backup.txt"` or any other name without changing the function body [1][3].

The `"""..."""` on the first line inside the function is a **docstring** — a plain-English description of what the function does. Python displays it when you call `help(save_results)`. It is a good habit to include one [2].

### Step 4 — Add a New Student With Append Mode

Later in the lab run, a new student's mark arrives. You want to add it to `results.txt` without erasing the existing three lines:

```python
def append_student(filename, name, score):
    """Append one student line to an existing results file."""
    with open(filename, "a") as f:
        line = name + "," + str(score) + "\n"
        f.write(line)

# Call it after save_results has already run:
append_student("results.txt", "David", 79)
```

After this call, `results.txt` contains:

```
Alice,88
Bob,74
Carol,91
David,79
```

The key difference from Step 3 is the mode string: `"a"` instead of `"w"`. Everything else — the `with` block, `.write()`, the `\n` — is identical [1][2].

### Complete Example Together

```python
students = [("Alice", 88), ("Bob", 74), ("Carol", 91)]


def save_results(filename, students):
    """Write each student name and score to filename, one per line."""
    with open(filename, "w") as f:
        for name, score in students:
            line = name + "," + str(score) + "\n"
            f.write(line)


def append_student(filename, name, score):
    """Append one student line to an existing results file."""
    with open(filename, "a") as f:
        line = name + "," + str(score) + "\n"
        f.write(line)


save_results("results.txt", students)
append_student("results.txt", "David", 79)
```

Run this and then open `results.txt` in any text editor to confirm the four lines are there. If you run `save_results` a second time, the first three lines will reappear and David's line will disappear — because write mode erases first [1][3].

## 7. Real-World Patterns

### Pattern 1 — Save Program Output to a File (Write Mode)

Write mode is the go-to pattern whenever a program generates a complete document or report and needs to save it to disk. Examples from real projects [1][2]:

- A data-processing script reads exam marks, computes per-student averages and a class summary, and writes the summary to `report.txt`. Every time the script runs with updated marks, it regenerates `report.txt` from scratch.
- A prompt-engineering tool builds a refined prompt from user inputs and writes the final prompt to `prompt.txt` so it can be pasted into an LLM interface.
- A grading script produces `grades.csv` each week — one row per student. It always writes the whole file because all marks may have changed.

In each case, the program owns the file completely. It recalculates everything and writes the full file on each run. Write mode (`'w'`) is correct because stale data from previous runs should not persist [3].

**Lab connection:** In the Week 12 lab, after computing averages with the functions from Topics 12.1–12.3, you will write the marks summary to disk using exactly this pattern — `save_results("results.txt", students)` writes the complete output file. This connects the file-writing skills you develop here directly to the lab deliverable [1].

### Pattern 2 — Append a Log Entry (Append Mode)

Append mode suits programs that run repeatedly and need to record what happened each time, building up a history [1][3]:

```python
import datetime

def log_run(log_file, message):
    """Append one timestamped log entry to log_file."""
    timestamp = str(datetime.datetime.now())
    with open(log_file, "a") as f:
        f.write(timestamp + " — " + message + "\n")

log_run("run_log.txt", "Processed 30 students. Average: 82.4")
log_run("run_log.txt", "Processed 31 students. Average: 83.1")
```

After two runs, `run_log.txt` might contain:

```
2026-06-14 09:12:03.451 — Processed 30 students. Average: 82.4
2026-06-14 10:05:22.119 — Processed 31 students. Average: 83.1
```

Each call to `log_run` adds exactly one line. Nothing is overwritten. Over weeks of runs the log grows, giving you an audit trail [2].

This pattern is used widely in production software under the name **logging** — a formal topic covered in later modules. The mechanics here are simple: open in `'a'`, write one line, close. The conceptual point is that append mode lets you grow a file incrementally without disturbing what is already there [3].

Note: `datetime` is a Python standard-library module that provides the current date and time. It is named here only to make the pattern concrete — the full `datetime` API is a later topic. Focus on the `open(..., "a")` and `.write()` parts [2].

## 8. Best Practices

**1. Always use the `with` block.**
Never rely on manually calling `f.close()`. The `with` block guarantees the file is closed — and buffered data flushed to disk — even if an error occurs inside the block [1][2].

```python
# Good
with open("results.txt", "w") as f:
    f.write("Alice,88\n")

# Fragile — if an error happens before f.close(), the file stays open and data may be lost
f = open("results.txt", "w")
f.write("Alice,88\n")
f.close()
```

**2. Think before opening in write mode.**
The instant you call `open("results.txt", "w")`, existing content is gone. A common mistake is opening in write mode inside a loop:

```python
# Bug — opens in write mode on every iteration, erasing previous output
for name, score in students:
    with open("results.txt", "w") as f:   # WRONG: re-erases every loop
        f.write(name + "," + str(score) + "\n")

# Fix — open once, write many times
with open("results.txt", "w") as f:
    for name, score in students:
        f.write(name + "," + str(score) + "\n")
```

The fixed version opens the file once, keeps it open for the whole loop, and closes it when the loop ends [1][3].

**3. Always include `\n` at the end of each line.**
Forgetting the newline character is the most common `.write()` mistake. As a habit, put `\n` at the end of every string that represents a complete line [1][3].

**4. Convert numbers to strings before writing.**
Do not try to write `int` or `float` values directly. Always wrap them in `str()` [2]:

```python
f.write(str(score))            # correct
f.write(str(round(avg, 2)))    # correct — round first, then convert
```

**5. Keep one function per file-writing task.**
Following the single-job principle from Topic 12.3: one function to save results, a separate function to append a log entry. Do not mix the two concerns in one function [1].

**6. Choose the mode that matches your intent.**
- You want to regenerate the whole file → `'w'`
- You want to add to an existing file → `'a'`
- When in doubt, think: "Do I want to keep what is already in the file?" If yes, use `'a'` [2].

**7. Error handling comes later.**
If the path is invalid or permissions are denied, Python raises an `IOError`. Handling that with `try/except` is covered in Topic 12.8. For now, use paths you know are valid [3].

## 9. Hands-On Exercise

Work through these steps in a Python file or interactive session:

1. Create a list of three tuples: `[("Alice", 88), ("Bob", 74), ("Carol", 91)]`.
2. Use a `with open("my_results.txt", "w")` block and a `for` loop to write each tuple as a line in the format `Name,Score\n`.
3. Open `my_results.txt` in a text editor (or use `print(open("my_results.txt").read())` in Python) to verify the three lines are there and separated correctly.
4. Call `open("my_results.txt", "w")` again — immediately close it without writing anything — then check the file. Observe that it is now empty. This is the write-mode gotcha in action.
5. Rebuild the file (step 2 again), then use `open("my_results.txt", "a")` to add a fourth student, `("David", 79)`. Verify all four lines are present.
6. Wrap steps 2 and 5 in two functions — `save_results(filename, students)` and `append_student(filename, name, score)` — and call them.

## 10. Key Takeaways

- **Write mode (`'w'`) erases first.** Calling `open(filename, "w")` destroys any existing content in the file immediately — before you write a single byte. Use it when you want to regenerate the whole file from scratch.
- **Append mode (`'a'`) adds to the end.** Calling `open(filename, "a")` never erases existing content. It places the bookmark at the end so every `.write()` extends the file. Use it when you want to grow a file incrementally.
- **`.write()` does not add newlines.** You must include `\n` explicitly in every string that should be its own line. Forgetting `\n` is the most common beginner mistake.
- **`.writelines()` writes a list of strings** in one call — but the same newline rule applies: include `\n` in each string in the list.
- **Numbers must be converted to strings** with `str()` before calling `.write()`. Passing a raw number raises a `TypeError`.
- **Use the `with` block** for every file-writing operation. It guarantees the file is closed and flushed, even if an error occurs inside the block.

## 11. Next Steps

_System-derived from the next entry in curriculum/sequence.md._
