<!-- GENERATED FILE — DO NOT EDIT BY HAND.
     Cresent view of 8.3 — What Is Computation.
     Source of truth: CIT 1.1, CIT 1.2, CIT 1.3.
     Regenerate: python Cresent/Technical/tools/generate_shared_readings.py -->
<!-- nav:top:start -->
Previous: —&emsp;·&emsp;[⬆ Table of Contents](../../../../../../README.md#part-b)&emsp;·&emsp;[8.4 — Why AI Gives Different Answers ➡](../8-4-why-ai-gives-different-answers/reading.md)
<!-- nav:top:end -->

---

# What is computation

## Overview

Computation is any process that takes information in, applies a defined set of steps to it, and produces a result. You encounter computation dozens of times a day — when a GPS picks a route, when a traffic light changes phase, when a vending machine checks your coins. Understanding what computation actually is gives you the foundation for everything else in this course: how computers make decisions, how AI systems work, and how to think through problems before writing a single line of code.

## Key Concepts

### 1. The three parts of every computation

Every computation — no matter how simple or complex — has the same three-part structure [1]:

1. **Input** — the raw information going in. Example: the numbers you type into a calculator.
2. **Process** — the defined steps applied to that information. Example: the addition or multiplication rules.
3. **Output** — the result that comes out. Example: the answer shown on the display.

This is called the **Input / Process / Output** model — or **I/P/O** for short. It applies to a pocket calculator, a weather forecast system, and every AI tool you have ever used.

![The input → process → output structure, shown in two everyday examples.](../../../../../../../../CIT/content-gen-example/content/m1-computational-thinking/week-1/1-understanding-computation/1-1-what-is-computation/artifacts/diagram.png)
*The input → process → output structure, shown in two everyday examples.*

Why does the I/P/O model matter? Because it breaks the assumption that computation only happens inside computers. Once you can identify the three parts, you can recognise computation anywhere — in a thermostat, in a cashier counting change, in a music box. It also gives you the first design questions for any solution: what is the input? What steps transform it? What output do I need? [1]

### 2. "Defined steps" — why precision matters

The word *defined* is doing important work. Computation requires that the steps are **specific and unambiguous** — precise instructions that leave no room for guessing [1].

Think about a recipe:

- **Vague:** "Add a pinch of salt." Two cooks add different amounts — this is not computable.
- **Defined:** "Add exactly 2 grams of salt." Every cook adds the same amount — this is computable.

When the steps are precise enough that anyone (or any machine) could follow them and get the same result, you have a computational process. Ambiguous steps break this: two runs on the same input produce different outputs, making the process unreliable and unverifiable [1].

### 3. What makes a task "computable"

**Computable** means: there exists a finite set of defined steps that always produces the correct result in a finite amount of time [1].

| Task | Computable? | Why |
|---|---|---|
| Add two numbers | Yes | Clear steps, always finishes [1] |
| Sort a list of names alphabetically | Yes | Clear steps, always finishes [1] |
| Find the shortest route between two cities | Yes | Steps exist; always finishes [1] |
| Decide whether a poem is "beautiful" | Not fully | No precise, agreed-upon steps exist |
| Predict exact weather in 10 years | Not fully | Steps exist but result is approximate |

The boundary shifts over time. Tasks once considered impossible for machines — recognising speech, identifying objects in photos — are now solved by modern AI (Artificial Intelligence) systems [2][3]. You will explore that shift in later topics.

### 4. Computers are not the only things that compute

Anything that takes an input, applies defined steps, and produces an output is computing — no silicon chip required [1].

**Traffic light on a timer**
- Input: time elapsed since the last phase change
- Process: if time ≥ green_duration, switch to amber; then red; then back to green
- Output: the light signal shown to drivers

**Vending machine**
- Input: coins inserted, button pressed
- Process: check whether inserted value ≥ item price AND item is in stock; if yes, dispense item and return change; if no, return coins
- Output: dispensed item + change, or all coins returned

**Human cashier**
- Input: purchase price and amount handed over
- Process: subtract price from payment; decompose the difference into fewest notes and coins available
- Output: the correct change handed back

The same I/P/O structure runs in every case. Recognising computation in the world around you — not just on screens — is the first step in **computational thinking**: approaching a problem by breaking it into steps, spotting patterns, and expressing a solution precisely [1].

### 5. AI is computation too

Modern AI systems — chat tools, recommendation engines, image recognisers — are also performing computation. They take inputs (your words, an image, your click history), apply sequences of defined steps, and produce outputs (a reply, a label, a recommendation) [2][3].

What makes AI distinctive is how the steps were determined — a process you will explore in a later module. The key point for now: AI is built on the same I/P/O foundation you have just learned. Whether a system is deterministic or probabilistic is covered in topics 1.2 and 1.3 — for now, the core structure is identical [1][2].

## Worked Example

Here is a single computation traced step by step: a bank card transaction check.

Every time you tap your card at a shop, a computation runs in the background — typically finishing in under 200 milliseconds [2][3].

**Step 1 — Input is gathered**

The system collects: merchant category, transaction amount, geographic location, time of day, and your recent transaction history.

**Step 2 — Process runs**

Each piece of input is checked against a set of rules:
- Is the amount more than 5× your 30-day average? → suspicion flag raised.
- Are there two transactions in different countries within 1 hour? → high-risk flag raised.
- Does the merchant category match your usual spending? → soft flag raised or cleared.

All flags are combined into a single **risk score**.

**Step 3 — Output is produced**

- Score below threshold → transaction approved.
- Score above threshold → transaction declined and an SMS alert sent to you.
- Score in the middle band → transaction routed to a human analyst for review.

Notice the structure: a defined input, a set of precise and unambiguous steps, a clear output. This is computation — and it runs billions of times a day across the global payments network [2][3].

## In Practice

Computation shows up in every industry. Three short examples:

- **Manufacturing:** a camera above a bottling line captures each bottle (input), checks fill level, cap position, and label alignment against tolerances (process), and sends a pass or fail signal to a sorting arm (output) [3].
- **Healthcare:** a radiology AI takes a scan and patient history (input), evaluates structural features against baseline profiles (process), and produces a ranked list of candidate conditions with probability scores for a clinician to review (output) [2][3].
- **Finance:** as shown in the Worked Example above — the fraud-detection system runs the same I/P/O structure for every card transaction globally [2][3].

**Habits that help when you start thinking computationally:**

- **Name the input first.** Be precise about what information you are starting with. Vague inputs lead to vague processes.
- **Make every step followable.** Ask: could someone else follow these steps exactly, without asking any questions? If not, the process needs more definition.
- **Check the output is answerable.** If the question has no single correct answer a defined process could reach, computation alone cannot solve it — you may need human judgment or a probability-based approach.
- **Do not confuse the computer with the computation.** Remove the laptop; computation stays. The concept is bigger than the machine [1].

## Key Takeaways

- **Computation is Input → Process → Output:** any system that takes information, applies defined steps, and produces a result is computing.
- **Defined means unambiguous:** vague instructions are not computation. Steps must be precise enough for anyone — or any machine — to follow without guessing.
- **Computers are not the only things that compute:** traffic lights, vending machines, and human cashiers all perform computation.
- **Computable means solvable by a finite set of defined steps:** not every problem is computable, but the boundary keeps moving as technology advances.
- **AI is computation:** the AI systems you already use are built on the same I/P/O structure introduced here — you will explore how they differ from simpler systems in topics 1.2 and 1.3.

## References

1. The Learn Notes, "Deterministic and Probabilistic Systems — What's the Deal?" <https://thelearnnotes.com/blog/deterministic-and-probabilistic-systems-what-s-the-deal->
2. Alphanome AI, "Probabilistic vs Deterministic Models in AI/ML: A Detailed Explanation." <https://www.alphanome.ai/post/probabilistic-vs-deterministic-models-in-ai-ml-a-detailed-explanation>
3. Gaine, "Probabilistic and Deterministic Results in AI Systems." <https://www.gaine.com/blog/probabilistic-and-deterministic-results-in-ai-systems>

---

# Deterministic systems — same input always gives the same output

## Overview

In topic 1.1 you learned that computation means taking an input, running a defined process on it, and producing an output. This topic focuses on a specific and extremely common property of computing systems: when the same input always produces the same output, without variation. That property is called **determinism**, and it is the foundation for why calculators, databases, and payroll systems can be trusted to give correct, consistent results every time they run [1].

## Key Concepts

### What "deterministic" means

A **deterministic system** is one whose output is completely fixed by its input. Give the system the same input twice — or a thousand times — and you will always get the same output back, with no variation and no surprises [1].

Here is the test you can apply to any system:

> If you gave this system the exact same input twice, would it always return the exact same output?

If yes, the system is deterministic. If the output could vary even slightly, the system is not fully deterministic [1][2].

The table below shows four systems and confirms why each one passes the test:

| System | Input | Output | Same every time? |
|---|---|---|---|
| Calculator: 17 × 6 | The numbers 17 and 6, the × operation | 102 | Yes [1] |
| Sort a list: [3, 1, 2] ascending | The list [3, 1, 2] | [1, 2, 3] | Yes [1] |
| Traffic light on a fixed timer | Time elapsed in current phase | Next colour to display | Yes [1] |
| Currency converter (fixed rate) | 100 USD, the exchange rate | The euro amount | Yes [2] |

In every case, knowing the input completely tells you the output. There is no uncertainty, no possibility of a different answer on a different day [1].

### Predictability and reproducibility

A deterministic system has two related but distinct benefits worth knowing by name.

- **Predictability** — before you run the system at all, you can work out what the output will be, as long as you know the input. If the rule is "multiply the two numbers," you can predict the answer for any pair without touching the computer [2].
- **Reproducibility** — if you run the same process on the same input on two different machines, in different countries, or five years apart, you get the same output. The result does not change with time, place, or hardware [1].

These two properties make deterministic systems trustworthy in real work:

- A banking system that rounded currency conversions differently on Tuesday than on Wednesday would be unusable.
- A sorting step that ordered the same list differently on each run would produce unreliable results.
- A program that produced different output from the same source code on two consecutive runs would make software impossible to test.

In every case, the guarantee of sameness is not just convenient — it is essential for the system to be trusted [1][2].

### Why "same input" means every part of the input

There is an important precision in the definition. "Same input" means *every part* of the input is identical — not just the obvious part you typed in.

Consider a navigation app calculating a route from point A to point B:

- If the input is only the two place names, the system always returns the same route.
- But if the input also includes the current time of day (to adjust for traffic), then the same destination pair at 8 a.m. and 2 p.m. are *different inputs*. Getting a different route is correct — the system is still deterministic, because the same full input (place names + time) always produces the same route [1].

A common mistake is to call a system non-deterministic when an input changed in a way you did not notice. The rule of thumb: if you see different outputs and are not sure why, **check whether any part of the input changed before concluding the system behaves randomly** [1][3].

This leads to the idea of **hidden inputs** — values that the process uses but that the user never types in directly. Common examples include:

- The current date or time (used by payroll rules, eligibility checks)
- A stored configuration value such as an exchange rate read from a settings file
- A system counter or log file that increments between runs [1][2][3]

Understanding hidden inputs is what allows you to correctly classify a system. Many systems that seem to behave unpredictably turn out to be fully deterministic once every input is written down explicitly [1].

### The diagram below shows the core idea

![The same input run twice through a deterministic system always produces the same output.](../../../../../../../../CIT/content-gen-example/content/m1-computational-thinking/week-1/1-understanding-computation/1-2-deterministic-systems-same-input-always-gives-the-same-outpu/artifacts/diagram.png)
*The same input run twice through a deterministic system always produces the same output.*

### The contrast: when output can vary

Non-deterministic is a bare name for the contrasting case — covered in topic 1.3. Knowing the contrast exists makes determinism clearer. Deterministic systems are the predictable, repeatable ones. They are not "better" or "worse" than other kinds — they are the right tool when the answer must be the same every single time, such as in arithmetic, sorting, or checking whether a password meets length rules [1][3].

## Worked Example

Apply the three-step determinism test to a vending machine — a system introduced in topic 1.1.

**Step 1 — Identify all the inputs, including hidden ones.**

- Coin value inserted
- Button pressed (e.g., B3)
- Price stored for B3
- Stock level of B3

**Step 2 — Run the process twice with exactly the same input (as a thought experiment).**

- Run 1: coin = £1.20, button = B3, price = £1.10, B3 in stock → item dispensed, £0.10 returned.
- Run 2: same values → same result: item dispensed, £0.10 returned.

**Step 3 — Ask: is there any way the output could differ?**

Only if an input changes. If B3 goes out of stock between runs, that is a change in the stock-level input — not random behaviour. With every input held constant, the output is always the same.

**Conclusion:** the vending machine is a deterministic system [1].

Notice that step 1 is the hardest part in practice. Getting a different output than expected is almost always a sign that step 1 was incomplete — a hidden input changed without you noticing.

## In Practice

Deterministic systems appear wherever the answer must be exactly right, every time. Here are the most common areas you will encounter them:

- **Financial calculations.** Every payroll run, purchase total, and tax deduction is deterministic. The same salary figure, tax rate, and deduction list must always produce the same net pay. Any variation is a legal error [1][2].
- **Database searches and sorting.** When you look up a record — a customer account, a medical file — a search runs. When results come back in alphabetical or date order, a sort runs. Both are deterministic: same query, same data, same result, every time. This reproducibility is what makes databases safe to use in hospitals and banks [1][3].
- **Build tools.** Software that translates source code into a runnable program must produce the same output every time it processes the same code. Without that guarantee, developers could never reliably reproduce a bug or verify a fix [1][2].

**Three habits for reasoning about determinism:**

1. **Check for hidden inputs first.** Before calling a system non-deterministic, list everything it reads — timestamps, config files, counters. A system that looks unpredictable often becomes predictable once every input is on the list [1].
2. **Separate "different outputs" from "non-deterministic."** A tax calculator produces different outputs for different income figures. That is correct and expected — it is still deterministic. The question is always whether the *same full input* yields the same output [2][3].
3. **Treat inconsistency as a bug signal.** If a system is supposed to be deterministic but gives inconsistent results, something is wrong: a hidden input is changing, or there is a design error. Inconsistency in a deterministic system is always a defect, not normal behaviour [1].

## Key Takeaways

- **A deterministic system always produces the same output for the same input.** This is a structural guarantee, not a guess or an approximation [1].
- **Predictability and reproducibility** are the two practical benefits: you can reason about the output before running, and re-run the process to verify a result [1][2].
- **"Same input" means every part of the input is identical**, including hidden inputs such as timestamps, stored settings, and system state. Different outputs do not automatically mean non-deterministic — always check whether the input also changed [1][3].
- **Hidden inputs are the most common source of confusion.** List everything the system reads before concluding it behaves randomly [1].
- **Non-deterministic systems exist and serve different purposes** — covered in topic 1.3. Knowing determinism clearly is the foundation for understanding that contrast.

## References

1. Wikipedia, "Deterministic system." <https://en.wikipedia.org/wiki/Deterministic_system>
2. Computer Science Wiki, "Determinism." <https://computersciencewiki.org/index.php/Determinism>
3. GeeksforGeeks, "Difference between Deterministic and Non-Deterministic Algorithms." <https://www.geeksforgeeks.org/dsa/difference-between-deterministic-and-non-deterministic-algorithms/>

---

# Probabilistic systems — same input can give different outputs

## Overview

In topic 1.2 you learned that deterministic systems always produce the same output for the same input. Not every system works that way. Some systems are designed so that the same input can produce a different output each time — and that variation is not a mistake. It is the point. This topic introduces that category: **probabilistic systems**, and explains why they exist, how they work, and where you encounter them every day [1].

## Key Concepts

### What a probabilistic system is

A **probabilistic system** is one where the output is not fully fixed by the input. Even with exactly the same input, the system can produce different outputs on different runs [1].

The word "probabilistic" comes from **probability** — the study of how likely different outcomes are, measured on a scale from 0 (impossible) to 1 (certain). A probabilistic system does not pick its output at random with no logic. Instead, it works with a range of possible outputs, each with a different likelihood, and selects one. Which one is selected can vary each time [1][2].

Here is the key distinction stated plainly:

> In a **deterministic** system, the input fixes the output — there is one answer and only one.
> In a **probabilistic** system, the input shapes the *range of possible answers* — there is a spread of answers, each more or less likely, and which one is produced can differ.

The input still matters — it narrows down which outputs are plausible. But it does not lock the output to a single value.

The table below contrasts four systems so you can see the pattern:

| System | Input | Possible outputs | Same every time? |
|---|---|---|---|
| AI story generator | "Write a short story about the sea" | Thousands of different valid stories | No — varies each run [1] |
| Weather forecast model | Today's temperature and pressure | "60% chance of rain," "70%," etc. | No — depends on how the model samples [2] |
| Spam filter (borderline email) | A message near the boundary | "Spam" or "Not spam" — close calls vary | No — probability close to 50% [3] |
| Dice roll | Roll a fair six-sided die | 1, 2, 3, 4, 5, or 6 | No — uniformly random [1] |

In every row, the input has not disappeared — it still shapes what outputs are plausible. But it does not fix a single answer.

### Probability and uncertainty — the two ideas underneath

Two concepts power every probabilistic system.

**Probability** is a way of expressing how likely something is. A probability of 0.7 means the event happens roughly 70% of the time across many trials. Different possible outputs have different probabilities, so some outputs show up far more often than others [1].

**Uncertainty** is the reason probabilistic systems exist. Some problems do not have one correct answer waiting to be found. The world is genuinely ambiguous — the same symptoms can point to different illnesses, the same weather data can lead to different forecasts, the same writing prompt can inspire thousands of valid stories. A probabilistic system is designed to work honestly inside that uncertainty rather than pretending a single fixed answer exists [2][3].

Together: a probabilistic system accepts that uncertainty is real, uses probability to represent how likely different answers are, and produces outputs that reflect that range — rather than forcing a false certainty.

### Randomness as a tool, not chaos

In everyday speech, "random" suggests chaos or arbitrariness. In computing, **randomness** is a design tool — something deliberately introduced to make the system behave usefully [1][2].

Randomness means the system uses a source of unpredictability when choosing among possible outputs. The choice varies from run to run even when the input is the same — because an unpredictable element is built into the process on purpose.

Examples of deliberate randomness:

- **Shuffling a playlist.** A music app that shuffles songs uses randomness intentionally. The same playlist, shuffled twice, gives different orders — and that variability is the feature, not a flaw [1].
- **Generating a security token.** A system that creates a one-time code uses randomness so the code is unpredictable to an attacker [2].
- **Recommender systems.** When a video platform suggests videos, some randomness is injected so that users with similar viewing histories do not all see the same list [3].

In each case, randomness is not a flaw — it is an intentional part of the design.

### The diagram below shows how the two system types compare

![Probabilistic vs deterministic system flow — same input, different possible outputs](../../../../../../../../CIT/content-gen-example/content/m1-computational-thinking/week-1/1-understanding-computation/1-3-probabilistic-systems-same-input-can-give-different-outputs/artifacts/diagram.png)
*The same input run through a deterministic system always produces one fixed output; run through a probabilistic system it can produce any of several possible outputs, each with a different likelihood.*

### Sampling — how the system picks one answer

A key step inside every probabilistic system is called **sampling** — picking one answer from a range of possible answers.

Think of it this way: imagine a bag containing ten cards. Seven are labelled "Option A," two are labelled "Option B," and one is labelled "Option C." The input to this system is "draw a card." The process is to reach in without looking and pull one out.

- Run it once: you get "Option A."
- Run it again with the same input: you might get "Option A," "Option B," or "Option C."
- The input is identical both times. The output can vary.
- But "Option A" appears far more often than "Option C" — the range is shaped by what is in the bag.

In an AI language model, the "bag" holds a range of possible next words, each with a likelihood attached. The sampling step is the act of drawing one. The input determines which words are in the bag and how many of each kind there are — but it does not fix which word is drawn [1][2].

### Output variation — what changes and what stays stable

**Output variation** is the name for this core property: the same input can yield different specific results across runs, even though the shape and distribution of those results stays stable [1].

Consider asking an AI assistant to complete "The cat sat on the ___":

- "mat" — very likely (appears perhaps 60% of the time)
- "chair" — somewhat likely (about 25%)
- "roof" — less likely (about 10%)
- "quantum accelerator" — extremely unlikely (under 1%)

The input sentence strongly shapes which completions are probable. But "mat" is not guaranteed on any single run. This is why probabilistic systems are not simply random noise — they are constrained by the input; they just cannot be pinned to a single fixed answer.

What you *can* predict about a probabilistic system:

- Which outputs are possible — the input constrains the space.
- Which outputs are most likely — some answers are far more probable than others.
- Long-run behaviour — over many runs with the same input, you can observe roughly how often each category of answer appears.

What you *cannot* predict: the exact output of any single run. That is what makes the system probabilistic.

### Temperature — a designed control on randomness

AI systems like language models are probabilistic. One concept that belongs here is the **temperature** setting: a control that tells the system how much variation to allow when sampling [1][2].

- A **lower temperature** makes the system more predictable — it tends to choose the most likely output almost every time.
- A **higher temperature** makes the system more varied — it samples more freely across a wider range of possible outputs, producing more surprising or creative results.

Temperature is a concrete example of a design choice that directly controls the defining property of a probabilistic system: how much the output can vary from run to run. You do not need to know the internal mechanics — just think of it as a "dial" that turns the level of variation up or down.

### When probabilistic is the right tool

Deterministic systems are essential when you need the answer to be exactly the same every time. But some problems genuinely call for a probabilistic approach [1][2][3].

| Situation | Why probabilistic fits |
|---|---|
| Creative generation (writing, images, music) | You want varied, valid outputs — a deterministic system would produce the same story every time [1] |
| Incomplete information (e.g. medical diagnosis) | The same symptoms can indicate different conditions; a ranked list of likelihoods is more honest and useful than a false-certainty single answer [2] |
| Modelling real-world uncertainty (weather) | Probabilistic forecasting gives a percentage likelihood — more truthful than pretending the future is known [2][3] |
| Personalisation at scale (recommendations) | Controlled randomness prevents every similar user from seeing the same list and lets the system learn from less-obvious choices [3] |

Situations where deterministic is still required:

- The correct answer is uniquely defined — arithmetic, sorting, database lookup.
- The same input must give the same output for legal, audit, or safety reasons.
- Reproducibility is essential — for testing, debugging, or regulatory compliance.

Neither type is universally superior. The right choice depends on what the problem requires [1][2].

## Worked Example

No code is needed here. A thought experiment makes the concept concrete.

**Goal:** Apply the three-step determinism test from topic 1.2 to decide whether an AI writing assistant is probabilistic or deterministic.

**Step 1 — Identify all inputs, including hidden ones.**

- Your prompt: "Give me an idea for a short story."
- The model's internal settings (including temperature).
- A random seed used at sampling time.

**Step 2 — Run the process twice with the same prompt.**

- Run 1: the assistant returns a story about a lighthouse keeper.
- Run 2, same prompt: the assistant returns a story about a lost robot.

**Step 3 — Ask: is there any way the output could differ?**

Yes — and the reason is *not* a hidden input that changed without you noticing. The process itself includes a designed source of variation: the sampling step draws from a range of plausible outputs using randomness. The same prompt leads to the same *range* of plausible stories but does not fix which one is drawn.

**Conclusion:** the AI writing assistant is a probabilistic system. Variation here is not a bug — it is the feature [1][2].

Notice how this test distinguishes probabilistic from deterministic with a hidden input. In topic 1.2, if you saw different outputs you were told to check whether an input had quietly changed. Here, even with every input held the same, the output can differ — because the process itself includes deliberate randomness. That distinction is the signal.

## In Practice

Probabilistic systems appear in many tools you already use or will use soon.

- **AI content generation.** Every time you use a modern AI writing assistant, a probabilistic system is at work. The same prompt can produce different essays, summaries, or code snippets on different runs — because a single "correct" response does not exist for open-ended creative tasks [1][2].
- **Spam and fraud detection.** Email providers estimate a spam likelihood for every incoming message. Messages near the boundary between spam and legitimate may be handled differently depending on exactly where that score falls [3].
- **Medical diagnosis support.** Software that assists doctors returns a ranked list of likely conditions, not a single definitive answer. The same set of symptoms re-entered might yield a slightly different ranking, reflecting genuine medical ambiguity [2][3].
- **Weather forecasting.** Running the same model many times and combining results gives a range of possible futures — far more useful for planning than a single deterministic projection that pretends to know the future exactly [2].

**Three habits for working with probabilistic systems:**

1. **Do not assume variation means error.** If a system produces different outputs for the same input, check whether it is designed to be probabilistic before concluding something is broken [1].
2. **Match the tool to the problem.** Use deterministic systems when the correct answer is unique and must be reproducible. Use probabilistic systems when the problem involves genuine uncertainty, creativity, or ambiguity [1][2].
3. **Treat probabilistic outputs as inputs to judgement.** High-stakes decisions — medical, legal, financial — should treat probabilistic outputs as one source of information, not as final verdicts [2][3].

## Key Takeaways

- **A probabilistic system can produce different outputs from the same input.** This is a designed feature, not a malfunction — the system intentionally includes a source of randomness or uncertainty [1].
- **The input still shapes what outputs are possible and likely** — some outputs are far more probable than others. Probabilistic is not the same as arbitrary [1][2].
- **Sampling is the step where the system picks one answer from a range of plausible answers.** The same input leads to the same range but does not fix which item from that range is selected [1][2].
- **Randomness and uncertainty are design tools.** When a problem involves creativity, ambiguity, or incomplete information, a probabilistic system is often more honest and more useful than a deterministic one [2][3].
- **The contrast with deterministic systems is the key mental model.** Both types take input and produce output; the difference is whether the same input always locks in the same output (deterministic) or leaves room for output variation (probabilistic) [1].

## References

1. Milvus AI Quick Reference, "How does probabilistic reasoning differ from deterministic reasoning." <https://milvus.io/ai-quick-reference/how-does-probabilistic-reasoning-differ-from-deterministic-reasoning>
2. Alphanome AI, "Probabilistic vs Deterministic Models in AI/ML — A Detailed Explanation." <https://www.alphanome.ai/post/probabilistic-vs-deterministic-models-in-ai-ml-a-detailed-explanation>
3. Gaine, "Probabilistic and Deterministic Results in AI Systems." <https://www.gaine.com/blog/probabilistic-and-deterministic-results-in-ai-systems>

---
<!-- nav:bottom:start -->
Previous: —&emsp;·&emsp;[⬆ Table of Contents](../../../../../../README.md#part-b)&emsp;·&emsp;[8.4 — Why AI Gives Different Answers ➡](../8-4-why-ai-gives-different-answers/reading.md)
<!-- nav:bottom:end -->
