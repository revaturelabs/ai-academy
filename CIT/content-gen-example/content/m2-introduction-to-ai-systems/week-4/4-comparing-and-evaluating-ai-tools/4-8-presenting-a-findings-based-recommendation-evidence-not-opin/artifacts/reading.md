<!-- nav:top:start -->
[⬅ Previous: 4.7 — How to compare two AI tools](../../4-7-how-to-compare-two-ai-tools-designing-a-measurable-evaluatio/artifacts/reading.md)&emsp;·&emsp;[⬆ Table of Contents](../../../../../../../README.md#curriculum-topic-index)&emsp;·&emsp;[Next: 5.1 — Real AI failure cases ➡](../../../../week-5/1-ai-failures-and-why-they-happen/5-1-real-ai-failure-cases-healthcare-misdiagnosis-hiring-bias-de/artifacts/reading.md)
<!-- nav:top:end -->

---

# Presenting a Findings-Based Recommendation — Evidence, Not Opinion

## Overview

You have designed a rubric, weighted the criteria, run a test protocol, and scored two AI tools. You now have a table of numbers. This topic teaches you how to turn those numbers into a short written recommendation that another person can read, check, and act on. The key shift is moving from "I think Tool A is better" — which no one can verify — to "Tool A scored 3.2 out of 4, and here is the specific evidence that explains why" — which anyone can trace [1].

## Key Concepts

### Opinion vs Evidence

When someone asks which tool is better, the natural impulse is to say how it felt. That is not wrong as a starting point, but it is not a recommendation. An **opinion** is a personal preference or feeling that another person cannot independently check — for example, "Tool A seemed smarter." An **evidence statement** is a specific, recorded result tied to your rubric, test protocol, or documented observation — for example, "Tool A scored 4 out of 5 on the accuracy criterion across three test runs" [1].

The practical difference matters. An opinion can be dismissed with a counter-opinion. Evidence can only be challenged by questioning the rubric design or the test protocol, both of which you have on record [1].

Use this quick filter before writing any sentence:

| Statement | Can another person check it? | Type |
|---|---|---|
| "Tool A felt more natural to use." | No — it is a feeling | Opinion |
| "Tool A scored 4/5 on ease-of-use in all three test runs." | Yes — score sheet is on record | Evidence |
| "I think Tool B is better for our team." | No — it is a belief | Opinion |
| "Tool B scored highest on the collaboration criterion (weight: 20%)." | Yes — rubric and scores are on record | Evidence |

Every sentence in a findings-based recommendation should pass the "can another person check this?" test [1].

### The Three-Part Structure

A **findings-based recommendation** is a short written statement that presents what your evaluation found, anchors the conclusion in specific evidence, and states a clear recommendation with any conditions attached [1][2].

It has three parts, presented in this order:

**Part 1 — Findings summary.** One or two sentences stating what the evaluation found overall. Name both tools, reference the rubric, and give the weighted totals.

> Example: "Using a five-criteria rubric weighted toward accuracy and accessibility, Tool A scored 3.2 out of 4 and Tool B scored 2.6 out of 4 across ten test tasks."

**Part 2 — Evidence anchor.** Two or three specific results — criterion name, score for each tool, and a concrete observation from the test — that explain why the totals landed where they did.

> Example: "Tool A's lead came from functionality (4/4 versus 2/4) and accuracy (3/4 versus 2/4). In three of the five test tasks, Tool B produced outputs containing factual errors; Tool A's outputs on the same tasks required no correction."

**Part 3 — Recommendation statement.** A clear conclusion tied directly to the findings, with any conditions or limitations named.

> Example: "We recommend Tool A for student coursework support. If this tool will be used with sensitive personal data, the privacy criterion — where both tools scored equally — should be re-evaluated with a stricter protocol before a final decision."

These three parts depend on each other. A recommendation without a findings summary looks arbitrary. A findings summary without an evidence anchor is just a number. An evidence anchor without a recommendation statement leaves the reader unsure what to do [1][2].

![Evidence-based recommendation flow](./diagram.png)

*How rubric scores move through a findings summary table, deciding criteria, evidence anchor, and trade-offs to reach a cited recommendation statement.*

### Translating Scores into Evidence

Rubric scores are your evidence, but a bare score is too thin on its own. A score of 2/4 on accuracy tells the reader a tool underperformed; it does not show what you actually observed. The evidence anchor must do two things: name the **descriptor level** (the written description of what that score means, from your rubric) that matched your observation, and point to a specific moment in your test [2][3].

A reliable format for each piece of cited evidence:

1. State the tool name and the criterion score.
2. Name the descriptor level that matched what you observed.
3. Give a specific example from the test showing why that descriptor applies.

> Example: "Tool B scored 2/4 on accuracy. This matches descriptor level 2 ('Several factual errors are present; a user relying on the output without checking would be misled on at least one point'). In Task 3, Tool B stated that a named AI system was released in 2022; the confirmed release date is 2023."

You do not need to do this for every criterion. Focus on the criteria that drove the conclusion. If Tool A won primarily on functionality and accuracy, those two criteria deserve full evidence citations. Others can be summarised briefly in the findings summary [1].

Before writing any prose, build a **findings summary table** — a five-column table that collects all your scores in one place:

| Criterion | Weight | Tool A score | Tool B score | Difference |
|---|---|---|---|---|
| Functionality | 30% | 4/4 | 2/4 | +2 Tool A |
| Accuracy | 25% | 3/4 | 2/4 | +1 Tool A |
| Privacy | 20% | 3/4 | 3/4 | Tie |
| Accessibility | 15% | 3/4 | 4/4 | +1 Tool B |
| Ethics and Bias | 10% | 3/4 | 3/4 | Tie |
| **Weighted total** | 100% | **3.20/4** | **2.60/4** | **+0.60 Tool A** |

The table does not make the decision — you do. But it makes the decision transparent. Anyone reading your recommendation can verify the totals and trace each number back to the rubric [2].

### Trade-offs and Limitations

**Trade-off** — a criterion where the tool you are not recommending actually scored higher than the one you are recommending. A strong recommendation names these directly, not to weaken the conclusion, but to show you analysed the full picture [2][3].

> Example: "Tool B scored 4/4 on accessibility, compared to Tool A's 3/4. For contexts where the tool will be used by learners with disabilities or on low-bandwidth connections, this difference is significant and should be factored back into the rubric before a final decision."

Readers who notice a lower score will trust your recommendation far more if you address it head-on rather than skip over it [1][2].

**Limitations** are gaps in your test design that might affect the conclusion. Stating them briefly is standard practice in evidence-based reasoning [2][3]. Common ones to name:

- **Test sample size:** "Five test tasks is a starter evaluation. A full review would use a larger, more varied set."
- **Single scorer:** "This rubric was scored by one person. A multi-scorer approach would test whether different evaluators reach the same conclusion."
- **Version and timing:** "Both tools were tested in June 2026. Both are updated regularly; scores may change with new versions."
- **Context specificity:** "The weights reflect a student audience. A professional legal-drafting context would require different weights."

Limitations bound your recommendation — they do not undermine it. Stating them is a sign of honest analysis, not weakness [3].

### Three Common Weaknesses

These patterns appear regularly in first drafts [1][2]:

**Weakness 1 — Vague claims without evidence.** The word "better" alone is not evidence.

| Weak | Stronger |
|---|---|
| "Tool A produced better outputs overall." | "Tool A's outputs required no editing in 4 of 5 tasks; Tool B required editing in all 5." |
| "Tool B felt harder to use." | "Tool B scored 2/4 on accessibility; Task 1 took 8 minutes on Tool B versus 2 minutes on Tool A." |

**Weakness 2 — Unsupported assertions.** A claim not backed by any score or observation.

| Weak | Stronger |
|---|---|
| "Tool B is more ethical." | "Tool B scored 4/4 on Ethics and Bias — no output used exclusionary language in any task, matching descriptor level 4." |

**Weakness 3 — Ignored trade-offs.** If the recommended tool scored lower on a criterion, naming it and explaining why it did not change the conclusion is essential.

| Weak | Stronger |
|---|---|
| "Therefore we recommend Tool A." (when Tool A scored lower on accessibility) | "We recommend Tool A. Tool B outperformed on accessibility (4/4 versus 3/4). If this tool will be used by a population with accessibility needs, that criterion should be reweighted before a final decision." |

## Worked Example

This example takes rubric scores from a completed evaluation and builds a full three-part recommendation, step by step.

**Scenario:** Two AI writing assistants — Tool A and Tool B — were evaluated on a five-criteria rubric (functionality 30%, accuracy 25%, privacy 20%, accessibility 15%, ethics and bias 10%) across five test tasks. Weighted totals: Tool A 3.20/4, Tool B 2.60/4.

**Step 1 — Build the findings summary table** (as shown in Key Concepts above). The table confirms Tool A leads on functionality and accuracy; Tool B leads on accessibility.

**Step 2 — Identify the deciding criteria.** The largest gaps are on functionality (+2 Tool A) and accuracy (+1 Tool A), both high-weighted criteria. These become the evidence anchor.

**Step 3 — Write Part 1 (findings summary):**
> "Using a five-criteria rubric weighted toward accuracy and functionality, Tool A scored 3.20 out of 4 and Tool B scored 2.60 out of 4 across five test tasks."

**Step 4 — Write Part 2 (evidence anchor):**
> "Tool A's lead came from functionality (4/4 versus 2/4) and accuracy (3/4 versus 2/4). On functionality, Tool A completed all five test tasks without error; Tool B failed two tasks entirely, matching descriptor level 2 ('Tool completes fewer than 60% of test tasks'). On accuracy, Tool B produced factual errors in three tasks — in Task 3, it reported an incorrect release date for a named AI system; Tool A's outputs required no factual correction."

**Step 5 — Identify the trade-off:**
Tool B scored 4/4 on accessibility; Tool A scored 3/4.

**Step 6 — Write Part 3 (recommendation statement with trade-off and limitation):**
> "We recommend Tool A for student coursework support. Tool B outperformed on accessibility (4/4 versus 3/4); if this tool will be used by learners with disabilities or on low-bandwidth connections, the accessibility criterion should be reweighted before a final decision. This evaluation used five test tasks scored by one evaluator in June 2026; a larger multi-evaluator review is recommended before any institutional adoption."

**Step 7 — Read aloud and remove opinion language.** Check for "felt," "seemed," "I think," "probably," "better" used without a score. None appear in the above — each claim traces to a rubric score, a descriptor level, or a test observation.

The result is a recommendation that a sceptical reader can follow from conclusion back to evidence without needing to trust the author's judgement [1][2].

## In Practice

The three-part structure — findings summary, evidence anchor, recommendation statement — is not unique to AI evaluation. It appears wherever a structured comparison leads to a decision [3].

**Technology procurement.** A university committee evaluating AI writing tools for student use produces a recommendation document before any purchase. The committee applies a rubric covering privacy, accessibility, accuracy, and academic-integrity risk. Each evaluator scores independently; the group resolves disagreements; the final recommendation follows the same pattern taught here [1][3].

**Research summaries for non-technical audiences.** When a technical team presents findings to a leadership group, the evidence anchor does the critical work: it selects the two or three most important results and explains why they matter, without requiring the audience to interpret a full scoring table [2][3].

**AI tool adoption in 2026.** As AI tools multiply, organisations need documented, auditable justifications for the tools they adopt. A structured recommendation grounded in rubric scores gives decision-makers something they can review, challenge, and revisit if conditions change [1][2].

**Common do/don't:**

- Do build the findings summary table before writing a single sentence of prose.
- Do name the criterion, score, and descriptor level in every evidence statement.
- Do address trade-offs directly — readers who notice a lower score will trust you more if you acknowledge it.
- Do not adjust weights after scoring to favour a tool you already prefer. That is fabrication, not evaluation.
- Do not use opinion language — "felt," "seemed," "I believe" — anywhere in the recommendation.
- Do not present an overall total without identifying which criteria drove it.
- Do not recommend both tools simultaneously. "Both have their strengths" is a deferral, not a recommendation.
- Do not over-claim: "Based on this evaluation, we recommend Tool A for this context" is honest and defensible; "This tool is definitively better" is not [1][2].

## Key Takeaways

- An **evidence-based recommendation** ties every claim to a rubric score, a descriptor match, or a recorded test observation. Opinion language ("felt," "seemed," "probably") is replaced by traceable evidence.
- A well-formed recommendation has three parts in order: **findings summary** (overall scores), **evidence anchor** (the two or three criteria that drove the result, with specific observations), and **recommendation statement** (a clear conclusion with any conditions or trade-offs named).
- **Trade-offs** — criteria where the recommended tool scored lower — must be named, not ignored. Acknowledging them demonstrates honest analysis and makes the recommendation more trustworthy.
- **Limitations** — test sample size, single-evaluator scoring, version and timing — should be stated briefly. They define the boundary of the recommendation; they do not invalidate it.
- The same three-part structure applies in professional contexts: technology procurement, research summaries for non-technical audiences, and AI tool adoption decisions all use findings, evidence anchor, and recommendation statement.

## References

1. ReadWriteThink. *Developing Evidence-Based Arguments — Strategy Guide.* https://www.readwritethink.org/professional-development/strategy-guides/developing-evidence-based-arguments
2. Scribbr. *How to Write Recommendations in Research.* https://www.scribbr.com/dissertation/recommendations-in-research/
3. Public Administration Institute. *Effective Structures for Presenting Research Findings.* https://pubadmin.institute/research-methodologies/effective-structures-presenting-research-findings

---
<!-- nav:bottom:start -->
[⬅ Previous: 4.7 — How to compare two AI tools](../../4-7-how-to-compare-two-ai-tools-designing-a-measurable-evaluatio/artifacts/reading.md)&emsp;·&emsp;[⬆ Table of Contents](../../../../../../../README.md#curriculum-topic-index)&emsp;·&emsp;[Next: 5.1 — Real AI failure cases ➡](../../../../week-5/1-ai-failures-and-why-they-happen/5-1-real-ai-failure-cases-healthcare-misdiagnosis-hiring-bias-de/artifacts/reading.md)
<!-- nav:bottom:end -->
