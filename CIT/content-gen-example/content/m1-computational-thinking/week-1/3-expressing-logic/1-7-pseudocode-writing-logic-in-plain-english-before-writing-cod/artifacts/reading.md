<!-- nav:top:start -->
[⬅ Previous: 1.6 — Abstraction](../../../2-problem-solving-foundations/1-6-abstraction-hiding-complexity-at-the-right-level/artifacts/reading.md)&emsp;·&emsp;[⬆ Table of Contents](../../../../../../../README.md#curriculum-topic-index)&emsp;·&emsp;[Next: 1.8 — Flowcharts ➡](../../1-8-flowcharts-visualising-logic-with-standard-shapes-and-arrows/artifacts/reading.md)
<!-- nav:top:end -->

---

# Pseudocode — writing logic in plain English before writing code

## Overview

Before you write a single line of code, you need a clear plan for what that code should do. Pseudocode is a way of writing that plan in plain, structured English — step by step, without the strict rules any real programming language imposes. In earlier topics you learned that computation means taking input, processing it through defined steps, and producing output; and that decomposition breaks a big problem into smaller sub-tasks. Pseudocode is where you write those sub-tasks out clearly, so you can check your logic before committing to any language.

## Key Concepts

### What pseudocode is

**Pseudocode** — a structured, step-by-step description of a process written in plain human-readable language, not in any specific programming language.

The word "pseudo" means "not real." So pseudocode is "fake code" — it looks a bit like code because it is ordered and precise, but a computer cannot run it directly. It is a plan, written for humans to read and check first [1].

Why does this matter? Because every programming language has **syntax** — the specific punctuation and keyword rules that language requires. One misplaced colon or missing bracket can break the whole program. If you try to write real code while simultaneously figuring out your logic AND learning the language's syntax rules, you are juggling two hard problems at once. Pseudocode lets you solve one problem at a time: logic first, syntax second [2].

Here is a simple everyday example — pseudocode for making a cup of tea:

```
START
  Boil water
  Place teabag in cup
  Pour boiling water into cup
  Wait 3 minutes
  Remove teabag
  Add milk if desired
END
```

That is pseudocode. It is structured, ordered, and readable by any person — no coding knowledge needed [1].

### The three building blocks of pseudocode

Every piece of pseudocode — and every program in every language — is built from exactly three patterns. These are the **building blocks of logic**.

**Building Block 1 — Sequence**

**Sequence** — doing steps one after another, in a fixed order. This is the simplest pattern: Step 1 happens, then Step 2, then Step 3. No skipping, no branching. Just a straight line of instructions.

Example:
```
GET the user's name
PRINT "Hello, " followed by the name
```

**Building Block 2 — Decision**

**Decision** — choosing between two or more paths based on a test. A decision is also called a **conditional** or a **branch**.

The test you check is called the **condition** — for example, "is the temperature above 30 degrees?" Depending on whether the condition is true or false, a different set of steps runs.

Example:
```
IF temperature is above 30 degrees
  PRINT "It is hot outside"
OTHERWISE
  PRINT "It is not that hot"
END IF
```

**Building Block 3 — Repetition**

**Repetition** — doing a step, or a group of steps, multiple times until a condition is met.

Example:
```
WHILE there are items in the shopping cart
  Calculate the price of the next item
  Add it to the running total
END WHILE
PRINT total cost
```

The steps inside the WHILE block repeat as long as the condition is true. When no items remain, the repetition stops [2].

These three building blocks — **sequence, decision, repetition** — are the skeleton of almost every program ever written [1].

![Three Building Blocks of Pseudocode](../artifacts/diagram.png)

### Pseudocode vs. real code — a direct comparison

It helps to see both forms side by side. Here is the same logic — "check whether a number is positive" — written two ways [2][3]:

| | Pseudocode | Python (one real language) |
|---|---|---|
| Get input | `GET a number from the user` | `number = int(input("Enter a number: "))` |
| Decision | `IF the number is greater than 0` | `if number > 0:` |
| Output (true) | `PRINT "The number is positive"` | `print("The number is positive")` |
| Output (false) | `OTHERWISE PRINT "Not positive"` | `else: print("Not positive")` |

Notice: pseudocode uses plain English ("GET a number from the user"). Python uses a specific built-in (`input()`) with required syntax — the colon after `if number > 0` is not optional. The logic is identical in both; pseudocode just captures the logic without the language-specific rules.

The same pseudocode could be translated into Python, JavaScript, Java, or any other language. You write the plan once; you choose the language later [1].

### Writing conventions

There is no single official pseudocode standard. Different textbooks and teams use slightly different keywords. What matters is that your pseudocode is readable, precise, ordered, and consistent — use the same keyword for the same thing throughout.

A few widely-used conventions [1][2]:

| Concept | Common keywords |
|---|---|
| Start / end a block | `START` / `END` |
| Decision | `IF … THEN … OTHERWISE …` |
| Repeat while condition is true | `WHILE … DO … END WHILE` |
| Repeat over a collection | `FOR EACH … DO … END FOR` |
| Assign a value | `SET x TO 5` |
| Show output | `PRINT`, `DISPLAY`, `OUTPUT` |
| Get input | `GET`, `READ`, `INPUT` |

You do not need to memorise this table now. Pick a consistent set and use it throughout one document [3].

## Worked Example

Here is a complete pseudocode example that uses all three building blocks together. The problem: find the highest score in a list of exam results.

**Step 1 — State the problem in one sentence.**
Find the highest score from a list of five exam results.

**Step 2 — Identify the inputs and output.**
- Input: a list of exam scores
- Output: the single highest score

**Step 3 — Write the pseudocode.**

```
START
  SET highest_score TO 0
  FOR EACH score IN the list of exam scores
    IF score > highest_score
      SET highest_score TO score
    END IF
  END FOR
  PRINT "The highest score is: " followed by highest_score
END
```

**Step 4 — Trace through it with a real example.**

Suppose the list is: 45, 72, 61, 88, 55.

1. `highest_score` starts at 0.
2. First score: 45 > 0? Yes — set `highest_score` to 45.
3. Second score: 72 > 45? Yes — set `highest_score` to 72.
4. Third score: 61 > 72? No — `highest_score` stays 72.
5. Fourth score: 88 > 72? Yes — set `highest_score` to 88.
6. Fifth score: 55 > 88? No — `highest_score` stays 88.
7. Loop ends. Print: "The highest score is: 88." — correct.

**Where each building block appears:**

- **Sequence** — `SET`, then `FOR EACH` loop, then `PRINT` happen in that fixed order.
- **Repetition** — the `FOR EACH` block repeats once for every score in the list.
- **Decision** — the `IF` inside the loop checks whether the current score beats the stored highest.

No knowledge of Python or any other language is needed to follow this logic. That is the point [2][3].

## In Practice

Pseudocode is not just a beginner exercise. It appears regularly in professional work [3]:

- **Software design.** Before writing a feature, developers write the logic as pseudocode so the team can agree on the approach before anyone writes production code.
- **Technical interviews.** Many engineering interviews ask candidates to explain their thinking in pseudocode first. Interviewers care about your logic, not whether you remember the exact syntax of a language.
- **Cross-team communication.** A non-technical colleague can describe a business rule — for example, "if a customer has more than three failed payments, flag the account" — in pseudocode, and a developer can implement it. Both parties only need to agree on the logic [1].
- **Documentation.** Pseudocode appears in technical documents when explaining how a process works, because it is readable without knowing the implementation language.

All of these uses share one thing: pseudocode lets you communicate the *what* and *how* of a process without getting stuck on *which language* to use.

**Do and avoid — a quick reference:**

| Do | Avoid |
|---|---|
| Write pseudocode before writing code | Writing pseudocode after coding to document it (defeats the purpose) |
| One action per line | Multiple actions crammed into one line |
| Use consistent keywords throughout | Mixing keywords (IF/OTHERWISE in one place, if/else in another) |
| Indent nested blocks to show structure | Flat indentation that hides which steps belong together |
| Trace through with a real example | Assuming it works without checking |
| Stay language-independent | Using language-specific syntax (e.g., a Python colon) in pseudocode |

You will encounter flowcharts as another way to visualise logic — you will cover that in the next topic [2].

## Key Takeaways

- **Pseudocode is structured plain English** that describes the logic of a process step by step — without using any specific programming language's syntax rules.
- **The three building blocks are sequence, decision, and repetition.** Every program in any language is built from combinations of these three patterns.
- **Pseudocode separates logic from syntax.** You solve "what should happen and in what order?" first, then answer "how do I write this in Python?" second.
- **There is no single official standard**, but good pseudocode is always readable, precise, ordered, and consistent within a document.
- **Writing pseudocode before code saves time.** A logic mistake caught in pseudocode is far cheaper to fix than the same mistake found after writing a full program [1].

## References

1. Codecademy, "Pseudocode and Flowchart: Complete Beginners Guide." <https://www.codecademy.com/article/pseudocode-and-flowchart-complete-beginners-guide>
2. GeeksforGeeks, "What is Pseudocode? A Complete Tutorial." <https://www.geeksforgeeks.org/dsa/what-is-pseudocode-a-complete-tutorial/>
3. Built In, "Pseudocode." <https://builtin.com/data-science/pseudocode>

---
<!-- nav:bottom:start -->
[⬅ Previous: 1.6 — Abstraction](../../../2-problem-solving-foundations/1-6-abstraction-hiding-complexity-at-the-right-level/artifacts/reading.md)&emsp;·&emsp;[⬆ Table of Contents](../../../../../../../README.md#curriculum-topic-index)&emsp;·&emsp;[Next: 1.8 — Flowcharts ➡](../../1-8-flowcharts-visualising-logic-with-standard-shapes-and-arrows/artifacts/reading.md)
<!-- nav:bottom:end -->
