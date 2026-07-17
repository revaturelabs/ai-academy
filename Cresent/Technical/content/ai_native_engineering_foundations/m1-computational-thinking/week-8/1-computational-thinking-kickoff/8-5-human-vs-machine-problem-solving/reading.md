<!-- GENERATED FILE — DO NOT EDIT BY HAND.
     Cresent view of 8.5 — Human vs Machine Problem-Solving.
     Source of truth: CIT 1.9, CIT 1.10, CIT 1.11.
     Regenerate: python Cresent/Technical/tools/generate_shared_readings.py -->
<!-- nav:top:start -->
Previous: [⬅ 8.4 — Why AI Gives Different Answers](../8-4-why-ai-gives-different-answers/reading.md)&emsp;·&emsp;[⬆ Table of Contents](../../../../../../README.md#part-b)&emsp;·&emsp;[9.1 — Core Computational Thinking Skills ➡](../../../week-9/1-computational-thinking/9-1-core-computational-thinking-skills/reading.md)
<!-- nav:top:end -->

---

# Algorithmic thinking — what makes a set of steps an algorithm

## Overview

You have already seen how to break a problem apart (decomposition), sketch a solution in plain English (pseudocode), and draw it as a flowchart. But not every list of steps is actually an algorithm. A recipe a human can muddle through — filling gaps with common sense — is not the same as a set of instructions a machine can follow without any guessing. Computers cannot fill in gaps. This reading explains what turns an ordinary list of steps into a true algorithm, and how the habit of thinking in algorithms makes you a sharper problem-solver long before you write a single line of code.

## Key Concepts

### What is an algorithm?

An **algorithm** is a finite, unambiguous sequence of steps that takes defined inputs, processes them, and always produces a result [1]. Every word in that definition matters:

- **Finite** — the steps end. They do not run forever.
- **Unambiguous** — each step has exactly one meaning. No step can be interpreted two different ways.
- **Defined inputs** — you know exactly what you are starting with.
- **Result** — you get a clear output you can inspect.

A cooking timer fits the definition: set it to 20 minutes, press start, the timer counts down, it beeps. Every run of those steps produces the same outcome. A note saying "cook until it smells right" does not — "smells right" means something different to every person who reads it.

### Instructions vs. algorithm — three ways a list of steps can fail

Most informal instructions fail as algorithms for one of three reasons [1]:

| Failure mode | What goes wrong | Example |
|---|---|---|
| **Missing steps** | A step the human fills in automatically is never written down | "Make tea" — steeping time is never mentioned |
| **Vague steps** | A step uses a word that has no single fixed meaning | "Add sugar to taste" — how much exactly? |
| **Wrong order** | Steps are listed out of sequence | "Boil the water after adding the tea bag" — the bag goes in cold water |

Any one of these three failures breaks a machine. Humans patch missing or vague steps with experience; machines cannot.

### Why vagueness breaks computation

Consider an instruction that says only "Do the right thing." A machine following this encounters the phrase and has no path forward. It might:

- halt and report an error,
- pick an arbitrary action and continue, or
- loop forever looking for more information.

None of those is the outcome you wanted. This is why **determinism** — the property you met in topic 1.2 — matters so much to algorithms. A deterministic process given the same input always produces the same output. Vague steps destroy determinism: two machines (or two runs of the same machine) hit "do the right thing" and produce different results. Edge cases — unusual but valid inputs — expose vagueness fastest, because they fall outside the normal scenario a human writer had in mind [2].

### The three properties every algorithm must have

An algorithm that works must be:

1. **Unambiguous** — every step has one and only one interpretation.
2. **Finite** — there is a stopping point; the process terminates.
3. **Result-producing** — the process delivers an observable output.

### What does "algorithmic thinking" mean?

**Algorithmic thinking** is the habit of writing steps precisely enough that even a machine — which has no common sense — could follow them. It is not a programming skill and it is not mathematics [1]. It is a mindset with four qualities:

- **Precise** — each step says exactly what to do, not roughly what to do.
- **Complete** — no step is missing; nothing is left for the reader to fill in.
- **Ordered** — steps are listed in the sequence they must happen.
- **Decisive** — when there is a choice to make, the rule for making it is written down.

### Version A vs. Version B — the diagram

The diagram below shows why these qualities matter in practice. On the left, a student exam pass/fail check written as a vague two-step instruction (Version A). On the right, the same check rewritten as a four-step algorithm with an explicit decision rule (Version B).

![Algorithmic thinking diagram](../../../../../../../../CIT/content-gen-example/content/m1-computational-thinking/week-1/4-algorithmic-thinking/1-9-algorithmic-thinking-what-makes-a-set-of-steps-an-algorithm/artifacts/diagram.png)
*Left: vague Version A instructions a human can interpret but a machine cannot follow. Right: Version B algorithm with an explicit score ≥ 50 decision rule that leaves no room for guessing.*

Notice that Version A says "check the result" without defining what counts as a pass. Version B states the rule — score ≥ 50 — so there is nothing left to interpret.

## Worked Example

The six-step mental checklist for turning a vague procedure into an algorithm:

1. Write down every step you can think of.
2. Check for missing steps — would a machine know what to do at every point?
3. Replace every vague word with a precise rule.
4. Put the steps in the order they must happen.
5. Add a decision rule for every fork — "if X, then Y; otherwise Z."
6. Confirm the process has a clear end and produces a result.

Here is that checklist applied to a library late-fee calculation — a domain the coffee and oven examples have not already covered.

| | Version A (informal) | Version B (algorithm) |
|---|---|---|
| **Step 1** | Look up the book | Receive the book's return date and today's date as inputs |
| **Step 2** | See if it's late | Calculate days overdue: today's date minus return date |
| **Step 3** | Charge a fee if needed | If days overdue > 0, multiply days overdue by the daily rate (£0.10) |
| **Step 4** | — *(missing)* | If days overdue ≤ 0, set fee to £0.00 |
| **Step 5** | — *(missing)* | Output the fee amount |
| **End** | Done | Stop |

Version A fails checklist items 2 (missing steps 4 and 5), 3 ("if needed" is vague — what counts as needed?), and 5 (no decision rule with a number). Version B passes all six checks: every step is written down, "overdue" is defined as a specific number of days, the fee rule uses a fixed rate, and there is a clear output and stop point [1].

## In Practice

Algorithmic thinking is not something that only matters when you sit down to code. It shows up any time a process must run the same way every time, regardless of who or what is running it.

**Medical protocols** — A hospital checklist for administering medication lists exact drug name, exact dose, exact time, and the patient's weight threshold. Nothing is left to "clinical judgment" mid-step; the judgment is built into the rule beforehand. Ambiguity in a medical protocol is a patient-safety risk. The same logic that makes an algorithm safe for a machine makes a protocol safe in a high-stakes human setting [2].

**GPS navigation** — When a GPS calculates a route, it runs an algorithm that checks every possible path, assigns a cost to each (distance, traffic, road type), and selects the lowest-cost path. The decision rule — compare costs, pick minimum — is explicit and repeatable. Every time you enter the same start and end address under the same traffic conditions, you get the same route. That reproducibility is only possible because the algorithm has no vague steps [3].

Both examples share the same pattern: a precise decision rule written in advance, applied consistently, producing a verifiable result.

## Key Takeaways

- An **algorithm** is a finite, unambiguous sequence of steps with defined inputs that always produces a result — not every list of instructions meets this bar.
- The three failure modes that prevent instructions from being algorithms are missing steps, vague steps, and wrong order.
- **Algorithmic thinking** is the habit of writing steps precisely, completely, in order, and with explicit decision rules — it is a mindset, not a programming skill.
- Vagueness destroys determinism: a step that can be interpreted two ways will produce two different outcomes, making the process unreliable.
- The six-step mental checklist — write, check for gaps, remove vague words, order correctly, add decision rules, confirm termination — turns any informal procedure into a true algorithm.

## References

[1] Bouras, A. S. (n.d.). *Properties of an Algorithm*. Retrieved from https://www.bouraspage.com/repository/algorithmic-thinking/properties-of-an-algorithm

[2] Wikipedia contributors. (n.d.). *Algorithm characterizations*. Wikipedia. https://en.wikipedia.org/wiki/Algorithm_characterizations

[3] Purdue CS182 course notes. (n.d.). *Algorithms and Growth of Functions*. https://www.cs.purdue.edu/homes/spa/courses/cs182/algorithms-rego.pdf

---

# Algorithms in Everyday Life — Recipes, GPS Routes, Sorting Queues

## Overview

You have been following algorithms your entire life — you just did not call them that. Every time you cook from a recipe, ask your phone for directions, or watch a website sort a list of search results, an algorithm is at work. This topic applies the definition of an algorithm from topic 1.9 to three concrete domains you already know, so you can recognise the structure in the world around you [1].

## Key Concepts

Algorithms show up in everyday life in three particularly clear domains: recipes, GPS routes, and sorting queues. Each one has the same shape — input goes in, a defined process runs, output comes out.

![Algorithms in everyday life: recipe, GPS, sorting — three parallel input→process→output flows](../../../../../../../../CIT/content-gen-example/content/m1-computational-thinking/week-1/4-algorithmic-thinking/1-10-algorithms-in-everyday-life-recipes-gps-routes-sorting-queue/artifacts/diagram.mmd)

*Each of the three domains follows the same algorithm structure: a defined input, a process with decisions and loops, and a stopping condition that produces the output.*

### Recipes

A recipe is one of the oldest examples of algorithmic thinking [1]. Consider a simple recipe for scrambled eggs:

1. Crack two eggs into a bowl.
2. Add a pinch of salt and pepper. Beat with a fork until fully mixed.
3. Melt half a teaspoon of butter in a non-stick pan over medium heat.
4. Pour the egg mixture into the pan.
5. Stir gently every 10 seconds.
6. If the eggs still look wet and liquid, continue stirring (return to step 5).
7. If the eggs look set and no longer liquid, remove from the heat.
8. Slide onto a plate. Stop.

Check this recipe against the algorithm properties from topic 1.9:

| Algorithm property | Does this recipe have it? | Where? |
|---|---|---|
| Precise steps | Yes | Exact quantities: "two eggs," "half a teaspoon" |
| Unambiguous | Yes | "Set and no longer liquid" is a testable condition |
| Complete | Yes | Every action from cracking eggs to plating is included |
| Stopping point | Yes | Step 8: Stop |
| A result | Yes | Scrambled eggs on a plate |

The recipe also uses the building blocks from topic 1.7: **sequence** (steps happen in order), **decision** (steps 6–7 form an if/otherwise branch), and **repetition** (step 5 loops until the decision is satisfied) [1][2].

**Why not every recipe qualifies.** Old recipe cards often say things like "bake until done" or "season to taste." These fail the algorithm test — "bake until done" does not define "done." A machine cannot evaluate it. A truly algorithmic recipe replaces that phrase with something testable: "Bake for 25 minutes, or until a toothpick inserted into the centre comes out clean." Either the toothpick comes out clean or it does not. The check is unambiguous [1].

| Part | What it is |
|---|---|
| Input | Raw ingredients and starting conditions |
| Process | Ordered steps, decisions, and loops |
| Output | The finished dish |

### GPS Routes

When you open a maps app and ask for directions, your phone does not guess a route. It runs an algorithm — a precise set of steps — to calculate the best path through all possible roads between your starting point and your destination [3].

**Route-finding** — the process an algorithm uses to discover a path from one point to another by evaluating travel costs for each possible road segment and choosing the lowest-cost option at each step.

Here is what the algorithm does, step by step:

1. Take your starting location and destination as the two inputs.
2. Build a picture of all connecting roads. Attach a travel time to each road segment.
3. From your current position, consider every road you could take next.
4. Calculate the total travel time to reach each candidate road from the start.
5. Pick the road segment with the lowest total travel time so far.
6. Repeat steps 3–5 from the new position until the destination is reached.
7. Trace back the path and output the turn-by-turn directions.
8. Stop.

Every step is exact. Every distance is measured. The algorithm stops when it reaches the destination — it does not run forever [3].

**What makes GPS algorithmic — not just guessing.** Compare a GPS route with vague directions: "Head north, go past the park, turn somewhere near the library." Those directions are ambiguous and rely on local knowledge the follower may not have. A GPS replaces every vague phrase with an exact rule: "Turn right in 300 metres at the intersection of Church Lane and Mill Road." Nothing is left to interpretation [3].

| Part | What it is |
|---|---|
| Input | Your starting location + your destination |
| Process | Evaluate travel times; always choose the lowest cumulative time; repeat until destination reached |
| Output | The unambiguous turn-by-turn sequence of directions |

One important point: the same algorithm, given the same inputs and the same traffic data, will always produce the same route. Change the traffic data and the algorithm produces a different route. The steps themselves do not change — the inputs do [3].

### Sorting Queues

Imagine 10 homework papers on a teacher's desk in random order. She wants them sorted alphabetically by student name. She compares the first two papers, swaps them if the second name comes before the first, then moves to the next pair, and keeps going until no more swaps are needed. She is following a repeatable, mechanical process — a sorting algorithm [1].

**Sorting algorithm** — a step-by-step process for putting a collection of items in a defined order by repeatedly comparing items and rearranging them according to a rule [2].

The process works like this:

1. Start at the beginning of the list.
2. Compare the first item and the second item.
3. If the first item should come after the second (based on the ordering rule), swap them.
4. Move to the next pair. Repeat steps 2–3.
5. Continue until you reach the end of the list. That is one pass.
6. If any swaps happened, go back to step 1 for a new pass.
7. If no swaps happened, the list is in order. Stop.

A short example makes this concrete:

Start: [Charlie, Alice, Bob]

- Pass 1, pair 1: "Charlie" vs "Alice" — C comes after A, so swap → [Alice, Charlie, Bob]
- Pass 1, pair 2: "Charlie" vs "Bob" — C comes after B, so swap → [Alice, Bob, Charlie]
- Pass 1 done. Swaps happened. Start Pass 2.
- Pass 2, pair 1: "Alice" vs "Bob" — no swap.
- Pass 2, pair 2: "Bob" vs "Charlie" — no swap.
- Pass 2 done. No swaps. Stop. Result: [Alice, Bob, Charlie] [1][2].

Sorting shows up constantly in everyday life:

- A website ranking search results by relevance.
- A music app listing songs alphabetically or by most-played.
- A school office organising exam papers by student number.
- A supermarket's self-checkout putting receipts in time order.

In every case the sorting algorithm does the same thing: compare, decide, rearrange, repeat until done [1].

| Part | What it is |
|---|---|
| Input | An unordered collection of items + a comparison rule |
| Process | Repeatedly compare pairs; swap when out of order; continue until no swaps needed |
| Output | The same items in the defined order |

### What all three domains share

Every example — recipes, GPS routes, sorting queues — is an algorithm because each has the same properties:

| Property | Recipe | GPS route | Sorting queue |
|---|---|---|---|
| Precise steps | Exact quantities and actions | Exact distances and road names | Exact comparison rule and swap condition |
| Complete | Every step from start to finish | Every road segment evaluated | Every pair compared |
| Unambiguous | Each step has one clear meaning | Each instruction has one valid action | The swap rule has no grey area |
| Stopping point | When the dish is plated | When the destination is reached | When no more swaps are needed |
| Input → process → output | Ingredients → cooking steps → finished dish | Start + destination → routing steps → directions | Unsorted list → compare/swap loop → sorted list |

The pattern: every algorithm has a defined starting state (input), a defined procedure (the steps), and a defined ending state (output + stop). Varying the input changes the output; the procedure itself stays the same [1][2][3].

## Worked Example

This worked example shows how to turn a vague real-world description into a proper algorithm.

**Scenario:** A cinema kiosk serves a queue of customers in arrival order. The manager wrote: "Serve customers in order. Be fair."

**Step 1 — Identify inputs and output.**
- Input: A list of customers, each with an arrival timestamp.
- Output: An ordered list of customers, earliest arrival first.

**Step 2 — Write the steps in plain language.**
"Check who arrived first and serve them. Move to the next person."

**Step 3 — Test for algorithmic quality.**

| Check | Result |
|---|---|
| Precise? | No — "check who arrived first" is vague when two customers share a timestamp |
| Complete? | No — does not say what to do when the queue is empty |
| Unambiguous? | No — "be fair" has no defined meaning for a machine |
| Has a stopping point? | No — "move to the next person" loops without stopping |

**Step 4 — Rewrite as an algorithm.**

1. Read the full list of customers and their arrival times.
2. Sort the list by arrival time, earliest first. If two customers share the same arrival time, sort alphabetically by surname.
3. Serve the customer at the top of the sorted list.
4. Remove that customer from the list.
5. If the list is not empty, go back to step 3.
6. If the list is empty, stop.

**Step 5 — Check again.**

| Check | Result |
|---|---|
| Precise? | Yes — every rule is exact, including the tie-breaking rule |
| Complete? | Yes — the empty-queue case is handled in step 6 |
| Unambiguous? | Yes — "alphabetically by surname" is a defined comparison rule |
| Has a stopping point? | Yes — step 6 stops when the list is empty |

This is the same discipline from topic 1.9: take a vague human description, expose every hidden assumption, and replace each assumption with an explicit, testable rule [1][3].

## In Practice

The three domains in this topic appear constantly in the technology you use every day.

**Procedure algorithms (like recipes).** Any app that walks you through a task step by step — a fitness app counting reps, a tax app guiding you through each form field — is running a procedure algorithm. The design challenge is always the same: every step must be precise enough that someone unfamiliar with the task can follow it without guessing [1].

**Network routing algorithms (like GPS).** Route-finding is not limited to roads. An email system routes your message through a network of servers using a routing algorithm — evaluate the options, pick the best path, continue until the destination is reached. A streaming service uses the same logic to find the nearest content delivery server [3].

**Sorting algorithms.** Sorting is one of the most common operations in any software system. Every time a spreadsheet sorts a column, a search engine orders results, or an e-commerce site ranks products by price, a sorting algorithm ran. The comparison rule changes — alphabetical, numerical, by rating — but the structure never does: compare, decide, rearrange, repeat, stop [1][2].

**Common pitfalls to avoid:**

- Do not mistake a goal for a step. "Serve customers fairly" is a goal, not an instruction.
- Do not assume a machine can infer context. "Bake until done" means nothing without a definition of "done."
- Do not forget the tie-breaking rule. Sorting fails when two items compare as equal and no rule says what happens next.

| Vague (not algorithmic) | Precise (algorithmic) |
|---|---|
| "Cook until ready" | "Cook for 8 minutes, or until the internal temperature reaches 75°C" |
| "Take the fastest route" | "Compare cumulative travel times; always choose the segment with the smallest total" |
| "Put these in order" | "Sort alphabetically A–Z; if two items start with the same letter, sort by the second letter" |
| "Serve customers fairly" | "Serve the customer with the earliest arrival timestamp; for equal timestamps, sort alphabetically by surname" |

## Key Takeaways

- Algorithms are not abstract — you encounter them every time you follow a recipe, use GPS navigation, or let an app sort a list for you.
- A **recipe** is an algorithm: it has inputs (ingredients), a process (ordered steps with decisions and loops), and an output (the finished dish). Vague recipe language ("bake until done") fails the algorithm test for the same reason vague instructions fail a machine.
- A **GPS route** is the output of an algorithm: the app takes your start and destination as inputs, evaluates road segments, selects the lowest-cost path at each step, and outputs an unambiguous turn-by-turn sequence. Same inputs, same route — every time.
- A **sorting algorithm** puts a collection in order by repeatedly comparing pairs of items and swapping them when out of order, stopping when no more swaps are needed. The comparison rule must be exact, or the process is not an algorithm.
- All three domains share the same properties from topic 1.9 — precise steps, completeness, no ambiguity, a defined stopping point, and a result. Varying the input changes the output; the procedure stays the same.

## References

1. learning.com — "7 Examples of Algorithms in Everyday Life for Students." https://www.learning.com/blog/7-examples-of-algorithms-in-everyday-life-for-students/
2. mimo.org — "Algorithm." Mimo Programming Concepts Glossary. https://mimo.org/glossary/programming-concepts/algorithm
3. enjoyalgorithms.com — "Introduction to Algorithms." https://www.enjoyalgorithms.com/blog/introduction-to-algorithms/

---

# The four properties of a good algorithm — finite, definite, input, output

## Overview

An algorithm is a precise, unambiguous set of steps — but what does "precise enough" actually mean? Computer scientists have agreed on four properties that every reliable algorithm must satisfy: **finiteness**, **definiteness**, **input**, and **output**. If even one property is missing, the instructions are not a well-formed algorithm — a computer following them could loop forever, behave unpredictably, or produce no result at all [1]. Learning these four properties gives you a concrete checklist to evaluate any algorithm you write or encounter [2].

## Key Concepts

Think of the four properties as four gates. An algorithm candidate must pass through every gate to earn the label "well-defined." The diagram below shows how the four properties work as a checklist — an algorithm candidate passes through each gate in turn.

![Four-property algorithm checklist](../../../../../../../../CIT/content-gen-example/content/m1-computational-thinking/week-1/4-algorithmic-thinking/1-11-the-four-properties-of-a-good-algorithm-finite-definite-inpu/artifacts/diagram.png)
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
Previous: [⬅ 8.4 — Why AI Gives Different Answers](../8-4-why-ai-gives-different-answers/reading.md)&emsp;·&emsp;[⬆ Table of Contents](../../../../../../README.md#part-b)&emsp;·&emsp;[9.1 — Core Computational Thinking Skills ➡](../../../week-9/1-computational-thinking/9-1-core-computational-thinking-skills/reading.md)
<!-- nav:bottom:end -->
