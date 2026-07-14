---
topic_id: 5.13
title: Knowing which governance framework applies to your system
position_in_module: 7
generated_at: 2026-06-22T16:10:00Z
resource_count: 3
---

# 1. Knowing which governance framework applies to your system — Topic Corpus

## 2. Prerequisites

This is the closing topic of Week 5. It does not teach a new framework — it pulls together the ones you already met and shows you how to pick the right one for a given system. So it leans on all of them:

- **5.7 EU AI Act — risk tiers** — a binding law, sorted into unacceptable / high / limited / minimal risk.
- **5.10 NIST AI Risk Management Framework** — voluntary US guidance built around Govern, Map, Measure, Manage.
- **5.11 White House Executive Order on AI (2023)** — a US Presidential order directing federal agencies.
- **5.12 India AI governance — MEITY advisory guidelines** — soft government advisories for online platforms.
- **5.4 The four pillars (fairness, transparency, accountability, harm prevention)** — the shared goals every framework above is reaching for.

You do not need any legal or technical background. If you have read 5.1 through 5.12, you are ready.

## 3. Learning Objectives

After this topic, you should be able to:

- Explain why "which framework applies to my system?" is an engineering decision, not just an ethics discussion.
- Use two simple questions — *where does my system operate?* and *what does it do?* — to find the frameworks that apply.
- State that the EU AI Act can apply to you even if you are based outside the EU, because of its **extraterritorial reach** [1].
- Recognize that more than one framework can apply to the same system at the same time — they are **not mutually exclusive**.
- Walk through one concrete example and name the framework(s) that apply to it.

## 4. Introduction

You have spent this week meeting four ways the world governs AI: a binding law (the EU AI Act, 5.7), voluntary guidance (NIST, 5.10), a Presidential order (the 2023 executive order, 5.11), and soft advisories (India's MEITY, 5.12). A fair question now is: *which of these actually applies to the thing I am building?*

Here is the key idea of this topic, and it is the takeaway for the whole week: **knowing which framework applies is part of the engineering job.** It is a design-time decision, like choosing a database or picking a security standard before you write code. Get it wrong and you build the wrong documentation, skip the wrong tests, and leave out the human-oversight controls the rules require [3].

So this topic does not re-teach the four frameworks. It teaches you to *decide* between them, using two plain questions and one worked example.

## 5. Core Concepts

### 5.1 Two questions decide almost everything

You do not need to memorize legal text to figure out which framework applies. Two questions get you most of the way [1][2][3]:

1. **Where does your system operate — whose users does it touch?** This is about **jurisdiction**. **Jurisdiction** means the area a government's rules cover — usually a country or region. The rules of a place can reach your system if your system reaches that place.
2. **What does your system do — how risky is it?** A spam filter and a tool that screens job applicants carry very different stakes. The riskier the use, the heavier the rules (this is the risk-tier idea from 5.7).

Question 1 tells you *which* frameworks are in play. Question 2 tells you *how hard* they bite. Work them in that order.

### 5.2 Question 1 — where does it operate? (jurisdiction-driven applicability)

Match your situation to a framework. These are not exclusive — read all the rows, not just the first that fits:

- **Does your system reach the EU market, or are its outputs used in the EU?** Then the **EU AI Act** (5.7) may apply — and here is the surprising part. The Act has **extraterritorial reach**: it can apply to you *even if you and your company are based outside the EU*, as long as your system is placed on the EU market or its **output is used in the EU** [1]. So a team in another country whose AI produces results that land in front of EU users can still be in scope. This is the single most concrete "does it apply to me?" trigger in the week — do not assume "we're not in Europe" makes the Act irrelevant [1].
- **Are you a US federal agency, or selling AI to one?** Then US **federal guidance** and the kind of direction in the **2023 Executive Order** (5.11) is the relevant lens — that order steered how agencies buy and use AI.
- **Are you operating an online platform in India?** Then India's **MEITY advisories** (5.12) speak to you — labeling and due-diligence expectations for platforms.
- **Do you want a best-practice framework to manage AI risk anywhere, with no law forcing it?** Then the **NIST AI RMF** (5.10) is the voluntary choice — you can adopt it regardless of where you operate.

Notice the pattern: a *place* (or the place your output lands) pulls in a *framework*. The EU AI Act stands out because its reach follows your output, not just your address [1].

### 5.3 Question 2 — what does it do? (risk-tier classification)

Once you know a framework is in play, its strength depends on what your system does. The clearest case is the EU AI Act, because you already know its tiers from 5.7:

- A system in the **unacceptable** tier is banned.
- A system in the **high-risk** tier (hiring, healthcare, law enforcement) is allowed only with documentation, testing, and human oversight.
- A **limited-risk** system (like a chatbot) mainly owes transparency.
- A **minimal-risk** system (a spam filter) carries almost no special rules.

So classification is a two-step move: first confirm a framework applies (Question 1), then place your system in that framework's risk levels to learn how heavy the obligations are (Question 2) [1][2]. The riskier the use, the more you must build in.

### 5.4 Frameworks are not mutually exclusive

A common beginner mistake is to assume exactly one framework applies. It does not work that way. **More than one can apply to the same system at the same time** — they are **not mutually exclusive** [2][3].

A worked example makes this concrete. Imagine a startup based in India builds an AI hiring tool:

- It is an **online service in India**, so the **MEITY advisories** (5.12) about platform due diligence speak to it.
- It is sold to **employers in the EU**, so its **output is used in the EU** — the **EU AI Act** (5.7) applies through extraterritorial reach [1], and because hiring is **high-risk**, the heavy obligations from 5.8 kick in.
- The team also chooses to follow the **NIST AI RMF** (5.10) voluntarily to organize its risk work.

That is three frameworks touching one product — a binding law, an advisory, and a voluntary standard — all at once. Recognizing the overlap *is* the skill this topic teaches.

### 5.5 Why this is an engineering decision, not an ethics seminar

You met the four pillars in 5.4 as ethical goals. This topic is where ethics becomes a build decision. Knowing the applicable framework directly shapes what you must engineer [3]:

- **Documentation.** A high-risk system under the EU AI Act needs written records of how it was built and tested (5.8). That is files you create at design time, not an afterthought.
- **Testing.** The framework tells you what testing to plan — including the red-teaming from 5.5 for the most-watched systems.
- **Human oversight.** High-risk rules require a person who can review and override the AI. That is a feature you architect in, not bolt on later.

So picking the framework is like picking a security standard before you ship: it changes the design. Doing it late means rebuilding. That is why the week's takeaway is that this is *part of the engineering job* — the person who knows which rules apply belongs in the design room, not just the ethics review [3].

### 5.6 Keeping this honest — limits and deferrals

Three honest caveats:

- **The soft frameworks are reversible or changeable.** The 2023 Executive Order (5.11) was an order a later President could revoke — and was revoked; India's MEITY advisories (5.12) are guidance a ministry can revise in days. Treat them as the soft, movable end of the scale, unlike the binding EU AI Act (5.7).
- **"Applies to" is not the same as "fully compliant."** This topic teaches you to spot *which* framework is in scope. The detailed legal compliance procedures and any certification bodies that sign off on conformity are specialist work named here only so you know they exist — they are beyond this beginner topic.
- **When in doubt, get expert help.** Engineers identify the applicable framework; lawyers confirm the fine print. Knowing which framework is in play is exactly what lets you ask the right expert the right question.

## 8. Best Practices

For a beginner, the goal is to run the two questions reliably and remember the overlap rule:

- **Ask "where does it operate?" before "what does it do?"** Jurisdiction picks the frameworks; risk level sets how hard they bite.
- **Never assume "we're not in the EU" lets you off.** If your system's output is used in the EU, the EU AI Act can still apply [1].
- **Expect overlap.** Check every framework against your system, not just the first that fits — they are not mutually exclusive.
- **Decide at design time.** Documentation, testing, and human-oversight requirements all flow from the framework, so settle it before you build, like a security standard.

## 9. Hands-On Exercise

Pick one AI system you have heard of (for example, a chatbot, a loan-scoring tool, or a photo-filter app). Run the two questions on it: (1) *Where does it operate, and could its output reach the EU?* (2) *What does it do, and how risky is that use?* Then write down every framework from 5.7, 5.10, 5.11, and 5.12 that could apply, and one sentence saying why. If you list more than one, you have understood the non-exclusivity point.

## 10. Key Takeaways

- Choosing the applicable governance framework is a **design-time engineering decision**, not just an ethics discussion — it shapes the documentation, testing, and human oversight you must build [3].
- Two questions do most of the work: **where does your system operate / whose users does it touch** (jurisdiction), and **what does it do** (risk level) [1][2].
- The **EU AI Act** has **extraterritorial reach** — it can apply even if you are based outside the EU, as long as your system's output is used in the EU [1].
- Frameworks are **not mutually exclusive**: a single system can fall under a binding law (EU AI Act, 5.7), an advisory (MEITY, 5.12), and a voluntary standard (NIST, 5.10) all at once [2][3].
- The EU AI Act is the binding end of the scale; the Executive Order (5.11) and MEITY advisories (5.12) are the soft, reversible or quickly-changed end, and NIST (5.10) is opt-in anywhere.

## 11. Next Steps

_System-derived from the next entry in curriculum/sequence.md._
