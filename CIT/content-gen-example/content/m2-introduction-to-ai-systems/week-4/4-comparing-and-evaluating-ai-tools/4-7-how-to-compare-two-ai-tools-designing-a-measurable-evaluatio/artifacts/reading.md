<!-- nav:top:start -->
[⬅ Previous: 4.6 — Multimodal AI](../../../3-multimodal-ai/4-6-multimodal-ai-working-with-text-image-audio-and-video-in-one/artifacts/reading.md)&emsp;·&emsp;[⬆ Table of Contents](../../../../../../../README.md#curriculum-topic-index)&emsp;·&emsp;[Next: 4.8 — Presenting a findings-based recommendation ➡](../../4-8-presenting-a-findings-based-recommendation-evidence-not-opin/artifacts/reading.md)
<!-- nav:top:end -->

---

# How to Compare Two AI Tools — Designing a Measurable Evaluation Rubric

## Overview

When two people try the same AI tool and reach different conclusions, the problem is usually not the tool — it is the lack of a shared standard for judging it. A **rubric** is that standard: a scoring guide that turns a personal impression into a measurable, repeatable comparison. This topic shows you how to build one from scratch. By the end, you will be able to compare any two AI tools and defend your conclusion with evidence rather than opinion [1].

## Key Concepts

### What Is an Evaluation Rubric?

In topic 3.10 you applied a rubric to judge the quality of AI *outputs* across five task types — creative, factual, logical, ethical, and coding. This topic applies the same scoring logic at a larger scale: judging the AI *tool* that produces those outputs.

An **evaluation rubric** is a structured scoring guide used to judge something against a fixed set of criteria. Every rubric has three essential parts [1]:

1. **Criteria** — the specific qualities you are judging (e.g., "accuracy of outputs")
2. **Performance levels** — the range of possible scores for each criterion (e.g., 1 = poor, 4 = excellent)
3. **Descriptors** — plain-language statements explaining what each score means

Descriptors are the most important part. Without them, "score 3" means something different to every person who uses the rubric. With good descriptors, two separate evaluators looking at the same tool output should award the same score — because they are matching what they see to the same written description.

**Quick example — one criterion, three levels:**

| Score | Level | Descriptor |
|---|---|---|
| 1 | Poor | Outputs contain frequent factual errors that would mislead a user |
| 2 | Acceptable | Outputs are mostly correct but contain noticeable gaps or vague statements |
| 3 | Excellent | Outputs are accurate, specific, and verifiable against a known source |

### Why a Rubric Instead of Just Trying the Tool?

Most people test an AI tool by trying it once and forming an impression. The problem: impressions are shaped by mood, the task you happened to choose, and the exact wording of your prompt. They are not repeatable, and someone else cannot check your work [2].

A rubric fixes three things at once:

- **Inconsistency** — both tools are tested against the exact same criteria, so the comparison is fair
- **Non-transferability** — another person can run the same rubric and reach a similar result
- **Indefensibility** — every score points to specific evidence, not a gut feeling [1][3]

The shift is from "I think Tool A is better" to "Tool A scored 4/5 on accuracy and 3/5 on privacy; Tool B scored 3/5 on accuracy and 4/5 on privacy — here is the evidence."

### The Five Common Criteria

A well-designed AI tool rubric draws from five broad areas that appear consistently across practitioner and academic frameworks [1][2][3]:

**1. Functionality** — What does the tool do, and how well?
- Does it complete the task you give it (summarise a document, answer a question, generate an image)?
- Is the output relevant to the input?
- Does it handle unusual requests without failing?

**2. Accuracy and Reliability** — How correct are the outputs?
- Are factual claims verifiable against a known source?
- Does the tool give consistent answers to the same question, or does it vary widely?
- Does it acknowledge uncertainty, or does it invent an answer? This is the hallucination risk you saw in topic 3.9.

**3. Privacy and Data Handling** — What happens to the data you provide?
- Is your input stored or used to train future versions of the model?
- Does the tool ask for sensitive information it does not need?
- Is there a readable privacy policy?

**4. Accessibility and Ease of Use** — Can the people who need it actually use it?
- Is the interface clear for a first-time user with no training?
- Does it work on the devices your users have (mobile, low-bandwidth)?
- Are there accessibility features for users with disabilities?

**5. Ethics and Bias** — Does the tool behave fairly and responsibly?
- Does it produce outputs that favour certain groups over others?
- Does it generate harmful or misleading content?
- Is it transparent about being an AI, not a human?

Practitioners sometimes add a sixth area — **cost and licensing** — covering whether the tool is free, freemium, or paid, and what usage limits apply [3].

### The Rubric Process

![Evaluation Rubric Framework](./diagram.png)
*The five-step process for comparing two AI tools: from defining criteria to comparing weighted totals.*

The diagram shows the sequence you follow every time you build a comparison rubric. Each step feeds the next; skipping one weakens the whole comparison.

### Writing Scoring Levels and Descriptors

Choosing criteria is the first step; writing clear descriptors is the harder one. A common scale is 1–4 (an even number forces a decision — no neutral middle score). The number of levels matters less than the quality of the descriptions [3].

**Rules for good descriptors:**

- Describe *observable behaviour* — something you can see in the output or documentation, not something you have to guess at
- Make adjacent levels clearly distinguishable — if levels 2 and 3 look the same, the rubric is not working
- Use consistent language across criteria so "level 3" means roughly the same standard everywhere
- Replace vague words like "good" or "adequate" with specific statements

**Example — Accuracy criterion, 4-level scale:**

| Score | Descriptor |
|---|---|
| 4 | Every factual claim is correct and verifiable; the tool explicitly flags uncertainty |
| 3 | Most claims are correct; minor errors present but do not affect usefulness |
| 2 | Several errors present; a user relying on the output without checking would be misled |
| 1 | Major factual errors or fabricated information that could cause harm if acted upon |

### Weighting Criteria

Not all criteria matter equally in every situation. A rubric can assign **weights** — numbers that reflect how much each criterion contributes to the final score. Weights must sum to 100% [1][3].

**Example — a 5-criterion weighted rubric:**

| Criterion | Weight | Score (1–4) | Weighted Score |
|---|---|---|---|
| Functionality | 30% | 3 | 0.90 |
| Accuracy and Reliability | 25% | 4 | 1.00 |
| Privacy and Data Handling | 20% | 2 | 0.40 |
| Accessibility and Ease of Use | 15% | 3 | 0.45 |
| Ethics and Bias | 10% | 3 | 0.30 |
| **Total** | **100%** | — | **3.05 / 4.00** |

Set your weights before you score. Adjusting weights after you have seen the results — to favour the tool you already preferred — is not evaluation; it is a disguised opinion.

### Collecting Comparable Evidence

A rubric scores evidence. Before you score, you need to collect that evidence by running the same set of test tasks on both tools under the same conditions.

A **test protocol** is a short written plan describing [2][3]:

- The exact tasks or prompts you will run (e.g., "Ask the tool to summarise this 300-word article")
- How many times you will run each task (three runs gives a more representative picture than one)
- The conditions: same device, same account tier, same time of day

Even a simple five-task protocol makes your evidence far stronger than a single casual test.

## Worked Example

Here is a complete walkthrough comparing two AI writing assistants — Tool A and Tool B — using a three-criteria rubric.

**Step 1 — Choose criteria and assign weights.**

The evaluator decides the comparison is for a student writing context, so accuracy and privacy matter most:

| Criterion | Weight |
|---|---|
| Accuracy and Reliability | 40% |
| Privacy and Data Handling | 35% |
| Accessibility and Ease of Use | 25% |

**Step 2 — Write descriptors (done before testing).**

For Accuracy, the evaluator writes the 4-level table shown in the Key Concepts section above. Similar tables are written for Privacy and Accessibility.

**Step 3 — Design the test protocol.**

The evaluator lists three specific tasks: (a) summarise a 200-word news paragraph, (b) answer a factual question about a historical event, (c) rewrite a sentence in formal English. Both tools receive the same prompts in the same order.

**Step 4 — Run the protocol and record raw output.**

Screenshots are taken for each task on each tool. Nothing is scored yet.

**Step 5 — Score each tool on each criterion.**

Matching the saved outputs to the descriptor tables:

| Criterion | Weight | Tool A Score | Tool B Score |
|---|---|---|---|
| Accuracy | 40% | 4 | 3 |
| Privacy | 35% | 2 | 4 |
| Accessibility | 25% | 3 | 3 |

**Step 6 — Calculate weighted totals.**

- Tool A: (4 × 0.40) + (2 × 0.35) + (3 × 0.25) = 1.60 + 0.70 + 0.75 = **3.05**
- Tool B: (3 × 0.40) + (4 × 0.35) + (3 × 0.25) = 1.20 + 1.40 + 0.75 = **3.35**

**Step 7 — Write the finding.**

Tool B scores higher overall (3.35 vs 3.05). Tool A is more accurate, but its low Privacy score (2/4) is a significant concern for a student context where personal writing is uploaded. Given the weights chosen, Tool B is the better fit — though the evaluator notes the comparison used only three prompts per task, and a larger test might narrow the gap.

## In Practice

Real organisations evaluating AI tools at scale — universities, hospitals, government agencies — use structured evaluation frameworks that closely mirror the rubric process above. They do not select tools based on vendor demos [1].

A university technology committee evaluating AI writing tools, for example, might run every candidate tool through criteria covering academic integrity risk, student data privacy, accessibility, and output quality. Each committee member scores independently; the group then compares scores and discusses gaps [1][2].

**Practical do's:**

- Write descriptors *before* you test. Writing them after unconsciously favours the tool you already prefer.
- Use the same prompts on both tools. Different prompts make the comparison meaningless.
- Keep raw evidence — screenshots, copied outputs. Anyone reviewing your work may ask to see it.
- State your weights and justify them. "I weighted Privacy at 35% because students upload personal writing" is a defensible statement.
- Acknowledge limitations. No five-task test is exhaustive; be honest about what your rubric does and does not cover.

**Practical don'ts:**

- Adjust weights after seeing the scores.
- Use vague language in descriptors — replace "performs adequately" with a specific statement.
- Rely on a single test run for criteria where randomness matters (accuracy, consistency).
- Compare tools at different pricing tiers without noting it — the free version of Tool A versus the paid version of Tool B is not a fair comparison.
- Ignore a critically low score because the overall total looks acceptable. A tool that scores 1/4 on Privacy is not rescued by high marks on everything else [3].

Practitioners also track evaluation over time. A tool that scores well today may score differently in six months if the underlying model is updated or its privacy policy changes. A rubric makes re-evaluation straightforward — run the same protocol again and compare the new score to the old one [3].

## Key Takeaways

- A **rubric** is a scoring guide with three parts — criteria, performance levels, and descriptors. It turns personal opinion about an AI tool into a measurable, repeatable comparison.
- The five common criteria for AI tool rubrics are **functionality**, **accuracy and reliability**, **privacy and data handling**, **accessibility and ease of use**, and **ethics and bias**.
- **Descriptors** — plain-language statements describing what each score level looks like in observable behaviour — are what make a rubric consistent; vague descriptors produce inconsistent scores.
- **Weights** reflect what matters most in your specific context; they must be set before scoring, never adjusted afterward to favour a preferred tool.
- A **test protocol** — the same tasks, same conditions, run on both tools — is what connects your rubric criteria to real evidence you can point to.

## References

[1] Academic Senate for California Community Colleges. *Criteria for Evaluating AI Tools: 2024 Rubric*. https://www.asccc.org/sites/default/files/Criteria_for_evaluating_AI_tools_2024_rubric_r.pdf

[2] eCampusOntario / McMaster University. "Evaluating AI Tools." *A Practical Guide to AI*. https://ecampusontario.pressbooks.pub/mcmasterpracticalaiguide/chapter/evaluating-ai-tools/

[3] Encord. "Rubric Evaluation of Generative AI: A Practical Assessment Framework." https://encord.com/rubric-evaluation-generative-ai-assessment/

---
<!-- nav:bottom:start -->
[⬅ Previous: 4.6 — Multimodal AI](../../../3-multimodal-ai/4-6-multimodal-ai-working-with-text-image-audio-and-video-in-one/artifacts/reading.md)&emsp;·&emsp;[⬆ Table of Contents](../../../../../../../README.md#curriculum-topic-index)&emsp;·&emsp;[Next: 4.8 — Presenting a findings-based recommendation ➡](../../4-8-presenting-a-findings-based-recommendation-evidence-not-opin/artifacts/reading.md)
<!-- nav:bottom:end -->
