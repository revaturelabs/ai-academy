---
topic_id: 3.8
title: The jagged frontier — tasks AI is superhuman at vs tasks where it is unreliable
position_in_module: 2
generated_at: 2026-06-17T00:00:00Z
resource_count: 3
---

# 1. The Jagged Frontier — Tasks AI Is Superhuman At vs Tasks Where It Is Unreliable — Topic Corpus

## 2. Prerequisites

This topic builds on two earlier topics:

- **3.2 — How LLMs Work**: You should understand what a large language model (LLM) is, how it is trained on text data, and what hallucination means — the model generating plausible-sounding but incorrect output.
- **3.5 — Scale and Emergent Capabilities**: You should understand what parameters (the learned weights inside a model) are, and how scaling a model to billions of parameters can cause surprising new abilities to appear.

## 3. Learning Objectives

By the end of this topic, you should be able to:

1. Define the **jagged frontier** and explain, in your own words, why AI capability is uneven across task types rather than uniformly strong or weak.
2. Give at least two examples of tasks where AI performs at or above expert human level, and explain why AI tends to excel there.
3. Give at least two examples of tasks where AI remains unreliable, and explain the underlying reason for each failure.
4. Explain what **calibration** means in the context of AI confidence, and describe why poor calibration is a safety risk.
5. Apply a simple probing method to test an AI system on an unfamiliar task and interpret whether the result is inside or outside the reliable zone.

## 4. Introduction

Imagine hiring a new colleague who can write a polished research summary in three minutes, pass a bar exam, and read a chest X-ray with expert accuracy — but then struggles to count the number of words in a single sentence and confidently gives you the wrong answer. That is not a fictional exaggeration. It is a reasonably accurate description of today's AI systems.

Most people, when they first use an AI assistant, expect it to behave like a calculator: consistent, reliable across all inputs, and either correct or visibly broken. Instead, they discover something stranger. The system can write a convincing legal brief but get simple arithmetic wrong. It can generate working code for a complex algorithm but fail to tell you whether a chair fits through a doorway. It can summarise a 400-page report in seconds but become dangerously confident about a fact it has invented.

This uneven landscape has a name: the **jagged frontier** [1]. The term was coined and popularised by Wharton professor Ethan Mollick to capture a key insight: AI capability does not rise or fall smoothly. Instead, it spikes high on some tasks and drops unexpectedly low on others, with no obvious pattern for a newcomer to detect from the outside [1].

Understanding the jagged frontier is not an academic exercise. If you deploy an AI tool for the wrong task category, you get a system that looks confident and is secretly wrong. That mismatch is the root cause of most real-world AI failures. Knowing where the frontier sits — and that it is moving — is a foundational practitioner skill.

## 5. Core Concepts

### 5.1 What the Jagged Frontier Is

The **jagged frontier** is the boundary between what AI systems currently do reliably well and what they do unreliably or poorly [1]. Mollick's key observation is that this boundary is not a smooth line. It zigzags in unpredictable ways [1].

Think of it as a map with peaks and valleys. At the peaks, AI performance is genuinely superhuman — it surpasses what even expert humans can achieve in terms of speed, scale, or accuracy. In the valleys, the same AI system produces errors so basic that a child would catch them.

The "jagged" part is what makes this hard to work with. You cannot simply say "AI is good at language tasks and bad at math." Some language tasks (like creative writing or summarisation) sit at the peaks; others (like reliably counting words or tracking a long chain of pronouns through a conversation) sit in the valleys. Some math tasks (like writing Python code that computes a formula) are peaks; others (like multi-step mental arithmetic) are valleys.

A related concept is the **capability cliff**: the phenomenon where AI performance is strong right up to a task variation, and then drops suddenly and steeply when the task is modified in a small way [2]. The cliff is why the frontier is jagged rather than gently sloped. You cannot always extrapolate from "it did this version well" to "it will do a slightly harder version adequately."

### 5.2 Where AI Is Superhuman

Several task categories sit consistently at or above the human-expert level for modern LLMs and associated AI systems [1][2].

**Pattern recognition in large datasets.** Humans can examine a few hundred data points before fatigue sets in. AI systems can scan millions of records, find statistical regularities, and flag anomalies at a scale no human team can match. This shows up in fraud detection (scanning millions of transactions), drug discovery (screening millions of molecular candidates), and recommendation systems.

**Medical image diagnosis.** AI models trained on large sets of labelled images — X-rays, retinal scans, skin lesion photographs — have matched or exceeded specialist radiologist accuracy on specific, well-defined tasks [2]. A key word here is "specific": the model is tested on the same type of image it trained on, in controlled conditions.

**Protein structure prediction.** DeepMind's AlphaFold solved a 50-year grand challenge in biology by predicting how proteins fold into three-dimensional shapes, a task considered extraordinarily difficult [2]. This is a landmark example of AI doing something that was practically impossible for human researchers at scale.

**Text generation, summarisation, and translation.** LLMs generate fluent, coherent text across many styles and languages [1]. On standard **benchmarks** — formal tests with defined correct answers and scoring rules used to measure and compare AI performance objectively — they score at or above the level of professional writers and translators on many measures.

**Code synthesis.** Modern LLMs can write working code in dozens of programming languages for well-specified problems. On public coding benchmarks, they score at expert-human level for standard algorithmic challenges [1].

**Games with complete information.** Systems like AlphaGo (board game Go) operate at levels no human can approach, but these are narrow, specialised AI systems, not LLMs, and are mentioned only for context.

The common thread in AI peaks: tasks with a large, clean training dataset, a well-defined output space, and a ground truth the model can learn from. Pattern matching within a known distribution is where AI shines.

### 5.3 Where AI Is Unreliable

The valleys are less intuitive, because they often involve tasks that feel simple to a human [1][2].

**Spatial reasoning.** **Spatial reasoning** is the ability to mentally manipulate objects in space — imagining what a shape looks like rotated, whether one object fits inside another, or which path through a physical space is shortest. LLMs process language tokens (as you learned in topic 3.4), not spatial representations. When asked "If I rotate this L-shaped piece 90 degrees clockwise, does it fit in this slot?", the model is working from verbal descriptions without any real spatial model — and it frequently gets this wrong [2].

**Counting objects.** Counting small numbers of items in a simple sentence or image is surprisingly difficult for LLMs. Because the model predicts likely next tokens rather than executing a counting algorithm, it can confidently mis-count. Ask an LLM how many letter 'r's are in the word "strawberry" and it will often say two instead of three — a well-documented failure.

**Reliable arithmetic.** LLMs are not calculators. They generate plausible sequences of digit tokens. For simple operations (2 + 2) this works fine because such patterns are heavily represented in training data. For multi-digit arithmetic done without a code execution tool, errors are common and unpredictable. This is a textbook capability cliff: reliable for trivial cases, unreliable for moderately complex ones, with no clean threshold [2].

**Multi-step logical deduction.** A **reasoning task** in AI refers to any problem where the correct answer requires following a chain of steps where each step depends on the previous one. LLMs can appear to reason fluently but often "short-circuit" — jumping to a plausible-sounding conclusion without actually tracking the logical chain. This is especially pronounced when the chain requires holding many intermediate facts in mind simultaneously.

**Calibration — knowing what it doesn't know.** **Calibration** in AI means the match between a model's expressed confidence and its actual accuracy [1][2]. A perfectly calibrated model that says it is 90% sure of an answer is correct 90% of the time. LLMs are often poorly calibrated: they express high confidence even when they are wrong. This is especially dangerous because the model does not have a reliable internal signal for "I am outside my training distribution." It generates the most plausible-sounding answer regardless — which is the mechanism behind hallucination (introduced in topic 3.2). Poor calibration makes it hard for users to know when to trust the output.

**Physical world sense.** LLMs were trained on text describing the world, not on sensory experience of the world. They can struggle with commonsense questions that depend on physical intuition: what happens when you drop something, how heavy an object is, whether a liquid will fit in a container. The training data contains answers to many such questions, but the model has no underlying physical model — it only has the statistical pattern of how humans describe physical events.

### 5.4 Why the Frontier Is Jagged Rather Than Smooth

If AI were simply "getting smarter" uniformly, you would expect capability to rise evenly. The jagged shape has specific causes [1][2].

**Training data distribution.** An LLM is trained on a massive corpus of human-written text scraped from the internet, books, and other sources. The model learns to produce outputs that match the statistical patterns in that corpus. Tasks that are heavily represented in training data — writing emails, translating common language pairs, explaining popular programming patterns — benefit from millions of examples. Tasks that are rare or absent in the training corpus — novel logical puzzles, unusual spatial configurations, specific niche knowledge — receive little learning signal. The result is high performance where training data is dense, and unreliability where it is sparse.

**Interpolation vs extrapolation.** When an LLM answers a question that closely resembles patterns in its training data, it is *interpolating* — filling in between examples it has seen, like estimating a point between two known data points. This is reliable. When the question requires genuine novel reasoning — working through a logic chain never seen in training — it is *extrapolating* (reasoning beyond what the training data covered), which LLMs do poorly. Most of the jagged valleys are extrapolation zones.

**Emergent capabilities and their limits.** As you learned in topic 3.5, scaling a model to many billions of parameters causes emergent capabilities — new abilities that appear suddenly at scale without being explicitly trained. This sounds like uniform improvement, but the emergence is uneven: some capabilities appear at 7 billion parameters, others at 70 billion, and some have not appeared at any scale yet. The result is a frontier that jumps up sharply in some areas while remaining flat in others. And when a capability is emergent rather than systematically trained, it can also fail in edge cases that seem superficially similar to cases where it works — producing the capability cliff effect [2].

**Hallucination as a structural failure mode.** Hallucination — generating confident, plausible, but false output — is not a bug that will be patched away. It emerges from the same mechanism that makes LLMs useful: predicting the most statistically likely next token [1]. Where the model is inside its training distribution, the most likely token is often correct. Where it is outside the distribution, the most likely token is still generated — it just is not grounded in anything real. Poor calibration means the model does not flag this difference. This is why hallucination disproportionately appears in the valleys of the jagged frontier.

### 5.5 The Frontier Is Moving

The frontier is not fixed. New model generations close some gaps [3].

In 2025, Mollick updated his jagged frontier analysis to note that newer models — including OpenAI's o3 and Google's Gemini 2.5 — show markedly improved performance on reasoning tasks that were previously deep in the valley [3]. Chain-of-thought prompting (covered in a later topic) has moved some multi-step logical tasks from unreliable to workable [3].

However, the frontier moving does not mean it disappears [3]. As gaps close on previously hard tasks, new use cases emerge that expose new gaps. And improved performance on benchmarks does not always transfer cleanly to real-world tasks that differ subtly from the test format. Additionally, the models getting better does not remove the need for human oversight: a system that is right 95% of the time on a task still needs a check if a 5% error rate is unacceptable for the use case [1][3].

The practical implication is that practitioner knowledge about the frontier needs regular refreshing. What was a valley in 2023 might be a peak in 2025 — and vice versa, as new task categories are tested.

## 6. Implementation

**How to probe the frontier for a specific task: a 5-step approach**

This approach maps directly onto the Capability Probe lab activity.

**Step 1 — Choose task categories deliberately.** Select tasks that span the frontier: creative writing (likely peak), factual recall on an obscure topic (mixed), logical deduction (likely valley), spatial description (likely valley), and code synthesis for a well-specified problem (likely peak). Do not pick only easy or only hard tasks — you want to observe the jagged shape.

**Step 2 — Run the AI on each task without coaching.** Give the task as you would give it to a knowledgeable human assistant. Do not add special prompting tricks yet. Record the response verbatim.

**Step 3 — Evaluate correctness independently.** For each task, determine the correct answer using a source that is not the AI (a textbook, a calculator, your own knowledge). Do not evaluate "does it sound confident?" — evaluate "is it right?". This is calibration testing: does expressed confidence match actual accuracy?

**Step 4 — Note capability cliffs.** After a successful result, try a small variation: add one step to a logical chain, make the arithmetic slightly larger, ask the spatial question from a different angle. Document where performance drops suddenly — these are the cliff edges.

**Step 5 — Document the frontier map.** For each task type, record: (a) was it reliable?, (b) where did it fail?, (c) did the model flag its uncertainty or state wrong answers confidently? This is your personal frontier map for the task domain, which you can update as models improve.

## 7. Real-World Patterns

**Medical AI diagnostics.** Several AI-assisted diagnostic tools have been approved for clinical use on the strength of their performance on specific imaging tasks [2]. The frontier here is narrow: a model trained to detect diabetic retinopathy in retinal scans may perform at specialist level on that specific task, but the same model should not be trusted for a different imaging modality or a different disease it was not trained on. The jagged frontier means "good at this imaging task" does not generalise to "good at medical imaging" [2].

**Legal and professional document work.** LLMs score at or above the median human score on bar exams and other professional licensing exams [1]. Law firms began using AI for contract review and legal research drafts. However, hallucination in legal citations — where the model invents plausible-sounding case names that do not exist — has led to court sanctions when lawyers filed AI-generated briefs without checking the citations [1]. The model was at the peak for prose generation and in the valley for factual reliability of specific citations.

**Code review and software engineering.** AI coding assistants have demonstrated measurable productivity gains for software developers on well-defined tasks [1]. But the reliability breaks down at the edges: testing edge cases, identifying subtle security vulnerabilities, or reasoning about complex system interactions across multiple files — tasks requiring the kind of multi-step logical tracking that sits in the valley.

**Customer-facing AI agents.** Companies deploying AI agents (introduced in topic 3.3) for customer service encounter the jagged frontier acutely. The agent handles routine queries (peak) well but fails or hallucinates on unusual edge cases (valley) — and the customer often cannot distinguish a confident wrong answer from a confident right one, because the agent's calibration is poor [2].

## 8. Best Practices

**Always test the specific task, not the general category.** "AI is good at writing" is too coarse. Test whether AI is good at your writing task. The capability cliff means a small change in task specification can move you from peak to valley [2].

**Treat AI output as a first draft, not a final answer.** For any task in a valley (arithmetic, factual citations, multi-step logic, spatial reasoning), build a human review step into your workflow. The cost of review is lower than the cost of a published error [1].

**Use AI's expressed confidence as a red flag, not a green light.** Poor calibration means a confident answer is not evidence of a correct answer. If anything, high confidence on an unusual question should prompt closer scrutiny, not less.

**Match the tool to the frontier, not the frontier to the tool.** If you discover a task reliably falls in the valley, do not attempt to "fix" it with more prompting alone. Either redesign the task to one the AI handles well, use a specialised tool (e.g., a calculator for arithmetic), or accept that this task requires human execution.

**Refresh your frontier map.** Because the frontier moves — as newer models like o3 and Gemini 2.5 close previously known gaps [3] — the knowledge that "AI can't do X" has a shelf life. Build a habit of re-testing tasks you assumed were valleys when a new model version is released.

**Do not assume benchmark scores transfer directly to your use case.** A benchmark measures performance on a specific, standardised test. Real-world tasks differ from benchmarks in subtle ways that can move them from peak to valley [1][3].

## 9. Hands-On Exercise

This exercise maps directly onto the **Capability Probe** lab activity.

Select one AI assistant (Claude, for instance) and run it through exactly five tasks, one per category:
1. **Creative** — ask it to write a short poem in the style of a given poet.
2. **Factual** — ask a specific factual question in a domain you know well enough to verify.
3. **Logical** — give it a three-step deductive reasoning puzzle (e.g., "Alice is taller than Bob. Bob is taller than Carlos. Is Carlos taller than Alice?") and then a five-step version.
4. **Ethical** — pose a morally ambiguous scenario and evaluate whether the response is nuanced or oversimplified.
5. **Coding** — ask it to write a short function with a clear specification.

For each task, independently verify the answer, record whether the model expressed appropriate uncertainty, and note any capability cliff you found in the logical task. Write up your findings as Journal Entry #2: which tasks were peaks, which were valleys, where did you find a cliff, and did the model's confidence match its accuracy?

## 10. Key Takeaways

- The **jagged frontier** is the uneven boundary of AI capability: AI is superhuman on some tasks and unreliable on others, with no smooth gradient between the two [1].
- AI peaks tend to occur where training data is dense and outputs are well-defined; AI valleys tend to occur at tasks requiring extrapolation, spatial reasoning, reliable arithmetic, or multi-step logical deduction [1][2].
- **Calibration** — the match between expressed confidence and actual accuracy — is poor in current LLMs, meaning confident answers can be wrong, and hallucination is a structural consequence of this, not a fixable bug [1].
- **Capability cliffs** mean that a small change to a task that the AI handles well can cause performance to drop suddenly and sharply [2].
- The frontier is moving: 2025 models like o3 and Gemini 2.5 have closed some valleys, but new gaps emerge with new use cases, and human oversight remains essential [3].

## 11. Next Steps

_System-derived from the next entry in curriculum/sequence.md._
