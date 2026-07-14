---
topic_id: "12.1"
title: "Functions — named, reusable blocks of logic"
position_in_module: 1
generated_at: "2026-06-13T00:00:00Z"
resource_count: 3
---

# 1. Functions — Named, Reusable Blocks of Logic — Topic Corpus

## 2. Prerequisites

This topic builds directly on concepts from Week 11:

- **11.3 — Variables:** you know how to name and store a value.
- **11.4 — Data types:** you know strings, integers, floats, and booleans.
- **11.5 — If / else:** you can write decision logic in code.
- **11.6 — For loops:** you can repeat an action across a list.

No other background is required. If you are comfortable with the four topics above, you are ready.

## 3. Learning Objectives

By the end of this topic you will be able to:

1. Explain in plain words what a Python function is and why functions exist.
2. Write a function using the `def` keyword with correct Python syntax.
3. Call (run) a function by name and observe when the code inside it executes.
4. Choose a clear, descriptive name for a function that signals what it does.
5. Recognise the difference between *defining* a function and *calling* a function.
6. Identify where functions appear in real AI-adjacent Python scripts.

## 4. Introduction

Imagine you work in a kitchen. Every morning you make toast: put bread in the toaster, push the lever, wait, take the toast out. You do not think through those steps from scratch each morning — you just know the routine. A **function** in Python is the same idea: you write a set of steps once, give that set a name, and from then on you just say the name to make Python run those steps.

Before you learned functions, your programs were a straight line of instructions read from top to bottom. That works fine for ten lines. But a real AI script might need to clean a piece of text in five different places. Without functions you copy those five cleaning steps into each place. If you later spot a mistake, you have to fix it in five places. With a function, you fix it once.

Functions are one of the most important building blocks in any programming language [1]. Python makes them easy to write and read — the same plain-English approach you have seen throughout Week 11 continues here [2].

Two things you will learn in the next topics — how to pass data into a function and how to get a result back — are intentionally left for Topic 12.2. Focus here on the shape of a function and the act of calling it.

## 5. Core Concepts

### 5.1 What a Function Is

**Function** — a named, reusable block of code that you write once and can run as many times as you like just by saying its name.

Think of it as a recipe card. The card has a title ("Make Toast"). The card has a list of steps. When someone reads the card and follows the steps, that is the function *running*. The card sitting in a drawer, unread, is the function *defined but not yet called*.

Every Python function has three parts [1]:

- **The name** — what you call the block. You pick this. It should describe what the function does.
- **The body** — the indented lines of code that run when you call the function.
- **A call** — the line elsewhere in your code that actually triggers the body to run.

### 5.2 The `def` Keyword

In Python, you create a function with the keyword `def` (short for "define") [2]. The format is always:

```
def function_name():
    # body — indented by 4 spaces
    step one
    step two
```

**`def`** — the Python keyword that signals "I am about to define a new function. The name that follows is how I will call it."

The colon (`:`) at the end of the `def` line is required — Python uses it to know the header line is finished and the body is about to begin [1].

**Indentation** — the four spaces before each line in the body. Indentation is how Python knows which lines belong to the function. A line that goes back to zero indentation is outside the function.

Example — a function that prints a greeting:

```python
def greet():
    print("Hello, welcome to the Python course!")
```

Right now, running the code above does nothing visible. The function is defined — the recipe card exists — but nobody has read it yet.

### 5.3 Calling a Function

**Function call** — a line of code that tells Python "run this function now."

To call a function, write its name followed by parentheses:

```python
greet()
```

When Python sees `greet()`, it jumps to the `def greet():` block, runs every indented line inside it (in this case one `print` statement), and then returns to the line after `greet()` and continues.

Full working example:

```python
def greet():
    print("Hello, welcome to the Python course!")

greet()          # first call — runs the body once
greet()          # second call — runs the exact same body again
greet()          # third call — still the same body
```

Output:

```
Hello, welcome to the Python course!
Hello, welcome to the Python course!
Hello, welcome to the Python course!
```

Three calls, three prints — and the code inside `greet()` was written only once. That is reuse [1][2].

### 5.4 Definition vs. Call — a Critical Distinction

This is the most common source of confusion for beginners, so pay close attention.

| Moment | What happens | Code |
|---|---|---|
| **Definition** (`def`) | Python reads the function and stores it in memory. No code runs yet. | `def greet():` ... |
| **Call** | Python actually runs the body. | `greet()` |

A function that is defined but never called does nothing. A call for a function that has not been defined yet causes a `NameError` crash. Definition must come first; call comes after.

```python
# This crashes — call before definition
greet()            # NameError: name 'greet' is not defined

def greet():
    print("Hello!")
```

```python
# This works — definition before call
def greet():
    print("Hello!")

greet()            # prints: Hello!
```

The rule: **write your `def` block before the line that calls it** [1].

### 5.5 Naming Conventions for Functions

Choosing a good name is not optional decoration — it is how you (and your teammates) understand code without running it [1].

Python's official style guide (PEP 8 — the community document that describes recommended Python coding conventions) says:

- Use **lowercase letters**.
- Separate words with **underscores** (`_`), not spaces or capital letters.
- The name should be a **verb or verb phrase** — functions *do* things.

| Good names | Why good |
|---|---|
| `greet()` | Clearly signals: "this greets someone." |
| `print_summary()` | Verb + noun — prints a summary. |
| `load_data()` | Verb + noun — loads data. |
| `calculate_average()` | Precisely states the action. |

| Avoid | Why to avoid |
|---|---|
| `x()` | No meaning at all. |
| `doStuff()` | camelCase style — not Python convention. |
| `function1()` | Generic — tells you nothing about what it does. |
| `Data()` | Starts with capital — reserved by convention for class names. |

A quick test: if you read just the function name and immediately know what it does, the name is good [1][3].

### 5.6 The Body Can Contain Anything You Already Know

The body of a function is ordinary Python code — the same code you wrote in Week 11. You can use variables (11.3), data types (11.4), `if`/`else` decisions (11.5), and `for` loops (11.6) inside a function body.

```python
def show_week():
    week_number = 12
    course_name = "Python for AI"
    print("Week:", week_number)
    print("Course:", course_name)

show_week()
```

There is nothing new *inside* the body — the only new ideas are the `def` line, the name, and the act of calling. Everything inside follows the same rules as before.

### 5.7 Code Reuse — Why Functions Exist

**Code reuse** — writing a piece of logic once and using it in many places, instead of copying the same code repeatedly.

Consider a script that prints a section separator line. Without a function:

```python
print("---")
# ... some other output ...
print("---")
# ... more output ...
print("---")
```

Three identical `print` statements scattered through the code. If you decide dashes should become equals signs, you edit three lines. With a function:

```python
def print_separator():
    print("---")

print_separator()
# ... some other output ...
print_separator()
# ... more output ...
print_separator()
```

Change `"---"` to `"==="` in one place and all three calls update automatically.

Real benefits of reuse [1][2]:

1. **Fix once.** A bug in the logic is fixed in one place, not ten.
2. **Read faster.** `print_separator()` tells you more at a glance than repeated `print("---")` lines.
3. **Test once.** You verify the function works once and trust every call thereafter.

## 6. Implementation

Writing and calling a Python function follows these ordered steps.

**Step 1 — Write the spec in plain English first (11.7 discipline).**

Before touching `def`, state in a comment what the function is supposed to do. One sentence is enough.

```python
# greet_user: print a welcome message to the screen
```

**Step 2 — Write the `def` line.**

```python
def greet_user():
```

Check: name is lowercase with underscores, ends with `():`.

**Step 3 — Write the body, indented by 4 spaces.**

```python
def greet_user():
    print("Welcome to the AI course!")
```

Check: every line in the body is indented the same amount.

**Step 4 — Call the function.**

Put the call *after* the definition, at zero indentation (back to the left margin).

```python
def greet_user():
    print("Welcome to the AI course!")

greet_user()
```

**Step 5 — Run and verify.**

Expected output:
```
Welcome to the AI course!
```

If you see `NameError`, the most likely cause is the call appearing before the `def`. Move the call below the definition.

**Step 6 — Call it more than once to confirm reuse.**

```python
greet_user()
greet_user()
```

Both calls produce the same output without duplicating the `print` statement. You have confirmed reuse [2][3].

## 7. Real-World Patterns

Functions appear in every Python AI script you will encounter in this course [1][3].

**Pattern 1 — Wrapping repeated output steps.**
Scripts that process data often print headers, separators, and summaries in multiple places. A function like `print_report_header()` or `print_separator()` removes duplication and keeps the main logic readable.

**Pattern 2 — Data loading.**
A function like `load_student_records()` appears at the top of scripts that process files (as in the lab activity for this week). The loading logic is written once; the function is called wherever the data is needed.

**Pattern 3 — Readable top-level flow.**
Professional Python scripts often read like a short list of function calls at the bottom of the file — `load_data()`, `check_records()`, `print_summary()`. Each call says exactly one thing. A reader can understand the overall flow at a glance without reading the implementation details [1].

You do not need to build those complete patterns yet. But recognising that functions are the building blocks of every real script helps you read professional Python code without feeling lost.

## 8. Best Practices

**Do:**

- **Name functions as verb phrases.** `calculate_average()`, `load_data()`, `print_report()` — each name tells you the action.
- **Define before calling.** Python reads top to bottom. Definition must come first.
- **Keep indentation consistent.** Four spaces per level. Mixing tabs and spaces causes errors in Python.
- **Write the plain-English spec as a comment above each function** (11.7 discipline). One sentence saying what the function does.
- **Test each function with a call immediately after writing it.** Catch problems early, before you build more code on top.

**Do not:**

- **Do not repeat yourself.** If you write the same block of code twice, that is a signal a function is needed.
- **Do not use vague names.** `do_thing()`, `helper()`, `process()` give no information about what happens.
- **Do not put the call before the `def`.** This always causes a `NameError`.
- **Do not mix tabs and spaces for indentation.** Choose spaces (4) and stick to them throughout your file.

**Common beginner mistake — forgetting the parentheses in the call:**

```python
def greet():
    print("Hi!")

greet      # does nothing — this is just referencing the function name, not calling it
greet()    # this actually runs the function
```

The empty parentheses `()` are required to *call* a function [2].

## 9. Hands-On Exercise

Open a new Colab notebook (as you set up in Topic 11.2).

1. Write a spec comment: `# print_hello: print "Hello from my first function!" to the screen`.
2. Define a function `print_hello` that prints that message.
3. Call `print_hello()` three times in a row.
4. Verify you see the message printed three times.
5. Now write a second function, `print_separator`, that prints `"---"` (a line of dashes).
6. Call `print_hello()`, then `print_separator()`, then `print_hello()` again.
7. Read the output. Notice how the two functions interleave — you controlled the order just by choosing which name to call and when.

Keep both functions in the notebook. You will extend them in the next topic when you learn how to pass data into a function.

## 10. Key Takeaways

- A **function** is a named, reusable block of code. You write the steps once; the name lets you run those steps anywhere, any number of times.
- The `def` keyword *defines* a function. Writing `def` does not run any code yet — it only stores the function in memory.
- A **function call** — the name followed by `()` — is what actually runs the body.
- **Definition must come before the call** in the file. Python reads top to bottom.
- **Names matter.** A function named `calculate_average()` tells you instantly what it does. A function named `x()` tells you nothing. Use lowercase verb phrases with underscores.

## 11. Next Steps

_System-derived from the next entry in curriculum/sequence.md._
