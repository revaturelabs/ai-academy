---
topic_id: 5.11
title: White House Executive Order on AI (2023) — key provisions
position_in_module: 5
generated_at: 2026-06-22T15:05:00Z
resource_count: 3
---

# 1. White House Executive Order on AI (2023) — key provisions — Topic Corpus

## 2. Prerequisites

This topic sits next to the two governance approaches you just met:

- **5.7 EU AI Act — risk tiers** — a binding law from the European Union. This topic is a third approach to set beside it.
- **5.10 NIST AI Risk Management Framework** — voluntary US guidance built around Govern, Map, Measure, Manage. This topic names a new job NIST was given.
- **5.4 The four pillars (fairness, transparency, accountability, harm prevention)** and **5.5 red-teaming** — the goals and the testing method this order leans on.

You do not need any legal or technical background. If you have read 5.1 through 5.10, you are ready.

## 3. Learning Objectives

After this topic, you should be able to:

- State what the 2023 White House Executive Order on AI was, who issued it, and what an executive order is, in plain words.
- List the order's key provisions: safety testing and red-team reporting for the most powerful models, transparency and reporting rules, civil-rights protections, and guidance for how federal agencies use AI.
- Explain how this executive action differs from the EU AI Act (binding law, 5.7) and the NIST AI RMF (voluntary guidance, 5.10).
- Explain why an executive order is narrower and more easily reversed than a law passed by a legislature.
- Recognize the order as a historical example of US executive AI governance, including the fact that it was later revoked.

## 4. Introduction

Imagine the most senior official in a country's government wants to act on a problem quickly, without waiting for the legislature to pass a new law. In the United States, the President can do this by signing an **executive order** — a written, signed instruction that tells the government's own agencies what to do [2]. It is not a law made by Congress; it is a direct command to the part of the government the President runs.

On October 30, 2023, the US President signed exactly such an order about artificial intelligence. Its formal name is **Executive Order 14110**, titled "Safe, Secure, and Trustworthy Development and Use of Artificial Intelligence" [1]. People usually shorten this to **EO 14110** or just "the 2023 AI Executive Order."

Why did this matter? You already know the harms AI can cause — the failures of 5.1, the hallucinations of 5.2, the data bias of 5.3. The EU answered with a binding law (5.7). NIST answered with voluntary guidance (5.10). EO 14110 was the United States' main *executive* answer in 2023: instead of a new law or optional advice, it was the President directing federal agencies to act on AI risk [1][2]. This topic teaches its key provisions.

## 5. Core Concepts

### 5.1 What an executive order is

An **executive order** is a signed, written instruction from the US President that directs **federal agencies** — the parts of the government that carry out its work, such as the Department of Commerce — to do something [2].

Two plain facts make executive orders different from laws:

- **It is not made by the legislature.** A law in the US is passed by Congress. An executive order is signed by the President alone, so it mainly commands the agencies the President controls — it cannot bind private citizens the way a full law can [2].
- **It can be undone by the next President.** Because one President signs it, a later President can cancel ("**revoke**") it with another order [2]. A law is much harder to undo.

Hold onto those two facts. They are why this order is **narrower** and more **reversible** than the EU AI Act of 5.7.

### 5.2 The big picture: directives to federal agencies

EO 14110 did not write detailed rules itself. Instead it set goals and gave **tasks to federal agencies** — telling each one what to produce and by when [1][3]. Think of it as the President assigning homework across the government: NIST gets one assignment, the Department of Commerce another, and so on [3].

Analysts grouped these assignments into several policy areas [3]. For a beginner, four key provisions capture the order. The next sections take them one at a time:

1. Safety testing and red-team reporting for the most powerful models.
2. Transparency and reporting requirements.
3. Civil-rights and equity protections.
4. Guidance for how the federal government itself uses AI.

### 5.3 Provision 1 — Safety testing for the most powerful models

This was the order's headline. It focused on the most powerful, general-purpose AI models — the order called these **dual-use foundation models**. "**Dual-use**" means a thing useful for good purposes could also be misused for serious harm [1].

The order required the companies building these top-tier models to do two things:

- **Run safety tests, including red-team testing** — the deliberate attempt to make a system fail that you met in 5.5 [1].
- **Report the results to the federal government** — share what those safety tests found, as the most capable models are developed [1].

How could an executive order require this of private companies, when an order normally cannot bind private citizens (5.1)? It used an existing law called the **Defense Production Act** — an older law that lets the government require certain reporting from industry on national-security grounds. The order leaned on that law as its legal footing for the reporting requirement [1][3]. You do not need the details of that law; just note the order reached private companies *through* an existing law, not on its own.

Alongside this, the order gave **NIST** (the agency from 5.10) a new job: **develop standards and tests** for what counts as safe, trustworthy AI, so that "safety testing" means something consistent [1][3]. This connects directly back to 5.10 — the same agency, now tasked by the President to write testing standards.

### 5.4 Provision 2 — Transparency and reporting

The order pushed for **transparency** — making AI activity visible rather than hidden, the same pillar you met in 5.4 [1].

In plain terms, two provisions aimed at this idea:

- **Reporting from frontier developers** — companies training the most powerful models had to report on those efforts and their safety testing, as covered above [1].
- **Helping people tell AI-generated content apart** — the order directed agencies to develop guidance for labeling and detecting AI-made content, so people are less easily deceived [1][3].

The goal was straightforward: reduce the cases where powerful AI, or its outputs, operate in the dark [1].

### 5.5 Provision 3 — Civil-rights and equity protections

The order treated AI fairness as a **civil-rights** matter. **Civil rights** are the basic legal protections that guard people from unfair treatment — for example, in hiring, housing, lending, or policing [1].

You already know from 5.3 that biased data can make an AI treat a group unfairly. EO 14110 directed federal agencies to **prevent AI from being used to discriminate**, especially in those high-stakes areas, and to use existing anti-discrimination law against AI-driven unfairness [1][3]. This is the **fairness** and **harm-prevention** pillars of 5.4, applied through the lens of people's legal rights.

### 5.6 Provision 4 — Governance of the government's own AI use

The last key provision pointed inward, at the government itself. The order set out **guidance for how federal agencies buy and use AI** in their own work — for example, requiring safeguards when an agency uses AI in ways that affect people's rights or safety, and pushing agencies to manage that AI responsibly [1][3].

Why does this matter? Governments are large AI users, not just rule-setters. By governing its *own* AI use, the federal government aimed to model responsible practice and protect the public from harms caused by government systems [1][3].

### 5.7 Where EO 14110 sits beside the EU AI Act and the NIST RMF

You have now seen three approaches. The clearest way to hold them is side by side:

| | EU AI Act (5.7) | NIST AI RMF (5.10) | EO 14110 (this topic) |
|---|---|---|---|
| What it is | A binding law | Voluntary guidance | A US executive order |
| Who issues it | The European Union | NIST (a US agency) | The US President |
| Who must obey | Anyone in scope, by law | No one — chosen freely | US federal agencies (plus some industry reporting via an existing law) |
| How easily undone | Hard — it's a law | N/A — it's optional | Easy — a later President can revoke it |
| Reach | Broad | As broad as you choose | Narrower — mainly directs the government |

The takeaway: EO 14110 was **stronger than voluntary guidance** (it commanded agencies and required some industry reporting) but **weaker and narrower than a full law** (it mostly steered the government, and could be cancelled by the next President) [1][2][3].

### 5.8 Context and limitations — and an important fact

Three things keep this topic honest:

- **It was an executive action, not a statute.** Most of its force fell on federal agencies. It could not, by itself, impose broad rules on private citizens the way the EU AI Act can [2].
- **It was reversible — and was reversed.** EO 14110 was signed on October 30, 2023, and was **revoked in January 2025** by a later administration [1]. So treat its provisions as a *historical, illustrative* example of US executive AI governance — the clearest single case of how a US President can act on AI risk — not as currently-in-force law.
- **Later US executive actions followed.** The United States continued to act on AI through other measures after 2023 — these are named here only so you know they exist, and are not covered in this topic.

These limits are exactly why the order is taught as a *case study* in governance, not as a rulebook to follow today.

## 8. Best Practices

For a beginner, the goal is to recognize the order's shape and place, not to recite legal detail. Useful heuristics:

- **Remember the four provisions in plain words:** test the most powerful models, be transparent, protect civil rights, govern the government's own AI use.
- **Know the one-line difference from the others:** the EU AI Act is a *law*, the NIST RMF is *optional guidance*, and EO 14110 was a *Presidential order* — in between in strength and reach.
- **"Order" does not mean "permanent."** An executive order can be revoked by a later President; this one was. That reversibility is a feature of the tool, not a detail to skip.
- **Same agency, new job.** When you see NIST here, connect it to 5.10 — the President tasked NIST with writing the safety-testing standards.

## 10. Key Takeaways

- An **executive order** is a signed instruction from the US President to federal agencies; it is not a law passed by the legislature, and a later President can revoke it [2].
- **EO 14110** (Oct 30, 2023), "Safe, Secure, and Trustworthy AI," was the United States' main 2023 executive action on AI, directing agencies to act on AI risk [1].
- Its **key provisions** were: safety testing and red-team reporting for the most powerful ("dual-use foundation") models, transparency and reporting rules, civil-rights protections, and guidance for the government's own AI use [1][3].
- It tasked **NIST** (from 5.10) with developing AI safety-testing standards, tying it directly to the framework you just studied [1][3].
- It sits **between** the binding EU AI Act (5.7) and the voluntary NIST RMF (5.10) — stronger than optional guidance, narrower and more reversible than a law — and was **revoked in January 2025**, so it is studied here as a historical example of US executive AI governance [1][2].

## 11. Next Steps

_System-derived from the next entry in curriculum/sequence.md._
