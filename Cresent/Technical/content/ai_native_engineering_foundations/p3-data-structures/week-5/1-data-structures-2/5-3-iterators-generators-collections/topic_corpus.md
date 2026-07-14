---
topic_id: 5.3
title: Iterators, Generators & Collections
position_in_module: 3
generated_at: 2026-07-14T00:00:00Z
resource_count: 3
---

# 1. Iterators, Generators & Collections — Topic Corpus

## 2. Prerequisites

- **5.2 Dictionaries** — key-value mapping, `keys()`/`values()`/`items()`, `KeyError`, and especially the two from-scratch patterns you built by hand: the `counts[w] = counts.get(w, 0) + 1` counting loop (§6 of 5.2) and the `d.setdefault(k, []).append(x)` grouping loop (§5.6/§6 of 5.2). This topic gives you the dedicated tools those sections pointed forward to.
- **5.1 Sets** — hashable elements and the idea that membership and counting depend on values being hashable.
- **4.1 Lists** — iteration with `for`, `in` membership, list comprehension `[x for x in xs]`.
- **4.2 Tuples** — immutability, tuple unpacking, and the motivation for giving fields *names* rather than remembering positions.
- P1/P2 (assumed): `for` loops, functions, and **generators / `yield`** (introduced in P2 — this topic re-establishes them, it does not teach them from zero).

## 3. Learning Objectives

By the end of this topic you should be able to:

- **Distinguish** an *iterable* from an *iterator*, and explain the iterator protocol — `iter()`, `next()`, and `StopIteration` — that a `for` loop runs under the hood.
- **Trace** what a `for` loop actually does when it walks any collection, and explain why an iterator is one-shot (it exhausts).
- **Recall** how a generator function uses `yield` to stream values lazily one at a time, and write a simple generator function and generator expression.
- **Use** `collections.Counter` to count hashable items in one line, and relate it to the `get(w, 0) + 1` loop you wrote in 5.2.
- **Use** `collections.defaultdict` with an `int` or `list` factory, and relate it to the `setdefault(k, []).append(x)` grouping loop you wrote in 5.2.
- **Use** `collections.namedtuple` to build readable, immutable records with named fields instead of bare positional tuples.

## 4. Introduction

Everything you have built this module — lists, tuples, sets, dictionaries — you have looped over with a `for` loop. You have written `for x in my_list`, `for c in my_set`, `for k, v in d.items()` without ever asking *how* Python knows what "the next item" is for each of these different structures. This topic answers that question. Underneath every `for` loop is a single, uniform mechanism — the **iterator protocol** — and understanding it turns the `for` loop from magic into something you can reason about, extend, and eventually write your own version of.

That mechanism also explains a tool you already met: **generators**. In P2 you saw functions that use `yield` to hand back values one at a time instead of building a whole list. It turns out a generator is just a convenient way to *make* an iterator — the same protocol, less typing. We re-establish that here so it clicks into the bigger picture.

Finally, this is the last topic of the module, and it closes a loop we opened twice. In 5.1 and 5.2 you built counting and grouping *by hand* — `counts.get(w, 0) + 1` and `setdefault(k, []).append(x)` — and each time a note promised "a dedicated tool later this week." That tool is the **`collections`** module: `Counter`, `defaultdict`, and `namedtuple`, three ready-made structures that make those exact patterns one line. **Assessment A2 — the Data Structures Portfolio — is due this week**, and knowing these tools completes your toolkit for its central question: *choose the right structure for the task, and reach for the idiom that expresses it cleanly.*

## 5. Core Concepts

### 5.1 Iterables vs iterators

Two words that sound alike name two genuinely different things, and the whole topic hinges on keeping them apart [1].

- An **iterable** is any object you can loop over — anything you can put after `in` in a `for` loop. Lists, tuples, sets, dictionaries, and strings are all iterables. Technically, an object is iterable if it defines a method called `__iter__` that hands back an iterator [1].
- An **iterator** is the object that actually does the walking. It knows *where it is* in the sequence and how to produce the *next* value. Technically, an object is an iterator if it defines a method called `__next__` that returns the next item each time it is called [1].

The relationship is: an iterable is a thing you *can* get an iterator from; an iterator is the thing that *does* the iterating [1]. A list is not itself an iterator — it does not remember a "current position." Instead, when you loop over a list, Python asks the list for a fresh iterator, and *that* iterator tracks the position. You can think of the iterable as a book and the iterator as a bookmark: the book holds the content, the bookmark remembers where you are, and you can have several bookmarks in the same book at once.

### 5.2 The iterator protocol: `iter()` and `next()`

You interact with this machinery through two built-in functions [1]:

- **`iter(obj)`** takes an iterable and returns a fresh iterator positioned at the start. Under the hood it calls the object's `__iter__` method [1].
- **`next(it)`** takes an iterator and returns its next value, advancing the position by one. Under the hood it calls the iterator's `__next__` method [1].

Watch it run by hand on a plain list:

```python
nums = [10, 20, 30]
it = iter(nums)        # get an iterator over the list

print(next(it))        # 10  — first item
print(next(it))        # 20  — second item
print(next(it))        # 30  — third item
print(next(it))        # StopIteration!  — nothing left
```

Each `next(it)` hands back the following value and moves the bookmark forward. When there are no items left, `next` does not return `None` or `-1` — it **raises `StopIteration`**, a special signal that means "the sequence is finished" [1]. That signal is the linchpin of the next section.

Note that `iter()` gave us a *separate* object; `nums` itself is untouched. If you called `iter(nums)` a second time you would get a brand-new iterator starting again at `10`. The list is reusable; each iterator is a single pass over it.

### 5.3 How a `for` loop works under the hood

Now the payoff. Every `for` loop you have ever written is shorthand for the protocol in §5.2. When you write [1]:

```python
for n in nums:
    print(n)
```

Python does exactly this, automatically:

1. Call `iter(nums)` **once** to get an iterator.
2. Call `next()` on that iterator to get the next value, and bind it to `n`.
3. Run the loop body.
4. Repeat steps 2–3.
5. When `next()` raises **`StopIteration`**, stop the loop silently — no error reaches you.

Spelled out with the raw protocol, the loop above is equivalent to:

```python
it = iter(nums)             # step 1
while True:
    try:
        n = next(it)        # step 2
    except StopIteration:   # step 5 — the loop's exit condition
        break
    print(n)                # step 3
```

This is worth sitting with, because it explains behaviour you would otherwise have to memorize. It explains why *any* iterable works in a `for` loop uniformly — the loop only ever speaks `iter()`/`next()`, so it does not care whether it is walking a list, a set, a dictionary, a file, or a generator. And it explains why the loop ends cleanly: `StopIteration` is the built-in "we're done" handshake, caught for you by the `for` statement [1].

### 5.4 An iterator is also an iterable — and it is one-shot

One subtlety trips people up, so state it plainly. An **iterator is itself an iterable**: calling `iter()` on an iterator returns *the same iterator* (its `__iter__` just returns `self`) [1]. That is why you can put an iterator directly in a `for` loop.

But an iterator is **one-shot** — it exhausts. Once `next()` has walked it to `StopIteration`, it is spent; looping it again yields nothing, because there is nothing left and the bookmark cannot rewind [1]:

```python
it = iter([1, 2, 3])
print(list(it))    # [1, 2, 3]  — first pass consumes the iterator
print(list(it))    # []          — nothing left; it is exhausted
```

Contrast that with the underlying list, which you can loop as many times as you like because each `for` loop asks it for a *fresh* iterator (§5.3). The rule to remember: **a list is reusable; an iterator is a single pass.** This distinction matters the moment you meet generators, because generators are iterators — and therefore one-shot too.

### 5.5 Generators recap: `yield` for streaming values

You already met generators in P2; here is the one-paragraph re-grounding, now that you can see where they fit. A **generator function** looks like an ordinary function but uses **`yield`** instead of (or in addition to) `return`. Calling it does not run the body — it hands back a **generator object**, which is a lazy iterator [2]. Each time you call `next()` on it (directly, or via a `for` loop), the function runs until it hits a `yield`, produces that value, and then **pauses** — freezing all its local state — until you ask for the next value [2]:

```python
def count_up_to(limit):
    n = 1
    while n <= limit:
        yield n        # hand back n, then pause here
        n += 1

for x in count_up_to(3):
    print(x)           # 1, then 2, then 3
```

Because a generator produces values **one at a time, on demand**, it never has to build the whole sequence in memory [2]. That laziness is the whole point: you can stream a million rows, or even model an *infinite* sequence, while only ever holding the current value. This is the memory-efficient alternative to building a giant list up front [2]. And it fits §5.3 perfectly — a generator is simply an iterator you wrote as a function, so the `for` loop drives it with the very same `iter()`/`next()`/`StopIteration` protocol. When the function finishes (falls off the end or hits `return`), Python raises `StopIteration` for you, which is exactly how the `for` loop above knows to stop [2].

There is also a compact one-liner form, the **generator expression** — a comprehension with **parentheses** instead of the square brackets of a list comprehension [2]:

```python
squares_list = [x * x for x in range(1_000_000)]   # builds the WHOLE list now
squares_gen  = (x * x for x in range(1_000_000))   # builds NOTHING yet; lazy
```

The list comprehension allocates a million numbers immediately; the generator expression allocates nothing until you iterate it, producing each square only as it is asked for [2]. Same syntax you already know from 4.1 and 5.1 comprehensions — swap `[]` for `()` and you get lazy streaming instead of an up-front list.

### 5.6 The `collections` module: purpose-built structures

Python's built-in `list`, `tuple`, `set`, and `dict` cover most needs, but a few patterns are common enough that the standard library ships specialized versions. They live in the **`collections`** module, which you import [3]:

```python
from collections import Counter, defaultdict, namedtuple
```

Three of them close loops opened earlier this week. `Counter` and `defaultdict` are the "dedicated tools" that 5.1 and 5.2 promised; `namedtuple` upgrades the bare tuples of 4.2. Each is a thin, readable improvement on something you can already do by hand — which is exactly why they are worth learning last: you understand the from-scratch version, so you can appreciate what the tool saves you [3].

### 5.7 `Counter` — counting done for you

In 5.2 you counted occurrences by hand with the dictionary pattern `counts[w] = counts.get(w, 0) + 1` — read the current count or 0, add one, store it back. **`Counter`** is a `dict` subclass that does exactly that, in one line: pass it any iterable and it returns a dictionary mapping each distinct item to how many times it appeared [3].

```python
# The from-scratch version you wrote in 5.2:
counts = {}
for ch in "mississippi":
    counts[ch] = counts.get(ch, 0) + 1

# The Counter version — same result, one line:
counts = Counter("mississippi")
# Counter({'i': 4, 's': 4, 'p': 2, 'm': 1})
```

Because a `Counter` *is* a dictionary, everything you learned in 5.2 still works: `counts['s']` gives `4`, and a key that was never seen returns `0` instead of raising `KeyError` (a small, convenient difference from a plain dict) [3]. It also adds the method you always wanted after counting — **`most_common(n)`**, which returns the `n` highest-count items already sorted, replacing the `sorted(items(), key=lambda kv: kv[1], reverse=True)` line from 5.2 [3]:

```python
words = ["red", "blue", "red", "green", "red", "blue"]
c = Counter(words)
print(c.most_common(2))    # [('red', 3), ('blue', 2)]
```

The items you count must be **hashable** — the same requirement as dictionary keys (5.2) and set elements (5.1), because `Counter` stores them as keys [3]. Reach for `Counter` whenever the task is "how many times does each thing occur?" — it is the idiomatic answer, and choosing it over a hand-rolled loop is exactly the A2-style judgment call.

### 5.8 `defaultdict` — no more missing-key handling

The other 5.2 pattern was grouping: `d.setdefault(k, []).append(x)`, where you had to "get-or-create the empty list" before appending, because `d[k].append(x)` on a missing key would raise `KeyError`. **`defaultdict`** is a `dict` subclass that removes that friction: you give it a **factory function** at creation, and whenever you access a *missing* key, it automatically calls the factory to create a default value for that key — no `KeyError` [3].

The two factories you will use constantly are `list` and `int` [3]:

```python
# Grouping — replaces setdefault(k, []).append(x) from 5.2:
groups = defaultdict(list)          # missing key auto-creates []
for name in ["ana", "ben", "amy"]:
    groups[name[0]].append(name)    # no setdefault needed
# {'a': ['ana', 'amy'], 'b': ['ben']}

# Counting — replaces get(k, 0) + 1 from 5.2:
counts = defaultdict(int)           # missing key auto-creates 0
for ch in "banana":
    counts[ch] += 1                 # no .get(ch, 0) needed
# {'b': 1, 'a': 3, 'n': 2}
```

The factory is *how* the default is made: `list` called with no arguments gives `[]`, `int()` gives `0`, so `defaultdict(list)` initializes missing keys to empty lists and `defaultdict(int)` to zero [3]. The key is created *on first access* — the moment you touch `groups[k]` for a new `k`, the empty list already exists to `.append` onto. Everything else is an ordinary dictionary, so `items()`, `keys()`, iteration, and the rest all behave exactly as in 5.2 [3].

For counting specifically, `Counter` (§5.7) is usually cleaner — use `defaultdict(int)` when you need custom increment logic, and `defaultdict(list)` (or `set`) for grouping, where it is the clear winner over `setdefault` [3].

### 5.9 `namedtuple` — tuples with named fields

In 4.2 you used tuples for fixed records — `point = (3, 5)` — but had to remember that `point[0]` was the x-coordinate and `point[1]` the y. That positional access is fragile: `record[4]` tells a reader nothing. **`namedtuple`** fixes this by letting you build a tuple type whose fields have *names*, while keeping everything that made tuples good: it is still a tuple, still immutable, still lightweight [3].

You define a named-tuple type once by giving it a type name and a list of field names, then create instances of it [3]:

```python
Point = namedtuple("Point", ["x", "y"])

p = Point(3, 5)
print(p.x, p.y)      # 3 5      — access by NAME
print(p[0], p[1])    # 3 5      — positional access still works too
```

The win is readability. `p.x` says what it means where `p[0]` did not, and because it is still a real tuple you can unpack it (`x, y = p`), compare it, and pass it anywhere a tuple is expected [3]. Like any tuple (4.2) it is **immutable** — `p.x = 9` raises an error — which makes a `namedtuple` an excellent, self-documenting way to model a fixed record: a coordinate, an RGB colour, a row from a CSV, a returned pair of values. It sits between a bare tuple (fast but anonymous) and a dictionary (labelled but mutable and heavier): use it when you want labelled fields *and* immutability [3].

## 6. Implementation

A decision guide for which tool this topic gives you:

1. **Do you need to understand or drive iteration manually** (e.g. peek one value at a time, or process a stream)? Use `iter()`/`next()` directly, and remember the iterator is one-shot (§5.4).
2. **Are you producing a sequence lazily, or streaming/large/infinite data?** Write a generator with `yield`, or a generator expression `(... for ... in ...)`, so you never build the whole thing in memory (§5.5).
3. **Is the task "how many times does each thing occur?"** Use `Counter(iterable)`, then `most_common(n)` to rank (§5.7).
4. **Is the task "group these items under a key," or "count with custom logic"?** Use `defaultdict(list)` for grouping, `defaultdict(int)` for counting (§5.8).
5. **Are you modelling a fixed record with named fields that should not change?** Use `namedtuple` (§5.9).

A worked example that ties the module together — take a stream of `(name, city)` sign-ins, count cities and group names by city:

```python
from collections import Counter, defaultdict, namedtuple

SignIn = namedtuple("SignIn", ["name", "city"])
records = [SignIn("Ana", "Paris"), SignIn("Ben", "Tokyo"),
           SignIn("Amy", "Paris"), SignIn("Cara", "Paris")]

# Count sign-ins per city — Counter over a generator expression (lazy, no temp list)
city_counts = Counter(r.city for r in records)
print(city_counts.most_common(1))     # [('Paris', 3)]

# Group names by city — defaultdict(list)
by_city = defaultdict(list)
for r in records:
    by_city[r.city].append(r.name)
# {'Paris': ['Ana', 'Amy', 'Cara'], 'Tokyo': ['Ben']}
```

Every piece here is something you built by hand earlier this week; the `collections` versions just say it more directly. Note `Counter(r.city for r in records)` feeds a **generator expression** (§5.5) straight into `Counter` — no intermediate list is ever built, which is the lazy-iteration idea paying off in one line.

## 7. Real-World Patterns

These tools appear constantly in working code, each as a cleaner answer to a task you would otherwise hand-roll:

- **Frequency analysis with `Counter`.** Word frequencies in text, most-visited pages in a log, most common error codes, top tags — all are `Counter(items).most_common(n)`. It is the default reach whenever a report asks "which happened most often?"
- **Grouping with `defaultdict(list)`.** Bucketing records by category — students by grade, orders by customer, files by extension — is `defaultdict(list)` plus a loop that appends. This is the everyday shape of turning a flat list into groups, and it is markedly cleaner than the `setdefault` version from 5.2.
- **Lazy streaming with generators.** Reading a huge file line by line, processing an API that returns pages of results, or building a pipeline of transformations all lean on generators so the program holds one item at a time rather than loading everything into memory (§5.5). This is how real data pipelines stay memory-safe on inputs too big to fit in RAM.
- **Readable records with `namedtuple`.** Function return values that bundle several pieces (`return Result(ok, message, code)`), rows parsed from a CSV, or fixed config records use `namedtuple` so callers write `result.code` instead of decoding `result[2]`.

For going further, the standard library's **`itertools`** module builds on the iterator protocol from §5.1–5.4 to compose iterators (chaining, grouping, windowing) — useful once you are comfortable here, but beyond this topic's scope.

## 8. Best Practices

- **Let the `for` loop drive iteration** in normal code; reach for raw `iter()`/`next()` only when you deliberately need one-value-at-a-time control (§5.2).
- **Remember an iterator is one-shot.** If you need to iterate the data twice, iterate the underlying *iterable* (the list/set/dict) each time, or materialize the iterator with `list(it)` once (§5.4).
- **Use a generator expression `(...)` instead of a list comprehension `[...]`** when the result is only iterated once or is large — it avoids building the whole list (§5.5).
- **Reach for `Counter` over a hand-written `get(x, 0) + 1` loop** for counting; use `most_common(n)` instead of re-sorting `items()` (§5.7).
- **Reach for `defaultdict(list)` over `setdefault(k, []).append(x)`** for grouping — it states the intent (missing key = empty list) once, at creation (§5.8).
- **Use `namedtuple` when a tuple's positions have meaning** — `p.x` documents what `p[0]` hid, at no cost to immutability (§5.9).
- **Do not mistake a `Counter`/`defaultdict` for a special type you must handle specially** — both *are* dictionaries; everything from 5.2 still applies.
- **Items counted by `Counter` and keys in a `defaultdict` must be hashable** — the same rule as set elements (5.1) and dict keys (5.2).

## 9. Hands-On Exercise

Given a list of log lines, each a string like `"WARN disk"`, `"ERROR net"`, `"WARN cpu"`:

1. Split each line into a `LogEntry = namedtuple("LogEntry", ["level", "subsystem"])` (§5.9).
2. Use a **generator expression** to stream the `level` of each entry into a `Counter`, then print `most_common()` to rank levels by frequency (§5.5, §5.7).
3. Build a `defaultdict(list)` mapping each `level` to the list of subsystems that reported at that level (§5.8).
4. As a protocol check: call `iter()` on your list, pull the first two entries with `next()`, and confirm a second full pass over the *iterator* yields nothing while a pass over the *list* still works (§5.2, §5.4).

This exercises the whole toolkit the A2 portfolio rewards: choosing the right structure and the idiom that expresses it.

## 10. Key Takeaways

- An **iterable** is anything you can loop over (`__iter__`); an **iterator** is the object that produces items one at a time (`__next__`). `iter(obj)` gets an iterator; `next(it)` advances it and raises **`StopIteration`** when exhausted.
- A **`for` loop is just this protocol**: it calls `iter()` once, then `next()` repeatedly, stopping silently on `StopIteration` — which is why every iterable loops uniformly. An **iterator is one-shot** (it exhausts); the underlying iterable is reusable.
- A **generator** (a function using `yield`, or a `(... for ...)` expression) is a lazy iterator that streams values one at a time without building them all in memory — ideal for large or infinite sequences.
- **`Counter(iterable)`** counts hashable items in one line and ranks them with **`most_common(n)`** — the dedicated replacement for the `get(w, 0) + 1` loop from 5.2.
- **`defaultdict(factory)`** auto-initializes missing keys by calling the factory: `defaultdict(list)` for grouping (replacing `setdefault(k, []).append`) and `defaultdict(int)` for counting.
- **`namedtuple`** gives a tuple named, self-documenting fields (`p.x`) while staying immutable — the readable upgrade to the bare tuples of 4.2.

## 11. Next Steps

_System-derived from the next entry in curriculum/sequence.md._
