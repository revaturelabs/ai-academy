---
topic_id: 7.1
title: File Handling
position_in_module: 1
generated_at: 2026-07-14T00:00:00Z
resource_count: 3
---

# 1. File Handling — Topic Corpus

## 2. Prerequisites

- **3.3 Modules, Packaging & Professional Tooling** — you need to know that Python has a standard library and that you bring extra tools into a program with an `import` statement. The `csv` and `json` tools used here are imported the same way.
- **5.2 Dictionaries (key-value mapping, `get()`, `items()`)** — JSON data maps directly onto Python dictionaries, so you should already be comfortable with `{"key": "value"}` lookups.
- **5.3 Iterators, Generators & Collections** — a for-loop can walk through a collection one item at a time. An open file behaves like that: you can loop over it line by line without loading everything at once.
- **4.1 Lists** — reading a file often produces a list of lines or a list of rows, and you already know how to index and loop over lists.

## 3. Learning Objectives

After this topic you should be able to:

- Explain the difference between text files and binary files, and between absolute and relative paths.
- Open a file with `open()` using the correct mode (`r`, `w`, `a`, `r+`) for the job.
- Read file contents with `read()`, `readline()`, and `readlines()`, and write content with `write()`.
- Use the `with` statement (a context manager) so files are closed automatically, even if something goes wrong.
- Read tabular data from a CSV file using Python's `csv` module.
- Load JSON data into Python objects with `json.load()` and save Python objects to JSON with `json.dump()`.

## 4. Introduction

Every program you have written so far forgets everything the moment it stops. Variables live in memory, and memory is wiped when the program exits. That is fine for a calculator, but useless for a program that has to remember yesterday's sales, a saved game, or a list of users. To remember things between runs, a program reads and writes **files** — data stored on disk that survives after the program ends.

Files are also how programs talk to each other and to the outside world. A spreadsheet exports a **CSV** file; a web API returns a **JSON** file; a log records what happened line by line. If you cannot open a file, pull the data out, and write results back, you cannot build anything that connects to real data.

This topic is the mechanics of file input/output (I/O): how to open a file, the different **modes** you can open it in, how to read and write, and how the `with` statement guarantees a file gets closed properly [1]. Then we handle two of the most common data formats you will meet in the wild — CSV and JSON. One thing we deliberately leave for the next topic: what happens when a file is missing or malformed. Opening a file that does not exist raises an error, and handling those errors robustly is the whole subject of topic 7.2 (Errors & Exceptions) and 7.3 (Case Study: Robust File Reader). Here we focus on the I/O itself.

## 5. Core Concepts

### <u>**Text files vs binary files.**</u>

A **text file** stores human-readable characters — letters, digits, punctuation — encoded as bytes using a scheme such as UTF-8. Source code, `.txt` notes, CSV, and JSON are all text files. A **binary file** stores raw bytes that are not meant to be read as characters: images (`.png`), audio (`.mp3`), and compiled programs are binary [1].

The practical difference is how you open them. Text mode (the default) hands you `str` values and quietly translates line endings between operating systems. Binary mode hands you raw `bytes`. In this topic we work entirely in text mode, which is what CSV and JSON need.

### <u>**Absolute vs relative paths.**</u>

A **path** is the address of a file. There are two kinds:

- An **absolute path** spells out the location from the very top of the filesystem, e.g. `C:\Users\Sam\data\sales.txt` on Windows or `/home/sam/data/sales.txt` on Linux/macOS. It works no matter where your program is running from.
- A **relative path** is given relative to the program's current working directory, e.g. `data/sales.txt`. It is shorter and portable between machines, but only resolves correctly if the program is run from the expected folder.

Analogy: an absolute path is a full postal address (country, city, street, number); a relative path is "two doors down from where you're standing." The relative one is only meaningful once we know where "you're standing" is. For most projects, relative paths are preferred because they keep the code working when the project folder is copied elsewhere.

### <u>**Opening a file: `open()` and modes.**</u>

You get access to a file with the built-in `open()` function, which returns a **file object** you then read from or write to [1]:

```python
f = open("notes.txt", "r")
```

The second argument is the **mode** — a short string that says what you intend to do. The four you need now:

- **`"r"` (read).** Open an existing file for reading. This is the default if you give no mode. If the file does not exist, Python raises an error.
- **`"w"` (write).** Open for writing. Creates the file if it does not exist, and **erases all existing content** if it does. Use with care.
- **`"a"` (append).** Open for writing, but new text is added to the **end** of the file. Existing content is kept.
- **`"r+"` (read and write).** Open an existing file for both reading and writing without truncating it first.

A quick way to remember the destructive ones: `"w"` wipes, `"a"` adds.

### <u>**Reading: `read()`, `readline()`, `readlines()`.**</u>

Once a file is open in a read mode, there are three ways to pull text out [1]:

- **`read()`** returns the entire contents as one big string. Simple, but loads the whole file into memory — fine for small files, wasteful for huge ones.
- **`readline()`** returns just the next single line, including its trailing newline character `\n`. Call it again to get the following line.
- **`readlines()`** returns a **list** of strings, one per line, again keeping the `\n` at the end of each.

There is a fourth, idiomatic option: loop directly over the file object. Because a file is iterable (see topic 5.3), `for line in f:` gives you one line at a time without loading the whole file — the memory-friendly default for reading line by line.

### <u>**Writing: `write()`.**</u>

In `"w"` or `"a"` mode you send text to the file with `write()`, which takes a string and returns the number of characters written [1]:

```python
f.write("Hello\n")
```

Note that `write()` does **not** add a newline for you — if you want lines, include `\n` yourself. To write many lines at once you can use `writelines(list_of_strings)`, but it likewise adds no newlines.

### <u>**Closing: `close()` and why it matters.**</u>

When you finish with a file you should call `f.close()`. Closing flushes any buffered data to disk and releases the operating-system handle so other programs can use the file [1]. Forgetting to close a file can mean your writes never actually land on disk, or the file stays locked. The problem is that if an error happens between `open()` and `close()`, the `close()` line may never run. The next concept fixes exactly this.

### <u>**Context managers: the `with` statement.**</u>

The **`with` statement** opens a file and guarantees it is closed automatically when the block ends — whether the block finishes normally or an error interrupts it [1]. An object that can be used this way (setting something up on entry and cleaning it up on exit) is called a **context manager**.

```python
with open("notes.txt", "r") as f:
    contents = f.read()
# file is automatically closed here
```

Analogy: `with` is like a self-closing door. You walk through it (do your work with the file), and no matter how you leave the room — calmly or in a panic — the door swings shut behind you. You never have to remember to close it. This is the recommended way to work with files, and every example from here on uses it.

### <u>**Reading CSVs: the `csv` module.**</u>

A **CSV** (Comma-Separated Values) file stores a table as plain text: one row per line, columns separated by commas. Because it is just text you *could* split each line on commas yourself, but that breaks the moment a value itself contains a comma (like `"Smith, Jr."`). Python's standard-library **`csv` module** handles those quoting rules for you [2].

You wrap the open file in a `csv.reader`, then loop over it. Each iteration yields one row as a **list of strings** [2]:

```python
import csv

with open("sales.csv", newline="") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)      # e.g. ['2026-01', 'Widgets', '120']
```

The `newline=""` argument in `open()` is important: the official docs specify it so the `csv` module can manage line endings itself and rows are not split incorrectly on some platforms [2]. There is also a `csv.writer` (with a `writerow` method) for producing CSV files, and a `csv.DictReader` that gives each row as a dictionary keyed by the header names instead of a plain list [2].

### <u>**Working with JSON: `json.load()` and `json.dump()`.**</u>

**JSON** (JavaScript Object Notation) is a text format for structured data — the common language of web APIs and configuration files. It maps neatly onto Python types: a JSON object becomes a `dict`, a JSON array becomes a `list`, and strings, numbers, `true`/`false`, and `null` become `str`, `int`/`float`, `bool`, and `None` [3].

The standard-library **`json` module** converts between the two directions [3]:

- **`json.load(file_object)`** reads JSON text from an open file and returns the equivalent Python object (usually a dict or list). This is *deserializing*.
- **`json.dump(python_object, file_object)`** writes a Python object to an open file as JSON text. This is *serializing*.

```python
import json

# Reading JSON from a file
with open("config.json", "r") as f:
    config = json.load(f)      # config is now a dict
print(config["name"])

# Writing a Python object to JSON
data = {"name": "Sam", "scores": [90, 85, 88]}
with open("out.json", "w") as f:
    json.dump(data, f, indent=2)   # indent=2 makes it human-readable
```

There are two sibling functions worth knowing by name: `json.loads()` and `json.dumps()` (note the `s`), which work on **strings** in memory rather than files [3]. `load`/`dump` are for files; `loads`/`dumps` are for strings.

## 6. Implementation

A minimal end-to-end workflow that touches all three formats. Assume a small text file, then a CSV, then JSON.

Step 1 — Write and then read a text file:

```python
# Write three lines
with open("greetings.txt", "w") as f:
    f.write("Hello\n")
    f.write("Bonjour\n")
    f.write("Hola\n")

# Read it back, line by line (memory-friendly)
with open("greetings.txt", "r") as f:
    for line in f:
        print(line.strip())   # strip() removes the trailing newline
```

Expected output:

```
Hello
Bonjour
Hola
```

Step 2 — Read a CSV and total a numeric column. Suppose `sales.csv` contains:

```
month,product,units
2026-01,Widgets,120
2026-02,Widgets,90
```

```python
import csv

total = 0
with open("sales.csv", newline="") as f:
    reader = csv.reader(f)
    header = next(reader)          # pull off the header row first
    for row in reader:
        total += int(row[2])       # units column, converted to int
print("Total units:", total)
```

Expected output:

```
Total units: 210
```

Step 3 — Round-trip a Python object through JSON:

```python
import json

record = {"user": "sam", "level": 4, "active": True}

with open("state.json", "w") as f:
    json.dump(record, f, indent=2)

with open("state.json", "r") as f:
    loaded = json.load(f)

print(loaded["level"], type(loaded))
```

Expected output:

```
4 <class 'dict'>
```

## 7. Real-World Patterns

- **Config files.** Applications store settings (API keys, feature flags, defaults) in a `config.json` and load it once at startup with `json.load()` — exactly the pattern above [3].
- **Data pipelines.** A common ETL-style task is: read a CSV exported from a spreadsheet or database, filter or transform the rows, and write a new CSV. The `csv` module's reader/writer pair covers both ends [2].
- **Logs.** Long-running programs append one line per event to a text file opened in `"a"` mode, so history accumulates rather than being overwritten.
- **Streaming large files.** When a file is too big to fit in memory, iterating `for line in f:` processes it one line at a time — the same laziness you saw with generators in topic 5.3.

## 8. Best Practices

- **Always use `with`.** Prefer `with open(...) as f:` over a bare `open()` so the file is closed for you, even on error [1].
- **Pick the mode deliberately.** Reach for `"w"` only when you truly want to overwrite; use `"a"` to add without destroying. Confusing the two silently erases data.
- **Pass `newline=""` when using the `csv` module.** The official docs call for it so rows are parsed correctly across platforms [2].
- **Match the JSON function to the source.** `json.load`/`json.dump` for open files; `json.loads`/`json.dumps` for strings [3].
- **Convert CSV values.** Everything read from a CSV arrives as a string, so cast to `int` or `float` before doing arithmetic — `int(row[2])`, not `row[2]`.
- **Don't hand-parse CSV or JSON.** Splitting on commas or slicing strings breaks on quoting and edge cases; the standard-library modules already handle them.

## 9. Hands-On Exercise

Create a text file `names.txt` with one name per line. Write a program that (1) opens it with `with`, (2) loops over the lines counting how many names there are and collecting them into a list, and (3) writes that list to `names.json` using `json.dump()`. Then reopen `names.json` with `json.load()` and print the count to confirm the round-trip worked.

## 10. Key Takeaways

- Files let a program remember data between runs and exchange it with other systems; text files hold readable characters, binary files hold raw bytes.
- `open(path, mode)` returns a file object; the mode (`r`, `w`, `a`, `r+`) decides whether you read, overwrite, append, or both — remember `"w"` wipes and `"a"` adds.
- Read with `read()`, `readline()`, `readlines()`, or by looping over the file; write with `write()` (you supply your own `\n`).
- The `with` statement is a context manager that closes the file automatically, so it is the safe default for all file work.
- Use the `csv` module (with `newline=""`) for tabular data and the `json` module (`load`/`dump` for files, `loads`/`dumps` for strings) for structured data.

## 11. Next Steps

_System-derived from the next entry in curriculum/sequence.md._
