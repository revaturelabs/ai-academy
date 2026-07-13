---
topic_id: 1.3
title: Operators & Expressions
position_in_module: 3
generated_at: 2026-07-13T00:00:00Z
resource_count: 3
---

# 1. Operators & Expressions — Topic Corpus

## 2. Prerequisites

- **1.1 The Python Environment** — you should be able to type code into a Colab cell, run it against the runtime, and read the output with `print()`.
- **1.2 Variables, Identifiers & Types** — you should be comfortable creating variables with the assignment operator `=`, reassigning them, following the `snake_case` naming convention, and recognizing the four basic types `int`, `float`, `str`, and `bool` (and that `True` and `False` are the two `bool` values). You will also use `type()` to inspect results here, and you will lean on the fact that Python is dynamically typed — a variable simply holds whatever value you last assigned.

## 3. Learning Objectives

By the end of this topic you will be able to:

- Use Python's arithmetic operators — `+`, `-`, `*`, `/`, `//`, `%`, and `**` — and explain how true division differs from floor division, including how each behaves with negative numbers.
- Predict how Python evaluates an expression by applying operator precedence, and control that order deliberately with parentheses.
- Compare two values with `==`, `!=`, `<`, `>`, `<=`, and `>=`, recognize that a comparison produces a `bool` result, and read a chained comparison such as `1 < x < 10`.
- Combine conditions with the logical operators `and`, `or`, and `not`, explain the precedence among them, and explain what short-circuit evaluation does and why it is useful.
- Identify which values Python treats as truthy and which as falsy, and explain how truthiness feeds the logical operators.

## 4. Introduction

In topic 1.2 you learned to name values and check their types. But a program that only stores values does not *do* anything with them. The moment you want to add a price to a tax, check whether a score passed a threshold, count off every third item, or decide "is the cart empty *and* is the user logged in" — you need **operators**.

An **operator** is a symbol (or a short keyword) that combines values to produce a new value. `+` adds. `==` checks whether two things are equal. `and` combines two yes/no conditions into one. When you put values, variables, and operators together into something Python can evaluate down to a single value, you have written an **expression**. `3 + 4` is an expression; so is `age >= 18`; so is `is_weekend and not is_raining`. Everything a program computes is built out of expressions, and expressions are built out of operators.

This topic covers the five ideas you will use in almost every program: arithmetic, the rules for which operator runs first (precedence), comparison, logical operators, and truthiness — how Python decides whether a value counts as "true" or "false." These are the tools that let your code make decisions. Every comparison and logical expression you write here produces a `bool`, and those booleans will drive the decisions your programs make later. For now the goal is to become fluent at writing an expression and predicting exactly what it evaluates to before you even run it.

## 5. Core Concepts

An **expression** is any piece of code that Python can evaluate to produce a single value [1]. When Python runs an expression, it works out the value and hands it back — you can print it, store it in a variable, or feed it into another, larger expression. `2 + 3` is an expression that evaluates to `5`. `2 + 3 > 4` is a bigger expression that first evaluates `2 + 3` to `5` and then evaluates `5 > 4` to `True`. This "evaluate down to one value" behavior is the whole game: every operator below takes one or more values (its **operands**) and produces a result you can use [1][3].

### 5.1 Arithmetic operators

Arithmetic operators do the math you would expect, on `int` and `float` values [1][3]:

| Operator | Name | Example | Result |
|----------|------|---------|--------|
| `+` | addition | `7 + 3` | `10` |
| `-` | subtraction | `7 - 3` | `4` |
| `*` | multiplication | `7 * 3` | `21` |
| `/` | true division | `7 / 2` | `3.5` |
| `//` | floor division | `7 // 2` | `3` |
| `%` | modulo (remainder) | `7 % 2` | `1` |
| `**` | exponentiation | `7 ** 2` | `49` |

**Addition, subtraction, multiplication.** These are the familiar three, and they behave exactly as they did in arithmetic class [1]:

```python
print(7 + 3)
print(7 - 3)
print(7 * 3)
```

Output:

```
10
4
21
```

One detail worth noticing early: the *type* of the result depends on the types of the operands. If both operands are `int`, the result of `+`, `-`, or `*` is an `int`. But the moment even one operand is a `float`, the result "promotes" to a `float` — Python quietly widens the answer to keep the fractional information [1][3]. This is sometimes called mixed-type arithmetic:

```python
print(7 + 3)
print(7 + 3.0)
print(2 * 4)
print(2 * 4.0)
print(type(7 + 3))
print(type(7 + 3.0))
```

Output:

```
10
10.0
8
8.0
<class 'int'>
<class 'float'>
```

Read this as: `int` plus `int` stays an `int`; `int` plus `float` becomes a `float`. Because you already met `type()` in 1.2, you can always confirm which kind of number you ended up with [1].

**True division vs floor division.** This is the one place Python surprises newcomers. The single slash `/` is **true division**: it always gives you the full answer, with a decimal part, as a `float` — even when the numbers divide evenly [1].

```python
print(7 / 2)
print(6 / 2)
print(10 / 5)
```

Output:

```
3.5
3.0
2.0
```

Notice that `6 / 2` gives `3.0`, not `3`, and `10 / 5` gives `2.0`, not `2`. True division *always* produces a `float`, even when the mathematical result is a whole number [1]. This is deliberate and consistent: you never have to guess whether `/` will hand you an `int` or a `float` — it is always a `float`.

The double slash `//` is **floor division**: it divides and then rounds *down* to the nearest whole number, discarding the fractional part [1][3].

```python
print(7 // 2)
print(6 // 2)
print(20 // 6)
```

Output:

```
3
3
3
```

Read `//` as "how many whole times does the second number fit into the first?" Seven contains two 2s fully (with 1 left over), so `7 // 2` is `3`. Twenty contains three 6s fully (18), with 2 left over, so `20 // 6` is `3`. Floor division is what you want when a fractional answer makes no sense — you cannot seat 3.5 people at a table, and you cannot fill 3.33 boxes with 6 items each.

The precise definition of `//` is not "chop off the decimal" but "round *toward negative infinity*" — always downward on the number line, never toward zero [2]. For positive numbers the two descriptions agree, but for negative numbers they differ, and this is where beginners get caught:

```python
print(7 // 2)
print(-7 // 2)
print(7 // -2)
```

Output:

```
3
-4
-4
```

Read `-7 // 2` carefully: the true answer is `-3.5`, and rounding *down* (toward negative infinity) gives `-4`, not `-3`. If Python simply chopped off the decimal it would give `-3`, but it rounds toward negative infinity instead, so you get `-4`. Keep this in mind whenever floor division touches a negative value.

**Modulo.** The `%` operator gives the **remainder** left over after floor division [1][3]. Since `7 // 2` is `3` with `1` left over, `7 % 2` is `1`. The remainder and the floor division always fit together: `(a // b) * b + (a % b)` reconstructs `a`.

```python
print(7 % 2)
print(8 % 2)
print(10 % 3)
print(20 % 6)
```

Output:

```
1
0
1
2
```

Modulo has two very common uses worth remembering now. The first is the **even/odd test**: `n % 2` is `0` when `n` is even and `1` when `n` is odd, because dividing by 2 leaves either nothing or exactly one over. More generally, `x % n == 0` tests whether `x` divides evenly by `n` — for example `x % 5 == 0` is `True` exactly when `x` is a multiple of 5 [3].

```python
print(10 % 2)
print(11 % 2)
print(15 % 5)
print(16 % 5)
```

Output:

```
0
1
0
1
```

The second common use is **wrap-around**: modulo keeps a number inside a fixed range `0` to `n-1`. Think of a 12-hour clock — after 12 you wrap back to 0. Any hour count taken `% 12` lands in `0..11`, and any position taken `% 7` cycles through the seven days of a week. Whenever you need something to "cycle" or "loop back around" through a fixed set of slots, modulo is the tool:

```python
print(13 % 12)
print(25 % 12)
print(8 % 7)
```

Output:

```
1
1
1
```

Modulo with negatives follows from floor division. Because Python floors toward negative infinity, the remainder always takes the sign of the *divisor* (the right operand), not the dividend [2]. That means `-7 % 2` is `1`, not `-1`:

```python
print(-7 % 2)
print(7 % -2)
```

Output:

```
1
-1
```

You do not need to reason about this every day, but you should recognize that `%` with a negative operand may not match the sign you expected — a point we return to in Section 7.

**Exponentiation.** The double asterisk `**` raises a number to a power [1][3]. `7 ** 2` is "7 squared" = `49`; `2 ** 10` is `1024`; and you can raise to fractional or larger powers too:

```python
print(7 ** 2)
print(2 ** 10)
print(5 ** 3)
```

Output:

```
49
1024
125
```

Do not confuse `**` (power) with `*` (multiply). `2 ** 3` is `8` (2×2×2), while `2 * 3` is `6`. The double asterisk means "raised to the power of," not "multiply twice."

### 5.2 Operator precedence

When an expression contains more than one operator, Python does not simply read left to right. It follows **operator precedence** — a fixed ranking that decides which operators run first [1][2]. This is the same "order of operations" you learned in arithmetic class (multiplication before addition), extended to every Python operator.

Consider:

```python
print(2 + 3 * 4)
```

Output:

```
14
```

Python does *not* compute `2 + 3` first to get `5 * 4 = 20`. Multiplication has higher precedence than addition, so `3 * 4` runs first (`12`), then `2 + 12` gives `14` [2].

Here is a precedence ladder, highest (runs first) at the top, for the operators in this topic [2]:

| Precedence | Operators | Group |
|------------|-----------|-------|
| Highest | `()` | parentheses (grouping) |
| | `**` | exponentiation |
| | `-x` | unary minus (negation) |
| | `*`, `/`, `//`, `%` | multiplication / division family |
| | `+`, `-` | addition / subtraction |
| | `<`, `<=`, `>`, `>=`, `==`, `!=` | comparisons |
| | `not` | logical NOT |
| | `and` | logical AND |
| Lowest | `or` | logical OR |

Several important facts fall out of this ladder.

**`**` binds tighter than unary minus.** Exponentiation sits *above* the negation operator, which produces a result that catches many people out [2]:

```python
print(-2 ** 2)
print((-2) ** 2)
```

Output:

```
-4
4
```

Read `-2 ** 2` as "negate the result of `2 ** 2`." Python computes `2 ** 2 = 4` first, then applies the leading minus to get `-4`. To square the *negative* number you must write `(-2) ** 2`, which is `4`. The parentheses force the negation to happen before the power.

**The multiplication family beats addition/subtraction.** `*`, `/`, `//`, and `%` all sit above `+` and `-`, so they run first:

```python
print(2 + 6 / 3)
print(10 - 2 * 3)
print(7 + 8 % 3)
```

Output:

```
4.0
4
9
```

In the first line `6 / 3` (which is `2.0`) runs before the `+`, giving `2 + 2.0 = 4.0`. In the second, `2 * 3` runs before the `-`, giving `10 - 6 = 4`. In the third, `8 % 3` (which is `2`) runs before the `+`, giving `7 + 2 = 9`.

**Arithmetic runs before comparison, and comparison runs before logic.** All the arithmetic runs before any comparison, and comparisons run before the logical operators — so `2 + 3 > 4 and 1 < 2` is read as `((2 + 3) > 4) and (1 < 2)`, i.e. `(5 > 4) and (1 < 2)`, i.e. `True and True`, i.e. `True` [2]. And when two operators have the *same* precedence (like `*` and `/`, or `+` and `-`), Python evaluates them left to right, a rule called left-associativity [2]:

```python
print(20 / 4 * 2)
print(20 - 4 - 2)
```

Output:

```
10.0
14
```

`20 / 4 * 2` is read left to right as `(20 / 4) * 2 = 5.0 * 2 = 10.0`, *not* `20 / (4 * 2) = 2.5`. Likewise `20 - 4 - 2` is `(20 - 4) - 2 = 14`.

**Evaluate one by hand.** Take `2 + 3 * 4 ** 2 - 1`. Working strictly down the ladder: `**` first, so `4 ** 2 = 16`; then `*`, so `3 * 16 = 48`; then left to right for `+` and `-`, so `2 + 48 = 50`, then `50 - 1 = 49`. Run it to confirm:

```python
print(2 + 3 * 4 ** 2 - 1)
```

Output:

```
49
```

**Use parentheses to control evaluation.** You do not have to memorize the whole ladder. Any time you are unsure — or any time the intent is not obvious at a glance — wrap the part you want done first in parentheses. Parentheses have the highest precedence, so they always win [1][2]:

```python
print(2 + 3 * 4)
print((2 + 3) * 4)
```

Output:

```
14
20
```

The parentheses in `(2 + 3) * 4` force the addition first, giving `5 * 4 = 20`. Even when parentheses are not strictly required, adding them to make the order clear is good style — it costs nothing and removes doubt for the next reader [2].

### 5.3 Comparison operators

A **comparison operator** compares two values and produces a `bool` — either `True` or `False` [1][3]. This is the bridge between raw values and decisions: a comparison is a question, and Python answers it with yes (`True`) or no (`False`).

| Operator | Meaning | Example | Result |
|----------|---------|---------|--------|
| `==` | equal to | `5 == 5` | `True` |
| `!=` | not equal to | `5 != 3` | `True` |
| `<` | less than | `3 < 5` | `True` |
| `>` | greater than | `3 > 5` | `False` |
| `<=` | less than or equal to | `5 <= 5` | `True` |
| `>=` | greater than or equal to | `3 >= 5` | `False` |

```python
print(5 == 5)
print(5 != 3)
print(3 < 5)
print(5 >= 10)
print(4 <= 4)
print(9 > 2)
```

Output:

```
True
True
True
False
True
True
```

Every one of those lines evaluates to a `bool`, and you can prove it with `type()` [1]:

```python
result = 3 < 5
print(result)
print(type(result))
```

Output:

```
True
<class 'bool'>
```

**Comparisons work on more than numbers.** `==` and `!=` also work on other values — for instance, two `str` values are equal only if they are exactly the same text, character for character. String comparison is case sensitive, just as identifiers and keywords were case sensitive in 1.2 [3]:

```python
print("cat" == "cat")
print("cat" == "Cat")
print("cat" != "dog")
```

Output:

```
True
False
True
```

**The single most common beginner bug** is confusing `==` with `=`. They are different operators for different jobs. A single `=` is the **assignment** operator you met in 1.2 — it stores a value in a variable and produces no answer you can print. A double `==` is the **equality comparison** — it asks a question and gives back `True` or `False`. `x = 5` puts `5` into `x`; `x == 5` asks "does `x` currently equal `5`?" [1]

```python
age = 20
print(age == 20)
print(age == 21)
```

Output:

```
True
False
```

**Comparison chaining.** Python lets you chain comparisons the way mathematics does. Instead of writing `18 <= age and age < 65`, you can write `18 <= age < 65`, and Python reads it as "is `age` between 18 and 65?" — evaluating each comparison and combining them for you [1][2]:

```python
x = 7
print(1 < x < 10)
print(0 < x < 5)
print(10 <= x <= 20)
```

Output:

```
True
False
False
```

Read `1 < x < 10` as "is `x` greater than 1 *and* less than 10?" Because `x` is `7`, the first line is `True`; the second is `False` because `7` is not below `5`; the third is `False` because `7` is not at least `10`. Chaining is a convenience that makes range checks read naturally, and each link in the chain still produces a `bool` [2].

### 5.4 Logical operators

**Logical operators** combine or invert `bool` values so you can express compound conditions — "this *and* that," "this *or* that," "*not* this" [1][3]. There are exactly three: `and`, `or`, and `not`. Note that these are plain English words, not symbols.

- `A and B` is `True` only when **both** `A` and `B` are true.
- `A or B` is `True` when **at least one** of `A` or `B` is true.
- `not A` flips the value: `not True` is `False`, `not False` is `True`.

The behavior of `and` and `or` is easiest to see as a small truth table. For every combination of two truth values:

| `A` | `B` | `A and B` | `A or B` |
|-----|-----|-----------|----------|
| `True` | `True` | `True` | `True` |
| `True` | `False` | `False` | `True` |
| `False` | `True` | `False` | `True` |
| `False` | `False` | `False` | `False` |

And `not` simply inverts a single value: `not True` is `False`, and `not False` is `True`. Confirm the rows in code:

```python
print(True and True)
print(True and False)
print(True or False)
print(False or False)
print(not True)
print(not False)
```

Output:

```
True
False
True
False
False
True
```

**Precedence among the logical operators.** The three do not all bind equally tightly. Their order, highest to lowest, is `not`, then `and`, then `or` [2]. This means `not` grabs its operand first, `and` groups before `or`, and you can often read a compound condition without extra parentheses if you keep that order in mind:

```python
print(True or False and False)
print(not False and True)
```

Output:

```
True
True
```

In the first line, `and` binds tighter than `or`, so Python reads it as `True or (False and False)` = `True or False` = `True` — *not* `(True or False) and False`, which would be `False`. In the second, `not` binds tightest, so it is `(not False) and True` = `True and True` = `True`. When the grouping matters and is not obvious, add parentheses.

**Combining logical operators with comparisons.** In practice you rarely type `True and False` literally — you combine *comparisons*, which each produce a `bool`. Recalling the precedence ladder from 5.2, comparisons run before the logical operators, so this reads naturally without extra parentheses [2]:

```python
age = 25
has_ticket = True
print(age >= 18 and has_ticket)
print(age < 13 or age >= 65)
```

Output:

```
True
False
```

Python evaluates `age >= 18` to `True`, leaves `has_ticket` as `True`, and `True and True` is `True` — so the person may enter. In the second line, `age < 13` is `False` and `age >= 65` is `False`, so `False or False` is `False` — a 25-year-old qualifies for neither the child nor the senior category.

### 5.5 Short-circuit evaluation

The logical operators are lazy in a useful way, a behavior called **short-circuit evaluation**. Python evaluates the left side first and *stops early* if the answer is already decided [1].

- For `and`: if the left side is falsy, the whole expression cannot be true, so Python returns the result without even looking at the right side.
- For `or`: if the left side is truthy, the whole expression is already true, so Python skips the right side.

The cleanest way to *prove* which side ran is to put something dangerous on the right — an expression that would crash if it were evaluated. The `10 / 0` below would normally raise a division-by-zero error:

```python
print(False and (10 / 0))
print(True or (10 / 0))
```

Output:

```
False
True
```

In the first line the left side of `and` is already `False`, so Python never evaluates the right side — no crash, and the result is `False` [1]. In the second line the left side of `or` is already `True`, so again the risky right side is skipped and the result is `True`. If short-circuiting did *not* happen, both lines would crash.

Contrast that with the cases where the right side *must* run because the left side did not settle the question:

```python
print(True and 5)
print(False or 9)
```

Output:

```
5
9
```

In `True and 5`, the left side is truthy so the outcome still depends on the right side, and Python evaluates it (returning `5`). In `False or 9`, the left side is falsy so `or` must look right, and it returns `9`. Short-circuiting is not a trick; it is a tool. You can put a cheap or protective check on the left and a more expensive or riskier check on the right, and rely on Python to skip the right side when it is safe to do so [1]. This is exactly why the order of your conditions can matter.

### 5.6 Boolean values and truthiness

You already know the two `bool` values from 1.2: `True` and `False`. What is new here is that Python will treat **any** value as either "true-ish" or "false-ish" when it is used in a logical context. This is called **truthiness** [1][3].

The rule is short. These values are **falsy** (treated as false):

- `False`
- the number zero: `0` and `0.0`
- the empty string: `""`

Almost everything else is **truthy** (treated as true): any non-zero number (`1`, `-5`, `3.14`), and any non-empty string (`"hi"`, and even `"False"` written as text — because it is a non-empty string, not the boolean `False`) [3].

You can see how Python categorizes a value using `not`, which forces truthiness evaluation and hands back a real `bool` — comparisons and logical operators already return genuine booleans, and truthiness is what governs how a *bare* value behaves inside `and`, `or`, and `not`:

```python
print(not 0)
print(not 5)
print(not "")
print(not "hi")
print(not 0.0)
print(not -3)
```

Output:

```
True
False
True
False
True
False
```

Read `not 0` as "not falsy" → `True`, and `not 5` as "not truthy" → `False`. Note that `-3` is truthy: falsiness is about being *zero*, not about being negative. And `0.0` is falsy just like `0`.

**How truthiness feeds the logical operators.** Because `and`, `or`, and `not` operate on truthiness, you can put bare values (not just comparisons) inside them. When you do, `and` and `or` actually return *one of the original operands*, chosen by the short-circuit rule from 5.5, rather than a plain `True`/`False` [1][3]:

```python
print("" or "default")
print("typed" or "default")
print("hi" and "world")
print(0 and 99)
```

Output:

```
default
typed
world
0
```

Trace each one. `"" or "default"`: the empty string on the left is falsy, so `or` must return the right side, `"default"`. `"typed" or "default"`: the left is truthy, so `or` short-circuits and returns `"typed"`. `"hi" and "world"`: the left is truthy, so `and` depends on the right and returns `"world"`. `0 and 99`: the left is falsy, so `and` short-circuits and returns `0`. For now the essential takeaway is simpler than the mechanics: know *which values are falsy* — the short list above — and understand that everything else is truthy, and that these truthy/falsy verdicts are what `and`, `or`, and `not` react to [3]. These boolean results will drive decisions in your programs later.

## 6. Implementation

A dependable way to build and check any expression is a short routine you can repeat:

1. Write the values and operators, and mentally apply the precedence ladder (5.2) to predict the result.
2. If the order is not obvious, add parentheses to make your intent explicit.
3. Run it in a Colab cell and `print()` the result.
4. If a comparison or logical result surprises you, `print(type(...))` — remember comparisons return a `bool`, arithmetic returns a number, and `/` specifically returns a `float`.

### 6.1 Arithmetic playground

Type these into a cell and run them. Predict each answer *before* you look:

```python
print(17 / 5)
print(17 // 5)
print(17 % 5)
print(2 ** 5)
print(3 + 4 * 2)
print((3 + 4) * 2)
```

Output:

```
3.4
3
2
32
11
14
```

Notice `17 / 5` is a `float` (`3.4`), `17 // 5` drops the fraction (`3`), and `17 % 5` is the remainder (`2`) — and `3 = 17 // 5` fits into `17` three times with `2` left over, so the floor division and modulo agree. The last two lines show precedence in action: without parentheses `*` beats `+` (`11`); with parentheses the addition goes first (`14`) [1][2].

Now push on the surprising edges — mixed types and negatives:

```python
print(10 / 2)
print(10 + 2.0)
print(-7 // 2)
print(-7 % 2)
print(-2 ** 2)
print((-2) ** 2)
```

Output:

```
5.0
12.0
-4
1
-4
4
```

`10 / 2` is `5.0`, not `5`, because true division always returns a `float`; `10 + 2.0` promotes to `12.0` because one operand is a `float`; `-7 // 2` rounds toward negative infinity to `-4`; `-7 % 2` is `1` (the remainder takes the divisor's sign); and `-2 ** 2` is `-4` because `**` binds tighter than the leading minus, while `(-2) ** 2` is `4` [1][2].

### 6.2 Precedence by parentheses

Take the *same* operands and change only the parentheses to see how the answer moves:

```python
print(2 + 3 * 4)
print((2 + 3) * 4)
print(2 * 3 + 4)
print(2 * (3 + 4))
print(100 / 5 / 2)
print(100 / (5 / 2))
```

Output:

```
14
20
10
14
10.0
40.0
```

The first pair shows `*` beating `+`, then parentheses overriding it. The middle pair does the same with the multiplication on the left. The last pair is the associativity lesson: `100 / 5 / 2` runs left to right as `(100 / 5) / 2 = 10.0`, but `100 / (5 / 2)` forces the right division first, giving `100 / 2.5 = 40.0` [2]. Whenever the grouping changes the answer, parentheses are earning their keep.

### 6.3 Building a compound boolean condition

Here we assemble a realistic "may this user enter?" condition step by step, storing intermediate booleans in well-named variables (recall `snake_case` from 1.2):

```python
score = 85
is_member = True
is_banned = False

passed = score >= 60
print(passed)
print(type(passed))

in_range = 60 <= score <= 100
print(in_range)

may_enter = passed and is_member and not is_banned
print(may_enter)
```

Output:

```
True
<class 'bool'>
True
True
```

`score >= 60` produces the `bool` `True`, which we stored in `passed`, and `type()` confirms it is a `bool` [1]. `60 <= score <= 100` is a chained comparison asking "is the score in the range 60–100?" — `True` here [2]. Finally `may_enter` combines three booleans: the person passed, is a member, and is *not* banned. Because `not` binds tighter than `and`, `not is_banned` is evaluated first (to `True`), and `True and True and True` is `True` [2].

### 6.4 Observing short-circuit evaluation

```python
user_typed = ""
print(user_typed != "" and user_typed == "yes")

fallback = user_typed or "guest"
print(fallback)
```

Output:

```
False
guest
```

In the first line the left condition `user_typed != ""` is `False` (the string is empty), so `and` short-circuits and the right condition is never checked [1]. This pattern — "first make sure there *is* a value, then look at what it is" — is one you will use often, and it depends on short-circuiting to be safe. In the second line, `user_typed` is the empty string (falsy), so `or` returns the right operand `"guest"`: a compact way to supply a default when a value is missing [1][3].

## 7. Real-World Patterns / Common Pitfalls

These are the mistakes that actually trip up beginners, each drawn straight from the concepts above.

**Using `=` when you mean `==`.** This is the number-one beginner bug and it ties straight back to the assignment operator from 1.2. `=` *assigns* a value into a variable; `==` *compares* two values and yields a `bool` [1]. `count = 5` changes `count`; `count == 5` asks a question. If your code seems to "always do the same thing" regardless of the data, or a value you expected to stay put has silently changed, check whether you typed one equals sign where you needed two.

**Expecting `/` to give a whole number.** `10 / 2` is `5.0`, not `5` — true division *always* returns a `float`, even for a clean division [1]. If you are counting how many whole groups fit, or you specifically need an `int`-looking whole number, use floor division `//`. Conversely, if you use `//` and are surprised to lose the fraction, switch back to `/`. Matching the operator to the meaning of your problem is the fix.

**Floor division and modulo with negatives.** Because `//` rounds toward negative infinity rather than toward zero, `-7 // 2` is `-4`, not `-3` [2]. And because the remainder follows the *divisor's* sign, `-7 % 2` is `1`, not `-1`. If you are doing arithmetic that can go negative — offsets, coordinates, differences — do not assume the result matches what a calculator that truncates toward zero would show. Print a couple of sample values at the boundaries to confirm.

**Precedence bugs fixed by parentheses.** The classic is squaring a negative: `-2 ** 2` is `-4` because `**` outranks unary minus; you need `(-2) ** 2` to get `4` [2]. Another is mixing arithmetic with comparison or logic and assuming left-to-right reading. Because arithmetic runs before comparison and comparison before `and`/`or`, an expression like `2 + 3 == 5 and 1 < 2` happens to work as intended — but the moment you are unsure, add parentheses: `((2 + 3) == 5) and (1 < 2)`. Explicit grouping never changes a *correct* result and often prevents an incorrect one [2].

**Getting `and`/`or` precedence backwards.** `and` binds tighter than `or`, so `True or False and False` is `True` (it reads as `True or (False and False)`), not `False` [2]. When a compound condition mixes `and` and `or`, group the parts explicitly so the reader — and you, six months from now — does not have to recall the ladder.

**Misreading chained comparisons.** `1 < x < 10` is a real range check meaning "`x` is above 1 and below 10" [2]. Beginners sometimes expect it to compare `1 < x` and then compare that boolean against `10`, but Python does the mathematically sensible thing and links the comparisons. It is fine to use, just read it as the range test it is.

**Relying on the truthiness of empty values.** Using a bare value as a condition leans on truthiness: `""`, `0`, and `0.0` are falsy, everything else truthy [3]. This is convenient — `name or "guest"` neatly supplies a default — but it can bite you when a legitimate value happens to be falsy. If `0` is a *valid* quantity, testing the value's truthiness will wrongly treat it as "missing," when you really meant to check whether a value was *provided*. When zero (or an empty string) is a real, meaningful value rather than a stand-in for "nothing," prefer an explicit comparison like `x == 0` over relying on truthiness [1][3].

## 8. Best Practices

- **Do** use parentheses whenever an expression mixes operators from different precedence levels — clarity beats cleverness, and parentheses cannot make a correct expression wrong [2].
- **Do** remember that `/` returns a `float` and `//` returns a floored whole number; pick the one that matches the meaning of your problem [1].
- **Don't** confuse `=` (assign) with `==` (compare) — this is the number-one beginner bug and it traces straight back to the assignment you learned in 1.2 [1].
- **Do** lean on `x % 2` to test even/odd and `x % n == 0` to test divisibility, and reach for `%` when you need a value to wrap around a fixed range [3].
- **Do** keep the falsy list in mind — `False`, `0`, `0.0`, `""` — and treat everything else as truthy [3].
- **Do** rely on short-circuit evaluation to guard a risky right-hand side behind a safe left-hand check, and remember the *order* of your conditions can therefore matter [1].
- **Do** watch floor division and modulo when negatives are in play — the rounding is toward negative infinity, not toward zero [2].

## 9. Hands-On Exercise

In a Colab cell, set `total = 17` and `groups = 5`. Print `total / groups`, `total // groups`, and `total % groups`, and explain to yourself why each result looks the way it does (and confirm that the floor division times `groups` plus the remainder gives back `17`). Then create `score = 72` and `attended = True`, and print a single expression that is `True` only when the score is at least 60 *and* the student attended. Rewrite the range part as a chained comparison `60 <= score <= 100`. Finally, print `not 0`, `not ""`, `not "x"`, and `-2 ** 2` versus `(-2) ** 2`, and confirm each result against the falsy/truthy and precedence rules above.

## 10. Key Takeaways

- Arithmetic operators include `+ - * **`, plus two kinds of division: `/` (true division, always a `float`) and `//` (floor division, rounds toward negative infinity), and `%` (remainder, whose sign follows the divisor); mixing an `int` with a `float` promotes the result to `float` [1].
- Operator precedence fixes which operator runs first (`**` before unary minus, `*`/`/`/`//`/`%` before `+`/`-`, arithmetic before comparison, comparison before logical, and `not` before `and` before `or`); parentheses override it and make intent clear [1][2].
- Comparison operators (`==`, `!=`, `<`, `>`, `<=`, `>=`) each produce a `bool`, can be chained as in `1 < x < 10`, and must not be confused with `=` (assign) versus `==` (compare) [1][3].
- Logical operators `and`, `or`, and `not` combine or invert conditions using short-circuit evaluation, skipping the right side when the result is already decided [1].
- Truthiness means every value acts as true or false in a logical context: `False`, `0`, `0.0`, and `""` are falsy; everything else is truthy — and that verdict is what `and`, `or`, and `not` react to [3].

## 11. Next Steps

_System-derived from the next entry in curriculum/sequence.md._
