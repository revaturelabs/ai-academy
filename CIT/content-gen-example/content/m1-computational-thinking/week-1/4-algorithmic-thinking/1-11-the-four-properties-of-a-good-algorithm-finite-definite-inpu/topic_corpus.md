---
topic_id: "1.11"
title: "The four properties of a good algorithm — finite, definite, input, output"
position_in_module: 3
generated_at: "2026-06-22T00:00:00Z"
resource_count: 3
---

# 1. The Four Properties of a Good Algorithm — Topic Corpus

## 2. Prerequisites

This topic builds directly on:

- **1.9 — Algorithmic thinking: what makes a set of steps an algorithm** — the concept of an algorithm as a precise, unambiguous set of steps.
- **1.10 — Algorithms in everyday life** — real-world examples (recipes, GPS routes, sorting) that made algorithms concrete.

You should be comfortable with the idea that an algorithm is a set of instructions before exploring *what makes those instructions qualify as a good algorithm*.

## 3. Learning Objectives

By the end of this topic, you should be able to:

- State the four properties of a good algorithm — finiteness, definiteness, input, and output — and explain each in plain language.
- Identify whether a given set of steps satisfies each of the four properties.
- Give an everyday example that illustrates each property.
- Explain why a set of instructions that fails any one property is not a reliable algorithm.
- Apply the four-property checklist to evaluate a simple algorithm you encounter.

## 4. Introduction

Imagine you ask a friend for directions to the nearest coffee shop. They say: "Walk forward. Keep walking. Eventually you'll get there."

Would you follow those directions? Probably not. They never end ("keep walking" could mean forever), they are vague about what "forward" means, and they do not tell you what success looks like. These directions fail as an algorithm — not because the goal is wrong, but because the instructions themselves are broken.

In topic 1.9 you learned that an algorithm is a precise, unambiguous set of steps. Now we go one level deeper: *precisely what makes a set of steps precise enough?* Computer scientists and mathematicians have agreed on four properties. If a set of instructions satisfies all four, it is a well-formed algorithm. If even one property is missing, the instructions are not a reliable algorithm — a computer following them could loop forever, do unpredictable things, or produce no result at all [1].

These four properties are: **finiteness**, **definiteness**, **input**, and **output**. You will encounter them every time you design, evaluate, or debug an algorithm — whether in pseudocode, a flowchart, or actual code [2].

## 5. Core Concepts

### 5.1 Property 1 — Finiteness

**Finiteness** — the property that an algorithm must stop after a limited number of steps.

An algorithm cannot run forever. Every path through the instructions — including any loops or repeated sections — must eventually reach an end. When you follow a recipe, you do not keep stirring indefinitely. The recipe says "stir for 2 minutes" or "stir until smooth," and then you move on. The process terminates [1].

Why does this matter? A computer will faithfully follow whatever instructions you give it. If those instructions say "keep doing this" with no condition to stop, the program runs forever. This is called an **infinite loop** — a situation where the algorithm never terminates. Infinite loops are one of the most common bugs in programming, and finiteness is the property designed to prevent them.

**Termination** — the moment when an algorithm reaches its end and stops. A good algorithm always terminates [2].

**Key point:** Every step in an algorithm should bring it closer to finishing. If you cannot identify the end point, the algorithm is not finite.

**Finite vs. not finite — examples:**

| Instructions | Finite? | Why |
|---|---|---|
| "Count down from 10 to 1, then stop" | Yes | Ends after exactly 10 steps |
| "Keep checking your email until a reply arrives" | Only sometimes | If no reply ever comes, it never stops |
| "Keep walking forward forever" | No | No stopping condition at all |

Notice the middle row. An algorithm that *might* not stop depending on circumstances is a risky algorithm. Good algorithm design guarantees termination regardless of input [3].

### 5.2 Property 2 — Definiteness

**Definiteness** — the property that every single step must be clear, precise, and unambiguous, with exactly one valid interpretation.

"Add some salt" is not definite. "Add half a teaspoon of salt" is definite. The difference is precision. A step is definite if anyone — or any computer — reading it would carry it out in exactly the same way, every time [1].

Ambiguity is the enemy of a good algorithm. In topic 1.9 you saw that incomplete or vague instructions are not truly algorithmic. Definiteness is the formal property that rules those out. Every action, every condition, and every decision in the algorithm must be stated precisely enough that no two people interpret it differently [2].

**Indefinite vs. definite steps:**

| Indefinite step | Definite version | Problem with the indefinite version |
|---|---|---|
| "Walk a bit" | "Walk exactly 50 metres north" | "A bit" means different things to different people |
| "Sort the list somehow" | "Compare adjacent pairs; swap if left is larger than right" | "Somehow" specifies no method |
| "Heat until warm" | "Heat to 80°C" | "Warm" is subjective |
| "Choose a good number" | "Choose the smallest number in the list" | "Good" is undefined |

A computer cannot guess at meaning. Computers do exactly what they are told. Definiteness ensures that what you tell the computer is precise enough to be executed without guesswork [3].

**Note:** "Unambiguous steps" — a term introduced in topic 1.9 — is the everyday way of saying "definite." Definiteness is the formal name for the same requirement [1].

### 5.3 Property 3 — Input

**Input (as an algorithm property)** — a declaration of the zero or more pieces of data that the algorithm receives before it starts and will operate on.

An algorithm usually works on something. A sorting algorithm works on a list of items. A navigation algorithm works on a starting location and a destination. A recipe works on the ingredients you provide. These are all inputs [1].

Two important points about the input property:

1. **The algorithm must state what inputs it expects.** If you do not declare what the algorithm receives, it cannot process anything reliably.
2. **The number of inputs can be zero or more.** Some algorithms need no external data at all. An algorithm that simply prints "Hello" and stops is valid. Zero inputs is a legitimate answer [2].

**Input in everyday algorithms:**

- A recipe for banana bread requires: 3 bananas, 2 cups flour, 1 egg. Those ingredients are the input.
- A GPS route algorithm requires: your current location and your destination. Without both, it cannot plot a route.
- An alarm clock algorithm requires: the time you want to wake up. With no time set, it does not know when to ring.
- A coin-flip simulation algorithm requires: nothing. It generates a result from scratch. Zero inputs [1].

**How this connects to topic 1.1:** In topic 1.1 you met the input/process/output model as a description of what computation does. Here, input is a *requirement* — the algorithm must declare its inputs explicitly. An algorithm that tries to use information it was never given has nothing reliable to work with [3].

### 5.4 Property 4 — Output

**Output (as an algorithm property)** — the requirement that an algorithm must produce at least one result after it finishes.

An algorithm that runs and produces nothing visible has no purpose. Running a sorting algorithm must give you a sorted list. Following a recipe must give you a baked good. Finding the maximum number in a list must give you a number. These are all outputs [1].

Two requirements for the output property:

1. **At least one output must be produced.** An algorithm that runs, does work, and silently disappears with no result does not qualify as a well-formed algorithm.
2. **The output must have a defined relationship to the input.** The output is what the algorithm was designed to produce from its input. A sorting algorithm does not output a random number — it outputs the sorted version of the list it received [2].

**Output in everyday algorithms:**

- A recipe algorithm outputs: a finished dish.
- A GPS route algorithm outputs: a sequence of turn-by-turn directions.
- An alarm clock algorithm outputs: a sound (the alarm) at a specific time.
- A sorting algorithm outputs: the original list arranged in a new order [3].

**How this connects to topic 1.1:** The output property closes the loop on the input/process/output model. Declaring the output upfront tells you and anyone reading your algorithm what the whole process is for [1].

### 5.5 The Four Properties as a Checklist

An algorithm is **well-defined** when all four properties hold simultaneously. A **well-defined algorithm** is a set of instructions that satisfies all four properties and can be executed correctly and consistently by anyone — or any computer — that follows it [1] [2].

Think of the four properties as a checklist you apply to any set of instructions:

| Property | The question to ask | What breaks if this property is missing |
|---|---|---|
| **Finiteness** | Does it always stop? | Infinite loop — runs forever with no result |
| **Definiteness** | Is every step clear and precise? | Ambiguity — different people do different things |
| **Input** | Does it state what data it needs? | Nothing to work with — undefined behaviour |
| **Output** | Does it produce a result? | No visible effect — the algorithm did nothing useful |

A set of instructions that fails even one of these tests is not a well-defined algorithm [3].

## 6. Implementation

You can apply the four-property checklist to any set of instructions you write or encounter. Here is a structured way to do it.

**Step-by-step checklist:**

1. **Test finiteness.** Trace through the steps. Is there a stopping condition for every loop or repeated section? Can you guarantee that condition will be reached?
2. **Test definiteness.** Read each step as if you are a machine with no common sense. Is there any word or phrase that could be interpreted in more than one way? If yes, rewrite it to be precise.
3. **Test input.** List every piece of data the algorithm needs to start. Are all of them declared? Does the algorithm ever use information it was never given?
4. **Test output.** Identify what the algorithm produces at the end. Is there at least one result? Does it follow logically from the inputs and the steps?

**Worked example — evaluating a simple algorithm:**

> Find the largest number in a list.
>
> Step 1: Take the first number in the list. Call it "current largest."
> Step 2: Look at the next number in the list.
> Step 3: If the next number is larger than "current largest," replace "current largest" with it.
> Step 4: Repeat steps 2–3 until you have checked every number in the list.
> Step 5: Report "current largest" as the result.

Apply the checklist:

- **Finite?** Yes. Step 4 ends when every number has been checked. The list has a fixed length, so this terminates.
- **Definite?** Yes. Every step uses precise language: "larger than," "replace," "every number."
- **Input?** Yes. The input is a list of numbers (at least one number required).
- **Output?** Yes. The output is the largest number found.

This passes all four. It is a well-defined algorithm [1] [3].

**Counter-example — an algorithm that fails:**

> Find a good number. Keep looking until you are satisfied.

- **Finite?** No. "Until you are satisfied" has no measurable stopping condition.
- **Definite?** No. "Good number" and "satisfied" are undefined.
- **Input?** Unclear. No stated list or range to search.
- **Output?** Unclear. No defined result.

This fails all four properties. It is not a well-defined algorithm [2].

## 7. Real-World Patterns

The four properties appear wherever reliable, automated processes are designed.

**Search engines** — the algorithm that finds results for your query must be finite (it cannot search indefinitely), definite (it must know exactly how to measure relevance), receive input (your search query), and produce output (a ranked list of results) [2].

**ATM cash dispensing** — the algorithm that handles a withdrawal must terminate after a fixed number of steps, follow definite rules for every case (what if the balance is too low?), accept input (the amount requested, your PIN, your account balance), and produce output (cash dispensed and a receipt) [1].

**Sorting passengers at an airport gate** — the process for assigning boarding groups must terminate when all passengers are grouped, use definite rules ("Group A = rows 1–10"), take a passenger list as input, and output an ordered boarding sequence [3].

These real-world systems fail exactly when one of the four properties breaks down — for example, a payment system that loops indefinitely when a server is slow (finiteness failure), or a form that accepts "any name" without specifying the allowed format (definiteness failure).

## 8. Best Practices

**Do:**
- Identify the stopping condition for any loop *before* writing the rest of the steps.
- Write every step as if the reader has no common sense — maximum precision.
- List all required inputs explicitly at the start of your algorithm description.
- State the expected output before you write the algorithm body (it keeps you focused on the goal).
- Run the four-property checklist on every algorithm you write, even short ones.

**Do not:**
- Use words like "a bit," "somehow," "appropriately," or "as needed" — these break definiteness.
- Assume the algorithm "will obviously stop eventually" — prove it by identifying the termination condition.
- Write an algorithm that silently discards its result — always make the output explicit.
- Treat the four properties as formalities — each one prevents a real class of failure.

**The single most common mistake:** writing a loop with a vague or missing stopping condition. Always ask: "What exact state of affairs causes this loop to stop?"

## 9. Hands-On Exercise

Choose one of the following everyday processes and write it out as a numbered list of steps. Then apply the four-property checklist to your own instructions.

**Option A — Making a cup of tea.** Write 6–10 steps. Then check: does it always stop? Is every step precise? What are the inputs? What is the output?

**Option B — Checking whether a number is even or odd.** Write the steps to take any whole number and report whether it is even or odd. Apply the checklist.

**Option C — Finding the youngest person in a group.** You have a group of people and you know each person's age. Write the steps to identify the youngest. Apply the checklist.

After writing your steps, swap with a partner. Can they follow your instructions exactly — without asking you any questions? If they need to ask a question, you have a definiteness problem. Find it and fix it [1].

## 10. Key Takeaways

- A **well-defined algorithm** must satisfy four properties: **finiteness** (it always stops), **definiteness** (every step is precise and unambiguous), **input** (it declares the data it needs — zero or more items), and **output** (it produces at least one result).
- Failing any single property makes the instructions unreliable — a computer following them could loop forever, behave unpredictably, or produce nothing useful.
- **Finiteness** requires a clear stopping condition for every loop or repeated section; "keep going until it feels right" is not a stopping condition.
- **Definiteness** is the formalization of the "unambiguous steps" requirement from topic 1.9 — every step must have exactly one valid interpretation.
- **Input** and **output** ground the algorithm in the input/process/output model introduced in topic 1.1: input declares what the algorithm needs; output declares what it will produce.

## 11. Next Steps

_System-derived from the next entry in curriculum/sequence.md._
