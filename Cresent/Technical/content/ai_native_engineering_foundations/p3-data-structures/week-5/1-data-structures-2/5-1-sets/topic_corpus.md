---
topic_id: 5.1
title: Sets
position_in_module: 1
generated_at: 2026-07-14T00:00:00Z
resource_count: 3
---

# 1. Sets — Topic Corpus

## 2. Prerequisites

- **4.1 Lists** — indexing, slicing, mutability, iteration, `in` membership, list comprehension.
- **4.2 Tuples** — immutability, and the idea that some objects can be used as fixed, hashable values.
- P1 (assumed): `int`/`float`/`str`/`bool`, operators, `print()`, f-strings, and the `in` membership idea.
- P2 (assumed): `for` loops, conditionals, functions.

## 3. Learning Objectives

By the end of this topic you should be able to:

- **Create** a set from literals and from an iterable, and explain the uniqueness guarantee that removes duplicates automatically.
- **Choose** a set over a list when the task is about uniqueness, membership testing, or overlap between collections.
- **Apply** the four core set operations — union, intersection, difference, and symmetric difference — using both operator (`|`, `&`, `-`, `^`) and method forms, and use their in-place variants when you want to mutate a set instead of building a new one.
- **Compare** two sets with the subset, superset, and disjoint relations (`<=`, `>=`, `<`, `>`, `issubset`, `issuperset`, `isdisjoint`).
- **Mutate** a set safely with `add`, `remove`, and `discard`, and describe how `remove` and `discard` differ on a missing element.
- **Explain** why set membership (`in`) is fast — roughly constant time via hashing — compared with scanning a list, and choose the structure accordingly.
- **Use** `frozenset` when you need an immutable set, and **write** a simple set comprehension by analogy with the list comprehension you already know.

## 4. Introduction

You already have lists and tuples. Both keep every item you put in — duplicates and all — and both remember order. But a lot of real data work is not about order at all. It is about *which distinct things are present* and *whether two collections overlap*. "Which unique tags did users apply?" "Which email addresses appear in both mailing lists?" "Which items are in the new inventory but not the old one?" Answering these with a list means writing loops that check for duplicates by hand — slow to write and easy to get wrong.

A **set** is Python's built-in answer. Think of it as "like a list, but unordered and with no duplicates" [1]. You throw items in, duplicates silently collapse to one, and Python gives you fast, readable operators for combining and comparing sets. It is the same mental model as the Venn diagrams you drew in school: two overlapping circles, and questions about what is in one, the other, both, or exactly one.

This matters right now. **Assessment A2 — the Data Structures Portfolio — is due this week**, and it asks you to *choose the right data structure for a data-handling task*. Sets are the correct pick whenever the task turns on uniqueness, membership, or overlap. Reaching for a set instead of a hand-rolled list loop is exactly the kind of judgment A2 rewards — and it is the first structural choice you will make in the Data Structures (2) module.

## 5. Core Concepts

### 5.1 What a set is

A set is an **unordered collection of unique, immutable elements** [1][3]. Three words carry the weight:

- **Unordered** — a set does not track position. There is no `my_set[0]`; indexing and slicing (which you used on lists and tuples in 4.1 and 4.2) simply do not apply. When you print a set the elements may appear in any order, and that order can change between runs [2].
- **Unique** — a set never holds two equal elements. This is the *uniqueness guarantee*, and it is the whole point.
- **Immutable elements** — every item you store must itself be immutable (hashable). Numbers, strings, and the tuples from 4.2 are fine. A list is not, because lists can change — try to put one in a set and Python raises `TypeError` [3]. (The set *itself* is mutable — you can add and remove elements — but each element must be an unchangeable value.)

It helps to place a set directly against the two structures you already know:

| | List (4.1) | Tuple (4.2) | Set (here) |
|---|---|---|---|
| Ordered / indexable | yes | yes | **no** |
| Allows duplicates | yes | yes | **no** |
| Mutable container | yes | no | yes |
| Elements must be immutable | no | no | **yes** |
| Written with | `[ ]` | `( )` | `{ }` or `set()` |

Read the "no" column top to bottom and you have the definition of a set at a glance: it drops order and duplicates in exchange for the uniqueness guarantee and fast membership. Everything else about how you *use* it — iterating with a `for` loop, testing with `in`, building with a comprehension — is deliberately the same as the lists and tuples you already know, so there is very little new syntax to absorb. The novelty is entirely in *what a set promises*, not in how you type it.

Why does dropping order buy anything? Because a list has to preserve position, checking "is X in this list?" means walking the list element by element. A set stores its elements by their hash value instead of by position, so a membership test goes almost straight to the answer regardless of how big the set is. That is the practical pay-off of giving up order: `in` on a set stays fast even when the collection is large, whereas `in` on a list gets slower as the list grows. When your program asks "have I seen this before?" thousands of times, that difference is the reason to choose a set — and it is also why storing only immutable elements is required, since the hash of an element must never change while it sits in the set. Section 5.9 makes this performance point concrete.

### 5.2 Creating sets and the uniqueness guarantee

Write a set with curly braces around comma-separated values, or build one from any iterable with `set()` [1][2]:

```python
colors = {"red", "green", "blue"}
digits = set([1, 2, 3, 2, 1])   # from a list
letters = set("hello")          # from a string
```

The uniqueness guarantee is enforced *at construction*. Duplicates collapse the moment the set is built — you do not have to ask for it, and there is no way to switch it off [1]:

```python
digits = {1, 2, 3, 2, 1}
print(digits)          # {1, 2, 3}  — the repeats are gone
letters = set("hello")
print(letters)         # {'h', 'e', 'l', 'o'} — one 'l', in some order
```

Notice two things in that output. First, `set("hello")` produced individual *characters*, not the whole word — `set()` iterates whatever you pass it, and iterating a string yields its characters. Second, the elements printed in an order that has nothing to do with how you typed them; never write code that depends on it.

This gives the single most common one-liner involving sets: **de-duplicate a list** by round-tripping it through a set.

```python
names = ["ana", "ben", "ana", "cara", "ben"]
unique_names = list(set(names))   # duplicates removed
```

The `list(set(...))` idiom removes duplicates but *discards order* in the process. If you needed the original order preserved, this is the wrong tool; if you only care about the distinct values, it is the cleanest thing you can write.

One trap: `{}` is an **empty dictionary**, not an empty set. To make an empty set you must call `set()` with no arguments [1][3]. (You will meet dictionaries in the next topic; for now just remember the empty-set rule.)

```python
empty = set()      # correct empty set
not_a_set = {}     # this is an empty dict, not a set
```

### 5.3 Membership testing

Because a set is built around uniqueness, its headline query is "is this element present?" — the same `in` operator you already use on lists, strings, and tuples [2]:

```python
colors = {"red", "green", "blue"}
print("red" in colors)         # True
print("purple" in colors)      # False
print("purple" not in colors)  # True
```

Conceptually a set is *designed* for this question, which is why membership and de-duplication are the two reasons you reach for one. You can also loop over a set with a `for` loop exactly as you would a list [2], remembering only that the order you visit elements in is not guaranteed:

```python
for c in colors:
    print(c)     # visits every element once, in no particular order
```

### 5.4 The four set operations — operators and methods

This is where sets earn their place. Each operation has two spellings: a **method** (which will accept any iterable as its argument) and an **operator** (which requires both sides to be sets) [1][3]. They mean the same thing; the operator form reads like math, and the method form is handy when your right-hand side happens to be a list.

Take two sets:

```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
```

**Union** — everything in *either* set, combined, with duplicates collapsed [1][3]:

```python
a | b            # {1, 2, 3, 4, 5, 6}
a.union(b)       # {1, 2, 3, 4, 5, 6} — same result
a.union([5, 6, 7])   # {1, 2, 3, 4, 5, 6, 7} — method takes any iterable
```

**Intersection** — only elements in *both* sets, i.e. the overlap [1][3]:

```python
a & b                   # {3, 4}
a.intersection(b)       # {3, 4} — same result
a.intersection([3, 4, 99])  # {3, 4} — a plain list is fine as the argument
```

**Difference** — elements in the first set but *not* the second. Order matters here, because "what is in A that is not in B" is a different question from "what is in B that is not in A" [1][3]:

```python
a - b               # {1, 2}   — in a, not in b
b - a               # {5, 6}   — in b, not in a
a.difference(b)     # {1, 2} — same as a - b
```

**Symmetric difference** — elements in *exactly one* of the sets, i.e. in either but not both. It is the union minus the intersection [1][3]:

```python
a ^ b                        # {1, 2, 5, 6}
a.symmetric_difference(b)    # {1, 2, 5, 6} — same result
```

A quick way to keep them straight, mapping to two overlapping circles A and B:

| Operation | Operator | Method | Venn region |
|---|---|---|---|
| Union | `A \| B` | `A.union(B)` | both circles, all of it |
| Intersection | `A & B` | `A.intersection(B)` | the overlap only |
| Difference | `A - B` | `A.difference(B)` | A only (left crescent) |
| Symmetric difference | `A ^ B` | `A.symmetric_difference(B)` | both crescents, not the overlap |

All four return a **new** set and leave the originals `a` and `b` untouched [1]. Because each returns a set, you can chain them: `a | b | c` unions three sets, and `(a | b) - c` reads as "everything in a or b, then drop anything in c."

The operator-versus-method difference is worth pinning down, because it is the one place the two spellings genuinely diverge [3]. The **operator requires a set on both sides**: `a & [3, 4]` raises `TypeError`, because `&` refuses a list. The **method is more forgiving** — it will iterate any iterable you hand it, so `a.intersection([3, 4])` works and returns `{3, 4}`. This is not a cosmetic detail. Real data usually arrives as a list, and the method form lets you compare against it without a conversion step:

```python
requested = ["python", "data", "web"]        # a list from user input
available = {"python", "sets", "data"}        # a set
matches = available.intersection(requested)   # {"python", "data"} — no set() call needed
# available & requested would raise TypeError
```

Rule of thumb: reach for the **operator** when both sides are already sets and you want the expression to read like math; reach for the **method** when one side is a list, string, or other iterable you would otherwise have to wrap in `set()` first.

### 5.5 In-place update operators and methods

Each of the four operations also has an **in-place** form that *modifies the set on the left* rather than returning a new set [1][3]. There are two ways to spell each in-place form, mirroring §5.4: an augmented-assignment operator and a named method.

| Operation | In-place operator | In-place method | Effect on the left set |
|---|---|---|---|
| Union | `s \|= t` | `s.update(t)` | add everything in `t` |
| Intersection | `s &= t` | `s.intersection_update(t)` | keep only what is also in `t` |
| Difference | `s -= t` | `s.difference_update(t)` | drop everything that is in `t` |
| Symmetric difference | `s ^= t` | `s.symmetric_difference_update(t)` | keep only what is in exactly one |

The contrast with §5.4 is the whole point. The plain operators (`|`, `&`, `-`, `^`) **build a brand-new set and leave both operands alone**. The in-place forms **mutate `s` and return nothing useful** (the method returns `None`, just like `list.append`). Compare:

```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

c = a | b        # a and b unchanged; c is a NEW set {1,2,3,4,5,6}
print(a)         # {1, 2, 3, 4} — untouched

a |= b           # a is MUTATED in place -> {1, 2, 3, 4, 5, 6}
print(a)         # {1, 2, 3, 4, 5, 6}
```

The method spelling behaves identically to the operator, and — like the methods in §5.4 — the in-place *methods* accept any iterable, while the augmented operators require a set:

```python
s = {1, 2, 3, 4, 5}
s.difference_update([2, 4])   # drop 2 and 4 -> {1, 3, 5}; list argument is fine
s -= {5}                       # {1, 3}
s &= {1, 9}                    # keep only what is also in {1,9} -> {1}
```

When should you use the in-place form? When you are **accumulating into one set over time** and do not need the old value — for example, merging many small batches of results into a running `all_seen` set. `all_seen |= batch` is both clearer and cheaper than `all_seen = all_seen | batch`, because it avoids allocating a new set each round. When you need to keep the original set intact, use the plain (non-assigning) forms from §5.4 instead.

Note that `s.update(...)` is simply the in-place union, and it is common enough to have its own name; there is no separate `union_update`. And `add` (§5.7) is the single-element special case of `update`.

### 5.6 Subset, superset, and disjoint relations

Beyond combining sets, you often need to *compare* them: does one set sit entirely inside another? Are they completely separate? Python answers these questions with three relations, each available as both an operator and a method [1][3].

Take:

```python
small = {1, 2}
big   = {1, 2, 3, 4}
other = {5, 6}
```

**Subset** — is every element of the left set also in the right set? `<=` (or `issubset`) [1][3]:

```python
small <= big          # True  — every element of small is in big
small.issubset(big)   # True
big <= small          # False
small <= small        # True  — a set is a subset of itself
```

**Superset** — the mirror image: does the left set contain every element of the right? `>=` (or `issuperset`) [1][3]:

```python
big >= small            # True  — big contains all of small
big.issuperset(small)   # True
```

**Proper (strict) subset / superset** — `<` and `>` add the requirement that the sets are *not equal*. `small < big` is `True` because `small` is inside `big` **and** they differ; `small < small` is `False`, because a set is not a *proper* subset of itself [3]:

```python
small < big     # True  — subset AND not equal
small < small   # False — equal, so not a PROPER subset
small <= small  # True  — subset (equality allowed)
```

**Disjoint** — do the two sets share *no* elements at all? `isdisjoint` (there is no operator for this one) [1][3]:

```python
small.isdisjoint(other)   # True  — {1,2} and {5,6} share nothing
small.isdisjoint(big)     # False — they share 1 and 2
```

These relations return `True`/`False`, so they read naturally inside an `if`. A worked example — checking whether a user has all the permissions an action requires:

```python
required = {"read", "write"}
user_has = {"read", "write", "delete"}

if required.issubset(user_has):
    print("allowed")     # required is a subset of what the user has -> runs
```

Like the methods in §5.4, `issubset`, `issuperset`, and `isdisjoint` accept any iterable, so `required.issubset(["read", "write", "delete"])` also works; the `<=`/`>=`/`<`/`>` operators require sets on both sides.

### 5.7 Mutating a set: add, remove, discard

A set is mutable, so you can change its contents after creation [1][2]:

- **`add(x)`** — insert one element. If it is already present, nothing happens — the uniqueness guarantee again [2].
- **`remove(x)`** — delete `x`. If `x` is **not** in the set, it raises `KeyError` [1].
- **`discard(x)`** — delete `x`. If `x` is **not** in the set, it does nothing — no error [1].

```python
colors = {"red", "green"}
colors.add("blue")       # {"red", "green", "blue"}
colors.add("red")        # unchanged — "red" already present

colors.remove("green")   # ok -> {"red", "blue"}
colors.discard("pink")   # no-op, no error
colors.remove("pink")    # KeyError!
```

The `remove` vs `discard` distinction is the one learners trip on. Rule of thumb: use `discard` when you just want the element gone and do not care whether it was there; use `remove` when its absence would be a genuine bug you would want to hear about immediately. (There is also `pop()`, which removes and returns *some* element — but since a set is unordered you cannot predict which one, so it is rarely what you want. And `clear()` empties the set entirely.)

Because `add` builds a set up one element at a time while silently ignoring repeats, the classic "collect the distinct things I encounter" loop is a natural fit:

```python
seen = set()
for word in stream_of_words:
    seen.add(word)     # duplicates simply have no effect
```

After the loop, `seen` holds exactly the distinct words — no duplicate check required.

### 5.8 `frozenset` — the immutable set

Everything so far assumes a set you can change. Sometimes you want the opposite: a set whose contents can never be modified after creation. That is a **`frozenset`** [1][3]. The relationship between `set` and `frozenset` is exactly the relationship between list and tuple you learned in 4.1 and 4.2: same data, one mutable and one frozen.

You build one from any iterable, and once built it has no `add`, `remove`, `discard`, `update`, or any other mutating method — attempting them raises `AttributeError` [3]:

```python
fs = frozenset([1, 2, 3, 2])   # {1, 2, 3} — duplicates still collapse
fs.add(4)                       # AttributeError — a frozenset cannot change
```

A `frozenset` still supports every **non-mutating** operation: membership testing with `in`, iteration, and all of union / intersection / difference / symmetric difference and the subset/superset/disjoint relations from §5.4 and §5.6 [1][3]. Those operations return new sets (a `frozenset` when both operands are frozen), which is fine — they never claimed to mutate anything.

Why would you want one? The key payoff mirrors tuple immutability from 4.2: **because a `frozenset` cannot change, it is itself hashable, so it can be an element of another set** [3]. A regular `set` cannot go inside a set (it is mutable, therefore unhashable), but a `frozenset` can. Worked example — a collection of *distinct pairings*, where each pairing is itself an unordered group:

```python
teams = set()
teams.add(frozenset({"ana", "ben"}))
teams.add(frozenset({"ben", "ana"}))   # same pair, unordered — collapses
teams.add(frozenset({"cara", "dan"}))
print(len(teams))    # 2 — the first two are the same unordered pair
```

Because `frozenset({"ana","ben"})` and `frozenset({"ben","ana"})` are equal (sets ignore order), the second `add` is a no-op, and `teams` holds exactly two distinct pairings. You could not do this with plain sets as elements — Python would raise `TypeError: unhashable type: 'set'`. The two other everyday uses: a `frozenset` makes a safe **constant** (a fixed set of allowed values that no code can accidentally mutate), and it can serve as a stable key in structures that require hashable keys.

### 5.9 Why set membership is fast — hashing

Set membership deserves its own explanation because it is the single biggest reason to choose a set over a list. When you write `x in my_list`, Python has no shortcut: it compares `x` against the first element, then the second, and so on until it finds a match or reaches the end. For a list of *n* items that is up to *n* comparisons — the cost grows with the list. This is a *linear* scan, often written O(n).

A set works differently. It stores each element in a location computed from the element's **hash** — a number derived from the element's value. To test `x in my_set`, Python hashes `x`, jumps straight to the location that hash points to, and checks only there. It does **not** walk the whole collection. On average this takes the same small amount of time no matter how many elements the set holds — roughly *constant* time, written O(1) [1]. (This is exactly why every element must be immutable/hashable, as §5.1 stressed: the hash must stay stable while the element sits in the set.)

The gap is dramatic at scale. Testing membership against a set of ten items and a set of ten million items costs about the same; testing against a *list* of ten million items can be a million times slower than against a list of ten. A quick sketch of the difference:

```python
big_list = list(range(1_000_000))
big_set  = set(range(1_000_000))

999_999 in big_list   # correct, but Python may scan ~1,000,000 items
999_999 in big_set    # correct, and effectively instant — one hash lookup
```

When does this matter? Any time you test membership **repeatedly** — inside a loop, once per incoming record, in a crawler checking "have I visited this URL?", in a filter that keeps only allowed values. If you find yourself writing `if item in some_list` inside a loop over many items, converting `some_list` to a set once, up front, and then testing against the set is often the single highest-impact change you can make. This is the performance argument behind the de-dup and "seen" patterns in §7 — and recognizing it is precisely the data-structure judgment A2 asks you to demonstrate.

### 5.10 Set comprehension

You already write list comprehensions (from 4.1) like `[x*x for x in nums]`. A **set comprehension** is the exact same syntax with curly braces instead of square brackets, and it produces a set — so duplicates in the result collapse automatically [1][3]:

```python
nums = [1, 2, 2, 3, 3, 3, 4]
squares = {x * x for x in nums}            # {1, 4, 9, 16}
```

Everything you know about list comprehensions — the `for` clause, the optional `if` filter — carries straight over. Two worked cases cover almost everything you will write.

**Filtering** — keep only the items that pass a condition, using the `if` clause exactly as in a list comprehension, but ending up with a de-duplicated set [1]:

```python
nums = [1, 2, 2, 3, 3, 3, 4]
evens = {x for x in nums if x % 2 == 0}    # {2, 4}
```

**De-dup while transforming** — apply a transformation and collect only the distinct results, in one line. This is the case where a set comprehension really shines over its list cousin, because the transform can map several different inputs to the same output and the set silently keeps just one [1]:

```python
raw_names = ["Ana", "ANA", "ana", "Ben", "BEN"]
distinct = {name.lower() for name in raw_names}   # {"ana", "ben"}
```

Five differently-cased inputs collapse to two distinct lower-cased names — the transform and the de-duplication happen together. The only differences from a list comprehension are the braces and the fact that the output is unordered and de-duplicated.

## 6. Implementation

A practical decision procedure for whether to reach for a set:

1. **Do you care about order or position?** If yes — you need `[0]`, sorting by insertion, or duplicates preserved — use a list. Stop.
2. **Do duplicates carry meaning** (e.g. counting how many times something occurs)? If yes, a plain set loses that information — keep a list for now. (You will meet a dedicated counting tool later this week.)
3. **Is the question "which distinct items?", "is X present?", or "how do these two collections overlap?"** If yes, use a set.
4. **Do you need the set itself to be fixed, or to live inside another set?** If yes, use a `frozenset` (§5.8).

A worked micro-example — find tags used in both of two articles, tags unique to the first, and the full tag vocabulary:

```python
tags_a = {"python", "data", "sets", "python"}   # dup collapses to one
tags_b = {"data", "sql", "sets"}

shared   = tags_a & tags_b     # {"data", "sets"}   — in both
only_a   = tags_a - tags_b     # {"python"}         — first only
all_tags = tags_a | tags_b     # {"python", "data", "sets", "sql"}
one_only = tags_a ^ tags_b     # {"python", "sql"}  — in exactly one
```

Four readable expressions replace four hand-written loops. That readability, plus the automatic uniqueness, is the reason sets are the correct structural choice for these questions — and demonstrating that judgment is exactly what the A2 portfolio asks for.

If instead you were *building up* a combined vocabulary across many articles, the in-place form from §5.5 is cleaner:

```python
vocabulary = set()
for article_tags in all_articles:       # each is a list of tags
    vocabulary |= set(article_tags)      # accumulate into one running set
# or equivalently: vocabulary.update(article_tags)  — no set() needed
```

## 7. Real-World Patterns

Sets show up constantly in working code, almost always for one of three jobs. Each one is a direct answer to the A2 question "which data structure fits this task?" — and in each the deciding factor is uniqueness, membership speed, or overlap.

- **De-duplication.** Log processing, data cleaning, and import pipelines routinely funnel a messy list through `set()` to get the distinct values before doing anything else. `unique = set(rows)` in one line replaces a hand-written duplicate-checking loop. When you must also transform while de-duplicating (lower-casing emails, stripping whitespace), the set comprehension from §5.10 does both at once: `{e.strip().lower() for e in raw_emails}`. Choosing a set here is an A2-style call: the task says "distinct," so the structure is a set.

- **Fast membership / "have I seen this already?" tracking.** Crawlers, deduping loops, and cycle detection keep a `seen = set()` and check `if item in seen` before processing — fast even when `seen` grows to millions of entries, precisely because set membership does not slow down the way list membership does (§5.9). The classic shape:

  ```python
  seen = set()
  for url in urls_to_visit:
      if url in seen:      # O(1) check — stays fast as seen grows
          continue
      seen.add(url)
      process(url)
  ```

  If `seen` were a list, that `if url in seen` inside the loop would turn the whole job quadratic. This is the single most common reason a working program swaps a list for a set, and naming that reason is exactly the reasoning A2 rewards.

- **Finding overlap and uniques between two collections.** Comparing "roles the user has" against "roles this action requires" is an intersection; "which required roles are missing" is a difference; "does the user have everything required?" is a subset check (§5.6). Audience overlap between two mailing lists, common friends between two users, items in the new inventory but not the old — all of these are one- or two-line set operations rather than nested loops:

  ```python
  new_inv = {"a", "b", "c", "d"}
  old_inv = {"b", "d", "e"}

  added   = new_inv - old_inv          # {"a", "c"} — newly stocked
  removed = old_inv - new_inv          # {"e"}       — discontinued
  common  = new_inv & old_inv          # {"b", "d"}  — carried over
  ```

Where the elements themselves must be treated as unordered groups — distinct pairings, distinct coordinate sets — the `frozenset` pattern from §5.8 lets those groups live inside an outer set so the uniqueness guarantee applies to whole groups, not just scalars.

## 8. Best Practices

- **Reach for a set the moment the task says "unique", "distinct", "already seen", or "in both."** These words are the signal.
- **When you test membership repeatedly, use a set, not a list.** Converting a list to a set once, before a loop of `in` checks, is often the biggest single speed-up you can make (§5.9).
- **De-duplicate with `list(set(x))`** — but remember it *discards order*. If order matters, this is the wrong tool.
- **Use `set()`, never `{}`, for an empty set.** `{}` is an empty dictionary.
- **Prefer `discard` over `remove`** unless a missing element genuinely indicates a bug — it avoids surprise `KeyError`s.
- **Use the in-place forms (`|=`, `&=`, `-=`, `^=`, `update`, …) when accumulating into one set** and the plain forms when you must keep the original intact.
- **Prefer the method form (`.union`, `.intersection`, …) when the other side is a list** — it avoids a `set()` conversion; use the operator when both sides are already sets.
- **Do not try to store lists (or other mutable objects) in a set.** Convert to a tuple (from 4.2), or use a `frozenset`, if you need a compound element.
- **Do not rely on iteration order.** If you print or loop a set and need a stable order, sort it explicitly: `sorted(my_set)`.

## 9. Hands-On Exercise

Given two lists of student IDs — `morning` and `afternoon` sessions — that may contain duplicate sign-ins:

1. Build a set from each list to get the distinct attendees.
2. Report students who attended **both** sessions (intersection), those who attended **only the morning** (difference), the **total distinct** headcount (union), and those who attended **exactly one** session (symmetric difference).
3. Use a subset check to decide whether *every* morning attendee also came in the afternoon (`morning_set.issubset(afternoon_set)`), and `isdisjoint` to check whether the two sessions shared *no* students at all.
4. Build a `set` of `frozenset` pairs of students who signed in together, and confirm that reordering a pair does not create a duplicate.

This maps directly to the set-operations lab (P3.5) and to the overlap-analysis pattern the A2 portfolio rewards.

## 10. Key Takeaways

- A set is an **unordered collection of unique, immutable elements**; the uniqueness guarantee removes duplicates automatically at construction.
- Sets are the right choice for **membership testing, de-duplication, and overlap** — not for ordered or position-based data; A2 rewards making that call explicitly.
- The four operations are **union (`|`), intersection (`&`), difference (`-`), and symmetric difference (`^`)**, each with a method form that also accepts a plain iterable, and each with an **in-place** variant (`|=`, `&=`, `-=`, `^=`) that mutates the left set instead of returning a new one.
- **Subset/superset/disjoint** relations (`<=`, `>=`, `<`, `>`, `issubset`, `issuperset`, `isdisjoint`) compare whether one set sits inside another or whether two sets share nothing.
- **Set membership (`in`) is roughly O(1) via hashing**, so it stays fast at any size, while list membership is a linear scan that slows as the list grows.
- A **`frozenset`** is the immutable set (set is to frozenset as list is to tuple); being immutable, it is hashable and can itself be an element of another set.
- A **set comprehension** is a list comprehension with curly braces; the result is unordered and de-duplicated, which makes it ideal for de-dup-while-transforming.

## 11. Next Steps

_System-derived from the next entry in curriculum/sequence.md._
