---
topic_id: 5.8
title: EU AI Act — obligations for high-risk systems (documentation, testing, human oversight)
position_in_module: 2
generated_at: 2026-06-22T08:10:00Z
resource_count: 3
---

# 1. EU AI Act — obligations for high-risk systems (documentation, testing, human oversight) — Topic Corpus

## 2. Prerequisites

This topic continues directly from the one before it and reuses several Week 5 ideas:

- **5.7 EU AI Act — risk tiers** — you already met the four tiers (unacceptable, high, limited, minimal) and learned that **high-risk** systems are *allowed but tightly controlled*. This topic opens up exactly what "tightly controlled" means.
- **5.4 The four pillars (fairness, transparency, accountability, harm prevention)** — the ethical goals these legal duties enforce.
- **5.5 Red-teaming** — the pre-deployment testing you already practiced; it is exactly the kind of testing the law expects here.

You do not need any legal background. If you have read 5.1 through 5.7, you are ready.

## 3. Learning Objectives

After this topic, you should be able to:

- Recall, from 5.7, that the **high-risk tier** is allowed but tightly controlled, and explain why obligations attach to it.
- Name the main obligations the EU AI Act (European Union Artificial Intelligence Act) places on high-risk systems, each in one plain sentence.
- Give a concrete everyday example for each obligation (documentation, testing, human oversight, and the rest).
- Distinguish a **provider's** duties from a **deployer's** duties at a plain level.
- Explain what a **conformity assessment** is and why it must happen *before* a system reaches the market.

## 4. Introduction

In 5.7 you learned the EU AI Act sorts AI into four risk tiers, and that **high-risk** systems — hiring tools, medical AI, police tools — are allowed only "under strict conditions." We stopped there on purpose. This topic is where those strict conditions get explained.

Think of it like a car. A car is allowed on the road, but only after it passes safety checks: working brakes, seatbelts, crash testing, and a paper trail proving all of it. High-risk AI is the same idea. It is permitted, but its makers must do real safety homework first, and keep doing it afterward [1][2].

Here is the one big question this topic answers: *if you build or use a high-risk AI system, what does the law actually make you do?* The answer is a short list of obligations. Learn that list and you understand the working core of the EU AI Act.

## 5. Core Concepts

### 5.1 Who has to obey — provider vs deployer

Before the obligations, you need to know *who* they fall on. The Act splits responsibility between two roles [2]:

- **Provider** — the organization that **builds** the AI system (or has it built) and puts it on the market under its own name. Think of the company that develops a hiring-screening tool and sells it.
- **Deployer** — the organization that **uses** the system in its own work. Think of the HR department that buys that hiring tool and runs it on real applicants.

The provider carries most of the heavy obligations, because they made the system and know it best. The deployer carries lighter, use-time duties — chiefly using the system as instructed and keeping a human in the loop [2][3]. A simple way to remember it:

| Role | Plain meaning | Main responsibility |
|---|---|---|
| Provider | Builds and sells the system | Do the safety homework before launch and document it |
| Deployer | Buys and uses the system | Use it as instructed and keep human oversight running |

### 5.2 The obligations on high-risk systems

These are the duties the Act attaches to a high-risk system. Each one is defined here in plain language with a concrete example. The provider is responsible for setting most of these up before the system is sold [1][2].

- **Risk management** — keep an ongoing process to spot and reduce the ways the system could harm people, across its whole life. *Example:* a medical-AI maker repeatedly asks "where could this misread a scan?" and fixes those weak spots, not just once but as the system keeps running.
- **Technical documentation** — written records describing how the system was built, what data it used, how it was tested, and how it works. ("**Technical documentation**" simply means this written paper trail.) *Example:* a folder a regulator could open and follow to understand the whole system.
- **Data governance** — make sure the data used to train and test the system is relevant, as complete as possible, and checked for bias. *Example:* before training a hiring tool, the team checks the data is not skewed against women — the data-bias problem you saw in 5.3.
- **Record-keeping (logging)** — the system automatically keeps **logs**, a running record of what it did and when. *Example:* a loan-scoring system saves each decision it made, so people can later trace why a particular applicant was rejected.
- **Transparency to deployers** — give the people who use the system clear instructions on what it does, its limits, and how to run it safely. *Example:* the hiring-tool maker ships a plain-language guide telling HR staff what the tool can and cannot reliably judge.
- **Human oversight** — design the system so a person can understand it, monitor it, and step in or override it when needed. *Example:* a doctor can review the AI's diagnosis suggestion and reject it, rather than the AI deciding alone [3]. This is the **accountability** pillar from 5.4 made concrete — a human stays answerable.
- **Accuracy, robustness, and cybersecurity** — the system must perform reliably, hold up against unusual or hostile inputs, and resist attacks. **Robustness** means the system keeps working sensibly even when conditions are messy or someone tries to trip it up. *Example:* testing a system against the **red-teaming** attacks from 5.5 — including the prompt-injection tricks from 5.6 — to confirm it does not break or leak.
- **Conformity assessment** — an official check, *before* the system goes on the market, that it meets all the requirements above. A **conformity assessment** is like the safety inspection a car must pass before it can be sold; only after passing can the system be placed on the market [1][2].

### 5.3 Why these obligations, and why before the market

Notice the pattern: most duties must be done *before* the system is sold or used, and then *kept up* while it runs. That ordering is deliberate. The Act tries to catch harm early — at the design stage — instead of waiting for a failure like the ones in 5.1 and then reacting [1].

The conformity assessment is the gate. A provider does the risk management, documentation, data, and testing work, then must pass that check *before* placing the system on the market. No pass, no market. After launch, risk management, logging, and human oversight keep going [2][3].

### 5.4 How this connects to the four pillars (5.4) and to testing (5.5)

These obligations are not new ethics — they are the four pillars from 5.4 turned into concrete tasks:

- **Harm prevention** → risk management and the accuracy/robustness duties.
- **Accountability** → human oversight, documentation, and logging, so someone can be held answerable.
- **Transparency** → clear instructions to deployers and an honest record of how the system works.
- **Fairness** → data governance that checks training data for bias.

And the testing obligation is exactly where **red-teaming (5.5)** lives: deliberately attacking your own system before deployment is how a provider earns the "robustness" and "accuracy" parts of the law.

### 5.5 Boundaries — what is covered elsewhere

To keep this topic focused, a few neighboring subjects are handled in their own topics and are *not* covered here:

- The detailed list of prohibited (unacceptable-risk) uses is 5.9.
- Other governance frameworks are separate topics: the NIST AI Risk Management Framework is 5.10, the US White House Executive Order on AI is 5.11, and India's MEITY advisory guidelines are 5.12.

## 8. Best Practices

For a beginner, the aim is to *recognize* these obligations, not to apply the law. A few heuristics:

- **Match each obligation to a pillar.** If you can say which of the four pillars (5.4) an obligation serves, you understand why it exists.
- **Remember "before, then ongoing."** Most duties are done before market entry and then maintained — the conformity assessment is the gate, not the finish line.
- **Provider builds, deployer uses.** When asked who is responsible, ask first whether the duty is about *making* the system (provider) or *using* it (deployer).
- **Testing is not optional theater.** The robustness obligation is real work — it is exactly the red-teaming (5.5) you already met.

## 9. Hands-On Exercise

Pick one high-risk system from 5.7 (for example, an AI tool that scores loan applicants). Write down, in one sentence each, how its maker would satisfy four of the obligations from section 5.2: documentation, data governance, human oversight, and testing/robustness. Then mark which of those duties fall on the **provider** and which the **deployer** would handle.

## 10. Key Takeaways

- High-risk systems from 5.7 are allowed but carry a fixed set of **obligations**: risk management, technical documentation, data governance, record-keeping, transparency to deployers, human oversight, accuracy/robustness/cybersecurity, and a conformity assessment [1][2].
- The **provider** (who builds the system) carries most duties; the **deployer** (who uses it) mainly follows instructions and keeps human oversight running [2][3].
- A **conformity assessment** is an official pre-market check — like a car safety inspection — that the system meets all requirements before it can be sold [1][2].
- **Human oversight** means a person can monitor and override the AI, making the accountability pillar from 5.4 concrete [3].
- The **testing/robustness** obligation is where **red-teaming (5.5)** fits: providers attack their own systems before launch to prove they hold up [1].

## 11. Next Steps

_System-derived from the next entry in curriculum/sequence.md._
