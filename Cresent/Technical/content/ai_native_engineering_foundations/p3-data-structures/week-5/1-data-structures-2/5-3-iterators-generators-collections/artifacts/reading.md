# Iterators, Generators & Collections

<sub>[&#8592; Previous: 5.2 Dictionaries](../../../../../../../content/ai_native_engineering_foundations/p3-data-structures/week-5/1-data-structures-2/5-2-dictionaries/artifacts/reading.md)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Go back to TOC](../../../../../../../README.md)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Next: 6.1 Object-Oriented Foundations &#8594;](../../../../../../../content/ai_native_engineering_foundations/p4-classes-objects/week-6/1-classes-objects/6-1-object-oriented-foundations/artifacts/reading.md)</sub>

---

## Overview

Every `for` loop you have written this module — over lists, tuples, sets, and dictionaries — has quietly relied on one uniform mechanism you never had to name: the iterator protocol. This topic pulls back the curtain on it, re-grounds the generators you met in P2 as a lightweight way to build iterators, and closes two loops from earlier this week by handing you the `collections` module's ready-made tools for counting, grouping, and record-keeping. This is the last topic of the module, and it completes your toolkit for **Assessment A2 — the Data Structures Portfolio (due this week)**, whose central question is: choose the right structure for the task, and reach for the idiom that expresses it cleanly.

## Key Concepts

<strong><u>Iterable vs iterator.</u></strong> Two words that sound alike name two genuinely different things, and the whole topic hinges on keeping them apart [1].

- An **iterable** is any object you can loop over — anything you can put after `in` in a `for` loop. Lists, tuples, sets, dictionaries, and strings are all iterables. Technically, an object is iterable if it defines a method called `__iter__` that hands back an iterator [1].
- An **iterator** is the object that actually does the walking. It knows *where it is* and how to produce the *next* value. Technically, an object is an iterator if it defines a method called `__next__` that returns the next item each time it is called [1].

A list is not itself an iterator — it does not remember a "current position." When you loop over a list, Python asks the list for a fresh iterator, and *that* iterator tracks the position [1]. Think of the iterable as a book and the iterator as a bookmark: the book holds the content, the bookmark remembers where you are, and you can have several bookmarks in one book at once.

<strong><u>The iterator protocol: `iter()` and `next()`.</u></strong> You interact with this machinery through two built-in functions [1]:

- **`iter(obj)`** takes an iterable and returns a fresh iterator positioned at the start (it calls the object's `__iter__`) [1].
- **`next(it)`** takes an iterator and returns its next value, advancing the position by one (it calls the iterator's `__next__`) [1].

When there are no items left, `next` does not return `None` or `-1` — it **raises `StopIteration`**, a special signal meaning "the sequence is finished" [1]. That signal is the linchpin of the `for` loop.

<strong><u>How a `for` loop works under the hood.</u></strong> Every `for` loop you have ever written is shorthand for that protocol. When you write `for n in nums:`, Python does exactly this, automatically [1]:

1. Call `iter(nums)` **once** to get an iterator.
2. Call `next()` on that iterator to get the next value, and bind it to `n`.
3. Run the loop body.
4. Repeat steps 2–3.
5. When `next()` raises **`StopIteration`**, stop the loop silently — no error reaches you.

This explains behaviour you would otherwise memorize: *any* iterable works in a `for` loop uniformly, because the loop only ever speaks `iter()`/`next()` — it does not care whether it is walking a list, a set, a dict, a file, or a generator. And the loop ends cleanly because `StopIteration` is the built-in "we're done" handshake, caught for you [1].

<strong><u>One-shot iterators.</u></strong> An iterator is itself an iterable — calling `iter()` on an iterator returns *the same iterator* — which is why you can drop one straight into a `for` loop [1]. But an iterator is **one-shot**: once `next()` has walked it to `StopIteration`, it is spent, and looping it again yields nothing because the bookmark cannot rewind [1]. Contrast that with the underlying list, which you can loop as many times as you like because each `for` loop asks it for a *fresh* iterator. The rule to remember: **a list is reusable; an iterator is a single pass.** This matters the moment you meet generators, because generators are iterators — and therefore one-shot too.

<strong><u>Generators recap: `yield` for streaming.</u></strong> You already met generators in P2; here is the re-grounding now that you can see where they fit. A **generator function** looks like an ordinary function but uses **`yield`** instead of (or with) `return`. Calling it does not run the body — it hands back a **generator object**, a lazy iterator [2]. Each `next()` runs the function until it hits a `yield`, produces that value, then **pauses** — freezing all local state — until you ask again [2]. Here is a real `def ... yield` function, driven by a `for` loop:

```python
def count_up_to(limit):
    n = 1
    while n <= limit:
        yield n        # hand back n, then pause here
        n += 1

for x in count_up_to(3):
    print(x)           # 1, then 2, then 3
```

The `for` loop drives `count_up_to` with the very same `iter()`/`next()`/`StopIteration` protocol from above — each pass resumes the function right after the `yield`, and when the function finishes Python raises `StopIteration` so the loop stops [2]. Because it produces values one at a time, on demand, a generator never builds the whole sequence in memory: you can stream a million rows, or model an *infinite* sequence, while holding only the current value [2].

<strong><u>Generator expressions.</u></strong> There is also a compact one-liner, the **generator expression** — a comprehension with **parentheses** instead of the square brackets of a list comprehension [2]:

```python
squares_list = [x * x for x in range(1_000_000)]   # builds the WHOLE list now
squares_gen  = (x * x for x in range(1_000_000))   # builds NOTHING yet; lazy
```

Same syntax you know from 4.1 and 5.1 comprehensions — swap `[]` for `()` and you get lazy streaming instead of an up-front list [2]. Use the function form when the logic needs statements (loops, conditions, bookkeeping); use the expression form when a single mapping fits on one line.

<strong><u>The `collections` module.</u></strong> Python's built-in `list`, `tuple`, `set`, and `dict` cover most needs, but a few patterns are common enough that the standard library ships specialized versions in the **`collections`** module [3]:

```python
from collections import Counter, defaultdict, namedtuple
```

Three of them close loops opened earlier this week — each a thin, readable improvement on something you can already do by hand, which is exactly why they are worth learning last [3].

<strong><u>Counter.</u></strong> In 5.2 you counted occurrences with the by-hand version you wrote, `counts[w] = counts.get(w, 0) + 1`. **`Counter`** is a `dict` subclass that does exactly that in one line: pass it any iterable and it maps each distinct item to how many times it appeared [3]. Because a `Counter` *is* a dictionary, everything from 5.2 still works — `counts['s']` gives the count, and an unseen key returns `0` instead of raising `KeyError` [3]. It also adds the method you always wanted: **`most_common(n)`** returns the `n` highest-count items already sorted, replacing the `sorted(items(), key=...)` line from 5.2 [3]. The items counted must be **hashable** — the same rule as dict keys (5.2) and set elements (5.1) [3].

<strong><u>defaultdict.</u></strong> The other 5.2 pattern was grouping — the by-hand version `d.setdefault(k, []).append(x)`, where you had to get-or-create the empty list first because `d[k].append(x)` on a missing key raises `KeyError`. **`defaultdict`** removes that friction: give it a **factory function** at creation, and any access to a *missing* key auto-calls the factory to create a default — no `KeyError` [3]. The two factories you will use constantly are `list` and `int`: `defaultdict(list)` initializes missing keys to `[]` (grouping), and `defaultdict(int)` to `0` (counting) [3]. Everything else is an ordinary dictionary [3].

<strong><u>namedtuple.</u></strong> In 4.2 you used bare tuples for records — `point = (3, 5)` — but had to remember that `point[0]` was x and `point[1]` was y; that positional access is fragile. **`namedtuple`** lets you build a tuple type whose fields have *names* while keeping everything that made tuples good: still a tuple, still immutable, still lightweight [3]. The win is readability — `p.x` says what it means where `p[0]` did not — and because it is still a real tuple you can unpack it, compare it, and pass it anywhere a tuple is expected [3]. It sits between a bare tuple (fast but anonymous) and a dictionary (labelled but mutable and heavier): use it when you want labelled fields *and* immutability [3].

## Worked Example

First, watch the protocol run by hand on a plain list — including the one-shot behaviour:

```python
nums = [10, 20, 30]
it = iter(nums)        # get an iterator over the list
print(next(it))        # 10
print(next(it))        # 20
print(next(it))        # 30
print(next(it))        # StopIteration!  — nothing left

it = iter([1, 2, 3])
print(list(it))    # [1, 2, 3]  — first pass consumes the iterator
print(list(it))    # []          — exhausted; a list would still be reusable
```

Now tie the whole toolkit together — take a stream of `(name, city)` sign-ins, count cities, and group names by city:

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

`SignIn` reads `r.city` instead of `r[1]`; `Counter(r.city for r in records)` feeds a **generator expression** straight in so no intermediate list is built; and `defaultdict(list)` drops the `setdefault` you needed in 5.2. Every piece is something you built by hand earlier this week — the `collections` versions just say it more directly.

## In Practice

A decision guide for which tool this topic gives you:

1. **Need to drive iteration manually** (peek one value at a time, process a stream)? Use `iter()`/`next()` directly, and remember the iterator is one-shot.
2. **Producing a sequence lazily, or streaming large/infinite data?** Write a generator with `yield`, or a generator expression `(... for ... in ...)`, so you never build the whole thing in memory.
3. **Task is "how many times does each thing occur?"** Use `Counter(iterable)`, then `most_common(n)` to rank.
4. **Task is "group items under a key," or "count with custom logic"?** Use `defaultdict(list)` for grouping, `defaultdict(int)` for counting.
5. **Modelling a fixed record with named fields that should not change?** Use `namedtuple`.

Where these show up in working code:

- **Frequency analysis with `Counter`** — word frequencies, most-visited pages, top error codes: all are `Counter(items).most_common(n)`, the default reach for "which happened most often?"
- **Grouping with `defaultdict(list)`** — students by grade, orders by customer, files by extension: append in a loop, markedly cleaner than the `setdefault` version from 5.2.
- **Lazy streaming with generators** — reading a huge file line by line, paging through an API, chaining transformations: hold one item at a time so pipelines stay memory-safe on inputs too big for RAM.
- **Readable records with `namedtuple`** — bundled return values (`return Result(ok, message, code)`), CSV rows, config records: callers write `result.code` instead of decoding `result[2]`.

A few guardrails:

- **Remember an iterator is one-shot** — to iterate twice, loop the underlying iterable each time, or materialize it once with `list(it)`.
- **Do not treat a `Counter`/`defaultdict` as special** — both *are* dictionaries; everything from 5.2 still applies.
- **Items counted by `Counter` and keys in a `defaultdict` must be hashable** — same rule as set elements (5.1) and dict keys (5.2).

For going further, the standard library's **`itertools`** module builds on this iterator protocol to compose iterators (chaining, grouping, windowing) — useful once you are comfortable here, but beyond this topic's scope.

## Key Takeaways

- An **iterable** is anything you can loop over (`__iter__`); an **iterator** produces items one at a time (`__next__`). `iter(obj)` gets an iterator; `next(it)` advances it and raises **`StopIteration`** when exhausted.
- A **`for` loop is just this protocol**: it calls `iter()` once, then `next()` repeatedly, stopping silently on `StopIteration` — which is why every iterable loops uniformly. An **iterator is one-shot**; the underlying iterable is reusable.
- A **generator** — a function using `yield` (like `count_up_to`), or a `(... for ...)` expression — is a lazy iterator that streams values without building them all in memory, ideal for large or infinite sequences.
- **`Counter(iterable)`** counts hashable items in one line and ranks them with **`most_common(n)`** — the dedicated replacement for the `get(w, 0) + 1` loop from 5.2.
- **`defaultdict(factory)`** auto-initializes missing keys: `defaultdict(list)` for grouping (replacing `setdefault(k, []).append`) and `defaultdict(int)` for counting.
- **`namedtuple`** gives a tuple named, self-documenting fields (`p.x`) while staying immutable — the readable upgrade to the bare tuples of 4.2.

## References

1. Real Python — *Iterators and Iterables in Python*. https://realpython.com/python-iterators-iterables/
2. Real Python — *How to Use Generators and yield in Python*. https://realpython.com/introduction-to-python-generators/
3. Real Python — *Python's collections: A Buffet of Specialized Data Types*. https://realpython.com/python-collections-module/

---

<sub>[&#8592; Previous: 5.2 Dictionaries](../../../../../../../content/ai_native_engineering_foundations/p3-data-structures/week-5/1-data-structures-2/5-2-dictionaries/artifacts/reading.md)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Go back to TOC](../../../../../../../README.md)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Next: 6.1 Object-Oriented Foundations &#8594;](../../../../../../../content/ai_native_engineering_foundations/p4-classes-objects/week-6/1-classes-objects/6-1-object-oriented-foundations/artifacts/reading.md)</sub>