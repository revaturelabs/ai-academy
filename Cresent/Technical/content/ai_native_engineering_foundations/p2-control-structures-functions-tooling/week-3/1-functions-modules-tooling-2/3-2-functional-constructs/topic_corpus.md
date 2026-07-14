---
topic_id: 3.2
title: Functional Constructs
position_in_module: 2
generated_at: 2026-07-14T00:00:00Z
resource_count: 4
---

# 1. Functional Constructs — Topic Corpus

## 2. Prerequisites

- **3.1 Functions** — everything here builds on `def`, `return`, and especially `*args`/`**kwargs`, which is exactly what a decorator's wrapper uses to accept any function's arguments.
- **2.2 Loops** — a generator is a function that behaves like something you can loop over with `for`; you need to be comfortable with `for` before `yield` makes sense.
- **1.3 Operators & Expressions** — a lambda body is a single expression, and sort keys are usually built from comparisons you already know (`len(w)`, `abs(n)`).
- **1.2 Variables, Identifiers & Types** — you will assign functions to names and pass them around like any other value.

## 3. Learning Objectives

- Write a `lambda` expression and explain when it is preferable to a named `def` function.
- Use a lambda as the `key` argument to `sorted()` to control how a list is ordered.
- Explain what a higher-order function is and describe what `map()` and `filter()` do conceptually.
- Write a simple decorator using the `@decorator` syntax, including a `@timer` that measures a function's run time.
- Write a generator function using `yield` and explain lazy evaluation — why a generator does not compute all its values up front.

## 4. Introduction

Picture three small, everyday problems. You have a list of words and want them ordered by length, not alphabetically. You have a function that is mysteriously slow and want to know exactly how many seconds it takes, every time it runs, without littering the code with `print(time.time())` calls. You need to produce the first million Fibonacci numbers, but building the whole list in memory before you use any of them wastes time and RAM. Python has one small, reusable idea behind the fix for all three: a function is just a value. You can hand a function to another function, wrap one function around another, and even write a function that produces its values one at a time instead of all at once. This topic covers four constructs built on that single idea: lambda expressions, higher-order functions like `sorted(key=...)`, decorators, and generators. None of them require new syntax you have not already met in Topic 3.1 — they are what `def`, `return`, and `*args`/`**kwargs` were quietly preparing you for.

## 5. Core Concepts

### 5.1 Lambda (anonymous) functions

A **lambda** is a small, unnamed function written on a single line with the `lambda` keyword instead of `def`. Its syntax is `lambda parameters: expression` — no parentheses around the parameters, no `return`, and no name unless you choose to assign one [1].

```python
square = lambda n: n * n
square(5)          # 25
```

`square` here behaves exactly like a one-line `def square(n): return n * n` — the expression after the colon is automatically returned. The real value of a lambda is not naming it and calling it later; it is passing it, unnamed, directly into another function that expects a function as an argument. That is the pattern the rest of this topic is built on: `sorted(words, key=lambda w: len(w))` reads as "sort `words`, and for each one, use its length as the thing to compare" [1]. A lambda can only hold a single expression — no loops, no multiple statements, no assignment. If the logic needs more than one line, write a regular `def` function instead and pass its name.

### 5.2 Higher-order functions: `map`, `filter`, `sorted(key=...)`

A **higher-order function** is a function that takes another function as an argument, returns one, or both [2]. This is only possible because functions are values in Python — you can store one in a variable, put it in a list, or hand it to another function, exactly as you would with a number or a string.

Three higher-order functions matter here:

- **`sorted(iterable, key=...)`** returns a new, sorted list. Without `key`, items are compared directly. With `key`, Python calls your function once per item and sorts by *that result* instead of the item itself [1][2]:

```python
words = ["banana", "fig", "kiwi", "watermelon"]
sorted(words, key=lambda w: len(w))
# ['fig', 'kiwi', 'banana', 'watermelon']  -- shortest to longest
sorted(words, key=lambda w: len(w), reverse=True)
# ['watermelon', 'banana', 'kiwi', 'fig']  -- longest to shortest
```

- **`map(function, iterable)`** applies `function` to every item and hands back the results, one transformed value per input value [1][2]:

```python
numbers = [1, 2, 3, 4]
doubled = map(lambda n: n * 2, numbers)
list(doubled)        # [2, 4, 6, 8]
```

`map()` itself does not hand you a list — it hands you a `map` object that produces values as you ask for them. Wrapping it in `list(...)` forces it to produce everything right now so you can see it. This "produce on demand" behavior is the same idea generators use in section 5.4.

- **`filter(function, iterable)`** keeps only the items where `function` returns a truthy value, and drops the rest [1][2]:

```python
evens = filter(lambda n: n % 2 == 0, numbers)
list(evens)          # [2, 4]
```

In practice, `sorted(key=...)` is the one of these three you will reach for constantly — ordering results by score, by distance, by length, by any rule you can write as a one-line function. `map` and `filter` are worth recognizing when you read other people's code, but a list comprehension (a later topic) often reads more clearly for the same job. What matters now is the underlying concept: passing a small function into a built-in one to customize its behavior.

### 5.3 Decorators (light introduction)

A **decorator** is a function that takes another function and returns a new function that wraps extra behavior around it, without changing the original function's code [3]. Python gives this pattern its own syntax: writing `@my_decorator` directly above a `def` is shorthand for defining the function and then reassigning its name to `my_decorator(function)` [3].

```python
def shout(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper

@shout
def greet(name):
    return f"hello, {name}"

greet("sam")   # "HELLO, SAM"
```

Three pieces make this work, and all three are things you already have from 3.1. `shout` is a function that accepts a function (`func`) and returns a function (`wrapper`). `wrapper` is defined *inside* `shout` and is what actually replaces `greet` — when you call `greet("sam")`, you are really calling `wrapper("sam")`, which calls the original `greet` internally and does something extra with its result. And `wrapper(*args, **kwargs)` uses exactly the `*args`/`**kwargs` collecting pattern from 3.1, because a decorator has to work on *any* function, regardless of how many arguments it takes — `wrapper` cannot know in advance whether it is wrapping a function that takes zero arguments or five.

The canonical example for this topic is `@timer`, a decorator that measures how long a function takes to run [3]:

```python
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f} seconds")
        return result
    return wrapper

@timer
def slow_add(a, b):
    total = 0
    for _ in range(10_000_000):
        total += 1
    return a + b

slow_add(2, 3)
# slow_add took 0.3521 seconds
# 5
```

`slow_add` still returns `5` to its caller exactly as before — the decorator adds the timing message as a side effect without touching a single line inside `slow_add`. This is the whole appeal of decorators: behavior like timing, logging, or checking permissions can be written once and applied to any function with a one-line `@` annotation.

### 5.4 Generators: the `yield` keyword and lazy evaluation

A **generator function** looks like an ordinary function, except its body contains at least one `yield` statement instead of (or alongside) `return` [4]. Calling a generator function does not run its body immediately — it returns a **generator object**, and the body only starts running when you start pulling values out of it, most commonly with a `for` loop [4].

```python
def count_up_to(n):
    current = 1
    while current <= n:
        yield current
        current += 1

for value in count_up_to(5):
    print(value)
# 1
# 2
# 3
# 4
# 5
```

Each time execution reaches `yield`, the function hands out that value and *pauses* — everything about its state (the value of `current`, where it is in the `while` loop) is frozen exactly where it stopped. When the `for` loop asks for the next value, the function wakes up right after the `yield` and keeps going until it hits `yield` again or the function ends [4]. This is **lazy evaluation**: values are produced one at a time, only when requested, instead of an entire list being built and held in memory up front [2][4].

The classic worked example is a Fibonacci generator:

```python
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b
```

`fibonacci()` never finishes on its own — the `while True` loop runs forever — but that is fine, because nothing forces it to produce every value at once. You just take as many as you need, the same way you consume any generator: with a `for` loop, stopping yourself once you have enough:

```python
count = 0
for value in fibonacci():
    print(value)
    count += 1
    if count == 5:
        break
# 0
# 1
# 1
# 2
# 3
```

Each pass through the loop, `fibonacci()` resumes right after its `yield`, computes the next `a, b` pair, and hands out the next value — local state (`a` and `b`) persists across every pause. The `break` is what stops the loop, not the generator running out; an infinite generator never runs out on its own, so it is the caller's job to decide when enough values have been produced. Try writing this as a regular function that `return`s a list, and you hit a wall immediately: a function cannot `return` an infinite list, because it would have to finish building it first, and it never would. A generator sidesteps the problem entirely by never building the whole sequence — it only ever holds the next value to produce. That is the concrete payoff of lazy evaluation: sequences that are enormous, or infinite, or simply not needed in full become usable.

## 6. Implementation

Building a `@timer` decorator, step by step:

1. Define an outer function (`timer`) that takes one parameter: the function being decorated.
2. Inside it, define an inner function (`wrapper`) with signature `(*args, **kwargs)` so it can accept any call.
3. Inside `wrapper`, record a start time, call the original function with the same `*args, **kwargs` it received, and record an end time.
4. Report or log the elapsed time, then `return` the original function's result unchanged.
5. Have `timer` `return wrapper` (not call it).
6. Apply it with `@timer` directly above the `def` of the function you want timed.

Building a lazy generator, step by step:

1. Write a normal function signature and body.
2. Wherever the function would normally build up a value to add to a result list, use `yield <value>` instead.
3. Use a loop (`while` for an unbounded sequence, `for` for a bounded one) so the function can produce more than one value across multiple resumptions.
4. Consume the generator with a `for` loop, using a counter and `break` if the generator is unbounded.

## 7. Real-World Patterns

`sorted(..., key=lambda ...)` is the pattern you will meet constantly once you start working with real data: ranking search results by relevance score, ordering log entries by timestamp, sorting a leaderboard by highest score first. The lambda is disposable — it exists for one call to `sorted()` and is never reused, which is exactly why it does not need a name [1].

Decorators show up anywhere the same wrapping behavior needs to apply to many different functions: timing slow operations to find performance bottlenecks, logging every call to a function for debugging, or retrying a flaky operation automatically before giving up. The `@timer` example in this topic is the simplest member of that family — the same wrapper structure, with different logic inside `wrapper`, covers all of them [3].

Generators earn their keep whenever the full sequence would be wasteful or impossible to hold in memory at once: reading a huge file, streaming rows from a large dataset, or producing values from a sequence — like Fibonacci — that has no natural end. Lazy evaluation means the program only pays for the values it actually asks for [2][4].

## 8. Best Practices

- **Keep lambdas to one short expression.** If you need more than one line of logic, or the logic is reused in more than one place, write a named `def` function instead — it is easier to read, test, and debug.
- **Reach for `sorted(key=...)` before writing custom comparison logic.** It is the standard, idiomatic way to sort by a derived value in Python.
- **Always give a decorator's wrapper the signature `(*args, **kwargs)`**, unless it is meant to wrap only one specific kind of function. Otherwise it will break on any function whose arguments don't match exactly what you hardcoded.
- **A decorator should return the wrapped function's result**, not swallow it — callers of the decorated function expect the same return value they would have gotten undecorated (plus whatever side effect the decorator adds).
- **Use a generator instead of building a full list** whenever the sequence is large, unbounded, or only partially needed — it trades a small amount of extra care for real memory savings.

## 9. Hands-On Exercise

Given `words = ["python", "ai", "engineering", "loop", "yield"]`, use `sorted(words, key=lambda w: len(w))` to print them shortest to longest, then longest to shortest. Next, write the `@timer` decorator shown above and apply it to a function that sums the numbers from `1` to `5_000_000` in a loop; confirm it prints a elapsed-time message and still returns the correct sum. Finally, write a generator function `countdown(n)` that `yield`s `n, n-1, ..., 1` and drive it with a `for` loop that prints each value.

## 10. Key Takeaways

- A lambda is a single-expression, unnamed function — useful for a one-off argument to another function, not for logic that needs a name or more than one line.
- A higher-order function accepts or returns another function; `sorted(key=...)`, `map()`, and `filter()` are the built-in examples, and `sorted(key=...)` is the one you will use most.
- A decorator is a function that wraps another function and returns the wrapper; `@decorator` syntax is shorthand for `func = decorator(func)`, and a general-purpose wrapper needs `*args, **kwargs` to accept any function's signature.
- A generator function uses `yield` instead of `return` to produce values one at a time, pausing between each `yield` and resuming exactly where it left off.
- Lazy evaluation — producing values only when asked for them — is what lets a generator represent a sequence too large, or too infinite, to ever build as a complete list.

## 11. Next Steps

_System-derived from the next entry in curriculum/sequence.md._
