<!-- nav:top:start -->
[⬅ Previous: 5.8 — EU AI Act](../../5-8-eu-ai-act-obligations-for-high-risk-systems-documentation-te/artifacts/reading.md)&emsp;·&emsp;[⬆ Table of Contents](../../../../../../../README.md#curriculum-topic-index)&emsp;·&emsp;[Next: 5.10 — NIST AI Risk Management Framework ➡](../../5-10-nist-ai-risk-management-framework-four-functions-govern-map/artifacts/reading.md)
<!-- nav:top:end -->

---

# EU AI Act — prohibited uses including social scoring and real-time biometric surveillance

## Overview

In topic 5.7 you met the EU AI Act's (European Union Artificial Intelligence Act's) pyramid of risk: four tiers, with heavier rules as the risk climbs. The very top of that pyramid is the **unacceptable-risk** tier. This topic looks at that tier up close.

These are uses the law does not regulate — it forbids them. Picture a camera that scans every face in a crowd live and checks it against a watchlist. Picture a government scoring citizens by their everyday behaviour and then deciding who gets a loan. The Act draws a hard line against exactly these uses [1][2]. Knowing where that line sits is how you spot the worst AI harms before they happen — and it is why this tier matters even though very few systems ever fall into it.

## Key Concepts

Everything in this topic is one idea seen from different angles: some AI uses are so harmful that the law bans them outright. We will start with what "banned" means, then look at the two headline cases, then list the rest.

### What "prohibited" means (and how it differs from "high-risk")

- **Prohibited use** — an AI use the law bans completely. There is no permit, no paperwork, no checklist that makes it legal. It is simply off-limits [1].
- These bans live in **Article 5** of the Act. "Article 5" is just the numbered section of the law where the banned list is written down [2].

The Act sorts AI by how much it could harm people. Most tiers say *"you may use this, but follow these rules."* The top tier is different. It says *"you may not use this at all"* [1].

![EU AI Act prohibited tier vs high-risk tier](./diagram.png)

*The prohibited tier sits at the narrow top of the risk pyramid — banned outright — while the high-risk tier below is allowed if providers follow the rules.*

**Why ban instead of regulate?** Think of the difference between a speed limit and a no-entry sign. A speed limit lets you drive if you follow the rules; a no-entry sign means you simply do not go there. For these uses the harm is judged so severe — a direct attack on human dignity, freedom, or safety — that no amount of paperwork could make them safe [1][3]. This is the **harm-prevention pillar** from 5.4 taken to its limit: when a harm is unacceptable, you prevent it by forbidding the practice entirely.

### Social scoring by governments

**Social scoring** — using AI to rate people based on their behaviour or personal traits over time, then treating them well or badly because of that score [1][2].

Here is a concrete example. A government system watches what citizens buy, who they spend time with, and whether they pay bills on time. It rolls all of that into a single "trust score." A high score gets you faster loans and better services. A low score gets you turned away from things that have nothing to do with the original behaviour [2].

The Act bans this because it produces two specific harms [2]:

- **Unfair treatment in unrelated situations** — being denied a job because of something you did in a completely different part of your life.
- **Treatment that is out of all proportion** — a small misstep leading to a large, lasting penalty.

Why is this so dangerous? Because it turns your whole life into a permanent grade that follows you everywhere. That strikes directly at fairness and dignity, which is why it sits in the banned tier [1].

### Real-time biometric surveillance in public spaces

First, two plain definitions:

- **Biometric** — identifying a person from a body trait, such as their face, fingerprint, or the way they walk.
- **Real-time** — happening live, as it occurs. The camera matches faces *in the moment* people walk past, not hours later from a saved recording.

So **real-time remote biometric identification in public spaces** means using AI to scan people live — for example, face-scanning a crowd in a train station and instantly matching faces against a database [1][2].

The Act bans this when it is done by law enforcement in publicly accessible spaces. Live mass face-scanning means everyone in the crowd is identified just for being there — not because they are suspected of anything. That is a sweeping loss of privacy for ordinary people who have done nothing wrong [1][2].

### The narrow exceptions to the biometric ban

The biometric ban is not absolute. The Act allows a few **narrow exceptions** — and the word *narrow* is the whole point. These are not loopholes. They are short, specific situations, each needing approval in advance [2][3]. The allowed cases are limited to things like:

1. Searching for specific victims, such as a missing child or a kidnapping victim.
2. Preventing a specific, imminent threat to life, such as a foreseeable terror attack.
3. Locating a suspect in a serious crime defined by the law.

Even then, the use must be authorized in advance and limited in time and place [3]. The default is still **banned**. A system that scans crowds live for general policing is on the banned side of that line [1][3].

### The other prohibited practices

Social scoring and real-time biometric surveillance are the two headline bans, but Article 5 lists several more. You only need to recognize them, not memorize legal detail [1][2]:

- **Manipulation that causes harm** — AI that uses hidden or deceptive techniques to push people into decisions they would not otherwise make, in a way that hurts them.
- **Exploiting vulnerabilities** — AI that takes advantage of someone's age, disability, or difficult situation to distort their behaviour.
- **Emotion recognition at work or school** — AI that claims to read people's emotions in workplaces or classrooms (with limited safety and medical exceptions).
- **Untargeted face-scraping** — building face databases by mass-collecting images from the internet or street cameras.
- **Predictive policing of individuals** — AI that predicts a person will commit a crime based purely on profiling them, not on real evidence.
- **Biometric categorization of sensitive traits** — sorting people by sensitive characteristics such as race or beliefs using their body data.

The common thread: each is a use where the harm to people's rights is judged too great to allow under any conditions [1][2].

## Worked Example

Suppose you are handed four AI systems and asked, for each one, "Is this **prohibited** (banned) or merely **high-risk** (allowed under rules)?" Walk through them using the sections above.

1. **A government "citizen trust score" that affects loan access.** This rates people by behaviour and then penalizes them in an unrelated situation (loans). That is **social scoring** — *prohibited* [2].
2. **A hiring tool that screens résumés.** It judges job applicants, which is serious, but it is not banned outright. It sits in the **high-risk** tier: allowed if the provider follows the rules. *Not prohibited.*
3. **Live face-scanning of a shopping street for general policing.** This is real-time biometric surveillance of a public space for everyday policing — exactly the banned case. *Prohibited* [1].
4. **Face-scanning authorized in advance to find a specific kidnapping victim.** This is one of the **narrow exceptions** — a specific victim, pre-authorized. It falls on the allowed side of the line [3].

Notice the pattern: cases 1 and 3 attack dignity or privacy so directly that no checklist could fix them, so they are banned. Cases 2 and 4 are controlled, not forbidden. The difference between case 3 and case 4 is not the technology — it is *why* and *how narrowly* it is used.

## In Practice

For a beginner, the goal is to *recognize a prohibited use when you see one*, not to apply the law. A few useful habits:

- **Ask "does this judge or watch people for who they are?"** Social scoring judges people; live biometric surveillance watches them. Both are red flags for the banned tier.
- **Remember "banned" is rare and deliberate.** Most AI is minimal-risk. Only a short, specific list is prohibited — do not assume every worrying AI is banned.
- **Watch the word "narrow."** The biometric exceptions are tiny and pre-authorized. If someone describes broad, everyday live face-scanning as "an exception," that is a red flag, not a real exception.
- **Trace it back to harm.** If a use attacks dignity, freedom, or fairness so directly that no checklist could fix it, that is why it sits in the banned tier rather than the high-risk one.

## Key Takeaways

- A **prohibited use** is an AI use the EU AI Act bans completely — it is the **unacceptable-risk** tier from 5.7, and it lives in **Article 5** [1][2].
- **Social scoring by governments** — rating people by behaviour and then treating them unfairly in unrelated situations — is banned because it attacks fairness and dignity [2].
- **Real-time biometric surveillance** — live face-scanning of people in public spaces — is banned, with only **narrow, pre-authorized exceptions** like finding a missing child or stopping an imminent attack [1][3].
- Article 5 also bans harmful **manipulation**, **exploiting vulnerabilities**, **emotion recognition at work or school**, untargeted **face-scraping**, individual **predictive policing**, and sensitive **biometric categorization** [1][2].
- These uses are **banned rather than regulated** because the harm is too severe for any safeguard to fix — the **harm-prevention pillar** from 5.4 at its limit [1][3].

## References

[1] European Commission. "What systems are prohibited under Article 5 AI Act (e.g. social scoring, emotion recognition)?" *AI Act Service Desk FAQ*. https://ai-act-service-desk.ec.europa.eu/en/ai-act/faq/what-systems-are-prohibited-under-article-5-ai-act-eg-social-scoring-emotion-recognition

[2] Future of Life Institute. "Article 5 — Prohibited AI Practices." *EU Artificial Intelligence Act*. https://artificialintelligenceact.eu/article/5/

[3] European Commission. "Commission publishes guidelines on prohibited artificial intelligence (AI) practices defined by the AI Act." *Shaping Europe's Digital Future*. https://digital-strategy.ec.europa.eu/en/library/commission-publishes-guidelines-prohibited-artificial-intelligence-ai-practices-defined-ai-act

---
<!-- nav:bottom:start -->
[⬅ Previous: 5.8 — EU AI Act](../../5-8-eu-ai-act-obligations-for-high-risk-systems-documentation-te/artifacts/reading.md)&emsp;·&emsp;[⬆ Table of Contents](../../../../../../../README.md#curriculum-topic-index)&emsp;·&emsp;[Next: 5.10 — NIST AI Risk Management Framework ➡](../../5-10-nist-ai-risk-management-framework-four-functions-govern-map/artifacts/reading.md)
<!-- nav:bottom:end -->
