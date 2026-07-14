<!-- nav:top:start -->
[⬅ Previous: 5.6 — Prompt injection](../../../3-safety-practices/5-6-prompt-injection-how-attackers-manipulate-ai-through-crafted/artifacts/reading.md)&emsp;·&emsp;[⬆ Table of Contents](../../../../../../../README.md#curriculum-topic-index)&emsp;·&emsp;[Next: 5.8 — EU AI Act ➡](../../5-8-eu-ai-act-obligations-for-high-risk-systems-documentation-te/artifacts/reading.md)
<!-- nav:top:end -->

---

# EU AI Act — risk tiers (unacceptable / high / limited / minimal risk)

## Overview

In earlier topics you saw AI go wrong in the real world: a hiring tool that downgraded women, AI that misread medical scans, and deepfakes that fooled people. Those harms were serious enough that governments decided rules were needed. The European Union answered with the **EU AI Act (European Union Artificial Intelligence Act)** — the first broad law in the world written specifically to govern artificial intelligence [1][2].

This topic teaches the one big idea behind that law: it does not treat every AI system the same way. Instead, it sorts systems by how much risk they pose to people, then applies heavier rules to higher risk [1]. Learn those tiers and you understand the heart of the law.

## Key Concepts

First, a plain definition. A **regulation** — here — is an official, legally binding rule set by a government that organizations must follow. The EU AI Act is one such regulation, aimed only at AI systems.

The Act's central choice is to be **risk-based**. Think of two systems: a chess-playing app and a system that decides who gets hired. They carry very different stakes. It would be wasteful to regulate the chess app like the hiring system, and dangerous to regulate the hiring system like the chess app.

So the Act asks one question of every AI system: how much could this harm people if it goes wrong? The answer places the system into one of four tiers, and the tier decides the rules [1][2]. The higher the risk, the stricter the obligations.

A natural way to picture this is a **pyramid**. A few dangerous systems sit at the narrow top with the most rules; most ordinary systems sit at the wide bottom with almost none.

![EU AI Act four-tier risk pyramid](./diagram.png)
*The four risk tiers, from the banned apex down to the unregulated base — width shows how many systems fall in each tier.*

Reading the pyramid from top to bottom, the four tiers and the law's response look like this:

| Tier | What the law does | Example |
|---|---|---|
| **Unacceptable** | Bans it outright | Government social scoring |
| **High** | Allows it under strict obligations | Hiring or healthcare AI |
| **Limited** | Requires transparency (disclose it is AI) | Chatbots, labeled deepfakes |
| **Minimal** | No mandatory rules | Spam filter, game AI |

A few terms in that table need unpacking, tier by tier.

**Unacceptable risk — banned.** At the very top are uses considered such a clear threat to people's safety or rights that they are simply not allowed at all [1][2]. One example is government social scoring: rating citizens by their behavior, then granting or denying them services based on the score. Another is real-time biometric surveillance in public spaces. **Biometric** means identifying a person from a body trait such as their face or fingerprint, and "real-time" means scanning crowds live as people walk by. The full list of banned uses is its own later topic — here you only need to know the top tier means *banned*.

**High risk — heavily regulated.** Just below sit high-risk systems. These are allowed, but only under strict conditions, because they make decisions that seriously affect people's lives or safety [1][3]. Typical examples are hiring software, AI in medical diagnosis, police tools that score suspects, and AI controlling critical infrastructure like power or water.

What does "heavily regulated" mean in plain terms? Before such a system can be used, its provider must do serious homework [1][3]:

- **Keep documentation** — written records of how the system was built and tested.
- **Test the system** — including the adversarial testing you met as red-teaming earlier.
- **Provide human oversight** — a person must be able to review and override the AI's decisions.
- **Pass a conformity assessment.** A **conformity assessment** is an official check, before launch, that the system meets the law's requirements — like the safety inspection a car must pass before it can be sold.

The detailed high-risk obligations are covered in upcoming topics; here you only need the headline — high risk means *allowed but tightly controlled*.

**Limited risk — transparency obligations.** Next down, the main duty is simple: be honest that AI is involved [1][2]. This is a **transparency** obligation — telling people plainly when they are dealing with AI, which is one of the four pillars from 5.4. Two everyday cases: a chatbot must tell you it is an AI so you are not fooled into thinking it is human, and a deepfake (AI-generated or AI-altered images, audio, or video) must be labeled as artificial. The rule is light — you can use these systems freely, you just cannot hide that they are AI [2].

**Minimal risk — no mandatory rules.** At the wide bottom sit minimal-risk systems — the vast majority of everyday AI [1][2]. Spam filters, recommendation features, and AI in video games all live here. The Act imposes no mandatory rules on them; providers may follow good practices voluntarily, but the law does not force special obligations.

Why this shape? Very few systems are banned, a manageable set are high-risk, and most are minimal-risk [1]. The law concentrates its effort where the danger is greatest.

The Act also connects straight back to the four pillars from 5.4 — it puts those ethical principles into law. Harm prevention becomes the banned tier. Accountability and fairness become the high-risk tier's documentation, testing, and oversight. Transparency becomes the limited-risk tier's disclosure duty [1][2]. The Act does not invent new ethics; it gives ethics you already know legal teeth.

## Worked Example

Suppose you have four AI systems and want to guess each one's tier. Work from the harm, not the technology — ask "who gets hurt if this fails, and how badly?"

1. **A movie recommender.** If it fails, you get a bad film suggestion. Low stakes, so this is **minimal risk** — no mandatory rules.
2. **An AI that scores loan applicants.** If it fails, someone is wrongly denied money that affects their life. That makes it **high risk** — documentation, testing, human oversight, and a conformity assessment all apply.
3. **A customer-service chatbot.** Low direct harm, but you should not be tricked into thinking it is a person. That is **limited risk** — it must disclose it is AI.
4. **A government system that ranks citizens by social behavior.** This strikes at dignity and freedom, so it is **unacceptable risk** — banned outright.

Notice the pattern: the tier follows the use and the potential harm, never how advanced the model is.

## In Practice

When you meet a new AI system and want to place it on the pyramid, a few habits help:

- **Start from the harm, not the technology.** Ask who gets hurt if it fails — not how clever the model is.
- **"High risk" is about the use, not the cleverness.** A simple model used in hiring can be high-risk; a sophisticated model in a game is minimal-risk.
- **Banned is rare on purpose.** Most AI is minimal-risk, so do not assume every system is heavily regulated.
- **Transparency is cheap and almost always wise.** Even when the law does not require it, telling users they are dealing with AI builds trust.

The EU AI Act is only one framework among several. Other approaches — the NIST AI Risk Management Framework, the US White House Executive Order on AI, and India's MEITY advisory guidelines — are covered in upcoming topics and are not part of this one.

## Key Takeaways

- The **EU AI Act** is the first broad law written to govern AI, and it is **risk-based**: heavier rules apply to higher-risk systems [1].
- There are **four tiers** — unacceptable (banned), high (heavily regulated), limited (transparency required), and minimal (no mandatory rules) [1][2].
- A system's tier is set by how much it could harm people, judged by its *use*, not by how advanced the technology is.
- High-risk systems must keep documentation, be tested, provide human oversight, and pass a **conformity assessment** before launch [1][3].
- The Act turns the four pillars from 5.4 — fairness, transparency, accountability, harm prevention — into enforceable law [1].

## References

1. European Commission — Regulatory framework for AI. https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai
2. European Parliament — EU AI Act: first regulation on artificial intelligence. https://www.europarl.europa.eu/topics/en/article/20230601STO93804/eu-ai-act-first-regulation-on-artificial-intelligence
3. EU AI Act compliance checker. https://artificialintelligenceact.eu/assessment/eu-ai-act-compliance-checker/

---
<!-- nav:bottom:start -->
[⬅ Previous: 5.6 — Prompt injection](../../../3-safety-practices/5-6-prompt-injection-how-attackers-manipulate-ai-through-crafted/artifacts/reading.md)&emsp;·&emsp;[⬆ Table of Contents](../../../../../../../README.md#curriculum-topic-index)&emsp;·&emsp;[Next: 5.8 — EU AI Act ➡](../../5-8-eu-ai-act-obligations-for-high-risk-systems-documentation-te/artifacts/reading.md)
<!-- nav:bottom:end -->
