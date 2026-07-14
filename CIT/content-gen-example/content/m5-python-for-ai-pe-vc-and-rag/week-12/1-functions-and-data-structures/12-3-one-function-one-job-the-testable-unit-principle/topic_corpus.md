---
topic_id: "12.3"
title: "One function = one job — the testable unit principle"
position_in_module: 3
generated_at: "2026-06-14T00:00:00Z"
resource_count: 3
---

# 1. One Function = One Job — The Testable Unit Principle — Topic Corpus

## 2. Prerequisites

This topic builds directly on Topics 12.1 and 12.2:

- **12.1 — Functions:** you can define a function with the `def` keyword and call it by name.
- **12.2 — Parameters and return values:** you can write functions that accept input and hand a result back to the caller.

Supporting background from Week 11:

- **11.7 — Spec-first discipline:** you know how to write a plain-English spec before writing any code.
- **11.9 — Edge cases:** you know that good code is tested at the boundaries of expected input.

## 3. Learning Objectives

By the end of this topic you will be able to:

1. Explain what it means for a function to have **one job**, and why that matters for testing.
2. Identify a function that is doing **more than one job** by reading its body and its name.
3. Use the **"and" naming heuristic** to detect multi-job functions before writing or reviewing code.
4. **Refactor** a multi-job function into two or more single-job functions that can each be tested independently.
5. Write a short, spec-first **manual test** for a single-job function using what you already know (call the function, compare the result to an expected value).

## 4. Introduction

You have written functions that define a named block of logic (12.1) and functions that accept input and return a result (12.2). Now a question arises: how much should one function do?

Imagine you ask a colleague to "get the coffee, greet every team member, update the spreadsheet, and send the daily email." That colleague does all four things — but if something goes wrong, which of the four caused the problem? You have no way to check "step 2" in isolation. You have to redo all four steps together to reproduce the bug.

Functions have the same problem. A function that does three things at once is hard to test, hard to fix, and hard to reuse. When you break it into three smaller functions — each doing exactly one thing — you can test and fix each piece independently.

This idea has a formal name: the **Single Responsibility Principle (SRP)**. It states that every piece of code should have one, and only one, reason to change [1]. In Week 12's lab you will write functions that read marks, compute averages, and write a summary file. Keeping those three responsibilities in separate functions is what makes each one testable on its own [1][2].

The "one function = one job" rule is the most practical version of SRP for beginner Python code. It does not require any advanced framework — just discipline about what each `def` block is asked to do [1][3].

## 5. Core Concepts

### 5.1 What "One Job" Means

A function has **one job** when its entire body is devoted to a single, clearly stated purpose [1]. You can describe that purpose in a single short sentence without using the word "and."

Examples of single-job functions:

| Function name | Job in one sentence |
|---|---|
| `compute_average(marks)` | Return the average of a list of marks. |
| `find_highest(marks)` | Return the largest value in a list of marks. |
| `classify_mark(mark)` | Return "Pass" or "Fail" for a given mark. |
| `write_average_to_file(average, filename)` | Write the average value to a file. |

Each function has one clear output and one clear responsibility. You can describe it without "and" [1][2].

A function does **more than one job** when its body mixes two or more of these concerns:

- Computing a value **and** saving it to a file
- Fetching data **and** formatting it for display
- Validating input **and** processing it **and** printing the result

When you find yourself writing "and" in your spec comment, that is a signal to split [1][3].

### 5.2 The "And" Naming Heuristic

The simplest tool for catching a multi-job function before it causes problems is to look at what you would naturally name it [3].

If the most accurate name for a function contains the word "and," the function probably has more than one job [1][3].

Examples:

| Name you are tempted to write | What the "and" reveals |
|---|---|
| `compute_and_print_average` | Two jobs: compute, then print. |
| `validate_and_save_mark` | Two jobs: validate, then save. |
| `fetch_and_format_results` | Two jobs: fetch data, then format it. |
| `read_file_and_calculate_stats` | Two jobs: read, then calculate. |

The fix is always the same: split the function at the "and" into two single-job functions, each with a clean name [1][3].

This heuristic is not a rule that bans the word "and" — it is a **smell detector** [3]. If you notice "and" appearing in the best name you can think of, pause and ask whether one function is doing two separate things.

**Smell** — in programming, a "smell" (sometimes "code smell") is a sign in the code that something might be wrong. It does not guarantee a bug, but it tells you to look closer. You will encounter this term throughout your career [3].

### 5.3 Why Single-Job Functions Are Testable

A function that does one job is **testable** because:

1. **The input and output are clear.** You know exactly what to pass in and exactly what value to compare the result against.
2. **Nothing else runs at the same time.** If the result is wrong, the problem is inside this one function — not somewhere else in a chain of mixed concerns.
3. **You can test it in isolation.** You do not need to set up the whole program to check whether `compute_average([60, 80, 100])` returns `80.0`. You just call it and look [1][2].

Compare that to a multi-job function like `compute_and_save_average(marks, filename)`. To test whether the average is correct, you also have to create a file, read it back, and check the file contents — even though you only care about the calculation. The responsibilities are tangled [1].

**Testable unit** — a piece of code small enough and focused enough that you can confirm it works by calling it once with a known input and checking the output [1][2]. A single-job function is a testable unit. A multi-job function usually is not.

In this course you will test functions manually: call the function, print the result, compare it to the expected value by eye. More powerful testing tools (like pytest — which you will encounter in later study) automate this check. But the principle is identical: one function, one job, one check [1].

### 5.4 How to Identify a Multi-Job Function

There are three reliable ways to spot a function that is doing too much.

**1. The "and" test on the name.**
Try to write a one-sentence spec for the function. If the sentence needs "and," the function has more than one job [1][3].

**2. The body has visibly separate phases.**
Look at the function body. If you can draw a horizontal line between "the part that computes" and "the part that saves" — or "the part that validates" and "the part that transforms" — those are two separate jobs [1].

```python
# MULTI-JOB — two phases visible in the body
def process_marks(marks, filename):
    # Phase 1: compute
    total = 0
    for mark in marks:
        total = total + mark
    average = total / len(marks)

    # Phase 2: write to file
    file = open(filename, "w")
    file.write("Average: " + str(average) + "\n")
    file.close()
```

Each phase belongs in its own function [1].

**3. The function is hard to call in a test.**
If you have to create a file, connect to a database, or set up another system just to call the function once in a test, the function is mixed with things that are not its core job [2].

### 5.5 Refactoring — Splitting One Function Into Two

**Refactoring** — changing how code is structured without changing what it does [3]. When you split a multi-job function into single-job functions, the program still produces the same result — but each piece is now independently testable.

The refactoring pattern for "one function doing two jobs" is always the same:

1. **Identify the two jobs.** Find the "and" in the spec, or the visible phase boundary in the body.
2. **Write a spec comment for each new function.** One sentence, no "and."
3. **Extract each phase into its own `def` block**, using `return` to pass the result from the first function to the second.
4. **Replace the original body** with two calls: one to the first new function, one to the second.
5. **Test each new function independently** before testing them together.

You will see this pattern applied in the Implementation section below [1][3].

## 6. Implementation

### Worked Example: From Multi-Job to Single-Job

**Goal:** compute the average of a list of marks, then write the result to a summary file.

---

**Step 1 — Write the multi-job version first, so you can see the problem clearly.**

```python
# compute_and_save_average: given a list of marks and a filename,
# compute the average AND write it to the file
def compute_and_save_average(marks, filename):
    total = 0
    for mark in marks:
        total = total + mark
    average = total / len(marks)
    file = open(filename, "w")
    file.write("Average: " + str(average) + "\n")
    file.close()
```

The "and" in the name, and the two visible phases in the body, are the signal [1][3].

---

**Step 2 — Identify the two jobs.**

- Job 1: compute the average (pure calculation, needs `marks`, returns a number).
- Job 2: write the average to a file (file I/O, needs the average value and a filename, returns nothing useful).

---

**Step 3 — Write a spec for each new function.**

```python
# compute_average: given a list of marks, return their average (sum / count)
# write_average_to_file: given a number (average) and a filename,
#                        write the average to the file
```

Neither spec contains "and" [1].

---

**Step 4 — Write the two single-job functions.**

```python
# compute_average: given a list of marks, return their average (sum / count)
def compute_average(marks):
    total = 0
    for mark in marks:
        total = total + mark
    return total / len(marks)


# write_average_to_file: given a number (average) and a filename,
# write the average to the file
def write_average_to_file(average, filename):
    file = open(filename, "w")
    file.write("Average: " + str(average) + "\n")
    file.close()
```

Each function does exactly one thing. Each has a name with no "and" [1][3].

---

**Step 5 — Combine them at the call site.**

```python
class_marks = [72, 88, 65, 90, 55]
avg = compute_average(class_marks)
write_average_to_file(avg, "summary.txt")
```

The program still produces the same result. But now you can test `compute_average` without touching a file [1][2].

---

**Step 6 — Test each function independently.**

```python
# Test compute_average in isolation — no file needed
result = compute_average([60, 80, 100])
print(result)           # expected: 80.0

result = compute_average([50, 50])
print(result)           # expected: 50.0

result = compute_average([100])
print(result)           # expected: 100.0
```

All three tests call the function with a known list and print the result. You compare by eye. No file involved, no other function running [2].

If `compute_average` passes all three tests, you know the computation is correct. Now you can test `write_average_to_file` separately — and if a bug appears in the file-writing step, you know immediately that `compute_average` is not the cause [1].

---

**Complete refactored version:**

```python
# compute_average: given a list of marks, return their average (sum / count)
def compute_average(marks):
    total = 0
    for mark in marks:
        total = total + mark
    return total / len(marks)


# write_average_to_file: given a number (average) and a filename,
# write the average to the file
def write_average_to_file(average, filename):
    file = open(filename, "w")
    file.write("Average: " + str(average) + "\n")
    file.close()


# --- call site ---
class_marks = [72, 88, 65, 90, 55]
avg = compute_average(class_marks)
write_average_to_file(avg, "summary.txt")
print("Done. Average was:", avg)
```

## 7. Real-World Patterns

The one-function-one-job rule appears in every real Python project [1][2].

**Pattern 1 — Three separate statistics functions (the lab activity pattern).**

The Week 12 lab asks you to compute average, highest, and lowest marks. Keeping those three computations in three separate functions lets you test each independently — and reuse them in any order [1][2]:

```python
# compute_average: given a list of marks, return their average
def compute_average(marks):
    total = 0
    for mark in marks:
        total = total + mark
    return total / len(marks)


# find_highest: given a list of marks, return the largest value
def find_highest(marks):
    highest = None
    for mark in marks:
        if highest is None or mark > highest:
            highest = mark
    return highest


# find_lowest: given a list of marks, return the smallest value
def find_lowest(marks):
    lowest = None
    for mark in marks:
        if lowest is None or mark < lowest:
            lowest = mark
    return lowest


# --- call site ---
class_marks = [72, 88, 65, 90, 55]
print("Average:", compute_average(class_marks))   # 74.0
print("Highest:", find_highest(class_marks))      # 90
print("Lowest: ", find_lowest(class_marks))       # 55
```

Each function can be tested independently with a small hand-crafted list — no file required [1][2]. The `highest = None` starting point uses a flag introduced in Topic 12.2: `None` means "we have not seen any mark yet," so the first mark in the loop always replaces it.

**Pattern 2 — Validation separated from processing.**

Mixing validation and processing in one function is a common source of bugs [3]:

```python
# MULTI-JOB — validates AND classifies in the same function
def validate_and_classify(mark):
    if mark < 0 or mark > 100:
        print("Invalid mark:", mark)
        return None
    if mark >= 50:
        return "Pass"
    else:
        return "Fail"
```

Split it into two single-job functions:

```python
# is_valid_mark: given a mark, return True if it is between 0 and 100, else False
def is_valid_mark(mark):
    if mark >= 0 and mark <= 100:
        return True
    else:
        return False


# classify_mark: given a valid mark, return "Pass" or "Fail"
def classify_mark(mark):
    if mark >= 50:
        return "Pass"
    else:
        return "Fail"


# --- call site ---
raw_mark = 73
if is_valid_mark(raw_mark):
    outcome = classify_mark(raw_mark)
    print(raw_mark, "->", outcome)
else:
    print("Invalid mark:", raw_mark)
```

Now you can test `is_valid_mark` on edge cases (0, 100, -1, 101) without running any classification logic — and vice versa [1][3].

## 8. Best Practices

**Do:**

- **Write the spec comment first, before the function body.** If you cannot write the spec in one sentence without "and," split the function before you write any code [1][2].
- **Use the "and" test as your first check.** Before you finalise a function name, ask: does the most accurate name contain "and"? If yes, split [3].
- **Test each single-job function independently before combining them.** Call it with two or three known inputs and compare the result to your expectation [1][2].
- **Pass results between functions using return values.** A single-job function returns its result; the caller passes that result to the next function. Shared global variables that both functions read and write are a sign of tangled concerns [1].
- **Name each function for what it does, not how it does it.** `compute_average` is better than `loop_and_divide` [2][3].

**Do not:**

- **Do not add "also" to a function's purpose.** "This function computes the average — and also saves it." That "also" is the smell. Split it [1][3].
- **Do not mix I/O (reading a file, printing to screen) with pure computation inside the same function.** Computation is easy to test with made-up data. I/O is harder. Keep them separate [1][2].
- **Do not interpret "one job" as "one line of code."** A function can be ten lines long and still have one job if every line is part of that same purpose. Length is not the issue — mixed responsibilities are [1].
- **Do not refactor prematurely.** Write the working multi-job version first if you need to think it through. Then split once the logic is clear. Refactoring a working function is safer than designing an imaginary split upfront [3].

| Anti-pattern | What it looks like | Fix |
|---|---|---|
| "and" in the name | `fetch_and_display_results` | Split at the "and" into two functions |
| Two visible phases in the body | Compute block, then file-write block | Extract each phase to its own `def` |
| Hard to test without setup | Must create a file to test a calculation | Separate the calculation from the file I/O |
| "also" inside the spec comment | "compute the average — also write it" | That "also" = a second job; split |

## 9. Hands-On Exercise

Open your Colab notebook.

1. Write this multi-job function exactly as shown — do not fix it yet:

```python
def score_and_print(marks):
    total = 0
    for mark in marks:
        total = total + mark
    average = total / len(marks)
    if average >= 50:
        print("Class result: Pass — average", average)
    else:
        print("Class result: Fail — average", average)
```

2. Apply the "and" test to the name. Write a comment identifying the two jobs.
3. Refactor into two functions: `compute_average(marks)` and `print_class_result(average)`. Write a spec comment for each.
4. Test `compute_average` with three inputs: `[60, 80, 100]` (expect `80.0`), `[40, 40]` (expect `40.0`), `[100]` (expect `100.0`).
5. Test `print_class_result` by calling it with `80.0` (expect a "Pass" line) and `40.0` (expect a "Fail" line).
6. Confirm the combined call `print_class_result(compute_average([60, 80, 100]))` produces the same output as the original `score_and_print`.

## 10. Key Takeaways

- A function has **one job** when its entire body serves a single, clearly stated purpose that you can describe in one sentence without using "and."
- The **"and" naming heuristic** is the fastest way to catch a multi-job function: if the most accurate name for the function contains "and," the function likely has two responsibilities that should be separated.
- A **testable unit** is a function small enough and focused enough that you can confirm it works by calling it once with a known input and comparing the output — no other system setup needed.
- **Refactoring** a multi-job function means splitting it at the "and" boundary, extracting each phase into its own `def` with a clean spec, and passing results between them using return values. The program produces the same result; each piece is now independently testable.
- Mixing I/O (file reads, prints) with pure computation in one function makes both harder to test. Keeping them separate is the most practical application of the one-job rule in this week's lab.

## 11. Next Steps

_System-derived from the next entry in curriculum/sequence.md._
