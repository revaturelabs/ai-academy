---
topic_id: "11.6"
title: "For loops — repeating an action across a list"
position_in_module: 4
generated_at: "2026-06-13T04:00:00Z"
resource_count: 5
---

# 1. For loops — repeating an action across a list — Topic Corpus

## 2. Prerequisites

This topic builds directly on 11.3 (variables), 11.4 (data types, arithmetic, `print()`), and 11.5 (if/else, comparison operators, `input()`). The indentation rule (4-space body inside a block) carries over unchanged from 11.5 — a `for` loop's body follows exactly the same rule.

One new built-in data structure is introduced here: the **list**. You have seen sequences before — strings are a sequence of characters, and you accessed characters by index (`name[0]`). A list extends that idea to any type of value.

## 3. Learning Objectives

By the end of this topic you will be able to:

1. Create a Python list literal containing values of the same type, and access elements by index using `list[i]` and `len(list)`.
2. Write a `for` loop that visits every item in a list and performs an action on each item, following the 4-space indentation rule.
3. Predict the output of a simple `for` loop from its code — step through it item by item in your head.
4. Use `range(n)` and `range(start, stop)` to generate a sequence of integers and iterate over it with a `for` loop.
5. Apply the accumulator pattern — initialise a total to zero before the loop, add each item inside the loop — to compute a running sum.

## 4. Introduction

The grade-average lab script you have been building since 11.3 uses three separate variables: `mark1`, `mark2`, `mark3`. To compute the total you write `total = mark1 + mark2 + mark3`. This works for exactly three marks. What if the student sat five assessments? Or ten? Rewriting the addition line each time is not a scalable approach [1][2].

A **for loop** solves this. It lets you tell Python: *"For each item in this collection, do the same thing."* Instead of listing marks in separate variables, you store them in a **list** — Python's ordered collection — and loop over the list once. The number of marks can grow without changing a single line of the loop code [1][2].

This pattern — *collect values into a list, loop over them once* — appears everywhere in computing, from grading scripts to batch-processing hundreds of documents through an AI pipeline.

## 5. Core Concepts

### 5.1 Lists — an ordered collection of values

A **list** is a sequence of values enclosed in square brackets and separated by commas [2][5]:

```python
marks = [88, 72, 91]
names = ["Alice", "Bob", "Charlie"]
```

Each value in a list is called an **element**. Elements are stored in order and can be accessed by their **index** — the same zero-based counting you used for string characters in 11.4 [1][2]:

```python
marks = [88, 72, 91]
print(marks[0])   # 88  ← first element
print(marks[1])   # 72  ← second element
print(marks[2])   # 91  ← third element
```

`len()` — already used on strings in 11.4 — works on lists too and returns the number of elements:

```python
print(len(marks))   # 3
```

For this topic, keep all elements in a list the same type (all `int`, all `str`). Lists that mix types are allowed by Python but add complexity covered in a later topic.

### 5.2 The for loop — visiting each item in turn

The `for` statement tells Python: *"Take each item from this sequence, one at a time, assign it to this variable, and run the indented block."* [1][2][3]

```python
marks = [88, 72, 91]
for mark in marks:
    print(mark)
```

Output:
```
88
72
91
```

The structure has four parts:

| Part | Example | What it does |
|---|---|---|
| `for` keyword | `for` | opens the loop |
| loop variable | `mark` | holds the current item each iteration |
| `in` keyword + sequence | `in marks` | the sequence being iterated |
| colon + indented body | `: print(mark)` | the code that runs once per item |

Python processes the loop step by step:
1. Takes the first element of `marks` (88), assigns it to `mark`, runs the body (`print(mark)` → prints 88).
2. Takes the second element (72), assigns it to `mark`, runs the body again.
3. Takes the third element (91), assigns it to `mark`, runs the body again.
4. No more elements — loop ends [1][2].

The loop variable name (`mark` above) is chosen by you — it should be the singular form of the list name to make the code readable (`for mark in marks`, `for name in names`) [2].

### 5.3 range() — generating a sequence of numbers

Sometimes you need to loop a fixed number of times rather than over an existing list. Python's built-in `range()` function generates a sequence of integers on demand [1][4]:

| Call | Generates | Example output |
|---|---|---|
| `range(3)` | `0, 1, 2` | 0-based, 3 steps |
| `range(1, 4)` | `1, 2, 3` | start at 1, stop before 4 |
| `range(0, 10, 2)` | `0, 2, 4, 6, 8` | step of 2 |

```python
for i in range(3):
    print(i)
```

Output:
```
0
1
2
```

`range(n)` generates n values starting at 0, not n values starting at 1 — the same zero-based counting as list indices. When you want 1, 2, 3 use `range(1, 4)` [4].

`range()` does not create the full list in memory — it generates one integer at a time as the loop needs it. For beginners this detail does not change how you use it; it matters for very large ranges [4].

### 5.4 The accumulator pattern

The most important pattern built on top of a for loop is the **accumulator**: start with a "zero value" before the loop, update it on every iteration, read the final result after the loop [1][2].

**Running sum (accumulator):**

```python
marks = [88, 72, 91]
total = 0               # 1. initialise to zero
for mark in marks:
    total += mark       # 2. add each item (total = total + mark)
print(total)            # 3. read after loop: 251
```

`total += mark` is shorthand for `total = total + mark`. It updates the variable in place — exactly what "accumulate" means [2].

After the loop, `total` holds the sum of all elements. Dividing by the count gives the average:

```python
average = total / len(marks)
print(average)   # 83.66666...
```

The general shape is:

```
result = <zero value>
for item in collection:
    result = result <operator> item
# use result here
```

A running count uses the same structure but adds 1 instead of the item value:

```python
pass_count = 0
for mark in marks:
    if mark >= 60:
        pass_count += 1
print(pass_count)   # 3  (all three marks pass)
```

Notice the `if` statement inside the loop body — this is where 11.5 and 11.6 combine. The loop visits every item; the `if` decides what to do with each one.

### 5.5 Combining for loops with if/else (brief)

The loop body can contain any Python code, including `if`/`elif`/`else` from 11.5. The indentation rule nests: the `for` body is indented 4 spaces; the `if` body inside it is indented another 4 spaces (8 total) [1][2]:

```python
marks = [88, 72, 45]
for mark in marks:
    if mark >= 60:
        print(str(mark) + " — Pass")
    else:
        print(str(mark) + " — Fail")
```

Output:
```
88 — Pass
72 — Pass
45 — Fail
```

## 6. Implementation

**Generalised grade-average script using a for loop:**

```python
# Marks stored in a list
marks = [88, 72, 91]

# Accumulator pattern: compute total
total = 0
for mark in marks:
    total += mark

# Compute and round average
average = total / len(marks)
average_rounded = round(average, 1)

# Assign letter grade (from 11.5)
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

print("Average: " + str(average_rounded) + "  Grade: " + grade)
```

Output:
```
Average: 83.7  Grade: B
```

Compare to the 11.4/11.5 version: `total = mark1 + mark2 + mark3`. If a fourth assessment is added, you only update the `marks` list — the loop code stays identical. This is the payoff of the accumulator pattern [1][2].

**Collecting marks from the user:**

Combining `input()` (11.5) with a for loop lets you collect any number of marks without duplicating input lines:

```python
marks = []
for i in range(3):
    mark = int(input("Mark " + str(i + 1) + ": "))
    marks.append(mark)   # adds mark to the list
```

`marks.append(mark)` adds an item to the end of a list [5]. This is the first list method introduced; deeper coverage of list methods (`.sort()`, `.remove()`, etc.) is deferred to a later topic.

## 7. Real-World Patterns

**Batch processing in AI pipelines.** An AI pipeline rarely processes one document at a time. A list of customer reviews, a list of student essays, or a list of support tickets is processed with a `for` loop: visit each item, pass it to the AI model, collect the result [2]. The accumulator pattern collects the outputs into a results list using `.append()`. This is structurally identical to the grade-average pattern above.

**Counting and filtering.** Counting how many items in a list meet a condition — `if score >= 0.7: count += 1` — is a key data-quality step before any AI inference. If fewer than N items pass the quality check, the pipeline aborts rather than running the model on bad data [1][2].

**range() for indexed access.** When you need both the index and the value — for example, to label output as "Mark 1:", "Mark 2:" — use `range(len(marks))` and access `marks[i]` inside the loop. Python has a built-in `enumerate()` that does this more cleanly; it is introduced in a later topic [1].

## 8. Best Practices

- **Name the loop variable as the singular of the list.** `for mark in marks`, `for name in names` — this reads almost like English and makes the loop body self-documenting [2].
- **Initialise the accumulator before the loop, not inside it.** If you write `total = 0` inside the loop body, it resets to zero on every iteration and you only ever accumulate the last item.
- **Do not use a loop where a built-in does the same job cleaner.** Python's `sum()` computes a list total directly (`total = sum(marks)`). Writing an explicit accumulator loop is the right learning step here; in production code you would usually reach for `sum()` [1].

## 9. Hands-On Exercise

Open a Colab cell and complete the following:

1. Create a list `scores = [70, 85, 55, 92, 61]`.
2. Use a `for` loop with an accumulator to compute the total.
3. Compute the average using `len(scores)`.
4. Print each score from `scores` followed by "Pass" or "Fail" (use `>= 60`).
5. Count and print how many scores pass.

Expected output:
```
Average: 72.6
70 — Pass
85 — Pass
55 — Fail
92 — Pass
61 — Pass
Passing: 4
```

## 10. Key Takeaways

- A **list** stores an ordered sequence of values in square brackets; elements are accessed by zero-based index; `len()` gives the count [1][5].
- A `for` loop visits every item in a list (or `range()` sequence) in order, running the indented body once per item [1][2][3].
- `range(n)` generates 0 through n−1; `range(start, stop)` generates start through stop−1 [4].
- The **accumulator pattern** — initialise to zero before the loop, update inside, read after — computes running sums and counts [1][2].
- The loop body can contain any prior Python code including `if`/`else`; the nested indentation is 4 + 4 = 8 spaces [1][2].

## 11. References

1. Python Software Foundation. *More Control Flow Tools — for Statements*. https://docs.python.org/3/tutorial/controlflow.html#for-statements
2. Real Python. *Python "for" Loops (Definite Iteration)*. https://realpython.com/python-for-loop/
3. W3Schools. *Python For Loops*. https://www.w3schools.com/python/python_for_loops.asp
4. Python Software Foundation. *Built-in Functions — range()*. https://docs.python.org/3/library/functions.html#func-range
5. Real Python. *Lists and Tuples in Python*. https://realpython.com/python-lists-tuples/
