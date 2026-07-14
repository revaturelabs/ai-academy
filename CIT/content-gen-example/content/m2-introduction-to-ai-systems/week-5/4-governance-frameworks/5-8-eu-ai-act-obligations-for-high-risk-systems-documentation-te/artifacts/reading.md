<!-- nav:top:start -->
[⬅ Previous: 5.7 — EU AI Act](../../5-7-eu-ai-act-risk-tiers-unacceptable-high-limited-minimal-risk/artifacts/reading.md)&emsp;·&emsp;[⬆ Table of Contents](../../../../../../../README.md#curriculum-topic-index)&emsp;·&emsp;[Next: 5.9 — EU AI Act ➡](../../5-9-eu-ai-act-prohibited-uses-including-social-scoring-and-real/artifacts/reading.md)
<!-- nav:top:end -->

---

# EU AI Act — obligations for high-risk systems (documentation, testing, human oversight)

## Overview

In 5.7 you met the four risk tiers the **EU AI Act (European Union Artificial Intelligence Act)** uses to sort AI, and you learned that **high-risk** systems are allowed but tightly controlled. This topic explains what "tightly controlled" actually means. The answer is a short, fixed list of duties the law places on these systems before they reach people and while they keep running [1]. Learn that list and you understand the working core of how the Act governs high-risk AI.

## Key Concepts

Think of a high-risk AI system like a car. A car is allowed on the road, but only after it passes safety checks — working brakes, crash testing, and a paper trail proving all of it. High-risk AI works the same way: it is permitted, but its makers must do real safety homework first, and keep doing it afterward [1][2].

### Who has to obey — provider vs deployer

Before the duties, you need to know *who* they fall on. The Act splits responsibility between two roles [2]:

- **Provider** — the organization that **builds** the AI system and puts it on the market under its own name. Example: the company that develops a hiring-screening tool and sells it.
- **Deployer** — the organization that **uses** the system in its own work. Example: the HR department that buys that hiring tool and runs it on real applicants.

Why the split? Because the provider made the system and knows it best, so it carries most of the heavy duties. The deployer carries lighter, use-time duties — mainly using the system as instructed and keeping a human in the loop [2][3].

| Role | Plain meaning | Main responsibility |
|---|---|---|
| Provider | Builds and sells the system | Do the safety homework before launch and document it |
| Deployer | Buys and uses the system | Use it as instructed and keep human oversight running |

### The path to market

The diagram below shows the shape of the whole obligation set: the provider does its safety work, that work must pass an official gate, and only then can the system be sold — after which some duties keep running.

![Path-to-market flow for a high-risk AI system](./diagram.png)
*A high-risk system's journey: provider safety duties → the conformity-assessment gate → placed on market → ongoing duties. Most work happens before launch; some duties continue afterward.*

The official gate in the middle is the **conformity assessment** — a check, *before* the system goes on the market, that it meets all the requirements. A **conformity assessment** is like the safety inspection a car must pass before it can be sold: no pass, no market [1][2].

### The obligations themselves

These are the duties the Act attaches to a high-risk system. The provider sets up most of them before the system is sold [1][2]:

- **Risk management** — an ongoing process to spot and reduce the ways the system could harm people, across its whole life. *Example:* a medical-AI maker keeps asking "where could this misread a scan?" and fixes those weak spots over time.
- **Technical documentation** — a written paper trail describing how the system was built, what data it used, how it was tested, and how it works. *Example:* a folder a regulator could open and follow to understand the whole system.
- **Data governance** — making sure the data used to train and test the system is relevant, as complete as possible, and checked for bias. *Example:* before training a hiring tool, the team checks the data is not skewed against women — the data-bias problem from 5.3.
- **Record-keeping (logging)** — the system automatically keeps **logs**, a running record of what it did and when. *Example:* a loan-scoring system saves each decision so people can later trace why an applicant was rejected.
- **Transparency to deployers** — giving the people who use the system clear instructions on what it does, its limits, and how to run it safely. *Example:* a plain-language guide telling HR staff what the tool can and cannot reliably judge.
- **Human oversight** — designing the system so a person can monitor it and step in or override it when needed. *Example:* a doctor reviews the AI's diagnosis suggestion and can reject it, rather than the AI deciding alone [3].
- **Accuracy, robustness, and cybersecurity** — the system must perform reliably and resist attacks. **Robustness** means the system keeps working sensibly even when conditions are messy or someone tries to trip it up. *Example:* testing the system against the red-teaming attacks from 5.5 to confirm it does not break or leak.

### Why these duties, and why before the market

Notice the pattern: most duties are done *before* the system is sold, then *kept up* while it runs. That ordering is deliberate — the Act tries to catch harm early, at the design stage, instead of reacting after a failure [1]. The conformity assessment is the gate that enforces it; after launch, risk management, logging, and human oversight keep going [2][3].

These duties are not new ethics. They are the four pillars from 5.4 turned into concrete tasks: risk management and robustness serve **harm prevention**; human oversight, documentation, and logging serve **accountability**; clear instructions serve **transparency**; data governance serves **fairness**.

The detailed list of prohibited uses (5.9) and the other governance frameworks — the NIST AI RMF, the US Executive Order on AI, and India's MEITY guidelines — are covered in upcoming topics, not here.

## Worked Example

Take one high-risk system from 5.7: an AI tool that scores loan applicants. Here is how its maker satisfies four of the obligations, and who is responsible for each.

1. **Technical documentation (provider)** — the maker writes up how the tool was built, what applicant data it learned from, and how it was tested, so a regulator could follow it.
2. **Data governance (provider)** — before training, the maker checks the loan-history data is relevant and not skewed against any group, then records that check.
3. **Testing / robustness (provider)** — the maker red-teams the tool, feeding it odd and hostile inputs to confirm it keeps scoring sensibly and does not break.
4. **Human oversight (deployer)** — the bank using the tool keeps a loan officer in the loop, able to review and override any score before a customer is rejected.

The first three fall on the **provider**, who builds the tool. The fourth is a use-time duty the **deployer** runs. Together they show the "before, then ongoing" split: the provider's homework clears the conformity-assessment gate, and oversight continues once the tool is live.

## In Practice

For a beginner, the goal is to *recognize* these obligations, not to apply the law. A few simple heuristics:

- **Match each obligation to a pillar.** If you can name which of the four pillars (5.4) a duty serves, you understand why it exists.
- **Remember "before, then ongoing."** Most duties are done before market entry and then maintained — the conformity assessment is the gate, not the finish line.
- **Provider builds, deployer uses.** When asked who is responsible, ask first whether the duty is about *making* the system (provider) or *using* it (deployer).
- **Testing is not optional theater.** The robustness duty is real work — it is exactly the red-teaming from 5.5 you already met.

## Key Takeaways

- High-risk systems from 5.7 are allowed but carry a fixed set of obligations: risk management, technical documentation, data governance, record-keeping, transparency to deployers, human oversight, and accuracy/robustness/cybersecurity [1][2].
- The **provider** (who builds the system) carries most duties; the **deployer** (who uses it) mainly follows instructions and keeps human oversight running [2][3].
- A **conformity assessment** is an official pre-market check — like a car safety inspection — that the system meets all requirements before it can be sold [1][2].
- **Human oversight** means a person can monitor and override the AI, making the accountability pillar from 5.4 concrete [3].
- Most duties happen *before* the market and are then maintained — the testing/robustness duty is where red-teaming (5.5) fits [1].

## References

1. The EU AI Act: High-Level Summary. <https://artificialintelligenceact.eu/high-level-summary/>
2. EU AI Act — Obligations of Providers of High-Risk AI Systems. <https://artificialintelligenceact.eu/article/16/>
3. European Commission AI Act Service Desk — Human Oversight. <https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-14>

---
<!-- nav:bottom:start -->
[⬅ Previous: 5.7 — EU AI Act](../../5-7-eu-ai-act-risk-tiers-unacceptable-high-limited-minimal-risk/artifacts/reading.md)&emsp;·&emsp;[⬆ Table of Contents](../../../../../../../README.md#curriculum-topic-index)&emsp;·&emsp;[Next: 5.9 — EU AI Act ➡](../../5-9-eu-ai-act-prohibited-uses-including-social-scoring-and-real/artifacts/reading.md)
<!-- nav:bottom:end -->
