# Conditionals

## Overview

Every program you have written so far runs top to bottom, one statement after another, no matter what. Real software has to *react*: a login screen behaves differently for the right password than the wrong one, and a task tracker sorts a job into "urgent," "soon," or "whenever." **Conditionals** give you that branching — they ask a yes/no question about your data and choose which statements to run based on the answer. That question is always a boolean expression that evaluates to `True` or `False`, exactly the values you met with comparison operators [3]. _This contributes to A1 — Python Core Skills Checkpoint (due W3)._

## Key Concepts

**The `if` statement.** The simplest conditional is a single `if`: a header line ending in a colon, followed by an indented block that runs only when the condition is `True` [3].

```python
temperature = 30

if temperature > 25:
    print("It is warm.")
    print("Consider a lighter jacket.")

print("Done checking.")
```

Read it literally: "if `temperature > 25` is `True`, run the indented block." Because `30 > 25`, both indented lines run. Had `temperature` been `20`, Python would skip the block and jump straight to `print("Done checking.")`, which is not indented and therefore not part of the `if`. Any value that is `True` or `False` can serve as the condition, so you can test a boolean variable directly — `if is_raining:` says the same thing as `if is_raining == True:`, more cleanly.

**Indentation is the structure.** Where many languages use braces `{ }` to group statements, Python uses **indentation** — and that indentation is not decoration, it is the grammar [3]. The standard is four spaces per level, and every line in a block must be indented the same amount.

```python
score = 55

if score >= 50:
    print("You passed.")      # part of the if block
    print("Well done.")       # still part of the if block
print("Results recorded.")     # NOT in the block — always runs
```

Mixing indentation, or forgetting it, produces an `IndentationError`. The shape of the code on the page matches the logic, so treat indentation with the same care you give the condition.

**`if` / `else`: two paths.** When you want one thing to happen on `True` and a different thing on `False`, add an `else`. Exactly one of the two blocks runs — never both, never neither. `else` has no condition of its own; it is the catch-all for everything the `if` did not cover [3].

```python
age = 16

if age >= 18:
    print("You may vote.")
else:
    print("You are too young to vote.")
```

**`if` / `elif` / `else`: multi-branch decisions.** For more than two possibilities, chain conditions with `elif` ("else if"). Python checks each condition **in order, top to bottom**, and runs the block for the *first* one that is `True`; once a branch matches, the rest are skipped. An optional final `else` handles the case where none matched [3].

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

A `grade` of `78` fails `>= 90` and `>= 80`, matches `>= 70`, and prints `C`. Notice we did not write `grade >= 70 and grade < 80` — because the `>= 80` branch already handled everything from 80 up, by the time we reach the `>= 70` test we know the grade is under 80. Three rules follow from top-to-bottom evaluation:

- **Order matters.** Put the most specific or most common conditions first; if two could both be true, the earlier one wins and the later one never runs.
- **Only one branch executes**, even if a later `elif` would also be `True`.
- **`else` is optional.** Leave it off for "do nothing when nothing matches," but including it guarantees a path always runs — often safer, since it catches values you did not anticipate.

**Compound conditions: `and`, `or`, `not`.** A condition need not be a single comparison. Combine comparisons with the logical operators to express richer tests [3]: `and` is `True` only when *both* sides are true, `or` is `True` when *at least one* side is, and `not` flips a boolean.

```python
age = 25
has_ticket = True

if age >= 18 and has_ticket:
    print("Admitted to the show.")

if not logged_in:
    print("Please log in first.")
```

"You may enter if you are an adult *and* you hold a ticket" reads almost like the English sentence, capturing in one branch what would otherwise need clumsy nesting. Two practical notes: group with parentheses when precedence is unclear — `if (a > 0 and b > 0) or c == 0:` — and remember a range check reads naturally as a chained comparison, `if 0 <= score <= 100:`.

**Nested conditionals.** The block inside an `if` can contain anything, including another `if`. Putting one conditional inside another is **nesting**, and each level adds a step of indentation [1]. Nesting fits when the second decision only makes sense *after* the first is answered — there is no point asking "are you an admin?" about someone who is not logged in. But every level shifts the code right and adds a fact to hold in your head. Often a nested test flattens into one combined condition:

```python
# Nested
if logged_in:
    if is_admin:
        print("Welcome, administrator.")

# Flattened — same result, easier to read
if logged_in and is_admin:
    print("Welcome, administrator.")
```

Prefer the flatter version when both conditions are simply required. Reserve genuine nesting for when the inner decision has its own `else` that the outer level does not share.

**The conditional (ternary) expression.** Sometimes an `if`/`else` exists only to pick between two *values*. Python offers a compact one-line form for that case, the **conditional expression** (informally, the "ternary operator") [1][2]. Its shape reads almost like English — "give me `value_if_true` if `condition` is true, else `value_if_false`" [2]:

```
value_if_true if condition else value_if_false
```

```python
age = 20
status = "adult" if age >= 18 else "minor"
```

The key distinction: a plain `if`/`else` is a **statement** — it directs what happens. A conditional expression *evaluates to a value*, so you can use it anywhere a value is expected, such as inside a `print` [1]:

```python
number = 7
print("even" if number % 2 == 0 else "odd")   # prints: odd
```

Use it only for simple two-way value choices that fit comfortably on one line. Chaining several ternaries together is possible but quickly becomes unreadable — when you feel that urge, an `if`/`elif`/`else` chain is the clearer choice [1].

## Worked Example

The week's lab is a **task classifier**: read a task's priority number and print how urgent it is. A reliable recipe for turning any plain-English decision into code is: state the question as a boolean, count the outcomes (two → `if`/`else`, three or more → `if`/`elif`/`else`), order branches from most specific to least, and decide whether you need a fallback `else`.

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

Step through it. `input()` returns text, so `int(...)` converts it to a number before the comparisons run. Suppose the user types `2`: Python tests `priority == 1` (false, skip), then `priority == 2` (true) — it prints `"Soon — do it today."` and skips every branch below, including the `else`. If the user types `9`, all three `==` tests fail and the final `else` catches it, so the program always responds sensibly rather than doing nothing. That last point is why the `else` earns its place here: it guards against input you did not anticipate.

## In Practice

- **Let indentation tell the truth.** Four spaces per level, consistent throughout a block. Never mix tabs and spaces.
- **Test booleans directly** — `if is_ready:`, not `if is_ready == True:`.
- **Order `elif` branches deliberately.** The first true one wins, so specific and common cases go first.
- **Prefer flat over nested.** If two conditions must both hold, combine them with `and` rather than nesting two `if`s. Reserve nesting for inner decisions with their own distinct outcomes, and keep it shallow — three-plus levels signals it is time to rethink the logic.
- **Use a conditional expression for value choices only**, and only when it stays readable on one line; never chain them.
- **Guard against the unexpected** with a final `else` when a stray input could otherwise silently do nothing.

## Key Takeaways

- A conditional runs a block of code based on a boolean condition: `if` runs its block only when the condition is `True`, and `else` covers the `False` case.
- `if`/`elif`/`else` chooses exactly one branch — Python checks conditions top to bottom and stops at the first `True`, so branch order matters.
- Indentation is not style in Python; it defines which statements belong to which branch, and inconsistent indentation is an error.
- Conditions can be compound: `and` requires both sides true, `or` requires at least one, and `not` flips a boolean.
- Nesting puts a decision inside a decision — keep it shallow and flatten "both must be true" cases with `and`.
- The conditional expression `A if condition else B` produces a value in one line, best used for simple two-way value choices.

These are the building blocks a program lives on, and they prepare you to translate plain-English decisions into tested control flow for the Python Core Skills Checkpoint.

## References

[1] Conditional Expressions in Python (nkmk note). https://note.nkmk.me/en/python-if-conditional-expressions/

[2] The Python Ternary Operator (Dataquest). https://www.dataquest.io/blog/python-ternary-operator/

[3] Python Conditional Control (KoderHQ). https://www.koderhq.com/tutorial/python/conditional-control/
