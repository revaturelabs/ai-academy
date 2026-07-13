---
topic_id: 1.4
title: Statements, Conversion & Output
position_in_module: 4
generated_at: 2026-07-13T00:00:00Z
resource_count: 3
---

# 1. Statements, Conversion & Output — Topic Corpus

## 2. Prerequisites

- **1.1 The Python Environment** — you can run a cell in Colab and use `print()`.
- **1.2 Variables, Identifiers & Types** — you can assign variables with `=`, and you know the four basic types `int`, `float`, `str`, `bool` and the `type()` function.
- **1.3 Operators & Expressions** — you can use arithmetic operators (`+ - * / // % **`), comparison operators (`== != < > <= >=`), and logical operators (`and`, `or`, `not`), and you understand truthiness (which values are falsy).

## 3. Learning Objectives

By the end of this topic you will be able to:

- Distinguish an assignment statement from an expression statement, and use chained assignment and tuple unpacking.
- Convert values between types with `int()`, `float()`, `str()`, and `bool()`, and predict truncation and truthiness results.
- Build readable output with f-strings, embedding expressions and applying format specifiers such as `:.2f`, `:d`, `:>10`, and `:^15`.
- Recognize variable type-hint syntax (e.g. `count: int = 0`) and read a simple `match`/`case` block.
- Write clear comments and apply the basics of PEP 8 style.

## 4. Introduction

Over the last three topics you learned to store values, know their types, and combine them with operators. This topic is the module closer: it turns that raw capability into programs that *communicate*. Three practical problems come together here.

First, real data rarely arrives in the type you want. A number typed by a user comes in as text (`"42"`, not `42`), and text can't be added to a number. You need **type conversion** to move a value from one type to another. Second, once you have a result, you need to *show* it — and "show it nicely," with two decimal places for a price or a value lined up in a column. That is what **f-strings** do. Third, as programs grow, you and your teammates need to *read* them: comments, consistent style, and a couple of newer syntax forms (type hints, `match`/`case`) that you'll increasingly see in real Python code.

None of this is exotic. It is the everyday glue that connects "I computed something" to "I displayed it clearly to a human." That's the difference between a snippet and a program.

## 5. Core Concepts

### 5.1 Statements: assignment vs expression

A **statement** is a complete instruction Python executes. You have already been writing them: `x = 5` is a statement, and so is `print(x)`.

Two kinds matter here. An **assignment statement** binds a value to a name using `=` — it does not produce a value of its own, it *stores* one:

```python
total = 10 + 5
```

An **expression statement** is an expression written on its own line, evaluated for its result or its side effect. A `print(...)` call is the one you'll write most:

```python
print(total)
```

Output:

```
15
```

The key difference: an assignment *saves* a value for later; an expression statement *does* something now (like printing) and, in a script, its value is discarded unless you capture it.

### 5.2 Chained assignment and tuple unpacking

Python offers two compact assignment forms that save typing and make intent clear.

**Chained assignment** binds the same value to several names at once:

```python
a = b = 5
print(a, b)
```

Output:

```
5 5
```

Both `a` and `b` now refer to `5`. This is handy when several variables should start at the same value.

**Tuple unpacking** assigns several values in one statement by matching them up position-by-position. The names on the left and the values on the right are paired left-to-right:

```python
x, y = 1, 2
print(x, y)
```

Output:

```
1 2
```

Here `x` becomes `1` and `y` becomes `2`. The counts must match — two names, two values. Unpacking is the clean way to give several related values their names in a single line, and it powers a common trick: swapping two variables without a temporary holder.

```python
x, y = y, x
print(x, y)
```

Output:

```
2 1
```

Python evaluates the whole right side first, then assigns — so the swap works with no third variable. (You are seeing the tuple `1, 2` used purely as an *assignment form* here; tuples as a full data structure come in a later course.)

### 5.3 Type conversion

Every value has a type (1.2). **Type conversion** — also called casting — produces a *new* value of a different type from an existing one. Python gives you one conversion function per basic type: `int()`, `float()`, `str()`, and `bool()` [2]. The original value is never changed; you get a converted copy back.

**`str()`** turns any value into its text form. This is the one you'll use most, because output is text:

```python
age = 42
print(str(age))
print(type(str(age)))
```

Output:

```
42
<class 'str'>
```

`str(42)` gives the *text* `"42"`, which looks the same when printed but is now a `str`, not an `int`.

**`int()`** turns a value into a whole number. From a string of digits it parses the number; from a float it **truncates** — it chops off the decimal part, it does *not* round:

```python
print(int("5"))
print(int(3.9))
print(int(-3.9))
```

Output:

```
5
3
-3
```

Note `int(3.9)` is `3`, not `4` — truncation always drops the fractional part and moves toward zero, so `int(-3.9)` is `-3` [2]. `int("5")` works because `"5"` is a clean integer string; `int("3.14")` raises a `ValueError`, because `"3.14"` is not a whole number in text form.

**`float()`** turns a value into a floating-point number, either by parsing text or by adding a decimal point to an integer:

```python
print(float("3.14"))
print(float(42))
```

Output:

```
3.14
42.0
```

**`bool()`** converts a value to `True` or `False` using the truthiness rules from 1.3. The falsy values — `0`, `0.0`, `""` (empty string) — convert to `False`; almost everything else converts to `True` [2]:

```python
print(bool(0))
print(bool(""))
print(bool(42))
print(bool("hi"))
```

Output:

```
False
False
True
True
```

The classic real problem conversion solves: text that *looks* like a number is still text. `"5" + 3` is an error because you can't add a string to an int. Convert first:

```python
quantity = "5"
print(int(quantity) + 3)
```

Output:

```
8
```

### 5.4 String basics: quotes, concatenation, indexing

A **string** (`str`) is text in quotes (1.2). Python accepts **single or double quotes** with no difference in meaning — pick one and be consistent. The reason both exist: use double quotes when the text contains an apostrophe, and single quotes when it contains a double quote, so you don't have to escape them:

```python
a = 'hello'
b = "hello"
c = "it's fine"
print(a, b, c)
```

Output:

```
hello hello it's fine
```

**Concatenation** joins strings with `+`. Both sides must be strings — this is exactly why `str()` matters:

```python
first = "Ada"
last = "Lovelace"
print(first + " " + last)
```

Output:

```
Ada Lovelace
```

**Indexing** reads one character out of a string by its position, written in square brackets. Positions start at **0**, not 1, so the first character is index `0`:

```python
name = "Python"
print(name[0])
print(name[1])
```

Output:

```
P
y
```

That's the introduction to indexing — enough to grab a character by position. (Slicing and the full string toolkit come later.)

### 5.5 Formatted output with f-strings

The best way to build readable output is the **f-string** (formatted string literal): a string prefixed with the letter `f`, in which anything inside curly braces `{}` is evaluated and its result dropped into the text [1].

```python
name = "Ada"
age = 42
print(f"{name} is {age} years old")
```

Output:

```
Ada is 42 years old
```

No `+`, no `str()` calls — Python converts each embedded value to text for you. Because the braces hold an *expression*, you can embed any expression, including the operators from 1.3 [1]:

```python
price = 20
qty = 3
print(f"Total: {price * qty}")
print(f"Cheaper? {price < 25}")
```

Output:

```
Total: 60
Cheaper? True
```

**Format specifiers** go after a colon inside the braces and control *how* the value is displayed [1]. The four you need:

- `:.2f` — a float shown to 2 decimal places (`f` = fixed-point, `.2` = two decimals). Ideal for money.
- `:d` — an integer in plain decimal form.
- `:>10` — right-align the value in a field 10 characters wide (`>` = align right).
- `:^15` — center the value in a field 15 characters wide (`^` = center).

```python
price = 19.5
print(f"{price:.2f}")
print(f"{42:d}")
print(f"{'hi':>10}")
print(f"{'hi':^15}")
```

Output:

```
19.50
42
        hi
      hi
```

`{price:.2f}` rounds and pads to two decimals, giving `19.50`. The alignment specifiers pad with spaces to make columns line up — invaluable when printing tables of data. You can combine width and precision too: `{price:>10.2f}` right-aligns a two-decimal number in a 10-wide field.

### 5.6 Type hints (introduction)

A **type hint** (also called an annotation) records what type a variable is *expected* to hold. You write it with a colon after the name:

```python
count: int = 0
name: str = "Ada"
price: float = 9.99
```

The hint after the colon (`int`, `str`, `float`) is documentation for humans and tools. Python does **not** enforce it — assigning a string to `count` above would still run — but editors and type-checkers use hints to catch mistakes and to autocomplete. Hints make code self-describing: a reader sees `count: int` and knows the intent instantly.

You will also see hints on functions — on their parameters and return type — which look like `def area(w: float, h: float) -> float:`. You'll meet functions properly in a later course; for now, just recognize the shape when you see it. At this stage, the takeaway is simply: `name: type` is Python telling you (and the tools) what a value is meant to be.

### 5.7 match-case (introduction)

`match`/`case` is **structural pattern matching**: you give it a value, and it runs the first `case` whose pattern matches [3]. On simple values it reads like a clean multi-way choice:

```python
status = "active"

match status:
    case "active":
        print("User is active")
    case "banned":
        print("Access denied")
    case _:
        print("Unknown status")
```

Output:

```
User is active
```

Python compares `status` against each `case` top-to-bottom. `case "active"` matches, so its block runs and the rest are skipped. The underscore `case _` is the **wildcard** — it matches anything, acting as a catch-all "none of the above" [3]. This is an *introduction*: recognize the shape (`match value:` then indented `case pattern:` blocks). Pattern matching on richer shapes, and the general control-flow it relates to, come later.

### 5.8 Comments and readability (PEP 8 intro)

A **comment** is text Python ignores — it's for humans reading the code. A line comment starts with `#`; everything after it on that line is skipped:

```python
tax_rate = 0.08  # 8% sales tax
subtotal = 50    # before tax
```

Good comments explain *why*, not the obvious *what*. `# add tax` above `total = subtotal * 1.08` says nothing the code doesn't; `# state law requires rounding up` earns its place.

**PEP 8** is Python's official style guide (you met its `snake_case` rule in 1.2). A few basics: use spaces around operators (`x = 5`, not `x=5`); one statement per line; keep lines reasonably short; and use blank lines to separate logical chunks. Consistent style makes code readable to every Python programmer, which matters the moment more than one person touches it.

## 6. Implementation

A reliable pattern for taking raw values and producing clean output:

1. **Get the value** in whatever type it arrives (often `str`).
2. **Convert** it to the type you need with `int()`, `float()`, `str()`, or `bool()`.
3. **Compute** using operators (1.3).
4. **Format** the result into an f-string with the right specifier.
5. **Print** it.

A worked example — a tiny receipt line:

```python
item: str = "Coffee"        # type hint documents intent
price_text: str = "4.5"     # imagine this came in as text
quantity: int = 3

price = float(price_text)   # convert text -> float
total = price * quantity    # compute with 1.3 operators

print(f"{item:>10}: {quantity:d} x {price:.2f} = {total:.2f}")
```

Output:

```
    Coffee: 3 x 4.50 = 13.50
```

Every piece from this topic appears: a type hint, a conversion (`float(price_text)`), arithmetic, an f-string, and specifiers for alignment (`:>10`), integer (`:d`), and money (`:.2f`).

## 7. Real-World Patterns / Common Pitfalls

- **Adding a number to text.** `"5" + 3` raises a `TypeError`. Convert first: `int("5") + 3` → `8`. This is the single most common beginner error, and conversion is the fix [2].
- **Expecting `int()` to round.** `int(3.9)` is `3`, not `4`. `int()` truncates toward zero [2]. If you want rounding, that's a different tool — `int()` always chops.
- **`int("3.14")` crashes.** `int()` only parses whole-number strings; a decimal string raises `ValueError`. Use `float("3.14")` for decimals, then convert to int if needed.
- **Forgetting the `f`.** `print("{name}")` prints the literal text `{name}` because there's no `f` prefix — the braces are only special in an f-string [1].
- **`:.2f` on an int.** `f"{42:.2f}"` gives `42.00` — the `f` specifier coerces the value to float form. Handy, but know it happens.
- **Assuming type hints enforce anything.** They don't. `count: int = "oops"` runs fine at execution time; hints guide humans and tools, not the interpreter.

## 8. Best Practices

- **Do** convert input to the type you need as early as possible, so the rest of your code works with clean types [2].
- **Do** use f-strings for all formatted output — they're the modern, readable default [1].
- **Do** use `:.2f` for money and `:>`/`:^` to line up columns [1].
- **Do** comment the *why*; skip comments that just restate the code.
- **Do** follow PEP 8: spaces around operators, `snake_case` names, one statement per line.
- **Don't** build output with a chain of `+` and `str()` calls when an f-string is clearer.
- **Don't** rely on type hints for correctness — they document, they don't enforce.

## 9. Hands-On Exercise

In a Colab cell, start with three string values: `name = "Ada"`, `age_text = "42"`, and `price_text = "19.5"`. Convert `age_text` to an `int` and `price_text` to a `float`. Then print a single f-string that shows the name centered in a 15-wide field, the age as an integer, and the price to two decimal places. Add a `# comment` explaining one line. Finally, write a small `match` block on `name` that prints a greeting for `"Ada"` and a default with `case _`.

## 10. Key Takeaways

- Assignment statements store a value; expression statements (like `print()`) act now. Chained assignment (`a = b = 5`) and tuple unpacking (`x, y = 1, 2`) are compact assignment forms.
- `int()`, `float()`, `str()`, `bool()` convert between types; `int()` truncates toward zero, and `bool()` follows truthiness (`0`, `0.0`, `""` → `False`).
- Strings use single or double quotes, join with `+`, and index from position `0` with `[]`.
- f-strings embed expressions in `{}` and format with specifiers — `:.2f`, `:d`, `:>10`, `:^15` — for clean, aligned output.
- Type hints (`count: int = 0`) and `match`/`case` are readable modern syntax you should recognize; comments and PEP 8 style keep code readable for everyone.

## 11. Next Steps

_System-derived from the next entry in curriculum/sequence.md._
