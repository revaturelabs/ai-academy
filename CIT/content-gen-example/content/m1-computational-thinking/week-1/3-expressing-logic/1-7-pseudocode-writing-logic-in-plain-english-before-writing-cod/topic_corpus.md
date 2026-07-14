---
topic_id: 1.7
title: Pseudocode — writing logic in plain English before writing code
position_in_module: 1
generated_at: 2026-06-21T00:00:00Z
resource_count: 3
---

# 1. Pseudocode — Writing Logic in Plain English Before Writing Code — Topic Corpus

## 2. Prerequisites

This topic builds directly on two earlier topics:

- **1.1 — What is computation**: introduced the idea that computation is a set of defined steps that take input, process it, and produce output. Pseudocode is how you write those steps in human-readable form.
- **1.5 — Decomposition**: introduced breaking a big problem into smaller sub-tasks. Pseudocode is where you express each sub-task as an explicit, ordered instruction.

These ideas are assumed known. This topic does not re-teach them.

## 3. Learning Objectives

By the end of this topic, you should be able to:

- Explain in your own words what pseudocode is and why it exists.
- Write basic pseudocode that describes a simple, real-world process using plain English.
- Identify the core building blocks of pseudocode: sequence, decision (IF/OTHERWISE), and repetition (REPEAT/WHILE).
- Translate a short block of pseudocode into the equivalent steps you would follow manually.
- Recognise the difference between pseudocode and actual programming code.
- Describe at least two reasons why writing pseudocode before coding helps you think more clearly.

## 4. Introduction

Imagine you are baking a cake for the first time. Before you touch a bowl or turn on the oven, you read the recipe. The recipe tells you, in plain language, exactly what to do and in what order: crack the eggs, then add flour, then mix, then bake. You are not reading a chemistry textbook about egg proteins. You are reading a clear, step-by-step plan a human wrote so another human could follow it.

Pseudocode does the same job — but for logic instead of baking [1].

When you want a computer to do something, you need to give it exact, ordered instructions. But programming languages are picky. They require specific words, specific punctuation, and specific formatting. One misplaced semicolon can break the whole thing. If you try to write a program from scratch while simultaneously figuring out the logic AND learning the language's rules, you are juggling two hard problems at once. Pseudocode separates those two problems. You figure out the logic first, in plain English. Then — once you are confident about the steps — you translate that plan into whichever programming language you need [2].

This is not a workaround for beginners. Professional software engineers, data scientists, and systems designers write pseudocode all the time. It is a thinking tool, not a training wheel.

## 5. Core Concepts

### 5.1 What Pseudocode Is

**Pseudocode** — a way of writing out the logic of a program using plain, human-readable language rather than the strict rules of any programming language [1].

The word "pseudo" means "fake" or "not real." So pseudocode is "fake code" — it looks a little like code (it is structured, step-by-step, and precise), but it is written in natural language and cannot be run directly by a computer [2].

Think of it this way:

- **Real code** — instructions the computer can execute directly (e.g., Python, JavaScript).
- **Pseudocode** — instructions a human can read and understand, before translating to real code.

Pseudocode sits between your idea and your first line of real code. It is the plan.

Here is a simple example. Suppose you want to describe "make a cup of tea":

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

That is pseudocode. It is structured (there is a clear START and END), it is ordered (each step follows the last), and it is readable by any person — even one who has never written a line of code [1].

### 5.2 Why Pseudocode Exists — The Bridge Between Human Intent and Machine Execution

In topic 1.1 you learned that computation is about taking input, processing it, and producing output. In topic 1.5 you learned that decomposition breaks a big problem into smaller sub-tasks. Pseudocode is how you express those sub-tasks in a form that is one step away from actual code [2].

There is a gap between human intent ("I want the system to check whether a user's password is correct") and machine execution ("run function check_password with the user's input and stored data, then return true or false"). Pseudocode bridges that gap. You write out the human intent in a structured way, and that structure maps naturally onto code later [1].

Without this bridge, you might:

- Start coding before you understand the problem fully.
- Get lost in the language's syntax when the real problem is the logic.
- Miss a step (like: "what happens if the password is wrong three times in a row?").
- Find a flaw after you have already written 200 lines of code.

Pseudocode forces you to think through the logic before you commit to a language [3].

### 5.3 The Three Building Blocks of Pseudocode

Pseudocode has three fundamental building blocks. You will see these same three patterns in every programming language you will ever use. They are not unique to pseudocode — they are the underlying structure of all logic [2].

#### Building Block 1 — Sequence

**Sequence** — doing steps one after another, in order.

This is the simplest pattern. Step 1 happens, then Step 2, then Step 3. No skipping, no branching. Just a straight line of instructions.

Example:
```
Get the user's name
Print "Hello, " followed by the name
```

The computer (or the person following the pseudocode) does the first line, then the second line, then stops.

#### Building Block 2 — Decision (IF / OTHERWISE)

**Decision** — choosing between two (or more) paths based on a condition.

Real problems almost always involve choices. "If the user is logged in, show the dashboard. Otherwise, show the login page." Pseudocode captures this with an IF / OTHERWISE structure [2].

Example:
```
IF temperature is above 30 degrees
  PRINT "It is hot outside"
OTHERWISE
  PRINT "It is not that hot"
END IF
```

The **condition** — the test you are checking ("is temperature above 30?") — determines which path is taken. Depending on whether the condition is true or false, a different set of steps runs. This pattern is sometimes also called a **conditional** or a **branch**.

#### Building Block 3 — Repetition (WHILE / FOR EACH)

**Repetition** — doing a step (or a group of steps) multiple times, until a condition is met or for each item in a collection.

Example:
```
WHILE there are items in the shopping cart
  Calculate the price of the next item
  Add it to the running total
END WHILE
PRINT total cost
```

The steps inside the WHILE block repeat as long as the condition is true ("there are items in the cart"). When there are no items left, the repetition stops and the program moves on [2].

These three building blocks — **sequence, decision, repetition** — are the skeleton of almost every program ever written. Pseudocode lets you plan which skeleton you need before writing a single line of real code [1].

### 5.4 Standard Conventions vs. Freestyle

One question beginners ask: "Is there a right way to write pseudocode?"

The honest answer is: there is no single official standard. Different textbooks, courses, and companies use slightly different keywords. Some use `IF / ELSE`, others use `IF / OTHERWISE`. Some write `LOOP`, others write `REPEAT` or `FOR EACH` [2].

What matters is that your pseudocode is:

1. **Readable** — another person can understand what it means.
2. **Precise** — it leaves out nothing important.
3. **Ordered** — steps are in the right sequence.
4. **Consistent** — you use the same keyword for the same thing throughout.

A few widely-used conventions are worth knowing [1][2]:

| Concept | Common keywords |
|---|---|
| Start/end of a block | `START` / `END` |
| Decision | `IF … THEN … ELSE …` or `IF … OTHERWISE …` |
| Repetition with condition | `WHILE … DO … END WHILE` |
| Repetition over a collection | `FOR EACH … DO … END FOR` |
| Assign a value | `SET x TO 5` or `x ← 5` |
| Show output | `PRINT`, `DISPLAY`, `OUTPUT` |
| Get input | `GET`, `READ`, `INPUT` |

You do not need to memorise this table right now. The key point is: pick a consistent set and stick to it within one document [3].

### 5.5 Pseudocode vs. Real Code — A Direct Comparison

It helps to see pseudocode and real code side by side. Here is the same logic — "check whether a number is positive or negative" — written in both forms [2][3]:

**Pseudocode:**
```
GET a number from the user
IF the number is greater than 0
  PRINT "The number is positive"
OTHERWISE
  PRINT "The number is not positive"
END IF
```

**Python (one real programming language):**
```python
number = int(input("Enter a number: "))
if number > 0:
    print("The number is positive")
else:
    print("The number is not positive")
```

Notice the differences:

- Pseudocode uses plain English ("GET a number from the user"). Python uses a specific function (`input()`).
- Pseudocode uses `IF … OTHERWISE`. Python uses `if … else` with a colon (`:`) that the language enforces.
- Pseudocode does not care which language you will use. The same pseudocode could be translated to Python, JavaScript, Java, or any other language.

The logic — the IF/OTHERWISE structure, the comparison, the two outputs — is identical in both. Pseudocode captures just the logic. Real code captures the logic AND the language-specific rules [1].

## 6. Implementation

### Writing Pseudocode: A Step-by-Step Method

Here is a repeatable process for writing pseudocode from scratch [1][2][3]:

1. **State the problem in one sentence.** What does this process need to do? Example: "Check whether a student has passed an exam."

2. **Identify the inputs.** What information do you need to start? Example: "The student's score."

3. **Identify the output.** What should the process produce or display at the end? Example: "A message saying 'Pass' or 'Fail'."

4. **List the steps in plain English, in order.** Do not worry about being formal yet. Just write down what needs to happen. Example:
   - Get the student's score.
   - Check if the score is 50 or above.
   - If yes, say "Pass."
   - If no, say "Fail."

5. **Convert your plain English list into pseudocode structure.** Apply the building blocks: wrap decisions in IF/OTHERWISE, wrap repetitions in WHILE or FOR EACH.

6. **Read it back.** Can you follow it like a recipe? Does it produce the right output for every possible input? If you find a missing step or a gap, fix it now — before writing any real code.

7. **Check the edge cases.** What happens if the input is unusual? What if the score is exactly 50? What if the score is 0? Good pseudocode handles these situations.

Applying this to the student-pass example:

```
START
  GET student_score
  IF student_score >= 50
    PRINT "Pass"
  OTHERWISE
    PRINT "Fail"
  END IF
END
```

That is complete, readable pseudocode. A developer reading this can translate it into any programming language in under a minute [2].

### A Slightly More Complex Example

Suppose you want to describe how to find the highest score in a list of five exam results:

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

This uses all three building blocks together:

- **Sequence**: SET, then FOR EACH loop, then PRINT — in that order.
- **Decision**: the IF inside the loop checks whether the current score beats the current highest.
- **Repetition**: the FOR EACH loop goes through every score in the list.

You do not need to know Python or any other language to understand this. The logic is clear in plain English [2][3].

## 7. Real-World Patterns

### Where Pseudocode Shows Up in Professional Work

Pseudocode is not just a classroom exercise. It appears across many professional contexts [3]:

**Software design.** Before writing a feature, developers write the logic as pseudocode. This helps the team agree on the approach before anyone writes production code.

**Technical interviews.** Many software engineering interviews ask candidates to explain their thinking in pseudocode before writing real code. Interviewers care more about your logic than whether you remember exact language syntax.

**Cross-team communication.** A business analyst might write pseudocode to describe a business rule — for example, "if a customer has more than three failed payments, flag the account" — for the developer to implement. Neither party needs to know the exact code. They just need to agree on the logic.

**Documentation.** Pseudocode appears in technical documentation when explaining how a process works, because it is readable without knowing the implementation language [1].

**Planning data pipelines.** Data scientists use pseudocode to plan how data will flow through a process before writing the actual code. You will encounter this in later modules.

All of these uses share one thing: pseudocode lets you communicate the *what* and *how* of a process without getting stuck in the *which language* question [3].

## 8. Best Practices

### Do

- **Write pseudocode before you write code**, even for small problems. It is faster to find a logic mistake in pseudocode than in a 50-line program [1].
- **Use consistent keywords.** Pick `IF/OTHERWISE` or `IF/ELSE` — do not mix them in the same document.
- **One action per line.** Do not cram two instructions into a single line.
- **Indent nested blocks.** If one set of steps is inside an IF or a WHILE, indent it. This makes the structure visible at a glance [2].
- **Test it mentally with a real example.** Walk through your pseudocode with a specific input (e.g., score = 45) and trace what happens. Does it produce the right output?
- **Keep it as simple as possible.** The goal is clarity, not completeness. You do not need to specify every detail — just enough that any developer could implement it correctly.

### Avoid

- **Avoid real code syntax.** If you write `if score >= 50:` with a Python colon, you are writing Python, not pseudocode. Stay language-independent.
- **Avoid skipping steps.** Pseudocode that says "process the data" without explaining how is too vague to be useful.
- **Avoid jargon your reader does not know.** If your reader does not know what a term means, write it out in plain English.
- **Avoid writing pseudocode after the code.** That defeats the purpose. Pseudocode is a planning tool, not a reverse-engineering tool [3].

| Do | Avoid |
|---|---|
| One action per line | Multiple actions crammed into one line |
| Consistent keywords throughout | Mixed keywords (IF/OTHERWISE one place, if/else another) |
| Indent nested blocks to show structure | Flat indentation that hides which steps belong together |
| Write pseudocode before coding | Writing pseudocode after coding to document |
| Test with a real example mentally | Assuming it works without tracing through |

## 9. Hands-On Exercise

**Exercise: Pseudocode for a real-world task from your chosen domain**

In the lab activity for this week, you are asked to choose a domain — a problem area you will build toward all semester.

Try this:

1. In one sentence, state a task from your chosen domain. Example: "My system should check whether a user's submitted form is complete before saving it."
2. Identify the inputs (what does the task need to start?) and the output (what should it produce?).
3. Write pseudocode for that task using the three building blocks: sequence, decision (IF/OTHERWISE), and repetition (WHILE or FOR EACH) where each is needed.
4. Swap your pseudocode with a classmate. Can they follow it exactly, without asking you any questions? If not — what step is missing or unclear?

The goal is not to get the syntax perfect. The goal is to notice where your thinking is clear and where it has gaps [1][2].

## 10. Key Takeaways

- **Pseudocode is structured plain English** that describes the logic of a process — step by step — without using any specific programming language's rules.
- **The three building blocks are sequence, decision, and repetition.** Almost every program in any language is made of combinations of these three patterns.
- **Pseudocode separates logic from syntax.** You solve the "what should happen and in what order?" question first. You answer the "how do I write this in Python?" question second.
- **There is no single official standard**, but good pseudocode is always readable, precise, ordered, and consistent.
- **Writing pseudocode before code saves time.** A logic mistake caught in pseudocode is far cheaper to fix than the same mistake caught after writing a full program.

## 11. Next Steps

_System-derived from the next entry in curriculum/sequence.md._
