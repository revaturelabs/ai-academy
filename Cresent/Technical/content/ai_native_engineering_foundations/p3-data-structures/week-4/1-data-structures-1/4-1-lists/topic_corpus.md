---
topic_id: 4.1
title: Lists
position_in_module: 1
generated_at: 2026-07-14T00:00:00Z
resource_count: 3
---

# 1. Lists — Topic Corpus

## 2. Prerequisites

This is the first topic in P3 (Data Structures) and builds directly on P1 (Python Foundations) and P2 (Control Flow & Functions). You should already be comfortable with:

- **Variables and assignment**, and the built-in types `int`, `float`, `str`, `bool` (P1).
- **Operators** — arithmetic (`+`, `*`), comparison (`==`, `<`, `>`), and how `+`/`*` behave on different types (P1).
- **Type conversion** with `int()`, `str()`, `float()`, `bool()`, and inspecting types with `type()` (P1).
- **`f-strings`** and **`print()`** for producing output (P1).
- **Conditionals** (`if`/`elif`/`else`) and **loops** (`for`, `while`), plus writing your own **functions** with `def` (P2).

Those tools are assumed. This topic reuses them freely (for example, a `for`-loop to walk a list, or an `f-string` to print a result) without re-explaining them.

## 3. Learning Objectives

After this topic you will be able to:

- **Create** a list literal and **access** any element using positive and negative indexing.
- **Slice** a list with a start, stop, and step — including the `[::2]` and `[::-1]` idioms.
- **Explain** what mutability means and **modify** a list in place.
- **Apply** the core list methods (`append`, `insert`, `remove`, `pop`, `extend`, `index`, `count`, `clear`) to the right task.
- **Iterate** over a list with a `for`-loop and **sort** it with `sort()` versus `sorted()`, using the `reverse` and `key=` arguments.
- **Build** a nested list and **write** a list comprehension that maps and/or filters in a single expression.

## 4. Introduction

Almost every real program juggles *collections* of things, not single values: a shopping cart of items, the scores in a game, the lines of a file, the rows returned from a query. Up to now you have worked with one value at a time — one `int`, one `str`. A **list** is Python's everyday container for holding many values in order, in a single variable [1].

Lists are the workhorse of Python. They are ordered (there is a first item, a second item, and so on), they can hold anything (numbers, strings, even other lists), and — crucially — they can *change* after you create them. That last property, called **mutability**, is what makes lists so useful for building up results as a program runs, and it is the feature that most distinguishes a list from the tuple you will meet in the next topic [2].

By the end of this topic you will be able to store a batch of values, reach into that batch by position, carve out sub-sections of it, grow and shrink it, sort it, and transform it into a new list with one compact expression. These are the same operations you will lean on constantly in the labs and in A2, the Data Structures Portfolio, where you must pick and manipulate the right structure for a data-handling task.

## 5. Core Concepts

### 5.1 Creating a list

A list is written as a comma-separated sequence of values inside **square brackets** `[ ]` [1]:

```python
fruits = ["apple", "banana", "cherry"]
numbers = [10, 20, 30, 40, 50]
mixed = ["Bob", 42, True, 3.14]   # items can be of different types
empty = []                         # a list with no items
```

A list is a single value (of type `list`) that happens to contain other values. You can check that with the tools you already know:

```python
print(type(fruits))   # <class 'list'>
print(len(fruits))    # 3  — len() gives the number of items
```

Items are called **elements**. The list keeps them in the order you wrote them; that order is part of the list's identity and does not shuffle on its own [1].

### 5.2 Indexing: positive and negative

Each element has a numbered position called its **index**. Python indexes from **zero**: the first element is at index `0`, the second at index `1`, and so on. You reach an element by writing the list name followed by the index in square brackets [3]:

```python
fruits = ["apple", "banana", "cherry"]
print(fruits[0])   # apple  — first element
print(fruits[1])   # banana
print(fruits[2])   # cherry — last element (len - 1)
```

Python also supports **negative indexing**, which counts from the *end*: `-1` is the last element, `-2` the second-to-last, and so on. This saves you from computing `len(list) - 1` every time you want the tail [3]:

```python
print(fruits[-1])  # cherry — last element
print(fruits[-2])  # banana
print(fruits[-3])  # apple  — same as fruits[0]
```

Asking for an index that does not exist (for example `fruits[3]` on a three-element list) raises an `IndexError`. Negative and positive indices point at the same physical slots from opposite directions — for a list of length `n`, index `0` and index `-n` are the same element.

### 5.3 Slicing with a step

**Slicing** pulls out a *range* of elements and returns them as a **new list**. The syntax is `list[start:stop:step]`, where `start` is included, `stop` is excluded, and `step` is how far to jump each time [3]:

```python
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(a[1:5])     # [1, 2, 3, 4]   — indices 1,2,3,4 (5 excluded)
print(a[:3])      # [0, 1, 2]      — start defaults to 0
print(a[7:])      # [7, 8, 9]      — stop defaults to len(a)
print(a[:])       # [0..9]         — a full (shallow) copy of the list
```

The optional third value, the **step**, controls the stride:

```python
print(a[::2])     # [0, 2, 4, 6, 8]  — every 2nd element
print(a[1:5:2])   # [1, 3]           — from 1 to 5, stepping by 2
print(a[::-1])    # [9, 8, 7, ... 0] — reversed, a negative step walks backward
```

Two idioms are worth memorising: `a[::2]` takes every second item, and `a[::-1]` produces a reversed copy of the list. Because a slice always builds a *new* list, slicing never changes the original [3].

### 5.4 Updating items and mutability

Lists are **mutable** — you can change their contents after creation without making a new list. Assigning to an index replaces the element in place [1]:

```python
colors = ["red", "green", "blue"]
colors[1] = "yellow"
print(colors)    # ['red', 'yellow', 'blue']
```

You can also assign to a slice to replace several elements at once:

```python
colors[0:2] = ["black", "white"]
print(colors)    # ['black', 'white', 'blue']
```

Mutability has a consequence worth understanding early. A variable holding a list holds a *reference* to that list, not a private copy. If two names point at the same list, a change through one name is visible through the other:

```python
a = [1, 2, 3]
b = a            # b and a refer to the SAME list
b.append(4)
print(a)         # [1, 2, 3, 4]  — a changed too!
```

If you want an independent copy, slice it (`b = a[:]`) or call `a.copy()`. This "same object, two names" behaviour is exactly what a tuple (topic 4.2) forbids by being immutable — but that is a story for the next topic; here the takeaway is simply that lists can be changed in place, and that sharing a list means sharing its changes [1][2].

### 5.5 List methods

Lists carry built-in **methods** — functions attached to the list that you call with the dot syntax `list.method(...)`. The following eight are the everyday set [1][2].

**Adding elements**

- `append(x)` — add `x` as a single new element at the end.
- `insert(i, x)` — insert `x` so that it lands at index `i`, shifting later items right.
- `extend(iterable)` — add *each* item of another list (or sequence) to the end.

```python
nums = [1, 2, 3]
nums.append(4)        # [1, 2, 3, 4]
nums.insert(0, 99)    # [99, 1, 2, 3, 4]  — 99 now at index 0
nums.extend([5, 6])   # [99, 1, 2, 3, 4, 5, 6]
```

Note the difference between `append` and `extend`: `nums.append([5, 6])` would add the *list* `[5, 6]` as one nested element, whereas `extend` unpacks it into individual elements [2].

**Removing elements**

- `remove(x)` — delete the first element equal to `x` (raises `ValueError` if not present).
- `pop(i)` — remove and **return** the element at index `i`; with no argument, `pop()` removes and returns the last element.
- `clear()` — remove every element, leaving `[]`.

```python
letters = ["a", "b", "c", "b"]
letters.remove("b")   # ['a', 'c', 'b']  — only the FIRST "b" goes
last = letters.pop()  # last == 'b', letters == ['a', 'c']
letters.clear()       # []
```

`pop` is the one that hands the value back to you, which makes it useful when you want to both retrieve and delete in one step [2].

**Searching and counting**

- `index(x)` — return the index of the first element equal to `x` (raises `ValueError` if absent).
- `count(x)` — return how many times `x` appears.

```python
scores = [10, 20, 10, 30, 10]
print(scores.index(20))  # 1
print(scores.count(10))  # 3
```

All of `append`, `insert`, `extend`, `remove`, `pop`, and `clear` change the list *in place* (they rely on mutability); `index` and `count` only read from it [1][2].

### 5.6 Looping through a list

Because a list is ordered and iterable, a `for`-loop (from P2) visits each element in turn:

```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"I like {fruit}")
```

When you also need the position, pair the loop with indices via `range(len(...))`, or iterate directly when you only need the values:

```python
for i in range(len(fruits)):
    print(f"{i}: {fruits[i]}")
```

Iterating a list is the most common thing you will do with one — walk the items, test each with a conditional, accumulate a result. This is the foundation the list comprehension in 5.8 compresses into one line [1].

### 5.7 Sorting: `sort()` vs `sorted()`

There are two ways to order a list, and the difference matters [2]:

- **`list.sort()`** is a *method* that sorts the list **in place** and returns `None`. The original list is rearranged.
- **`sorted(list)`** is a *built-in function* that returns a **new** sorted list and leaves the original untouched.

```python
nums = [3, 1, 2]

nums.sort()                 # nums is now [1, 2, 3]; sort() returns None
print(nums)                 # [1, 2, 3]

original = [3, 1, 2]
result = sorted(original)   # result == [1, 2, 3]
print(original)             # [3, 1, 2] — unchanged
```

A common mistake is writing `nums = nums.sort()`, which assigns `None` to `nums` because `sort()` returns nothing. Use the method when you don't need the original order back, and the function when you do.

Both accept the same two keyword arguments [2]:

- **`reverse=True`** sorts from largest to smallest (descending).
- **`key=`** takes a function applied to each element to decide the sort order. The list is sorted by the *result* of that function, not by the element itself.

```python
words = ["banana", "apple", "kiwi"]

print(sorted(words, reverse=True))     # ['kiwi', 'banana', 'apple']
print(sorted(words, key=len))          # ['kiwi', 'apple', 'banana'] — by length
print(sorted(words, key=len, reverse=True))  # longest first
```

The `key` function can be any function that takes one element and returns a comparable value — `len` here, but equally a function you define with `def` to sort by, say, the last character or a numeric field [2].

### 5.8 Nested lists (lists of lists)

A list element can itself be a list. This gives you a **nested list** — a natural way to represent a grid, a table, or rows of data [2]:

```python
grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

print(grid[0])       # [1, 2, 3]  — the first row (a list)
print(grid[0][2])    # 3          — row 0, then column 2 within it
print(grid[2][0])    # 7          — row 2, column 0
```

The first index selects a row; the second index reaches inside that row. To visit every cell, nest one loop inside another:

```python
for row in grid:
    for value in row:
        print(value, end=" ")
    print()          # newline after each row
```

Nested lists are how you model two-dimensional data before you meet richer structures later in the course. Each inner list is a full-fledged list with all the methods and slicing you have already learned.

### 5.9 List comprehension

A **list comprehension** builds a new list from an existing sequence in a single expression. It replaces the common "create an empty list, loop, append" pattern with one compact line [1][2]. The pattern below produces the same result three ways:

```python
# The long way
squares = []
for n in range(5):
    squares.append(n * n)
# squares == [0, 1, 4, 9, 16]

# The comprehension
squares = [n * n for n in range(5)]
```

Read it left to right: **`[expression for item in iterable]`** — "the expression, for each item in the iterable." The part before `for` is what each new element will be (**mapping**); the loop supplies the items.

You can add an `if` clause to **filter** — keep only items that pass a condition:

```python
evens = [n for n in range(10) if n % 2 == 0]   # [0, 2, 4, 6, 8]
```

And you can combine mapping and filtering in the same expression — transform *and* select at once:

```python
nums = [1, 2, 3, 4, 5, 6]
doubled_evens = [n * 2 for n in nums if n % 2 == 0]   # [4, 8, 12]
```

Comprehensions are idiomatic Python: shorter, faster to read once you know the pattern, and they always return a fresh list without touching the source. Reach for one whenever you find yourself writing "make an empty list, loop, append" [2].

## 6. Implementation

A practical way to reason about which list operation to use:

1. **Need one value by position?** Use indexing — `a[i]` for a known position, `a[-1]` for the last.
2. **Need a contiguous chunk, every-nth item, or a reversed copy?** Use a slice — `a[start:stop:step]`.
3. **Growing the list?** `append` for one item at the end, `insert` for a specific position, `extend` to tack on a whole sequence.
4. **Shrinking the list?** `remove` when you know the *value*, `pop` when you know the *position* (and want the value back), `clear` to empty it.
5. **Answering a question about contents?** `index` for "where is it?", `count` for "how many?", `in` for "is it there?" (`"apple" in fruits` returns a `bool`).
6. **Reordering?** `sort()` to change the list itself, `sorted()` to get a new ordered list; add `reverse=` and/or `key=` to control the order.
7. **Transforming every item into a new list?** A list comprehension — with an `if` clause if you also need to filter.

A useful mental checkpoint: methods like `sort`, `append`, and `remove` mutate and return `None`; functions and slices like `sorted` and `a[:]` return a new list. Whenever a call "seems to lose your data," check whether you assigned the `None` result of an in-place method.

## 7. Real-World Patterns

- **Accumulating results.** Start with `results = []`, loop over some input, and `append` each computed value — the bread-and-butter pattern behind reports, parsed files, and API responses [1].
- **Filtering and transforming data.** A single comprehension like `[row for row in rows if row[0] == "active"]` selects matching records; `[price * 1.1 for price in prices]` reprices a column. This is the everyday shape of data cleanup [2].
- **Ranking and top-N.** `sorted(scores, reverse=True)[:3]` sorts descending and slices the top three — sorting plus slicing composed together.
- **A stack.** `append` to push and `pop()` to remove the most recent item gives you a last-in-first-out stack with no extra machinery [2].
- **Tabular data.** A nested list (list of rows) is the simplest in-memory table before you reach dedicated data structures later in the course.

## 8. Best Practices

- **Prefer a comprehension** over the empty-list-plus-`append` loop when you are simply mapping or filtering — it is clearer and returns a new list.
- **Don't write `x = mylist.sort()`.** `sort()` returns `None`. Call `mylist.sort()` on its own line, or use `sorted(mylist)` if you want a value to assign.
- **Remember lists are shared by reference.** `b = a` does not copy; use `a[:]` or `a.copy()` when you need an independent list.
- **Match the remover to what you know:** `remove(value)` versus `pop(index)`. Calling `remove` with a value that isn't present raises `ValueError` — guard with `if value in mylist:` when unsure.
- **Use negative indices** (`a[-1]`) instead of `a[len(a)-1]` — shorter and less error-prone.
- **Keep `key=` functions simple.** A named function (`def by_length(w): return len(w)`) or a built-in like `len` reads better than a tangled expression.

## 9. Hands-On Exercise

Start with `temps = [68, 71, 65, 74, 69, 72, 66]` (a week of temperatures).

1. Print the first and last readings using indexing (one positive, one negative), then print every other day with a step slice.
2. `append` a new reading, then `sort()` the list and print the three warmest days using `sorted(..., reverse=True)[:3]`.
3. Build a list comprehension that keeps only the temperatures above 70, and one that converts each reading to a label string with an `f-string`.

## 10. Key Takeaways

- A list is an ordered, mutable collection written with `[ ]`; elements are reached by index, with `0` as the first and `-1` as the last.
- Slicing (`a[start:stop:step]`) returns a *new* list; `a[::2]` takes every second item and `a[::-1]` reverses.
- Because lists are mutable, in-place methods (`append`, `insert`, `extend`, `remove`, `pop`, `clear`) change the list itself and return `None`, while `sorted()` and slices produce new lists.
- `sort()` reorders in place; `sorted()` returns a new sorted list — both accept `reverse=` and `key=`.
- A list comprehension maps and/or filters in one expression, replacing the empty-list-loop-`append` pattern; a nested list models two-dimensional data.

## 11. Next Steps

_System-derived from the next entry in curriculum/sequence.md._
