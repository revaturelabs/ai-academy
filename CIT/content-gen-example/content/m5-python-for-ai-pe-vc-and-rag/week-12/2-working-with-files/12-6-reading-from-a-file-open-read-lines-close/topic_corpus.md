---
topic_id: "12.6"
title: "Reading from a file — open, read lines, close"
position_in_module: 1
generated_at: "2026-06-14T00:00:00Z"
resource_count: 3
---

# 1. Reading from a File — Open, Read Lines, Close — Topic Corpus

## 2. Prerequisites

This topic assumes the following prior knowledge:

- **12.1 — Functions:** you can define a function with `def` and call it by name.
- **12.4 — Lists:** you know how to create a list, access items by index, use `len()`, `append()`, and iterate with a `for` loop. `.readlines()` returns a list, so list skills apply directly.
- **12.5 — Dictionaries:** you have seen key-value storage; real-world patterns in this topic combine file reading with dictionaries.
- **Week 11 — Strings:** you can work with text values. Each line from a file is a string, and you will use string methods (`.strip()`, `.split()`) on it.
- **Week 11 — For loops and if/else:** you can repeat code over a sequence and make conditional decisions.

## 3. Learning Objectives

By the end of this topic you will be able to:

1. Open a text file for reading using the `open()` function with mode `'r'` and explain what the returned **file object** represents.
2. Read the entire file contents as a single string using `.read()`.
3. Read all lines into a list using `.readlines()`, and read one line at a time using `.readline()`.
4. Close a file correctly using `.close()` and explain why resource cleanup matters.
5. Use a `with` block to open and automatically close a file — the preferred pattern in Python.
6. Iterate over every line in a file using `for line in file:` and remove trailing whitespace with `.strip()`.

## 4. Introduction

Every program you have written so far stores its values in variables. Variables vanish when the program stops — run the program again and the data is gone. A **file** solves this: it stores data on disk so it persists between runs. This is how the lab works: student marks live in a text file, your program reads them in, processes them with the functions from Topics 12.1–12.4, and writes a summary back out.

This topic covers one direction: *reading* from a file that already exists [1]. The reverse direction — writing a new file or appending to an existing one — is Topic 12.7.

The Python workflow for reading a file is always the same three steps:

1. **Open** the file — tell Python which file you want and what you want to do with it.
2. **Read** the contents — pull the text into Python variables.
3. **Close** the file — release the connection so the operating system can use it for other things.

Python provides the `open()` function for step 1, several reading methods for step 2, and `.close()` for step 3. It also provides a `with` block that handles open and close automatically — that is the pattern you will use in practice [1][2].

## 5. Core Concepts

### 5.1 What a Text File Is

A **text file** is a sequence of characters stored on disk [1]. The content is divided into lines by a special **newline character**, written as `\n`. When you read a file in Python, you see the raw text — including those `\n` characters at the end of each line.

For this topic, all files are **plain text**: `.txt` files or simple comma-separated `.csv` files you can open in any text editor. Each line is a string of characters followed by `\n`. Binary files (images, compiled programs) behave differently and are not covered here [1].

**Key point:** a line you read from a file looks like `'Alice,88\n'`, not `'Alice,88'`. Removing the trailing `\n` is the first thing you do when processing a line — covered in Section 5.7 [1][3].

### 5.2 Opening a File with `open()`

`open()` is a Python built-in function that connects your program to a file on disk and returns a **file object** [1][2]:

```python
f = open("marks.txt", "r")
```

**Two arguments:**

- **Filename** — the name of the file to open. If the file is in the same folder as your script or notebook, just the filename is enough.
- **Mode** — a string telling Python what you intend to do with the file:

| Mode | Meaning |
|---|---|
| `'r'` | Read — open for reading. The file must already exist. |
| `'w'` | Write — create a new file or overwrite an existing one. Topic 12.7. |
| `'a'` | Append — add to the end of an existing file. Topic 12.7. |

For this topic, mode is always `'r'`. If the file does not exist, Python raises a **`FileNotFoundError`** — an error meaning the specified file could not be found on disk. Error handling for missing files is covered in a later topic [1][2].

**The return value — a file object:**

`open()` returns a **file object** (sometimes called a file handle). Think of it as a bookmark sitting at the start of the file. All reading methods belong to this object. When you call a reading method, the bookmark moves forward so the next call picks up where the last left off [1][3].

```python
f = open("marks.txt", "r")
# f is the file object; bookmark is at the start of marks.txt
```

### 5.3 Reading the File — Three Methods

Once the file is open, you have three ways to read its contents [1][3].

---

**`.read()` — read the entire file as one string:**

```python
f = open("marks.txt", "r")
content = f.read()
print(content)
f.close()
```

`content` is a single string containing every character in the file, including `\n` between lines. Useful when you need the whole text at once — to search for a pattern, count characters, or pass to another function [1].

---

**`.readlines()` — read all lines into a list:**

```python
f = open("marks.txt", "r")
lines = f.readlines()
print(lines)
# ['Alice,88\n', 'Bob,72\n', 'Carol,95\n']
f.close()
```

Each item in the list is one line from the file, with its trailing `\n` intact. Because the result is a plain Python list, everything from Topic 12.4 applies: `len(lines)` counts lines, `lines[0]` accesses the first, and a `for` loop processes each one [1][2].

---

**`.readline()` — read one line at a time:**

```python
f = open("marks.txt", "r")
first  = f.readline()   # 'Alice,88\n'
second = f.readline()   # 'Bob,72\n'
third  = f.readline()   # 'Carol,95\n'
end    = f.readline()   # '' — empty string signals end of file
f.close()
```

Each call to `.readline()` reads the next line and moves the bookmark forward. When the end of the file is reached, `.readline()` returns an empty string `''` — not `'\n'`, which would mean a genuinely blank line [1][3].

---

**Choosing a method:**

| Method | Returns | Use when |
|---|---|---|
| `.read()` | Whole file as one string | You need the entire text at once |
| `.readlines()` | List of all lines (each with `\n`) | You need all lines as a list to index or process |
| `.readline()` | One line at a time | Reading a large file where loading all lines uses too much memory |

### 5.4 Closing a File with `.close()`

Every file you open must be closed when you are done with it [1][2]:

```python
f = open("marks.txt", "r")
content = f.read()
f.close()   # release the connection
```

**Why closing matters:**

- The operating system limits how many files a program can have open at once. Leaving files open wastes that limited resource.
- On some systems, data is not confirmed until the file is closed — critical for writing but a good habit for reading too.
- Forgetting `.close()` in a long-running program causes a **resource leak** — the program slowly exhausts its available file handles.

The `with` statement in Section 5.5 closes the file automatically [1].

### 5.5 The `with` Block — the Preferred Pattern

A `with` block opens the file, runs your code, and **automatically closes the file** when the block ends — even if an error occurs inside [1][3]:

```python
with open("marks.txt", "r") as f:
    content = f.read()
# file is closed here automatically — no .close() needed
print(content)
```

**Breaking this down:**

- `open("marks.txt", "r")` — opens the file.
- `as f` — gives the file object the name `f` inside the block.
- The indented block is where you do your reading. `f` is valid only inside that block.
- When the block ends — whether normally or due to an error — Python closes `f` for you.

**Why `with` is always preferred:**

- Shorter — no separate `.close()` call to forget.
- Safer — guaranteed to close even if your code crashes partway through.
- Conventional — every Python tutorial, textbook, and production codebase uses `with` for file access [1][2][3].

From this point on, every file example in this course uses a `with` block.

### 5.6 Iterating Line by Line with `for`

The cleanest way to process a file one line at a time is to loop directly over the file object [1][3]:

```python
with open("marks.txt", "r") as f:
    for line in f:
        print(line)
```

This reads and processes one line at a time without loading the entire file into memory. It produces the same result as looping over the list from `.readlines()`, but is more memory-efficient for large files [1].

Each `line` variable includes a trailing `\n`. `print(line)` therefore looks double-spaced because `print()` also adds a newline. Section 5.7 shows how to strip it [1].

### 5.7 Cleaning Lines with `.strip()`

Lines read from a file carry a trailing `\n`. Use `.strip()` to remove it (along with any leading or trailing whitespace) before processing [1][2]:

```python
with open("marks.txt", "r") as f:
    for line in f:
        clean = line.strip()   # 'Alice,88\n' → 'Alice,88'
        print(clean)
```

Output:
```
Alice,88
Bob,72
Carol,95
```

`.strip()` is a **string method** — called on a string value with dot notation, it returns a new string with whitespace removed from both ends. It does not change the original string [1].

**Why stripping matters:** `'Alice,88\n'` and `'Alice,88'` are not equal strings in Python — the `\n` makes them different. Stripping before any comparison or type conversion is required habit when working with file data [1][2].

## 6. Implementation

### Worked Example: Reading Student Marks from a File

**Goal:** read a file where each line is `name,score`, extract the names and scores, and return them as a list of pairs.

**The file — `marks.txt`:**
```
Alice,88
Bob,72
Carol,95
```

---

**Step 1 — Open and print raw lines:**

```python
with open("marks.txt", "r") as f:
    for line in f:
        print(line)
```

Output (double-spaced from raw `\n`):
```
Alice,88

Bob,72

Carol,95

```

---

**Step 2 — Strip the newline:**

```python
with open("marks.txt", "r") as f:
    for line in f:
        clean = line.strip()
        print(clean)
```

Output:
```
Alice,88
Bob,72
Carol,95
```

---

**Step 3 — Split on comma to get name and score separately:**

```python
with open("marks.txt", "r") as f:
    for line in f:
        clean = line.strip()
        parts = clean.split(",")   # ['Alice', '88']
        name  = parts[0]
        score = parts[1]
        print(name, "scored", score)
```

Output:
```
Alice scored 88
Bob scored 72
Carol scored 95
```

`.split(",")` is a string method that splits at every comma and returns a list. `parts[0]` is the name; `parts[1]` is the score as a string [1][2].

---

**Step 4 — Wrap in a function:**

```python
def load_marks(filename):
    results = []
    with open(filename, "r") as f:
        for line in f:
            clean = line.strip()
            if clean:                       # skip blank lines
                parts = clean.split(",")
                name  = parts[0]
                score = int(parts[1])       # convert '88' to integer 88
                results.append([name, score])
    return results

data = load_marks("marks.txt")
for row in data:
    print(row[0], "→", row[1])
```

Output:
```
Alice → 88
Bob → 72
Carol → 95
```

Key points: `if clean:` skips empty lines (an empty string is falsy); `int(parts[1])` converts the score string to an integer so arithmetic works later [1][2][3].

## 7. Real-World Patterns

### Pattern 1 — Reading a Dataset for Statistical Processing

The lab reads a marks file and computes average, highest, and lowest. The general shape [1][2]:

```python
def load_scores(filename):
    scores = []
    with open(filename, "r") as f:
        for line in f:
            value = line.strip()
            if value:
                scores.append(int(value))
    return scores

scores = load_scores("marks.txt")
print("Count:", len(scores))
print("Average:", sum(scores) / len(scores))
```

`load_scores` returns a plain list of integers — then all list operations from Topic 12.4 and functions from Topics 12.1–12.3 apply directly [1][3].

### Pattern 2 — Reading a Key-Value Configuration File

Programs often store settings as one `key=value` per line. Reading it produces a dictionary from Topic 12.5 [1][3]:

```python
settings = {}
with open("config.txt", "r") as f:
    for line in f:
        clean = line.strip()
        if clean and "=" in clean:
            key, value = clean.split("=", 1)
            settings[key] = value

print(settings["model"])
```

`split("=", 1)` splits at the first `=` only, preserving any `=` inside the value. The result is a dictionary ready to use anywhere in the program [1][2].

## 8. Best Practices

**Do:**

- **Always use a `with` block.** It is the Python standard and closes the file automatically [1][2][3].
- **Always call `.strip()` on every line before processing.** Raw lines include `\n`; forgetting to strip is the most common source of file-processing bugs.
- **Check for empty lines with `if clean:` before splitting or converting** — blank lines at the end of a file are common and cause errors when split or passed to `int()`.
- **Convert numeric strings with `int()` or `float()`** before arithmetic. A score read from a file is the string `'88'`, not the integer `88`.
- **Wrap file reading in a function** with a `filename` parameter so the rest of your program works with data, not file objects [1].

**Do not:**

- **Do not open a file without a `with` block** unless you have a specific reason to manage the lifecycle manually.
- **Do not call `.read()` twice on the same file object.** After the first call the bookmark is at the end; a second call returns `''`. Close and reopen, or use `.readlines()` once.
- **Do not assume the file exists.** Python raises **`FileNotFoundError`** if it does not. Handling missing files requires `try/except`, covered in a later topic.
- **Do not use `.readlines()` on very large files** — it loads everything into memory at once. Use `for line in f:` for large datasets.

| Situation | Right approach | Common mistake |
|---|---|---|
| Open + auto-close | `with open(...) as f:` | `f = open(...)` without `.close()` |
| Process every line | `for line in f: line.strip()` | Forgetting `.strip()` → `\n` in data |
| Skip blank lines | `if clean:` before split | Calling `split()` on `''` → empty-list crash |
| Read numbers | `int(line.strip())` | Using string directly in arithmetic → TypeError |
| Re-read file | Close and reopen | Calling `.read()` twice → empty string |

## 9. Hands-On Exercise

Open your Colab notebook.

1. Create `students.txt` using `%%writefile students.txt`. Add three lines, each with a name and a score separated by a comma.
2. Write a `with open("students.txt", "r") as f:` block that uses `for line in f:` to print every line.
3. Modify the loop to strip each line and print the clean version — no extra blank lines in output.
4. Further modify to split each line on `","` and print `"<name> scored <score>"` for each row.
5. Move the reading logic into a function `load_students(filename)` that returns a list of `[name, score_as_integer]` pairs. Call it and print `len()` of the result.
6. Add an `if clean:` guard inside the function to skip blank lines.

## 10. Key Takeaways

- `open("filename.txt", "r")` opens a text file for reading and returns a **file object**. Mode `'r'` is read-only; if the file does not exist, Python raises **`FileNotFoundError`**.
- Three reading methods: `.read()` (whole file as one string), `.readlines()` (all lines as a list, each with `\n`), `.readline()` (one line at a time; returns `''` at end of file).
- Always close a file when done — but use `with open(...) as f:` instead of calling `.close()` manually: it closes automatically, even on error.
- Lines from a file include a trailing `\n`; always call `.strip()` before comparing, splitting, or converting.
- Iterate line by line with `for line in f:` — memory-efficient and the preferred pattern.
- Files bridge Python programs and persistent data on disk — the foundation of the lab's CSV-reading and summary-writing tasks.

## 11. Next Steps

_System-derived from the next entry in curriculum/sequence.md._
