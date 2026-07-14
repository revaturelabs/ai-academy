---
topic_id: "11.3"
title: "Variables — naming and storing values"
position_in_module: 1
generated_at: "2026-06-12T00:30:00Z"
resource_count: 5
---

# 1. Variables — naming and storing values — Topic Corpus

## 2. Prerequisites

This topic builds directly on:

- **11.1** — Python's role: the orchestration layer. Students already know what Python is, that it is interpreted, and that code runs in Google Colab.
- **11.2** — Notebooks, code cells, and the Colab environment. Students know how to open a notebook, write in a code cell, and run a cell with Shift+Enter.

No prior programming knowledge is assumed beyond topics 11.1 and 11.2.

## 3. Learning Objectives

By the end of this topic, students will be able to:

- Explain what a variable is using a concrete everyday analogy.
- Assign a value to a variable using the `=` operator and identify what each part of an assignment statement means.
- Name the four basic data types in Python — `str`, `int`, `float`, and `bool` — and give an example of each.
- Use `type()` to check the data type of a value or variable.
- Apply Python's naming rules to write valid, descriptive variable names in snake_case.
- Demonstrate that a variable can be reassigned to a new value during a program.

## 4. Introduction

Before a Python program can do anything useful — calculate a grade, call an AI model, or process a document — it needs somewhere to keep the pieces of information it is working with. Where does it store a student's name? How does it remember a score? How does it know whether a student is currently enrolled?

The answer, in Python and in virtually every programming language, is **variables** [3].

Think about how you use a sticky note. You pick up the note, write something on it — a name, a number, a reminder — and stick it somewhere you will see it again. Later, you can read what you wrote, change it, or stick a new note in its place. A variable in Python works in almost exactly the same way: you give a piece of information a name, and Python holds onto it so you can use it again whenever you need it [3][5].

This topic is about the most fundamental act in programming: naming a value and storing it. Everything you will build in this course — from the grade-average script in the lab this week to AI pipelines in weeks 12 and 13 — starts with this single operation.

> **Note:** Code examples in this topic use `print()` to show output. The `print()` function will be explained fully in topic 11.4; for now, just know that `print(something)` displays the value of `something` in the output area of your notebook.

## 5. Core Concepts

### 5.1 What is a variable?

A **variable** is a named label that points to a value stored in the computer's memory [3][4]. The name is chosen by you, the programmer. The value is whatever piece of information you want to keep track of.

This is the key mental model: a variable is **not** a box that contains a value. It is more like a label on a sticky note that you have placed on top of a value. At any moment, you can read what the sticky note says, remove the note and put it on a new value, or throw it away entirely [3].

In Python, you create a variable — and point it at a value — using the **assignment operator**, which is the `=` sign [1][3]:

```python
student_name = "Alice"
```

After this line runs:
- `student_name` is the variable name (the label you chose).
- `"Alice"` is the value (the piece of information the label is pointing to).
- `=` is the assignment operator: it says "make this name point to this value" [3][5].

The `=` sign in Python does **not** mean "these two things are equal" the way it does in mathematics. It means "assign the value on the right to the name on the left" [3]. This is an important distinction. `student_name = "Alice"` is an instruction — it tells Python to do something. It is not a statement of fact.

### 5.2 The assignment operator — reading the line correctly

Every assignment statement has the same structure:

```
variable_name = value
```

Read it from right to left: "evaluate whatever is on the right, then point the name on the left at that result." [3]

```python
age = 20
```

Python evaluates the right side (the number `20`), then creates the label `age` pointing to it. The next time you write `age` anywhere in your program, Python looks up the label and finds `20` [3][5].

A variable that has never been assigned does not exist yet. If you try to use a variable name that Python has never seen, it will produce a runtime error — exactly the kind of error described in topic 11.1 [1].

### 5.3 The four basic data types

Not all values are the same kind of thing. The number `20` is different from the text `"Alice"`. Python uses the idea of a **data type** (often shortened to **type**) to distinguish between different kinds of values [2][4].

There are four basic data types you will use constantly [2][4]:

---

#### `str` — text (string)

A **string** (`str`) is a sequence of characters — letters, digits, spaces, punctuation, anything you can type [1][2]. Strings are always wrapped in quotation marks (either single `'` or double `"` — Python accepts both).

**Everyday analogy:** A string is like a sticky note with words written on it. The note can say anything — a name, a sentence, a question — but it is always treated as text, not as a number to calculate with [4][5].

```python
student_name = "Alice"
course_title = "Python for AI"
```

A number written inside quotation marks is still a string, not a number:

```python
student_id = "20240071"   # this is text, not a number
```

---

#### `int` — whole numbers (integer)

An **integer** (`int`) is a whole number — no decimal point [1][2].

**Everyday analogy:** An integer is like counting whole items — 6 eggs, 3 marks on a test, 12 students in a room. You cannot have 6.5 eggs; it is always a complete, whole count [4].

```python
age = 20
marks_out_of = 100
student_count = 3
```

---

#### `float` — numbers with a decimal point (floating-point)

A **float** is a number that can have a decimal point — it can represent fractional or continuous values [1][2].

**Everyday analogy:** A float is like a measurement — 1.75 metres tall, 73.5 kg, a grade average of 87.5. These values fall between whole numbers, so they need a decimal representation [4].

```python
height_m = 1.75
weight_kg = 73.5
grade_average = 87.5
```

---

#### `bool` — True or False (Boolean)

A **Boolean** (`bool`) holds exactly one of two values: `True` or `False` [2][4]. Note the capital letters — `True` and `False` must be written with a capital first letter in Python; `true` and `false` (lowercase) do not work [2].

**Everyday analogy:** A bool is like a light switch. It is either on (`True`) or off (`False`). There is no in-between [4][5].

```python
is_enrolled = True
has_submitted = False
```

Booleans become important when your program needs to make a decision — "if the student is enrolled, do this; otherwise, do that." Conditionals (if/else) are covered in topic 11.5.

---

### 5.4 Using `type()` to check a data type

Python provides a built-in function called `type()` that tells you what data type a value or variable is [1][2]. You will use this constantly when you are unsure what kind of value you are working with.

```python
student_name = "Alice"
age = 20
grade_average = 87.5
is_enrolled = True

print(type(student_name))    # <class 'str'>
print(type(age))             # <class 'int'>
print(type(grade_average))   # <class 'float'>
print(type(is_enrolled))     # <class 'bool'>
```

The output — `<class 'str'>`, `<class 'int'>`, `<class 'float'>`, `<class 'bool'>` — tells you the type of each variable [2]. Ignore the word `class` for now; it is just Python's way of reporting the type. What matters is the name after it: `str`, `int`, `float`, or `bool`.

You can also call `type()` directly on a value without a variable:

```python
print(type("hello"))    # <class 'str'>
print(type(42))         # <class 'int'>
print(type(3.14))       # <class 'float'>
print(type(True))       # <class 'bool'>
```

Getting into the habit of checking types early prevents a very common class of errors: trying to do arithmetic with a string, or treating a number as if it were text [3][4].

### 5.5 Naming rules — what makes a valid variable name

Python has strict rules about what names you are allowed to give a variable [1][3][5]:

**Rules you must follow:**
1. A variable name may contain letters (`a`–`z`, `A`–`Z`), digits (`0`–`9`), and underscores (`_`).
2. A variable name **cannot start with a digit**. `3marks` is invalid; `marks_3` is valid [3][5].
3. A variable name **cannot contain spaces**. `student name` is invalid; `student_name` is valid [3][5].
4. Variable names are **case-sensitive**: `age`, `Age`, and `AGE` are three different variables [3].
5. You cannot use Python's **reserved words** (also called keywords) as variable names. Words like `if`, `for`, `True`, `False`, `and`, `not`, `import`, `return` already have special meanings in Python and cannot be used as labels [1][3].

**Conventions you should follow:**
- Use **snake_case**: all lowercase letters, with underscores between words. `student_name`, `grade_average`, `is_enrolled` [3][5].
- Choose **descriptive names** that say what the variable holds. `grade_average` is clear; `x` or `g` is not [3][5].
- Avoid single-letter names except as simple counters (a practice covered in later topics).

**Examples — valid and invalid:**

| Name | Valid? | Reason |
|---|---|---|
| `student_name` | Yes | Lowercase, snake_case, descriptive |
| `age` | Yes | Clear and simple |
| `grade_average` | Yes | Descriptive, snake_case |
| `3marks` | **No** | Starts with a digit |
| `student name` | **No** | Contains a space |
| `if` | **No** | Reserved keyword |
| `StudentName` | Yes (but avoid) | Valid syntax, but not snake_case convention |

Following naming conventions matters more than you might expect. Code is read far more often than it is written — by you later, by teammates, by AI tools helping you [3]. Readable names make everything easier.

### 5.6 Reassignment — variables can change

A variable's value is not fixed. You can point a variable at a new value at any time simply by assigning to it again [1][3][5]:

```python
score = 55
print(score)   # 55

score = 72
print(score)   # 72
```

After the second assignment, `score` points to `72`. The value `55` is no longer accessible through `score`. Python just updated where the label points [3].

You can also change the type of a variable's value by reassigning it — Python allows a variable that held an integer to later hold a string, for example [3][4]. This flexibility is part of why Python is described as a **dynamically typed** language: the type is associated with the value, not with the variable name itself. You will not need to declare "this variable holds integers" in advance, the way some other languages require [3]. For now, just know that reassignment is allowed and normal.

```python
status = "enrolled"
print(status)   # enrolled

status = False
print(status)   # False
```

While dynamic typing is flexible, using a variable for fundamentally different kinds of values at different points in the same program can make code confusing to read. Good practice is to keep a variable's role consistent [3][5].

## 6. Implementation

This section shows a complete example that uses all four data types and the naming practices from section 5. Read through it as a whole picture, then look at it one line at a time.

```python
# Student record — variables for one student

student_name   = "Alice"        # str   — the student's name
student_id     = "20240071"     # str   — an ID treated as text, not a number
age            = 20             # int   — whole years
grade_average  = 87.5           # float — calculated average mark
is_enrolled    = True           # bool  — currently registered?

# Check the type of each variable
print(type(student_name))    # <class 'str'>
print(type(student_id))      # <class 'str'>
print(type(age))             # <class 'int'>
print(type(grade_average))   # <class 'float'>
print(type(is_enrolled))     # <class 'bool'>
```

Work through this example in a code cell in Google Colab (as introduced in topic 11.2) [2][5]:

1. Open a new code cell.
2. Copy the code above, or type it yourself (typing it is better for learning).
3. Press Shift+Enter to run the cell.
4. Read the five lines of type output and match each line to the variable that produced it.
5. Change `grade_average` to an integer (e.g., `grade_average = 87`) and re-run. What does `type()` report now?

This pattern — assign a variable, then immediately check its type — is a useful habit when you are starting out [3][4].

**The grade-average lab script (a preview)**

The lab activity this week asks you to write a script that takes a student's name and three marks, then outputs the average and a letter grade. The first step of building that script is defining the variables you will need. A well-chosen set of starting variables might look like this:

```python
student_name = "Alice"
mark_1 = 75
mark_2 = 88
mark_3 = 91
```

The values are stored. The next step — doing arithmetic with those values and deciding which grade to assign — requires operators and conditionals, which arrive in topics 11.4 and 11.5.

## 7. Real-World Patterns

Variables are not a beginner's training exercise. They are how every piece of data enters and moves through a real Python program [3][4].

**In an AI pipeline**, the outputs from an AI model are always captured in variables before the next step does anything with them [4]. A typical interaction with a language model's API might look like:

```python
user_question = "What is photosynthesis?"
model_response = call_ai_model(user_question)   # hypothetical — API calls covered in week 12
```

Here, `user_question` is a `str` variable holding what the user typed. `model_response` is a variable that will hold whatever the AI model returns. Every subsequent step of the pipeline — checking whether the response is long enough, extracting a specific part of it, logging it — will work with the `model_response` variable [4].

**In data processing**, variables hold intermediate results as the program progresses. A program reading three exam marks, calculating their average, and classifying the result will store: the three raw marks (three `int` or `float` variables), the calculated average (a `float`), and the final grade letter (a `str`) [3][4]. Each variable is a checkpoint in the pipeline.

**In configuration**, boolean variables are especially common. A program might have:

```python
debug_mode = True
save_to_file = False
```

These two `bool` variables control the program's behaviour: if `debug_mode` is `True`, extra information is printed; if `save_to_file` is `False`, output goes to the screen rather than a file. Changing one line of code changes the whole behaviour of the program [4][5].

## 8. Best Practices

**Choose names that explain themselves.** `grade_average` tells you exactly what it holds. `g`, `x`, or `temp` do not — and you will forget what they mean within minutes [3][5]. When your program gets longer, or when you ask an AI assistant to help you understand your own code, clear names make the difference between a readable program and a confusing one.

**Use snake_case consistently.** Python's community convention is clear: lowercase, underscores between words [3]. Following it means your code looks the same as the examples in documentation, tutorials, and AI-generated suggestions. Breaking it means friction everywhere.

**Do not reuse variable names for unrelated things.** If you used `score` to hold an exam result, do not later reuse it to hold a student ID. Create a new, properly named variable instead [3][5]. Dynamic typing allows you to reuse names — but doing so for different purposes makes code very hard to follow.

**Check types early when something does not behave as expected.** If Python is complaining that it cannot do arithmetic, or that a comparison is not working the way you expected, the first thing to check is what type the variable actually holds [3][4]. `type(my_variable)` is the fastest debugging tool for this class of problem.

**Keep the value and the type consistent with the name's meaning.** A variable named `student_count` should hold an `int`, not a `float` or a string. The name advertises the type implicitly [3][5]. Violating this expectation surprises the next person (or AI assistant) reading your code.

## 9. Hands-On Exercise

This exercise is a warm-up for the lab activity. It takes about 10 minutes to complete in a Google Colab notebook [2].

**Exercise: Student record in five lines**

1. Open a new code cell in Google Colab.
2. Create exactly five variables: one for a student's name (`str`), one for their age (`int`), one for their overall grade average as a decimal (`float`), and one for whether they have completed their assignment this week (`bool`). Choose one more variable of any type for a detail about the student that you pick yourself.
3. Use `type()` and `print()` to display the type of each variable. Confirm that the output matches what you expected.
4. Reassign the grade-average variable to a new value (different from your original). Call `type()` again. Did the type change?
5. Try creating a variable with an invalid name — for example, `3rd_mark = 90` — and run the cell. Read the error message. Write a comment in the cell explaining what the error says in plain English.

**Discussion question (text cell):** In the lab activity for this week, you will need variables for a student's name and three individual marks. What names would you give those four variables? Why did you choose those names?

## 10. Key Takeaways

- A **variable** is a named label that points to a value in memory. The `=` operator assigns a value to a name — it does not test equality [3][5].
- Python has four fundamental data types: **`str`** (text), **`int`** (whole numbers), **`float`** (decimal numbers), and **`bool`** (`True` or `False`). Every value you store in a variable has one of these types [2][4].
- Use `type()` at any time to find out what data type a variable or value holds — this is one of the most useful early-stage debugging tools [1][2].
- Variable names must follow Python's rules: start with a letter or underscore, no spaces, no reserved keywords. By convention, use **snake_case** and choose **descriptive names** [3][5].
- Variables can be **reassigned** — pointed at a new value — at any point. Python is dynamically typed, so the new value can even be a different type, though good practice is to keep a variable's role consistent throughout a program [3][4].

## 11. Next Steps

_System-derived from the next entry in curriculum/sequence.md._
