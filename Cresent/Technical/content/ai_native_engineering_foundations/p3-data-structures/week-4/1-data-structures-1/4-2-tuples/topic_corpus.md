---
topic_id: 4.2
title: Tuples
position_in_module: 2
generated_at: 2026-07-14
resource_count: 3
---

# 1. Tuples — Topic Corpus

## 2. Prerequisites

- **4.1 Lists** (same module) — you already know indexing (positive and negative), slicing, iteration with `for`, mutability, and list methods. Tuples are taught here largely by contrast with lists, so this topic leans directly on that knowledge.
- **P1 1.4 Variables & assignment** — you saw chained/tuple-style assignment briefly (`x, y = 1, 2`). This topic teaches that mechanism fully.
- **P1** — types (`int`, `float`, `str`, `bool`), the `+` and `*` operators, comparison, `type()`, `print()`, f-strings.
- **P2** — `for` loops and `def` functions.

## 3. Learning Objectives

- **Create** tuples by packing values, by the `tuple()` constructor, and **access** their elements by index, just as you index a list.
- **Explain** immutability and identify what a tuple forbids that a list allows.
- **Apply** tuple unpacking to assign several variables at once, to swap two variables with `a, b = b, a`, and to loop over lists of tuples.
- **Use** nested tuples and reach values inside them with chained indexing.
- **Perform** the basic tuple operations: concatenation (`+`), repetition (`*`), membership (`in`), the two tuple methods `count()` and `index()`, and lexicographic comparison.
- **Decide** when a tuple is the right choice over a list, and how to "change" a tuple by building a new one.

## 4. Introduction

You just spent 4.1 learning lists — ordered, indexable, and freely editable. A **tuple** is the same idea with one deliberate restriction removed: you cannot change it after you create it. That single difference — immutability — is the whole point of the topic. Where a list says "here is a collection I might edit," a tuple says "here is a fixed group of values that belong together and will not move." [1]

Why would you ever *want* less power? Because a fixed collection is easier to reason about and safe to hand around. A pair of GPS coordinates, an RGB color, a row returned from a database, the day/month/year of a date — these are groups where changing one value in place would usually be a bug, not a feature. Tuples let you say "these values travel as a unit and stay put." [1]

You have also already met tuples without knowing it. Back in P1 you wrote `x, y = 1, 2`. The right-hand side `1, 2` is a tuple, and the left-hand side is *unpacking* it. In this topic that trick graduates from a curiosity into a tool you will reach for constantly — including the one-line variable swap `a, b = b, a`. This is also the last topic in the module, so it closes out the "sequences" story: list first, tuple second. The upcoming **A2 Data Structures Portfolio** will ask you to pick the right structure for a task, and "list or tuple?" is one of the first choices you will make.

## 5. Core Concepts

### 5.1 What a tuple is

A tuple is an **ordered, immutable sequence** of values. "Ordered" and "sequence" mean it behaves like a list for reading: elements have positions, you index them, you can loop over them, you can slice them. "Immutable" means that once built, its contents cannot be changed — no adding, no removing, no reassigning an element. [1][2]

You write a tuple with parentheses and comma-separated values:

```python
point = (3, 5)
rgb = (255, 128, 0)
person = ("Ada", 36, True)          # mixed types are fine
empty = ()                          # an empty tuple
```

The values do not have to share a type — `("Ada", 36, True)` mixes `str`, `int`, and `bool`, exactly as a list can. [2]

**Packing.** The parentheses are actually optional. When you write several comma-separated values, Python *packs* them into a tuple automatically. This is called tuple packing: [3]

```python
point = 3, 5          # same as (3, 5) — parentheses not required
type(point)           # <class 'tuple'>
```

The comma is what makes a tuple, not the parentheses. That leads to one gotcha worth memorizing:

```python
single = (42)         # NOT a tuple — this is just the int 42 in parentheses
single = (42,)        # a one-element tuple — note the trailing comma
type((42))            # <class 'int'>
type((42,))           # <class 'tuple'>
```

For a single-element tuple you must include a trailing comma, because `(42)` is read as a parenthesized number. [2]

**The `tuple()` constructor.** Besides literal syntax, you can build a tuple from any existing iterable — a list, a string, a range — by passing it to `tuple()`. This is the standard way to "freeze" a list into a tuple, or to turn a string into a tuple of its characters: [3]

```python
tuple([1, 2, 3])      # (1, 2, 3)   — from a list
tuple("abc")          # ('a', 'b', 'c')   — from a string, one char per element
tuple(range(4))       # (0, 1, 2, 3)   — from a range
tuple()               # ()   — an empty tuple, same as ()
```

Note `tuple([1, 2, 3])` takes **one** argument (the iterable). A common mistake is writing `tuple(1, 2, 3)`, which raises a `TypeError` — the constructor consumes a single iterable, not loose values. When you already have the items loose, just use the comma form `(1, 2, 3)`. [3]

### 5.2 Accessing elements: indexing and slicing

Because a tuple is a sequence, everything you learned about reading a list in 4.1 applies unchanged. Indexing starts at `0`, negative indices count from the end, and slicing returns a new tuple: [2]

```python
person = ("Ada", 36, True)
person[0]        # 'Ada'
person[-1]       # True   (last element)
person[0:2]      # ('Ada', 36)   — a slice, itself a tuple
len(person)      # 3
```

Slicing follows the same `[start:stop:step]` shape you used on lists, and every slice is a brand-new tuple: [2]

```python
nums = (10, 20, 30, 40, 50)
nums[1:4]        # (20, 30, 40)   — stop index is excluded
nums[:2]         # (10, 20)       — start defaults to 0
nums[3:]         # (40, 50)       — stop defaults to the end
nums[::2]        # (10, 30, 50)   — every second element
nums[::-1]       # (50, 40, 30, 20, 10)   — reversed
```

You can also iterate with a `for` loop and test membership, again just like a list:

```python
for value in person:
    print(value)

"Ada" in person     # True
99 in person        # False
```

The only thing you cannot do is *write*. This raises an error:

```python
person[1] = 40   # TypeError: 'tuple' object does not support item assignment
```

That error is the defining behavior of a tuple. A list would have accepted the assignment; a tuple refuses it. [1]

### 5.3 Immutability — the core difference from lists

Immutability means the tuple object itself cannot be altered after creation. There is no `.append()`, no `.remove()`, no `.sort()`, no `.pop()`, no `.insert()`, no index assignment — none of the mutating operations you used on lists in 4.1. A tuple only offers the read operations. [1][2]

Lists carry a whole family of mutating methods precisely because they are meant to change: `append`, `extend`, `insert`, `remove`, `pop`, `clear`, `sort`, `reverse`. **Tuples have none of these.** Trying any of them fails, because the method simply does not exist on a tuple: [1]

```python
point = (3, 5)
point.append(7)     # AttributeError: 'tuple' object has no attribute 'append'
point.sort()        # AttributeError: 'tuple' object has no attribute 'sort'
```

In fact, a tuple exposes exactly **two** methods — `count()` and `index()` (both read-only, covered in 5.7) — versus the roughly dozen a list carries. That short menu *is* the immutability guarantee, expressed as an API. [1]

If you need a "changed" tuple, you build a new one rather than editing the old one:

```python
point = (3, 5)
point = point + (7,)     # rebinds point to a NEW tuple (3, 5, 7)
```

Nothing was mutated here — the `+` produced a fresh tuple and `point` was reassigned to it. The original `(3, 5)` was untouched.

**Subtlety worth naming once:** immutability applies to the tuple's *structure* — which objects it holds and in what order — not necessarily to those objects' internal contents. If a tuple happens to contain a list, that inner list can still be edited, because the list itself is mutable; the tuple simply cannot swap it out for a different object. For the everyday case where tuples hold numbers, strings, and other tuples, treat a tuple as fully fixed. [1]

Because tuples are immutable and hashable in the common case, you will later be able to use a tuple as a dictionary key where a list cannot be — a small preview of why the fixed-versus-changeable distinction matters beyond this topic.

### 5.4 Tuple assignment and unpacking

**Unpacking** is the reverse of packing: you spread a tuple's values across several variables in one statement. The number of variables on the left must match the number of values on the right. [3]

```python
point = (3, 5)
x, y = point          # x = 3, y = 5
```

You can pack and unpack in the same line — which is exactly what the P1 form `x, y = 1, 2` was doing: the right side packs `(1, 2)`, the left side unpacks it. [3]

This gives Python its clean **variable swap**. In many languages swapping two variables needs a temporary third variable. In Python you unpack a packed pair: [3]

```python
a = 1
b = 2
a, b = b, a          # now a = 2, b = 1
```

The right-hand side `b, a` is evaluated *first* into the tuple `(2, 1)`, then unpacked into `a` and `b`. Because the whole right side is built before any assignment happens, no temporary variable is needed and the order is safe.

Unpacking is also why looping over structured data reads so well. When each element of a list is a tuple, the `for` loop can unpack it directly in the header: [3]

```python
pairs = [("Ada", 36), ("Alan", 41)]
for name, age in pairs:          # each tuple unpacks into name, age
    print(f"{name} is {age}")
```

This is far cleaner than indexing inside the loop (`row[0]`, `row[1]`). The same shape works for three-part records:

```python
scores = [("Ada", "math", 95), ("Alan", "cs", 88)]
for name, subject, score in scores:
    print(f"{name} scored {score} in {subject}")
```

If the counts do not match, Python raises a `ValueError` ("too many / not enough values to unpack"), which is a helpful signal that the data was not shaped the way you expected:

```python
x, y = (1, 2, 3)     # ValueError: too many values to unpack (expected 2)
```

**Star-unpacking (modern Python).** When you want the first item (or last) plus "everything else," prefix one target with `*` to collect the remainder into a list: [3]

```python
first, *rest = (1, 2, 3, 4)     # first = 1, rest = [2, 3, 4]
*head, last = (1, 2, 3, 4)      # head = [1, 2, 3], last = 4
```

The starred variable always becomes a list, and there may be at most one star on the left side. Reach for this when the exact length varies but you only care about the ends.

### 5.5 Nested tuples

A tuple can contain other tuples, just as a list can contain lists. This is how you represent tables, grids, or grouped records without any new syntax: [2]

```python
matrix = ((1, 2, 3),
          (4, 5, 6))
matrix[0]        # (1, 2, 3)   — the first inner tuple
matrix[0][2]     # 3           — chained indexing: row 0, column 2
matrix[1][0]     # 4
len(matrix)      # 2           — two rows
len(matrix[0])   # 3           — three columns in row 0
```

Reading a nested value is chained indexing, identical in feel to nested lists from 4.1: the first index selects the inner tuple, the second selects inside it. Immutability nests too — you cannot reassign `matrix[0]` to a different inner tuple.

A common real shape is a table of labeled records, where each row is itself a tuple. You can index down to a single field, and you can unpack a whole row at once:

```python
people = (("Ada", 36, "London"),
          ("Alan", 41, "Manchester"))
people[1][2]           # 'Manchester'
name, age, city = people[0]     # name='Ada', age=36, city='London'
```

Iterating over the outer tuple while unpacking each inner tuple combines everything in 5.4 and 5.5:

```python
for name, age, city in people:
    print(f"{name} ({age}) lives in {city}")
```

### 5.6 Basic tuple operations

Three operations round out the everyday toolkit; you already know all three operators from lists and from P1. [2]

**Concatenation with `+`** joins two tuples into a new one:

```python
(1, 2) + (3, 4)      # (1, 2, 3, 4)
```

**Repetition with `*`** repeats a tuple a whole number of times:

```python
(0,) * 3             # (0, 0, 0)
("ok",) * 2          # ('ok', 'ok')
```

**Membership with `in`** tests whether a value is present, returning a `bool`:

```python
3 in (1, 2, 3)       # True
9 in (1, 2, 3)       # False
```

Both `+` and `*` produce brand-new tuples rather than modifying an operand — consistent with immutability. `len()`, indexing, slicing, and `for`-iteration are available too. What is *absent* is any method that would change the tuple in place. [2]

### 5.7 The two tuple methods: `count()` and `index()`

A tuple offers exactly two methods, both of which only *read* — they never change the tuple, so they fit immutability perfectly. [1][2]

**`count(value)`** returns how many times a value appears:

```python
marks = (7, 3, 7, 7, 1)
marks.count(7)       # 3   — 7 appears three times
marks.count(9)       # 0   — not present, so zero
```

**`index(value)`** returns the position of the *first* occurrence of a value:

```python
marks = (7, 3, 7, 7, 1)
marks.index(7)       # 0   — first 7 is at position 0
marks.index(1)       # 4
marks.index(99)      # ValueError: tuple.index(x): x not in tuple
```

Note `index` raises a `ValueError` if the value is absent, so guard it with `in` when you are unsure:

```python
if 99 in marks:
    print(marks.index(99))
```

Contrast this with lists. A list has `count()` and `index()` too, but *also* `append`, `insert`, `remove`, `pop`, `sort`, `reverse`, and more — all of which mutate. The tuple keeps only the two that observe without changing. If you catch yourself wishing a tuple had `.append()`, that is the language telling you to use a list. [1]

### 5.8 Lexicographic comparison

Tuples support the comparison operators `<`, `>`, `==`, `<=`, `>=` from P1, and they compare **element by element, left to right** — the same rule dictionaries use for words, which is why it is called *lexicographic* (dictionary-order) comparison. [3]

Python compares the first elements; if they are equal it moves to the second, and so on, until a pair differs or one tuple runs out:

```python
(1, 2) < (1, 3)      # True  — first elements tie, 2 < 3 decides
(1, 2) == (1, 2)     # True  — same length, all elements equal
(1, 2, 3) < (1, 3)   # True  — 2 < 3 at position 1 decides; 3rd element never checked
(1, 2) < (1, 2, 0)   # True  — all shared elements tie, shorter tuple is "less"
("a", "b") < ("a", "c")   # True  — strings compare too
```

This is exactly what makes sorting a list of tuples "just work." Sorting orders by the first element, breaking ties with the second, and so on: [3]

```python
records = [("Ada", 36), ("Alan", 31), ("Ada", 20)]
sorted(records)      # [('Ada', 20), ('Ada', 36), ('Alan', 31)]
```

Here `"Ada"` sorts before `"Alan"`, and within the two `"Ada"` entries the ages `20` and `36` break the tie. You get multi-key sorting for free, purely because tuples compare position by position. (Comparison only works when the paired elements are themselves comparable — comparing a number to a string at the same position raises a `TypeError`.)

## 6. Implementation

Choosing and using a tuple is a small decision procedure. Walk it in order.

**Step 1 — List or tuple?** Ask one question: *will the collection's membership change?*
- If items will be added, removed, or reordered over the collection's life → **list**.
- If the group is a fixed-size, fixed-meaning record whose parts stay put → **tuple**. [1]

Rules of thumb: a coordinate, color, date, or "row" of related fields is a tuple; a running to-do list, a growing log, or a queue is a list.

**Step 2 — Pack or construct?**
- If you have the values loose in code, **pack** them: `p = 3, 5` or `p = (3, 5)`.
- If you already have an iterable (a list, a string, a range) and want it frozen, **construct**: `tuple(some_list)`. [3]

**Step 3 — Read by unpacking when the shape is known.**
- Fixed, known shape → unpack: `x, y = p`. Clearer than `p[0]` / `p[1]`, and it fails loudly on a shape mismatch.
- Position-by-position or variable length → index or slice: `p[0]`, `p[1:]`.

**Step 4 — "Changing" a tuple = building a new one.** You never mutate; you rebind:

```python
p = (3, 5)
p = p + (7,)          # append-like: new tuple (3, 5, 7)
p = (9,) + p[1:]      # replace element 0: new tuple (9, 5, 7)
```

The pattern `old[:i] + (new_value,) + old[i+1:]` produces a tuple identical to `old` except at position `i`. Nothing was mutated; `p` simply points at a fresh tuple.

**Worked multi-step example — building and processing `(name, score)` records.**

```python
# 1. Build a list of tuples (each record is a fixed 2-field tuple).
records = [("Ada", 95), ("Alan", 88), ("Grace", 95), ("Alan", 72)]

# 2. Iterate by unpacking, and use count/index for lookups.
names = tuple(name for _, name in [])   # (illustrative) — usually just loop:
total = 0
for name, score in records:             # unpack each tuple in the loop header
    total += score
average = total / len(records)          # 87.5

# 3. Membership + method: does anyone have a perfect-ish 95, and where first?
scores_only = tuple(score for name, score in records)   # (95, 88, 95, 72)
scores_only.count(95)      # 2   — two 95s
scores_only.index(95)      # 0   — first 95 is Ada's

# 4. Sort the records lexicographically (by name, then score).
ranked = sorted(records)   # [('Ada', 95), ('Alan', 72), ('Alan', 88), ('Grace', 95)]

# 5. "Change" Ada's record without mutating: rebuild the list with a new tuple.
records[0] = ("Ada", 100)  # allowed — the LIST is mutable; we swapped in a NEW tuple
                           # the old ('Ada', 95) tuple was never edited in place
```

Notice the division of labor: the **list** holds the changing collection of records, and each **tuple** is a fixed record inside it. Step 5 is the whole immutability story in one line — we did not edit a tuple, we replaced one tuple with a different one inside a mutable list. [1]

## 7. Real-World Patterns

- **Coordinates and fixed-size records.** A point `(x, y)`, a color `(r, g, b)`, or a date `(year, month, day)` is a group whose size never changes and whose parts have fixed meaning by position. A tuple communicates "these belong together and stay put" better than a list would. [1]
- **Returning several values from a function.** A `def` can `return name, age` and the caller unpacks it: `n, a = get_person()`. Under the hood that return value is a tuple — the most common place tuples appear without anyone typing parentheses. [3]
- **Iterating over paired data.** Looping `for name, age in pairs:` over a list of tuples reads almost like English and is the standard shape for row-by-row data. [3]
- **Multi-key sorting.** Because tuples compare lexicographically, `sorted(list_of_tuples)` orders by the first field, then the second, and so on — a free, readable way to sort records by more than one key. [3]

## 8. Best Practices

- **Prefer a tuple when the collection is fixed;** prefer a list when you expect to add, remove, or reorder items. Size and role that never change → tuple. Contents that grow or shrink → list. [1]
- **Use unpacking instead of indexing when the shape is known.** `x, y = point` is clearer than `point[0]` / `point[1]`, and it fails loudly if the data is the wrong shape.
- **Remember the trailing comma for one-element tuples:** `(x,)`, not `(x)`. The missing comma is a common, quiet bug.
- **Guard `index()` with `in`.** `t.index(v)` raises `ValueError` when `v` is absent; test `if v in t:` first if you are not sure.
- **Reach for `tuple(iterable)` to freeze a list**, and remember it takes one iterable — `tuple(1, 2, 3)` is an error, `tuple([1, 2, 3])` is correct.
- **Do not reach for a list just because you *might* change it "someday."** Choosing a tuple documents intent — it tells the next reader (and your future self) that these values are not meant to move. [1]
- **Don't fight immutability.** If you find yourself wanting to append repeatedly, that collection is a list, not a tuple.

## 9. Hands-On Exercise

Sketch (for the tuple lab): (1) Pack a coordinate `p = 4, 9` and print each part using unpacking. (2) Swap two variables with `a, b = b, a` and print the result. (3) Build a list of `(name, score)` tuples, loop over it unpacking `name, score`, and print an f-string per row; then call `.count()` and `.index()` on a tuple of just the scores. (4) `sorted()` your list of records and observe the lexicographic order. (5) Freeze a list with `tuple([...])`, then try to reassign one element and observe the `TypeError` — that error is the lesson.

## 10. Key Takeaways

- A tuple is an ordered, immutable sequence: it reads like a list (index, slice, loop, `in`) but cannot be changed after creation, and it has only two methods — `count()` and `index()`.
- The comma makes a tuple, not the parentheses — and a single-element tuple needs a trailing comma: `(x,)`. Build from any iterable with `tuple(iterable)`.
- Unpacking spreads a tuple across variables; the counts must match (`a, b = b, a` swaps with no temporary, `first, *rest = t` collects the remainder).
- Tuples compare lexicographically (`(1, 2) < (1, 3)` is `True`), which makes `sorted()` on a list of tuples do multi-key ordering for free.
- To "change" a tuple you build a new one; choose a tuple when the collection is fixed and a list when it will change — often a mutable list of fixed tuples.

## 11. Next Steps

_System-derived from the next entry in curriculum/sequence.md._
