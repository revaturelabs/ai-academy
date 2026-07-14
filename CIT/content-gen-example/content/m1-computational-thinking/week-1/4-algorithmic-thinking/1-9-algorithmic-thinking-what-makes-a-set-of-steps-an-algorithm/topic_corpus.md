---
topic_id: "1.9"
title: "Algorithmic thinking — what makes a set of steps an algorithm"
position_in_module: 1
generated_at: "2026-06-22T00:00:00Z"
resource_count: 3
---

# 1. Algorithmic Thinking — What Makes a Set of Steps an Algorithm — Topic Corpus

## 2. Prerequisites

This topic builds on concepts introduced in earlier topics:

- **1.1 What is computation** — the idea of input → process → output and defined steps
- **1.5 Decomposition** — breaking a problem into smaller, manageable sub-tasks
- **1.7 Pseudocode** — writing logic as sequence, decision, and repetition before coding
- **1.8 Flowcharts** — representing logic as a diagram with terminators, process boxes, decision diamonds, and flowlines

## 3. Learning Objectives

By the end of this topic, you will be able to:

- Explain what an algorithm is in plain language, without using programming jargon.
- Describe the key characteristics that distinguish an algorithm from an arbitrary list of steps.
- Apply the idea of algorithmic thinking to a familiar everyday task.
- Identify, by inspection, whether a given set of steps qualifies as an algorithm or falls short.
- Explain why clear, unambiguous instructions matter when writing steps for a computer to follow.

## 4. Introduction

Imagine you hand a friend a piece of paper that says: "Make a cup of tea. Be sensible about it." Your friend laughs, nods, and makes tea. A computer, however, would stare blankly. It has no idea what "be sensible" means. It cannot fill in gaps. It cannot guess. It needs every step spelled out, in the right order, with no room for interpretation.

That gap — between a loose set of instructions a human can muddle through and a precise set of instructions a machine can execute without any guesswork — is exactly what this topic is about. What is it that turns vague directions into a true **algorithm**?

The word algorithm sounds technical, but the idea is ancient. Long before computers existed, people wrote down step-by-step methods for doing things: how to bake bread, how to divide numbers, how to plan a route. Computers did not invent the concept of an algorithm. They just made us much more careful about what it means [1].

By the end of this topic, you will have a clear picture of what makes a set of steps an algorithm — and just as importantly, what is missing when a set of steps falls short. The next two topics will build on this: topic 1.10 will look at algorithms in everyday life, and topic 1.11 will walk through each formal property in detail.

## 5. Core Concepts

### 5.1 What is an algorithm?

**Algorithm** — a precise, step-by-step set of instructions for solving a problem or completing a task, designed so that anyone (or any machine) who follows it exactly will reach the same correct result [1].

That last part matters: "anyone who follows it exactly." An algorithm is not personal. It does not depend on who runs it. It does not rely on common sense or experience to fill in blanks. It works the same way every single time.

Compare these two sets of "instructions" for making a cup of instant coffee:

| Version A (vague) | Version B (algorithm-like) |
|---|---|
| Put some coffee in a cup. | Place one level teaspoon of instant coffee granules into a clean 250 ml mug. |
| Add water. | Pour 200 ml of water that has been boiled and cooled for 30 seconds into the mug. |
| Make it taste right. | Stir for 5 seconds until no granules are visible. |

Version A relies on judgment ("some coffee," "make it taste right"). A machine cannot follow it. Version B is precise enough that a machine — or a robot, or a person who has never made coffee before — could follow it exactly [1].

### 5.2 The difference between instructions and an algorithm

Not every list of steps is an algorithm. Consider a page torn from a notebook that says:

1. Turn on the oven.
2. Enjoy your meal.

There are steps, and they are numbered. But something is clearly missing. The jump from step 1 to step 2 skips every important part — preparing the food, setting the temperature, timing the cook, removing the dish. This list of steps is **incomplete** — it leaves out entire actions, and there is no way to reach the goal by following only what is written [1].

An algorithm closes that gap. It leaves nothing out. Every action needed to move from the starting state to the goal is included, in the right order, with no gaps that require guesswork [1].

Now consider a second example: directions to a friend's house. A person might hand you a note that says "Head north, go past the park, turn somewhere near the library, and it is the house with the blue door on that street." A human with local knowledge might muddle through. But these directions are **incomplete and ambiguous**: Which park? Turn where exactly near the library — before it, after it, at the corner? Which street? How far down? If your phone's GPS gave you those directions, you would go nowhere useful. A GPS works precisely because it gives algorithmic directions: "In 400 metres, turn left onto Maple Street. In 1.2 kilometres, turn right onto Church Lane. Your destination is on the right." Every turn is named. Every distance is exact. Nothing is left to interpretation [3].

These two examples show the same failure showing up differently. In the oven example, **steps are missing entirely** — the process jumps from start to goal with no explanation of how to get there. In the directions example, **steps are present but vague** — they exist but cannot be followed without extra knowledge the instruction-giver assumed you had.

Both failures matter equally. Here is what goes wrong at each gap:

- **Missing steps** — the executor (a machine, a robot, or a person following instructions strictly) reaches a point where there is nothing to do next. It cannot proceed. A machine halts or crashes.
- **Vague steps** — the executor reaches a step but cannot determine what action to take. It may produce a wrong output, stop entirely, or — in the case of a machine — pick an action arbitrarily, giving different results each time.
- **Steps in the wrong order** — even if every step is present and precise, the wrong order breaks the process just as badly. If you are told to stir the coffee before adding the hot water, nothing dissolves correctly. Order is a core property of an algorithm: each step must be able to run given only what the previous steps have produced [1].

The three things that push a list of steps toward being a true algorithm are:

1. **Unambiguous steps** — each step has exactly one meaning. There is no room for interpretation. "Add a little salt" is ambiguous. "Add half a teaspoon of salt" is unambiguous.
2. **A clear stopping point** — the instructions end. They do not loop forever without stopping. You reach the goal and you stop. (Topic 1.11 will cover this formally.)
3. **A result** — following the steps produces something: an answer, a product, a decision. A list of steps that produces nothing useful is not an algorithm. (Topic 1.11 will cover this formally.)

### 5.3 Algorithmic thinking as a mindset

**Algorithmic thinking** is the habit of approaching problems by asking: "How could I write this down precisely enough that someone — or something — could follow it without needing to ask me any questions?" [1][2]

It is a mindset, not a tool. You do not need a computer to think algorithmically. You need the discipline to:

- **Be precise.** Replace vague language with exact language.
- **Be complete.** Include every step, even the ones that feel obvious.
- **Be ordered.** Arrange steps so each one can be done before the next one needs it.
- **Be decisive.** When there is a choice to make, say so explicitly rather than leaving it to judgment.

This connects directly to what you learned in topic 1.7 (pseudocode) and topic 1.8 (flowcharts). Those tools exist precisely because humans need a way to check their own thinking for precision before handing instructions to a machine. Writing pseudocode or drawing a flowchart forces you into algorithmic thinking — you cannot leave a step vague and draw it in a flowchart at the same time.

### 5.4 Why vagueness breaks computation

In topic 1.2 you learned that computation is deterministic: give the same input, follow the same steps, and you always get the same output. Vagueness in instructions breaks that guarantee — and the failure is predictable once you trace it step by step.

Imagine an instruction that says: "Do the right thing here." Now imagine a machine trying to execute it. The machine reads the instruction. It looks for a rule to follow — something that says "if this condition, take that action." There is no rule. The instruction does not define what "the right thing" is. The machine has no branch to follow, no condition to check, and no defined output to produce. At this point, three bad things can happen:

1. The machine **stops completely** — it reaches an instruction it cannot interpret and halts with an error.
2. The machine **picks an action arbitrarily** — if it has some default behavior, it may take that action, producing an output that is wrong for this situation.
3. The machine **produces different output each time** — different machines, or the same machine on different runs, may resolve the ambiguity differently, giving inconsistent results.

All three outcomes break the core promise of computation: same input, same output, every time [2].

This connects directly to determinism from topic 1.2. Determinism means: the same input, processed by the same steps, must always produce the same output. A vague instruction makes the process non-deterministic — the same input can produce different outputs depending on who or what is following the instruction, and what they choose to do with the vagueness. Reproducibility disappears [3].

This is also why programmers test edge cases. An edge case is a situation that sits at the boundary of what the instructions cover — an unusual input, an unexpected value, a scenario the writer did not think about. When programmers test edge cases, they are finding the places where their instructions were not precise enough. Each discovered edge case reveals a gap: an instruction that was vague enough to fail on some inputs even though it worked on the obvious ones. Fixing those gaps is the process of making instructions more algorithmic [2].

The practical lesson: every vague word in an instruction is a potential failure point. "Add enough water," "check if it looks right," "proceed as appropriate" — each of these is a place where computation can break down. An algorithm replaces every one of those phrases with an exact rule [3].

### 5.5 What "algorithmic" does NOT mean

A common misunderstanding is that an algorithm must be mathematical or must be written in code. Neither is true [2].

- A recipe for bread can be an algorithm, if it is precise enough.
- A set of directions to a friend's house can be an algorithm, if every turn is unambiguous.
- A code snippet is not automatically an algorithm — it must still be correct, complete, and have a stopping point.

The word "algorithm" describes a quality of a set of instructions, not a form they must take. You will explore real-world examples of algorithms in topic 1.10.

### 5.6 From steps to algorithm: a worked contrast

Here is the same task written two ways.

**Task:** Decide whether a student has passed or failed an exam. Passing score is 50 or above.

**Version A — a list of steps (not yet an algorithm):**

1. Look at the student's score.
2. Decide if they passed.

**Version B — algorithmic:**

1. Read the student's score.
2. If the score is 50 or above, write "Pass."
3. If the score is below 50, write "Fail."
4. Stop.

Version A has a decision buried inside ("decide if they passed") that requires outside knowledge. A machine reading Version A does not know what "passed" means. Version B makes the decision rule explicit: 50 or above means Pass, below 50 means Fail. Nothing is left to guesswork [1][3].

Notice that Version B uses the same building blocks you saw in topic 1.7 (pseudocode): a sequence of steps, a condition (score ≥ 50), and a decision (if/otherwise branch). Algorithmic thinking puts those building blocks together deliberately to produce something a machine can execute without ambiguity.

## 6. Implementation

The following demonstrates the process of turning a vague task into an algorithmic one. Use this as a mental checklist when you are writing your own steps.

**Step 1 — Write down the goal in one sentence.**
Example: "Sort three numbers from smallest to largest."

**Step 2 — Write out your steps in plain language, quickly, without worrying about precision.**
Example: "Look at the numbers, put them in order."

**Step 3 — Ask: can someone follow this without asking me any questions?**
If the answer is no, find the vague part and replace it.

**Step 4 — Replace every vague word or phrase with an exact instruction.**
Example: "Compare the first and second number. If the first is larger, swap them. Compare the second and third number. If the second is larger, swap them. Compare the first and second number again. If the first is larger, swap them. Stop."

**Step 5 — Check that there is a clear stopping point.**
The final step above says "Stop." It does not loop endlessly.

**Step 6 — Check that the steps produce a result.**
After the final step, the three numbers are in order. That is the result.

Following these six steps is an act of algorithmic thinking. You are not yet writing code — you are disciplining your own thinking so that the instructions could, in principle, be handed to a machine [1][3].

---

Now here is a fully worked second example using a different domain: checking whether a library book is overdue.

**Goal:** Determine whether a borrowed library book should be flagged as overdue.

**Draft steps (vague — not yet algorithmic):**

1. Check the book.
2. See if it is late.
3. Flag it if needed.

These draft steps have every problem we have identified. Step 1 does not say what to check. Step 2 does not say what "late" means or how to determine it. Step 3 does not define "if needed." A machine cannot follow any of these.

Apply the six-step checklist:

- **Goal (Step 1):** Determine whether a library book's return date has passed today's date.
- **Draft (Step 2):** Written above — vague.
- **Ask (Step 3):** Can a machine follow "see if it is late"? No. What is "late"? What does "check the book" mean? What is "flag"?
- **Replace vague phrases (Step 4):** Write the algorithmic version below.
- **Check stopping point (Step 5):** The last instruction says "Stop" — the process ends.
- **Check result (Step 6):** The book is either marked "Overdue" or "On Time" — a defined output.

**Algorithmic version (after revision):**

1. Read the book's due date.
2. Read today's date.
3. If today's date is after the due date, mark the book "Overdue."
4. If today's date is on or before the due date, mark the book "On Time."
5. Stop.

| Vague draft | Algorithmic revision |
|---|---|
| "Check the book." | "Read the book's due date." |
| "See if it is late." | "If today's date is after the due date …" |
| "Flag it if needed." | "Mark the book 'Overdue'." |

The BEFORE version relies on unstated knowledge — what "late" means and what "flag" involves. The AFTER version defines every term and every rule explicitly. Nothing is left to judgment. A machine reading the AFTER version can execute it on any book, with any due date, and always reach the same correct answer [1][3].

This is the core pattern of algorithmic thinking: take a task you understand intuitively, expose every hidden assumption, and replace each assumption with an explicit rule.

## 7. Real-World Patterns

Algorithmic thinking appears wherever someone must give instructions to a system that cannot use judgment:

- **Assembly instructions** — flat-pack furniture instructions try to be algorithmic. When they fall short, problems follow immediately. For example: a step that says "attach the bracket as shown in diagram B" is ambiguous when diagram B shows two possible orientations and does not indicate which is correct. A human assembler may guess — and may guess wrong, requiring disassembly and a restart. A robot on a factory line cannot guess at all: it reads the instruction, finds no single defined action, and stops. The ambiguity in the instruction translates directly into a failure in the process. Truly algorithmic assembly instructions label every component, specify every orientation, and state every measurement — leaving nothing to interpretation [1].

- **Medical protocols** — a triage protocol in an emergency room is one of the clearest real-world algorithms. A protocol converts a nurse's clinical judgment into a defined set of rules: "If the patient's blood pressure is below 90/60, assign Priority 1. If the patient is conscious and breathing without assistance and blood pressure is 90/60 or above, assign Priority 2." The protocol exists so that any trained person following it will reach the same decision for the same patient — regardless of their years of experience, their instincts, or their personal judgment. Consistency is the goal. The algorithm is what delivers that consistency: it removes the variability that comes from relying on judgment alone [2].

- **Navigation apps** — when you ask a GPS for directions, it runs an algorithm that produces a precise, unambiguous sequence of turns. It does not say "go generally north." It says "turn left in 200 metres onto Oak Street." Behind the scenes, the algorithm compares candidate routes and picks one based on a defined cost metric — shortest time, shortest distance, or fewest turns — and then outputs that route as a step-by-step sequence. Every step is named, every distance is measured, and the process stops when you reach your destination [3]. Topic 1.10 will look at routing algorithms in more detail.

- **Sorting and searching** — whenever a website sorts search results or a spreadsheet sorts a column, it runs an algorithm. What makes sorting algorithmic is a defined comparison rule (which value is "smaller"), a defined stopping condition (when no more swaps are needed), and a defined output (the sorted list). Without those three properties — rule, stopping point, result — the process would be inconsistent and unpredictable [3].

The common thread: wherever consistency, repeatability, and no-guesswork matter, an algorithm is the tool. Humans can fill in gaps with experience; machines cannot. Every example above works because the instructions are complete, unambiguous, and ordered — the same properties that separate a list of steps from a true algorithm.

## 8. Best Practices

**Do:**
- Write steps as if the reader has no background knowledge about the task.
- Test your steps by pretending to be a machine: follow them literally and see what happens.
- Give every decision an explicit rule ("if X, do Y; otherwise, do Z").
- Include a step that says when to stop.

**Do not:**
- Use words like "approximately," "as needed," "suitably," or "correctly" — these require judgment.
- Assume the reader knows what the goal is without being told explicitly.
- Skip "obvious" steps. What is obvious to you is not obvious to a machine.
- Write steps that run forever without a clear stopping point.

| Vague (not algorithmic) | Precise (algorithmic) |
|---|---|
| "Add enough water" | "Add exactly 300 ml of water" |
| "Repeat until done" | "Repeat until the counter reaches 10" |
| "Choose the best option" | "Choose the option with the lowest cost" |
| "Handle errors appropriately" | "If an error occurs, display 'Error: try again' and stop" |
| "Do the right thing" | "If the value is greater than 100, set it to 100; otherwise leave it unchanged" |

## 9. Hands-On Exercise

Pick a task you do automatically every day — for example, making breakfast, locking your front door, or choosing what to wear.

1. Write down the steps you follow, quickly, without thinking too hard.
2. Read them back as if you were a machine with no common sense. Find every place where you used a vague word or skipped a step.
3. Rewrite the steps, replacing every vague phrase with a precise one and filling in every gap.
4. Show your rewritten steps to a classmate. Ask them to follow your steps literally. Did they end up where you expected?

This exercise is the core discipline of algorithmic thinking: taking something you do naturally and making it precise enough to hand to something that cannot think for itself.

## 10. Key Takeaways

- An **algorithm** is a precise, complete, unambiguous, and finite set of steps that solves a problem and produces a result — not just any list of instructions.
- The crucial difference between a list of steps and an algorithm is **precision and completeness**: every step must be exact, nothing can be left to interpretation or common sense.
- **Algorithmic thinking** is the mindset of writing instructions precisely enough that they can be followed without judgment — a skill that applies long before, and far beyond, writing code.
- Vague instructions break computation because computers cannot fill in gaps; the same input must always produce the same output.
- The building blocks you already know — sequence, decision, repetition (from topic 1.7) and flowchart shapes (from topic 1.8) — are the tools you use to express algorithmic thinking precisely.

## 11. Next Steps

_System-derived from the next entry in curriculum/sequence.md._
