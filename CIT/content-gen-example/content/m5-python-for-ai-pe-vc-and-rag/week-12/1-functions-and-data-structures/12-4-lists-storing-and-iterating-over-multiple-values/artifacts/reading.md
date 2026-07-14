<!-- nav:top:start -->
[⬅ Previous: 12.3 — One function = one job](../../12-3-one-function-one-job-the-testable-unit-principle/artifacts/reading.md)&emsp;·&emsp;[⬆ Table of Contents](../../../../../../../README.md#curriculum-topic-index)&emsp;·&emsp;[Next: 12.5 — Dictionaries ➡](../../12-5-dictionaries-key-value-pairs-for-structured-data/artifacts/reading.md)
<!-- nav:top:end -->

---

# Lists — storing and iterating over multiple values

## Overview

So far in Week 12 you have written functions that compute one result from a single value. Real programs rarely deal with just one value — you might have ten student scores, twenty prices, or a hundred names. A **list** solves this by holding any number of values under a single variable name. You can look up, change, add, and loop over every item with just a few lines of code [1]. By the end of this topic you will know exactly how to build that list, grow it item by item, and hand it off to the single-job functions you practised in Topic 12.3.

## Key Concepts

### The problem lists solve

Imagine storing ten exam scores without a list. You would write `score1 = 72`, `score2 = 88`, and so on — ten separate variables. Adding an eleventh score means changing your code. Looping over all ten requires ten separate lines. A list collapses all of that into one named container.

### Creating a list

You write values between square brackets `[` `]`, separated by commas:

```python
marks = [72, 88, 65, 90, 55]
```

`marks` is now one variable that holds five numbers in the order you wrote them [1]. An empty list — with no items yet — is just `[]`.

- **List** — a Python value that stores an ordered sequence of items.
- **Item** (also called an **element**) — one value inside the list.
- **Square brackets** — the `[` and `]` characters used to create a list and to read items from it.

### Accessing and modifying items by index

![Lists — structure and iteration](../artifacts/diagram.png)

To read one item, write the list name followed by its position number inside square brackets. That position number is the **index** [1].

```python
print(marks[0])   # 72  — first item
print(marks[1])   # 88  — second item
print(marks[4])   # 55  — fifth item
```

- **Index** — the position number of an item. Always starts at **zero**, not one.

| Index | 0  | 1  | 2  | 3  | 4  |
|-------|----|----|----|----|-----|
| Value | 72 | 88 | 65 | 90 | 55 |

To change an item, assign a new value to its index:

```python
marks[2] = 70          # replace 65 with 70
print(marks)           # [72, 88, 70, 90, 55]
```

### Adding items with `append()`

`append()` adds one new item to the **end** of an existing list [1]:

```python
marks = [72, 88, 65]
marks.append(90)
marks.append(55)
print(marks)       # [72, 88, 65, 90, 55]
```

- **`append()`** — a list operation that adds one item to the end. Called with dot notation: `my_list.append(value)`.

Existing items keep their positions and their indexes when you append.

### Finding the length with `len()`

`len()` returns how many items are in the list [1][2]:

```python
print(len(marks))   # 5
```

- **`len()`** — a Python built-in that returns the number of items in a list. Use it in calculations so your code still works when the list grows or shrinks.

### Iterating over a list

**Iterating** means going through a list one item at a time [1]. The simplest form:

```python
for mark in marks:
    print(mark)
```

The loop runs once for each item. On the first pass, `mark` holds `72`; on the second, `88`; and so on until every item has been visited [1][2]. You do not need to track any index yourself.

Use `for i in range(len(marks)):` when you also need the index — for example, to modify items in place:

```python
for i in range(len(marks)):
    marks[i] = marks[i] + 5   # add a 5-point bonus to every mark
```

`range(len(marks))` produces the sequence `0, 1, 2, 3, 4`. Inside the loop, `marks[i]` looks up the item at that position [1][3].

## Worked Example

**Goal:** start with an empty list, add marks with `append()`, compute the total and average, then find the highest mark using a function from Topic 12.3.

**Step 1 — Create an empty list.**

```python
marks = []
```

The list exists but holds zero items. `len(marks)` returns `0`.

**Step 2 — Add marks with `append()`.**

```python
marks.append(72)
marks.append(88)
marks.append(65)
marks.append(90)
marks.append(55)

print(marks)       # [72, 88, 65, 90, 55]
print(len(marks))  # 5
```

**Step 3 — Iterate to compute the total.**

```python
total = 0
for mark in marks:
    total = total + mark

print(total)   # 370
```

**Step 4 — Compute the average using `len()`.**

```python
average = total / len(marks)
print(average)   # 74.0
```

Using `len(marks)` rather than the hardcoded number `5` means the calculation stays correct if you add or remove marks later [1].

**Step 5 — Find the highest mark.**

```python
def find_highest(marks):
    highest = marks[0]           # start with the first mark as the best guess
    for mark in marks:
        if mark > highest:
            highest = mark
    return highest

print(find_highest(marks))   # 90
```

The loop compares every mark to the current `highest`. When it finds a bigger value, it updates `highest`. After visiting all marks, `highest` holds the largest value [1][3].

**Complete program:**

```python
marks = []
marks.append(72)
marks.append(88)
marks.append(65)
marks.append(90)
marks.append(55)

total = 0
for mark in marks:
    total = total + mark
average = total / len(marks)

def find_highest(marks):
    highest = marks[0]
    for mark in marks:
        if mark > highest:
            highest = mark
    return highest

print("Marks:  ", marks)
print("Average:", average)
print("Highest:", find_highest(marks))
```

Output:

```
Marks:   [72, 88, 65, 90, 55]
Average: 74.0
Highest: 90
```

## In Practice

**Pattern 1 — Collecting results from a loop.**

When a program processes multiple inputs and needs to keep all the results, it creates an empty list and appends each result as it arrives. This pattern is everywhere in data processing and in code that calls an API (Application Programming Interface) — you will use APIs later in Week 12 [2][3]:

```python
results = []
for prompt in prompts:
    response = send_to_model(prompt)
    results.append(response)
```

**Pattern 2 — Storing a batch of prompts for an LLM.**

When you call an LLM (Large Language Model), you will call one later in Week 12 — a list holds multiple prompts in a predictable order so you can loop over them cleanly [3]:

```python
prompts = [
    "Summarise this document in one sentence.",
    "List three key risks in this proposal.",
    "What follow-up questions would you ask?"
]
for prompt in prompts:
    print("Sending prompt:", prompt)
```

**Pattern 3 — The Week 12 lab pattern.**

In the lab you will read marks from a CSV (Comma-Separated Values) file. Each mark goes into a list. Then you pass the list to single-job functions — `compute_average`, `find_highest`, `find_lowest` — exactly the functions you practised in Topic 12.3 [1][2]. The list makes the program work the same way whether there are 10 marks or 100.

## Key Takeaways

- A **list** stores an ordered sequence of values under one variable name. Create one with square brackets: `marks = [72, 88, 65]`.
- Items are accessed and modified by their **index**, which starts at `0`. The first item is `marks[0]`, the last item of a five-item list is `marks[4]`.
- `list_name.append(value)` adds one item to the end of the list without changing any existing items or their indexes.
- `len(list_name)` returns the number of items. Use it in calculations instead of a hardcoded number so your code still works when the list grows or shrinks.
- `for item in list_name:` iterates over every item. Use `for i in range(len(list_name)):` when you also need the index — for example, to modify items in place.
- The create-append-iterate pattern is fundamental to AI and data-processing programs: collecting API responses, storing batches of prompts, and holding scores read from a file all rely on it.

## References

1. Software Carpentry, "Programming with Python — Storing Multiple Values in Lists." https://swcarpentry.github.io/python-novice-inflammation/04-lists.html
2. W3Schools, "Python — Loop Lists." https://www.w3schools.com/python/python_lists_loop.asp
3. learnpython.com, "How to Loop Over a List in Python." https://learnpython.com/blog/python-list-loop/

---
<!-- nav:bottom:start -->
[⬅ Previous: 12.3 — One function = one job](../../12-3-one-function-one-job-the-testable-unit-principle/artifacts/reading.md)&emsp;·&emsp;[⬆ Table of Contents](../../../../../../../README.md#curriculum-topic-index)&emsp;·&emsp;[Next: 12.5 — Dictionaries ➡](../../12-5-dictionaries-key-value-pairs-for-structured-data/artifacts/reading.md)
<!-- nav:bottom:end -->
