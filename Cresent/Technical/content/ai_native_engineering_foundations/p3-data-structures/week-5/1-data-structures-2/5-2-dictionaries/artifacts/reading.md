# Dictionaries

<sub>[&#8592; Previous: 5.1 Sets](../../../../../../../content/ai_native_engineering_foundations/p3-data-structures/week-5/1-data-structures-2/5-1-sets/artifacts/reading.md)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Go back to TOC](../../../../../../../README.md)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Next: 5.3 Iterators, Generators & Collections &#8594;](../../../../../../../content/ai_native_engineering_foundations/p3-data-structures/week-5/1-data-structures-2/5-3-iterators-generators-collections/artifacts/reading.md)</sub>

---

## Overview

In 5.1 you hit a trap: `{}` is not an empty set — it is an empty **dictionary**. This topic is the payoff. Lists and sets answer "which items do I have?" A dictionary answers a different, extremely common question: "given *this*, what is the *corresponding* thing?" Given a username, what is their email? Given a word, how many times did it appear? Each is a **lookup** — you hold a key and want the value attached to it. You could fake this with two parallel lists matched by position, but that is fragile and slow; a dictionary stores the pairing directly. It is the single most-reached-for structure in real Python, because so much real data is naturally a set of labelled values. _This contributes to A2 — Data Structures Portfolio (due W5), which rewards knowing when a problem is really a lookup and reaching for a dictionary instead of hand-matched lists._

## Key Concepts

**What a dictionary is.** A **dictionary** (type `dict`) is a **mutable mapping of unique keys to values** [1]. "Mapping" is the key word: it maps each key to exactly one value, like a real-world dictionary maps each word to its definition [1]. Four properties define it:

- **Key-value pairs.** Every entry is a pair — a key and the value it points to. You look things up *by key*, never by position [1].
- **Keys are unique.** A dictionary cannot hold the same key twice; assigning to an existing key overwrites its value rather than adding a second entry — the same uniqueness idea you saw with set elements in 5.1 [1].
- **Keys must be hashable (immutable).** Strings, numbers, and the tuples from 4.2 make valid keys; a list does not, because lists can change. This is the same hashability requirement set *elements* had in 5.1: the key's hash is used to find the value fast, so it must never change [1].
- **Values can be anything.** A value can be a number, a string, a list, or even another dictionary, and values need not be unique — two keys may point to the same value [1].

A dictionary is written with curly braces, a colon between each key and value, commas between pairs:

```python
capitals = {"France": "Paris", "Japan": "Tokyo", "Egypt": "Cairo"}
```

A dictionary **is ordered**: since Python 3.7 it remembers the order in which you inserted keys, and looping visits them in that order [1] — a genuine difference from the unordered set you just learned. And the "written with" row resolves the 5.1 trap: `{}` is an empty dict, `{key: value}` is a non-empty dict, and `set()` is how you make an empty set.

**Creating and accessing by key.** There are three everyday ways to create a dictionary [1]:

- Braces with literal pairs: `capitals = {"France": "Paris"}`
- The `dict()` constructor with keyword arguments (keys become strings): `dict(name="Ana", age=30)`
- From a list of `(key, value)` pairs: `dict([("a", 1), ("b", 2)])`

You **access a value by putting its key in square brackets** — the same brackets you used for list indexing in 4.1, except the "index" is now a key instead of a position [1]:

```python
print(capitals["France"])      # Paris
```

The one thing to watch: **asking for a key that does not exist raises `KeyError`** and stops your program — the dictionary equivalent of an out-of-range list index [1]. You can check for a key with `in`, exactly as with lists and sets, and note that `in` tests **keys, not values** [1]:

```python
print("France" in capitals)    # True  — France is a key
print("Paris" in capitals)     # False — Paris is a value, not a key
```

**Adding, modifying, and deleting entries.** A dictionary is mutable, so you can change its contents after creation. Three operations cover almost everything [1]:

- **Add or modify with assignment.** `d[k] = v` is both add and update: if `k` is new the pair is added; if `k` already exists its value is overwritten. There is no separate "add" versus "update" syntax — this is the uniqueness guarantee in action, since a key can appear only once.
- **Delete with `del`.** `del d[k]` removes a key and its value entirely. Like bracket access, it raises `KeyError` if the key is absent.
- **Remove-and-return with `pop()`.** `d.pop(k)` deletes a key *and hands you back its value*, which `del` does not. It also raises `KeyError` on a missing key — unless you give it a default second argument, in which case it returns that default instead of raising.

```python
scores = {"ana": 10}
scores["ben"] = 8              # NEW -> adds the pair
scores["ana"] = 12            # EXISTS -> overwrites 10 with 12
taken = scores.pop("ben")     # taken == 8; "ben" now removed
missing = scores.pop("zoe", 0)  # absent -> returns 0, no error
```

Reach for `del` when you only want the key gone; reach for `pop()` when you want the value on the way out. The optional default on `pop()` is the safe form when you are not certain the key exists.

**Looping through a dictionary.** Because a dictionary holds pairs, there are three things you might iterate — the keys, the values, or both together — and Python gives you a method for each [1]:

- **`keys()`** — just the keys. Looping directly over the dictionary (`for k in d`) is identical to `for k in d.keys()`; keys are what you get by default, visited in insertion order.
- **`values()`** — just the values.
- **`items()`** — both, as `(key, value)` tuples, which you **unpack** into two loop variables using the same tuple unpacking you saw in 4.2.

```python
for country, city in capitals.items():
    print(country, "->", city)
```

`items()` is the workhorse: when you need both the key and its value inside the loop, `for k, v in d.items()` is cleaner than looping the keys and re-looking-up each value with `d[k]` [1]. One note: these three methods return **view objects**, not lists — a view stays connected to the dictionary, and you can wrap it in `list()` when you need an actual list [1].

**Sorting a dictionary — by key and by value.** A dictionary keeps insertion order, but often you want it in *sorted* order. The tool is the built-in `sorted()` you already use on lists [1]. There are two moves:

- **Sort by key.** Passing a dictionary straight to `sorted()` sorts its keys (because iterating a dict yields keys), returning a sorted list of keys: `for name in sorted(scores):`. It returns a new list and does **not** change the dictionary.
- **Sort by value.** Sort the *pairs* from `items()` and tell `sorted()` to use the value with the `key=` argument and a small `lambda` — a one-line anonymous function [1].

```python
scores = {"ben": 8, "ana": 12, "cara": 10}
by_value = sorted(scores.items(), key=lambda kv: kv[1])
# [('ben', 8), ('cara', 10), ('ana', 12)]  — low to high value
top = sorted(scores.items(), key=lambda kv: kv[1], reverse=True)
# [('ana', 12), ('cara', 10), ('ben', 8)]  — reverse=True ranks high first
```

Read `key=lambda kv: kv[1]` as "for each pair `kv`, sort using `kv[1]`, the value." The pattern is always the same: sort `items()`, choose element `[0]` for by-key or `[1]` for by-value. The result is a list of pairs you can loop over or feed back into `dict(...)` to build a new, value-ordered dictionary.

**Safe access: `get()` and `setdefault()`.** Two methods let you read or initialize a key *without* risking a `KeyError` [1]:

- **get(key, default).** Returns the value if the key exists, otherwise returns a default (or `None` if none is supplied). Crucially, it **does not modify the dictionary** — a missing key stays missing. Use it whenever a key might be absent and you have a sensible fallback, instead of writing `if k in d: ... else: ...`.
- **setdefault(key, default).** `get()`'s active sibling. If the key exists it returns the existing value and changes nothing; if the key is **absent** it *inserts* the key with the default **and** returns that default.

```python
prefs = {"theme": "dark"}
prefs.setdefault("theme", "light")   # exists -> returns "dark", no change
prefs.setdefault("font", "sans")     # absent -> inserts, returns "sans"
```

The difference is exactly whether the dictionary is left alone: `get()` reads only; `setdefault()` reads *and* creates the key when it was missing. `setdefault()` shines when building a dictionary whose values are containers — `d.setdefault(k, []).append(x)` gets-or-creates a list, then appends to it, a workhorse grouping move. (There is a dedicated tool that makes this grouping even smoother, which you will meet later this week — for now, `setdefault` does the job.)

**Nested dictionaries.** Because a dictionary's values can be anything, a value can itself be a dictionary. A **nested dictionary** is a dictionary whose values are dictionaries — the natural way to model records that have their own fields, and the shape JSON from an API or a config file arrives in [3]:

```python
users = {
    "u1": {"name": "Ana", "age": 30, "city": "Paris"},
    "u2": {"name": "Ben", "age": 25, "city": "Tokyo"},
}
print(users["u1"]["name"])     # Ana
```

To reach a value two levels deep, **chain the bracket lookups**: the first bracket selects the inner dictionary, the second selects a field within it [3]. Read `users["u1"]["name"]` left to right — `users["u1"]` gives Ana's whole record, then `["name"]` pulls the name out. Nested records often have *missing* fields, so `get()` is especially valuable one level down, where a bare `record["city"]` would raise `KeyError` for any record lacking that field [3].

**Dictionary comprehension — building and inverting.** You already write set comprehensions from 5.1 and list comprehensions from 4.1. A **dictionary comprehension** is the same idea with one addition: because a dictionary needs a key *and* a value, you write `key: value` (with a colon) before the `for` clause [2]. The braces are the same; the colon is what makes it a dict rather than a set comprehension. Two uses matter most:

- **Building a dictionary from an iterable** — `{n: n * n for n in range(1, 5)}` maps each number to its square, and you can add an `if` filter to keep only some pairs [2].
- **Inverting a dictionary** — swapping keys and values so you can look up in the opposite direction: `{v: k for k, v in d.items()}` [2].

```python
country_code = {"France": "FR", "Japan": "JP"}
code_country = {code: country for country, code in country_code.items()}
# {"FR": "France", "JP": "Japan"}
```

One caution the comprehension cannot fix: inverting only works cleanly when the **original values are unique**. If two keys shared a value, they would both try to become the same key in the inverted dictionary, and by the uniqueness rule the later one silently overwrites the earlier — you lose an entry [2].

## Worked Example

Count how many times each word appears in a list, then rank the words most-frequent-first:

```python
words = ["red", "blue", "red", "green", "red", "blue"]

counts = {}
for w in words:
    counts[w] = counts.get(w, 0) + 1     # get-or-0, then add one
# counts == {"red": 3, "blue": 2, "green": 1}

ranked = sorted(counts.items(), key=lambda kv: kv[1], reverse=True)
# [("red", 3), ("blue", 2), ("green", 1)]
```

Two ideas combine here. `counts.get(w, 0) + 1` reads the current count — or `0` if the word is new — adds one, and stores it back with assignment, so the first sighting of a word initializes it and every later one increments it. Then `sorted(..., key=lambda kv: kv[1], reverse=True)` ranks by value, highest first. This word-count-then-rank shape is one of the most common in all of data work, and it is pure dictionary. (Python has a dedicated counting tool that shortens the counting half of this — you will meet it later this week; the `get`-based version above is the from-scratch equivalent.)

## In Practice

Dictionaries are the most-used non-trivial structure in real Python, almost always for one of these jobs — each a direct answer to the A2 question "which structure fits this task?":

- **Records and configuration.** A single "thing with named fields" — a user, a product, a settings block — is a dictionary; collections of them become a dictionary of dictionaries keyed by id. This is the shape of JSON, so any data from a web API or config file lands as nested dictionaries.
- **Lookup tables.** Any "translate this into that" mapping — country code to name, status code to message, username to permissions — is a dictionary. Instead of a chain of `if`/`elif`, store the mapping once and look it up, with `get()` supplying a fallback for inputs you did not anticipate.
- **Counting and grouping.** "How many times did each thing occur?" uses the `get(x, 0) + 1` pattern; "group these items by attribute" uses `setdefault(key, []).append(item)`. Both are everywhere in analytics and log processing.
- **Reverse lookups by inverting.** When a name-to-id map suddenly needs id-to-name, invert it with a one-line comprehension rather than maintaining two hand-synced dictionaries — as long as the values were unique.

Do / don't habits worth keeping:

- **Do** use `get()` (with a default) instead of bare brackets when a key might be missing; bare `d[k]` is for keys you are certain exist.
- **Do** loop with `items()` when you need both key and value.
- **Don't** use a mutable object like a list as a key — keys must be hashable, so use a string, number, or tuple (4.2).
- **Don't** forget `{}` is an empty dict and `set()` is an empty set — the 5.1 trap, stated as a habit.

## Key Takeaways

- A dictionary is a **mutable, insertion-ordered mapping of unique, hashable keys to arbitrary values**; you access a value **by key** with `d[k]`, and a missing key raises `KeyError`.
- Assignment `d[k] = v` **adds** a new key or **overwrites** an existing one; `del d[k]` removes a key; `d.pop(k[, default])` removes it **and returns its value**.
- Loop with **`keys()`, `values()`, or `items()`** — and use `for k, v in d.items()` whenever you need both the key and its value.
- **Sort keys with `sorted(d)`** and by value with **`sorted(d.items(), key=lambda kv: kv[1])`**; sorting produces a new list and leaves the dictionary's own order intact.
- **`get(k, default)`** reads safely without raising or changing the dict; **`setdefault(k, default)`** returns the existing value or inserts the default — ideal for get-or-create-a-container patterns.
- A **nested dictionary** stores dictionaries as values (the shape of JSON); reach two levels deep with chained brackets `d[outer][inner]`. A **dictionary comprehension** `{k: v for ...}` builds a dict and `{v: k for k, v in d.items()}` **inverts** one — cleanly only when the original values are unique.

## References

1. Real Python — *Dictionaries in Python*. https://realpython.com/python-dicts/
2. Real Python — *Python Dictionary Comprehensions*. https://realpython.com/python-dictionary-comprehension/
3. W3Schools — *Python Nested Dictionaries*. https://www.w3schools.com/python/python_dictionaries_nested.asp

---

<sub>[&#8592; Previous: 5.1 Sets](../../../../../../../content/ai_native_engineering_foundations/p3-data-structures/week-5/1-data-structures-2/5-1-sets/artifacts/reading.md)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Go back to TOC](../../../../../../../README.md)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Next: 5.3 Iterators, Generators & Collections &#8594;](../../../../../../../content/ai_native_engineering_foundations/p3-data-structures/week-5/1-data-structures-2/5-3-iterators-generators-collections/artifacts/reading.md)</sub>
