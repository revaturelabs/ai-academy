---
topic_id: "1.2"
title: "Deterministic systems — same input always gives the same output"
position_in_module: 2
generated_at: "2026-06-19T00:00:00Z"
resource_count: 3
---

# 1. Deterministic systems — same input always gives the same output — Topic Corpus

## 2. Prerequisites

This topic builds directly on **Topic 1.1 — What is computation**. You should be comfortable with the three-part model — input, process, output — and the idea that computation requires defined, unambiguous steps. Those concepts are used throughout this topic without being re-explained.

## 3. Learning Objectives

By the end of this topic, you will be able to:

- Define what a deterministic system is in plain, everyday terms.
- Explain why the phrase "same input always gives the same output" is the test for determinism.
- Give at least three real-world examples of deterministic systems and identify why each one qualifies.
- Distinguish a deterministic system from one where the output can vary — without needing to define the technical details of that variation.
- Explain why predictability and reproducibility matter in practical computing systems.

## 4. Introduction

Imagine pressing the "2 + 3" buttons on a calculator. The screen shows 5. You press the same buttons tomorrow. You get 5. You ask a friend to press the same buttons. They get 5.

That never-changing, always-the-same result is not an accident. It is the defining property of an enormous class of computing systems — and it has a name: **determinism**.

Now think about asking a modern AI chatbot the same question twice. You type "What is the capital of France?" and it says "Paris." But if you ask "Write me a short poem about autumn," you might get a different poem every time. Same input, different output. Something different is happening there.

This topic is about the first category: systems where the input completely determines the output, every single time, without exception. Understanding this property — and being able to spot it in real systems — is a foundation skill for the rest of this course [1].

## 5. Core Concepts

### 5.1 What "deterministic" means

**Deterministic system** — a system where every output is completely determined by its input. Give the system the exact same input, and it will always produce the exact same output, with no variation [1].

The word comes from the Latin *determinare*, meaning "to fix" or "to bound." A deterministic system is one whose outcome is *fixed* by the input — there is no room for surprise, randomness, or variation.

Here is the test you can apply to any system:

> If you gave this system the same input twice — or a thousand times — would it always return the same output?

If yes, the system is deterministic. If the output could vary even a little, it is not fully deterministic [1][2].

**Concrete examples before the formal definition:**

| System | Input | Output | Same every time? |
|---|---|---|---|
| Calculator: 17 × 6 | The numbers 17 and 6, the × operation | 102 | Yes [1] |
| Sort a list: [3, 1, 2] ascending | The list [3, 1, 2] | [1, 2, 3] | Yes [1] |
| Traffic light on a fixed timer | Time elapsed in current phase | Next colour to display | Yes [1] |
| Currency converter (fixed rate) | 100 USD, the exchange rate | The euro amount | Yes [2] |

In every row, knowing the input completely tells you the output. There is no uncertainty, no possibility of a different answer on a different day [1].

### 5.2 The two key properties: predictability and reproducibility

A deterministic system has two related but distinct properties worth naming separately.

**Predictability** — before you even run the system, you can work out what the output will be, as long as you know the input. If you know the rule "multiply the two inputs," you can predict the output for any pair of numbers without running the computation at all [2].

**Reproducibility** — if you run the same process on the same input on two different machines, in two different countries, or five years apart, you will get the same output. The result is reproducible across time, place, and hardware [1].

These two properties make deterministic systems extremely valuable in practice:

- A banking system that rounded currency conversions differently on Tuesday than on Wednesday would be unusable.
- A sorting algorithm that ordered the same list differently each time would produce unreliable results.
- A program that translated the same source code differently on two runs would make software impossible to test.

In every case, the guarantee of sameness is not just convenient — it is essential for the system to be trusted [1][2].

### 5.3 Why "same input" means *exactly* the same input

There is an important precision in the definition. When we say "same input," we mean *every part* of the input is identical — not just the obvious part.

Consider a navigation app calculating a route from point A to point B:

- If the input is just the two place names, a deterministic routing system always returns the same route.
- But if the input also includes the current time of day (to account for traffic), then the same destination pair at 8 a.m. and 2 p.m. are *different* inputs. The system may correctly return a different route — while still being deterministic, because the same full input (place names + time) always produces the same route [1].

A common mistake is to say "this system is not deterministic" when the input has changed in a way you did not notice. A system can be perfectly deterministic while producing different outputs in different circumstances — as long as the full input also changed [1][3].

**Rule of thumb:** if you see different outputs and are not sure why, check whether any part of the input is different before concluding the system is non-deterministic.

### 5.4 Determinism in programs and processes

In Topic 1.1, you saw that computation requires defined steps. Algorithms are covered in detail later in this module. For most classical computing processes, the sequence of steps and the final output are fully fixed for any given input [2][3].

Examples of deterministic processes in computing:

- **Arithmetic**: adding, subtracting, multiplying, or dividing two numbers always produces a fixed result for any given pair [1].
- **Sorting**: a well-specified sorting procedure applied to the same list always returns the same sorted list [1][3].
- **Searching**: a procedure that looks for a value in a list either finds it or does not — and the answer is the same every time the same list and value are used [3].
- Encryption is covered in later modules [2].

Determinism is not just a property of toy examples. It is a deliberate design choice in the vast majority of production computing systems — from database queries to file compression to network routing [1][2].

### 5.5 Naming the contrast: when output can vary

The opposite of a deterministic system is a non-deterministic system — covered in topic 1.3.

Knowing that contrast exists makes the concept of determinism clearer. Deterministic systems are the predictable, repeatable ones. They are not "better" or "worse" — they are the right tool when the answer must be the same every time, such as in arithmetic, sorting, or verifying whether a password meets rules [1][3].

### 5.6 Hidden inputs and why they matter

One of the most important practical skills related to determinism is recognising inputs that are not obviously visible. These are sometimes called **hidden inputs** — pieces of information that the process uses without the user explicitly providing them [1].

Common hidden inputs include:

- **The current date or time** — a payroll system that computes overtime might apply different rules depending on whether it is a weekday or a public holiday. The date is an input, even if the user never types it [1].
- **Stored configuration** — a currency converter that reads an exchange rate from a settings file is taking that rate as an input. If the rate changes between runs, the output changes — but the system is still deterministic; the input simply changed [2].
- **System state** — a process that reads from a counter or a log file incorporates the current value of that counter as part of its input. Two runs where the counter holds different values are runs with different inputs [1][3].

Understanding hidden inputs is what allows you to correctly classify a system. Many systems that appear non-deterministic at first glance turn out to be fully deterministic once every input is written down explicitly [1].

A useful exercise: take any system whose output you are trying to understand, and list every value it reads before producing its output — not just the values you typed in. That full list is the true input. Only after constructing it can you fairly ask whether the same input always gives the same output [2][3].

### 5.7 More deterministic systems — Input/Process/Output breakdowns

The Input → Process → Output model from Topic 1.1 is a direct tool for testing determinism. For any system, if you can fully specify the inputs and the process never introduces randomness, the output is determined. Here are additional examples with explicit breakdowns [1][2]:

**Password-strength checker**
- Input: a string of characters entered by the user
- Process: check length, check for uppercase letters, check for digits, check for special characters
- Output: "strong," "medium," or "weak"
- Same every time? Yes — the same string always receives the same rating [1]

**Post-code lookup**
- Input: a post code (e.g., "SW1A 1AA")
- Process: look up the post code in a fixed reference table
- Output: the corresponding address region
- Same every time? Yes — the same post code always maps to the same region in an unchanged table [2][3]

**Delivery cost calculator**
- Input: item weight in grams, delivery zone (a number from 1 to 5)
- Process: apply a fixed pricing table (e.g., zone 1 up to 500 g = £2.99)
- Output: the delivery price
- Same every time? Yes — the same weight and zone always produce the same price [1][2]

**Voting-age eligibility check**
- Input: date of birth, current date
- Process: calculate difference in years, compare to 18
- Output: "eligible" or "not eligible"
- Same every time? Yes — note that the current date is an explicit input here. Once both values are fixed, the output is fixed [3]

These examples share a common structure: all inputs are known and fixed, the process follows defined rules without randomness, and therefore the output is always the same. That structure is the signature of a deterministic system [1][2].

## 6. Implementation

No code is required for this topic. The concept of determinism is about the *property* of a process, not a particular programming technique.

To check whether any system or procedure is deterministic, apply this three-step test:

1. **Identify all the inputs.** Write down everything the system takes in — including any hidden inputs such as the current time, a stored setting, or a flag. Missing an input is the most common cause of misclassifying a system.
2. **Run the process (mentally or on paper) twice with exactly the same input.** This can be a thought experiment — you do not need a computer. Ask: are the outputs identical?
3. **Ask: is there any way the output could differ?** If you can think of a scenario where the same full input produces a different output — a random element, a hidden setting, a changing environment — the system has a non-deterministic component.

If step 2 always gives the same output and step 3 finds no scenario where it could differ, the system is deterministic [1][2].

**Example — applying the test to a vending machine (revisiting Topic 1.1):**

From Topic 1.1, a vending machine takes coins and a button press, checks stock and price, then either dispenses the item or returns the coins.

1. Full inputs: coin value inserted, button pressed, stock level of the selected item, price stored in the machine.
2. Run with: coin value = £1.20, button = B3, B3 price = £1.10, B3 in stock. Result: item dispensed, £0.10 returned. Run again with the same full input. Same result.
3. Could it differ? Only if one of the inputs changes — for example, if B3 goes out of stock. But that is a change in input, not randomness. With every input constant, the output is the same every time.

Conclusion: the vending machine is a deterministic system [1].

## 7. Real-World Patterns

Deterministic systems are the backbone of computing infrastructure. Here are three areas where you will encounter them — and where the deterministic property is the key design requirement.

### Arithmetic and financial calculations

Every time an amount is calculated — a purchase total, a tax deduction, a salary payment — the system performing the calculation is deterministic. The same salary figure, tax rate, and deduction list must always produce the same net pay. Any variation would be a system error, and in payroll systems, errors have legal consequences [1][2].

Determinism is built into standard arithmetic rules. 17.5% of £1,200 is £210, today, tomorrow, and a decade from now — regardless of what machine performs the calculation [1].

### Sorting and searching in databases

Every time you look up a record in a database — a customer account, a medical record, a product entry — a search process runs. Every time results come back in alphabetical or date order, a sorting process runs. Both are deterministic: given the same data and the same query, the same records are returned in the same order, every time [1][3].

This reproducibility is what makes databases reliable enough to use in hospitals, banks, and government systems. If a search for "patient ID 4872" returned different records on different queries, the system would be dangerous [1].

### Build tools and code execution

Build tools that translate code into a runnable program must produce the same result every time they process the same code — any non-deterministic build step would make software unreliable [1]. This is essential: if the output varied, developers could never reliably reproduce a bug, test a fix, or verify that a deployed program is exactly the one they tested [2][3].

### Where determinism is a specification requirement

In several fields, determinism is not just convenient — it is required:

- **Aviation and medical devices**: flight control software and medical device firmware must be deterministic by regulation. The same sensor reading must always produce the same control response, without exception [1].
- Cryptographic systems (covered in later modules) depend on determinism to function correctly [2].
- **Version control**: tools that track changes to files use deterministic hashing (covered in later modules) to detect whether anything has changed [1][3].

In all of these cases, the deterministic property is what allows the system to be trusted, audited, and certified [1][2].

## 8. Best Practices

When thinking about any computing system — whether you are building one, using one, or evaluating one — these habits will serve you well.

- **Check for hidden inputs.** The most common mistake when reasoning about determinism is missing an input. Time of day, a stored configuration value, a user setting — these are all inputs, even if they are not typed in by hand. A system that looks non-deterministic often turns out to be deterministic once every input is accounted for.

- **Separate "produces different outputs" from "non-deterministic."** Different outputs do not automatically mean non-deterministic. A tax calculator produces different outputs for different income figures — that is expected, and the system is entirely deterministic. The question is always whether the same *full* input yields the same output.

- **Value determinism where correctness matters.** For any problem where the answer must be exactly right — currency conversion, medical dosage calculation, legal record lookup — confirm that the system is deterministic. Variation in those contexts is a defect, not a feature [1][2].

- **Use reproducibility as a debugging tool.** If a system is supposed to be deterministic but gives inconsistent results, that inconsistency signals a problem: a hidden input is changing, a component is behaving unexpectedly, or a design error exists. Inconsistency in a nominally deterministic system is always a bug [1].

- **Know when determinism is not the goal.** Some problems are better served by systems that can vary their output. Recognising which category a problem falls into is a key skill — topic 1.3 covers this.

## 9. Hands-On Exercise

This exercise connects the flowchart activity from the lab session to the determinism concept.

1. Choose two everyday tasks — for example, making a cup of tea, and calculating the cost of items in a shopping basket.
2. Draw a simple flowchart for each task on paper or in Excalidraw. Show each step as a box, with arrows connecting them in order. Where a decision is made (for example, "Is the kettle full?"), draw a diamond shape with two arrows labelled Yes and No.
3. For each flowchart, ask: if someone followed these steps from exactly the same starting conditions every time, would they always reach the same result? If yes, you have drawn a deterministic process.
4. Swap your flowcharts with a partner. Can they follow the steps exactly, without asking any clarifying questions? If they get stuck because a step is ambiguous, that step needs to be made more precise. Precision is a prerequisite for determinism.

The goal is to see that drawing a process precisely enough for someone else to follow without interpretation is the same challenge as making a process deterministic.

## 10. Key Takeaways

- **A deterministic system always produces the same output for the same input.** This is a guarantee built into the structure of the system, not a guess or an approximation [1].
- **Predictability and reproducibility** are the two practical benefits: you can reason about the output before running the system, and you can re-run it to verify a result [1][2].
- **"Same input" means every part of the input is identical**, including any hidden inputs such as settings or timestamps. Different outputs do not always mean non-deterministic — first check whether the input also changed [1][3].
- **Most classical computing systems are deterministic by design**: arithmetic, sorting, searching, and encrypting all rely on this property for correctness and trust [1][2][3].
- **Non-deterministic systems exist** and will be covered in topic 1.3. Knowing what determinism is makes that contrast clearer.

## 11. Next Steps

_System-derived from the next entry in curriculum/sequence.md._
