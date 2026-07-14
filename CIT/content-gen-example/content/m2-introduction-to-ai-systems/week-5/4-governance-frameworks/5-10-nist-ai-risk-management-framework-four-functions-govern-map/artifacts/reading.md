<!-- nav:top:start -->
[⬅ Previous: 5.9 — EU AI Act](../../5-9-eu-ai-act-prohibited-uses-including-social-scoring-and-real/artifacts/reading.md)&emsp;·&emsp;[⬆ Table of Contents](../../../../../../../README.md#curriculum-topic-index)&emsp;·&emsp;[Next: 5.11 — White House Executive Order on AI (2023) ➡](../../5-11-white-house-executive-order-on-ai-2023-key-provisions/artifacts/reading.md)
<!-- nav:top:end -->

---

# NIST AI Risk Management Framework — four functions: Govern, Map, Measure, Manage

## Overview

In 5.7 you met the EU AI Act — a binding law that sorts AI by risk. A binding law tells you the line you must not cross, but it does not tell you what to actually *do* day to day to keep your AI safe. That routine is what a **framework** gives you. This topic introduces the most widely used one — the **NIST AI Risk Management Framework** — and its four simple jobs: Govern, Map, Measure, and Manage. Learn those four words and you understand the spine of how organizations manage AI risk.

## Key Concepts

### What the AI RMF is, and what "voluntary" means

- **Framework** — a structured, reusable set of steps an organization follows to handle a problem. Here, the problem is AI risk.
- **NIST** — the **National Institute of Standards and Technology**, a US government agency that writes technical standards and guidance (it also defines things like official time and measurement units) [3].
- **AI RMF (AI Risk Management Framework)** — NIST's guide that helps any organization building or using AI to find, understand, reduce, and keep watching the risks AI can create [1]. NIST published version 1.0 in January 2023, working with industry, universities, and the public [1].

One thing to note up front: NIST does not police anyone. It writes guidance and publishes it; organizations then decide for themselves whether to follow it.

The single most important fact about the AI RMF is one word: **voluntary**.

**Voluntary** means no law forces you to use it. An organization adopts the AI RMF because it chooses to, not because a regulator will punish it for ignoring it [3]. That is the sharp contrast with the EU AI Act from 5.7:

| | EU AI Act (5.7) | NIST AI RMF (this topic) |
|---|---|---|
| What it is | A binding law | Voluntary guidance |
| Who issues it | The European Union | NIST, a US agency |
| If you ignore it | You can be penalized | No legal penalty |
| What it tells you | The risk line you must not cross | A routine for managing risk yourself |

So why follow guidance nobody forces on you? Because it is genuinely useful, and because customers, partners, and government buyers increasingly *expect* it. The framework gives everyone a common, trusted vocabulary for talking about AI risk [3]. Saying "we follow the NIST AI RMF" tells a customer something concrete about how carefully you build.

### What "AI risk" means here

Before the four functions make sense, fix what they act on. **Risk** — the chance that something goes wrong, combined with how bad it would be if it did [1]. For AI, that "something going wrong" is exactly the failures you already studied:

- A model that confidently states a falsehood (hallucination, 5.2).
- A model that treats a group unfairly because its training data was skewed (data bias, 5.3).
- The real harms of 5.1 — a misdiagnosis, a biased hiring screen.

The AI RMF's job is to make an organization deal with these possibilities on purpose, in an organized way, instead of hoping they never happen [1].

### The four functions as a continuous loop

NIST organizes the whole job of managing AI risk into **four functions** — a function here just means a group of related activities, a "job to be done" [1][2]. The four are **Govern, Map, Measure, and Manage**.

A useful first picture: three of the functions form a working cycle, and the fourth sits in the middle holding it all together.

![NIST AI RMF as a continuous loop](./diagram.png)
*Govern sits at the center as the cross-cutting function; Map → Measure → Manage repeat as an ongoing loop, not a one-time checklist.*

- **Govern** is the center — the culture, rules, and responsibilities that make the other three actually happen.
- **Map → Measure → Manage** is the working cycle you repeat: first understand the context, then assess the risks, then act on them.

A beginner's trap is to read this as a checklist you finish once. It is not. AI systems and the world around them keep changing — new users, new data, new ways to misuse them. So an organization keeps cycling: Map the context, Measure the risks, Manage them, then loop back and Map again as things change — all the while held together by Govern at the center [1].

### The four functions, one at a time

- **Govern — set up the culture and rules.** Govern puts the right people, policies, and responsibilities in place so managing AI risk is an ongoing habit, not an afterthought [1][2]. It answers: *Who is responsible? What are our rules?* For example, writing down a company policy for how AI may be used, and naming who is accountable when a system causes harm (the accountability pillar from 5.4). Govern **cuts across the other three** — you cannot Map, Measure, or Manage well if no one is responsible and there are no rules. That is why it sits at the center: it is the soil the other three grow in [2].
- **Map — understand the context and spot the risks.** Map is about understanding the situation your AI system lives in, so you can see what could go wrong [1][2]. It answers: *What is this for? Who could it affect? Where might it cause harm?* For example, listing who a hiring tool could help or hurt, and where biased outputs (5.3) might appear. Think of it as drawing the map *before* the journey — you note the cliffs and rough roads so the later steps know where to look [2].
- **Measure — assess and track the risks.** Measure analyzes and tracks the risks you mapped, using tests and numbers wherever possible [1][2]. It answers: *How big is each risk, really? Is the system actually behaving well?* For example, testing whether a system performs equally across different groups, running the adversarial testing you met as **red-teaming** in 5.5, or tracking error rates over time. Measure turns a vague worry ("it might be biased") into evidence ("it is wrong 3 times more often for this group") [1].
- **Manage — act on the risks.** Manage acts on what you measured: reducing the biggest risks first, deciding what to do about the rest, and responding when something goes wrong [1][2]. It answers: *Given what we found, what do we actually do?* For example, retraining a biased model, adding human oversight for high-stakes decisions, or deciding a small risk is acceptable and writing that decision down. Manage is where the framework finally changes the real system [1].

## Worked Example

Suppose your team is building a **résumé-screening tool** that ranks job applicants. Here is one sentence per function, walked through in order.

1. **Govern** — Write down who owns this tool and set one rule: *no candidate is rejected by the AI alone without a human review.* This names responsibility before any code ships.
2. **Map** — Ask who this could hurt. The risk: the tool could quietly favor one group over another if past hiring data was skewed (the data bias of 5.3). You write that risk down so the next step knows to look for it.
3. **Measure** — Test it. You check whether the tool scores equally qualified applicants the same across different groups, and you find it ranks one group lower 3 times more often. Now you have evidence, not a worry.
4. **Manage** — Act on the evidence. You retrain the model on better-balanced data, keep the human-review rule, and write down the decision.

Then you loop back: months later, new applicants arrive and the data shifts, so you **Map** the changed context and run the cycle again. That loop — not a one-time pass — is the whole point.

## In Practice

- **Remember the four words in order: Govern, Map, Measure, Manage.** Map before Measure before Manage; Govern wraps all three.
- **"Voluntary" is not "weak."** Plenty of serious organizations follow the AI RMF by choice because customers and government buyers expect it [3].
- **It is a loop, not a checklist.** If someone treats AI risk as "done" after one pass, that is the mistake the framework is built to prevent.
- **Pair it with the law — do not confuse them.** The EU AI Act (5.7) says what you must not do; the AI RMF helps you do the rest well.
- **It is the four pillars, made practical.** Govern names who is responsible (accountability, 5.4); Map and Measure find harms before users do; Measure tests for the fairness gaps of 5.3; documenting each step makes the organization's choices transparent [1][2].

## Key Takeaways

- The **NIST AI Risk Management Framework (AI RMF)** is voluntary guidance from **NIST** (a US government agency) for finding and reducing the risks AI can create [1][3].
- It is **voluntary** — no law forces it — which contrasts sharply with the EU AI Act (5.7) being binding law; yet it is widely adopted because it is trusted and expected [3].
- Its spine is **four functions: Govern, Map, Measure, Manage** [1][2].
- **Govern** sets culture and ties the rest together; **Map** spots risks; **Measure** assesses them with evidence; **Manage** acts on them [1][2].
- The four functions form a **continuous loop**, not a one-time checklist, because AI systems and their risks keep changing [1].

## References

[1] National Institute of Standards and Technology. *Artificial Intelligence Risk Management Framework (AI RMF 1.0)*, NIST AI 100-1, January 2023. https://nvlpubs.nist.gov/nistpubs/ai/nist.ai.100-1.pdf
[2] NIST AI Resource Center. "AI RMF Core — Govern, Map, Measure, Manage." https://airc.nist.gov/airmf-resources/airmf/5-sec-core/
[3] National Institute of Standards and Technology. "AI Risk Management Framework" (program page). https://www.nist.gov/itl/ai-risk-management-framework

---
<!-- nav:bottom:start -->
[⬅ Previous: 5.9 — EU AI Act](../../5-9-eu-ai-act-prohibited-uses-including-social-scoring-and-real/artifacts/reading.md)&emsp;·&emsp;[⬆ Table of Contents](../../../../../../../README.md#curriculum-topic-index)&emsp;·&emsp;[Next: 5.11 — White House Executive Order on AI (2023) ➡](../../5-11-white-house-executive-order-on-ai-2023-key-provisions/artifacts/reading.md)
<!-- nav:bottom:end -->
