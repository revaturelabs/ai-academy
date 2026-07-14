---
topic_id: 7.3
title: "Case Study: Building a Robust File Reader"
position_in_module: 3
generated_at: 2026-07-14T00:00:00Z
resource_count: 3
---

# 1. Case Study: Building a Robust File Reader — Topic Corpus

## 2. Prerequisites

- **7.1 File Handling** — you can `open()` a file inside a `with` block and read a CSV with the `csv` module (using `newline=""`), including `csv.reader` (rows as lists) and `csv.DictReader` (rows as dictionaries keyed by the header). This case study reads and writes CSVs exactly that way.
- **7.2 Errors & Exceptions** — you can write `try`/`except`, catch `FileNotFoundError`, `ValueError`, and `KeyError`, order `except` blocks specific-to-general, and `raise` your own error. The robust reader is precisely where per-row `try`/`except` gets applied for real.
- **5.2 Dictionaries** — each CSV row becomes a `dict`; you look values up by column name and use `get()` for keys that might be missing.
- **4.1 Lists** — good rows and bad rows are each collected into a list as we walk the file.
- **3.1 Functions** — the reader is packaged as a function that takes a path and returns its results, so callers can reuse it.

## 3. Learning Objectives

After this topic you should be able to:

- Explain why a real-world data reader must **skip and log** bad rows instead of crashing on the first one.
- Structure a read loop so a `try`/`except` wraps the processing of **each individual row**, isolating one bad row from the rest.
- Validate a row's fields — presence, type, and range — and `raise` a clear error when a row is invalid.
- **Separate valid records from invalid ones**, returning clean data in one collection and an error report in another.
- Assemble file opening, CSV parsing, per-row validation, and error collection into one complete, runnable reader function.
- Write the clean rows back out to a new CSV so downstream code only ever sees good data.

## 4. Introduction

You have all the parts now. In 7.1 you learned to open files and read a CSV; in 7.2 you learned to catch exceptions instead of crashing. This topic is where those two skills meet a fact of professional life: **real data is dirty**. A CSV exported from a spreadsheet, a form, or another team's system will have blank cells, a price typed as `"free"`, a missing column, a stray header repeated halfway down. A naive reader that does `int(row["price"])` on every row works perfectly in the demo and then explodes on row 4,812 of the customer's file — losing the other 9,000 good rows with it.

The professional answer is a **robust file reader**: a reader that processes what it can, sets aside what it can't, records *why* each bad row was rejected, and keeps going to the end. Instead of "all or nothing," you get two clean piles — the **valid** records you can use, and the **invalid** ones you can report back to whoever produced the file. That "keep going, but write down what broke" behavior is the single most useful pattern in this whole module.

This is a capstone. We are not learning new syntax — we are combining `with`, `csv.DictReader`, `try`/`except`, validation, and `raise` into one program that you could genuinely drop into a real project [1][2]. We build it in layers: first a fragile version that crashes, then the per-row guard that saves it, then validation, then separating and writing out the results.

## 5. Core Concepts

### <u>**Why "robust" means "keep going."**</u>

A **robust** reader is one that survives bad input. The opposite is a **fragile** reader: one bad row and the whole program stops with a traceback, discarding every row it had already read and every row it hadn't reached yet. That is almost never what you want when processing a data file, because the failure is usually in the *data*, not in your code — and the person who can fix the data needs to know *which* rows were bad and *why* [3].

The core behavior has a name we'll use throughout: the **skip-and-log pattern**. For each row: try to process it; if it fails, record the failure (the row and its reason) and move on to the next row. Nothing crashes the loop. At the end you have processed the entire file and you know exactly what happened to every row.

Analogy: think of a quality inspector on a conveyor belt. A defective item doesn't stop the belt — the inspector pulls it off, drops it in the "rejects" bin with a note ("cracked lid"), and lets the belt keep moving. The good items flow on to shipping. A fragile reader is an inspector who, on seeing the first defect, shuts down the entire factory.

### <u>**Per-row `try`/`except`: putting the guard in the right place.**</u>

The whole trick is *where* you put the `try`/`except`. In 7.2 you often wrapped an entire operation. Here you wrap **the body of the loop, once per row**:

```python
for row in reader:
    try:
        # process THIS row
        ...
    except SomeError:
        # this row failed — record it and continue to the next row
        ...
```

Because the `try` sits *inside* the `for` loop, an exception raised while processing one row jumps only to that iteration's `except` block. Python then continues the loop with the next row [1]. If you instead wrapped the `for` loop from the *outside*, the first bad row would break out of the whole loop and you'd lose the rest — that is the fragile version. Same exceptions, same handlers; the placement is the entire difference.

### <u>**Validation: deciding what "bad" means.**</u>

Before you can reject a row you must define what a *good* row is. **Validation** is checking a row against those rules. For a row like `{"name": "Sam", "age": "34", "email": "sam@x.com"}` the rules might be:

- **Presence** — the columns you need actually exist. A missing `"age"` key raises `KeyError` (from 7.2); or use `row.get("age")` and check for `None`.
- **Type / format** — `int(row["age"])` succeeds. If the cell holds `"thirty"`, `int()` raises `ValueError` (from 7.2). Remember from 7.1 that everything read from a CSV is a **string**, so numeric fields must be converted, and conversion is exactly where bad data reveals itself.
- **Range / business rule** — even a valid integer can be nonsense. An `age` of `-5` or `500` is the right type but the wrong value, so *you* `raise ValueError("age out of range")` yourself (the `raise`-early idea from 7.2).

Validation can fail in two ways, and both are handled the same: Python *raises for you* (`ValueError` from `int("cat")`, `KeyError` from a missing column), or *you raise* when a business rule is broken. Either way the per-row `except` catches it.

### <u>**Separating valid from invalid data.**</u>

The output of a robust reader is not one thing, it's **two collections** [3]:

- a list of **valid records** — the rows that passed every check, converted into clean Python values ready to use; and
- a list of **errors** — one entry per bad row, each recording *which* row (a line number is invaluable) and *why* it failed.

Keeping these separate is the payoff. Downstream code loops over the valid list and trusts every item. A human reads the error list to fix the source file. You never mix "data I can use" with "data I must report" — a mistake that leads to silently processing garbage. In code this is just two lists you append to as you go:

```python
valid = []
errors = []
```

For the error entries, a small `dict` per failure reads well: `{"line": 5, "row": {...}, "reason": "age out of range"}`.

### <u>**Logging the bad rows.**</u>

"Logging" here just means **recording** each rejection somewhere you can inspect later — it does not require any special library. Two beginner-friendly options:

- **Collect to a list** (what we do above): append an error `dict` to `errors`. The caller decides what to do with them — print a summary, write them to a file, count them. This keeps the reader pure and testable.
- **Print as you go**: a quick `print(f"Skipping line {n}: {reason}")` gives immediate feedback while developing.

Python's standard library also has a dedicated `logging` module (e.g. `logging.warning(...)`) built for exactly this in larger applications, but you don't need it to understand the pattern, and we won't rely on it here. The concept — *don't discard a failure silently; write it down* — is what matters, and a plain list captures it perfectly.

### <u>**`csv.DictReader` and malformed rows.**</u>

We build the reader on `csv.DictReader` (from 7.1) because addressing fields by name — `row["age"]` — is clearer than by position — `row[2]` — and it survives columns being reordered. `DictReader` reads the first line as the header and yields each subsequent row as a `dict` mapping header → value [2].

One CSV-specific wrinkle worth naming: a row can have the **wrong number of fields**. If a data row has *more* values than there are headers, `DictReader` puts the extras under a special key you name with `restkey`; if a row has *fewer* values, the missing columns are filled with `restval` (default `None`) [2]. So a short row won't raise on its own — the missing field quietly becomes `None`, which your validation must then catch (that's why the presence check matters). Knowing this stops "why is `age` suddenly `None`?" from becoming a mystery.

## 6. Implementation

We build the reader in four moves. Our sample file `people.csv` is deliberately messy:

```
name,age,email
Sam,34,sam@example.com
Ada,thirty,ada@example.com
Lee,-5,lee@example.com
Kai,29
Rob,41,rob@example.com
```

Row by row: Sam is fine; Ada's age is not a number (`ValueError`); Lee's age is out of range (business-rule failure); Kai is missing the `email` column entirely (a short row — `email` becomes `None`); Rob is fine.

### Move 1 — The fragile version (what NOT to ship)

```python
import csv

def read_people_fragile(path):
    people = []
    with open(path, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            person = {
                "name": row["name"],
                "age": int(row["age"]),          # explodes on "thirty"
                "email": row["email"].lower(),
            }
            people.append(person)
    return people

print(read_people_fragile("people.csv"))
```

This crashes on Ada's row with `ValueError: invalid literal for int() with base 10: 'thirty'`. Sam's good row is already in `people`, but it's thrown away when the exception propagates, and Lee, Kai, and Rob are never even read. One bad cell, total loss.

### Move 2 — Add the per-row guard (skip-and-log)

Move the `try`/`except` *inside* the loop so one bad row can't sink the rest:

```python
import csv

def read_people(path):
    valid = []
    errors = []
    with open(path, newline="") as f:
        reader = csv.DictReader(f)
        for line_no, row in enumerate(reader, start=2):   # data starts on line 2
            try:
                person = {
                    "name": row["name"],
                    "age": int(row["age"]),
                    "email": row["email"].lower(),
                }
                valid.append(person)
            except (ValueError, KeyError, AttributeError) as err:
                errors.append({"line": line_no, "row": row, "reason": str(err)})
    return valid, errors
```

`enumerate(reader, start=2)` numbers the rows starting at 2, since line 1 was the header — so error messages point at the real line in the file. The grouped `except (ValueError, KeyError, AttributeError)` (from 7.2) catches the three ways this row can fail: `int()` on a non-number (`ValueError`), a truly missing key (`KeyError`), and calling `.lower()` on `None` when a short row left `email` as `None` (`AttributeError`). Each failure is appended to `errors` and the loop continues.

### Move 3 — Add real validation with a raised error

`int("-5")` succeeds, so Lee's out-of-range age would slip through Move 2. We add an explicit business-rule check and `raise` our own `ValueError` (the raise-early idea from 7.2). Pulling validation into its own function keeps the loop readable (3.1):

```python
import csv

def validate_row(row):
    """Return a clean person dict, or raise ValueError/KeyError if the row is bad."""
    name = row["name"]                      # KeyError if column missing
    age_text = row.get("age")               # None if missing (short row)
    email = row.get("email")

    if not name:
        raise ValueError("name is empty")
    if age_text is None:
        raise ValueError("age is missing")
    age = int(age_text)                     # ValueError if not a number
    if age < 0 or age > 150:
        raise ValueError(f"age {age} out of range")
    if not email:
        raise ValueError("email is missing")

    return {"name": name, "age": age, "email": email.lower()}


def read_people(path):
    valid = []
    errors = []
    with open(path, newline="") as f:
        reader = csv.DictReader(f)
        for line_no, row in enumerate(reader, start=2):
            try:
                valid.append(validate_row(row))
            except (ValueError, KeyError) as err:
                errors.append({"line": line_no, "row": row, "reason": str(err)})
    return valid, errors
```

Now every rule funnels through one `raise`/`except` channel: whether Python raises (`int("thirty")`) or we raise (`age -5 out of range`, `email is missing`), the loop's `except` catches it, logs it, and moves on.

### Move 4 — Run it, report, and write valid rows out

The caller uses the two collections: print a summary of the errors, and write the clean rows to a new CSV with `csv.DictWriter` (the writer side of the `csv` module from 7.1) so downstream code only sees good data [1][2]:

```python
valid, errors = read_people("people.csv")

print(f"Read {len(valid)} valid rows, {len(errors)} bad rows.\n")

print("Valid records:")
for person in valid:
    print(" ", person)

print("\nErrors:")
for e in errors:
    print(f"  line {e['line']}: {e['reason']}  ->  {e['row']}")

# Separate the valid data into its own file
with open("people_clean.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "age", "email"])
    writer.writeheader()
    writer.writerows(valid)
```

Expected output:

```
Read 2 valid rows, 3 bad rows.

Valid records:
  {'name': 'Sam', 'age': 34, 'email': 'sam@example.com'}
  {'name': 'Rob', 'age': 41, 'email': 'rob@example.com'}

Errors:
  line 3: invalid literal for int() with base 10: 'thirty'  ->  {'name': 'Ada', 'age': 'thirty', 'email': 'ada@example.com'}
  line 4: age -5 out of range  ->  {'name': 'Lee', 'age': '-5', 'email': 'lee@example.com'}
  line 5: email is missing  ->  {'name': 'Kai', 'age': '29', 'email': None}
```

And `people_clean.csv` now contains only the two good rows:

```
name,age,email
Sam,34,sam@example.com
Rob,41,rob@example.com
```

That is the complete robust reader: it read the entire messy file, kept the 2 good rows, rejected the 3 bad ones *with reasons and line numbers*, never crashed, and produced a clean output file the rest of the system can trust.

## 7. Real-World Patterns

- **Data import / ETL.** Loading a customer's CSV into a database is the textbook case: import the valid rows, and hand back a rejects report so they can fix the file and resend. The valid/invalid split *is* the deliverable [3].
- **Form and upload processing.** A web app that accepts an uploaded spreadsheet validates each row, accepts the good ones, and shows the user a list of "row 12: invalid email" errors — the exact skip-and-log shape built above.
- **Parsing exercises and interviews.** "Parse this CSV, skipping malformed lines" is a common coding-interview task, and the per-row-try/collect-errors structure is the expected answer [3].
- **Nightly batch jobs.** A scheduled job that must finish even when a few records are dirty relies on skip-and-log so one bad row never aborts the run; the error list becomes tomorrow morning's cleanup ticket.

## 8. Best Practices

- **Wrap each row, not the whole loop.** The `try`/`except` goes *inside* the `for`, so one bad row is isolated and the loop continues [1].
- **Record the line number.** `enumerate(reader, start=2)` turns "something failed" into "line 5 failed," which is the difference between a useful and a useless error report.
- **Validate before you trust.** Check presence, type, and range. `int()` will catch non-numbers; *you* must catch out-of-range values by raising your own `ValueError` (7.2).
- **Return two collections, not one.** Keep valid records and errors separate so callers never accidentally process a bad row [3].
- **Catch specific exceptions.** Group the ones you actually expect — `except (ValueError, KeyError)` — rather than a bare `except:` that would also hide real bugs in your code (7.2).
- **Never fail silently.** A skipped row must be logged (collected or printed). Skipping without recording is worse than crashing, because the data quietly goes missing.
- **Keep validation in its own function.** `validate_row(row)` is easy to read, easy to reuse, and easy to test in isolation (3.1).

## 9. Hands-On Exercise

Take the `read_people` reader above and extend it for a `products.csv` with columns `sku,name,price`. Write a `validate_product(row)` that requires a non-empty `sku`, converts `price` with `float()` (catching non-numbers), and raises a `ValueError` if `price` is negative. Run it against a file where at least two rows are bad (one non-numeric price, one negative price), print a "read N valid, M bad" summary with line numbers, and write the valid products to `products_clean.csv` with `csv.DictWriter`. Confirm the clean file contains only the good rows.

## 10. Key Takeaways

- A **robust reader** processes an entire file even when some rows are bad; it uses the **skip-and-log pattern** — reject the bad row with a reason, then continue.
- The key move is placing the `try`/`except` **inside** the read loop so a failure jumps to that one iteration's handler and the loop keeps going, instead of breaking out.
- **Validation** checks each row for presence, type, and range; failures come either from Python (`ValueError`, `KeyError`) or from a rule *you* enforce with `raise`, and the per-row `except` handles both the same way.
- A robust reader returns **two collections** — valid records and an errors report (with line numbers and reasons) — so clean data and rejects never get mixed.
- The full pattern combines everything in this module: `with` + `csv.DictReader` to read, per-row `try`/`except` to guard, validation + `raise` to judge, and `csv.DictWriter` to write the clean rows back out.

## 11. Next Steps

_System-derived from the next entry in curriculum/sequence.md._
