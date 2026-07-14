---
topic_id: 3.1
title: Functions
position_in_module: 1
generated_at: 2026-07-13T00:00:00Z
resource_count: 4
---

# 1. Functions — Topic Corpus

## 2. Prerequisites

- **1.2 Variables, Identifiers & Types** — a function's parameters and return values are just named values with types.
- **1.3 Operators & Expressions** — comparison and boolean expressions form the conditions inside a function.
- **1.4 Statements, Conversion & Output** — you already call `print()`, `input()`, and `int()`; those are functions, and now you will write your own.
- **2.1 Conditionals** — a recursion base case is nothing more than an `if` that stops the process.
- **2.2 Loops** — the iterative way to repeat work; recursion is the alternative you will contrast it against.

## 3. Learning Objectives

- Define a function with `def`, give it parameters, and return a value to the caller.
- Distinguish positional, keyword, and default arguments, and pass them correctly.
- Explain what `*args` and `**kwargs` collect, and iterate over extra positional arguments with a loop.
- Describe local versus global scope and state what the `global` keyword does.
- Write a recursive function with a correct base case and recursive case, using factorial as the model.
- Attach a docstring so a function documents its own purpose.

## 4. Introduction

You have already been calling functions. Every `print("hello")` and every `int("42")` hands work to a block of code someone else wrote, then gets an answer back. A **function** is a named, reusable block of code that takes some inputs, does one job, and gives back a result. Writing your own is the moment your programs stop being one long script and start being organized tools.

This matters right now. Your Week 3 assessment (A1, the Python Core Skills Checkpoint) asks you to translate a plain-English problem into correct, tested Python. The clean way to do that is to name the operation, wrap it in a function, and return an answer that a test can check. A script that only prints is hard to test; a function that returns a value is easy to test. So functions are the capstone skill here — everything about defining them cleanly and returning real values pays off directly on the checkpoint.

## 5. Core Concepts

### 5.1 Defining and calling functions

You create a function with the `def` keyword, a name, a pair of parentheses, and a colon. The indented block below is the function **body**. Defining a function does not run it — it just teaches Python what the name means. You **call** it later by writing the name followed by parentheses [1].

```python
def greet():
    print("Hello there")

greet()   # this line runs the body -> Hello there
```

A function that only prints has done something visible but handed nothing back. To send a value to whoever called it, use the `return` statement. `return` ends the function immediately and produces a value the caller can store or use [1].

```python
def square(n):
    return n * n

answer = square(5)   # answer is now 25
print(answer)
```

The difference between printing and returning is the single most important idea in this topic. `print` shows a value on screen and is gone; `return` gives the value back so the rest of the program — including an automated test — can use it. A function with no `return` statement (or a bare `return`) hands back the special value `None`.

### 5.2 Parameters and arguments

A **parameter** is the name listed inside the parentheses when you define the function. An **argument** is the actual value you supply when you call it. In `def square(n)`, `n` is a parameter; in `square(5)`, `5` is the argument [3].

**Positional arguments** are matched to parameters by their order — the first argument fills the first parameter, and so on [3].

```python
def power(base, exponent):
    result = 1
    for _ in range(exponent):
        result = result * base
    return result

power(2, 3)   # base=2, exponent=3 -> 8
```

**Keyword arguments** are matched by name instead of position, so order stops mattering and the call reads more clearly [1][3].

```python
power(exponent=3, base=2)   # still 8 — names win over order
```

**Default arguments** give a parameter a fallback value used when the caller omits it. This makes the argument optional [1][2].

```python
def greet(name, greeting="Hello"):
    return greeting + ", " + name

greet("Sam")                    # "Hello, Sam"
greet("Sam", "Welcome")         # "Welcome, Sam"
```

There is one ordering rule to remember: parameters with defaults must come after parameters without them, and in a call, positional arguments must come before keyword arguments.

One important warning from the docs: **a default value is evaluated once, at the moment the function is defined, not each time it is called** [1][2]. For a plain number or string default this never bites you. It becomes a real trap when the default is a value that can be changed in place, so the safe habit is to keep defaults as simple fixed values like a number, a string, or `None`.

### 5.3 `*args` and `**kwargs` (introduction)

Sometimes you do not know in advance how many arguments a caller will pass. Putting a `*` before a parameter name tells Python to collect all the extra **positional** arguments together under that one name — by convention it is called `*args`. You can then walk through them with a `for` loop [1].

```python
def total(*args):
    running = 0
    for value in args:
        running = running + value
    return running

total(3, 4, 5)        # 12
total(10, 20)         # 30
total()               # 0
```

The `*` is what matters; the word `args` is just the customary name. Similarly, `**kwargs` (two stars) collects any extra **keyword** arguments the caller passes, keyed by their names [1]. You will use `**kwargs` more heavily in later topics; for now the concept to hold is: one star gathers extra positional arguments, two stars gather extra keyword arguments, and both let a function accept a flexible number of inputs.

### 5.4 Scope: local vs global

**Scope** is the region of a program where a name is visible. A variable created inside a function is **local** — it exists only while the function runs and cannot be seen from outside [1].

```python
def compute():
    temp = 42        # local to compute
    return temp

compute()
print(temp)          # ERROR: temp is not defined out here
```

A variable defined at the top level of your file, outside any function, is **global** — functions can read it. But if a function *assigns* to a name, Python treats that name as local by default, which is usually what you want because it keeps functions from stepping on each other's variables.

When you genuinely need a function to reassign a global variable, the `global` keyword declares that intent [1].

```python
counter = 0

def bump():
    global counter
    counter = counter + 1

bump()
print(counter)       # 1
```

Use `global` sparingly. Functions that take inputs as parameters and hand results back with `return` are far easier to reason about and to test than functions that quietly reach out and mutate shared global state. Keep `global` as the rare exception, not the habit.

### 5.5 Recursion

**Recursion** is a technique where a function solves a problem by calling itself on a smaller version of that same problem [4]. Every recursive function needs two parts. The **base case** is the simplest input, small enough that the answer is known directly without any further call — it is what stops the recursion from running forever [4]. The **recursive case** is the branch where the function calls itself on a smaller or simpler input and combines that result to produce its own answer [4].

The classic worked example is **factorial**: `n!` is `n × (n-1) × ... × 1`, and `0!` is defined as `1` [4]. Notice that `n!` equals `n × (n-1)!` — the definition already refers to a smaller factorial, which is exactly a recursive shape.

```python
def factorial(n):
    if n == 0:            # base case
        return 1
    return n * factorial(n - 1)   # recursive case

factorial(4)   # 4 * 3 * 2 * 1 = 24
```

Each call to `factorial` that has not yet hit the base case is placed on the **call stack** — the mechanism Python uses to keep track of every function call that is still waiting on a result [4]. Trace `factorial(4)`: it needs `4 * factorial(3)`, which needs `3 * factorial(2)`, then `2 * factorial(1)`, then `1 * factorial(0)`, and each of those calls stacks on top of the last, waiting. `factorial(0)` hits the base case and returns `1`. Now the stack unwinds from the top down: `1`, then `1 * 1 = 1`, then `2 * 1 = 2`, then `3 * 2 = 6`, then `4 * 6 = 24`.

If the base case were missing or unreachable, the function would keep calling itself and keep pushing new frames onto the call stack. Python limits how deep that stack can get, and once a program exceeds it, Python raises a `RecursionError` reporting "maximum recursion depth exceeded" rather than letting the program hang or crash the interpreter [4].

The same job can be done with a `for` loop and an accumulator, exactly as you saw in Topic 2.2. Recursion is not faster here; it is a different way of thinking that shines when a problem is naturally defined in terms of a smaller copy of itself. Getting the base case right is the whole game.

### 5.6 Docstrings

A **docstring** is a string literal placed as the very first statement inside a function body, written in triple quotes. Python stores it so tools and readers can see what the function does. It is the standard, built-in way to document a function [1].

```python
def factorial(n):
    """Return n! for a non-negative integer n."""
    if n == 0:
        return 1
    return n * factorial(n - 1)
```

A good docstring says what the function does, what it expects, and what it returns — in one or a few plain sentences. It is documentation that travels with the code instead of drifting out of date in a separate file.

## 6. Implementation

A reliable recipe for writing a function from a plain-English problem — the exact skill A1 tests:

1. **Name the job.** Turn the verb in the problem into a function name (e.g. "compute the total" → `total`).
2. **List the inputs as parameters.** What does the function need to know? Those become parameters. Give sensible defaults to any that are optional.
3. **Write a one-line docstring** stating what it returns.
4. **Do the work in the body**, using the conditionals and loops you already know.
5. **`return` the answer** — do not merely `print` it, so a test can check the value.
6. **Call it with sample inputs** and confirm the returned value is correct.

## 8. Best Practices

- **Return, don't print, when the value will be reused.** Print only when the message itself is the goal.
- **One function, one job.** A function that does exactly one thing is easy to name, test, and reuse.
- **Keep default arguments simple and fixed** (a number, a string, or `None`) — remember defaults are evaluated once at definition time.
- **Prefer parameters and return values over `global`.** Reaching out to mutate global state makes functions hard to test.
- **Always give a recursive function a reachable base case** before you write the recursive call.
- **Write a docstring for every non-trivial function.** Future-you is the first reader.

## 9. Hands-On Exercise

Write `factorial(n)` recursively with a base case at `n == 0` and a one-line docstring, then call it on `0`, `1`, and `5`. Next write `greet(name, greeting="Hello")` using a default argument and call it both with and without the second argument. Finally write `total(*args)` that sums its arguments with a `for` loop and returns the result; confirm `total(3, 4, 5)` returns `12` and `total()` returns `0`.

## 10. Key Takeaways

- A function is defined with `def`, does one job, and hands a value back with `return`; returning (not printing) is what makes a function testable.
- Arguments are passed by position or by name, and default arguments make parameters optional — but a default is evaluated once, at definition time.
- `*args` collects extra positional arguments (loop over them to use them) and `**kwargs` collects extra keyword arguments.
- Variables assigned inside a function are local by default; `global` is the rare exception for reassigning a top-level name.
- A recursive function must have a base case that stops the calls and a recursive case that shrinks the problem; factorial is the canonical example.

## 11. Next Steps

_System-derived from the next entry in curriculum/sequence.md._
