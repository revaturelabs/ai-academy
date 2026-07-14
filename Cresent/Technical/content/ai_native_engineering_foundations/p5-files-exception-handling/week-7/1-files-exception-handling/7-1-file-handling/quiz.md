# Quiz — 7.1 File Handling

> Bias-defensive MCQ bank generated from the approved topic corpus. Correct-answer
> positions have been shuffled with a topic-seeded RNG; option lengths are balanced.
> `$bias_defense_applied = true` (see `quiz.json`).

$CATEGORY: CIT/AINEF/week-7/7.1-file-handling

---

**Q1.** A `.png` image and a `.txt` note differ in an important way for file I/O. Which statement is correct?

- A) Both are text files, so both hand you `str` values when opened in the default mode.
- B) The `.txt` file is binary and the `.png` file is text, since images are human-readable.
- C) The `.txt` file is a text file (readable characters), while the `.png` is a binary file (raw bytes).
- D) Neither can be opened by Python because `open()` only works on `.csv` and `.json`.

**Answer: C** — A text file stores human-readable characters encoded as bytes; a binary file such as an image stores raw bytes not meant to be read as characters. (Corpus §5, Text vs binary)

---

**Q2.** What is the practical advantage of a **relative** path like `data/sales.txt` over an absolute path?

- A) It stays valid when the project folder is copied elsewhere, as long as the program runs from the expected directory.
- B) It spells out the location from the very top of the filesystem, so it works from anywhere.
- C) It is required whenever you open a binary file, unlike absolute paths which only work for text.
- D) It loads the whole file into memory faster than an absolute path does at open time.

**Answer: A** — A relative path is resolved against the current working directory; it is portable between machines but only resolves if run from the expected folder. (Corpus §5, Absolute vs relative)

---

**Q3.** You open an existing file with `open("log.txt", "w")` and then write to it. What happens to the data that was already in `log.txt`?

- A) The new text is inserted at the top, pushing the old content further down in the file.
- B) The new text is added to the end; the existing content is preserved untouched.
- C) Python raises an error because `"w"` cannot be used on a file that already exists.
- D) All existing content is erased, because `"w"` truncates the file when it opens it.

**Answer: D** — `"w"` (write) creates the file if absent and erases all existing content if present. Remember: `"w"` wipes. (Corpus §5, open() and modes)

---

**Q4.** A program needs to add one new line per event to `events.log` without destroying the history already in the file. Which mode should it open the file in?

- A) `"r"`, because reading a file automatically preserves and extends it.
- B) `"a"` (append), because new text is added to the end and existing content is kept.
- C) `"w"`, because write mode always keeps whatever was there before.
- D) `"r+"`, because that is the only mode that can create a brand-new file.

**Answer: B** — Append mode adds new text to the end of the file while keeping existing content. Remember: `"a"` adds. (Corpus §5, open() and modes)

---

**Q5.** What does `f.readlines()` return when called on an open text file?

- A) A list of strings, one per line, each still keeping its trailing newline character.
- B) A single string containing the entire contents of the file all at once.
- C) Only the next single line of the file, advancing an internal position each call.
- D) A list of integers giving the length in characters of every line in the file.

**Answer: A** — `readlines()` returns a list of strings, one per line, each retaining its `\n`. (Corpus §5, Reading)

---

**Q6.** For a very large file you want to process one line at a time without loading it all into memory. Which approach does the corpus recommend as the memory-friendly default?

- A) Call `read()` once and then split the returned string on the `\n` character yourself.
- B) Call `readlines()` to get the full list, then loop over that list line by line.
- C) Open the file in binary mode so the operating system streams the bytes for you.
- D) Loop directly over the file object with `for line in f:`, which yields one line at a time.

**Answer: D** — A file object is iterable; looping with `for line in f:` gives one line at a time without loading the whole file. (Corpus §5, Reading)

---

**Q7.** After running `f.write("Hello")` followed by `f.write("World")` on a file opened in `"w"` mode, what does the file contain?

- A) `Hello` and `World` on two separate lines, because `write()` adds a newline after each call.
- B) `HelloWorld` on a single line, because `write()` does not add a newline for you.
- C) `Hello\nWorld\n`, because `write()` appends `\n` to every string automatically.
- D) An error, because you must call `writelines()` to write more than one string.

**Answer: B** — `write()` writes exactly the string you give it and does not add a newline; you supply `\n` yourself. (Corpus §5, Writing)

---

**Q8.** Why is using a `with open(...) as f:` block preferred over calling `open()` and `close()` manually?

- A) Because `with` loads the file faster and compresses it automatically on disk.
- B) Because `with` opens the file in append mode by default, protecting existing data.
- C) Because `with` closes the file automatically when the block ends, even if an error interrupts it.
- D) Because `with` converts every line of the file into a dictionary as it reads.

**Answer: C** — The `with` statement is a context manager that guarantees the file is closed when the block exits, normally or on error. (Corpus §5, Context managers)

---

**Q9.** When reading a CSV with `csv.reader`, the corpus opens the file as `open("sales.csv", newline="")`. Why pass `newline=""`?

- A) So the `csv` module can manage line endings itself and rows are not split incorrectly across platforms.
- B) So the file is opened in binary mode, which the `csv` module requires for numeric columns.
- C) So each row is returned as a dictionary keyed by the header names instead of a list.
- D) So the trailing newline is stripped from every string value before your loop sees it.

**Answer: A** — The docs specify `newline=""` so the `csv` module handles line endings itself, avoiding rows being split incorrectly on some platforms. (Corpus §5, Reading CSVs)

---

**Q10.** Iterating over a `csv.reader`, each row comes back as `['2026-01', 'Widgets', '120']`. To total the third column you write `total += int(row[2])`. Why the `int(...)` call?

- A) Because `csv.reader` returns each row as a tuple, and tuples cannot be added directly.
- B) Because the `csv` module reverses column order, so you must re-cast to restore it.
- C) Because `int()` is what tells `csv.reader` which column holds the header row.
- D) Because every value read from a CSV arrives as a string, so it must be cast before arithmetic.

**Answer: D** — CSV values always arrive as strings; you must convert to `int` or `float` before doing math. (Corpus §5 & §8, Reading CSVs)

---

**Q11.** You have JSON *text already stored in a Python string variable* (not in a file). Which function turns that string into a Python object?

- A) `json.load()`, because `load` works on any JSON source whether it is a string or a file.
- B) `json.loads()`, because the `s`-suffixed functions operate on strings in memory.
- C) `json.dump()`, because `dump` reads JSON and returns the matching Python object.
- D) `csv.DictReader()`, because JSON strings are parsed by the CSV module's dict reader.

**Answer: B** — `loads`/`dumps` (with the `s`) work on strings; `load`/`dump` work on open files. (Corpus §5, Working with JSON)

---

**Q12.** A JSON file contains `{"active": true, "scores": [90, 85], "name": null}`. After `data = json.load(f)`, what Python types do these values become?

- A) `true` stays the string `"true"`, the array becomes a tuple, and `null` becomes the empty string.
- B) `true` becomes `1`, the array becomes a set, and `null` becomes the string `"None"`.
- C) `true` becomes `bool` (`True`), the array becomes a `list`, and `null` becomes `None`.
- D) Every value becomes a `str`, because JSON is a text format and loses type information.

**Answer: C** — JSON maps onto Python types: object→dict, array→list, true/false→bool, number→int/float, null→None. (Corpus §5, Working with JSON)

---

**Q13. (Short answer)** In one word, name the Python statement — a context manager — that opens a file and guarantees it is closed automatically when the block ends, even if an error occurs.

- Accepted answers: `with`, `with statement`, `the with statement`

**Answer explanation:** The `with` statement sets the file up on entry and closes it on exit no matter how the block is left. (Corpus §5, Context managers)
