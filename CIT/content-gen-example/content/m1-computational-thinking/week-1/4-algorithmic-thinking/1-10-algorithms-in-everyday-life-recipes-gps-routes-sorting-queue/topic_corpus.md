---
topic_id: "1.10"
title: "Algorithms in everyday life — recipes, GPS routes, sorting queues"
position_in_module: 2
generated_at: "2026-06-22T00:00:00Z"
resource_count: 3
---

# 1. Algorithms in Everyday Life — Recipes, GPS Routes, Sorting Queues — Topic Corpus

## 2. Prerequisites

This topic builds directly on:

- **1.9 Algorithmic thinking** — the definition of an algorithm (a precise, complete, unambiguous, finite set of steps that solves a problem and produces a result) and the mindset of writing instructions precisely enough for a machine to follow without guesswork.

Concepts from earlier topics that appear here:
- **1.1 What is computation** — input → process → output
- **1.5 Decomposition** — breaking a task into sub-steps
- **1.7 Pseudocode** — sequence, decision, and repetition as the building blocks of logic
- **1.8 Flowcharts** — terminators, process boxes, decision diamonds, flowlines

## 3. Learning Objectives

By the end of this topic, you will be able to:

- Identify a familiar real-world process (a recipe, a GPS route, a queue sorting system) as an algorithm and explain why it qualifies.
- Trace the input → process → output structure through each of the three example domains.
- Spot where a vague everyday instruction would fail if a machine tried to follow it, and describe the fix.
- Explain, in plain language, how a GPS navigation app produces a route as an algorithm.
- Describe what a sorting algorithm does — in terms a non-technical person can understand — using a real-world queue or list as the example.
- Connect each example domain back to the properties of an algorithm established in topic 1.9.

## 4. Introduction

You have already been following algorithms for your entire life. You just did not call them that.

Every time you cook from a recipe, your phone gives you turn-by-turn directions, or a website lists search results in a useful order, an algorithm is at work. Sometimes you are the one running the algorithm — reading each step of a recipe in sequence, making decisions ("if the sauce looks too thick, add more water"), and stopping when the dish is done. Other times a machine runs the algorithm for you — your maps app silently calculates the fastest route and tells you what to do next.

Topic 1.9 gave you the definition: an algorithm is a precise, complete, unambiguous, finite set of steps that solves a problem and produces a result. This topic applies that definition to three concrete domains you already know from everyday life:

1. **Recipes** — following a sequence of cooking steps with decisions and stopping points.
2. **GPS routes** — a machine calculating the best path through a network of roads.
3. **Sorting queues** — putting items in order by comparing and rearranging them one step at a time.

By the end, you will be able to look at any of these and say: "I can see the algorithm in there" — and you will know exactly which part of the algorithm is doing which job [1].

## 5. Core Concepts

### 5.1 The recipe as an algorithm

A recipe is one of the oldest examples of algorithmic thinking. It was written down long before computers existed. Yet a good recipe has every property that makes a set of steps an algorithm [1].

Consider a simple recipe for making scrambled eggs:

1. Crack two eggs into a bowl.
2. Add a pinch of salt and a pinch of pepper.
3. Beat with a fork until the yolk and white are fully mixed.
4. Place a non-stick pan on medium heat and add half a teaspoon of butter.
5. Wait until the butter has melted and starts to bubble.
6. Pour the egg mixture into the pan.
7. Stir gently with a spatula every 10 seconds.
8. If the eggs look wet and liquid, continue stirring (go back to step 7).
9. If the eggs look set and no longer liquid, remove the pan from the heat.
10. Slide the eggs onto a plate.
11. Stop.

Now check this recipe against the algorithm properties from topic 1.9:

| Algorithm property | Does this recipe have it? | Where? |
|---|---|---|
| Precise steps | Yes | Every step uses exact quantities and actions ("two eggs," "half a teaspoon") |
| Unambiguous | Mostly yes | "Set and no longer liquid" is a testable stopping signal |
| Complete (nothing left out) | Yes | Every action from cracking eggs to plating is included |
| A stopping point | Yes | Step 11: "Stop." |
| A result | Yes | Scrambled eggs on a plate |

The recipe also uses the building blocks you learned in topic 1.7: **sequence** (steps 1–6 happen in order), **decision** (steps 8–9 form an if/otherwise branch), and **repetition** (step 7 loops back until the decision in steps 8–9 is satisfied) [1][2].

**Why recipes are not always algorithmic.** Not every recipe is as precise as this one. Old recipe cards often say things like "bake until done" or "season to taste." These phrases fail the algorithm test. "Bake until done" does not define "done." A machine cannot evaluate it. A beginner cook may not know what "done" looks like. A truly algorithmic recipe replaces that phrase with something like: "Bake for 25 minutes, or until a toothpick inserted into the centre comes out clean." That version is testable. Either the toothpick comes out clean or it does not. The machine — or the beginner — can check and decide [1].

**The recipe domain summarised:**

| Part | What it is |
|---|---|
| Input | Raw ingredients and starting conditions (pan temperature, quantities) |
| Process | The ordered list of steps, including decisions and loops |
| Output | The finished dish |

This is the same input → process → output structure you learned in topic 1.1. The recipe is just a familiar, kitchen-sized version of it [2].

### 5.2 GPS routes as algorithms

When you open a maps app and ask for directions from your home to a library, your phone does not guess a route. It runs an algorithm — a precise set of steps — to calculate the best path through all the possible roads between your starting point and your destination [3].

**Route-finding** — the process an algorithm uses to discover a path from one point to another across a network of connected roads, by evaluating travel costs for each possible road segment and choosing the lowest-cost option at each step.

Here is a simplified version of what happens, step by step:

1. The maps app takes your starting point and your destination as its two inputs.
2. It builds a picture of all the roads connecting nearby intersections. Every road segment has a measured travel time attached to it (based on speed limit and distance, or live traffic data).
3. It starts at your location and considers every road you could take from there.
4. For each possible next road, it calculates the total travel time to reach that road from the start.
5. It picks the road segment that gives the lowest total travel time so far.
6. It repeats steps 3–5 from the new position, adding more road segments, until it reaches your destination.
7. It traces back the path it built and outputs the sequence of turns: "Turn left on Oak Street in 400 metres. Turn right on Church Lane in 1.2 kilometres. Your destination is on the right."
8. Stop.

Every step is exact. Every distance is measured. The algorithm stops when it reaches the destination — it does not run forever. The output is a specific, ordered, unambiguous sequence of turn-by-turn directions [3].

**Why GPS navigation is algorithmic.** Compare a GPS route with the vague directions from topic 1.9: "Head north, go past the park, turn somewhere near the library." Those directions are not algorithmic — they are ambiguous, they rely on local knowledge the follower may not have, and they have no precise stopping condition. A GPS replaces every vague phrase with an exact rule. "Somewhere near the library" becomes "turn right in 300 metres at the intersection of Church Lane and Mill Road." Nothing is left to interpretation [3].

**The inputs, process, and output of GPS routing:**

| Part | What it is |
|---|---|
| Input | Your starting location + your destination |
| Process | Evaluate travel times for road segments; always choose the lowest cumulative time; repeat until destination reached |
| Output | The turn-by-turn sequence of directions |

**One more key point:** the same algorithm, given the same starting point and destination with the same traffic data, will always produce the same route. This is the determinism you learned in topic 1.2 — same input, same steps, same output, every time. Change the traffic data (a new input) and the algorithm produces a different route. The steps themselves do not change; the inputs do [3].

### 5.3 Sorting queues as algorithms

Imagine a stack of 10 homework papers on a teacher's desk, in random order. The teacher wants them in alphabetical order by student name. How does she do it?

She might compare the first two papers, swap them if the second name comes before the first alphabetically, then move to the next pair, and keep going until no more swaps are needed. She is following a repeatable, mechanical process that can be written down as exact steps — that is a sorting algorithm [1].

**Sorting algorithm** — a step-by-step process for putting a collection of items in a defined order by repeatedly comparing items and rearranging them according to a rule [2].

The most intuitive sorting process to understand works like this:

1. Start at the beginning of the list.
2. Compare the first item and the second item.
3. If the first item should come after the second item (based on the ordering rule), swap them.
4. Move to the next pair (second and third items). Repeat steps 2–3.
5. Continue until you reach the end of the list. That is one pass.
6. If any swaps happened during this pass, go back to step 1 and start a new pass.
7. If no swaps happened during the pass, the list is in order. Stop.

This process will always sort any list into the correct order, no matter how jumbled the starting state. It is precise (compare and swap is a defined action), complete (it handles every pair), unambiguous (the swap rule has no grey area), and finite (it stops when no swaps are needed) [2].

**A sorting example with a short list:**

Start: [Charlie, Alice, Bob]

- Pass 1, pair 1: Compare "Charlie" and "Alice." C comes after A, so swap. → [Alice, Charlie, Bob]
- Pass 1, pair 2: Compare "Charlie" and "Bob." C comes after B, so swap. → [Alice, Bob, Charlie]
- Pass 1 done. Swaps happened. Start Pass 2.
- Pass 2, pair 1: Compare "Alice" and "Bob." A comes before B. No swap.
- Pass 2, pair 2: Compare "Bob" and "Charlie." B comes before C. No swap.
- Pass 2 done. No swaps. **Stop.** Result: [Alice, Bob, Charlie] [1][2].

**Where you see sorting in everyday life.** Any time a list is put in a useful order, a sorting process ran:

- A website that shows search results ranked by relevance.
- A music app that lists songs alphabetically or by most-played.
- A school office that organises exam papers by student number.
- A supermarket's self-checkout putting receipts in time order.

In every case, the sorting algorithm does the same thing: compare two items, decide which comes first, rearrange, repeat until done [1].

**The inputs, process, and output of sorting:**

| Part | What it is |
|---|---|
| Input | An unordered collection of items + a comparison rule (alphabetical, numerical, chronological) |
| Process | Repeatedly compare pairs; swap when out of order; continue until no more swaps needed |
| Output | The same items in the defined order |

**What makes sorting algorithmic — not just tidying.** You can sort a list by feel — grab whatever looks wrong and move it. The result might be correct, but the process is not algorithmic because it relies on judgment about "whatever looks wrong." A sorting algorithm replaces that judgment with a defined rule: compare this item to that one; if this condition is true, swap; if not, do not swap. The rule is the same every time, applied to every pair, until the defined stopping condition is met [2].

### 5.4 What the three domains share

Every example in this topic — recipes, GPS routes, sorting queues — is an algorithm because each one has all the same properties:

| Property | Recipe | GPS route | Sorting queue |
|---|---|---|---|
| Precise steps | Exact quantities, exact actions | Exact distances, exact road names | Exact comparison rule, exact swap condition |
| Complete | Every step from start to finish included | Every road segment evaluated, every turn named | Every pair compared, every swap recorded |
| Unambiguous | Each step has one clear meaning | Each instruction has one valid action | The swap rule has no grey area |
| Stopping point | Stop when the dish is plated | Stop when destination is reached | Stop when no more swaps are needed |
| Input → process → output | Ingredients → cooking steps → finished dish | Start + destination → routing steps → turn-by-turn directions | Unsorted list → compare/swap loop → sorted list |

The pattern that holds across all three: every algorithm has a defined starting state (input), a defined procedure (the steps), and a defined ending state (output + stop). Varying the input changes the output, but the procedure itself stays the same. This is why algorithms are powerful — one procedure can handle many different inputs and produce correct results each time [1][2][3].

## 6. Implementation

This section walks through turning a vague real-world description into a proper algorithm. Use this as a mental checklist.

**Scenario:** A cinema ticket kiosk serves a queue of customers in arrival order. The manager wrote down: "Serve customers in order. Be fair."

**Step 1 — Identify the inputs and the output.**
- Input: A list of customers, each with an arrival timestamp.
- Output: An ordered list of customers, earliest arrival first.

**Step 2 — Write the steps in plain language.**
"Check who arrived first and serve them. Move to the next person."

**Step 3 — Test for algorithmic quality.**

| Check | Result |
|---|---|
| Precise? | No — "check who arrived first" is vague when two customers have the same timestamp |
| Complete? | No — does not say what to do when the queue is empty |
| Unambiguous? | No — "be fair" has no defined meaning for a machine |
| Has a stopping point? | No — "move to the next person" loops without stopping |

**Step 4 — Rewrite as an algorithm.**

1. Read the full list of customers and their arrival times.
2. Sort the list by arrival time, earliest first. If two customers have the same arrival time, sort them alphabetically by surname.
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

This is the same discipline you practised in topic 1.9: take a task described in vague human language, expose every hidden assumption, and replace each assumption with an explicit, testable rule [1][3].

## 7. Real-World Patterns

The three algorithm domains in this topic appear constantly in the technology you use every day.

**Recipes and procedure algorithms.** Whenever an app walks you through a task step by step — a fitness app counting your reps and instructing you on the next exercise, a tax app guiding you through each form field in order — you are being walked through a procedure algorithm. The design challenge is always the same as for a recipe: every step must be precise enough for someone unfamiliar with the domain to follow without guessing [1].

**GPS routing and network algorithms.** Route-finding algorithms are not limited to roads. An email system routes your message from your device through a network of servers to the recipient — it uses a routing algorithm to decide which server to pass the message through next. A streaming service decides which content delivery server is closest to you by running a similar calculation. The underlying idea — evaluate the options, pick the best path, continue until the destination is reached — is the same in each case [3].

**Sorting and ordering algorithms.** Sorting is one of the most common operations in any software system. Every time a spreadsheet sorts a column, a search engine orders its results, or an e-commerce site ranks products by price, a sorting algorithm ran. The comparison rule changes — alphabetical, numerical, by rating, by date — but the structure is always the same: compare, decide, rearrange, repeat, stop [1][2].

## 8. Best Practices

When you are trying to recognise or write an algorithm in a real-world context, these habits will keep you on track.

**Do:**
- Look for the input → process → output structure. If you can name all three parts, you are likely looking at something algorithmic.
- Check whether the stopping condition is defined. "Until done" is not a stopping condition. "Until no more swaps are needed" is.
- Check whether the comparison rule (in sorting) or the decision condition (in branching) has exactly one valid answer for any given situation.
- When a step says "choose the best option," ask: "best by what rule?" That rule must be stated explicitly.

**Do not:**
- Mistake a list of goals for an algorithm. "Serve customers fairly" is a goal, not a step.
- Assume a machine can infer context. "Bake until done" means nothing to a machine.
- Forget the tie-breaking rule. Sorting processes fail when two items compare as equal and no rule says what happens next.

| Vague (not algorithmic) | Precise (algorithmic) |
|---|---|
| "Cook until ready" | "Cook for 8 minutes, or until the internal temperature reaches 75°C" |
| "Take the fastest route" | "Compare cumulative travel times for all candidate road segments; always choose the segment with the smallest total" |
| "Put these in order" | "Sort alphabetically A–Z; if two items start with the same letter, sort by the second letter" |
| "Serve customers fairly" | "Serve the customer with the earliest arrival timestamp first; for equal timestamps, sort alphabetically by surname" |

## 9. Hands-On Exercise

Choose one of the three domains from this topic and turn a vague real-world description into a proper algorithm.

1. Pick your domain: a recipe you know, a set of directions you give someone regularly, or a way you sort or organise things (papers, a playlist, a bookshelf).
2. Write the vague version first — the kind of description you would give a friend who already knows the task.
3. Read it back as if you were a machine that cannot assume anything. Find every phrase that requires judgment or guesswork.
4. Rewrite each vague phrase as an exact rule. Add any missing steps. Add a clear stopping condition.
5. Check your rewrite against the four properties: precise, complete, unambiguous, has a stopping point.

Share your before-and-after with a classmate. Ask them to follow your rewritten version literally. Does it produce the right result without them needing to ask you any questions?

## 10. Key Takeaways

- An algorithm is not an abstract idea — it is something you encounter every time you follow a recipe, use GPS navigation, or let an app sort a list for you.
- A **recipe** is an algorithm: it has inputs (ingredients), a process (ordered steps with decisions and loops), and an output (the finished dish). Vague recipe language ("bake until done") fails the algorithm test for the same reason vague code does.
- A **GPS route** is the output of an algorithm: the app takes your start and destination as inputs, runs a route-finding process that evaluates road segments and selects the lowest-cost path at each step, and outputs an unambiguous turn-by-turn sequence. Same inputs, same route — every time.
- A **sorting algorithm** puts a collection in order by repeatedly comparing pairs of items and swapping them when they are in the wrong order, stopping when no more swaps are needed. The comparison rule must be exact, or the process is not an algorithm.
- All three domains share the same algorithm properties from topic 1.9: precise steps, completeness, no ambiguity, a defined stopping point, and a result. Varying the input changes the output; the procedure stays the same.

## 11. Next Steps

_System-derived from the next entry in curriculum/sequence.md._
