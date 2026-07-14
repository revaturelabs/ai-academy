---
topic_id: "12.5"
title: "Dictionaries — key-value pairs for structured data"
position_in_module: 5
generated_at: "2026-06-14T00:00:00Z"
resource_count: 3
---

# 1. Dictionaries — Key-Value Pairs for Structured Data — Topic Corpus

## 2. Prerequisites

This topic builds directly on earlier Week 12 topics and assumes Python basics from Week 11:

- **12.1 — Functions:** you can define a function with `def` and call it by name.
- **12.2 — Parameters and return values:** you know how to pass values into a function and get a result back.
- **12.3 — One function = one job:** you understand why each function should have a single, clearly stated purpose.
- **12.4 — Lists:** you know how to create a list with square brackets, access items by index, use `len()`, `append()`, and iterate with a `for` loop.

Supporting background from Week 11:

- **Variables:** you know how to store a single value in a variable (e.g. `score = 85`).
- **Strings:** you know how to write and use text values in double or single quotes.
- **For loops and if/else:** you can repeat code and make decisions.

## 3. Learning Objectives

By the end of this topic you will be able to:

1. Create a Python **dictionary** using curly-brace syntax and store key-value pairs inside it.
2. **Access** a value by its key, and explain why a key is different from an index.
3. **Add** a new key-value pair to a dictionary and **modify** the value of an existing key.
4. **Check** whether a key exists in a dictionary using the `in` keyword.
5. **Iterate** over a dictionary's keys, values, and key-value pairs using `for`, `.values()`, and `.items()`.
6. Retrieve a value **safely** using `.get()` so the program does not crash on a missing key.

## 4. Introduction

In Topic 12.4 you learned how to store a list of marks: `[72, 88, 65, 90, 55]`. That works well when all you need is the raw numbers in order. But what if you need to know *which student* each mark belongs to? With a plain list, you have no way to label the values — you can only reach them by position (index 0, index 1, and so on).

A **dictionary** solves that problem. Instead of numbering its slots from zero, a dictionary lets you choose your own labels — called **keys**. Each key is paired with a value. To look up a value, you use its key instead of a position number.

Here is an example. Imagine you are storing information about one student:

```python
student = {"name": "Alice", "score": 88, "grade": "B"}
```

To get Alice's score, you write:

```python
print(student["score"])   # 88
```

No counting, no guessing positions. The label `"score"` goes straight to the right value [1].

Dictionaries are essential in Python because almost all structured data — a student record, a product listing, a response from an AI model — arrives as key-value pairs. When you call the Anthropic API later in Week 12, the response you receive is built from dictionaries. Understanding dictionaries now means you will be able to read and use that response without confusion [2][3].

## 5. Core Concepts

### 5.1 What a Dictionary Is

A **dictionary** is a Python value that stores an unordered collection of **key-value pairs** [1]. Think of it like an actual paper dictionary: you look up a word (the key) and find its definition (the value). You do not have to flip through every page in order — you jump straight to the word you want.

**Key vocabulary:**

- **Dictionary** — a Python value that maps keys to values. Created with curly braces `{` and `}`.
- **Key** — the label you use to look something up. Keys must be unique inside one dictionary (no duplicates) and are usually strings. You can also use integers as keys, but strings are most common for beginners [1].
- **Value** — the data stored under a key. A value can be any Python type: a string, an integer, a boolean, or even a list.
- **Key-value pair** — one key and its associated value, written together as `key: value` and separated from other pairs by a comma.

Creating a dictionary:

```python
student = {"name": "Alice", "score": 88, "grade": "B"}
```

Breaking this down:

- `{` — opens the dictionary.
- `"name": "Alice"` — first key-value pair. Key is `"name"`, value is `"Alice"`.
- `,` — separates pairs.
- `"score": 88` — second pair. Key is `"score"`, value is the integer `88`.
- `"grade": "B"` — third pair.
- `}` — closes the dictionary.

You can also create an empty dictionary and fill it in later:

```python
config = {}   # empty dictionary — zero pairs right now
```

This is the dictionary equivalent of starting with an empty list [1][2].

### 5.2 Accessing a Value by Key

To read one value from a dictionary, write the dictionary name followed by the key inside square brackets [1]:

```python
student = {"name": "Alice", "score": 88, "grade": "B"}

print(student["name"])    # Alice
print(student["score"])   # 88
print(student["grade"])   # B
```

This looks similar to accessing a list item by index, but there is an important difference:

| | List | Dictionary |
|---|---|---|
| How you reach a value | By **position number** (index) | By **label** (key) |
| What happens if label/position is missing | `IndexError` | `KeyError` |
| Order matters? | Yes — order is fixed | No — pairs have no guaranteed order |

If you ask for a key that does not exist, Python raises a `KeyError`:

```python
print(student["age"])   # KeyError: 'age'
```

You will learn the safe way to handle this in Section 5.5 [1].

### 5.3 Adding and Modifying Key-Value Pairs

**Adding a new pair** works by assigning a value to a key that does not yet exist in the dictionary [1][2]:

```python
student = {"name": "Alice", "score": 88}
student["grade"] = "B"          # adds a new key "grade" with value "B"
print(student)
# {"name": "Alice", "score": 88, "grade": "B"}
```

**Modifying an existing value** uses exactly the same syntax — you assign to a key that already exists:

```python
student["score"] = 95           # updates the existing "score" key
print(student["score"])         # 95
```

Python checks whether the key exists. If it does, the value is updated. If it does not, a new pair is created. The syntax is identical for both operations [1].

This is different from lists. With a list you must use `append()` to add a new slot; you cannot write `marks[5] = 99` on a five-item list because index 5 does not exist. With a dictionary, you can freely add any new key at any time [1][2].

### 5.4 Checking Whether a Key Exists

Before reading a key you are not sure about, you can check whether it is there using the `in` keyword [1][3]:

```python
student = {"name": "Alice", "score": 88}

if "score" in student:
    print("Score found:", student["score"])
else:
    print("No score recorded")
```

Output:

```
Score found: 88
```

`"score" in student` returns `True` if `"score"` is a key in the dictionary, `False` if it is not. This is the same `in` keyword you already know from `for item in list` — here it is used as a membership test, not a loop [1][3].

Checking first and then reading is a safe pattern, but Python also provides a single-step version — see Section 5.5.

### 5.5 Getting a Value Safely with `.get()`

`.get()` is a dictionary operation that looks up a key and returns its value, but **does not crash if the key is missing** [1]. Instead, it returns a default value you choose.

```python
student = {"name": "Alice", "score": 88}

grade = student.get("grade", "Not assigned")
print(grade)    # Not assigned — because "grade" is not in the dictionary

score = student.get("score", 0)
print(score)    # 88 — the key exists, so the actual value is returned
```

Syntax:

```python
dictionary.get("key", default_value)
```

- First argument: the key to look up.
- Second argument: what to return when the key is missing (the **default**).
- If the second argument is left out and the key is missing, `.get()` returns `None` — a special Python value meaning "nothing here" [1][3].

Use `.get()` whenever you are reading data that might be incomplete — for example, a student record that may not always have a `"grade"` field, or an API response that may not always include an optional field [1][2].

**`None`** — a Python value that means "nothing" or "no value". You first saw this as the implicit return of a function that has no `return` statement (Topic 12.2). It appears here again as the default when `.get()` finds nothing.

### 5.6 Iterating Over a Dictionary

Dictionaries support three iteration patterns. Choose the one that matches what you need [1][3].

---

**Pattern A — Iterate over keys only:**

```python
student = {"name": "Alice", "score": 88, "grade": "B"}

for key in student:
    print(key)
```

Output:

```
name
score
grade
```

When you write `for key in dictionary:`, Python gives you the keys one at a time. The variable name `key` is just a convention — you can use any name [1].

---

**Pattern B — Iterate over values only, using `.values()`:**

```python
for value in student.values():
    print(value)
```

Output:

```
Alice
88
B
```

`.values()` gives you the values without the keys [1][3].

---

**Pattern C — Iterate over both key and value together, using `.items()`:**

```python
for key, value in student.items():
    print(key, "→", value)
```

Output:

```
name → Alice
score → 88
grade → B
```

`.items()` gives you each pair as two variables at once — `key` and `value`. This is the most commonly used iteration pattern when you need to process the full record [1][2][3].

---

| You need | Pattern | Syntax |
|---|---|---|
| Just the keys | Keys | `for key in dict:` |
| Just the values | Values | `for value in dict.values():` |
| Both key and value | Items | `for key, value in dict.items():` |

### 5.7 Counting Pairs with `len()`

`len()` works on dictionaries exactly as it does on lists — it returns the number of key-value pairs [1][2]:

```python
student = {"name": "Alice", "score": 88, "grade": "B"}
print(len(student))   # 3
```

Three pairs means `len()` returns `3`. This reuses the same `len()` function you already know from Topic 12.4 — Python's built-in functions work across many types of values.

## 6. Implementation

### Worked Example: A Student Record

**Goal:** build a student record dictionary, fill it in, check it, iterate over it, and use `.get()` safely.

This pattern directly mirrors what you will do when you parse an API response later in Week 12 — the response arrives as structured key-value data, and you read specific fields by name [1][2].

---

**Step 1 — Create the dictionary.**

```python
student = {"name": "Alice", "score": 88}
```

Two pairs exist: `"name"` and `"score"` [1].

---

**Step 2 — Add a new field.**

```python
student["grade"] = "B"
print(student)
# {"name": "Alice", "score": 88, "grade": "B"}
```

The dictionary now has three pairs [1][2].

---

**Step 3 — Update an existing field.**

```python
student["score"] = 92
print(student["score"])   # 92
```

The `"score"` key already exists, so its value is overwritten [1].

---

**Step 4 — Check for a key before reading it.**

```python
if "grade" in student:
    print("Grade:", student["grade"])
else:
    print("No grade assigned")
```

Output:

```
Grade: B
```

---

**Step 5 — Use `.get()` for a field that might be missing.**

```python
status = student.get("status", "active")
print(status)   # active — "status" was never added
```

No crash. The default `"active"` is returned [1][3].

---

**Step 6 — Iterate and print every field.**

```python
for key, value in student.items():
    print(key, ":", value)
```

Output:

```
name : Alice
score : 92
grade : B
```

---

**Complete program:**

```python
# Build and populate
student = {"name": "Alice", "score": 88}
student["grade"] = "B"
student["score"] = 92

# Safe read
status = student.get("status", "active")

# Print every field
print("Student record:")
for key, value in student.items():
    print(" ", key, ":", value)
print("Status:", status)
print("Total fields:", len(student))
```

Output:

```
Student record:
  name : Alice
  score : 92
  grade : B
Status: active
Total fields: 3
```

### Building a Dictionary from a List

A common pattern is to take a list of values and build a dictionary from them — for example, pairing student names with their scores:

```python
names  = ["Alice", "Bob", "Carol"]
scores = [92, 78, 85]

grade_book = {}

for i in range(len(names)):
    grade_book[names[i]] = scores[i]

print(grade_book)
# {"Alice": 92, "Bob": 78, "Carol": 85}
```

This uses the `range(len())` pattern from Topic 12.4 to step through both lists at the same index and build a new dictionary one pair at a time [1][2][3].

## 7. Real-World Patterns

Dictionaries appear in almost every Python program that deals with structured data. Here are three patterns you will use directly in this course [1][2][3].

**Pattern 1 — Storing a record with named fields.**

When a system needs to hold several pieces of information about one thing, a dictionary is the natural container:

```python
product = {
    "id": "P001",
    "name": "Laptop",
    "price": 799.99,
    "in_stock": True
}

print(product["name"])    # Laptop
print(product["price"])   # 799.99
```

Each field has a clear name. Reading `product["price"]` is far more readable than `product[2]` would be on a list [1][2].

**Pattern 2 — Configuration and settings.**

Programs often store settings as a dictionary so any part of the code can look up a setting by name:

```python
config = {
    "model": "claude-sonnet-4-5",
    "max_tokens": 1024,
    "temperature": 0.7
}

print("Using model:", config["model"])
```

When you call the Anthropic API later in Week 12, the parameters you pass — which model to use, how long the response can be — are structured exactly like this [2][3].

**Pattern 3 — Parsing a structured response.**

When an external service sends you data, it usually arrives as key-value pairs. A simplified example of what an AI API response looks like as a Python structure:

```python
response = {
    "model": "claude-sonnet-4-5",
    "stop_reason": "end_turn",
    "text": "Here is a summary of your document.",
    "status": "success"
}

print("Model used:", response["model"])
print("Stop reason:", response["stop_reason"])
reply_text = response.get("text", "")
print("Reply:", reply_text)
```

This is exactly the pattern you will use when you call an LLM (Large Language Model) — you will call one later in Week 12 — and read its reply. The field names in that response are keys; reading them by name is reading a dictionary [1][2][3].

Nested dictionaries (covered in a later topic) allow values to themselves be dictionaries, enabling richer response structures.

## 8. Best Practices

**Do:**

- **Use descriptive string keys.** `student["score"]` tells you exactly what you are reading. `student[0]` on a list does not [1][2].
- **Use `.get()` when a key might be absent** — especially when reading data from an external source (a file, an API, user input). A missing key should not crash your program [1][3].
- **Check `"key" in dict` before reading** when you need to take different actions depending on whether the key exists (e.g., log a warning, use a fallback) [1].
- **Use `.items()` when you need both the key and the value in a loop.** Fetching the key first and then looking up the value (`for key in dict: value = dict[key]`) works but is unnecessarily verbose [1][3].
- **Use `len()` to count pairs**, just as you use it to count list items. The same built-in function, the same mental model [1][2].

**Do not:**

- **Do not use a list when labels matter.** If you catch yourself writing `record[0]` to mean "name" and `record[1]` to mean "score", switch to a dictionary [1].
- **Do not write logic that depends on key order.** In Python, dictionaries remember the order you added items, but code that relies on a specific key order is fragile. Access values by key, not by position [1][2].
- **Do not use a list as a dictionary key.** Keys must be **immutable** — a value that cannot be changed after it is created. Python strings and integers are immutable; lists are not. If you try to use a list as a key, Python raises a **`TypeError`** — an error Python raises when you use a value in the wrong way. Stick to strings or integers as keys [1][3].
- **Do not read a key without checking first** if the data might be incomplete. Use `.get()` or `in` instead of assuming the key is always there [1].

| Situation | Right approach | Common mistake |
|---|---|---|
| Read a value you know exists | `dict["key"]` | `dict.get("key")` — unnecessarily obscures intent |
| Read a value that might be missing | `dict.get("key", default)` | `dict["key"]` — crashes on missing key |
| Add or update a value | `dict["key"] = value` | Trying `append()` — `append` belongs to lists, not dicts |
| Loop over everything | `for key, value in dict.items():` | `for key in dict: value = dict[key]` — verbose |
| Count the pairs | `len(dict)` | Manually counting with a variable |

## 9. Hands-On Exercise

Open your Colab notebook.

1. Create a dictionary called `person` with three keys: `"name"` (your name as a string), `"age"` (an integer), and `"city"` (a string).
2. Print the value of `"name"`, then print the value of `"age"`.
3. Add a new key `"country"` with the value `"India"`. Print `len(person)` — you should see `4`.
4. Change the `"age"` value to a different number. Print `person["age"]` to confirm.
5. Use `"email" in person` to check whether `"email"` is a key. It is not — print `"No email"` in the `else` branch.
6. Use `.get()` to read `"phone"` with a default of `"unknown"`. Print the result.
7. Write a `for key, value in person.items():` loop that prints every field on its own line.

## 10. Key Takeaways

- A **dictionary** stores key-value pairs inside curly braces: `{"name": "Alice", "score": 88}`. Unlike a list, you reach values by label (key), not by position.
- Access a value with `dict["key"]`. Add or update a value with `dict["key"] = new_value` — the same syntax handles both cases.
- Use `"key" in dict` to check whether a key exists before reading it, or use `dict.get("key", default)` to read safely in one step.
- Iterate over a dictionary with `for key in dict:` (keys only), `for value in dict.values():` (values only), or `for key, value in dict.items():` (both — the most common pattern).
- `len(dict)` counts the number of key-value pairs, just as `len(list)` counts items.
- Dictionaries are the natural container for structured data — student records, API configuration, and AI model responses all use the same key-value shape.

## 11. Next Steps

_System-derived from the next entry in curriculum/sequence.md._
