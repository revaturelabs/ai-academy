---
topic_id: 5.10
title: NIST AI Risk Management Framework — four functions: Govern, Map, Measure, Manage
position_in_module: 4
generated_at: 2026-06-22T14:20:00Z
resource_count: 3
---

# 1. NIST AI Risk Management Framework — four functions: Govern, Map, Measure, Manage — Topic Corpus

## 2. Prerequisites

This topic builds directly on earlier Week 5 material:

- **5.7 EU AI Act — risk tiers** — your first look at how a government turns AI risk into rules. This topic introduces a second, very different framework to set beside it.
- **5.4 The four pillars (fairness, transparency, accountability, harm prevention)** — the ethical goals the framework helps an organization protect.
- **5.1 Real AI failure cases** and **5.2/5.3 hallucination and data bias** — the kinds of harm the framework is meant to catch before they reach users.

You do not need any legal or technical background. If you have read 5.1 through 5.9, you are ready.

## 3. Learning Objectives

After this topic, you should be able to:

- Explain what the NIST AI Risk Management Framework (AI RMF) is, and who publishes it, in one or two plain sentences.
- Explain what "voluntary" means here, and contrast it with the EU AI Act being binding law (from 5.7).
- Name the four functions — Govern, Map, Measure, Manage — and say in plain words what each one does.
- Describe how the four functions work together as an ongoing loop rather than a one-time checklist.
- Recognize why so many companies and government agencies adopt a voluntary framework even when no law forces them to.

## 4. Introduction

In 5.7 you met the EU AI Act: a binding law that sorts AI by risk and forces rules on the riskiest systems. A **binding law** is a rule you can be penalized for breaking. But what should an organization actually *do*, day to day, to keep its AI from causing the harms you saw in 5.1, 5.2, and 5.3? A risk law tells you the line you must not cross. It does not hand you a routine for staying safe.

That routine is what a **framework** gives you. A **framework** is a structured, reusable set of steps an organization follows to handle a problem — here, the problem of AI risk. The most widely used one is the **NIST AI Risk Management Framework (AI RMF)**, published in 2023 [1].

**NIST** stands for the **National Institute of Standards and Technology** — a US government agency that writes technical standards and guidance (it also defines things like official time and measurement units) [3]. NIST does not police anyone. It publishes guidance that organizations choose to follow. The heart of its AI guidance is **four functions: Govern, Map, Measure, and Manage** [1][2]. Learn those four words and you understand the spine of this framework.

## 5. Core Concepts

### 5.1 What the AI RMF is, and what "voluntary" means

The **AI RMF** is a guide that helps any organization building or using AI to find, understand, reduce, and keep watching the risks that AI can create [1]. NIST published version 1.0 in January 2023, working with industry, universities, and the public [1][3].

The single most important fact about it is one word: **voluntary**.

**Voluntary** means no law forces you to use it. An organization adopts the AI RMF because it chooses to, not because a regulator will punish it for ignoring it [3]. This is the sharp contrast with the EU AI Act from 5.7:

| | EU AI Act (5.7) | NIST AI RMF (this topic) |
|---|---|---|
| What it is | A binding law | Voluntary guidance |
| Who issues it | The European Union | NIST, a US government agency |
| If you ignore it | You can be penalized | No legal penalty |
| What it tells you | The risk line you must not cross | A routine for managing risk yourself |

So why follow guidance that nobody forces on you? Because it is genuinely useful, and because customers, partners, and government buyers increasingly *expect* it. The framework is widely adopted across enterprise companies and government agencies precisely because it gives a common, trusted vocabulary for talking about AI risk [3]. Saying "we follow the NIST AI RMF" tells a customer something concrete about how carefully you build.

### 5.2 What "AI risk" means here

Before the four functions make sense, fix what they act on. **Risk** is the chance that something goes wrong, combined with how bad it would be if it did [1].

For AI, that "something going wrong" is exactly the failures you already studied:

- A model that confidently states a falsehood (hallucination, 5.2).
- A model that treats a group unfairly because its training data was skewed (data bias, 5.3).
- The real harms of 5.1 — a misdiagnosis, a biased hiring screen.

The AI RMF's job is to make an organization deal with these possibilities on purpose, in an organized way, instead of hoping they never happen [1].

### 5.3 The four functions — the spine of the framework

NIST organizes the whole job of managing AI risk into **four functions**. A **function** here just means a group of related activities — a "job to be done" [1][2]. The four are **Govern, Map, Measure, and Manage**.

A useful first picture: three of the functions form a working cycle, and the fourth sits in the middle holding it all together.

- **Govern** is the center — the culture, rules, and responsibilities that make the other three actually happen.
- **Map → Measure → Manage** is the working cycle you repeat: first understand the context, then assess the risks, then act on them.

The next sections take each in turn.

### 5.4 Govern — set up the culture and rules

**Govern** is about putting the right people, policies, and responsibilities in place so that managing AI risk is a real, ongoing habit — not an afterthought [1][2].

In plain terms, Govern answers: *Who is responsible? What are our rules? How do we make sure they are followed?* Concrete examples:

- Writing down a company policy for how AI may and may not be used.
- Naming who is accountable when an AI system causes harm (the **accountability** pillar from 5.4).
- Training staff so they know the risks and their duties.

Govern is special because it **cuts across the other three functions** [1]. You cannot Map, Measure, or Manage well if no one is responsible and there are no rules. That is why it sits at the center: it is the soil the other three grow in [2].

### 5.5 Map — understand the context and spot the risks

**Map** is about understanding the situation your AI system lives in, so you can see what could go wrong [1][2].

Mapping answers: *What is this system for? Who could it affect? Where might it cause harm?* Examples:

- Writing down what the system is supposed to do, and where it will be used.
- Listing who could be helped or hurt by it — users, bystanders, specific groups.
- Spotting likely failure points, such as the chance of biased outputs (5.3) for a hiring tool.

You can think of Map as drawing the map *before* the journey: you note the cliffs and the rough roads so the later steps know where to look [2]. Skip it, and you measure the wrong things and manage risks you never noticed.

### 5.6 Measure — assess and track the risks

**Measure** is about analyzing and tracking the risks you mapped, using tests and numbers wherever you can [1][2].

Measuring answers: *How big is each risk, really? Is the system actually behaving well?* Examples:

- Testing whether the system performs equally well across different groups of people (checking for the bias from 5.3).
- Running the adversarial testing you met as **red-teaming** in 5.5 to probe for failures on purpose.
- Tracking error rates over time, not just once at launch.

Measure turns a vague worry ("it might be biased") into evidence ("it is wrong 3 times more often for this group"). Without measurement, Manage is just guessing [1].

### 5.7 Manage — act on the risks

**Manage** is about acting on what you measured: reducing the biggest risks first, deciding what to do about the rest, and responding when something goes wrong [1][2].

Managing answers: *Given what we found, what do we actually do?* Examples:

- Fixing or retraining a model that the Measure step showed to be biased.
- Adding human oversight so a person reviews high-stakes AI decisions.
- Deciding a risk is small enough to accept and watch — and writing that decision down.
- Having a plan ready for when a system fails in use.

Manage is where the framework finally changes the real system. Map and Measure produce understanding; Manage produces action [1].

### 5.8 The four functions as a continuous loop

A beginner's trap is to read Govern → Map → Measure → Manage as a checklist you finish once. It is not. It is a **continuous loop** [1][2].

AI systems and the world around them keep changing — new users, new data, new ways to misuse them. So an organization keeps cycling: Map the context, Measure the risks, Manage them, then loop back and Map again as things change — all the while held together by Govern at the center [1].

Here is the whole framework in one table:

| Function | One-line job | Plain question it answers |
|---|---|---|
| **Govern** | Set culture, rules, responsibilities (and tie the rest together) | Who is responsible, and what are our rules? |
| **Map** | Understand context and spot risks | What is this for, and what could go wrong? |
| **Measure** | Assess and track the risks | How big is each risk, with evidence? |
| **Manage** | Act on the risks | What do we actually do about them? |

### 5.9 How this connects back to the pillars (5.4)

The AI RMF is, in effect, a practical routine for living out the four pillars from 5.4:

- **Accountability** → Govern names who is responsible.
- **Harm prevention** → Map and Measure find harms before users do.
- **Fairness** → Measure tests for the bias of 5.3; Manage fixes it.
- **Transparency** → documenting each step makes the organization's choices visible.

So nothing here is brand-new ethics. It is the four pillars you already know, turned into a repeatable four-step work routine [1][2].

## 8. Best Practices

For a beginner, the goal is to *recognize what each function is for*, not to run a full risk program. Useful heuristics:

- **Remember the four words in order: Govern, Map, Measure, Manage.** Map before Measure before Manage; Govern wraps all three.
- **"Voluntary" is not "weak."** Plenty of serious organizations follow the AI RMF by choice because customers and government buyers expect it.
- **It is a loop, not a checklist.** If someone treats AI risk as "done" after one pass, that is the mistake the framework is built to prevent.
- **Pair it with the law, do not confuse them.** The EU AI Act (5.7) says what you must not do; the AI RMF helps you do the rest well. They fit together.

## 9. Hands-On Exercise

Pick one AI system you know — say, a chatbot or a hiring screener. Write one sentence for each function: (1) **Govern** — who should be responsible and what one rule would you set? (2) **Map** — who could this system hurt? (3) **Measure** — what one thing would you test? (4) **Manage** — what would you do if the test came back bad? Then re-read section 5.8 and check that your four sentences flow as a loop.

## 10. Key Takeaways

- The **NIST AI Risk Management Framework (AI RMF)** is voluntary guidance from **NIST** (a US government agency) for finding and reducing the risks AI can create [1][3].
- It is **voluntary** — no law forces it — which contrasts sharply with the EU AI Act (5.7) being **binding law**; yet it is widely adopted across enterprise and government because it is trusted and expected [3].
- Its spine is **four functions: Govern, Map, Measure, Manage** [1][2].
- **Govern** sets culture and responsibilities and ties the rest together; **Map** understands context and spots risks; **Measure** assesses them with evidence; **Manage** acts on them [1][2].
- The four functions form a **continuous loop**, not a one-time checklist, because AI systems and their risks keep changing [1].

## 11. Next Steps

_System-derived from the next entry in curriculum/sequence.md._
