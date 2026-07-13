---
topic_id: 2.1
title: Conditionals
position_in_module: 1
generated_at: 2026-07-13T00:00:00Z
resource_count: 3
---

# 1. Conditionals — Topic Corpus

## 2. Prerequisites

- **1.2 Variables, Identifiers & Types** — you must be comfortable storing a value in a variable and knowing whether it is a number, a string, or a boolean.
- **1.3 Operators & Expressions** — this topic builds directly on the comparison operators (`<`, `>`, `==`, `!=`, `<=`, `>=`) and the boolean type (`True` / `False`) introduced there. A condition is just a boolean expression.
- **1.4 Statements, Conversion & Output** — you will use `input()`, `print()`, and type conversion (for example `int(...)`) in the examples and the exercise.

## 3. Learning Objectives

After this topic you will be able to:

- **Write** a single `if` statement that runs a block of code only when a condition is `True`.
- **Build** multi-branch decisions with `if` / `elif` / `else`, choosing exactly one path out of several.
- **Explain** how indentation defines which statements belong to a branch in Python.
- **Combine** comparisons with `and`, `or`, and `not` to form richer conditions.
- **Nest** one conditional inside another and judge when nesting helps or hurts readability.
- **Rewrite** a simple value-choosing `if`/`else` as a conditional (ternary) expression.

## 4. Introduction

Every program you have written so far runs top to bottom, one statement after another, no matter what. That is fine for a calculator that always does the same thing — but real software has to *react*. A login screen behaves differently for the right password than the wrong one. A thermostat turns the heat on below a target temperature and off above it. A task tracker sorts a job into "urgent," "soon," or "whenever" based on its due date.

That branching — "do this *only if* something is true, otherwise do that instead" — is what **conditionals** give you. A conditional asks a yes/no question about your data and then chooses which statements to run based on the answer. The question is always a boolean expression: something that evaluates to `True` or `False`, exactly the values you met with comparison operators [3].

By the end of this topic you will be able to build the kind of logic that a real program lives on. The running example for the week's lab is a **task classifier**: read a task's priority number and print how urgent it is. That is nothing more than a chain of conditionals, and you will have all the pieces to write it.

## 5. Core Concepts

### 5.1 The `if` statement: run code only when a condition holds

The simplest conditional is a single `if`. It has a header line ending in a colon, followed by an indented block that runs only when the condition is `True` [3].

```python
temperature = 30

if temperature > 25:
    print("It is warm.")
    print("Consider a lighter jacket.")

print("Done checking.")
```

Read it literally: "if `temperature > 25` is `True`, run the indented block." The condition `temperature > 25` is a boolean expression — it evaluates to `True` or `False` just like the comparisons from topic 1.3. Because `30 > 25` is `True`, both indented `print` lines run. If `temperature` had been `20`, Python would skip the whole block and jump straight to `print("Done checking.")`, which is *not* indented and therefore not part of the `if`.

Anything whose value is `True` or `False` can be the condition. You can store a condition in a variable, too:

```python
is_raining = True

if is_raining:
    print("Bring an umbrella.")
```

Here the condition is simply the boolean value `is_raining`. Writing `if is_raining == True` would work but is redundant — the value is already `True` or `False`, so `if is_raining` says the same thing more cleanly.

### 5.2 Indentation *is* the structure

In many languages, braces `{ }` mark which statements belong together. Python uses **indentation** instead: the statements that are indented under the `if` header form its block, and that indentation is not decoration — it is the grammar [3].

```python
score = 55

if score >= 50:
    print("You passed.")      # part of the if block
    print("Well done.")       # still part of the if block
print("Results recorded.")     # NOT part of the if block — always runs
```

The standard is **four spaces** per level. Every line in a block must be indented the same amount; mixing indentation, or forgetting it entirely, produces an `IndentationError`. This makes Python code visually honest — the shape of the code on the page matches the logic. It also means that lining things up carelessly changes behaviour, so treat indentation with the same care you give the condition itself.

### 5.3 `if` / `else`: choosing between two paths

Often you want one thing to happen when the condition is `True` and a *different* thing when it is `False`. That is what `else` is for. The `else` block runs exactly when the `if` condition is `False` [3].

```python
age = 16

if age >= 18:
    print("You may vote.")
else:
    print("You are too young to vote.")
```

Exactly one of the two blocks runs — never both, never neither. `else` has no condition of its own; it is the catch-all for "everything the `if` did not cover."

### 5.4 `if` / `elif` / `else`: multi-branch decisions

When there are more than two possibilities, chain them with `elif` (short for "else if"). Python checks each condition **in order, top to bottom**, and runs the block for the *first* one that is `True`. Once a branch matches, the rest are skipped entirely. An optional final `else` handles the case where none matched [3].

```python
priority = 2

if priority == 1:
    print("Urgent — do it now.")
elif priority == 2:
    print("Soon — do it today.")
elif priority == 3:
    print("Whenever — no rush.")
else:
    print("Unknown priority.")
```

This is the shape of the week's **task classifier** lab. A few things worth internalising:

- **Order matters.** Because Python stops at the first `True` branch, put the most specific or most common conditions first. If two conditions could both be true, the earlier one wins and the later one never runs.
- **Only one branch executes.** Even if a later `elif` would also be `True`, it is never reached once an earlier branch matches.
- **`else` is optional.** Leave it off if you genuinely want "do nothing when nothing matches." Include it to guarantee some path always runs — which is often safer, because it catches values you did not anticipate.

Ranges are a common use, and here order is what makes it correct:

```python
grade = 78

if grade >= 90:
    print("A")
elif grade >= 80:
    print("B")
elif grade >= 70:
    print("C")
else:
    print("Below C")
```

A `grade` of `78` fails `>= 90` and `>= 80`, matches `>= 70`, and prints `C`. Notice we did not have to write `grade >= 70 and grade < 80` — because the `>= 80` branch above already handled everything from 80 up, by the time we reach the `>= 70` test we know the grade is under 80.

### 5.5 Boolean expressions in conditions: `and`, `or`, `not`

A condition does not have to be a single comparison. You can combine comparisons with the logical operators `and`, `or`, and `not` to express compound tests [3].

- **`and`** is `True` only when *both* sides are `True`.
- **`or`** is `True` when *at least one* side is `True`.
- **`not`** flips a boolean: `not True` is `False`, and `not False` is `True`.

```python
age = 25
has_ticket = True

if age >= 18 and has_ticket:
    print("Admitted to the show.")

temperature = 5
if temperature < 0 or temperature > 35:
    print("Extreme temperature warning.")

logged_in = False
if not logged_in:
    print("Please log in first.")
```

Combining operators lets one branch capture an idea that would otherwise need clumsy nesting. "You may enter if you are an adult *and* you hold a ticket" reads almost like the English sentence.

Two practical notes:

- You can group with parentheses to make precedence obvious: `if (a > 0 and b > 0) or c == 0:`. When in doubt, add parentheses — they cost nothing and remove ambiguity.
- A range check reads naturally as a chained comparison: `if 0 <= score <= 100:` is Python shorthand for `score >= 0 and score <= 100`.

### 5.6 Nested conditionals: decisions inside decisions

The block inside an `if` can contain *anything* — including another `if`. Putting one conditional inside another is called **nesting**, and each level adds another step of indentation [1].

```python
logged_in = True
is_admin = False

if logged_in:
    if is_admin:
        print("Welcome, administrator.")
    else:
        print("Welcome, user.")
else:
    print("Access denied. Please log in.")
```

The inner `if`/`else` is only reached when the outer condition (`logged_in`) is `True`. Nesting is useful when the second decision only makes sense *after* the first has been answered — there is no point asking "are you an admin?" about someone who is not logged in at all.

The trade-off is **readability**. Every level of nesting shifts the code further right and adds a fact you have to hold in your head. Two levels are usually fine; three or more become hard to follow. Often a nested test can be flattened into a single combined condition:

```python
# Nested
if logged_in:
    if is_admin:
        print("Welcome, administrator.")

# Flattened — same result, easier to read
if logged_in and is_admin:
    print("Welcome, administrator.")
```

Prefer the flatter version when the two conditions are simply both required. Reach for genuine nesting only when the branches diverge — that is, when the inner decision has its own `else` that the outer level does not share.

### 5.7 The conditional (ternary) expression

Sometimes an `if`/`else` exists only to pick between two *values*. Python offers a compact one-line form for exactly that case, called the **conditional expression** (informally, the "ternary operator") [1][2].

Its shape is:

```
value_if_true if condition else value_if_false
```

Read left to right it is almost English: "give me `value_if_true` if `condition` is true, else `value_if_false`" [2].

```python
age = 20

# Long form
if age >= 18:
    status = "adult"
else:
    status = "minor"

# Same thing as a conditional expression
status = "adult" if age >= 18 else "minor"
```

Both produce `status == "adult"`. The key distinction: a plain `if`/`else` is a **statement** — it directs what happens. A conditional expression is an **expression** — it *evaluates to a value*, so you can use it anywhere a value is expected, such as the right-hand side of an assignment or directly inside a `print` [1]:

```python
number = 7
print("even" if number % 2 == 0 else "odd")   # prints: odd
```

Use the conditional expression when you are choosing between two simple values and it fits comfortably on one line. Stick with a full `if`/`else` when the branches do more than produce a value, or when squeezing the logic onto one line would make it cryptic. Chaining several ternaries together (one inside another) is possible but quickly becomes unreadable — when you feel that urge, an `if`/`elif`/`else` chain is the clearer choice [1].

## 6. Implementation

A reliable recipe for turning a plain-English decision into a conditional:

1. **State the question as a boolean.** What is `True`-or-`False` fact does the decision hinge on? ("Is the priority equal to 1?")
2. **Count the outcomes.** Two outcomes → `if`/`else`. Three or more → `if`/`elif`/.../`else`. One outcome with "do nothing otherwise" → a bare `if`.
3. **Order the branches** from most specific / most likely to least, remembering Python stops at the first `True` branch.
4. **Write each condition** using comparison operators, joining them with `and` / `or` / `not` where one branch needs a compound test.
5. **Indent each block** consistently (four spaces) so it clearly belongs to its header.
6. **Decide on the `else`.** Add it to guarantee a fallback for unexpected input; omit it only when doing nothing is genuinely correct.
7. **Simplify.** If an `if`/`else` only assigns one of two values, consider the conditional expression. If a nested `if` is just "both must be true," flatten it with `and`.

Worked example — the task classifier:

```python
priority = int(input("Enter task priority (1-3): "))

if priority == 1:
    print("Urgent — do it now.")
elif priority == 2:
    print("Soon — do it today.")
elif priority == 3:
    print("Whenever — no rush.")
else:
    print("Unknown priority. Please enter 1, 2, or 3.")
```

`input()` returns text, so `int(...)` converts it to a number (topic 1.4) before the comparisons run. The `else` catches anything outside 1–3, so the program always responds sensibly.

## 8. Best Practices

- **Let indentation tell the truth.** Four spaces per level, consistent throughout a block. Never mix tabs and spaces.
- **Test booleans directly.** Write `if is_ready:` rather than `if is_ready == True:`.
- **Order `elif` branches deliberately** — the first true one wins, so specific and common cases go first.
- **Prefer flat over nested.** If two conditions must both hold, combine them with `and` instead of nesting two `if`s. Reserve nesting for cases where an inner decision has its own distinct outcomes.
- **Keep nesting shallow.** Three-plus levels of indentation is a signal to rethink the logic or combine conditions.
- **Use a conditional expression for value choices only**, and only when it stays readable on one line — never chain them.
- **Guard against the unexpected** with a final `else` when a stray input could otherwise silently do nothing.

## 9. Hands-On Exercise

Extend the task classifier. Read *two* inputs: a priority number (1–3) and whether the task is blocked (`"yes"`/`"no"`). Print `"Urgent — do it now."` only when the priority is `1` **and** the task is not blocked; if it is blocked, print `"Blocked — resolve dependency first."` regardless of priority. Handle priorities 2 and 3 as before, and add an `else` for invalid priorities. Then rewrite one of your two-value decisions (for example, choosing the word `"today"` vs `"later"`) as a conditional expression.

## 10. Key Takeaways

- A conditional runs a block of code based on a boolean condition; `if` runs code only when its condition is `True`, and `else` covers the `False` case.
- `if`/`elif`/`else` chooses exactly one branch — Python checks conditions top to bottom and stops at the first `True`, so branch order matters.
- In Python, indentation is not style — it defines which statements belong to which branch, and inconsistent indentation is an error.
- Conditions can be compound: `and` requires both sides true, `or` requires at least one, and `not` flips a boolean.
- Nesting puts a decision inside a decision; keep it shallow and flatten "both must be true" cases with `and`.
- The conditional expression `A if condition else B` produces a value in one line and is best used for simple two-way value choices.

## 11. Next Steps

_System-derived from the next entry in curriculum/sequence.md._
