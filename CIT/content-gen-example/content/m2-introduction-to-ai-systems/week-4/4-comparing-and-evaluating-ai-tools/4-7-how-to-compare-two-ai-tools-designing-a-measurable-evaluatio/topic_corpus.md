---
topic_id: 4.7
title: How to compare two AI tools — designing a measurable evaluation rubric
position_in_module: 1
generated_at: 2026-06-17T00:00:00Z
resource_count: 3
---

# 1. How to Compare Two AI Tools — Designing a Measurable Evaluation Rubric — Topic Corpus

## 2. Prerequisites

This topic builds on vocabulary developed across Module 4. You should be familiar with:

- **4.1 Foundation models** — what an AI model is and the range of tasks it can handle
- **4.4 Agents** and **4.5 Tool use** — AI systems that call external services to extend their capabilities
- **4.6 Multimodal AI** — AI that works with more than one type of input (text, image, audio, video)
- **3.10 How to evaluate AI output across five task types** — an earlier introduction to judging AI output quality

No programming background is assumed. You will not write code in this topic.

## 3. Learning Objectives

By the end of this topic you should be able to:

- Explain what an evaluation rubric is and why it produces more reliable comparisons than personal opinion
- Name at least four criteria that commonly appear in AI tool evaluation rubrics and describe what each one measures
- Distinguish between vague qualitative judgement and measurable, descriptor-anchored criteria
- Design a five-criteria rubric with performance levels and scoring descriptors for comparing two AI tools
- Apply your rubric to a pair of AI tools and produce a defensible, evidence-based conclusion

## 4. Introduction

Imagine two colleagues each try a new AI writing assistant. One says, "I liked Tool A — it felt smarter." The other says, "Tool B was better — it was faster." Both opinions are honest. Neither helps your team decide which tool to actually use.

This is the core problem with informal comparisons: they are personal, hard to repeat, and impossible to defend when someone asks "why?" A rubric solves this problem.

A **rubric** is a scoring guide — a table that lists specific criteria, describes what each level of performance looks like, and assigns a number to each level. Rubrics are common in education (teachers use them to mark essays fairly), and they work equally well for evaluating AI tools.

When you evaluate an AI tool with a rubric, you move from "I think Tool A is better" to "Tool A scored 4/5 on accuracy and 3/5 on privacy; Tool B scored 3/5 on accuracy and 4/5 on privacy — here is the evidence." That shift from opinion to evidence is what makes a comparison defensible [1][2].

This skill feeds directly into your A2 AI Systems Essay (due week 6), where you will need to compare AI tools in writing — backed by evidence.

## 5. Core Concepts

### 5.1 What Is an Evaluation Rubric?

An **evaluation rubric** is a structured scoring guide used to judge something against a fixed set of criteria. Every rubric has three parts [1]:

1. **Criteria** — the specific qualities you are judging (e.g., "accuracy of outputs")
2. **Performance levels** — the range of possible scores for each criterion (e.g., 1 = poor, 2 = acceptable, 3 = good, 4 = excellent)
3. **Descriptors** — plain-language statements that explain what each score means (e.g., "score 3 = outputs are usually correct; occasional minor errors that are easy to spot")

A rubric without descriptors is just a number table. Descriptors are what make scoring consistent — two different people using the same rubric should award the same score because they are matching observations to the same written description.

**Example — one criterion, three levels:**

| Score | Level | Descriptor |
|---|---|---|
| 1 | Poor | Outputs contain frequent factual errors that would mislead a user |
| 2 | Acceptable | Outputs are mostly correct but contain noticeable gaps or vague statements |
| 3 | Excellent | Outputs are accurate, specific, and verifiable against a known source |

### 5.2 Why Use a Rubric Instead of Just Testing the Tool?

Trying an AI tool without a rubric is common. You test it, form an impression, and move on. The problem is that impressions are:

- **Inconsistent** — your mood, the task you chose, and the prompt you wrote all shape the result [2]
- **Not transferable** — another person cannot reproduce your test or check your work
- **Not comparable** — without the same criteria applied to both tools, you are not comparing the same things

A rubric fixes all three problems. Because both tools are scored against the same criteria, at the same levels, with the same descriptors, the comparison is:

- **Repeatable** — someone else can run the same rubric and reach a similar result
- **Transparent** — the scoring is visible, not hidden inside one person's head
- **Defensible** — you can justify each score by pointing to specific evidence [1][3]

### 5.3 Common Criteria for AI Tool Rubrics

A well-designed AI tool rubric typically draws from five broad areas. These are not the only possible criteria, but they appear consistently across practitioner and academic frameworks [1][2][3].

**1. Functionality**

What does the tool actually do, and how well does it do it?

- Does it complete the task you give it (summarise a document, answer a question, generate an image)?
- Is the output relevant to the input?
- Does it handle unusual or edge-case requests without breaking?

**2. Accuracy and Reliability**

How correct are the outputs?

- Are factual claims verifiable against a known source?
- Does the tool give consistent answers to the same question, or does it vary widely?
- Does it acknowledge when it does not know something, or does it invent an answer? Hallucination — introduced in topic 3.9 — is the main risk here.

**3. Privacy and Data Handling**

What happens to the data you give the tool?

- Is your input stored? Is it used to train future versions of the model?
- Does the tool ask for sensitive personal information it does not need?
- Is there a readable privacy policy?

This criterion matters most when the tool will process real student or professional data [1].

**4. Accessibility and Ease of Use**

Can the people who need it actually use it?

- Is the interface clear enough for a first-time user with no training?
- Does it work on the devices your users have (mobile, low-bandwidth connection)?
- Is there language support for non-English speakers?
- Are there accessibility features for users with disabilities (screen reader support, adjustable contrast)?

**5. Ethics and Bias**

Does the tool behave fairly and responsibly?

- Does it produce outputs that favour certain groups over others?
- Does it generate harmful, offensive, or misleading content?
- Is it transparent about being an AI system rather than a human?

These five criteria map directly onto the framework used in academic AI evaluation guides [1][2]. Real-world practitioners sometimes add a sixth criterion — **cost and licensing** — covering whether the tool is free, freemium, or paid, and what the usage limits are [3].

### 5.4 Writing Scoring Levels and Descriptors

Choosing criteria is the first step. Writing clear descriptors is the harder step.

A common scale is 1–4 (an even number forces a decision — there is no neutral middle). Some rubrics use 1–3 or 1–5. The number of levels matters less than the quality of the descriptors.

**Rules for writing good descriptors [3]:**

- Each descriptor must describe *observable behaviour* — something you can see in the tool's output or documentation, not something you have to infer
- Descriptors at adjacent levels must be clearly different — if levels 2 and 3 are hard to tell apart, the rubric is not working
- Use consistent language across criteria so that "level 3" means roughly the same standard everywhere
- Avoid vague words like "good" or "adequate" — replace them with specific statements

**Example — Accuracy criterion, 4-level scale:**

| Score | Descriptor |
|---|---|
| 4 | Every factual claim in the output is correct and can be verified against a reliable source; the tool explicitly flags uncertainty when it exists |
| 3 | Most factual claims are correct; minor errors are present but do not affect the usefulness of the output |
| 2 | Several factual errors are present; a user relying on the output without checking would be misled on at least one point |
| 1 | The output contains major factual errors or fabricated information that could cause significant harm if acted upon |

### 5.5 Weighting Criteria

Not all criteria matter equally in every situation. A rubric can assign **weights** — numbers that reflect how much each criterion contributes to the final score. Weights must sum to 100% [1][3].

**Example — a 5-criterion rubric with weights:**

| Criterion | Weight | Score (1–4) | Weighted Score |
|---|---|---|---|
| Functionality | 30% | 3 | 0.90 |
| Accuracy and Reliability | 25% | 4 | 1.00 |
| Privacy and Data Handling | 20% | 2 | 0.40 |
| Accessibility and Ease of Use | 15% | 3 | 0.45 |
| Ethics and Bias | 10% | 3 | 0.30 |
| **Total** | **100%** | — | **3.05 / 4.00** |

Weights should reflect the real needs of your context. If a tool will process personal health records, Privacy might be weighted at 40%. If a tool is a creative writing assistant for a general audience, Functionality and Accessibility might dominate.

**Critical rule:** Set your weights before you score. Changing weights after scoring to favour a preferred tool is not evaluation — it is a disguised opinion.

### 5.6 Test Protocol — Collecting Comparable Evidence

A rubric scores evidence. Before you can score, you need to collect comparable evidence from both tools. This means running the same set of test tasks on both tools, under the same conditions.

A **test protocol** is a short written description of [2][3]:

- The exact tasks or prompts you will run (e.g., "Ask the tool to summarise this 300-word news article")
- The number of times you will run each task (running once introduces randomness; three runs gives a more representative picture)
- The conditions (same device, same account tier, same time of day)

Even a simple five-task protocol makes your evidence much stronger than a single casual test.

## 6. Implementation

### Designing Your Rubric — Step by Step

Follow this procedure in the lab activity.

1. **Choose two AI tools to compare.** Pick tools you can access and test. They should be broadly comparable — e.g., two AI writing assistants, two AI tutoring chatbots.

2. **Choose 5 criteria.** Start with the five common criteria from section 5.3. You may swap one out if your context makes a different criterion more important — but state your reason.

3. **Assign weights to your criteria.** The five weights must sum to 100%. Think about who will use the tool, for what purpose, and with what data.

4. **Write 3–4 level descriptors for each criterion.** Follow the rules in section 5.4: observable, clearly distinguishable, no vague words. Write descriptors before you test the tools.

5. **Design a test protocol.** List 3–5 specific tasks or prompts you will run on both tools. Same tasks, same order, on both tools.

6. **Run the protocol on both tools.** Record raw outputs — screenshots or copied text — as evidence.

7. **Score each tool on each criterion.** Use only the evidence from step 6. Assign the score whose descriptor best matches what you observed.

8. **Calculate weighted totals.** Multiply each score by its criterion weight; sum across criteria.

9. **Write your findings.** State which tool scored higher and why. Point to specific evidence for every claim. Acknowledge any limitations (e.g., "I only tested three prompts; a larger test might give different results").

## 7. Real-World Patterns

### How Organisations Evaluate AI Tools

Organisations adopting AI tools at scale — universities, hospitals, government agencies, large companies — do not select tools based on vendor demos. They use structured evaluation frameworks that closely resemble the rubric described in this topic [1].

A university technology committee evaluating AI writing tools, for example, might run every candidate tool through criteria covering academic integrity risk, student data privacy, accessibility, and output quality across different subject areas. Each committee member scores independently; then the group compares scores and discusses gaps [1][2].

Practitioners working with AI at the application level also track **evaluation over time**. A tool that scores well in January may score worse in March if the underlying model is updated, its pricing changes, or a privacy incident occurs. Rubrics make re-evaluation tractable — run the same protocol again and compare the new score to the old one [3].

The lab activity for this topic mirrors this process directly: you design the rubric, run the protocol, score two tools, and defend your conclusion — the same sequence a practitioner follows.

## 8. Best Practices

**Do:**

- Write descriptors before you test. If you write them after, you will unconsciously favour the tool you already prefer.
- Use the same prompts on both tools. Different prompts make the comparison meaningless.
- Keep your raw evidence — screenshots, copied outputs. Reviewers (and your essay marker) may ask to see it.
- State your weights and justify them. "I weighted Privacy at 30% because the tool will process student records" is a defensible statement.
- Acknowledge limitations. No five-task test is exhaustive. Be honest about what your rubric does and does not cover.

**Do not:**

- Adjust weights after you have seen the scores.
- Use vague language in descriptors — replace "performs adequately" with a specific statement.
- Rely on a single test run for criteria where randomness matters (accuracy, consistency).
- Compare tools at different pricing tiers without noting it — free version of Tool A versus paid version of Tool B is not a fair comparison.
- Ignore a critically low score because the overall total looks acceptable. A tool that fails on Privacy is not rescued by high scores on Accessibility.

## 9. Hands-On Exercise

**Design your evaluation rubric (starter)**

1. Pick any two AI tools you can access (e.g., two AI chatbots, two AI image generators).
2. Using the five common criteria from section 5.3, assign weights that sum to 100%.
3. Write a 3-level descriptor (poor / acceptable / good) for the Accuracy criterion only.
4. List two specific prompts or tasks you would run on both tools.
5. Share your rubric with a classmate — can they understand your descriptors without your explanation? If not, revise until they can.

You will extend this into a full five-criteria rubric during the class lab session.

## 10. Key Takeaways

- A **rubric** is a scoring guide with criteria, performance levels, and descriptors — it turns a personal opinion about an AI tool into a measurable, defensible comparison.
- Common criteria for AI tool rubrics include **functionality**, **accuracy and reliability**, **privacy and data handling**, **accessibility and ease of use**, and **ethics and bias**.
- **Descriptors** — plain-English statements describing what each score level looks like — are what make a rubric consistent; vague descriptors produce inconsistent scores.
- **Weights** let you reflect what matters most in your context; they must be set before scoring, not adjusted afterward.
- A **test protocol** — the same tasks, same conditions, run on both tools — is what connects your rubric to real evidence.

## 11. Next Steps

_System-derived from the next entry in curriculum/sequence.md._
