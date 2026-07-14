<!-- nav:top:start -->
[⬅ Previous: 1.9 — Algorithmic thinking](../../1-9-algorithmic-thinking-what-makes-a-set-of-steps-an-algorithm/artifacts/reading.md)&emsp;·&emsp;[⬆ Table of Contents](../../../../../../../README.md#curriculum-topic-index)&emsp;·&emsp;[Next: 1.11 — The four properties of a good algorithm ➡](../../1-11-the-four-properties-of-a-good-algorithm-finite-definite-inpu/artifacts/reading.md)
<!-- nav:top:end -->

---

# Algorithms in Everyday Life — Recipes, GPS Routes, Sorting Queues

## Overview

You have been following algorithms your entire life — you just did not call them that. Every time you cook from a recipe, ask your phone for directions, or watch a website sort a list of search results, an algorithm is at work. This topic applies the definition of an algorithm from topic 1.9 to three concrete domains you already know, so you can recognise the structure in the world around you [1].

## Key Concepts

Algorithms show up in everyday life in three particularly clear domains: recipes, GPS routes, and sorting queues. Each one has the same shape — input goes in, a defined process runs, output comes out.

![Algorithms in everyday life: recipe, GPS, sorting — three parallel input→process→output flows](./diagram.mmd)

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
<!-- nav:bottom:start -->
[⬅ Previous: 1.9 — Algorithmic thinking](../../1-9-algorithmic-thinking-what-makes-a-set-of-steps-an-algorithm/artifacts/reading.md)&emsp;·&emsp;[⬆ Table of Contents](../../../../../../../README.md#curriculum-topic-index)&emsp;·&emsp;[Next: 1.11 — The four properties of a good algorithm ➡](../../1-11-the-four-properties-of-a-good-algorithm-finite-definite-inpu/artifacts/reading.md)
<!-- nav:bottom:end -->
