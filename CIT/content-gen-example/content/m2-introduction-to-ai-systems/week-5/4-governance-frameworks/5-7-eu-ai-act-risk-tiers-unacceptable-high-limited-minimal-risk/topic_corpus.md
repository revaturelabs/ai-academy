---
topic_id: 5.7
title: EU AI Act — risk tiers (unacceptable / high / limited / minimal risk)
position_in_module: 1
generated_at: 2026-06-22T08:05:00Z
resource_count: 3
---

# 1. EU AI Act — risk tiers (unacceptable / high / limited / minimal risk) — Topic Corpus

## 2. Prerequisites

This topic builds directly on earlier Week 5 material:

- **5.1 Real AI failure cases** — the hiring, healthcare, and deepfake harms that motivate regulation.
- **5.4 The four pillars (fairness, transparency, accountability, harm prevention)** — the ethical goals this law turns into legal rules.
- **5.5 Red-teaming** — the kind of pre-deployment testing the law requires for its most-watched systems.

You do not need any legal background. If you have read 5.1 through 5.6, you are ready.

## 3. Learning Objectives

After this topic, you should be able to:

- Explain what the EU AI Act (European Union Artificial Intelligence Act) is, in one or two plain sentences.
- Name the four risk tiers — unacceptable, high, limited, and minimal — and order them from most to least dangerous.
- Give a concrete example of an AI system in each tier.
- Describe, at a high level, what the law requires for each tier (from "banned" down to "no special rules").
- Connect the Act back to the four pillars from 5.4 — see how it turns ethics into enforceable law.

## 4. Introduction

In 5.1 you saw AI go wrong in the real world: a hiring tool that downgraded women, AI that misread medical scans, deepfakes that fooled people. Those were not just bad luck. They were harms serious enough that governments decided rules were needed.

The European Union answered with the **EU AI Act (European Union Artificial Intelligence Act)** — the first broad law in the world written specifically to govern artificial intelligence [1][2]. A **regulation** here just means an official, legally binding rule set by a government that organizations must follow.

Here is the one big idea of this topic. The Act does *not* treat every AI system the same way. Instead, it sorts systems by **how much risk they pose to people**, and it applies *heavier rules to higher risk* [1]. That sorting is called the **risk-tier approach**, and it has four levels. Learn those four levels and you understand the heart of this law.

## 5. Core Concepts

### 5.1 What "risk-based" means

The Act's central choice is to be **risk-based**. A chess-playing app and a system that decides who gets hired carry very different stakes. It would be wasteful to regulate the chess app like the hiring system, and dangerous to regulate the hiring system like the chess app.

So the Act asks one question of every AI system: *how much could this harm people if it goes wrong?* The answer places the system into one of four tiers, and the tier decides the rules [1][2]. The higher the risk, the stricter the obligations.

A natural way to picture this is a **pyramid**. A few systems sit at the dangerous top with the most rules; most systems sit at the wide bottom with almost none.

### 5.2 Tier 1 — Unacceptable risk (banned)

At the very top are uses considered such a clear threat to people's safety or rights that they are simply **not allowed at all** [1][2].

Two often-cited examples:

- **Social scoring by governments** — rating citizens by their behavior and then granting or denying them services based on that score.
- **Real-time biometric surveillance in public spaces** (with narrow exceptions). **Biometric** means identifying a person from a body trait such as their face or fingerprint. "Real-time" here means scanning crowds live as people walk by.

These are prohibited because they strike directly at human dignity and freedom. The full list of prohibited uses is its own topic later this week (5.9) — here you only need to know that the top tier means *banned*.

### 5.3 Tier 2 — High risk (heavily regulated)

Just below the banned tier sit **high-risk** systems. These are *allowed*, but only under strict conditions, because they make decisions that seriously affect people's lives or safety [1][3].

Typical high-risk areas:

- **Hiring** — software that screens job applicants (exactly the 5.1 failure case).
- **Healthcare** — AI used in medical diagnosis or treatment decisions.
- **Law enforcement** — tools used by police, such as risk-scoring suspects.
- **Critical infrastructure** — AI controlling things like power or water supply.

What does "heavily regulated" mean in plain terms? Before such a system can be used, its provider must do serious homework [1][3]:

- **Keep documentation** — written records of how the system was built and tested.
- **Test the system** — including the kind of adversarial testing you met as red-teaming in 5.5.
- **Provide human oversight** — a person must be able to review and override the AI's decisions.
- **Pass a conformity assessment.** A **conformity assessment** is an official check, before launch, that the system meets the law's requirements — like a safety inspection a car must pass before it can be sold.

The detailed obligations for high-risk systems are the next topic (5.8); here you only need the headline — high risk means *allowed but tightly controlled*.

### 5.4 Tier 3 — Limited risk (transparency obligations)

Next down are **limited-risk** systems. The main duty here is simple: be honest that AI is involved [1][2]. This is a **transparency** obligation — and transparency is one of the four pillars from 5.4.

Two everyday examples:

- **Chatbots** — if you are talking to an AI, it must tell you so, so you are not fooled into thinking it is a human.
- **Deepfakes** — AI-generated or AI-altered images, audio, or video (the deepfake harm from 5.1) must be **labeled** as artificial.

The rule is light: you can use these systems freely, you just cannot hide that they are AI [2].

### 5.5 Tier 4 — Minimal risk (no mandatory rules)

At the wide bottom of the pyramid sit **minimal-risk** systems — the vast majority of everyday AI [1][2]. Examples include AI spam filters, recommendation features, and AI in video games.

For these, the Act imposes **no mandatory rules**. Providers may follow good practices voluntarily, but the law does not force special obligations. Most AI you use day to day lives here.

### 5.6 The pyramid as a whole

Reading the four tiers top to bottom:

| Tier | Risk level | What the law does | Example |
|---|---|---|---|
| Unacceptable | Highest | Bans it outright | Government social scoring |
| High | High | Allows it under strict obligations | Hiring or healthcare AI |
| Limited | Lower | Requires transparency (disclose it is AI) | Chatbots, labeled deepfakes |
| Minimal | Lowest | No mandatory rules | Spam filter, game AI |

The shape matters: very few systems are banned, a manageable set are high-risk, and most are minimal-risk [1]. The law concentrates its effort where the danger is greatest.

### 5.7 How this connects to the four pillars (5.4)

The Act is essentially the four pillars from 5.4 written into law:

- **Harm prevention** → the unacceptable tier bans the worst harms outright.
- **Accountability and fairness** → the high-risk tier forces documentation, testing, and human oversight, so someone is answerable for fair outcomes.
- **Transparency** → the limited-risk tier forces disclosure that AI is in use.

So the Act does not introduce new ethics. It takes ethics you already know and gives them legal teeth [1][2].

### 5.8 Other governance frameworks (covered in later topics)

The EU AI Act is one framework among several. Other governments and bodies have their own approaches: the NIST AI Risk Management Framework (5.10), the US White House Executive Order on AI (5.11), and India's MEITY advisory guidelines (5.12). Those are separate topics later this week and are not covered here.

## 8. Best Practices

For a beginner, the goal is to *recognize the tiers*, not to apply the law. Useful heuristics:

- **Start from the harm, not the technology.** To guess a system's tier, ask "who gets hurt if this fails, and how badly?" — not "how advanced is the model?"
- **"High-risk" is about the use, not the cleverness.** A simple model used in hiring can be high-risk; a sophisticated model used in a game is minimal-risk.
- **Banned is rare on purpose.** Most AI is minimal-risk. Do not assume every AI system is heavily regulated.
- **Transparency is cheap and almost always wise.** Even when not legally required, telling users they are dealing with AI builds trust (the transparency pillar from 5.4).

## 9. Hands-On Exercise

Make a four-row table with the tiers as rows. For each of these systems, decide which tier you think it belongs to and write one sentence of reasoning: (1) a movie recommender, (2) an AI that scores loan applicants, (3) a customer-service chatbot, (4) a government system that ranks citizens by social behavior. Then re-read section 5.6 and check yourself.

## 10. Key Takeaways

- The **EU AI Act** is the first broad law written to govern AI, and it is **risk-based**: heavier rules apply to higher-risk systems [1].
- There are **four tiers** — unacceptable (banned), high (heavily regulated), limited (transparency required), and minimal (no mandatory rules) [1][2].
- A system's tier is set by **how much it could harm people**, judged by its *use*, not by how advanced the technology is.
- High-risk systems must keep documentation, be tested, provide human oversight, and pass a **conformity assessment** before launch [1][3].
- The Act turns the **four pillars** from 5.4 — fairness, transparency, accountability, harm prevention — into enforceable law [1].

## 11. Next Steps

_System-derived from the next entry in curriculum/sequence.md._
