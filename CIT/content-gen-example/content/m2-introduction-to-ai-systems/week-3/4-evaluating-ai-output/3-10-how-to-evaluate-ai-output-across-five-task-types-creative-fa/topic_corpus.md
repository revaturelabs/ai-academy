---
topic_id: "3.10"
title: "How to evaluate AI output across five task types — creative, factual, logical, ethical, coding"
position_in_module: 1
generated_at: "2026-06-17T00:00:00Z"
resource_count: 3
---

# 1. How to Evaluate AI Output Across Five Task Types — Topic Corpus

## 2. Prerequisites

This topic builds on concepts introduced in earlier week-3 topics:

- **3.2** — Large Language Models, hallucination, prompting, context window
- **3.6** — Temperature and stochastic output (why the same prompt can produce different results)
- **3.8** — Jagged frontier, benchmarks, capability cliffs, calibration
- **3.9** — Factual hallucination, attributional hallucination, faithful-but-wrong hallucination, overconfidence bias, grounding, provenance

No prior programming experience is required.

---

## 3. Learning Objectives

By the end of this topic, you will be able to:

1. Name the five AI output task types and explain why each one needs its own evaluation criteria.
2. Apply at least three evaluation criteria to creative AI output without incorrectly using factual accuracy as the standard.
3. Apply at least three evaluation criteria to factual AI output, including checking citations for hallucination.
4. Apply at least three evaluation criteria to logical AI output by tracing each reasoning step.
5. Apply the five-step general evaluation workflow to a real AI output and document the result in a structured format.

---

## 4. Introduction

Imagine you ask an AI system to do three different things in a row: write a short poem about autumn, explain the causes of World War I, and fix a bug in a few lines of code. You get three responses. How do you know whether any of them is good?

The honest answer is: it depends on what kind of task it was. Judging the poem by whether every line is a verified historical fact would be absurd. Judging the bug fix by whether it sounds poetic would be equally wrong. Yet this kind of mismatch is easy to make — especially when AI output tends to arrive in the same fluent, confident style regardless of whether it is accurate, coherent, or appropriate [1].

The deeper problem is that fluency is not quality. An AI can generate a polished, grammatically perfect paragraph that is entirely wrong, biased, or logically broken [1]. "Sounds right" is not a verification method.

This is why evaluation frameworks break AI tasks into **types** and assign each type its own **rubric** — a structured checklist of criteria you apply when assessing a piece of work. Different task types call for genuinely different criteria, and applying the right criteria is the first skill of responsible AI use [2].

In this topic you will learn five distinct task types, a concrete rubric for each, and a five-step general evaluation workflow you can use on any AI output. These tools will serve you directly when completing your Assessment A1 Specification Portfolio, which is due this week.

---

## 5. Core Concepts

### 5.1 What "evaluation" means in this context

**Evaluation** here means a human examining an AI output and making a structured judgment about its quality, correctness, and appropriateness for the task that was given. This is human evaluation — not automated machine-learning metrics such as BLEU or ROUGE scores, which measure text similarity numerically and are a separate, more technical topic. The evaluator in this topic is you [3].

Good evaluation is systematic. Without a structure, people tend to judge AI output by gut feel, which usually reduces to "does it sound convincing?" — an unreliable standard when dealing with a system that can hallucinate with full confidence (as you learned in topic 3.9). A structured **rubric** replaces gut feel with explicit, repeatable criteria [2].

A rubric assigns specific dimensions to evaluate, usually with a scale (for example: Pass / Partial / Fail, or 1 to 4). Rather than asking "is this good overall?", a rubric asks "does this pass criterion A? Does it pass criterion B?" Each criterion is rated separately. This prevents one strong dimension from hiding a serious weakness in another [2].

### 5.2 Why different task types need different criteria

All five task types involve an AI producing text (or code), so it is tempting to apply one universal measure. The problem is that "quality" has a different meaning depending on what the output is supposed to accomplish [1]:

- For a **creative** output, factual accuracy is the wrong bar — fiction and poetry are not expected to be factually true.
- For a **factual** output, novelty and originality are the wrong bar — you want reliability, not surprise.
- For a **logical** output, a confident, smooth tone is the wrong bar — an argument can sound polished and contain a hidden logical gap.
- For an **ethical** output, personal agreement is the wrong bar — your own values may not represent the full range of perspectives that matter.
- For a **coding** output, the only bar that counts at the floor level is whether the code actually runs and does what was asked — something a poem can never be judged by.

Mismatching rubric to task type produces two kinds of error: false confidence ("this factual report sounds creative and engaging — it must be good!") and false failure ("this poem doesn't cite any sources — terrible!"). Both errors lead to bad decisions about when to trust and when to question AI output [1][2].

### 5.3 Task type 1 — Creative output

**Creative tasks** ask the AI to produce something original in expression: a poem, a story, an advertising slogan, a piece of dialogue, a list of brainstorm ideas, a metaphor. The goal is expressive, imaginative, or aesthetic effect. Factual accuracy is not required — and should not be used as an evaluation criterion [1].

Evaluation criteria for creative output [1][2]:

| Criterion | What to check |
|---|---|
| **Originality** | Does the output bring a fresh angle, image, or voice? Or is it generic and formulaic — for example, a poem that uses only the most predictable rhyme scheme and the most cliched imagery? |
| **Coherence** | Does the piece hold together internally? Do the ideas, images, or characters connect to each other in a way that makes sense, or does the output jump between unrelated elements? |
| **Prompt adherence** | Did the AI actually follow the creative brief? If you asked for a humorous tone and received a solemn one, or asked for exactly 100 words and got 300, the output has failed this criterion regardless of how polished it sounds. |
| **Stylistic consistency** | Does the writing maintain a consistent voice, register (formal vs. informal), and style throughout? Jarring shifts mid-piece are a quality problem even in creative work. |

Factual accuracy does not appear in this table. That is intentional. A fictional story involving dragons is not "wrong" because dragons do not exist.

### 5.4 Task type 2 — Factual output

**Factual tasks** ask the AI to retrieve, summarise, or explain real-world information: "What were the main causes of the 2008 financial crisis?", "Explain how mRNA vaccines work", "Summarise this news article." The output is expected to accurately represent reality, and its claims should be verifiable [1].

This is the task type most exposed to the hallucination problem you studied in topics 3.2 and 3.9. An AI can produce a fluent, confident-sounding factual summary that contains errors, invented references, or distorted evidence. The hallucination may be completely invisible unless you check.

Evaluation criteria for factual output [1][2][3]:

| Criterion | What to check |
|---|---|
| **Accuracy** | Can each key claim be verified against a reliable source? Cross-check at least the most significant assertions — especially dates, names, statistics, and causal claims. |
| **Citation integrity** | If the output includes references, do those references actually exist? Do they say what the AI claims they say? Invented citations are a common form of attributional hallucination (topic 3.9). |
| **Completeness** | Are important facts missing that would change the overall picture? Partial truths can be as misleading as outright errors. |
| **Source provenance** | Can you trace where the information came from? An AI that asserts "studies show..." without naming any study is producing ungrounded output — a provenance failure (topic 3.9). |

### 5.5 Task type 3 — Logical output

**Logical tasks** ask the AI to reason toward a conclusion: "Given these two conditions, what follows?", "Evaluate the strengths and weaknesses of this argument", "Is this proposal internally consistent?" The output is a chain of reasoning, and each step in that chain should follow validly from the step before it [1].

AI systems can produce logical-sounding text that contains hidden flaws. The output may reach a correct-seeming conclusion by a faulty route — and in decisions that matter, the route matters as much as the destination.

Evaluation criteria for logical output [1][3]:

| Criterion | What to check |
|---|---|
| **Step validity** | Does each individual reasoning step hold? Does each conclusion follow from what was stated just before it, or does the argument make an unstated assumption or hidden jump? |
| **No unwarranted leaps** | Does the output skip from an early premise to a distant conclusion without filling in the intermediate steps? If so, the argument has a gap that needs to be identified. |
| **Correct conclusion from stated premises** | Even if each local step looks valid, does the final conclusion actually follow from the premises the AI accepted at the start? A logical error can be introduced at any point in the chain. |
| **Acknowledgment of uncertainty** | Where the reasoning depends on assumptions or contested evidence, does the output say so? Overconfident logical claims without flagged uncertainty are a calibration problem (topic 3.8). |

### 5.6 Task type 4 — Ethical output

**Ethical tasks** ask the AI to comment on questions of right and wrong, fairness, values, or social impact: "Is it fair to use facial recognition in schools?", "Write a balanced overview of the debate about gene editing in agriculture", "What are the ethical considerations of using AI in hiring decisions?" These tasks are especially sensitive because ethical questions often involve genuinely competing values, and there may be no single correct answer [1].

AI systems trained on large bodies of human text may embed cultural biases, present one viewpoint as if it were universal, or fail to represent the perspectives of affected communities — particularly communities that are underrepresented in the training data [3].

Evaluation criteria for ethical output [1][2][3]:

| Criterion | What to check |
|---|---|
| **Balance of perspectives** | Does the output represent more than one legitimate viewpoint? On genuinely contested questions, a balanced response acknowledges the strongest versions of competing positions, not just one side. |
| **Absence of harmful stereotypes** | Does the output rely on generalisations about groups — by gender, race, religion, nationality, age, disability, or other characteristics — that could reinforce harmful stereotypes? |
| **Appropriate caveats** | Does the output acknowledge the limits of its own perspective? Ethical questions rooted in specific cultural or historical contexts should not be answered as if one framework applies everywhere. |
| **AI values not presented as universal truth** | Does the output present a particular set of values as the only reasonable ones, without acknowledging that other ethical frameworks exist? An AI should not function as a moral authority. |

### 5.7 Task type 5 — Coding output

**Coding tasks** ask the AI to write, fix, or explain code: "Write a Python function that returns the largest number in a list", "Fix the bug in this JavaScript snippet", "Explain what this SQL query does." The output is software — and unlike the other four task types, software has a direct, testable relationship with correctness [1].

Coding output is unique because it can be empirically tested: you run it and see what happens. However, running without crashing is only the minimum bar.

Evaluation criteria for coding output [1][2][3]:

| Criterion | What to check |
|---|---|
| **Runs without error** | Does the code execute without throwing exceptions, syntax errors, or runtime crashes? This is the floor, not the ceiling of quality. |
| **Meets stated requirements** | Does the code actually do what was asked? A function that is supposed to return the largest number but always returns the last number has failed this criterion even if it runs without error. |
| **Handles edge cases** | What happens with empty input, very large input, negative numbers, null values, or other boundary conditions? AI-generated code frequently handles the expected "happy path" and breaks on edge cases. |
| **Readability** | Is the code reasonably understandable? Variable names, structure, and comments should help a reader understand what the code is doing. Readable code is maintainable code. |

### 5.8 Quick-reference rubric summary

| Task type | Primary question to ask | Do NOT use as the primary bar |
|---|---|---|
| Creative | Is it original, coherent, and faithful to the brief? | Factual accuracy |
| Factual | Is it accurate, and do the sources actually exist? | Originality or novelty |
| Logical | Does each step follow validly from the last? | Fluency or confidence of tone |
| Ethical | Are all affected perspectives represented fairly? | Whether you personally agree |
| Coding | Does it run, meet requirements, and handle edge cases? | Whether it sounds plausible |

---

## 6. Implementation — A Five-Step Evaluation Workflow

The following five steps can be applied to any AI output, regardless of task type. Work through them in order [2][3].

**Step 1: Identify the task type.**
Before you evaluate anything, ask: what kind of task was this? Which of the five types — creative, factual, logical, ethical, or coding — best describes what the AI was asked to produce? If the task crosses types (for example, an ethical argument that relies on factual claims), note both and apply both rubrics to the relevant sections.

**Step 2: Select the rubric before reading the output.**
Once you have identified the task type, write down the criteria you will use before you read the output carefully. This step matters: if you read the output first, it will anchor your expectations and make it harder to spot problems. Committing to the criteria in advance protects your judgment from the output's surface quality [2].

**Step 3: Apply each criterion independently.**
Work through the criteria one at a time. For each criterion, assign a rating — for example, Pass / Partial / Fail, or 1 to 4 — and write one sentence of evidence. Do not let strong performance on one criterion mask weak performance on another. An AI output can be highly original (creative: pass) while being factually inaccurate (factual: fail) at the same time. These are separate dimensions [1].

**Step 4: Identify the most serious failure.**
Once all criteria are rated, identify the single most important problem. Not all failures carry the same weight: a minor stylistic inconsistency in a brainstorm is less serious than a hallucinated citation in a factual report. Prioritise your findings so you know what to address first [3].

**Step 5: Document your decision.**
Record your findings in a structured format — a completed rubric table, a short written report, or a notes section in your portfolio. Then make a decision: accept the output as-is, accept it with edits, or reject it and regenerate. If you accept with edits or reject, write down what prompted that decision. This documentation is evidence for your Specification Portfolio (Assessment A1) and is also the kind of record that professional AI practitioners keep to remain accountable for the outputs they approve [2][3].

---

## 7. Real-World Patterns — How Each Task Type Goes Wrong

Knowing the typical failure modes for each task type helps you know what to look for before you even start evaluating [1][3].

**Creative — The generic default voice.** AI systems trained on large amounts of text tend to produce an "average" of all the creative writing they have seen. The result is often grammatically clean but distinctly mediocre: predictable metaphors, the safest possible structure, a tone that could belong to anyone. The criterion most often failed is originality. If you notice that every AI-generated poem rhymes in the same simple scheme and uses the same small vocabulary of "beautiful," "golden," and "eternal," originality has not been met.

**Factual — The plausible but invented citation.** A well-documented pattern (see topics 3.2 and 3.9): the AI produces a reference that sounds exactly like a real academic paper — plausible-sounding authors, a realistic journal title, a year, and a plausible-sounding topic — but the paper does not exist. Readers who do not verify citations will treat invented sources as real. The criterion failed is citation integrity. Verification method: paste the citation into a search engine or database (Google Scholar, PubMed, a library catalogue) and confirm it exists [1].

**Logical — The confident conclusion with a hidden gap.** An AI may produce a well-formatted argument — numbered premises, smooth transitions, a clear-sounding conclusion — while quietly skipping from premise 2 to conclusion 5 without the intermediate steps. The text reads as if the reasoning is complete, but the logic has a gap. The criterion failed is "no unwarranted leaps." Verification method: restate each step in your own words and ask whether it genuinely follows from the step just before it [3].

**Ethical — False universalism.** An AI may answer an ethical question as if one cultural or philosophical framework's answer is the obvious, universal answer — without acknowledging that other traditions, communities, or value systems would respond differently. The criterion failed is "AI values not presented as universal truth." Check for this by asking yourself: after reading this response, which perspectives are absent? Who is not mentioned, and would their answer differ?

**Coding — The happy-path trap.** AI-generated code frequently handles the main expected scenario correctly but crashes or produces wrong output for edge cases (empty list, null input, negative numbers, very large inputs). The code passes the developer's own test but fails in production when real data arrives. The criterion failed is edge case handling. Verification method: run the code with inputs that are empty, at the boundary of what is expected, and deliberately unexpected [1][3].

---

## 8. Best Practices

**Commit to the rubric before reading the output.** If you read first and evaluate second, the output anchors your judgment. Establish your criteria first [2].

**Rate each criterion separately.** Keep a distinct row or line for each dimension. Do not collapse everything into a single overall impression. AI output commonly has uneven quality across dimensions — one criterion can pass while another fails [1].

**Verify, do not trust.** For factual and logical outputs especially, "sounds convincing" is not a verification method. Check key claims against a source you trust that was not itself produced by the AI you are evaluating [3].

**Match evaluation effort to stakes.** A five-minute internal brainstorm needs a lighter evaluation than a customer-facing factual report. The five-step workflow scales: for low-stakes work, a mental walkthrough may suffice; for high-stakes work, a written rubric with documented ratings is appropriate [3].

**Document accepted flaws explicitly.** When you accept an AI output despite known weaknesses, write down what the weaknesses are and why you accepted it anyway. Undocumented acceptance of flawed output is a quality risk. Documented acceptance with clear reasoning is an informed professional decision — and it is what Assessment A1 asks you to demonstrate [2].

**Treat these rubrics as starting points.** The criteria in this topic are a foundation, not a final authority. As you work in specific domains — healthcare, law, education, software engineering — you will develop more nuanced criteria suited to the particular risks and standards of those fields [1][3].

---

## 9. Hands-On Exercise

This exercise directly prepares you for Journal Entry #3 and Assessment A1.

**Part A — Ethical and factual task type.**
Run the following prompt through an AI system of your choice: *"Explain the main arguments for and against using AI in criminal sentencing decisions."*

Before reading the output carefully, write down: (1) which task type(s) this represents, and (2) which criteria from section 5 you will apply. Then read the output and apply each criterion with a rating (Pass / Partial / Fail) and one sentence of evidence. Identify the single most serious quality problem, if any. Apply step 5 of the workflow: decide whether to accept, accept with edits, or reject, and document your reasoning.

**Part B — A second task type.**
Repeat the process with a different task type: either ask the AI to write a short creative piece (e.g., a three-sentence description of a city at dawn from the perspective of someone who has never slept there), or ask it to fix a simple code snippet of your choice.

**Compare the two rubrics.** After both parts, write two sentences: one identifying where the criteria were completely different between your two task types, and one identifying whether applying the wrong rubric to either output would have changed your conclusion.

---

## 10. Key Takeaways

- AI output quality depends on task type. Applying the wrong evaluation bar — for example, checking a poem for factual accuracy — produces meaningless results and leads to bad decisions about when to trust AI output [1][2].
- The five task types are: **creative** (originality, coherence, prompt adherence, stylistic consistency), **factual** (accuracy, citation integrity, completeness, provenance), **logical** (step validity, no unwarranted leaps, correct conclusion from premises, appropriate uncertainty), **ethical** (balance of perspectives, absence of harmful stereotypes, appropriate caveats, no false universalism), and **coding** (runs without error, meets requirements, handles edge cases, readability) [1][2][3].
- Fluency and confident tone are not evaluation criteria for any of the five task types. They are surface features that can conceal serious quality failures.
- The five-step evaluation workflow — identify task type, select rubric before reading, apply criteria independently, identify the worst failure, document and decide — provides a repeatable method for any AI output [2][3].
- Documenting your evaluations, including known failures you chose to accept and why, is both professionally responsible practice and a direct requirement of Assessment A1.

---

## 11. Next Steps

_System-derived from the next entry in curriculum/sequence.md._
