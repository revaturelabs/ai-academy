---
topic_id: 7.2
title: Errors & Exceptions
position_in_module: 2
generated_at: 2026-07-14T00:00:00Z
resource_count: 3
---

# 1. Errors & Exceptions — Topic Corpus

## 2. Prerequisites

- **7.1 File Handling** — you have opened files with `open()` and the `with` statement, and read CSV and JSON. We deliberately deferred one question there: what happens when the file you ask for does not exist? That missing-file error is where this topic begins.
- **6.1–6.3 Classes, Objects & Inheritance** — an exception is a class, and a *custom* exception is just a class that inherits from `Exception`. You already know how `class Child(Parent):` works, so the custom-exception example will feel familiar.
- **5.2 Dictionaries (`get()`, key lookups)** — you saw that looking up a missing key raises a `KeyError`; here we name that error and learn to catch it.
- **1.1–3.3 Python foundations** — you can read functions, loops, and `import` statements, all of which appear in the examples.

## 3. Learning Objectives

After this topic you should be able to:

- Distinguish a **syntax error** from an **exception**, and describe how built-in exceptions are organized into a class hierarchy.
- Write a `try` / `except` block to catch an exception and keep a program from crashing.
- Use `else` and `finally` clauses to separate the "it worked" path from guaranteed cleanup.
- Handle several different error types with multiple `except` blocks or a grouped `except (A, B):`.
- Recognize the common built-in exceptions — `FileNotFoundError`, `ValueError`, `KeyError`, `IndexError`, `ZeroDivisionError`, `TypeError`, `AttributeError` — and what triggers each.
- Signal an error yourself with `raise`, and define a small custom exception by subclassing `Exception`.

## 4. Introduction

In the last topic you wrote `with open("sales.csv") as f:` and everything worked — *because the file was there*. But what happens the day someone deletes `sales.csv`, or types the wrong filename? Try it, and Python stops the program cold with a red message ending in `FileNotFoundError`. That is the thread we promised to pick up: the real world is full of missing files, bad input, and empty lists, and a program that crashes on the first surprise is not a program you can ship.

There are two very different kinds of "something went wrong." One is a **syntax error** — you wrote code Python cannot even read, like a missing colon. Those are caught before the program runs, and you fix them by editing the code. The other is an **exception** — the code is valid and runs, but at some moment an operation cannot be completed: a file is missing, a number cannot be divided by zero, a list index is out of range [1]. Exceptions happen *while the program is running*, often because of data or conditions you did not control.

This topic is about that second kind: what exceptions are, how Python organizes them, and — most importantly — how to *handle* them so your program can respond gracefully instead of crashing [1][3]. The mechanics you learn here are exactly what the next topic (7.3, the Robust File Reader case study) puts to work end-to-end.

## 5. Core Concepts

### <u>**Errors vs exceptions.**</u>

A **syntax error** (also called a parsing error) means Python could not understand your code at all — a missing parenthesis, a misspelled keyword, a colon left off an `if`. Python reports these *before running a single line* and points at the spot with a little `^` arrow [1]. You fix them by correcting the source.

An **exception** is different: the code is syntactically valid and Python starts executing it, but partway through, a statement asks for something impossible — reading a file that isn't there, converting the word `"cat"` to an integer, indexing past the end of a list [1]. When that happens, Python **raises** an exception. If nothing catches it, the program stops and prints a **traceback**: the chain of calls that led to the error, ending with the exception's type and message.

The key insight: syntax errors are bugs you fix at write-time; exceptions are runtime events you *plan for and handle*. This whole topic is about the second.

### <u>**The exception hierarchy.**</u>

Every exception in Python is an **object**, and every exception type is a **class** [2]. Those classes are arranged in an inheritance tree, just like the classes you built in topics 6.1–6.3. At the top sits `BaseException`; almost everything you care about inherits from its child `Exception` [2].

A simplified slice of the tree:

```
BaseException
 └── Exception
      ├── ArithmeticError
      │    └── ZeroDivisionError
      ├── LookupError
      │    ├── IndexError
      │    └── KeyError
      ├── OSError
      │    └── FileNotFoundError
      ├── ValueError
      ├── TypeError
      └── AttributeError
```

Why does the tree matter? Because catching a **parent** class also catches all its **children**. If you write `except LookupError:`, you catch both `IndexError` and `KeyError`, since both inherit from `LookupError` [2]. And `except Exception:` catches almost everything — which is powerful but usually *too* broad, because it hides bugs you'd rather see. The art is catching at the right level of the tree: specific enough to be meaningful, broad enough to cover the cases you truly expect.

### <u>**Handling exceptions: `try` / `except`.**</u>

The core tool is the **`try` / `except`** statement. You put the risky code in the `try` block; if an exception is raised there, Python jumps to a matching `except` block instead of crashing [1]:

```python
try:
    number = int(input("Enter a number: "))
    print("You entered", number)
except ValueError:
    print("That wasn't a valid number.")
```

If the user types `42`, the `try` block runs to the end and the `except` is skipped. If they type `hello`, `int()` raises a `ValueError`, Python skips the rest of the `try` and runs the `except ValueError:` block instead. Either way the program keeps running. This is the whole idea: **anticipate what can go wrong, and describe the response.**

You can also capture the exception object itself with `as` to inspect its message [1]:

```python
try:
    value = int("cat")
except ValueError as err:
    print("Could not convert:", err)   # Could not convert: invalid literal for int() with base 10: 'cat'
```

### <u>**Catching a missing file (the 7.1 thread).**</u>

Now we can answer the question left open in File Handling. Opening a file that does not exist raises `FileNotFoundError` [2]. Wrapping the `open()` in a `try` lets you respond instead of crashing:

```python
try:
    with open("sales.csv") as f:
        data = f.read()
except FileNotFoundError:
    print("sales.csv not found — did you export it yet?")
    data = ""
```

Notice `with` and `try` compose naturally: the `with` still closes the file properly, and the `try` catches the error that `open()` might raise. This tiny pattern is the seed of the robust reader you'll build next topic.

### <u>**`else` and `finally`.**</u>

A `try` statement has two more optional clauses [1]:

- **`else`** runs only if the `try` block finished with **no** exception. It's where you put "the work that should happen when everything went fine" — kept separate from the `try` so you aren't accidentally catching exceptions from the success path.
- **`finally`** runs **no matter what** — whether an exception happened, was caught, or wasn't. It's for cleanup that must always occur (closing a resource, releasing a lock).

```python
try:
    f = open("data.txt")
except FileNotFoundError:
    print("File missing.")
else:
    print("Opened successfully; reading now.")
    print(f.read())
    f.close()
finally:
    print("Done trying to read data.txt.")
```

Read it as a sentence: *try* this; if it fails this way, do the *except*; if it succeeded, also do the *else*; and in every case, *finally* do this last. (In practice `with` handles most file cleanup, so `finally` shines for resources that don't have a context manager.)

### <u>**Handling multiple exceptions.**</u>

Different failures often need different responses, so a single `try` can have several `except` blocks. Python checks them **top to bottom** and runs the **first** one that matches [1]:

```python
try:
    row = records[index]
    count = int(row["units"])
    average = total / count
except IndexError:
    print("No record at that position.")
except KeyError:
    print("That row has no 'units' column.")
except ValueError:
    print("'units' wasn't a number.")
except ZeroDivisionError:
    print("Can't divide by zero.")
```

Because matching stops at the first hit, order matters when the types are related: **put more specific exceptions before their parents**. If you wrote `except LookupError:` above `except KeyError:`, the `KeyError` block could never run, because `KeyError` is a `LookupError` and the broader block would catch it first [2].

When several error types deserve the **same** response, group them in a tuple with one `except` [1]:

```python
try:
    value = int(row[2])
except (IndexError, ValueError):
    value = 0   # missing column or non-numeric — treat as zero either way
```

### <u>**Common built-in exceptions.**</u>

You will meet these constantly [2]:

- **`FileNotFoundError`** — you tried to open a file that isn't there (a subclass of `OSError`).
- **`ValueError`** — a value has the right *type* but an unacceptable *content*, e.g. `int("cat")`.
- **`IOError`** — an input/output operation failed (a disk problem, a broken stream). In modern Python `IOError` is actually an alias for `OSError`, the same family `FileNotFoundError` belongs to [2].
- **`KeyError`** — you looked up a dictionary key that doesn't exist, e.g. `record["missing"]`. (Recall from 5.2 that `dict.get()` avoids this by returning `None` instead.)
- **`IndexError`** — you indexed a list or string past its end, e.g. `items[99]` on a 3-item list.
- **`ZeroDivisionError`** — you divided by zero, e.g. `total / 0`.
- **`TypeError`** — you used a value of the wrong *type* for an operation, e.g. `"3" + 5` (string plus int).
- **`AttributeError`** — you accessed an attribute or method an object doesn't have, e.g. calling `.append()` on an integer.

A useful pairing: `ValueError` is "right type, wrong value" while `TypeError` is "wrong type entirely." `int("cat")` is a `ValueError` (a string, just not a numeric one); `len(5)` is a `TypeError` (integers have no length).

### <u>**Raising exceptions: the `raise` statement.**</u>

You don't only *catch* exceptions — sometimes your own code should *signal* that something is wrong. The **`raise`** statement does that [1]:

```python
def set_age(age):
    if age < 0:
        raise ValueError("age cannot be negative")
    return age
```

Now `set_age(-3)` stops and raises a `ValueError` with your message, which a caller can catch with `try`/`except` just like a built-in one. Raising early — as soon as you detect bad data — is often better than letting a wrong value flow deeper into the program where the eventual crash is harder to trace.

### <u>**Custom exceptions (brief).**</u>

When none of the built-in types names your situation well, you can define your own. A **custom exception** is simply a class that inherits from `Exception` [1]:

```python
class InvalidRecordError(Exception):
    """Raised when a data record fails validation."""

def parse(record):
    if "units" not in record:
        raise InvalidRecordError("record is missing the 'units' field")
    return int(record["units"])
```

That's all it takes — the body can be just a docstring. Because `InvalidRecordError` inherits from `Exception`, it works with `try`/`except` exactly like the built-ins, and a caller can catch it by name: `except InvalidRecordError:`. Custom exceptions make error handling read like your problem domain rather than Python's generic vocabulary. (This is a light introduction; the outline keeps it brief on purpose.)

## 6. Implementation

A small, complete example that ties the pieces together: a function that safely reads a number from a file, using the missing-file thread from 7.1 plus multiple exceptions, `else`, and `finally`.

Step 1 — Define the function with layered handling:

```python
def read_count(path):
    try:
        with open(path) as f:
            text = f.read().strip()
        count = int(text)
    except FileNotFoundError:
        print(f"'{path}' not found; using 0.")
        return 0
    except ValueError:
        print(f"'{path}' did not contain a number; using 0.")
        return 0
    else:
        print("Read succeeded.")
        return count
    finally:
        print(f"Finished attempting to read '{path}'.")
```

Step 2 — Exercise all three paths:

```python
# (a) file exists and contains "42"
print(read_count("good.txt"))

# (b) file does not exist
print(read_count("missing.txt"))

# (c) file exists but contains "hello"
print(read_count("bad.txt"))
```

Expected output:

```
Read succeeded.
Finished attempting to read 'good.txt'.
42
'missing.txt' not found; using 0.
Finished attempting to read 'missing.txt'.
0
'bad.txt' did not contain a number; using 0.
Finished attempting to read 'bad.txt'.
0
```

Notice how `finally` prints in *every* case, `else` prints only on success, and each `except` produces its own tailored message. This layered shape is the skeleton of the robust file reader in the next topic.

## 7. Real-World Patterns

- **Guarding file and network I/O.** Any operation that touches the outside world — a file, a database, a web request — can fail for reasons your code didn't cause. Wrapping it in `try`/`except` and reacting (retry, default value, clear message) is the standard defensive pattern [1].
- **Validating input at the boundary.** Programs `raise` their own `ValueError` or a custom exception the moment bad data arrives (a negative age, a missing field), so failures surface where they're easy to diagnose rather than deep inside later code [1].
- **Cleanup with `finally`.** Long-running services release locks, close connections, or delete temp files in a `finally` block so the cleanup happens even when the main work throws [1].
- **Domain-specific error types.** Larger codebases define custom exceptions (like `InvalidRecordError`) so callers can catch *their* errors distinctly from unrelated built-in ones [1].

## 8. Best Practices

- **Catch specific exceptions, not bare `except:`.** A blanket `except:` (or even `except Exception:`) swallows bugs you'd want to see. Name the errors you actually expect [1][3].
- **Order `except` blocks specific-to-general.** Because the first match wins, put child classes before parent classes, or the parent will shadow them [2].
- **Keep the `try` block small.** Wrap only the line(s) that can fail, so you know exactly what you're catching and don't accidentally hide an error from unrelated code.
- **Use `else` for the success path.** Code that should run *only when no exception occurred* belongs in `else`, not tacked onto the end of `try`.
- **Prefer `get()` over catching `KeyError`** when a missing dictionary key is expected and has a sensible default (from 5.2) — handling isn't always the answer; sometimes prevention is cleaner.
- **`raise` early on bad data.** Validate inputs and raise a clear exception up front rather than letting a bad value cause a confusing crash later.

## 9. Hands-On Exercise

Write a function `safe_divide(a, b)` that returns `a / b`, but catches `ZeroDivisionError` and returns the string `"undefined"` instead, and catches `TypeError` (e.g. someone passes `"3"`) and returns `"bad input"`. Add a `finally` clause that prints `"division attempted"` every time. Call it with `(10, 2)`, `(10, 0)`, and `(10, "x")` and confirm each path behaves as expected.

## 10. Key Takeaways

- A **syntax error** is caught before the program runs; an **exception** is a runtime event (missing file, bad value, out-of-range index) that you can *handle* instead of crashing.
- Exceptions are classes in an inheritance tree, so catching a parent (`LookupError`) also catches its children (`IndexError`, `KeyError`) — order `except` blocks specific-to-general.
- `try`/`except` responds to errors; `else` runs only on success; `finally` always runs for cleanup; multiple `except` blocks (or a grouped `except (A, B):`) handle different failures.
- Know the common ones on sight: `FileNotFoundError`, `ValueError` (right type/wrong value), `TypeError` (wrong type), `KeyError`, `IndexError`, `ZeroDivisionError`, `AttributeError`.
- You can `raise` an exception yourself to signal bad data, and define a **custom exception** by subclassing `Exception` when the built-in names don't fit.

## 11. Next Steps

_System-derived from the next entry in curriculum/sequence.md._
