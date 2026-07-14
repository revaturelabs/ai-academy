---
topic_id: "1.1"
title: "What is computation"
position_in_module: 1
generated_at: "2026-06-19T00:00:00Z"
resource_count: 3
---

# 1. What is computation — Topic Corpus

## 2. Prerequisites

_No formal prerequisites._

## 3. Learning Objectives

By the end of this topic, you will be able to:

- Describe what computation means in plain, everyday terms.
- Explain the idea that a computer follows a set of instructions to produce a result.
- Give at least two real-world examples of computation happening outside a computer.
- Identify the three basic parts of any computation: input, process, and output.
- Distinguish between a task a computer can compute and one it currently cannot.

## 4. Introduction

You use computation every day — even when you are not near a computer.

When you type a search query into a phone and get results back, something happened in between. When a GPS app tells you to "turn left in 200 metres," something decided that route was better than the alternatives. That "something" is computation.

Computation sounds technical, but the core idea is simple. It means: **take some information in, do something with it, and produce a result**. That is it. A calculator does this. Your phone does this. A traffic-light controller does this. Even a recipe does a version of this — you take ingredients (input), follow steps (process), and get a meal (output).

This topic answers one question: *what exactly is computation?* Once you have that answer, the rest of this course builds on it — exploring how computers make decisions, how AI systems work, and how you can think like a problem-solver even before you write a single line of code.

## 5. Core Concepts

### 5.1 The word "computation" — what it actually means

**Computation** — any process that takes information, applies a defined set of steps to it, and produces a result.

The word comes from the Latin *computare*, meaning "to reckon" or "to calculate." For centuries, a "computer" was a *person* — someone whose job was to perform arithmetic by hand. Human computers calculated artillery tables, navigation routes, and census data. Only in the twentieth century did the word shift to mean an electronic machine [1].

Today, computation refers to any systematic processing of information — whether it happens inside a silicon chip, in a human brain doing long division, or in a mechanical device like an abacus [1].

Three things are always present in computation:

1. **Input** — the raw information going in. (Example: the numbers you type into a calculator.)
2. **Process** — the defined steps applied to that information. (Example: the addition or multiplication rules.)
3. **Output** — the result that comes out. (Example: the answer shown on the display.)

This input → process → output pattern is so fundamental that you will see it again and again throughout this course and throughout your career.

**Why the three-part model matters.** It is easy to think of computation as something that only happens inside computers. The I/P/O model breaks that assumption. Once you can identify the three parts, you can recognise computation anywhere — in a thermostat, in a boardroom decision checklist, in the immune system's response to a virus. The model also gives you a framework for *designing* computational solutions: before you write a single line of code, the first questions to answer are always "what is the input?", "what steps transform it?", and "what output do I need?" [1].

**A brief history: humans as computers.** Before electronic machines, organisations employed rooms full of human computers. During the Second World War, the ballistics tables used by artillery crews were calculated by teams of women — each person performing one arithmetic step and passing the result to the next. The NASA space programme used human computers, including mathematicians, to calculate launch trajectories by hand until the 1960s. This history is worth knowing for two reasons. First, it shows that computation is a *process*, not a machine — the process existed long before the machines. Second, it shows that the rules of computation are stable across very different substrates: a person with a pencil, a mechanical calculator, and a modern processor all apply the same arithmetic rules. The device changes; the structure of the process does not [1].

**Scaling up: from a single calculation to a system.** A single computation — add 3 and 5 — is trivial. What makes modern computing interesting is that billions of these trivial operations can be chained together, running faster than a human can blink. A weather forecast involves hundreds of billions of arithmetic operations applied to sensor readings from satellites, ships, and weather stations. Each individual operation follows the same I/P/O structure. Computation at scale is just many small I/P/O steps coordinated into a larger I/P/O structure. The input to the whole system might be "sensor readings from 10,000 weather stations," the process is a large set of mathematical rules, and the output is "tomorrow's forecast" [1].

### 5.2 "Defined steps" — why a recipe is a useful model

The word *defined* is doing important work in the definition above. Computation requires that the steps are **specific and unambiguous** — not vague guidelines, but precise instructions that leave no room for guessing [1].

Think about a recipe. "Add a pinch of salt" is a vague instruction — two cooks would add different amounts. "Add exactly 2 grams of salt" is a defined instruction — every cook would add the same amount. Computation works like the second version [1].

When the steps are specific enough that any machine (or person, or robot) could follow them and always get the same result, you have the seed of a computational process [1].

This idea — that computation needs precise, unambiguous steps — is why engineers and scientists spent so much of the twentieth century figuring out how to write instructions clearly. It is also why languages like pseudocode and flowcharts exist; you will cover those in later topics in this module.

**What "unambiguous" looks like in practice.** Consider the instruction "go to the nearest exit." This sounds simple, but it is ambiguous: nearest by straight-line distance, or by walkable path? Nearest with the door already open, or any door? A human interprets common sense; a machine cannot. A computation-ready version of the same instruction might read: "find all exits with unlocked doors; calculate the walking distance to each; return the exit with the smallest walking distance." Every word in that version can be executed mechanically, with no interpretation required [1].

**Why ambiguity is the enemy of computation.** When steps are ambiguous, two executions of the same process on the same input can produce different outputs. That makes the process unreliable and unverifiable. Reliable computation — the kind you can trust to run a hospital ventilator or a bank's payment system — depends absolutely on defined steps. Ambiguity is not just an inconvenience; in safety-critical systems, it is a design failure [1].

### 5.3 What makes something "computable"

Not everything is computable. **Computable** means: there exists a finite set of defined steps that always produces the correct result in a finite amount of time [1].

Here are examples on both sides of that line:

| Task | Computable? | Why |
|---|---|---|
| Add two numbers | Yes | Clear steps, always finishes [1] |
| Sort a list of names alphabetically | Yes | Clear steps, always finishes [1] |
| Find the shortest route between two cities | Yes | A set of defined steps exists; takes time, but always finishes [1] |
| Convert a temperature from Celsius to Fahrenheit | Yes | Single arithmetic formula, always finishes [1] |
| Check whether a password meets complexity rules | Yes | Rules are precise and verifiable; always finishes [1] |
| Decide whether any given poem is "beautiful" | Not fully | No precise, agreed-upon steps exist |
| Predict exactly what weather will be in 10 years | Not fully | Too many unknowns; steps exist but result is approximate |
| Decide whether *any* possible program will eventually stop | Not fully | Proved unsolvable in general — no finite set of steps works for all cases |

The boundary between computable and not-yet-computable shifts over time. Problems once considered impossible for machines — like recognising speech or identifying objects in photos — are now solved by modern AI (Artificial Intelligence) systems [2][3]. You will explore those systems later in this course.

**Why the boundary matters.** Knowing whether a task is computable shapes how you approach it. If a task is fully computable, you can design a reliable process and deploy it at scale. If a task is only partially computable — like predicting weather far in advance — you can still build a system, but you have to be honest about its limits: it will give you a *probability*, not a certainty. Many real-world systems, including modern AI, are built on this second model. They do not give definitive answers; they give well-informed probabilities [1][2].

**The role of time.** Computability is not just about whether steps exist, but whether they finish in a *reasonable* amount of time. Some problems are technically computable but take so long that they are practically impossible: if computing the answer to a chess game required a billion years, the answer is useless even though it exists in principle. Computer scientists study the relationship between problem size and computation time, which is why phrases like "this would take longer than the age of the universe" appear in technical discussions. For this course, the key point is that "computable" implicitly includes "fast enough to be useful" [1].

### 5.4 Computers are not the only things that compute

The word "computer" today almost always means an electronic device — a laptop, a phone, a server. But the concept of computation is broader.

Anything that takes an input, applies defined steps, and produces an output is performing computation. Examples outside a typical electronic computer:

**Traffic light on a timer.**
- Input: time elapsed since last phase change.
- Process: a fixed sequence encoded in the controller — if time ≥ green_duration, switch to amber; if time ≥ amber_duration, switch to red; if time ≥ red_duration, switch to green.
- Output: the light signal displayed to drivers and pedestrians.
The process is deterministic: the same elapsed-time input always produces the same phase output. There is no random element; the light behaves exactly the same every cycle [1].

**Vending machine.**
- Input: coins inserted (value), button pressed (item identifier).
- Process: check whether inserted value ≥ item price; check whether the selected item is in stock; if both conditions true, dispatch item and return change; otherwise return coins.
- Output: dispensed item + change, or all coins returned.
This is a slightly more complex computation — it involves a conditional (an if/then branch). The machine computes two things simultaneously: the arithmetic (is there enough money?) and a stock check (is the item available?). Modern vending machines add further steps: logging each transaction, detecting coin jams, reporting low-stock alerts. Each additional feature adds steps to the process without changing the fundamental I/P/O structure [1][2].

**Human cashier counting change.**
- Input: the purchase price and the amount of money handed over.
- Process: subtract purchase price from amount received; decompose the difference into the fewest notes and coins available.
- Output: the correct change denominations handed back.
A cashier does this computation mentally. The same process runs in the electronic point-of-sale terminal on the counter — the substrate is different, but the steps are identical [1].

**A mechanical music box.**
- Input: a physical cylinder with raised pins at precise positions.
- Process: as the cylinder rotates, each pin plucks a specific metal tine; the tine vibrates at its tuned frequency.
- Output: a melody.
The "program" for this computation is physical — encoded as the arrangement of pins on the cylinder. Swapping cylinders changes the melody. This is an early example of *stored computation*: the process is fixed, but the input (the cylinder) determines the output. You can think of the cylinder as an early form of data storage [1].

**A thermostat.**
- Input: the current room temperature read by a sensor.
- Process: compare current temperature against the set-point temperature; if current < set-point, activate heating; if current ≥ set-point + tolerance, deactivate heating.
- Output: on/off signal to the heating system.
A thermostat is one of the simplest feedback-driven computations in everyday life. The output (heating on or off) changes the environment, which then changes the next input (room temperature). This loop — output affecting future input — is called a *feedback loop* and appears in everything from cruise control to industrial process management [1].

None of these require a silicon chip. They all perform computation [1][2].

Recognising computation in the world around you — not just on screens — is the first step in **computational thinking**, which is the core skill this entire course builds.

**Computational thinking** — approaching a problem the way you would need to in order to explain it to a machine: by breaking it into steps, spotting patterns, and expressing a solution precisely [1]. You will build this skill across all six modules of the course.

### 5.5 Why this matters for AI

Modern AI systems — including the chat tools and recommendation systems you probably already use — are also performing computation. They take inputs (your words, your click history, an image), apply large sequences of defined steps, and produce outputs (a reply, a recommendation, a label).

What makes AI computation interesting is that the steps were not all hand-written by a programmer. A large part of them were determined through a process you will explore in a later module — but the fundamental structure is the same: input → process → output [2][3].

You will explore deterministic systems and probabilistic systems in topics 1.2 and 1.3, and the reason AI gives different answers to the same question in topic 1.4. For now, the key point is: **AI is computation**. Understanding computation is understanding the foundation everything else sits on.

## 6. Implementation

There is no code in this topic. Computation as a concept predates programming languages.

If you want to see the input → process → output structure in action right now, try this thought experiment:

1. Pick any everyday device: a microwave, a lift (elevator), a turnstile at a metro station.
2. Write down what goes **in** (input).
3. Write down what the device **does with it** (process — as specifically as you can).
4. Write down what comes **out** (output).

This mental exercise is the first move in computational thinking. You are not writing code — you are recognising structure.

## 7. Real-World Patterns

Computation appears in every industry. Here are three domains where you will see it explicitly named:

**Manufacturing — automated quality control.**

Modern assembly lines rely on machine-vision systems to inspect every item produced. Here is how the computation unfolds in a typical bottling plant:

- *Input:* a high-resolution image of each bottle captured by a camera mounted above the conveyor belt; metadata including the production batch number and timestamp.
- *Process:* the image is passed through a rule set that checks fill level (is the liquid within the tolerance band?), cap position (is the cap fully seated?), label alignment (is the label within ±2mm of the target position?), and container integrity (are there cracks or deformations?). Each check is a comparison: measured value vs acceptable range.
- *Output:* a pass/fail signal sent to a pneumatic arm. Pass: bottle continues down the conveyor. Fail: the pneumatic arm diverts the bottle to a rejection bin. A count of failures per batch is logged for quality-control reporting.

Every step is defined and unambiguous. The same image, run through the same rule set, produces the same result every time. This is deterministic computation at industrial scale — thousands of I/P/O cycles per minute [3].

**Finance — fraud detection.**

Every time you use a bank card, a fraud-detection computation runs in the background, typically completing in under 200 milliseconds:

- *Input:* transaction record containing: merchant category code, transaction amount, geographic location, time of day, device fingerprint, and the cardholder's recent transaction history.
- *Process:* the transaction is scored against hundreds of rules and statistical patterns. Examples of individual rules: "transaction amount is 5× the 30-day average" triggers a suspicion flag; "two transactions in different countries within 1 hour" triggers a high-risk flag; "merchant category mismatch with the customer's typical spending profile" triggers a soft flag. The rule outputs are aggregated into a single risk score.
- *Output:* a decision — approve, decline, or route to secondary review. A risk score above a high threshold triggers an automatic decline and an SMS alert to the cardholder. A score in the medium band routes the transaction to a human analyst queue for review [2][3].

This system performs computation billions of times per day, globally. The defined steps are reviewed and updated by data science teams as fraud patterns evolve — but at any given moment, the system is executing deterministic rules on well-defined inputs to produce a binary decision output [2][3].

**Healthcare — diagnostic decision support.**

AI-assisted diagnostic tools are now deployed in radiology departments to help detect conditions such as diabetic retinopathy, pneumonia, and certain cancers from scanned images:

- *Input:* a digital scan (X-ray, MRI, or retinal photograph) along with the patient's age, clinical history flags, and scan metadata.
- *Process:* the image is processed through a set of rules that identify structural features — density gradients, edge patterns, symmetry deviations from normal baseline profiles. Each feature is evaluated against threshold values and context rules. The system does not render a diagnosis; it calculates a probability score for a small set of candidate conditions.
- *Output:* a ranked list of candidate conditions, each paired with a probability score and a visual overlay on the scan highlighting the regions that contributed most to the score. A radiologist reviews this output before any clinical decision is made.

Critically, the output is a *probability*, not a verdict. The computation is designed to augment a clinician's judgment, not replace it. This reflects a key property of probabilistic computation: unlike the quality-control bottling example where every decision is deterministic, diagnostic AI acknowledges uncertainty in its output explicitly [2][3].

In every case: input → process → output. The scale, speed, and complexity vary. The structure does not [1].

## 8. Best Practices

When you start thinking about any problem computationally, these habits help:

- **Name the input first.** Before thinking about how to solve something, be precise about what information you are starting with. Vague inputs produce vague processes.
- **Be specific about the process.** Vague steps ("do the clever bit") are not computation. Ask: could someone else follow these steps exactly, without asking you any questions? If the answer is no, the process needs more definition.
- **Check the output is answerable.** If the question you are asking has no single correct answer that a defined process could reach, computation alone cannot solve it — you may need human judgment, probability, or a different framing.
- **Do not confuse the computer with the computation.** Removing your laptop from the equation does not remove computation from the world. The concept is bigger than the machine.
- **Distinguish deterministic from probabilistic early.** Some problems have one correct answer for a given input (a sort, a currency conversion). Others have outputs that are necessarily probabilistic (a fraud risk score, a weather forecast). Knowing which type you are dealing with shapes how you design the process and how you communicate the output to users [1][2].

## 9. Hands-On Exercise

Try this before the next session (no computer required):

1. Pick two real-world tasks from your daily life — for example, making tea, or searching for a bus route.
2. For each task, write down: (a) what the input is, (b) the steps in the process, and (c) what the output is.
3. Check your steps: are they specific enough that a robot with no common sense could follow them? If not, rewrite them until they are.

Bring both examples to the lab session. You will use them when you draw flowcharts in Excalidraw.

## 10. Key Takeaways

- **Computation is input → process → output**: any system that takes information, applies defined steps, and produces a result is computing.
- **The steps must be precise**: vague instructions are not computation. Specific, unambiguous steps are the hallmark of a computable process.
- **Computers are not the only things that compute**: traffic lights, vending machines, and human cashiers all perform computation. The concept is bigger than the device.
- **Computable means solvable by a finite set of defined steps**: not every problem is computable, but the boundary keeps moving as technology advances.
- **AI is computation at scale**: the AI systems you already use every day are built on the same input → process → output structure you have just learned.

## 11. Next Steps

_System-derived from the next entry in curriculum/sequence.md._
