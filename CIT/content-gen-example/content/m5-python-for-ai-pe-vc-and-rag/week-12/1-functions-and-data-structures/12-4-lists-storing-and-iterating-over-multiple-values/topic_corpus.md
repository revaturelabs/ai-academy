---
topic_id: "12.4"
title: "Lists — storing and iterating over multiple values"
position_in_module: 4
generated_at: "2026-06-14T00:00:00Z"
resource_count: 3
---

# 1. Lists — Storing and Iterating Over Multiple Values — Topic Corpus

## 2. Prerequisites

This topic builds on earlier Week 12 topics and assumes Python basics from Week 11:

- **12.1 — Functions:** you can define a function with `def` and call it by name.
- **12.2 — Parameters and return values:** you know how to pass values into a function and get a result back.
- **12.3 — One function = one job:** you understand why each function should have a single, clearly stated purpose.

Supporting background from Week 11:

- **Variables:** you know how to store a single value in a variable (e.g. `score = 85`).
- **For loops:** you know how to repeat a block of code using `for`.
- **If/else:** you can write conditional logic.

## 3. Learning Objectives

By the end of this topic you will be able to:

1. Create a Python **list** with square-bracket syntax and store multiple values inside it.
2. **Access** any item in a list by its position number (index), starting from zero.
3. **Modify** a specific item in a list by assigning a new value to its index.
4. **Iterate** over every item in a list using a `for item in list:` loop.
5. Use `append()` to add a new item to the end of a list and `len()` to count how many items the list contains.
6. Describe one concrete way lists appear in AI and Python programs — such as storing a batch of prompts or a set of scores.

## 4. Introduction

So far in Week 12 you have worked with functions that compute a single number — for example, the average of some marks. But where do those marks come from? In a real program, you rarely have just one value at a time. You have a whole collection: ten student scores, twenty product prices, a hundred customer names.

Imagine trying to store ten exam scores without a list. You would need ten separate variables: `score1 = 72`, `score2 = 88`, `score3 = 65` ... and so on. Adding an eleventh score would mean changing your code. Looping over all ten scores would require ten separate lines. That approach breaks the moment the number of values changes.

A **list** solves this. It lets you hold any number of values under a single name. You can look up any value by its position, change a value, add new values, and loop over all of them with one simple instruction. Lists are one of the most-used data structures in Python — you will encounter them in virtually every program you write in this course [1].

In the Week 12 lab, for example, you will read a CSV file containing ten student marks. Those marks will land in a list. Then you will pass the list to `compute_average`, `find_highest`, and `find_lowest` — the single-job functions you practised in Topic 12.3. By the end of this topic you will know exactly how to build that list, add items to it, and loop over it [1][2].

## 5. Core Concepts

### 5.1 What a List Is

A **list** is a Python value that holds a sequence of items in a fixed order [1]. Think of it as a row of numbered storage boxes. Each box holds one value. The boxes are numbered starting from zero.

You create a list by writing the values between square brackets `[` and `]`, separated by commas:

```python
marks = [72, 88, 65, 90, 55]
```

After this line runs, `marks` is a single variable that holds five numbers. The numbers keep the order you wrote them in — `72` is first, `88` is second, and so on [1].

A list can hold any type of value Python already knows:

```python
names    = ["Alice", "Bob", "Carol"]   # strings
scores   = [10, 9, 8, 7]              # integers
empty    = []                          # an empty list — zero items
```

**Key vocabulary:**

- **List** — a Python value that stores an ordered sequence of items.
- **Item** (also called an **element**) — one value inside the list.
- **Square brackets** — the `[` and `]` characters used to create a list and to access items inside it.

### 5.2 Accessing Items by Index

To read one item from a list, write the list name followed by the item's position number inside square brackets. That position number is called the **index** [1].

```python
marks = [72, 88, 65, 90, 55]
print(marks[0])   # 72  — the first item
print(marks[1])   # 88  — the second item
print(marks[4])   # 55  — the fifth item
```

**Important:** Python counts from zero, not from one. The first item is at index `0`, the second at index `1`, the last item of a five-item list is at index `4` [1].

| Index | 0  | 1  | 2  | 3  | 4  |
|-------|----|----|----|----|-----|
| Value | 72 | 88 | 65 | 90 | 55 |

If you try to access an index that does not exist — for example `marks[5]` on a five-item list — Python raises an `IndexError`. You will learn how to handle errors in a later topic. For now, keep your indexes within range [1].

**Index** — the position number of an item inside a list. Always starts at zero.

### 5.3 Modifying Items by Index

You can change an item that already exists in a list by assigning a new value to its index:

```python
marks = [72, 88, 65, 90, 55]
marks[2] = 70          # change the item at index 2
print(marks)           # [72, 88, 70, 90, 55]
```

The list now has `70` at position 2 instead of `65`. The other items are unchanged [1][2].

This is useful when you want to correct a single value without rebuilding the whole list.

### 5.4 Finding the Length with `len()`

`len()` is a built-in Python function that tells you how many items are in a list [1]:

```python
marks = [72, 88, 65, 90, 55]
print(len(marks))   # 5
```

With lists, `len()` becomes especially useful because the list can grow or shrink. You often need to ask "how many items do I have right now?" before doing a calculation [1][2].

**`len()`** — a Python built-in that returns the number of items in a list (or the number of characters in a string). Called like a function: `len(my_list)`.

### 5.5 Adding Items with `append()`

`append()` is a list operation that adds one new item to the **end** of an existing list [1]:

```python
marks = [72, 88, 65]
marks.append(90)
marks.append(55)
print(marks)       # [72, 88, 65, 90, 55]
print(len(marks))  # 5
```

You call `append()` using dot notation: `list_name.append(new_value)`. The dot means "run the `append` operation on this particular list" [2].

`append()` always adds to the end. Existing items keep their positions and their indexes [1].

**`append()`** — a list operation that adds one item to the end of the list. Called with dot notation: `my_list.append(value)`.

**Method** — an operation that belongs to a particular type of value. `append()` belongs to lists. You will hear the word "method" more in later topics — for now, just remember the pattern: `list_name.append(value)` [2].

### 5.6 Iterating Over a List with a For Loop

**Iterating** means going through a collection one item at a time [1]. In Python the simplest way to iterate over a list is:

```python
for item in list_name:
    # code that runs once for each item
```

Each time the loop runs, the variable `item` automatically holds the next value from the list. You do not need to track any index yourself [1][2].

Example:

```python
marks = [72, 88, 65, 90, 55]

for mark in marks:
    print(mark)
```

Output:

```
72
88
65
90
55
```

The loop runs five times — once for each item in `marks`. On the first pass, `mark` equals `72`. On the second, `mark` equals `88`. And so on until every item has been visited [1].

**Iterating** — moving through a list one item at a time, performing the same operation on each item.

You can choose any name for the loop variable — `mark`, `score`, `name`, `item`. A descriptive name makes the code easier to read [2][3].

### 5.7 Iterating with an Index Using `range(len())`

Sometimes you need both the item's value **and** its position number inside the loop. You can combine `range()` and `len()` to get both:

```python
marks = [72, 88, 65, 90, 55]

for i in range(len(marks)):
    print("Index", i, "has value", marks[i])
```

Output:

```
Index 0 has value 72
Index 1 has value 88
Index 2 has value 65
Index 3 has value 90
Index 4 has value 55
```

`range(len(marks))` produces the sequence `0, 1, 2, 3, 4` — one number for each index position. Inside the loop, `marks[i]` looks up the item at that position [1][3].

Use `for item in list:` when you only need the value. Use `for i in range(len(list)):` when you also need the index — for example, when modifying items [1][3].

## 6. Implementation

### Worked Example: Building and Using a Marks List

**Goal:** start with an empty list, add marks one by one with `append()`, then iterate to compute the total and the average.

This pattern directly matches what you will do in the Week 12 lab when reading marks from a file — each mark arrives one at a time and gets appended to the list [1][2].

---

**Step 1 — Create an empty list.**

```python
marks = []
```

The list exists but holds zero items. `len(marks)` returns `0` right now [1].

---

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

Each call to `append()` places the new mark at the end of the list [1][2].

---

**Step 3 — Iterate to compute the total.**

```python
total = 0
for mark in marks:
    total = total + mark

print(total)   # 370
```

The loop visits each mark in order, adding it to `total`. When the loop finishes, `total` holds the sum of all marks [1].

---

**Step 4 — Compute the average using `len()`.**

```python
average = total / len(marks)
print(average)   # 74.0
```

`len(marks)` gives `5`. The division produces `74.0` [1][2].

---

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

The loop compares every mark to the current `highest`. When it finds a bigger one, it updates `highest`. After visiting all marks, `highest` holds the largest value [1][3].

---

**Complete program:**

```python
# Build the list
marks = []
marks.append(72)
marks.append(88)
marks.append(65)
marks.append(90)
marks.append(55)

# Compute total and average
total = 0
for mark in marks:
    total = total + mark
average = total / len(marks)

# Find the highest
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

### Modifying Items During Iteration

If you need to change every item in a list — for example, add a 5-point bonus to each mark — use the index-based loop so you can write back to the list:

```python
marks = [72, 88, 65, 90, 55]

for i in range(len(marks)):
    marks[i] = marks[i] + 5

print(marks)   # [77, 93, 70, 95, 60]
```

The `for item in list:` form gives you a copy of each value for that pass. Changing `item` does NOT change the list. The index form (`marks[i] = ...`) writes back to the actual list [1][3].

## 7. Real-World Patterns

Lists appear in almost every Python program that deals with more than one value at a time. Here are three patterns you will use in this course [1][2][3].

**Pattern 1 — Collecting results from a loop.**

When a program processes multiple inputs and wants to keep all the results, it creates an empty list and appends each result:

```python
results = []

prompts = ["What is AI?", "What is Python?", "What is a list?"]
for prompt in prompts:
    # send_to_model() would call an AI model — you will write this later in Week 12
    response = send_to_model(prompt)
    results.append(response)

print(len(results), "responses collected")
```

This pattern — empty list, loop, `append()` — is everywhere in data processing and in code that calls APIs (Application Programming Interfaces — connections to external services like AI models, which you will cover later in Week 12) [2][3].

**Pattern 2 — Storing a batch of prompts for an LLM.**

When you call an LLM (Large Language Model — an AI system that generates text), you often want to send multiple different prompts and collect all the answers. A list holds those prompts in a predictable order:

```python
prompts = [
    "Summarise this document in one sentence.",
    "List three key risks in this proposal.",
    "What follow-up questions would you ask?"
]

for prompt in prompts:
    print("Sending prompt:", prompt)
    # ... send prompt to the model and handle the response
```

The list makes it easy to add, remove, or change one prompt without touching the rest [3].

**Pattern 3 — Storing and scanning scores (the lab pattern).**

In the Week 12 lab you will read marks from a CSV file. Each mark goes into a list. Then you pass the list to single-job functions — one to compute the average, one to find the highest, one to find the lowest [1][2]:

```python
marks = [72, 88, 65, 90, 55, 77, 61, 84, 70, 59]

total = 0
for mark in marks:
    total = total + mark
average = total / len(marks)

print("Average:", average)
print("Count:  ", len(marks))
```

The list makes the program flexible — it works the same way whether there are 10 marks or 100 [1].

## 8. Best Practices

**Do:**

- **Create an empty list first, then `append()`** when you do not know the values in advance (e.g. reading from a file line by line). Do not try to pre-fill all the slots [1][2].
- **Use a descriptive name for the list and for the loop variable.** `marks` + `mark`, `names` + `name`, `scores` + `score` — the singular/plural pattern makes loops easy to read [2][3].
- **Use `len()` in calculations** rather than hardcoding a number. `total / len(marks)` is correct even if someone adds or removes a mark; `total / 5` breaks the moment the list changes [1].
- **Use `for item in list:`** when you only need the value. Use `for i in range(len(list)):` when you also need the index — especially if you want to modify items [1][3].
- **Set a starting value from the list** (e.g. `highest = marks[0]`) when looking for a maximum or minimum. This is safer than inventing a magic starting number [1].

**Do not:**

- **Do not access `marks[5]` on a five-item list.** The last valid index is `4`. Accessing beyond the end causes an `IndexError` [1].
- **Do not confuse `for item in list:` with `for i in range(len(list)):`** when you intend to modify items. Changing `item` in the first form does not change the actual list [1][3].
- **Do not build ten separate variables** (`score1`, `score2`, ..., `score10`) when you need to loop over them. That is exactly what lists are for.
- **Do not forget the colon** at the end of the `for` line. `for mark in marks` without `:` is a syntax error — Python requires it [2].

| Situation | Right approach | Common mistake |
|---|---|---|
| Build a list from unknown inputs | Start with `[]`, use `append()` | Pre-filling with placeholder values |
| Count the items | `len(marks)` | Hardcoding the number |
| Loop to read values | `for mark in marks:` | Unnecessary index loop |
| Loop to modify values | `for i in range(len(marks)):` | `for mark in marks:` then assigning to `mark` |

## 9. Hands-On Exercise

Open your Colab notebook.

1. Create an empty list called `scores`. Use `append()` to add these five values one at a time: `83, 91, 74, 60, 88`.
2. Print the list, then print `len(scores)`. Confirm you see `[83, 91, 74, 60, 88]` and `5`.
3. Print the first item (`scores[0]`) and the last item (`scores[4]`).
4. Change the fourth item (index 3) from `60` to `65`. Print the list to confirm the change.
5. Write a `for` loop that prints each score on its own line.
6. Write a second `for` loop that computes the total. Then compute and print the average using `len()`.
7. Bonus: write a `for i in range(len(scores)):` loop that prints `"Score at index X: Y"` for each item.

## 10. Key Takeaways

- A **list** stores an ordered sequence of values under a single variable name. You create one with square brackets: `marks = [72, 88, 65]`.
- Items are accessed and modified by their **index**, which starts at `0`. The first item is `marks[0]`, the second is `marks[1]`, and so on.
- `len(list_name)` returns the number of items in the list. Use it in calculations so your code still works when the list grows or shrinks.
- `list_name.append(value)` adds one item to the end of the list without changing any existing items or their indexes.
- `for item in list_name:` iterates over the list, running the loop body once for each item. Use `for i in range(len(list_name)):` when you also need the index — for example, to modify items in place.
- Lists are fundamental to AI and data-processing programs: collecting API responses, storing batches of prompts, holding scores read from a file — all rely on the same create-append-iterate pattern.

## 11. Next Steps

_System-derived from the next entry in curriculum/sequence.md._
