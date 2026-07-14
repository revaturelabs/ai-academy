# Tuples

## Overview

You just spent 4.1 learning lists — ordered, indexable, and freely editable. A **tuple** is the same idea with one deliberate restriction removed: you cannot change it after you create it. That single difference — immutability — is the whole point of the topic. Where a list says "here is a collection I might edit," a tuple says "here is a fixed group of values that belong together and will not move" [1]. A pair of coordinates, an RGB color, or a database row are groups where changing one value in place would usually be a bug, not a feature, and picking "list or tuple?" is one of the first data-structure choices you will make.

_This contributes to A2 — Data Structures Portfolio (due W5)._

## Key Concepts

<u>**What a tuple is.**</u> A tuple is an **ordered, immutable sequence** of values. "Ordered" and "sequence" mean it behaves like a list for reading: elements have positions, you index them, loop over them, and slice them. "Immutable" means that once built, its contents cannot change — no adding, removing, or reassigning an element [1][2]. You write one with parentheses and comma-separated values, and the values need not share a type:

```python
point  = (3, 5)
rgb    = (255, 128, 0)
person = ("Ada", 36, True)   # mixed types are fine, exactly like a list
empty  = ()                  # an empty tuple
```

<u>**Packing & the `tuple()` constructor.**</u> The parentheses are actually optional — when you write several comma-separated values, Python *packs* them into a tuple automatically [3]. The comma is what makes a tuple, not the parentheses, which leads to one gotcha: `(42)` is just the int `42`, so a one-element tuple needs a trailing comma, `(42,)`. Besides literal syntax, `tuple()` builds a tuple from any existing iterable [3]:

```python
point  = 3, 5         # same as (3, 5) — packing, no parentheses needed
single = (42,)        # a one-element tuple — note the trailing comma
tuple([1, 2, 3])      # (1, 2, 3)          — freeze a list
tuple("abc")          # ('a', 'b', 'c')    — one char per element
tuple(range(4))       # (0, 1, 2, 3)
```

Note that `tuple()` takes **one** argument — an iterable. Writing `tuple(1, 2, 3)` raises a `TypeError`; when the items are loose, use the comma form `(1, 2, 3)` instead [3].

<u>**Indexing & slicing.**</u> Because a tuple is a sequence, everything you learned about reading a list in 4.1 applies unchanged: indexing starts at `0`, negative indices count from the end, slicing uses `[start:stop:step]` and returns a brand-new tuple, and you can loop and test membership [2]:

```python
person = ("Ada", 36, True)
person[0]        # 'Ada'
person[-1]       # True     (last element)
person[0:2]      # ('Ada', 36)  — a slice, itself a tuple
nums = (10, 20, 30, 40, 50)
nums[::-1]       # (50, 40, 30, 20, 10)  — reversed
```

<u>**Immutability.**</u> The one thing you cannot do is *write*. `person[1] = 40` raises `TypeError: 'tuple' object does not support item assignment` — a list would accept it, a tuple refuses [1]. A tuple has none of the mutating methods you used on lists (`append`, `insert`, `remove`, `pop`, `sort`, `reverse`); calling one raises an `AttributeError` because the method does not exist [1][2]. In fact a tuple exposes exactly **two** methods — `count()` and `index()`, both read-only — versus the roughly dozen a list carries; that short menu *is* the immutability guarantee expressed as an API. To get a "changed" tuple you build a new one rather than editing the old:

```python
point = (3, 5)
point = point + (7,)   # rebinds point to a NEW tuple (3, 5, 7); original untouched
```

One subtlety, named once: immutability applies to the tuple's *structure* — which objects it holds and in what order — not to those objects' internals. A tuple holding a list can still have that inner list edited, but for the everyday case of numbers, strings, and other tuples, treat a tuple as fully fixed [1]. (Because tuples are immutable in the common case, you will later be able to use one as a dictionary key where a list cannot.)

<u>**Unpacking & swap.**</u> **Unpacking** is the reverse of packing: you spread a tuple's values across several variables in one statement, and the counts must match or Python raises a `ValueError` [3]. The P1 form `x, y = 1, 2` was doing exactly this — the right side packs `(1, 2)`, the left side unpacks it. This gives Python its clean **variable swap**, with no temporary variable, because the whole right side is built into a tuple *before* any assignment happens:

```python
a, b = b, a          # right side packs (b, a), then unpacks — swap done

pairs = [("Ada", 36), ("Alan", 41)]
for name, age in pairs:          # each tuple unpacks in the loop header
    print(f"{name} is {age}")    # cleaner than row[0], row[1]
```

Star-unpacking collects "everything else" into a list: `first, *rest = (1, 2, 3, 4)` gives `first = 1`, `rest = [2, 3, 4]`; at most one star is allowed [3].

<u>**Nested tuples.**</u> A tuple can contain other tuples, so you can represent tables or grids with no new syntax. Reading a nested value is **chained indexing** — the first index selects the inner tuple, the second reaches inside it — and immutability nests too [2]:

```python
matrix = ((1, 2, 3),
          (4, 5, 6))
matrix[0]        # (1, 2, 3)  — the first inner tuple
matrix[0][2]     # 3          — chained indexing: row 0, column 2
name, age, city = ("Ada", 36, "London")   # unpack a whole record at once
```

<u>**Operations & methods.**</u> Three operations round out the toolkit, all using operators you already know from lists and P1 [2]:

- **Concatenation `+`** joins two tuples into a new one: `(1, 2) + (3, 4)` → `(1, 2, 3, 4)`.
- **Repetition `*`** repeats a tuple: `(0,) * 3` → `(0, 0, 0)`.
- **Membership `in`** tests presence, returning a `bool`: `3 in (1, 2, 3)` → `True`.

Both `+` and `*` produce fresh tuples rather than modifying an operand, consistent with immutability. The two read-only methods are [1][2]:

- **`count(value)`** returns how many times a value appears: `(7, 3, 7, 7, 1).count(7)` → `3`.
- **`index(value)`** returns the position of the *first* occurrence: `(7, 3, 7, 7, 1).index(7)` → `0`; it raises `ValueError` if the value is absent, so guard it with `in` when unsure.

<u>**Comparison.**</u> Tuples support `<`, `>`, `==`, `<=`, `>=` and compare **element by element, left to right** — the same rule dictionaries use for words, which is why it is called *lexicographic* (dictionary-order) comparison [3]. Python compares the first elements; if they tie it moves to the second, and so on, until a pair differs or one tuple runs out:

```python
(1, 2) < (1, 3)        # True  — first tie, 2 < 3 decides
(1, 2) < (1, 2, 0)     # True  — shared elements tie, shorter is "less"
("a", "b") < ("a", "c")  # True — strings compare too
```

This is why sorting a list of tuples "just works": `sorted()` orders by the first field, breaks ties with the second, and so on — multi-key ordering for free [3]. (Comparison only works when paired elements are themselves comparable; a number versus a string raises a `TypeError`.)

<u>**Tuple vs list.**</u> Ask one question — *will the collection's membership change?* [1] Decide like this:

- Items will be added, removed, or reordered → **list** (a to-do list, a growing log, a queue).
- The group is a fixed-size, fixed-meaning record whose parts stay put → **tuple** (a coordinate, color, date, or row).
- You have loose values in code → **pack** them: `p = 3, 5`.
- You already have an iterable and want it frozen → **construct**: `tuple(some_list)`.
- The shape is known → read by **unpacking** (`x, y = p`); it is clearer than indexing and fails loudly on a mismatch.

## Worked Example

Here a **list** holds the changing collection of records, while each **tuple** is a fixed record inside it — the two structures doing their natural jobs:

```python
# 1. Build a list of fixed 2-field tuples.
records = [("Ada", 95), ("Alan", 88), ("Grace", 95), ("Alan", 72)]

# 2. Iterate by unpacking each tuple in the loop header.
total = 0
for name, score in records:
    total += score
average = total / len(records)          # 87.5

# 3. Membership + methods on a tuple of just the scores.
scores_only = (95, 88, 95, 72)
scores_only.count(95)      # 2  — two 95s
scores_only.index(95)      # 0  — first 95 is Ada's

# 4. Sort lexicographically: by name, then score.
ranked = sorted(records)   # [('Ada', 95), ('Alan', 72), ('Alan', 88), ('Grace', 95)]

# 5. "Change" Ada's record without mutating a tuple.
records[0] = ("Ada", 100)  # the LIST is mutable; we swap in a NEW tuple
                           # the old ('Ada', 95) tuple was never edited in place
```

Step 5 is the whole immutability story in one line: we did not edit a tuple, we replaced one tuple with a different one inside a mutable list [1].

## In Practice

- **Coordinates and fixed-size records.** A point `(x, y)`, color `(r, g, b)`, or date `(year, month, day)` is a group whose size and per-position meaning never change — a tuple says "these belong together and stay put" better than a list [1].
- **Returning several values from a function.** `return name, age` and the caller unpacks `n, a = get_person()`; the return value is a tuple — the most common place tuples appear without anyone typing parentheses [3].
- **Iterating over paired data.** `for name, age in pairs:` over a list of tuples reads almost like English and is the standard row-by-row shape [3].
- **Multi-key sorting.** `sorted(list_of_tuples)` orders by the first field, then the second, purely because tuples compare lexicographically [3].
- **Do / don't.** Remember the trailing comma in `(x,)`; guard `index()` with `in`; use `tuple(iterable)` (one argument) to freeze a list; and don't fight immutability — if you keep wanting to `.append()`, that collection is a list [1].

## Key Takeaways

- A tuple is an ordered, immutable sequence: it reads like a list (index, slice, loop, `in`) but cannot change after creation, and it has only two methods — `count()` and `index()`.
- The comma makes a tuple, not the parentheses; a single-element tuple needs a trailing comma `(x,)`, and `tuple(iterable)` freezes any iterable.
- Unpacking spreads a tuple across variables (counts must match); `a, b = b, a` swaps with no temporary variable.
- Tuples compare lexicographically, so `sorted()` on a list of tuples gives multi-key ordering for free.
- To "change" a tuple you build a new one; choose a tuple when the collection is fixed and a list when it will change — often a mutable list of fixed tuples.

## References

1. Real Python — *Lists and Tuples in Python*. https://realpython.com/python-lists-tuples/
2. W3Schools — *Python Tuples*. https://www.w3schools.com/python/python_tuples.asp
3. Python Software Foundation — *Data Structures* (Python Tutorial). https://docs.python.org/3/tutorial/datastructures.html
