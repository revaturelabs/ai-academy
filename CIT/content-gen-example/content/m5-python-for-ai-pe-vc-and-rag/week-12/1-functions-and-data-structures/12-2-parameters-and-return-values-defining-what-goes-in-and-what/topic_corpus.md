---
topic_id: "12.2"
title: "Parameters and return values — defining what goes in and what comes out"
position_in_module: 2
generated_at: "2026-06-14T00:00:00Z"
resource_count: 3
---

# 1. Parameters and Return Values — Defining What Goes In and What Comes Out — Topic Corpus

## 2. Prerequisites

This topic builds directly on Topic 12.1:

- **12.1 — Functions:** you know how to define a function with the `def` keyword, call it by name, and recognise the difference between defining and calling.

Supporting background from Week 11:

- **11.3 — Variables:** you can name and store a value with `=`.
- **11.4 — Data types:** you know strings, integers, floats, and booleans.

If you are comfortable with those topics, you are ready.

## 3. Learning Objectives

By the end of this topic you will be able to:

1. Distinguish between a **parameter** (the placeholder in the definition) and an **argument** (the actual value passed in the call).
2. Write a function that accepts one or more positional parameters.
3. Write a function that uses the `return` keyword to send a value back to the caller.
4. Assign the value returned by a function to a variable and use it in further code.
5. Explain what Python produces when a function has no `return` statement (implicit `None`).
6. Identify when a function should return a value versus when it only needs to print.

## 4. Introduction

In Topic 12.1 you learned to write functions — named blocks of code you can call by name. The functions you wrote there were like light switches: flip the switch and the same thing happens every time. Useful, but limited.

Most real tasks are more like a calculator than a light switch. You type *in* two numbers, the calculator does something with them, and a result comes *back* out. To turn your Python functions into calculators you need two ideas: **parameters** (what goes in) and **return values** (what comes out).

Consider the lab activity for this week: you will work with a list of student marks and compute the average, the highest mark, and the lowest mark. You could hard-code every mark directly inside the function — but then the function only works for that one set of marks. With parameters, you write the function once and pass in any list of marks at call time. With a return value, the computed average comes back to you so you can store it, print it, or compare it to a threshold.

These two ideas — parameters and return values — are what let you build functions that are genuinely reusable tools [1][2].

## 5. Core Concepts

### 5.1 Parameters and Arguments

#### 5.1.1 The Terminology

Beginners often hear "parameter" and "argument" used interchangeably, even by experienced programmers [2]. They are almost the same thing, but there is a useful distinction worth knowing:

- A **parameter** is the named placeholder you write in the function definition. It is the slot [2].
- An **argument** is the actual value you pass when you call the function. It is what goes into the slot [2].

Think of a vending machine. The machine has a *slot* (parameter) — any coin fits there. When you push a specific coin in (argument), that is the value the machine works with [2].

The difference is about *where you are standing*:
- Inside the `def` line → you are looking at **parameters**.
- At the call line → you are passing **arguments** [2].

```python
# "name" is the PARAMETER — the placeholder in the definition
def greet(name):
    print("Hello,", name)

# "Alice" is the ARGUMENT — the actual value passed in the call
greet("Alice")
```

You will often hear both words used for the same concept, and that is fine [2]. What matters is that you understand the mechanism: you write a placeholder in `def`, you pass a real value at the call.

#### 5.1.2 Writing a Function with a Parameter

Add a parameter inside the parentheses on the `def` line, right where the empty `()` used to be [2]:

```python
def greet(name):
    print("Hello,", name)
```

`name` is now a variable that exists inside the function [2]. When you call `greet("Alice")`, Python sets `name = "Alice"` automatically before running the body.

```python
greet("Alice")    # prints: Hello, Alice
greet("Bob")      # prints: Hello, Bob
greet("Carol")    # prints: Hello, Carol
```

The same function, three different results — because the argument changed each time [2]. This is the core value of parameters: **one definition, many different inputs** [2][3].

#### 5.1.3 Positional Parameters

When a function has more than one parameter, Python matches arguments to parameters **by position** — the first argument goes to the first parameter, the second to the second, and so on [2]. These are called **positional parameters** [2].

```python
def describe_student(name, mark):
    print(name, "scored", mark)

describe_student("Alice", 87)   # name="Alice", mark=87
describe_student("Bob", 92)     # name="Bob",   mark=92
```

Order matters [2]. If you write `describe_student(87, "Alice")`, Python assigns `name=87` and `mark="Alice"` — the wrong way around.

You will learn more flexible ways to pass arguments in later topics (keyword arguments, default values). For now, positional is all you need.

### 5.2 Return Values

#### 5.2.1 What a Return Value Is

Some functions do a job and report back a result. The `return` keyword is how a function sends a value back to whoever called it [1].

```python
def add(a, b):
    return a + b
```

When Python reaches `return a + b`, two things happen simultaneously [1]:
1. The expression `a + b` is evaluated.
2. That value is handed back to the caller and the function stops running immediately.

```python
result = add(3, 4)   # result is now 7
print(result)        # prints: 7
```

Without `return`, there is nothing to capture — the function produces no value [1].

#### 5.2.2 The `return` Keyword

**`return`** — a Python keyword that exits the function and sends a value back to the caller [1].

Rules:
- `return` can appear anywhere in the function body [1].
- When Python hits `return`, it exits the function immediately — no lines after `return` in the same execution path will run [1].
- A function can have multiple `return` statements (for example, one in each branch of an `if`/`else`) [1].

```python
def classify_mark(mark):
    if mark >= 50:
        return "Pass"
    else:
        return "Fail"

outcome = classify_mark(73)
print(outcome)    # prints: Pass
```

Python reaches `return "Pass"` and stops. The `return "Fail"` line does not run for a mark of 73 [1].

#### 5.2.3 Using the Returned Value

The returned value is usable the moment the call finishes [1]. You can:

**Assign it to a variable:**

```python
average = compute_average(marks)
print("Class average:", average)
```

**Use it directly in an expression:**

```python
if compute_average(marks) >= 50:
    print("Class passed on average.")
```

**Pass it to another function:**

```python
print(compute_average(marks))
```

All three patterns are valid [1]. In most cases, assigning to a variable first makes the code easier to read and easier to debug — you can `print(average)` if something goes wrong [1].

#### 5.2.4 Returning Nothing — Implicit `None`

Not every function needs to return a value [1]. If your function only needs to print something, display a report, or write to a file, you may not need `return` at all.

When a function has no `return` statement — or has a bare `return` with nothing after it — Python automatically returns a special value called `None` [1][3].

**`None`** — Python's way of saying "this function produced no value." It is not a number, not a string, not a boolean. It is a placeholder that means "nothing here" [1].

```python
def print_greeting(name):
    print("Hello,", name)
    # no return statement

result = print_greeting("Alice")   # prints: Hello, Alice
print(result)                      # prints: None
```

The function ran, printed the greeting, and returned nothing — so `result` holds `None` [1].

This surprises many beginners [3]. The key question to ask: *Does this function need to hand a value back to the caller?*

- **Prints something / writes to a file / modifies something** → probably no `return` needed [1].
- **Computes something the caller will use** → needs `return` [1].

If you accidentally write:

```python
average = print_greeting("Alice")   # average is None — not what you want!
```

...you have captured `None` instead of a useful number [3]. This is one of the most common beginner mistakes with functions. Always ask: does this function compute something, or does it just do something?

`None` has more uses in Python that you will explore in later topics. For now, the only thing you need to know is: a function that does not `return` anything gives back `None` [1][3].

#### 5.2.5 Return vs. Print — a Common Confusion

These two functions look similar but behave very differently [1]:

```python
def add_print(a, b):
    print(a + b)        # shows the result on screen; returns None

def add_return(a, b):
    return a + b        # sends the result back to the caller; shows nothing by itself
```

```python
# With add_print:
result = add_print(3, 4)   # shows 7 on screen
print(result)              # prints: None  ← not 7!

# With add_return:
result = add_return(3, 4)  # nothing on screen yet
print(result)              # prints: 7  ← correct
```

`print` makes something visible. `return` makes something *usable* [1]. Most functions that compute something should `return` the result and leave the printing to the caller — that way the caller decides whether to print, save, or pass the value onward [1][2].

## 6. Implementation

Here is how to write a complete function with parameters and a return value, step by step.

**Goal:** write a function that computes the average of a list of marks.

---

**Step 1 — Write the plain-English spec first (11.7 discipline).**

```python
# compute_average: given a list of numbers, return their average (sum / count)
```

Commit to what goes in and what comes out before writing any code [2]. This "spec-first" habit makes it much easier to test your function after you write it.

---

**Step 2 — Write the `def` line with parameters.**

Decide what the function needs to receive. Here: a list of marks [2].

```python
def compute_average(marks):
```

`marks` is the parameter — a placeholder [2]. You do not know yet what list will be passed; that is fine.

---

**Step 3 — Write the body using the parameter.**

Inside the body, use `marks` as if it is an ordinary variable holding a list — because when the function runs, it will be exactly that [2].

```python
def compute_average(marks):
    total = 0
    for mark in marks:
        total = total + mark
    average = total / len(marks)
```

This uses the for loop (11.6) and variables (11.3) you already know [2]. `len(marks)` gives the number of items in the list — a built-in that tells you the length.

---

**Step 4 — Add the `return` statement.**

The caller needs the computed average, so return it [1].

```python
def compute_average(marks):
    total = 0
    for mark in marks:
        total = total + mark
    average = total / len(marks)
    return average
```

Without `return average`, the computed value would be lost the moment the function finishes [1].

---

**Step 5 — Call the function, passing an argument.**

```python
class_marks = [72, 88, 65, 90, 55]
result = compute_average(class_marks)
print("Average:", result)
```

`class_marks` is the argument — the actual list passed to the `marks` parameter [2]. The function runs with that data and returns the average into `result`.

---

**Step 6 — Read the output and verify.**

Expected output:
```
Average: 74.0
```

---

**Step 7 — Test with a different argument (11.9 edge-case thinking).**

```python
another_group = [40, 40, 40]
print("Average:", compute_average(another_group))   # expects 40.0
```

Same function, different data [2]. The parameter made this possible without rewriting anything [2][3].

---

**Complete working version:**

```python
# compute_average: given a list of numbers, return their average (sum / count)
def compute_average(marks):
    total = 0
    for mark in marks:
        total = total + mark
    average = total / len(marks)
    return average

class_marks = [72, 88, 65, 90, 55]
result = compute_average(class_marks)
print("Average:", result)          # Average: 74.0
```

## 7. Real-World Patterns

Parameters and return values are the bread and butter of every Python script you will write in this course [1].

**Pattern 1 — Computing a summary statistic.**

The lab activity asks you to compute average, highest, and lowest marks. With parameters and return values, you write three clean, testable functions [1][3]:

```python
# compute_average: return the mean of a list of marks
def compute_average(marks):
    total = 0
    for mark in marks:
        total = total + mark
    return total / len(marks)

# find_highest: return the largest value in the list
def find_highest(marks):
    highest = None
    for mark in marks:
        if highest is None or mark > highest:
            highest = mark
    return highest

# find_lowest: return the smallest value in the list
def find_lowest(marks):
    lowest = None
    for mark in marks:
        if lowest is None or mark < lowest:
            lowest = mark
    return lowest
```

Each function does one job, accepts the marks list as an argument, and returns a single number [1]. The `highest = None` starting point uses a flag: `None` means "we have not seen any mark yet." The first mark in the loop always replaces `None` because `highest is None` is true. After that, the comparison `mark > highest` keeps it updated [3]. You can test each function independently before combining them.

**Pattern 2 — A function that builds a report string.**

A function can accept several values as parameters and use a return value to produce a formatted string. The caller decides what to do with that string — print it, store it, or pass it along [1][2]:

```python
# format_report: given a student name and score, return a formatted report string
def format_report(student_name, score):
    outcome = classify_mark(score)
    return student_name + ": " + str(score) + " — " + outcome

line = format_report("Alice", 72)
print(line)    # Alice: 72 — Pass

line = format_report("Bob", 45)
print(line)    # Bob: 45 — Fail
```

`format_report` takes two parameters and hands back a string. The caller (`print(line)`) decides what to do with it. Notice that `format_report` calls `classify_mark` and uses its return value — functions build on each other, each doing one job and passing results to the next [1].

**Pattern 3 — Classify and decide.**

In AI and prompt engineering scripts you often need to classify a value and route accordingly [1]:

```python
# classify_mark: return "Pass" or "Fail" depending on the mark
def classify_mark(mark):
    if mark >= 50:
        return "Pass"
    else:
        return "Fail"

for student_mark in [45, 72, 50]:
    outcome = classify_mark(student_mark)
    print(student_mark, "->", outcome)
```

Output:
```
45 -> Fail
72 -> Pass
50 -> Pass
```

The return value is used immediately inside the loop. No global variables, no printing inside the function — clean separation of concerns [1].

## 8. Best Practices

**Do:**

- **Name parameters to match what they represent.** `marks`, `filename`, `student_name` — not `x`, `y`, `z`. A reader should understand the function just from its `def` line [2].
- **Return a value when the function computes something.** If the caller needs to use the result, `return` it. Let the caller decide whether to print, save, or pass it on [1].
- **Assign the return value to a named variable.** `average = compute_average(marks)` is more readable and debuggable than using the call result directly in a long expression [1].
- **Test your function with multiple arguments immediately after writing it.** Confirm the output changes correctly as the input changes [2].
- **Write your plain-English spec first (11.7).** State what goes in and what comes out before writing any code [2].

**Do not:**

- **Do not `print` inside a function when you should `return`.** Printing inside the function hides the value from the caller. Return it; let the caller print [1].
- **Do not forget to capture the return value.** Writing `compute_average(marks)` without assigning the result to a variable throws the computed average away immediately [1].
- **Do not use vague parameter names.** `def compute_average(x)` works but tells you nothing. `def compute_average(marks)` is immediately clear [2].
- **Do not pass arguments in the wrong order for positional parameters.** `describe_student("Alice", 87)` and `describe_student(87, "Alice")` are both syntactically valid — Python will not warn you — but only the first is correct [2].
- **Do not assume a function that prints also returns something useful.** If you try to capture the result of a `print`-only function, you will get `None` [1][2].

**Common mistake — capturing `None` by accident:**

```python
def show_total(marks):
    total = 0
    for mark in marks:
        total = total + mark
    print("Total:", total)    # prints but returns None

# WRONG — result is None, not a number
result = show_total([70, 80, 90])
print(result + 1)             # TypeError: unsupported operand type(s) for +: 'NoneType' and 'int'

# RIGHT — if you need the total, return it
def compute_total(marks):
    total = 0
    for mark in marks:
        total = total + mark
    return total

total = compute_total([70, 80, 90])
print(total + 1)              # 241
```

The mistake is using `show_total` as if it returns a number. It does not — it only prints [1]. If you need a value back, the function must use `return` [1].

## 9. Hands-On Exercise

Open your Colab notebook from Topic 12.1.

1. Write a spec comment: `# square: given a number, return its square (number * number)`.
2. Define the function `square(number)` that returns `number * number`.
3. Call `square(5)` and assign the result to `result`. Print `result` — expect `25`.
4. Call `square(0)` and print the result — expect `0`. (Edge case: zero.)
5. Call `square(-3)` and print the result — expect `9`. (Edge case: negative number.)
6. Now write a second function with two parameters: `describe_square(number, label)` that prints `label + ": " + str(square(number))`. Call it: `describe_square(4, "Four squared")` — expect `Four squared: 16`.

Notice: `describe_square` calls `square` and uses its return value. This is how functions build on each other — each does one job, passes results to the next.

## 10. Key Takeaways

- A **parameter** is the named placeholder in a function definition (`def greet(name):`). An **argument** is the actual value passed at the call (`greet("Alice")`). The terminology differs; the mechanism is the same: the argument fills the parameter's slot.
- **Positional parameters** are matched by order: the first argument goes to the first parameter, the second to the second. Order matters.
- The **`return` keyword** exits the function and sends a value back to the caller. Code after `return` in the same execution path does not run.
- A function with no `return` statement silently returns **`None`** — Python's way of saying "this function produced no value." Capturing `None` when you expected a number is one of the most common beginner mistakes.
- **`print` makes a value visible; `return` makes a value usable.** Functions that compute results should `return` them and leave printing to the caller.

## 11. Next Steps

_System-derived from the next entry in curriculum/sequence.md._
