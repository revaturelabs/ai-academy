<!-- nav:top:start -->
[⬅ Previous: 1.10 — Algorithms in everyday life](../../1-10-algorithms-in-everyday-life-recipes-gps-routes-sorting-queue/artifacts/reading.md)&emsp;·&emsp;[⬆ Table of Contents](../../../../../../../README.md#curriculum-topic-index)&emsp;·&emsp;[Next: 1.12 — Choosing your domain ➡](../../../5-applying-it-to-your-domain/1-12-choosing-your-domain-writing-a-3-sentence-problem-statement/artifacts/reading.md)
<!-- nav:top:end -->

---

# The four properties of a good algorithm — finite, definite, input, output

## Overview

An algorithm is a precise, unambiguous set of steps — but what does "precise enough" actually mean? Computer scientists have agreed on four properties that every reliable algorithm must satisfy: **finiteness**, **definiteness**, **input**, and **output**. If even one property is missing, the instructions are not a well-formed algorithm — a computer following them could loop forever, behave unpredictably, or produce no result at all [1]. Learning these four properties gives you a concrete checklist to evaluate any algorithm you write or encounter [2].

## Key Concepts

Think of the four properties as four gates. An algorithm candidate must pass through every gate to earn the label "well-defined." The diagram below shows how the four properties work as a checklist — an algorithm candidate passes through each gate in turn.

![Four-property algorithm checklist](./diagram.png)
*A four-gate decision chain: algorithm candidate → finite? → definite? → input declared? → output declared? → well-defined or not well-defined.*

### 1. Finiteness

**Finiteness** — the property that an algorithm must stop after a limited number of steps.

Every path through the instructions — including any loops — must eventually reach an end. When you follow a recipe, you do not stir indefinitely; the recipe says "stir for 2 minutes" and then you move on [1].

Why does this matter? A computer will faithfully follow whatever instructions you give it. If those instructions say "keep doing this" with no condition to stop, the result is an **infinite loop** — a situation where the algorithm never terminates. **Termination** is the moment an algorithm reaches its end and stops. A good algorithm always terminates [2].

**Key point:** Every step should bring the algorithm closer to finishing. If you cannot identify the end point, the algorithm is not finite.

| Instructions | Finite? | Why |
|---|---|---|
| "Count down from 10 to 1, then stop" | Yes | Ends after exactly 10 steps |
| "Keep checking your email until a reply arrives" | Only sometimes | If no reply ever comes, it never stops |
| "Keep walking forward forever" | No | No stopping condition at all |

Notice the middle row: an algorithm that *might* not stop depending on circumstances is a risky algorithm. Good algorithm design guarantees termination regardless of input [3].

### 2. Definiteness

**Definiteness** — the property that every step must be clear, precise, and unambiguous, with exactly one valid interpretation.

"Add some salt" is not definite. "Add half a teaspoon of salt" is definite. A step is definite if anyone — or any computer — reading it would carry it out in exactly the same way, every time [1]. Definiteness is the formal name for the "unambiguous steps" requirement you saw in topic 1.9.

A computer cannot guess at meaning. Computers do exactly what they are told — nothing more, nothing less [3].

| Indefinite step | Definite version | Problem with the indefinite version |
|---|---|---|
| "Walk a bit" | "Walk exactly 50 metres north" | "A bit" means different things to different people |
| "Sort the list somehow" | "Compare adjacent pairs; swap if left is larger than right" | "Somehow" specifies no method |
| "Heat until warm" | "Heat to 80°C" | "Warm" is subjective |
| "Choose a good number" | "Choose the smallest number in the list" | "Good" is undefined |

### 3. Input

**Input (as an algorithm property)** — a declaration of the zero or more pieces of data that the algorithm receives before it starts and will operate on.

An algorithm usually works on something. A sorting algorithm works on a list of items. A GPS navigation algorithm works on a starting location and a destination. These data items are the algorithm's inputs [1].

Two important points about input:

1. **The algorithm must state what inputs it expects.** If you do not declare what the algorithm receives, it cannot process anything reliably.
2. **The number of inputs can be zero or more.** Some algorithms need no external data at all — a coin-flip simulation generates a result from scratch. Zero inputs is a legitimate answer [2].

| Algorithm | Inputs |
|---|---|
| Banana bread recipe | 3 bananas, 2 cups flour, 1 egg |
| GPS route | Your current location + destination |
| Alarm clock | The time you want to wake up |
| Coin-flip simulation | None (zero inputs) |

This connects directly to the input/process/output model from topic 1.1. There, input described what computation receives. Here, input is a *requirement* — the algorithm must declare its inputs explicitly before it can run [3].

### 4. Output

**Output (as an algorithm property)** — the requirement that an algorithm must produce at least one result after it finishes.

An algorithm that runs and produces nothing visible has no purpose. Running a sorting algorithm must give you a sorted list. Finding the largest number in a list must give you a number. These are all outputs [1].

Two requirements for the output property:

1. **At least one output must be produced.** An algorithm that runs, does work, and silently disappears with no result is not a well-formed algorithm.
2. **The output must have a defined relationship to the input.** A sorting algorithm outputs the sorted version of the list it received — not a random number [2].

Output closes the loop on the input/process/output model from topic 1.1: declaring the output upfront tells you — and anyone reading your algorithm — what the whole process is for [3].

### The four properties as a checklist

A **well-defined algorithm** satisfies all four properties simultaneously and can be executed correctly and consistently by anyone — or any computer — that follows it [1] [2].

| Property | The question to ask | What breaks if this is missing |
|---|---|---|
| **Finiteness** | Does it always stop? | Infinite loop — runs forever with no result |
| **Definiteness** | Is every step clear and precise? | Ambiguity — different people do different things |
| **Input** | Does it state what data it needs? | Nothing to work with — undefined behaviour |
| **Output** | Does it produce a result? | No visible effect — the algorithm did nothing useful |

A set of instructions that fails even one of these tests is not a well-defined algorithm [3].

## Worked Example

Here is a simple algorithm. Apply the four-property checklist to decide whether it is well-defined.

**Algorithm — Find the largest number in a list:**

1. Take the first number in the list. Call it "current largest."
2. Look at the next number in the list.
3. If the next number is larger than "current largest," replace "current largest" with it.
4. Repeat steps 2–3 until you have checked every number in the list.
5. Report "current largest" as the result.

**Checklist:**

- **Finite?** Yes. Step 4 ends when every number has been checked. The list has a fixed length, so this always terminates.
- **Definite?** Yes. Every step uses precise language: "larger than," "replace," "every number."
- **Input?** Yes. The input is a list of numbers (at least one number required).
- **Output?** Yes. The output is the largest number found.

This passes all four. It is a well-defined algorithm [1] [3].

**Counter-example — an algorithm that fails:**

> "Find a good number. Keep looking until you are satisfied."

- **Finite?** No — "until you are satisfied" has no measurable stopping condition.
- **Definite?** No — "good number" and "satisfied" are undefined.
- **Input?** Unclear — no list or range is stated.
- **Output?** Unclear — no defined result is declared.

This fails all four properties. It is not a well-defined algorithm [2].

## In Practice

You can apply the four-property checklist to any algorithm you write. Here is the sequence:

1. **Test finiteness.** Trace through the steps. Is there a stopping condition for every loop? Can you guarantee that condition will be reached?
2. **Test definiteness.** Read each step as if you are a machine with no common sense. Is any word or phrase open to more than one interpretation? If yes, rewrite it precisely.
3. **Test input.** List every piece of data the algorithm needs to start. Are all of them declared? Does the algorithm ever use information it was never given?
4. **Test output.** Identify what the algorithm produces at the end. Is there at least one result? Does it follow logically from the inputs and the steps?

**Real-world patterns — where all four properties must hold:**

- **ATM cash dispensing** — must terminate after fixed steps (finiteness), follow definite rules for every case such as insufficient balance (definiteness), accept the amount requested and your PIN as input (input), and produce cash plus a receipt (output) [1].
- **Search engine** — must stop after returning results (finiteness), know exactly how to measure relevance (definiteness), receive your search query (input), and return a ranked list of results (output) [2].
- **Airport boarding** — must finish when all passengers are grouped (finiteness), use definite rules such as "Group A = rows 1–10" (definiteness), take the passenger list as input (input), and produce an ordered boarding sequence (output) [3].

These real-world systems fail exactly when one of the four properties breaks down — for example, a payment system that loops indefinitely when a server is slow is a finiteness failure; a form that accepts "any name" without specifying the allowed format is a definiteness failure.

**Common mistakes to avoid:**

- Using words like "a bit," "somehow," "appropriately," or "as needed" — these break definiteness.
- Assuming a loop "will obviously stop eventually" — identify the exact termination condition instead.
- Writing an algorithm that silently discards its result — always make the output explicit.
- Treating the four properties as formalities — each one prevents a real class of failure.

**Try it yourself (lab activity):**

1. Choose an everyday process — for example, making a cup of tea or unlocking a phone. Write it out as 5–8 numbered steps.
2. Apply the four-property checklist to your own steps: Does it always stop? Is every step precise? What are the inputs? What is the output?
3. Swap with a partner. Can they follow your instructions exactly, without asking any questions? Any step that prompts a question is a definiteness gap — rewrite that step until it is unambiguous.

## Key Takeaways

- A **well-defined algorithm** must satisfy four properties: **finiteness** (always stops), **definiteness** (every step has exactly one valid interpretation), **input** (declares the data it needs — zero or more items), and **output** (produces at least one result).
- Failing any single property makes the instructions unreliable — a computer following them could loop forever, behave unpredictably, or produce nothing useful.
- **Finiteness** requires a clear stopping condition for every loop; "keep going until it feels right" is not a stopping condition.
- **Definiteness** is the formal name for the "unambiguous steps" requirement from topic 1.9 — every step must have exactly one valid interpretation.
- **Input** and **output** ground the algorithm in the input/process/output model from topic 1.1 — input declares what the algorithm needs; output declares what it will produce.

## References

1. Aristides Bouras, "Properties of an Algorithm," *Algorithmic Thinking*. <https://bouraspage.com/repository/algorithmic-thinking/properties-of-an-algorithm>
2. Study.com, "Properties of Algorithms." <https://study.com/academy/lesson/properties-of-algorithms.html>
3. Quescol, "Algorithm Criteria and Characteristics." <https://quescol.com/data-structure/algorithm-criteria-and-characteristics>

---
<!-- nav:bottom:start -->
[⬅ Previous: 1.10 — Algorithms in everyday life](../../1-10-algorithms-in-everyday-life-recipes-gps-routes-sorting-queue/artifacts/reading.md)&emsp;·&emsp;[⬆ Table of Contents](../../../../../../../README.md#curriculum-topic-index)&emsp;·&emsp;[Next: 1.12 — Choosing your domain ➡](../../../5-applying-it-to-your-domain/1-12-choosing-your-domain-writing-a-3-sentence-problem-statement/artifacts/reading.md)
<!-- nav:bottom:end -->
