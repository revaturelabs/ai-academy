---
topic_id: "11.9"
title: "Edge cases — testing what happens at the boundary of expected input"
position_in_module: 3
generated_at: "2026-06-13T00:08:00Z"
resource_count: 3
---

# Edge Cases — Testing What Happens at the Boundary of Expected Input — Topic Corpus

## 2. Prerequisites

This topic builds directly on:

- **11.6** For loops — repeating an action across a list (lists, iteration, accumulator pattern)
- **11.7** Spec-first discipline (plain-English spec, prompt from spec, spec mismatch)
- **11.8** The golden rule — never run code you cannot explain (silent failure, loud failure, four-question test, code ownership)

Concepts from 11.3 (variables), 11.4 (data types), and 11.5 (if/else) are also assumed and may be referenced without re-definition.

---

## 3. Learning Objectives

By the end of this topic you will be able to:

- Define what an edge case is and explain why boundaries in input expose more bugs than typical inputs do.
- Identify at least three edge-case categories (empty input, zero, maximum/minimum value) for a given function.
- Predict the expected output for an edge-case input before running code.
- Run manual edge-case tests on the week-11 lab script and record whether each test passes or fails.
- Explain the difference between an edge case and a normal case, using your own example.

---

## 4. Introduction

Imagine you are a baker. You write a recipe that says: "For every guest, bake one cupcake." The recipe works perfectly when you have ten guests, twenty guests, or thirty guests. But what happens if you have zero guests? What happens if someone types "one hundred" instead of a number? Your recipe was never tested for those situations.

Code has the same problem. Most beginners test their programs with comfortable, middle-of-the-road inputs — the kind of inputs they were thinking about when they wrote the code. A grade calculator works fine when a student scores 75 out of 100. But what about a score of zero? What about a score of 100? What about a list with no scores at all?

Those uncomfortable inputs — the ones right at the edge of what your code is supposed to handle — are called **edge cases**. Professional programmers test edge cases deliberately, before they hand code to anyone else. In the A4 portfolio assessment (due week 13), you are required to include at least three edge-case tests per notebook. This topic shows you exactly how to find those edge cases and what to do with them. [1]

---

## 5. Core Concepts

### 5.1 What is an edge case?

An **edge case** is an input that sits at or just beyond the boundary of what your code was designed to handle. [1]

Think about a function that calculates the average of a list of marks. The "normal" inputs are lists with several numbers: `[70, 80, 65]`. An edge case is any input that pushes against a limit:

- A list with **no items at all**: `[]`
- A list with exactly **one item**: `[55]`
- A mark of exactly **zero**: `[0, 80, 90]`
- A mark at the **maximum possible value**: `[100, 100, 100]`
- A **negative** number: `[-5, 80, 90]`

Each of these is at a boundary. Your code may handle the normal case perfectly and still break on every one of these. [1][2]

**Edge case in plain language:** an input your code might never have been tested with, because it is at an extreme or an unusual limit of the expected range.

Here is a second analogy that uses a different kind of boundary. Imagine a function that converts a numerical mark into a letter grade: below 70 is F, 70 to 79 is C, 80 to 89 is B, 90 and above is A. A student who scores 75 lands cleanly in the C band — no surprises. A student who scores exactly 80 stands right on the line between C and B. That dividing line is an edge case. Whatever logic your code uses to decide "which side of 80 is this?", it must be exactly right. A score of 80 might be the only input in the whole valid range that triggers a mismatch between what the spec says and what `>=` versus `>` actually does in code. Every grade boundary in that switch — 70, 80, and 90 — is its own edge case, and each one deserves its own test. [1][2]

### 5.2 Normal inputs versus edge-case inputs

To find edge cases, you first need to think clearly about what "normal" looks like. Researchers and educators call this an **equivalence class** — a group of inputs that all behave the same way inside your code. [1][2]

Here is an example for a function that prints a letter grade given a mark out of 100:

| Group | Example inputs | What they have in common | What the code does |
|---|---|---|---|
| Normal passing marks | 60, 70, 75, 85, 90 | All likely to produce A, B, or C without surprises | Falls into a middle branch of the if/else chain cleanly; no boundary is touched |
| Exactly the boundary between grades | 70, 80, 90 | Right on the dividing line between two grades | Triggers the exact comparison operator in your condition — `>=` vs `>` decides the outcome here |
| Minimum valid input | 0 | The lowest mark a student can receive | Forces the code down the F branch and tests whether zero is handled as a real mark, not as "no data" |
| Maximum valid input | 100 | The highest mark a student can receive | Tests whether the A branch accepts 100 and whether any formatting or arithmetic produces unexpected output at the top of the range |
| Invalid input | -1, 101, "hello" | Outside the defined range entirely | May produce a wrong letter grade silently, or crash loudly — either way, the code's behaviour here should be a conscious decision |

Edge cases live at the borders between these groups. When input crosses from one group to another, that is where bugs hide. [2]

Testing one value from the middle of each group confirms that group works. But only testing right at the border confirms the boundary logic is correct. A bug at the boundary between "passing" and "failing" could affect every student who scores exactly 70. That is not a rare input — in any real class it will happen. [1][2]

**Equivalence class in plain language:** a set of inputs that your code treats the same way. You only need to test one input from the middle of each group. You must test inputs right at the border.

**Boundary value in plain language:** the specific input that sits exactly on the line between two groups. Boundary values are the most important edge cases to test. [1]

### 5.3 Why edges expose bugs

This is the key insight: bugs do not usually hide in the middle of normal inputs. They hide at the edges. [1][2]

Here is why. When you write an if/else condition — for example, `if mark >= 70:` — you had a particular number in mind. But what about exactly 70? Is that included or not? What about 69? These questions are easy to answer wrong, and easy to miss when you only test with inputs like 75 or 80.

Consider this code:

```python
def grade(mark):
    if mark > 70:
        return "B"
    else:
        return "C"
```

Test it with 75 — it returns "B". That seems right. Test it with 60 — it returns "C". That seems right too. But test it with exactly 70 — it returns "C". Is that what the spec said? If the spec says "70 and above is a B", then this code has a bug, and only the edge case of 70 would catch it. [2]

This type of error — where code is wrong by exactly one step at the boundary — is called an **off-by-one error**. Off-by-one errors are one of the most common bugs in all of programming, and they almost always live at edge cases. [1]

Here is a second, different situation where an off-by-one error appears. Suppose your script is supposed to print a congratulations message for any student who scores above the class average, and the class average happens to be 72.5. Your code uses `if student_score > 72.5:`. A student who scores exactly 72.5 will not see the congratulations message — they are excluded by the strict `>`. If the spec says "above or equal to the average", the correct operator is `>=`. Without testing the exact average as an input, you would never discover this. Normal test inputs — scores like 65 or 80 — would pass and pass and pass, while the boundary value of 72.5 silently applies the wrong rule. [1][2]

Both examples follow the same pattern: a condition that is off by one operator (`>` instead of `>=`, or vice versa) produces wrong output for exactly the inputs that sit on the boundary — and those inputs are real, not exotic.

### 5.4 The three most common edge-case categories

For the kinds of programs you write in this course, three categories of edge cases come up again and again. [1][3]

**1. Empty input**

What happens when there is nothing at all?

- An empty list: `[]`
- An empty string: `""`

For a grade-averaging script, an empty list of marks is a genuine edge case. If your code tries to compute the sum divided by the length of an empty list, Python will stop with a division-by-zero error because `len([])` is 0, and dividing any number by 0 is undefined. That is a **loud failure** (a term from topic 11.8) — Python tells you something went wrong with a clear error message in the output. But if your code has a different structure — for example, it accumulates a sum with a loop and then uses a pre-set default — it might produce a wrong answer of 0.0 silently and keep running. Empty input is the category most likely to produce one of these two extremes: a crash or a silent wrong answer. [3]

**2. Zero**

Zero is different from "nothing". A mark of zero is a real mark — a student may legitimately score zero. But zero causes special behaviour in arithmetic. Dividing by zero is undefined. A sum of zero may look like "no data" to your code even when there is one item. In Python, the integer `0` and the float `0.0` are both **falsy** — meaning that an `if score:` check treats zero the same as False, which can cause your code to skip processing a perfectly valid mark. Always ask: what happens when a number input is zero? The answer reveals whether your code treats zero as a special signal or as a legitimate value. [3]

**3. Minimum and maximum values**

Every range has endpoints. For a mark-out-of-100 system, the endpoints are 0 and 100. Test both. For a list of three students, test what happens with exactly one student. Test what happens with the largest number of students allowed. At the maximum end, some formatting choices can produce unexpected output — for example, an average of 100.0 printed with a format string intended for two-digit numbers may display differently than expected, shifting columns in a printed table. These are not catastrophic bugs, but they are exactly the kind of thing an assessor or a user will notice. [1][2]

These three categories are not exhaustive, but they cover the majority of edge-case bugs beginners encounter. The primary resource for this topic organises thinking about inputs this way: decide what the normal range is, then deliberately step to its edges. [1]

### 5.5 Predicting expected output before running code

Here is the most important technique in edge-case testing. Before you run your code with an edge-case input, write down what you expect the output to be. [1][2]

This is called a **test prediction**.

If you run the code first and then look at the output, your brain naturally accepts whatever you see as correct. That is a well-known trap. Instead:

1. Read your spec.
2. Ask: for this edge-case input, what does the spec say the output should be?
3. Write that prediction down.
4. Run the code.
5. Compare the actual output to your prediction.

If they match — the test passes. If they do not match — the test fails, and you have found a bug. [2]

The prediction step is what separates a real test from simply "running your code and looking at things". Without a prediction, you cannot know whether the result is correct. This connects directly to the golden rule from topic 11.8: you must understand what your code is doing, not just observe it.

---

## 6. Implementation

This section walks you through exactly how to test edge cases in the week-11 lab script: a program that takes a student name and three marks, then prints the average and a letter grade.

### Step 1 — Read your spec

Before you can identify edge cases, you need a spec (from topic 11.7). Here is a minimal spec for the lab script:

> The script takes a student's name (a string) and three marks (numbers from 0 to 100). It computes the average of the three marks and prints a letter grade: A for 90 and above, B for 80–89, C for 70–79, F for below 70.

Now you have a defined range (0 to 100) and defined boundaries (70, 80, 90). Those boundaries are exactly where you should test. This is why spec-first discipline (topic 11.7) is a prerequisite: you can only identify where the edges are if you have a spec that spells out the range and the rules. A script written without a spec has no defined edges — you would be guessing which inputs to test. [1]

### Step 2 — Identify your edge cases

Ask these questions about your spec:

| Question | Edge case to test |
|---|---|
| What is the lowest valid input? | Marks of 0, 0, 0 |
| What is the highest valid input? | Marks of 100, 100, 100 |
| What happens right at the C/F boundary? | Average of exactly 70 (the C/F line) |
| What happens right at the B/C boundary? | Average of exactly 80 (the B/C line) |
| What if all marks are the same moderate value? | Marks of 50, 50, 50 |

For A4, you need at least three. Choose the three that feel most uncertain to you given your code. You can also push further: "What happens if two marks are the same?" — for example `[70, 70, 80]` — is a valid edge question. In this specific script the average of those three is 73.3, which lands safely in the C band, so it is probably not the most revealing test. But asking the question is good practice: generating candidate edge cases and then deciding which ones are genuinely on a boundary is a skill you build by asking more questions, not fewer. [1][2]

### Step 3 — Write your prediction before running

For each edge case, write your prediction in a code comment or in your journal before you run anything. Writing predictions as code comments — rather than in a separate notebook margin or on paper — is better for three reasons: the prediction stays with the code so it cannot get lost, it survives when you copy your notebook into another environment, and it is visible to the assessor reading your portfolio without any extra explanation. [2]

```python
# Edge case 1: all zeros
# Input: name="Ali", marks=[0, 0, 0]
# Expected average: 0.0
# Expected grade: F  (0 is below 70)
# Prediction: script prints "Ali: average = 0.0, grade = F"

# Edge case 2: average exactly on the 70 boundary
# Input: name="Sam", marks=[70, 70, 70]
# Expected average: 70.0
# Expected grade: C  (spec says 70–79 is C)
# Prediction: script prints "Sam: average = 70.0, grade = C"

# Edge case 3: perfect marks
# Input: name="Zoe", marks=[100, 100, 100]
# Expected average: 100.0
# Expected grade: A  (100 is 90 and above)
# Prediction: script prints "Zoe: average = 100.0, grade = A"
```

### Step 4 — Run and compare

Run the script with each set of edge-case inputs. After each run, record what you actually observed:

```
Edge case 1 result: "Ali: average = 0.0, grade = F"  →  PASS
Edge case 2 result: "Sam: average = 70.0, grade = F"  →  FAIL (expected C, got F)
Edge case 3 result: "Zoe: average = 100.0, grade = A"  →  PASS
```

A failing test is the point. You have found a bug before anyone else sees it. Go back to your code and check the condition at the 70 boundary. If the code says `if average > 70:`, that is the bug — it excludes the value 70 itself. Change it to `if average >= 70:` and the boundary now includes 70, which matches the spec's rule that 70–79 is a C. Re-run the edge case to confirm the fix works. [1]

### Step 5 — Record the outcome

For A4, you must show your edge-case tests in your notebook. Write them in a dedicated cell, with:

- The input you tested
- Your prediction
- The actual output
- Pass or Fail

That record is what the assessor will look for. Honest documentation of a failure — with an explanation of where the bug is — scores better than pretending the test never happened. A model journal entry might read: "Edge case 2 FAILED: the script returned grade F for an average of 70.0, but the spec requires C. The bug is `> 70` on line 12; the correct operator is `>= 70`." That sentence shows the assessor that you understood the bug, not just that you ran the code. [1][2]

---

## 7. Real-World Patterns

Professional developers think about edge cases before they write a single line of code. When a developer receives a specification, one of their first questions is: "Where are the boundaries in this input?" [1]

In AI engineering — the broader context of this course — edge cases matter enormously. An AI pipeline is a chain of functions. Each function takes inputs. If an upstream function passes an empty list or a zero to a downstream function, the whole chain can fail silently. Silent failure (from topic 11.8) is especially dangerous in this context, because the pipeline may keep running and produce plausible-looking wrong output without any warning. [3]

A practical professional habit: after writing any function, ask yourself "what is the most inconvenient input someone could give this?" Then test it. This question alone will catch a large fraction of real-world bugs. [3]

When a professional finds a failing edge-case test, finding the failure is only the beginning. The next step is to fix the condition — for example, changing `> 70` to `>= 70` — and then re-run every test in the set, not just the one that failed. This second re-run checks that the fix did not accidentally break a test that was passing before. Professionals call this a regression check (a formal testing concept you will cover later); in a small lab script you can do this by hand in under a minute. [1][3]

When you present your portfolio for A4, the assessor reading it is doing something structurally similar to a code review. A reviewer's first questions are not "does the normal case work?" — they assume it does. Their first questions are "did you test zero? did you test the boundary values? what happens with an empty list?" If your portfolio shows documented edge-case tests with written predictions, you are answering those questions before they are asked. If the portfolio shows only tests of comfortable middle values, it signals that boundaries were not considered. Documenting your edge-case thinking explicitly is therefore both good engineering practice and good evidence of understanding. [1][2]

Large technology teams use automated test frameworks — named pytest and unittest in Python — to run edge-case tests automatically every time code changes. You will not use those frameworks in this course (they are a topic for later in your learning). But the thinking is identical. Every automated test was written by a developer who sat down and predicted: "For this input, I expect this output." [1]

---

## 8. Best Practices

**Do:**

- Write your prediction BEFORE you run the code. This is the single most important habit in edge-case testing. [2]
- Test the minimum valid input (e.g., 0, one item in a list).
- Test the maximum valid input (e.g., 100, the largest allowed value).
- Test every boundary where your if/else conditions switch (e.g., exactly 70, exactly 80, exactly 90 in the grade script).
- Record each test — input, prediction, actual output, and pass/fail — in your notebook.
- Fix failing tests before submitting. If you cannot fix one, explain where the bug is.

**Do not:**

- Do not skip edge-case testing because the normal case works. Normal passing tells you almost nothing about boundaries.
- Do not look at the output first and then decide what you "expected". That defeats the purpose of the prediction. [2]
- Do not only test the value you were thinking of when you wrote the code. That value is the least likely to reveal a bug.
- Do not ignore a failing test and submit without noting it. A4 rewards honest documentation over hidden failures.

---

## 9. Hands-On Exercise

This exercise corresponds directly to Step 4 of the week-11 lab (Journal Entry #6).

**Setup:** You have the grade-calculator script from the lab. It takes a student name and three marks, computes the average, and prints a letter grade (A/B/C/F).

**Task:** Run the three edge-case tests below. For each one, write your prediction first, then run the script, then record the result.

| # | Input | Your prediction (write before running) | Actual output | Pass / Fail |
|---|---|---|---|---|
| 1 | name = "Test", marks = [0, 0, 0] | _Write here_ | _Run and fill_ | _Fill_ |
| 2 | name = "Test", marks = [70, 70, 70] | _Write here_ | _Run and fill_ | _Fill_ |
| 3 | name = "Test", marks = [100, 100, 100] | _Write here_ | _Run and fill_ | _Fill_ |

**Reflection for Journal Entry #6:** After completing the three tests, answer in one or two sentences: Did any test fail? If yes — which condition in your code was wrong, and what did you change to fix it?

---

## 10. Key Takeaways

- An **edge case** is an input at the boundary of your function's expected range — such as zero, an empty list, or the exact value where a condition switches. [1]
- Bugs hide at boundaries. Code that works perfectly on normal inputs can fail on edge inputs — often silently. [1][2]
- Always write your **test prediction** before running the code. A test without a prediction is not a test — it is just running code. [2]
- The three most reliable edge cases to check are: **empty input**, **zero**, and **minimum/maximum values**. [1][3]
- For A4, each notebook must include at least three documented edge-case tests — with inputs, predictions, and outcomes. This is a graded requirement.

---

## 11. Next Steps

_System-derived from the next entry in curriculum/sequence.md._
