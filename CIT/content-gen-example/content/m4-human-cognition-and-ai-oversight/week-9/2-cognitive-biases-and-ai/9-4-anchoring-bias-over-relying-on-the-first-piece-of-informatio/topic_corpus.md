---
topic_id: "9.4"
title: "Anchoring bias — over-relying on the first piece of information received"
position_in_module: 2
generated_at: "2026-06-12T00:00:00Z"
resource_count: 3
---

# 1. Anchoring Bias — Over-Relying on the First Piece of Information Received — Topic Corpus

## 2. Prerequisites

- **9.1 — System 1 thinking:** System 1 is the fast, automatic thinking mode that drives most everyday decisions. Anchoring bias operates largely through System 1.
- **9.2 — System 2 thinking:** System 2 is the slow, deliberate mode that can, in principle, correct System 1 errors — but often fails to correct them fully. The insufficiency of adjustment, covered in this topic, explains why.
- **9.3 — Confirmation bias:** Like confirmation bias, anchoring bias is a cognitive bias that distorts judgment. Knowing that biases are systematic and predictable (not random noise) is assumed from 9.3.

## 3. Learning Objectives

By the end of this topic, you will be able to:

1. **Define** anchoring bias in plain language and identify its two core components: the initial anchor and the adjustment heuristic.
2. **Explain** why the adjustment heuristic consistently produces insufficient adjustment — why people stop adjusting too soon.
3. **Recall** the original Tversky and Kahneman wheel-of-fortune experiment as empirical evidence that anchoring bias is real, measurable, and independent of the relevance of the anchor.
4. **Identify** at least three ways anchoring bias appears in AI-assisted work, including first-pass AI outputs acting as anchors.
5. **Distinguish** anchoring bias from confirmation bias by describing the mechanism that drives each one.
6. **Apply** awareness of anchoring bias to a self-check question: "What number or starting point did I see first, and am I still too close to it?"

## 4. Introduction

Imagine you walk into a market to buy a jacket. The first stall has a sign: "Was $500, now $250." You feel like you are getting a bargain. Two stalls later you find the same jacket for $200 — no sale sign, no drama. It no longer feels like a deal. Why? You were anchored to that $500 price. The first number you saw shaped every price you judged after it.

This is anchoring bias at work. It is the human tendency to give too much weight to the first piece of information received — the "anchor" — and to let it pull all later judgments toward it, even when the anchor is irrelevant, random, or wrong.

Anchoring bias was first documented in a controlled experiment in the 1970s by psychologists Amos Tversky and Daniel Kahneman [1]. In the decades since, researchers have replicated the finding hundreds of times across cultures, ages, professions, and levels of expertise [3]. It is one of the most robust and consistently observed effects in psychology.

Why does this matter for someone working with AI tools? AI systems regularly produce a first output — a number, a draft, a recommendation, a cost estimate. That first output becomes your anchor, whether you intend it to or not. If you then evaluate the output's quality, adjust its number, or make a decision based on it, anchoring bias will pull your judgment back toward whatever the AI said first. Understanding anchoring bias is not just interesting psychology — it is a practical skill for anyone who needs to oversee, evaluate, or act on AI-generated information.

## 5. Core Concepts

### 5.1 What is an anchor?

**Anchor** — the first piece of information you encounter on a topic. It acts as a mental reference point that shapes all estimates and judgments you make afterward.

An anchor can be:

- A number ("the price is usually around $1,000")
- A statement ("this model is roughly 90% accurate")
- A starting value in a negotiation
- The first answer an AI generates when you ask it a question

Once an anchor is set, it is very difficult to ignore. Your brain treats it as a baseline and measures everything else relative to it. If the anchor is high, your estimates tend to be higher than they would otherwise be. If the anchor is low, your estimates tend to be lower.

Key insight: **the anchor does not have to be accurate or even relevant to have this effect.**

In one famous experiment, Tversky and Kahneman spun a wheel-of-fortune rigged to land on either 10 or 65. Participants watched the wheel land, then were asked: "What percentage of African countries are members of the United Nations?" The wheel result was completely unrelated to the question. But participants who saw 65 gave answers averaging around 45%, while participants who saw 10 gave answers averaging around 25% [1]. A random number from a game wheel shifted estimates of a factual world question by 20 percentage points.

### 5.2 The adjustment heuristic

A **heuristic** — as you learned in topic 9.1 — is a mental shortcut. The **adjustment heuristic** is the specific shortcut the brain uses when it has an anchor: you start at the anchor and then adjust away from it until you reach a value that feels acceptable.

The process looks like this:

1. An anchor is received (a number, a statement, a first answer).
2. The brain takes the anchor as the starting point.
3. The brain makes incremental adjustments — nudging the estimate up or down.
4. Adjustment stops when the estimate "feels right."

The problem is that "feels right" arrives too early. People stop adjusting before they have moved far enough from the anchor. This pattern is called **insufficient adjustment**.

### 5.3 Why adjustment is insufficient

Why do we stop too soon? Two reinforcing reasons explain this.

**Reason 1: Adjustment is a System 2 activity — and System 2 is effortful.**

As you learned in topic 9.2, System 2 thinking is cognitively expensive. It requires working memory and deliberate effort, and it fatigues over time. Adjusting away from an anchor means running calculations in your head, questioning your starting point, and actively searching for disconfirming information. That is System 2 work. The moment adjustment "feels plausible," System 2 tends to stop — conserving cognitive resources [1].

**Reason 2: The anchor activates anchor-consistent information in memory.**

Research suggests that anchors do not just set a starting point — they also activate information in memory that is consistent with the anchor [2]. If someone tells you "this software costs around $5,000," your mind retrieves examples and facts that are consistent with expensive enterprise software. That information then feels like evidence your estimate is in the right ballpark — even though the anchor itself triggered that search. You have been steered toward anchor-consistent evidence without realising it.

The result: even people who know they should adjust still end up too close to the anchor. Studies of experts — real-estate agents, financial analysts, experienced negotiators — show the same anchoring effects as novices, just slightly reduced [2]. Expertise narrows the bias; it does not eliminate it.

### 5.4 Anchoring bias is universal and measurable

Large-scale empirical research confirms that anchoring bias is not a rare quirk of a few susceptible individuals. It is a universal feature of human cognition [3].

Key empirical findings:

- Anchoring effects have been replicated across dozens of countries and cultural contexts.
- The effect occurs with arbitrary anchors (like a randomly generated number) just as it does with plausible-sounding ones.
- People with higher education, domain expertise, or explicit warnings about anchoring still show significant anchoring effects — the warning reduces the bias but does not remove it [3].
- The effect is measurable: anchors can shift numerical estimates by 10–35% in typical experiments [3].

This universality matters because it means you cannot simply decide to "not be anchored." You need structural strategies that interrupt the anchoring process before your estimate forms. The Judgment Framework (topics 9.7–9.9) provides one such structure — you will cover it later in this module.

### 5.5 Anchoring bias and System 1

In topic 9.1 you learned that System 1 is automatic: it processes information fast, without deliberate effort, and produces an immediate intuitive response. Anchoring bias is primarily a System 1 effect.

When an anchor arrives, System 1 registers it instantly and begins constructing a mental picture around that anchor. By the time System 2 is asked to evaluate or adjust, System 1 has already shaped the starting point of that evaluation. System 2 is adjusting away from a position that System 1 has already treated as the baseline — not from a neutral, blank-slate starting point.

This is why the anchoring effect is so hard to shake. It is not a failure of intelligence or care. It is a structural feature of how fast and slow thinking interact.

### 5.6 Distinguishing anchoring bias from confirmation bias

You learned about confirmation bias in topic 9.3. Both are cognitive biases, but they operate differently.

| Feature | Confirmation bias | Anchoring bias |
|---|---|---|
| What distorts judgment | Existing beliefs and expectations | The first number or statement encountered |
| When it activates | When searching for or interpreting evidence | When forming an estimate from a starting value |
| Core mechanism | Selective search and biased interpretation | Anchor-and-adjust: stopping too close to the anchor |
| Can a random input trigger it? | No — it requires a prior belief to confirm | Yes — even a random number can anchor an estimate |

Both biases are driven largely by System 1, and both resist System 2 correction — but they are triggered by different inputs and distort reasoning in different ways.

## 6. Worked Example

**Scenario:** You are evaluating a draft report generated by an AI writing assistant.

**Step 1 — The anchor is set.**
You ask the AI to estimate the project budget. It outputs: "Based on similar projects, a budget of approximately $180,000 seems appropriate."
That number — $180,000 — is now your anchor. Your brain registers it as the starting point, even before you have reviewed a single project detail.

**Step 2 — You begin reviewing the project details.**
The project scope is actually smaller than the examples the AI compared it to. You think: "This should probably be less. Maybe $160,000."

**Step 3 — Adjustment stops too soon.**
$160,000 "feels reasonable" — it is lower than the AI's number, so it feels like you have corrected the estimate. You stop adjusting. But if you had started with no anchor and built the estimate from scratch, independent research on similar small projects suggests $95,000–$110,000 is the realistic range.

**Step 4 — The final judgment is biased toward the anchor.**
Your estimate of $160,000 is far higher than the evidence-based range — because the AI's initial output anchored you to a high starting point. You adjusted, but not nearly far enough.

**The mechanism at each step:**

1. AI produces a first output → anchor set automatically (System 1 registers it).
2. You notice the anchor may be wrong → System 2 begins adjustment.
3. Adjustment "feels sufficient" at $160,000 → System 2 stops; insufficient adjustment occurs.
4. Final estimate remains biased toward $180,000 → anchoring bias has distorted the judgment.

**The takeaway:** Reviewing an AI's first output and then forming your own judgment is not the same as forming an independent judgment. The moment you see the AI's number, you have an anchor. Forming your own estimate before looking at the AI's output is one way to reduce this effect.

## 7. Common Misconceptions

**Misconception 1: "I know about anchoring bias, so I won't be affected by it."**

Correction: Awareness reduces the effect slightly, but does not eliminate it [3]. Studies in which participants are explicitly warned about anchoring — and even told the anchor is random and irrelevant — still show significant anchoring effects. The bias operates largely at the System 1 level, below conscious control. Knowing about it gives you a partial advantage, but it must be paired with behavioral strategies (like forming an independent estimate first) to meaningfully reduce the bias.

**Misconception 2: "Anchoring bias only affects people who are not experts in their domain."**

Correction: Domain expertise reduces anchoring bias, but does not eliminate it [2]. Real-estate agents, financial advisors, experienced negotiators, and trained evaluators all show anchoring effects in controlled studies — just modestly smaller ones than non-experts. This is why even skilled professionals who work with AI tools need to actively manage anchoring, not simply trust their expertise to protect them.

**Misconception 3: "An anchor only works if it is a plausible number — random or irrelevant numbers do not count."**

Correction: The original Tversky and Kahneman wheel-of-fortune experiment directly refutes this [1]. A randomly generated number from a game wheel — which participants knew was random — still shifted their estimates by approximately 20 percentage points. Anchoring does not require the anchor to be meaningful, relevant, or credible. The mere act of seeing a number first is enough to bias subsequent estimates.

## 8. Connection to AI Context

Anchoring bias becomes especially relevant — and especially risky — when working with AI tools. Here is why.

### AI outputs arrive first

In most AI-assisted workflows, the AI produces something — a number, a draft, a recommendation — before the human evaluates it. That first output is an anchor, by definition. The human's subsequent judgment is shaped by it, whether or not the human is aware of this.

This is structurally different from situations where humans form an opinion first and then check a tool. When AI outputs come first, the anchor is set before the human has engaged with the underlying evidence.

### Common AI-context anchoring scenarios

| Scenario | What anchors you | Risk |
|---|---|---|
| AI generates a cost, timeline, or score estimate | The AI's number | Your revised estimate stays too close to the AI's figure, even if the evidence points elsewhere |
| AI drafts a summary or report | The AI's framing and word choices | Your edits stay structurally close to the AI's version; deeper flaws are not caught |
| AI states a model's accuracy as "approximately 87%" | The "87%" figure | You use 87% as the baseline even when your test conditions differ significantly |
| AI gives a first recommendation (e.g., risk rating) | The AI's recommendation | You fail to revise sufficiently even when contradicting evidence is found |

### The first-pass anchor

One specific pattern worth naming: the **first-pass anchor**. When an AI generates a first draft or first answer, that output becomes the anchor for every revision cycle that follows. Each revision starts from the AI's starting point, not from a blank slate. Over multiple revision passes, the final output may remain structurally close to the first AI output — not because revisions were careless, but because each round was anchored to the previous version.

For high-stakes documents or decisions, generating two independent AI outputs (with different prompts or starting conditions) and comparing them before forming a judgment can disrupt the single-anchor effect.

### Anchoring and AI-assisted evaluation

When you evaluate an AI system's performance, anchoring bias can distort the evaluation itself. If you are told "this AI achieves about 80% accuracy" before running your own evaluation, your test design — which cases you choose, how you interpret borderline results, when you decide the test is complete — will be anchored to 80% [2].

Later in this module you will encounter the Judgment Framework, which provides a structured set of questions to apply before acting on any AI output. One effect of that framework is to interrupt anchoring by forcing independent reasoning before the AI's first answer is accepted.

## 9. Hands-On / Reflection Prompt

Take a few minutes to answer these questions. There are no right or wrong answers — the goal is to notice your own anchoring patterns.

1. **Recall a recent decision** — at work, in a purchase, or in any evaluation task — where you saw a number or estimate early in the process. Did that first number influence your final answer? Looking back, do you think you adjusted enough, too little, or more than needed?

2. **Imagine this situation:** You ask an AI tool to estimate how long a task will take. It says "approximately 3 hours." You think it will probably take longer. How far from "3 hours" would your revised estimate be? Now imagine you had not seen the AI's estimate — would your independent guess have been the same? What does any gap (or lack of gap) tell you about how anchored you were?

3. **Name one step you could take** before looking at an AI's first output — for a task you do regularly — that would help you form a more independent judgment. Why would that step reduce the anchoring effect?

## 10. Key Vocabulary

| Term | Definition |
|---|---|
| **Anchoring bias** | The tendency to give too much weight to the first piece of information received and to let it pull subsequent judgments toward it, even when that information is wrong or irrelevant. |
| **Anchor** | The first number, statement, or piece of information encountered on a topic; it acts as a mental reference point for all later estimates and decisions. |
| **Adjustment heuristic** | A mental shortcut in which the brain starts at the anchor and makes incremental adjustments up or down until an estimate "feels acceptable." |
| **Insufficient adjustment** | The consistent pattern in which adjustments away from an anchor stop too soon, leaving the final estimate closer to the anchor than the evidence warrants. |
| **Primacy effect** | The general tendency to give more weight to information that arrives first; anchoring bias is one specific expression of the primacy effect in numerical estimation. |
| **System 1 thinking** | Fast, automatic, intuitive thinking (from topic 9.1) — the mode through which the anchor is first registered and treated as a mental baseline. |
| **First-pass anchor** | The first output an AI system produces; because it arrives before the human has formed an independent view, it functions as an anchor for all subsequent evaluation and revision. |
| **Cognitive heuristic** | A mental shortcut that reduces the effort of a decision — useful in many situations but prone to systematic errors (biases) in others. |

## 11. Further Reading

1. Cherry, K. (updated). *What Is the Anchoring Bias?* Simply Psychology. https://www.simplypsychology.org/what-is-the-anchoring-bias.html — Beginner-friendly overview of anchoring bias covering the original Tversky and Kahneman experiments, the adjustment heuristic, and everyday examples.

2. The Decision Lab. *Anchoring Bias.* https://thedecisionlab.com/biases/anchoring-bias — Decision-science perspective on why anchoring persists in real-world settings, with examples from negotiation, pricing, and professional domains, plus practical mitigation strategies.

3. Mannes, A. E., & Moore, D. A. (large-scale empirical study). See also: https://arxiv.org/abs/1911.12275 — Large-scale empirical quantification of anchoring bias effect sizes across multiple domains; demonstrates that the effect is robust even when anchors are random and participants are warned in advance.
