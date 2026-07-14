---
topic_id: 5.5
title: Red-teaming — systematically testing your own system for failure before deployment
position_in_module: 1
generated_at: 2026-06-22T07:10:00Z
resource_count: 3
---

# 1. Red-teaming — systematically testing your own system for failure before deployment — Topic Corpus

## 2. Prerequisites

This topic builds directly on the earlier safety topics in this week:

- **5.1 Real AI failure cases** — the kinds of harm (healthcare misdiagnosis, hiring bias, deepfake harm) that red-teaming tries to catch before they reach real users.
- **5.2 Hallucination** — one specific failure (the AI stating falsehoods confidently) that a red team deliberately tries to trigger.
- **5.3 Data bias** — biased training data producing biased output, another failure a red team hunts for.
- **5.4 The four pillars** — especially **harm prevention**. Red-teaming is the hands-on testing that the harm-prevention pillar asks for.

## 3. Learning Objectives

After this topic you should be able to:

- Explain in plain language what AI red-teaming is and why a team tests its own system on purpose.
- Describe why this adversarial testing happens *before* deployment, not after.
- Name who typically does red-teaming and the three points in time when it happens.
- List the main categories of attacks and failures a red team probes for.
- Connect red-teaming back to the harm-prevention pillar and to the real failures from topics 5.1–5.3.

## 4. Introduction

Imagine you built a banking app and, the day before launch, you hired a locksmith to *try to break in*. Not because you want them to succeed — but because you would rather they find the broken lock than a thief find it. That is the whole idea behind red-teaming.

**Red-teaming** in AI means deliberately attacking your own AI system to find its weaknesses before real users — or real attackers — do [1]. You play the role of the "bad guy" against your own product. Every failure you find in your own test is a failure a real person will *not* run into after launch.

In topic 5.4 you met the four pillars of responsible AI, and the last pillar was **harm prevention**. That pillar said you must actively look for harm before it happens. Red-teaming is exactly how you do that looking — it is the proactive testing harm prevention requires.

## 5. Core Concepts

### 5.1 What "red team" means

The name comes from military and cybersecurity practice. A **red team** is a group that pretends to be the enemy and attacks a system, while the **blue team** is the group that builds and defends it [1]. In AI, the red team's job is to make the AI behave badly on purpose, so the builders can fix it.

- **Adversarial** — a word you will see a lot here. It simply means "acting like an opponent who is trying to make something go wrong." An adversarial test is a test designed to break your system, not to confirm it works.

Why test adversarially instead of just running normal checks? Because normal testing asks "does it work when used correctly?" Red-teaming asks the harder question: "what happens when someone uses it *incorrectly*, or tries to trick it?" Real users — and real attackers — do not stay inside the lines.

### 5.2 Why test your own system for failure before deployment

**Deployment** means releasing your system so real people can use it. Once a system is deployed, every weakness is now a live risk to real users [3].

Think back to topic 5.1. A diagnostic AI that misdiagnoses, a hiring tool that is biased, a model that produces a harmful deepfake — those were failures that reached the real world. Red-teaming is the step that could have caught each of them in a test lab instead of in the news.

The core logic is simple:

1. Failures found in testing cost you a fix.
2. Failures found after launch cost real harm to real people — and the loss of trust that follows.

So you spend effort finding failures yourself, on purpose, while it is still cheap and private to fix them.

### 5.3 Who does red-teaming

Red-teaming is usually a mix of people and tools, not a single role [1][2]:

- **Internal security and AI engineers** — the team that built the system, now deliberately attacking it.
- **Dedicated red-team specialists** — people whose whole job is finding ways to break AI systems.
- **Automated tools** — open-source and commercial tools that fire thousands of adversarial inputs at the system automatically, far faster than a human could type them [2].

A key rule: the people attacking should think differently from the people who built it. If you only test the situations you already imagined, you only find the problems you already expected. Fresh, adversarial eyes find the surprises.

### 5.4 When red-teaming happens (the testing timeline)

Red-teaming is not a one-time event you do once and forget. It happens at three points in time [3]:

| When | Why test then |
|---|---|
| **Before deployment** | Catch failures before any real user can hit them. This is the main gate. |
| **After updates** | A new model version or a changed prompt can quietly break something that used to be safe. Re-test. |
| **Ongoing** | New attack tricks are invented all the time. A system safe last month may be vulnerable today, so testing continues for the life of the system. |

The big idea: an AI system is never "tested once and done." Because the system changes and the attacks change, red-teaming is a repeating activity.

### 5.5 What red teams probe for (categories of attacks and failures)

A red team works through a checklist of known ways AI systems fail. The main categories are [1][2]:

- **Jailbreaks** — A **jailbreak** is an input crafted to make the AI ignore its own safety rules and do something it was told not to do (for example, being talked into giving dangerous instructions). The red team tries many phrasings to see if any get past the guardrails.
- **Harmful outputs** — getting the system to produce content that is hateful, dangerous, or otherwise damaging. This connects straight back to the **harm prevention** pillar from 5.4.
- **Data leakage** — **Data leakage** is when the AI accidentally reveals private or sensitive information it should have kept secret, such as another user's data or internal instructions.
- **Data poisoning** — **Data poisoning** is when an attacker sneaks bad examples into the data the model learns from, so the model learns the wrong thing on purpose. A red team checks how exposed the system is to this.
- **Triggering known failures** — deliberately trying to make the AI hallucinate (5.2) or produce biased output (5.3), to measure how often it happens.
- **Prompt injection** — one more attack class a red team probes; you will cover this in detail next, in topic 5.6.

Notice that the red team is not inventing brand-new dangers. It is systematically going through the failure types you already met in 5.1–5.3, plus a few attacker-driven ones, and checking each against the actual system.

## 6. Implementation

Here is the repeating loop a red team follows. You do not need code to understand it — it is the same shape as the locksmith story.

1. **Plan** — pick which failure categories to test for (jailbreaks, harmful outputs, data leakage, and so on).
2. **Attack** — feed the system adversarial inputs, by hand or with automated tools, trying to make it fail [2].
3. **Find** — record every input that produced a bad result. Each one is a discovered weakness.
4. **Fix** — the building team patches the weakness (for example, tightens a guardrail or filters an input).
5. **Re-test (regression test)** — run the same attacks again to confirm the fix worked *and* did not break anything else. A **regression test** is a repeat of earlier tests to make sure a change did not bring back an old problem.

Steps 2 through 5 repeat. Each pass should leave fewer failures than the last. This loop is why a single round of red-teaming is rarely enough.

## 7. Real-World Patterns

In practice, teams rarely test by hand alone. Open-source and commercial red-teaming tools let you describe your AI application once, then automatically generate and fire large batches of adversarial inputs at it, scoring which ones broke through [2]. This turns "a few people typing tricky prompts" into "thousands of attacks run overnight."

Red-teaming is also increasingly an expectation, not just a nice-to-have. Some published risk-management guidance — for example, NIST AI 600-1 — recommends red-teaming for AI systems as part of responsible practice [3]. You will meet the governance frameworks that say things like this later in this week; for now, just note that "test your own system adversarially" is becoming a documented standard, not only good advice.

## 8. Best Practices

- **Do** test before launch, after every meaningful update, and on an ongoing basis — not once [3].
- **Do** bring in people who did not build the system, so they are not blind to its assumptions.
- **Do** treat every found failure as a win — that is the entire point of the exercise.
- **Don't** stop after one round; re-test after each fix to catch anything you broke (regression testing).
- **Don't** confuse normal "does it work?" testing with adversarial "can I break it?" testing — you need both.

## 9. Hands-On Exercise

Pick any chatbot you can access. Spend ten minutes acting as a one-person red team: write down three different things you would *not* want it to do (for example, give unsafe advice, reveal a hidden instruction, or confidently state something false). Try to get it to do each one, and record what happened. For each result, note whether you found a weakness and what a fix might look like.

## 10. Key Takeaways

- Red-teaming is deliberately attacking your own AI system to find weaknesses before real users or attackers do [1].
- You test before deployment because a failure caught in a test costs a fix, while a failure caught after launch costs real harm [3].
- Red-teaming is done by internal engineers, dedicated specialists, and automated tools, and it happens before deployment, after updates, and on an ongoing basis [2][3].
- Red teams probe known failure categories — jailbreaks, harmful outputs, data leakage, data poisoning, and triggering hallucination or bias — following a repeating test → find → fix → re-test loop.
- Red-teaming is the proactive testing the harm-prevention pillar (5.4) asks for, and it is how the real failures of 5.1–5.3 could be caught before launch.

## 11. Next Steps

_System-derived from the next entry in curriculum/sequence.md._
