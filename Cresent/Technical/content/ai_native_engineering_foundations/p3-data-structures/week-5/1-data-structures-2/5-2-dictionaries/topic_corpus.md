---
topic_id: 5.2
title: Dictionaries
position_in_module: 2
generated_at: 2026-07-14T00:00:00Z
resource_count: 3
---

# 1. Dictionaries — Topic Corpus

## 2. Prerequisites

- **5.1 Sets** — unordered collection of unique, hashable elements; the fact that `{}` is an **empty dictionary, not an empty set**; membership as a fast hash-based lookup; comprehension syntax with curly braces.
- **4.1 Lists** — indexing, iteration with `for`, `in` membership, and list comprehension.
- **4.2 Tuples** — immutability, and the idea that a fixed tuple is a hashable value.
- P1/P2 (assumed): `int`/`str`/`bool`, operators, `print()`, f-strings, `for` loops, conditionals, and functions.

## 3. Learning Objectives

By the end of this topic you should be able to:

- **Create** a dictionary of key-value pairs and **access** a value by its key, and explain why keys must be unique and hashable while values can be anything.
- **Add, modify, and delete** entries with assignment (`d[k] = v`), `del d[k]`, and `d.pop(k)`, and describe what each does when the key is missing.
- **Loop** over a dictionary's keys, values, and pairs using `keys()`, `values()`, and `items()`.
- **Sort** a dictionary's contents by key and by value using `sorted()` with a key function.
- **Read and build nested dictionaries** — dictionaries whose values are themselves dictionaries — and access a value two levels deep.
- **Use** `get()` and `setdefault()` to read or initialize a key safely without triggering a `KeyError`.
- **Write** a dictionary comprehension to build a dictionary from an iterable, and to **invert** an existing dictionary (swap keys and values).

## 4. Introduction

In 5.1 you learned a trap: `{}` is not an empty set — it is an empty **dictionary**. This topic is the payoff of that trap. A dictionary is the structure those curly braces were really built for.

Lists and sets answer "which items do I have?" A dictionary answers a different, extremely common question: "given *this*, what is the *corresponding* thing?" Given a username, what is their email? Given a country code, what is the country name? Given a word, how many times did it appear? Every one of these is a **lookup** — you hold a key and you want the value attached to it. You *could* do this with two parallel lists (one of usernames, one of emails, matched up by position), but that is fragile and slow. A dictionary stores the pairing directly: each **key** points straight at its **value**.

This matters right now. **Assessment A2 — the Data Structures Portfolio — is due this week**, and it asks you to *choose the right structure for a task*. The dictionary is the single most-reached-for structure in real Python, because so much real data is naturally a set of labelled values: a user record, a config file, a JSON payload from an API, a count of how often each thing occurred. Knowing when a problem is really a lookup — and reaching for a dictionary instead of hand-matched lists — is exactly the judgment A2 rewards.

## 5. Core Concepts

### 5.1 What a dictionary is

A **dictionary** (type `dict`) is a **mutable mapping of unique keys to values** [1]. "Mapping" is the key word: it maps each key to exactly one value, like a real-world dictionary maps each word to its definition, or a phone book maps each name to a number [1]. Four properties define it:

- **Key-value pairs.** Every entry is a pair: a **key** and the **value** it points to. You look things up *by key*, never by position [1].
- **Keys are unique.** A dictionary cannot hold the same key twice. Assigning to an existing key overwrites its value rather than adding a second entry — the same uniqueness idea you saw with set elements in 5.1 [1].
- **Keys must be hashable (immutable).** Strings, numbers, and the tuples from 4.2 make valid keys; a list does not, because lists can change. This is the same hashability requirement that set *elements* had in 5.1 — for the same reason (§5.9 of that topic): the key's hash is used to find the value fast, so it must never change [1].
- **Values can be anything.** Unlike keys, values carry no restriction. A value can be a number, a string, a list, or even another dictionary (§5.7). Values also need not be unique — two different keys may point to the same value [1].

A dictionary is written with curly braces, with a colon between each key and its value, and commas between pairs:

```python
capitals = {"France": "Paris", "Japan": "Tokyo", "Egypt": "Cairo"}
```

Read that as three mappings: `"France"` maps to `"Paris"`, and so on. The keys here are all strings, but they need not be — `{1: "one", 2: "two"}` uses integer keys, and mixed key types are legal too.

It helps to place a dictionary next to the structures you already know:

| | List (4.1) | Set (5.1) | Dict (here) |
|---|---|---|---|
| Access by | position `[i]` | (membership only) | **key `[k]`** |
| Stores | values | unique values | **key → value pairs** |
| Duplicates allowed | yes | no | no duplicate **keys** |
| Ordered | yes | no | **yes (insertion order)** |
| Written with | `[ ]` | `{ }` / `set()` | `{key: value}` / `{}` |

Two rows deserve a note. First, a dictionary **is ordered**: since Python 3.7 it remembers the order in which you inserted keys, and looping visits them in that order [1]. (This is a genuine difference from the set you just learned, which is unordered.) Second, the "written with" row is the resolution of the 5.1 trap: `{}` is an empty dict, and `{key: value}` — pairs with colons — is a non-empty dict. To make an empty set you needed `set()`; to make an empty dict you just write `{}` or `dict()`.

### 5.2 Creating and accessing by key

There are three everyday ways to create a dictionary [1]:

```python
# 1. Braces with literal pairs
capitals = {"France": "Paris", "Japan": "Tokyo"}

# 2. The dict() constructor with keyword arguments (keys become strings)
person = dict(name="Ana", age=30)          # {"name": "Ana", "age": 30}

# 3. From a list of (key, value) pairs
pairs = [("a", 1), ("b", 2)]
d = dict(pairs)                            # {"a": 1, "b": 2}

# An empty dictionary, ready to fill later:
empty = {}                                 # NOT an empty set (see 5.1)
```

You **access a value by putting its key in square brackets** — the same brackets you used for list *indexing* in 4.1, except the "index" is now a key instead of a position [1]:

```python
capitals = {"France": "Paris", "Japan": "Tokyo"}
print(capitals["France"])      # Paris
print(capitals["Japan"])       # Tokyo
```

The one thing to watch: **asking for a key that does not exist raises `KeyError`** and stops your program [1]:

```python
print(capitals["Spain"])       # KeyError: 'Spain'
```

This is the dictionary equivalent of an out-of-range list index. Because missing keys are so common in real data, Python gives you two safe ways to handle them — the `in` operator to check first, and the `get()` method to supply a fallback — both covered in §5.6. For now, remember the rule: **bracket access assumes the key is there; if you are not sure, do not use bare brackets.**

You can check for a key with `in`, exactly as you did with lists and sets in 4.1 and 5.1 — and note that `in` tests **keys, not values** [1]:

```python
print("France" in capitals)    # True  — France is a key
print("Paris" in capitals)     # False — Paris is a value, not a key
```

### 5.3 Adding, modifying, and deleting entries

A dictionary is **mutable**, so you can change its contents after creation. Three operations cover almost everything [1].

**Add or modify with assignment.** Assigning to a key does one of two things depending on whether the key already exists — and this is the single most important behaviour to internalize [1]:

```python
scores = {"ana": 10}
scores["ben"] = 8       # key "ben" is NEW -> ADDS the pair
scores["ana"] = 12      # key "ana" EXISTS -> OVERWRITES 10 with 12
print(scores)           # {"ana": 12, "ben": 8}
```

There is no separate "add" versus "update" syntax — `d[k] = v` is both. If `k` is new, the pair is added; if `k` is already present, its value is replaced. This is the uniqueness guarantee from §5.1 in action: a key can appear only once, so a second assignment can only overwrite.

**Delete with `del`.** The `del` statement removes a key and its value entirely [1]:

```python
del scores["ben"]       # removes the "ben" -> 8 pair
del scores["zoe"]       # KeyError — "zoe" is not a key
```

Like bracket *access*, `del` raises `KeyError` if the key is absent.

**Remove-and-return with `pop()`.** The `pop()` method deletes a key **and hands you back its value**, which `del` does not [1]:

```python
scores = {"ana": 12, "ben": 8}
taken = scores.pop("ben")     # taken == 8; "ben" now removed
```

`pop()` also raises `KeyError` on a missing key — *unless* you give it a default second argument, in which case it returns that default instead of raising [1]:

```python
missing = scores.pop("zoe", 0)   # "zoe" absent -> returns 0, no error
```

Reach for `del` when you only want the key gone; reach for `pop()` when you want the value on the way out (for example, removing an item from a to-do dictionary and doing something with it). The optional default on `pop()` is the safe form when you are not certain the key exists.

### 5.4 Looping through a dictionary

Because a dictionary holds pairs, there are three things you might want to iterate: the keys, the values, or both together. Python gives you a method for each [1].

**Looping directly over the dictionary gives its keys.** This is the default and the most common form:

```python
capitals = {"France": "Paris", "Japan": "Tokyo"}
for country in capitals:            # iterates the KEYS
    print(country, "->", capitals[country])
```

Writing `for k in d` is identical to `for k in d.keys()` — the keys are what you get by default [1]. The loop visits keys in insertion order (§5.1).

**`keys()`, `values()`, `items()`** make the intent explicit and give you the piece you want [1]:

```python
for country in capitals.keys():     # just the keys
    print(country)

for city in capitals.values():      # just the values
    print(city)

for country, city in capitals.items():   # both, as (key, value) pairs
    print(country, "is capital-partnered with", city)
```

`items()` is the workhorse. It yields each pair as a two-element `(key, value)` tuple, which you **unpack** into two loop variables — the same tuple unpacking you saw in 4.2. When you need both the key and its value inside the loop (which is most of the time), `for k, v in d.items()` is cleaner than looping the keys and re-looking-up each value with `d[k]` [1].

One note: `keys()`, `values()`, and `items()` return **view objects**, not lists. A view stays connected to the dictionary — if the dictionary changes, the view reflects it — and you can loop over it or wrap it in `list()` if you need an actual list [1]. For everyday looping the distinction rarely matters; just know that `list(d.keys())` gives you a plain list of keys when you want one.

### 5.5 Sorting a dictionary — by key and by value

A dictionary keeps insertion order, but often you want the entries in *sorted* order — alphabetical by key, or ranked by value. The tool is the built-in `sorted()` you can already use on lists, applied thoughtfully [1].

**Sort by key.** Passing a dictionary straight to `sorted()` sorts its **keys** (because iterating a dict yields keys, §5.4), returning a sorted **list of keys** [1]:

```python
scores = {"ben": 8, "ana": 12, "cara": 10}
for name in sorted(scores):              # keys in alphabetical order
    print(name, scores[name])            # ana 12 / ben 8 / cara 10
```

`sorted()` returns a new list and does **not** change the dictionary itself — the dictionary keeps its original insertion order; you have simply chosen an order to *visit* it in.

**Sort by value.** To rank entries by their value, sort the **pairs** from `items()` and tell `sorted()` to use the value (the second element of each pair) as the sort key. You do that with the `key=` argument and a small `lambda` — a one-line anonymous function [1]:

```python
scores = {"ben": 8, "ana": 12, "cara": 10}

by_value = sorted(scores.items(), key=lambda kv: kv[1])
# [('ben', 8), ('cara', 10), ('ana', 12)]  — pairs, low to high value
```

Read `key=lambda kv: kv[1]` as: "for each pair `kv`, sort using `kv[1]`, the value." To rank highest-first, add `reverse=True`:

```python
top = sorted(scores.items(), key=lambda kv: kv[1], reverse=True)
# [('ana', 12), ('cara', 10), ('ben', 8)]
```

The result is a list of pairs, which you can loop over directly (`for name, score in top:`) or feed back into `dict(...)` to build a new, value-ordered dictionary — dictionaries preserve the order you insert in, so `dict(top)` is a dictionary sorted by value. To sort by key but get pairs back, use `key=lambda kv: kv[0]` (the first element). The pattern is always the same: sort `items()`, choose element `[0]` for by-key or `[1]` for by-value.

### 5.6 Safe access: `get()` and `setdefault()`

§5.2 warned that bracket access raises `KeyError` on a missing key. Two methods let you read or initialize a key **without** that risk [1].

**`get(key, default)` — read with a fallback.** `get()` returns the value if the key exists, and otherwise returns a default instead of raising. With no default supplied it returns `None` [1]:

```python
capitals = {"France": "Paris"}
print(capitals.get("France"))          # Paris
print(capitals.get("Spain"))           # None    — absent, no error
print(capitals.get("Spain", "unknown"))# unknown  — supplied default
```

Crucially, `get()` **does not modify the dictionary** — a missing key stays missing; you just get a fallback value back. Use `get()` whenever a key might be absent and you have a sensible default, instead of writing `if k in d: ... else: ...`.

**`setdefault(key, default)` — read, or insert then read.** `setdefault()` is `get()`'s active sibling. If the key exists, it returns the existing value (and changes nothing). If the key is **absent**, it *inserts* the key with the given default **and** returns that default [1]:

```python
prefs = {"theme": "dark"}
prefs.setdefault("theme", "light")    # exists -> returns "dark", no change
prefs.setdefault("font", "sans")      # absent -> inserts, returns "sans"
print(prefs)     # {"theme": "dark", "font": "sans"}
```

The difference between the two is exactly whether the dictionary is left alone: `get()` reads only; `setdefault()` reads *and* creates the key when it was missing. `setdefault()` shines when you are building up a dictionary whose values are containers — for example, grouping items into lists under a key:

```python
by_first_letter = {}
for name in ["ana", "ben", "amy"]:
    by_first_letter.setdefault(name[0], []).append(name)
# {"a": ["ana", "amy"], "b": ["ben"]}
```

On the first `"a"`, `setdefault` inserts `"a": []` and returns that new empty list to `.append` onto; on the second `"a"`, it returns the *existing* list. This "get-or-create the container" move is a workhorse pattern. (There is a dedicated tool that makes this grouping even smoother, which you will meet later this week — for now, `setdefault` does the job.)

### 5.7 Nested dictionaries

Because a dictionary's values can be anything (§5.1), a value can itself be a dictionary. A **nested dictionary** is a dictionary whose values are dictionaries — the natural way to model records that have their own fields [3]. This is how JSON from an API, a config file, or a database row typically arrives.

```python
users = {
    "u1": {"name": "Ana", "age": 30, "city": "Paris"},
    "u2": {"name": "Ben", "age": 25, "city": "Tokyo"},
}
```

Here the outer dictionary maps a user id to a value that is *itself* a dictionary of that user's fields. To reach a value two levels deep, **chain the bracket lookups** — the first bracket selects the inner dictionary, the second selects a field within it [3]:

```python
print(users["u1"]["name"])     # Ana
print(users["u2"]["city"])     # Tokyo
```

Read `users["u1"]["name"]` left to right: `users["u1"]` gives you Ana's whole record (the inner dict), and `["name"]` then pulls the name out of it. Assignment works the same way, and you can add or change nested fields in place [3]:

```python
users["u1"]["age"] = 31              # modify a nested field
users["u3"] = {"name": "Cara"}       # add a whole new nested record
users["u3"]["city"] = "Cairo"        # then add a field to it
```

Looping combines with §5.4 naturally — loop the outer dictionary, then work with each inner one:

```python
for uid, record in users.items():
    print(uid, "->", record["name"], "in", record.get("city", "?"))
```

Note the `.get("city", "?")`: nested records often have *missing* fields, so `get()` (§5.6) is especially valuable one level down, where a bare `record["city"]` would raise `KeyError` for any record lacking that field [3]. The same safe-access discipline you learned for flat dictionaries matters even more once data is nested.

### 5.8 Dictionary comprehension — building and inverting

You already write set comprehensions from 5.1 (`{x for x in nums}`) and list comprehensions from 4.1. A **dictionary comprehension** is the same idea, with one addition: because a dictionary needs a key *and* a value, you write `key: value` (with a colon) before the `for` clause [2]. The braces are the same; the colon is what makes it a dict rather than a set comprehension.

**Building a dictionary from an iterable** — the core use. Suppose you want each number mapped to its square [2]:

```python
squares = {n: n * n for n in range(1, 5)}
# {1: 1, 2: 4, 3: 9, 4: 16}
```

Read it as: "for each `n`, make a pair whose key is `n` and whose value is `n * n`." As with the comprehensions you already know, you can add an `if` filter to keep only some pairs [2]:

```python
evens = {n: n * n for n in range(1, 7) if n % 2 == 0}
# {2: 4, 4: 16, 6: 36}
```

A very common source is `items()` — transforming an existing dictionary into a new one. For example, applying a discount to every price [2]:

```python
prices = {"pen": 2.0, "book": 10.0}
sale = {item: price * 0.9 for item, price in prices.items()}
# {"pen": 1.8, "book": 9.0}
```

**Inverting a dictionary** — the signature two-liner that dictionary comprehensions make trivial. To swap keys and values (so you can look up in the opposite direction), loop `items()` and put the value where the key was and vice versa [2]:

```python
country_code = {"France": "FR", "Japan": "JP"}
code_country = {code: country for country, code in country_code.items()}
# {"FR": "France", "JP": "Japan"}
```

Now `code_country["FR"]` gives `"France"` — you have reversed the direction of lookup. One caution the comprehension cannot fix: inverting only works cleanly when the **original values are unique**. If two keys shared a value, they would both try to become the same key in the inverted dictionary, and — by the uniqueness rule from §5.1 — the later one silently overwrites the earlier one, so you lose an entry. Invert only when values are distinct, or accept that duplicates collapse [2].

## 6. Implementation

A practical decision procedure for whether a dictionary is the right structure, and which access method to use:

1. **Is the task a lookup — "given X, what is the corresponding Y?"** If yes, that is a dictionary: X is the key, Y is the value. If you find yourself keeping two parallel lists matched by position, collapse them into one dictionary.
2. **Might the key be missing when you read it?** Use `get()` (with a default) instead of bare brackets to avoid `KeyError`. Use `setdefault()` if you also want to *create* the key when it is absent.
3. **Do you need both key and value in a loop?** Use `for k, v in d.items()`. Just keys: `for k in d`. Just values: `for v in d.values()`.
4. **Do you need the entries in order?** They are already in insertion order; for alphabetical or ranked order, `sorted(d)` (by key) or `sorted(d.items(), key=lambda kv: kv[1])` (by value).
5. **Do records have their own fields?** Nest a dictionary as the value, and access with chained brackets `d[outer][inner]`.

A worked micro-example — count how many times each word appears in a list, then report the words ranked most-frequent-first:

```python
words = ["red", "blue", "red", "green", "red", "blue"]

counts = {}
for w in words:
    counts[w] = counts.get(w, 0) + 1     # get-or-0, then add one
# counts == {"red": 3, "blue": 2, "green": 1}

ranked = sorted(counts.items(), key=lambda kv: kv[1], reverse=True)
# [("red", 3), ("blue", 2), ("green", 1)]
```

Two ideas combine here. `counts.get(w, 0) + 1` (§5.6) reads the current count or 0 if the word is new, adds one, and stores it back with assignment (§5.3) — so the first sighting of a word initializes it and every later one increments it. Then `sorted(..., key=lambda kv: kv[1], reverse=True)` (§5.5) ranks by value. This word-count-then-rank shape is one of the most common in all of data work, and it is pure dictionary. (Python has a dedicated counting tool that shortens the counting half of this — you will meet it later this week; the `get`-based version above is the from-scratch equivalent.)

## 7. Real-World Patterns

Dictionaries are the most-used non-trivial structure in real Python, almost always for one of these jobs — each a direct answer to the A2 question "which structure fits this task?"

- **Records and configuration.** A single "thing with named fields" — a user, a product, a settings block — is a dictionary: `{"name": ..., "email": ..., "active": True}`. Collections of such things become a dictionary of dictionaries keyed by id (§5.7). This is exactly the shape of JSON, so any data pulled from a web API or read from a config file lands in your program as nested dictionaries and lists. Reaching for a dict here — rather than positional lists — is the A2-style call: the data has *labels*, so the structure is keyed.

- **Lookup tables.** Any "translate this into that" mapping is a dictionary: country code to country name, product id to price, HTTP status code to message, username to permissions. Instead of a chain of `if`/`elif`, you store the mapping once and look it up: `MESSAGES.get(code, "unknown")`. The `get()` fallback (§5.6) handles inputs you did not anticipate without crashing.

- **Counting and grouping.** "How many times did each thing occur?" is a dictionary from thing to count, built with the `get(x, 0) + 1` pattern from §6. "Group these items by some attribute" is a dictionary from attribute to a list of items, built with the `setdefault(key, []).append(item)` pattern from §6. Both are everywhere in analytics, log processing, and reporting — and both are natural dictionary work. (A dedicated tool later this week streamlines both; the dictionary versions here are the foundation it builds on.)

- **Reverse lookups by inverting.** When you have a name-to-id map but suddenly need id-to-name, you invert it with a one-line dictionary comprehension (§5.8) rather than maintaining two hand-synced dictionaries — as long as the values were unique.

## 8. Best Practices

- **When a task is "given X, get Y," use a dictionary.** Two parallel lists matched by position is the anti-pattern a dictionary replaces.
- **Use `get()` (with a default) instead of bare brackets when a key might be missing.** Bare `d[k]` is for keys you are certain exist; otherwise you invite `KeyError`.
- **Use `setdefault()` to get-or-create a container value**, e.g. `d.setdefault(k, []).append(x)` for grouping. It reads and initializes in one step.
- **Loop with `items()` when you need both key and value** — it is clearer and avoids re-looking-up `d[k]` inside the loop.
- **Remember `in` tests keys, not values.** `"Paris" in capitals` is `False` even when Paris is a value.
- **`sorted(d)` gives sorted keys and does not change the dict.** Sorting is a way to *visit* the dictionary in order, not to reorder it in place.
- **Invert a dictionary only when its values are unique** — duplicate values collapse to a single key and silently lose entries.
- **Do not use a mutable object (like a list) as a key.** Keys must be hashable; use a string, number, or tuple (4.2).
- **Use `{}` for an empty dict and `set()` for an empty set** — the 5.1 trap, stated as a habit.

## 9. Hands-On Exercise

Given a list of student records, each a small dictionary like `{"name": "Ana", "score": 88, "city": "Paris"}`:

1. Build one nested dictionary keyed by name, so `students["Ana"]` returns Ana's record (§5.7).
2. Use `get()` to print each student's `city`, falling back to `"unknown"` when the field is absent (§5.6).
3. Produce a list of `(name, score)` pairs sorted by score, highest first, with `sorted(..., key=lambda kv: kv[1], reverse=True)` (§5.5).
4. Build a `grade -> [names]` grouping with `setdefault` (§5.6), then **invert** a simple `name -> grade` dictionary into `grade -> name` with a comprehension and note what happens when two students share a grade (§5.8).

This maps directly to the "choose and manipulate the right structure" judgment the A2 portfolio rewards.

## 10. Key Takeaways

- A dictionary is a **mutable, insertion-ordered mapping of unique, hashable keys to arbitrary values**; you access a value **by key** with `d[k]`, and a missing key raises `KeyError`.
- Assignment `d[k] = v` **adds** a new key or **overwrites** an existing one; `del d[k]` removes a key; `d.pop(k[, default])` removes it **and returns its value**.
- Loop with **`keys()`, `values()`, or `items()`** — and use `for k, v in d.items()` whenever you need both the key and its value.
- **Sort keys with `sorted(d)`** and sort by value with **`sorted(d.items(), key=lambda kv: kv[1])`**; sorting produces a new list and leaves the dictionary's own order intact.
- **`get(k, default)`** reads safely without raising and without changing the dict; **`setdefault(k, default)`** returns the existing value or inserts the default — ideal for get-or-create-a-container patterns.
- A **nested dictionary** stores dictionaries as values (the shape of JSON and records); reach two levels deep with chained brackets `d[outer][inner]`.
- A **dictionary comprehension** `{k: v for ...}` builds a dict from an iterable, and `{v: k for k, v in d.items()}` **inverts** one — cleanly only when the original values are unique.

## 11. Next Steps

_System-derived from the next entry in curriculum/sequence.md._
