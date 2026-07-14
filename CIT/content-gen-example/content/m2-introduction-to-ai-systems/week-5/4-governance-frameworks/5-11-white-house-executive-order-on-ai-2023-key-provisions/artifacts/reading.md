<!-- nav:top:start -->
[⬅ Previous: 5.10 — NIST AI Risk Management Framework](../../5-10-nist-ai-risk-management-framework-four-functions-govern-map/artifacts/reading.md)&emsp;·&emsp;[⬆ Table of Contents](../../../../../../../README.md#curriculum-topic-index)&emsp;·&emsp;[Next: 5.12 — India AI governance ➡](../../5-12-india-ai-governance-meity-advisory-guidelines/artifacts/reading.md)
<!-- nav:top:end -->

---

# White House Executive Order on AI (2023) — key provisions

## Overview

In 5.7 you met the EU AI Act, a binding law. In 5.10 you met the NIST AI RMF, voluntary guidance. This topic is a third way a government can act on AI risk: a **US Presidential executive order**. On October 30, 2023, the US President signed one about artificial intelligence, and learning its key provisions shows you what executive action can — and cannot — do.

## Key Concepts

### What an executive order is

Imagine the most senior official in a government wants to act quickly, without waiting for the legislature to pass a new law. In the United States, the President can do this by signing an executive order.

- **Executive order** — a signed, written instruction from the US President that tells **federal agencies** what to do [2].
- **Federal agencies** — the parts of the government that carry out its work, such as the Department of Commerce [2].

Two plain facts make an executive order different from a law:

- **It is not made by the legislature.** A law in the US is passed by Congress. An executive order is signed by the President alone, so it mainly commands the agencies the President controls — it cannot bind private citizens the way a full law can [2].
- **It can be undone by the next President.** Because one President signs it, a later President can cancel it with another order [2]. To **revoke** an order means to cancel it. A law is much harder to undo.

Hold onto those two facts. They are why this order is narrower and more easily reversed than the EU AI Act of 5.7.

### The order itself, and the big picture

The order's formal name is **Executive Order 14110 (EO 14110)**, titled "Safe, Secure, and Trustworthy Development and Use of Artificial Intelligence" [1]. People shorten it to EO 14110 or "the 2023 AI Executive Order."

EO 14110 did not write detailed rules itself. Instead it set goals and gave tasks to federal agencies — telling each one what to produce and by when [1][3]. Think of it as the President assigning homework across the government: NIST gets one assignment, another agency gets another [3].

For a beginner, four key provisions capture the order. The next sections take them one at a time.

### Provision 1 — Safety testing for the most powerful models

This was the order's headline. It focused on the most powerful, general-purpose AI models, which the order called **dual-use foundation models**. **Dual-use** means a thing useful for good purposes could also be misused for serious harm [1].

The order required the companies building these top-tier models to do two things:

- **Run safety tests, including red-team testing** — the deliberate attempt to make a system fail that you met in 5.5 [1].
- **Report the results to the federal government** — share what those safety tests found as the most capable models are built [1].

How can an order require this of private companies, when an order normally cannot bind private citizens? It leaned on an existing law as its legal footing, so the order reached private companies *through* that law, not on its own [1][3]. The order also gave **NIST** (the agency from 5.10) a new job: develop standards and tests for what counts as safe, trustworthy AI, so that "safety testing" means something consistent [1][3].

### Provision 2 — Transparency and reporting

The order pushed for **transparency** — making AI activity visible rather than hidden, the same pillar you met in 5.4 [1]. Two provisions aimed at this:

- **Reporting from frontier developers** — companies training the most powerful models had to report on those efforts and their safety testing [1].
- **Helping people tell AI-generated content apart** — agencies were directed to develop guidance for labeling and detecting AI-made content, so people are less easily deceived [1][3].

The goal was simple: reduce the cases where powerful AI, or its outputs, operate in the dark [1].

### Provision 3 — Civil-rights and equity protections

The order treated AI fairness as a civil-rights matter. **Civil rights** are the basic legal protections that guard people from unfair treatment — for example, in hiring, housing, lending, or policing [1].

You know from 5.3 that biased data can make an AI treat a group unfairly. EO 14110 directed agencies to prevent AI from being used to discriminate in those high-stakes areas, and to use existing anti-discrimination law against AI-driven unfairness [1][3]. This is the fairness and harm-prevention pillars of 5.4, applied through people's legal rights.

### Provision 4 — Governance of the government's own AI use

The last provision pointed inward, at the government itself. The order set out guidance for how federal agencies buy and use AI in their own work — for example, requiring safeguards when an agency uses AI in ways that affect people's rights or safety [1][3].

Why does this matter? Governments are large AI users, not just rule-setters. By governing its own AI use, the federal government aimed to model responsible practice and protect the public from harms caused by government systems [1][3].

### Where EO 14110 sits beside the EU AI Act and the NIST RMF

You have now seen three approaches. The clearest way to hold them is side by side.

![Comparing the EU AI Act, NIST AI RMF, and EO 14110](./diagram.png)
*The three governance approaches compared across four axes: who issues it, who must obey, how easily it is undone, and how far it reaches.*

| | EU AI Act (5.7) | NIST AI RMF (5.10) | EO 14110 (this topic) |
|---|---|---|---|
| What it is | A binding law | Voluntary guidance | A US executive order |
| Who issues it | The European Union | NIST (a US agency) | The US President |
| Who must obey | Anyone in scope, by law | No one — chosen freely | US federal agencies (plus some industry reporting via an existing law) |
| How easily undone | Hard — it's a law | N/A — it's optional | Easy — a later President can revoke it |
| Reach | Broad | As broad as you choose | Narrower — mainly directs the government |

The takeaway: EO 14110 was **stronger than voluntary guidance** (it commanded agencies and required some industry reporting) but **weaker and narrower than a full law** (it mostly steered the government, and could be cancelled by the next President) [1][2][3].

### One important fact: it was reversed

EO 14110 was signed on October 30, 2023, and was revoked in January 2025 by a later administration [1]. Other US executive actions on AI followed after 2023; those exist but are not covered here.

So treat the order's provisions as a *historical, illustrative* example of US executive AI governance — the clearest single case of how a US President can act on AI risk — not as currently-in-force law [1][2].

## Worked Example

Walk through how the order's first provision was meant to work, step by step, for a company building one of the most powerful AI models.

1. **The model is in scope.** The model is general-purpose and could be misused for serious harm, so it counts as a dual-use foundation model the order targets [1].
2. **The company runs safety tests.** This includes red-team testing — deliberately trying to make the model fail or produce harmful output (5.5) [1].
3. **The company reports the results.** It shares what the safety tests found with the federal government, using the existing law that gave the order its legal footing [1][3].
4. **NIST writes the standard.** In parallel, NIST develops the safety-testing standards, so "safety testing" means the same consistent thing across companies (5.10) [1][3].

That chain — scope the model, test it, report, standardize — is the order's headline provision in action.

## In Practice

- **Remember the four provisions in plain words:** test the most powerful models, be transparent, protect civil rights, govern the government's own AI use.
- **Know the one-line difference from the others:** the EU AI Act is a *law*, the NIST RMF is *optional guidance*, and EO 14110 was a *Presidential order* — in between in strength and reach.
- **"Order" does not mean "permanent."** An executive order can be revoked by a later President; this one was. That reversibility is a feature of the tool, not a detail to skip.
- **Same agency, new job.** When you see NIST here, connect it to 5.10 — the President tasked NIST with writing the safety-testing standards.

## Key Takeaways

- An **executive order** is a signed instruction from the US President to federal agencies; it is not a law passed by the legislature, and a later President can revoke it [2].
- **EO 14110** (Oct 30, 2023), "Safe, Secure, and Trustworthy AI," was the United States' main 2023 executive action on AI, directing agencies to act on AI risk [1].
- Its **key provisions** were: safety testing and red-team reporting for the most powerful ("dual-use foundation") models, transparency and reporting rules, civil-rights protections, and guidance for the government's own AI use [1][3].
- It tasked **NIST** (from 5.10) with developing AI safety-testing standards, tying it directly to the framework you just studied [1][3].
- It sits **between** the binding EU AI Act (5.7) and the voluntary NIST RMF (5.10) — stronger than optional guidance, narrower and more reversible than a law — and was revoked in January 2025, so it is studied here as a historical example [1][2].

## References

[1] The White House. *Executive Order 14110: Safe, Secure, and Trustworthy Development and Use of Artificial Intelligence*, October 30, 2023. https://www.federalregister.gov/documents/2023/11/01/2023-24283/safe-secure-and-trustworthy-development-and-use-of-artificial-intelligence
[2] Congressional Research Service. *Highlights of the 2023 Executive Order on Artificial Intelligence*, R47843. https://www.congress.gov/crs-product/R47843
[3] Center for Security and Emerging Technology (CSET), Georgetown University. "EO 14110 on Safe, Secure, and Trustworthy AI — Trackers." https://cset.georgetown.edu/article/eo-14410-on-safe-secure-and-trustworthy-ai-trackers/

---
<!-- nav:bottom:start -->
[⬅ Previous: 5.10 — NIST AI Risk Management Framework](../../5-10-nist-ai-risk-management-framework-four-functions-govern-map/artifacts/reading.md)&emsp;·&emsp;[⬆ Table of Contents](../../../../../../../README.md#curriculum-topic-index)&emsp;·&emsp;[Next: 5.12 — India AI governance ➡](../../5-12-india-ai-governance-meity-advisory-guidelines/artifacts/reading.md)
<!-- nav:bottom:end -->
