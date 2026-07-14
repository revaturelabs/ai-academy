# File Handling

## Overview

Every program you have written so far forgets everything the moment it stops — variables live in memory, and memory is wiped when the program exits. To remember data between runs, and to exchange it with other systems, a program reads and writes **files**: data stored on disk that survives after the program ends. This topic covers the mechanics of file input/output — opening files in the right mode, reading and writing text, closing files safely with the `with` statement, and handling the two most common data formats you will meet in the wild: CSV and JSON.

## Key Concepts

### Text files vs binary files

A **text file** stores human-readable characters — letters, digits, punctuation — encoded as bytes using a scheme such as UTF-8. Source code, `.txt` notes, CSV, and JSON are all text files. A **binary file** stores raw bytes not meant to be read as characters: images (`.png`), audio (`.mp3`), and compiled programs [1]. The practical difference is how you open them. Text mode (the default) hands you `str` values and quietly translates line endings between operating systems; binary mode hands you raw `bytes`. Everything in this topic works in text mode, which is what CSV and JSON need.

### Absolute vs relative paths

A **path** is the address of a file, and there are two kinds:

- An **absolute path** spells out the location from the top of the filesystem, e.g. `C:\Users\Sam\data\sales.txt` on Windows or `/home/sam/data/sales.txt` on Linux/macOS. It works no matter where your program runs from.
- A **relative path** is given relative to the program's current working directory, e.g. `data/sales.txt`. It is shorter and portable, but only resolves correctly if the program is run from the expected folder.

Think of an absolute path as a full postal address and a relative path as "two doors down from where you're standing" — the relative one only means something once we know where you are standing. Most projects prefer relative paths so the code keeps working when the project folder is copied elsewhere.

### Opening a file: `open()` and modes

You get access to a file with the built-in `open()` function, which returns a **file object** you then read from or write to [1]. The second argument is the **mode** — a short string saying what you intend to do. The four you need now:

- **`"r"` (read).** Open an existing file for reading; this is the default. If the file does not exist, Python raises an error (handling that is the subject of the next topic).
- **`"w"` (write).** Creates the file if it does not exist, and **erases all existing content** if it does. Use with care.
- **`"a"` (append).** Opens for writing, but new text is added to the **end**; existing content is kept.
- **`"r+"` (read and write).** Opens an existing file for both reading and writing without truncating it first.

A quick way to remember the destructive ones: `"w"` wipes, `"a"` adds.

### Reading and writing

Once a file is open in a read mode, there are three ways to pull text out [1]:

- **`read()`** returns the entire contents as one big string. Simple, but loads the whole file into memory — fine for small files, wasteful for huge ones.
- **`readline()`** returns just the next single line, including its trailing newline `\n`. Call it again for the next line.
- **`readlines()`** returns a **list** of strings, one per line, again keeping the `\n` at the end of each.

There is a fourth, idiomatic option: loop directly over the file object. Because a file is iterable, `for line in f:` gives you one line at a time without loading the whole file — the memory-friendly default. To write, you use `write()`, which takes a string and returns the number of characters written [1]. Note that `write()` does **not** add a newline for you — if you want lines, include `\n` yourself.

### Closing safely: the `with` statement

When you finish with a file you should close it, which flushes any buffered data to disk and releases the operating-system handle so other programs can use the file [1]. Forgetting to close can mean your writes never land on disk, or the file stays locked. The problem with calling `close()` by hand is that if something goes wrong between opening and closing, the close line may never run.

The **`with` statement** solves this: it opens a file and guarantees it is closed automatically when the block ends — whether the block finishes normally or is interrupted [1]. An object that works this way, setting something up on entry and cleaning it up on exit, is called a **context manager**.

```python
with open("notes.txt", "r") as f:
    contents = f.read()
# file is automatically closed here
```

Think of `with` as a self-closing door: you walk through it to do your work, and no matter how you leave the room — calmly or in a panic — the door swings shut behind you. This is the recommended way to work with files, and every example from here on uses it.

### Reading CSVs: the `csv` module

A **CSV** (Comma-Separated Values) file stores a table as plain text: one row per line, columns separated by commas. You *could* split each line on commas yourself, but that breaks the moment a value itself contains a comma (like `"Smith, Jr."`). Python's standard-library **`csv` module** handles those quoting rules for you [2]. You wrap the open file in a `csv.reader` and loop over it; each iteration yields one row as a **list of strings** [2]. The `newline=""` argument in `open()` matters here: the official docs specify it so the `csv` module can manage line endings itself and rows are not split incorrectly on some platforms [2]. There is also a `csv.writer` (with a `writerow` method) for producing CSVs, and a `csv.DictReader` that gives each row as a dictionary keyed by the header names instead of a plain list [2].

### Working with JSON: `json.load()` and `json.dump()`

**JSON** (JavaScript Object Notation) is a text format for structured data — the common language of web APIs and configuration files. It maps neatly onto Python types: a JSON object becomes a `dict`, a JSON array becomes a `list`, and strings, numbers, `true`/`false`, and `null` become `str`, `int`/`float`, `bool`, and `None` [3]. The standard-library **`json` module** converts between the two directions [3]:

- **`json.load(file_object)`** reads JSON text from an open file and returns the equivalent Python object (usually a dict or list). This is *deserializing*.
- **`json.dump(python_object, file_object)`** writes a Python object to an open file as JSON text. This is *serializing*.

Two siblings are worth knowing by name: `json.loads()` and `json.dumps()` (note the `s`), which work on **strings** in memory rather than files [3]. The rule of thumb: `load`/`dump` are for files; `loads`/`dumps` are for strings.

## Worked Example

A minimal end-to-end workflow that touches all three formats.

**Step 1 — Write, then read a text file line by line:**

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

**Step 2 — Read a CSV and total a numeric column.** Suppose `sales.csv` contains:

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

Notice the `int(row[2])`: everything read from a CSV arrives as a string, so you must cast before doing arithmetic.

**Step 3 — Round-trip a Python object through JSON:**

```python
import json

record = {"user": "sam", "level": 4, "active": True}

with open("state.json", "w") as f:
    json.dump(record, f, indent=2)   # indent=2 makes it human-readable

with open("state.json", "r") as f:
    loaded = json.load(f)

print(loaded["level"], type(loaded))
```

Expected output:

```
4 <class 'dict'>
```

The object went out to disk as JSON text and came back as a Python `dict` — a complete round-trip.

## In Practice

Where file handling shows up in real code:

- **Config files.** Applications store settings (API keys, feature flags, defaults) in a `config.json` and load it once at startup with `json.load()` [3].
- **Data pipelines.** A common ETL-style task: read a CSV exported from a spreadsheet or database, transform the rows, and write a new CSV. The `csv` module's reader/writer pair covers both ends [2].
- **Logs.** Long-running programs append one line per event to a text file opened in `"a"` mode, so history accumulates rather than being overwritten.
- **Streaming large files.** When a file is too big to fit in memory, iterating `for line in f:` processes it one line at a time.

Habits worth keeping:

- **Always use `with`** so the file is closed for you, even on error [1].
- **Pick the mode deliberately** — reach for `"w"` only when you truly want to overwrite; use `"a"` to add without destroying.
- **Pass `newline=""`** when using the `csv` module [2], and **match the JSON function to the source** — `load`/`dump` for files, `loads`/`dumps` for strings [3].
- **Don't hand-parse CSV or JSON.** Splitting on commas or slicing strings breaks on quoting and edge cases; the standard-library modules already handle them.

## Key Takeaways

- Files let a program remember data between runs and exchange it with other systems; text files hold readable characters, binary files hold raw bytes.
- `open(path, mode)` returns a file object; the mode (`r`, `w`, `a`, `r+`) decides whether you read, overwrite, append, or both — remember `"w"` wipes and `"a"` adds.
- Read with `read()`, `readline()`, `readlines()`, or by looping over the file; write with `write()`, supplying your own `\n`.
- The `with` statement is a context manager that closes the file automatically, so it is the safe default for all file work.
- Use the `csv` module (with `newline=""`) for tabular data and the `json` module (`load`/`dump` for files, `loads`/`dumps` for strings) for structured data.

## References

1. Real Python — *Reading and Writing Files in Python*. https://realpython.com/read-write-files-python/
2. Python documentation — *csv — CSV File Reading and Writing*. https://docs.python.org/3/library/csv.html
3. Real Python — *Working With JSON Data in Python*. https://realpython.com/python-json/
