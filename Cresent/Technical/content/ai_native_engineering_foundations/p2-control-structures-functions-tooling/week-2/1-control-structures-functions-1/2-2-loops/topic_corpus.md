---
topic_id: 2.2
title: Loops
position_in_module: 2
generated_at: 2026-07-13T00:00:00Z
resource_count: 3
---

# 1. Loops — Topic Corpus

## 2. Prerequisites

- **1.2 Variables, Identifiers & Types** — you will store and update values across repetitions, and you will iterate over the characters of a string.
- **1.3 Operators & Expressions** — a loop's continuation test is a boolean expression built from comparison operators (`<`, `>`, `==`, `!=`) and, where needed, `and` / `or` / `not`.
- **1.4 Statements, Conversion & Output** — examples use `print()`, `input()`, and `int(...)` conversion.
- **2.1 Conditionals** — loops and `if` go together constantly: you will place an `if` inside a loop and trigger an early exit under a condition. Indentation-as-block-structure carries straight over.

## 3. Learning Objectives

After this topic you will be able to:

- **Write** a `while` loop that repeats a block as long as a condition holds, and explain how to stop it from running forever.
- **Iterate** over a sequence with a `for` loop, naming the loop variable that takes each value in turn.
- **Generate** numeric sequences with `range()` using its `start`, `stop`, and `step` arguments.
- **Use** `enumerate()` to get an index alongside each value, and `zip()` to walk two sequences in step.
- **Control** a loop from inside its body with `break` (leave early) and `continue` (skip to the next iteration).
- **Nest** one loop inside another and describe what the loop `else` clause does.

## 4. Introduction

Conditionals let a program choose a path *once*. But most real work is repetitive: print every character of a name, count down from ten to zero, check every row against every column, keep asking for input until the user finally types something valid. Writing the same statement out by hand a hundred times is absurd — and impossible when you do not know in advance how many times you will need it.

A **loop** solves this. It runs a block of code over and over, either a fixed number of times or until some condition changes. Python gives you two loop keywords: `while`, which repeats *as long as* a condition is `True`, and `for`, which repeats *once for each item* in a sequence [1]. This week's labs live entirely on these: a countdown built with `while`, a walk over a string's characters with `for` and `enumerate`, and a multiplication table built from one loop nested inside another. By the end you will have every construct those labs need.

## 5. Core Concepts

### 5.1 The `while` loop: repeat as long as a condition holds

A `while` loop has the same shape as an `if`: a header line ending in a colon, then an indented block. The difference is that after the block runs, Python goes *back* to the top and tests the condition again. It keeps repeating the block as long as the condition is `True`, and stops the moment the condition becomes `False` [1].

```python
count = 5

while count > 0:
    print(count)
    count = count - 1

print("Lift off!")
```

Read it literally: "while `count > 0` is `True`, run the block." The block prints `count` and then subtracts one from it. So it prints `5`, `4`, `3`, `2`, `1`, and when `count` reaches `0` the condition `count > 0` is `False`, the loop ends, and `print("Lift off!")` runs. That is exactly the week's **while countdown** lab.

The crucial part is the line `count = count - 1`. Something inside the loop must eventually make the condition `False`. This is the loop's *progress* toward stopping.

### 5.2 Infinite loops and how to avoid them

If the condition never becomes `False`, the loop never stops. That is an **infinite loop**, and it is the classic `while` bug [3].

```python
count = 5

while count > 0:
    print(count)
    # forgot to change count — count stays 5 forever
```

Because `count` is never decreased, `count > 0` is always `True` and the program prints `5` endlessly until you force it to quit. Avoiding this comes down to one discipline: **every `while` loop needs something in its body that moves the condition toward `False`.** Before you run a `while` loop, ask yourself: "What changes each time, and how does that eventually make the condition false?" If you cannot answer, you have an infinite loop.

An infinite loop is not always a mistake — a `while True:` loop that runs "forever" is a common pattern *when paired with a `break`* (Section 5.6) that leaves the loop on some event. The rule is simply that there must be *some* way out.

### 5.3 The `for` loop and the loop variable

A `for` loop repeats its block **once for each item in a sequence**. On each pass, a variable — the **loop variable** — is set to the next item, and the block runs with that value [1]. You do not manage a counter or a stop condition yourself; the `for` loop handles that for you by walking the sequence to its end.

A string is a sequence of characters, so you can loop over one directly:

```python
for letter in "cat":
    print(letter)
```

This prints `c`, then `a`, then `t`, each on its own line. On the first pass `letter` is `"c"`, on the second `"a"`, on the third `"t"`; after the last character the loop ends automatically. The name `letter` is your choice — `for ch in "cat":` would work identically. Pick a name that describes one item [2].

Use a `for` loop when you know the collection you are walking through. Use a `while` loop when you are repeating until a condition changes and do not know the count in advance.

### 5.4 `range()`: generating numeric sequences

Often you want to repeat something a fixed number of times, or count through numbers. `range()` produces a sequence of integers for a `for` loop to walk over [1]. It has three forms:

- `range(stop)` — counts from `0` up to but **not including** `stop`.
- `range(start, stop)` — counts from `start` up to but not including `stop`.
- `range(start, stop, step)` — counts from `start` toward `stop`, moving by `step` each time.

```python
for i in range(5):
    print(i)            # 0 1 2 3 4

for i in range(2, 6):
    print(i)            # 2 3 4 5

for i in range(0, 10, 2):
    print(i)            # 0 2 4 6 8
```

Two things trip people up. First, the `stop` value is **exclusive** — `range(5)` gives five numbers `0` through `4`, not `1` through `5` [1]. This matches how `range` pairs with the length of a sequence. Second, `step` can be negative to count *down*:

```python
for i in range(5, 0, -1):
    print(i)            # 5 4 3 2 1
```

That gives an alternative, counter-free way to write the countdown from Section 5.1. `range()` is the standard way to say "do this N times": `for i in range(3):` runs its block three times, whether or not you use `i` inside.

### 5.5 `enumerate()` and `zip()`: index-with-value and paired sequences

When you loop over a sequence you often want to know *where* you are as well as *what* the value is — the position (index) alongside the item. `enumerate()` gives you both. On each pass it hands back two things: a counter (starting at `0`) and the item itself [1][2].

```python
for index, letter in enumerate("cat"):
    print(index, letter)
```

This prints:

```
0 c
1 a
2 t
```

Here `index, letter` unpacks the two values `enumerate` produces each pass into two loop variables at once. This is the **for + enumerate** lab: reporting each character together with its position. If you want the count to start at `1` instead of `0`, pass a start value: `enumerate("cat", 1)` yields `1 c`, `2 a`, `3 t` [2].

`zip()` solves a different problem: walking **two sequences together**, one item from each per pass [1][2]. It pairs up the first item of each, then the second, and so on:

```python
for letter, digit in zip("abc", "123"):
    print(letter, digit)
```

This prints `a 1`, then `b 2`, then `c 3`. `zip` stops at the end of the **shorter** sequence, so pairing `"abcd"` with `"12"` yields only two pairs [2]. Use `zip` whenever two sequences are meant to be read side by side.

### 5.6 `break` and `continue`: controlling the loop from inside

Sometimes you need to change a loop's flow from within its body. Two keywords do this [1]:

- **`break`** immediately **leaves the loop entirely** — no more iterations, execution jumps to the first statement after the loop.
- **`continue`** **skips the rest of the current iteration** and goes straight to the next one.

`break` is what turns a deliberate `while True:` into a controlled loop. It is the tool behind the **break/continue** lab — for example, stop searching once you find what you want:

```python
for letter in "python":
    if letter == "h":
        print("Found h — stopping.")
        break
    print(letter)
```

This prints `p`, `y`, `t`, then hits `h`, prints the message, and `break` ends the loop — the `o` and `n` are never reached. Notice the `if` inside the loop: this is where conditionals and loops combine.

`continue` skips forward without leaving:

```python
for i in range(6):
    if i % 2 == 0:
        continue
    print(i)            # 1 3 5
```

When `i` is even, `continue` jumps to the next pass before reaching the `print`, so only odd numbers are printed. `break` says "I am done with this loop"; `continue` says "I am done with *this one pass*, move on."

### 5.7 Nested loops

A loop's body can contain anything — including another loop. A loop inside a loop is a **nested loop** [3]. For every single pass of the outer loop, the inner loop runs all the way through. This is how you produce a grid or table, pairing every value on the outside with every value on the inside.

```python
for row in range(1, 4):
    for col in range(1, 4):
        print(row * col, end=" ")
    print()
```

The outer loop sets `row` to `1`, `2`, `3` in turn. For each `row`, the inner loop runs `col` through `1`, `2`, `3`, printing `row * col`. The `end=" "` keeps the products on one line separated by spaces, and the bare `print()` after the inner loop moves to a new line for the next row. The output is a multiplication table — exactly the week's **nested loops multiplication table** lab:

```
1 2 3
2 4 6
3 6 9
```

If the outer loop runs `n` times and the inner runs `m` times, the inner body runs `n × m` times in total. Keep nesting shallow: two levels are common, but each added level multiplies the work and the difficulty of reading it.

### 5.8 The loop `else` clause (brief)

Python allows an optional `else` attached to a loop. The loop `else` block runs **only if the loop finished normally** — that is, without being stopped by a `break` [1]. If a `break` fired, the `else` is skipped.

```python
for letter in "cat":
    if letter == "z":
        print("Found z.")
        break
else:
    print("No z in the word.")
```

Because `"cat"` contains no `"z"`, the `break` never fires, the loop runs to its end, and the `else` prints `No z in the word.` Had the word contained a `"z"`, the `break` would have run and the `else` would have been skipped. The loop `else` is a compact way to say "do this if we searched the whole sequence and never found what we were looking for." It is a niche feature — recognise it when you see it, and reach for it only when it genuinely reads more clearly than a flag variable.

## 6. Implementation

A recipe for choosing and building the right loop:

1. **Do you know how many times, or over what?** If you are walking a known sequence (a string, a `range`), use a `for` loop. If you are repeating until a condition changes and the count is unknown, use a `while` loop.
2. **For a `while` loop, identify the progress step.** What changes each pass, and how does it eventually make the condition `False`? Write that line before you run it — this is your guard against an infinite loop.
3. **For a `for` loop, name the loop variable** after one item (`letter`, `i`, `row`). Use `range()` for counting, `enumerate()` when you also need the index, `zip()` when you are walking two sequences together.
4. **Add control flow if needed.** Use `break` to leave as soon as a condition is met; use `continue` to skip passes that do not apply. These usually sit under an `if` inside the loop.
5. **Nest only when the problem is a grid or pairing**, and keep it to two levels where you can.

Worked example — the while countdown with a clean exit:

```python
count = int(input("Count down from: "))

while count > 0:
    print(count)
    count = count - 1
print("Done.")
```

`int(...)` converts the text from `input()` into a number (topic 1.4). Each pass prints `count` and decreases it, so the condition marches toward `False` and the loop always ends.

## 7. Real-World Patterns

- **Input validation.** A `while` loop keeps re-asking until the input is acceptable: `while True:` read input, and `break` once it passes a check — otherwise loop again. This is the everyday reason to write a `while True:` with a `break`.
- **Search.** Loop over a sequence, `break` the moment you find the target, and use the loop `else` to handle "not found."
- **Counting and totals.** A `for i in range(...)` loop that accumulates a running number in a variable underlies progress counters, sums, and averages.
- **Grids and tables.** Nested loops generate anything two-dimensional — multiplication tables, coordinate pairs, rows-and-columns reports.

## 8. Best Practices

- **Guarantee progress in every `while` loop.** Something in the body must move the condition toward `False`, or use a deliberate `break`. Never leave a loop with no way out by accident.
- **Prefer `for` when you know the sequence.** It manages the counter and the stopping for you, so it cannot run away like a mis-written `while`.
- **Use `range(len)` thinking sparingly** — reach for `enumerate()` when you want index *and* value, and `zip()` when you want two sequences in step. They read more clearly than manual index bookkeeping.
- **Keep nesting shallow.** Two levels are fine; three or more usually signals it is time to rethink the structure.
- **Use `break` and `continue` to simplify, not to obscure.** A well-placed `break` can replace an awkward flag; overusing them scattered through a long body makes flow hard to trace.
- **Name loop variables for what they hold.** `for letter in word:` and `for i in range(n):` tell the reader what each pass represents.

## 9. Hands-On Exercise

Ask the user for a word. First, use a `for` loop with `enumerate()` to print each character with its position number starting at `1`. Then loop over the word again and, using `break`, stop and report the position of the first vowel you find (`a`, `e`, `i`, `o`, `u`); attach a loop `else` that prints "no vowels found" if the loop completes without a `break`. Finally, use nested loops with `range()` to print a small multiplication table up to the length of the word.

## 10. Key Takeaways

- A `while` loop repeats as long as its condition is `True`; every `while` loop must contain something that eventually makes the condition `False` (or a `break`), or it runs forever.
- A `for` loop runs once per item in a sequence, binding each item to the loop variable in turn; use it to walk a string or a `range()`.
- `range()` produces integers with `start`, `stop`, and `step` arguments, where `stop` is exclusive and `step` may be negative to count down.
- `enumerate()` pairs each item with an index, and `zip()` walks two sequences together, stopping at the shorter one.
- `break` leaves a loop immediately; `continue` skips to the next iteration; a loop `else` runs only when the loop finishes without a `break`.
- Nested loops run the inner loop fully for each pass of the outer loop, producing grids and tables — keep the nesting shallow.

## 11. Next Steps

_System-derived from the next entry in curriculum/sequence.md._
