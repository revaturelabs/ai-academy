---
topic_id: 1.2
title: Variables, Identifiers & Types
position_in_module: 2
generated_at: 2026-07-13T00:00:00Z
resource_count: 3
---

# 1. Variables, Identifiers & Types — Topic Corpus

## 2. Prerequisites

- **1.1 The Python Environment** — you should be able to open a Colab notebook, type code in a cell, run it, and use `print()` to see output. That is all you need here.

## 3. Learning Objectives

By the end of this topic you will be able to:

- Create a variable using the assignment operator (`=`) and change its value by reassigning it.
- Apply Python's naming rules and the `snake_case` convention to write legal, readable identifiers.
- Recognize the four basic value types: `int`, `float`, `str`, and `bool`.
- Use the `type()` function to inspect the type of any value.
- Explain, in plain terms, what "dynamic typing" means in Python.

## 4. Introduction

In topic 1.1 you learned to run a cell and print a result. But printing a value once and forgetting it is not very useful. Real programs need to *hold on* to values — a user's name, a price, a count of items — and use them again later.

That is what a **variable** does. It gives a value a name so you can refer to it as many times as you like. Without variables, you would have to type the same literal value everywhere you needed it, and if that value ever changed you would have to hunt down every copy. A variable lets you say "the price" once and reuse it — and change it in one place.

In this topic you will learn how to create variables, the rules for naming them, the four kinds of values you will use most often, and a small tool (`type()`) that tells you what kind of value you are holding. These are the building blocks for everything else in Python — every later topic assumes you can confidently name a value and know what type it is.

## 5. Core Concepts

### 5.1 Variables and assignment

A **variable** is a name that refers to a value. You create one with the **assignment operator**, the single equals sign `=`. The name goes on the left, the value goes on the right:

```python
x = 5
print(x)
```

Output:

```
5
```

Read `x = 5` as "let `x` refer to the value `5`" — *not* as "x equals 5" in the math sense. This distinction matters. In mathematics, `=` states a fact that is either true or false. In Python, `=` performs an *action*: it binds the name on the left to the object on the right [1]. After that line runs, any time you write `x`, Python looks up the value it points to and uses it in place of the name.

Because the right side is evaluated first and then handed to the name, you can put any value there — a plain number, a piece of text, or even the value another variable is already holding:

```python
first = 5
second = first
print(first, second)
```

Output:

```
5 5
```

Here `second = first` does not link the two names together forever. It copies the *current* value of `first` (which is `5`) and gives that to `second`. The name on the left always ends up referring to whatever the right side worked out to be [1].

One more habit worth forming early: the name must exist before you use it. If you try to `print(total)` before you have ever written `total = ...`, Python has no value to look up and reports a `NameError`. A variable comes into being the moment you first assign to it — not before.

### 5.2 Reassignment — changing a variable's value

You are not stuck with the first value. You can **reassign** a variable — give it a new value — at any time by writing another assignment to the same name:

```python
count = 10
print(count)
count = 20
print(count)
```

Output:

```
10
20
```

The second assignment replaces the first. The name `count` now refers to `20`; the old `10` is gone — nothing in your program remembers it anymore. This is completely normal and happens constantly in real programs: a score goes up, a balance goes down, a status changes, a running total grows.

You can even use a variable's *current* value on the right side to compute its *next* value. Python evaluates the whole right side first, using the old value, and only then rebinds the name:

```python
score = 100
score = score + 50
print(score)
```

Output:

```
150
```

Read the middle line as: "take the current value of `score` (100), work out `score + 50` (150), then let `score` now refer to that result." The name `score` is being updated in place from the programmer's point of view, even though under the hood Python just points the name at a new value [1].

### 5.3 Identifiers — naming rules

The name you give a variable is called an **identifier**. Python has firm *rules* about which names are legal, and a separate *convention* about which names are good style. Rules are enforced by Python — break one and your code will not run. Conventions are agreements between programmers — break one and your code still runs, but other people (and future you) will find it harder to read.

**The rules (Python enforces these) [3]:**

- An identifier may contain letters, digits, and the underscore `_`.
- It must **not start with a digit**. `age2` is fine; `2age` is an error.
- It may not contain spaces or punctuation like `-`, `!`, or `$`. So `user-name` is illegal (Python reads the `-` as something else), but `user_name` is fine.
- It must not be a **reserved keyword** (covered in 5.4).

Here is what a broken name looks like:

```python
2age = 30
```

Output:

```
SyntaxError: invalid decimal literal
```

Python refuses to run it. Fix it by starting with a letter or underscore, e.g. `age2`. Notice that a `SyntaxError` stops the code before it does anything at all — Python could not even make sense of the line [3].

### 5.4 Reserved keywords and case sensitivity

**Reserved keywords** are words Python has already claimed for its own grammar — words like `if`, `for`, `class`, `def`, `True`, and `False`. You cannot use them as variable names, because Python needs them to mean their special thing [3]. Trying to name a variable `for`:

```python
for = 5
```

Output:

```
SyntaxError: invalid syntax
```

You do not need to memorize the full keyword list right now. Just know that if a name causes a strange `SyntaxError` and the name is a short common English word, a keyword clash is a likely cause — rename it (for example, `for_loop_count` or `iteration`).

**Case sensitivity:** Python treats uppercase and lowercase letters as different. `score`, `Score`, and `SCORE` are three completely separate variables, with no connection between them [3]:

```python
score = 1
Score = 2
print(score, Score)
```

Output:

```
1 2
```

This is a common source of confusion for beginners, because in everyday writing "Score" and "score" mean the same word. In Python they do not. Pick one spelling for each variable and stay consistent, or you will end up with two variables when you meant one.

### 5.5 The `snake_case` convention

Legal is not the same as good. The official Python style guide, **PEP 8**, says variable names should be lowercase with words separated by underscores — a style called **`snake_case`** [2]. So write `user_name`, not `username`, `UserName`, or `usernm`.

If you have seen another language before, you may know **camelCase** (`userName`, `totalPrice`) — capitalizing each word after the first, with no underscores. That style is common in languages like JavaScript and Java, and Python will happily *run* a camelCase name because it breaks no rule. But it is not the Python convention, and mixing styles in one codebase looks inconsistent to Python programmers. In Python, prefer `snake_case` [2].

Good names also *describe* what the value is. `total_price` tells a reader far more than `tp` or `x`:

```python
total_price = 19.99
print(total_price)
```

Output:

```
19.99
```

Clear names are one of the cheapest ways to make code easy to read, and they cost you nothing but a few extra keystrokes.

### 5.6 Values and types

Every value in Python has a **type** — a category that says what kind of thing the value is and what you can do with it. You will use four basic types constantly:

- **`int`** — an integer, a whole number with no decimal point: `5`, `0`, `-42`.
- **`float`** — a floating-point number, a number *with* a decimal point: `3.14`, `-0.5`, `2.0`. Note that `2.0` is a `float` even though it equals a whole number, because it was *written* with a decimal point. `2` is an `int`; `2.0` is a `float`. The decimal point is the deciding factor.
- **`str`** — a string, a piece of text wrapped in quotes: `"hello"`, `'Python'`. You can use single or double quotes; just be consistent within a value. The quotes are how Python knows it is text and not code — `"5"` is the *text* five, while `5` is the *number* five.
- **`bool`** — a Boolean, a truth value that is one of exactly two values: `True` or `False`. Note the capital first letter — `True` and `False` are written that way and no other. In this topic, that is all you need to know: `True` and `False` are the two values of type `bool`.

```python
age = 30
price = 9.99
name = "Ada"
is_active = True
print(age, price, name, is_active)
```

Output:

```
30 9.99 Ada True
```

The type matters because it controls what a value can do and how it behaves. You will explore operations on these values in the next topic; for now, the goal is simply to recognize each type when you see it.

### 5.7 Inspecting types with `type()`

When you are not sure what type a value is, ask Python directly with the built-in **`type()`** function. You put a value or a variable inside the parentheses, and it reports the type [3]:

```python
print(type(30))
print(type(9.99))
print(type("Ada"))
print(type(True))
```

Output:

```
<class 'int'>
<class 'float'>
<class 'str'>
<class 'bool'>
```

The word `class` here just means "type" — read `<class 'int'>` as "this is an `int`." You can also pass a variable rather than a literal, and `type()` reports the type of whatever the variable currently refers to:

```python
price = 9.99
print(type(price))
```

Output:

```
<class 'float'>
```

`type()` is your everyday tool for checking a value when a program does not behave the way you expected. It takes one line, and it never changes the value — it just tells you what the value is.

### 5.8 Dynamic typing

You may have noticed something: when you wrote `age = 30` you never told Python "this is an integer." You just assigned the value, and Python figured out the type on its own. This is called **dynamic typing** [1].

Dynamic typing means two things:

1. You do not declare a variable's type in advance. The value you assign decides the type. (In some other languages you must announce "this variable holds an integer" before you can use it — Python does not make you do that.)
2. A variable can refer to a value of one type now and a different type later. The variable is just a name; it is the *value* that carries the type.

```python
data = 100
print(type(data))
data = "one hundred"
print(type(data))
```

Output:

```
<class 'int'>
<class 'str'>
```

The name `data` pointed to an `int`, then to a `str`. Python allowed this without complaint because the type belongs to the value, not to the name [1]. This makes Python flexible and quick to write. It also means *you* are responsible for keeping track of what a variable holds — Python will not warn you if a name that "should" be a number suddenly holds text. That is exactly why `type()` is so handy.

## 6. Implementation

A reliable habit when creating and checking a variable is a short sequence you can repeat every time:

1. Choose a clear, `snake_case` name that describes the value.
2. Assign the value with `=` (name on the left, value on the right).
3. If you are unsure of the type, print `type(name)` to confirm.
4. Reassign whenever the value needs to change — Python allows it freely.

### 6.1 Assign and inspect each of the four types

Type these into separate Colab cells (or one cell) and run them. This is the fastest way to build a mental picture of what each type looks like:

```python
items_in_cart = 3
unit_price = 4.50
customer_name = "Ada"
cart_is_empty = False

print(type(items_in_cart))
print(type(unit_price))
print(type(customer_name))
print(type(cart_is_empty))
```

Output:

```
<class 'int'>
<class 'float'>
<class 'str'>
<class 'bool'>
```

Each name follows `snake_case`, each value is one of the four basic types, and `type()` confirms what each one is [3]. Note how the decimal point in `4.50` makes `unit_price` a `float`, while `3` with no decimal point makes `items_in_cart` an `int`.

### 6.2 Reassign a variable and watch the value change

```python
items_in_cart = 3
print(items_in_cart)
items_in_cart = 4
print(items_in_cart)
items_in_cart = items_in_cart + 1
print(items_in_cart)
```

Output:

```
3
4
5
```

The first two lines show a straight replacement. The last assignment uses the current value (`4`) to compute the next value (`5`) and rebinds the name to it [1].

### 6.3 Observe dynamic typing directly

Now combine reassignment with `type()` to *see* the type change follow the value:

```python
label = 100
print(type(label))

label = 3.14
print(type(label))

label = "one hundred"
print(type(label))

label = True
print(type(label))
```

Output:

```
<class 'int'>
<class 'float'>
<class 'str'>
<class 'bool'>
```

One name, four different types over its lifetime — because the type rides along with the value, not with the name [1]. Running this yourself and reading the four lines of output is the single clearest demonstration of dynamic typing you can do.

## 7. Real-World Patterns / Common Pitfalls

These are the mistakes that actually bite beginners in day-to-day coding. Each one comes straight from the concepts above.

**Reassigning and losing the old value.** Once you reassign a name, the previous value is gone — the name no longer remembers it [1]. If you still need the old value later, save it in a *second* variable before you overwrite the first:

```python
balance = 100
old_balance = balance
balance = 40
print(old_balance, balance)
```

Output:

```
100 40
```

Without the `old_balance = balance` line, the `100` would be unrecoverable after `balance = 40`.

**`snake_case` vs the `camelCase` you may know from elsewhere.** If you learned another language first, your fingers may want to type `userName` or `totalPrice`. Python will run those names, but they violate PEP 8 [2]. Retrain the habit early: `user_name`, `total_price`. Consistency across a codebase matters more than any single name.

**Accidentally shadowing a reserved keyword.** New programmers often reach for natural words like `class`, `type`, `list`, or `for` as variable names. Some (like `for` and `class`) are keywords and cause an outright `SyntaxError` [3]. Others (like `type`) are not keywords but are built-in names — assigning `type = 5` would quietly replace the `type()` function for the rest of that session, so your later `type(x)` calls would break in confusing ways. The fix is the same: choose a more specific name, such as `student_type` or `item_class`.

**Case-sensitivity bugs (`Total` vs `total`).** Because Python is case sensitive, a single stray capital letter creates a brand-new variable instead of reusing the one you meant [3]:

```python
total = 50
print(Total)
```

Output:

```
NameError: name 'Total' is not defined
```

You set `total` but read `Total`, so Python complains it has never seen `Total`. When you get a `NameError` on a name you are *sure* you created, check the capitalization first.

**Assuming a name has a fixed type.** Because Python is dynamically typed, a variable that held a number a moment ago can hold text now, and nothing stops it [1]. If a program misbehaves, do not assume you know what a variable holds — check with `type()`:

```python
quantity = 5
print(type(quantity))
quantity = "five"
print(type(quantity))
```

Output:

```
<class 'int'>
<class 'str'>
```

Reaching for `type()` the moment something surprises you will save you far more time than staring at the code and guessing.

## 8. Best Practices

- **Do** use descriptive `snake_case` names: `total_price`, `user_name`, `is_logged_in` [2].
- **Don't** use single letters like `x` or `d` for anything that lives more than a line or two — future readers (including you) will not know what they mean.
- **Don't** try to reuse a reserved keyword as a name; Python will reject it [3].
- **Don't** overwrite built-in names like `type` or `list` with your own variables — it breaks the tools you rely on.
- **Do** remember case sensitivity: `Total` and `total` are different variables [3].
- **Do** use `type()` to check a value when a program surprises you — it takes one line and often reveals the bug [3].

## 9. Hands-On Exercise

In a Colab cell, create four variables — one `int`, one `float`, one `str`, and one `bool` — using clear `snake_case` names. Print each variable and its `type()`. Then reassign your `int` variable to a string value and print its type again to watch dynamic typing in action.

## 10. Key Takeaways

- A variable is a name that refers to a value; you create and change it with the assignment operator `=`, which binds the name on the left to the value on the right [1].
- Identifiers must follow Python's rules (letters, digits, underscores; no leading digit; no keywords) and should follow the `snake_case` convention from PEP 8 [2].
- Python names are case sensitive: `score` and `Score` are different variables [3].
- The four basic types are `int`, `float`, `str`, and `bool`; `type()` reports the type of any value [3].
- Python uses dynamic typing — the type belongs to the value, not the name, so a variable can hold different types over time [1].

## 11. Next Steps

_System-derived from the next entry in curriculum/sequence.md._
