<!-- nav:top:start -->
[⬅ Previous: 5.12 — India AI governance](../../5-12-india-ai-governance-meity-advisory-guidelines/artifacts/reading.md)&emsp;·&emsp;[⬆ Table of Contents](../../../../../../../README.md#curriculum-topic-index)&emsp;·&emsp;[Next: 6.1 — Why every AI system is built on numbers ➡](../../../../../m3-applied-maths-for-ai/week-6/1-why-numbers-matter-in-ai/6-1-why-every-ai-system-is-built-on-numbers/artifacts/reading.md)
<!-- nav:top:end -->

---

# Knowing which governance framework applies to your system

## Overview

This week you met four ways the world governs AI: a binding law (the EU AI Act, 5.7), voluntary guidance (the NIST AI RMF, 5.10), a US Presidential order (EO 14110, 5.11), and soft government advisories (India's MEITY guidelines, 5.12). A fair question now is: which of these actually applies to the thing you are building? This topic does not re-teach those four frameworks. It teaches you to *decide* between them, because picking the right one is part of the engineering job, not just an ethics conversation [3].

## Key Concepts

Here is the headline idea, and it is the takeaway for the whole week: **knowing which framework applies is a design-time engineering decision.** It is like choosing a database or a security standard before you write code. Get it wrong and you build the wrong documentation, skip the wrong tests, and leave out the human-oversight controls the rules require [3].

You do not need to memorize legal text to make this decision. Two plain questions get you most of the way [1][2][3].

1. **Where does your system operate — whose users does it touch?** This is about **jurisdiction**. **Jurisdiction — the area a government's rules cover, usually a country or region.** The rules of a place can reach your system when your system reaches that place.
2. **What does your system do — how risky is it?** A spam filter and a tool that screens job applicants carry very different stakes. The riskier the use, the heavier the rules.

Work them in that order: Question 1 tells you *which* frameworks are in play; Question 2 tells you *how hard* they bite.

![Decision flowchart for choosing which governance framework applies to an AI system](./diagram.png)
*Start at your AI system, answer the jurisdiction and use questions on each branch, and follow them to the EU AI Act, EO 14110, MEITY advisories, or NIST AI RMF. More than one branch can apply to the same system.*

### Question 1 — where does it operate?

Match your situation to a framework. These are not exclusive, so read every row, not just the first that fits [1][2]:

- **Does your system reach the EU market, or are its outputs used in the EU?** Then the **EU AI Act** (5.7) may apply. Here is the surprising part: the Act has **extraterritorial reach**. **Extraterritorial reach — a law that can apply to you even when you and your company sit outside the place that wrote it.** The EU AI Act can apply as long as your system is placed on the EU market or its **output is used in the EU** [1]. So a team in another country whose AI produces results that land in front of EU users can still be in scope. Do not assume "we're not in Europe" makes the Act irrelevant [1].
- **Are you a US federal agency, or selling AI to one?** Then US federal guidance, of the kind in **EO 14110** (5.11), is the relevant lens. That order steered how agencies buy and use AI.
- **Are you operating an online platform in India?** Then India's **MEITY advisories** (5.12) speak to you, with labeling and due-diligence expectations for platforms.
- **Do you want a best-practice way to manage AI risk anywhere, with no law forcing it?** Then the **NIST AI RMF** (5.10) is the voluntary choice — you can adopt it wherever you operate.

The pattern is simple: a *place* (or the place your output lands) pulls in a *framework*. The EU AI Act stands out because its reach follows your output, not just your address [1].

### Question 2 — what does it do?

Once you know a framework is in play, its strength depends on what your system does. The clearest case is the EU AI Act, because you already know its risk tiers from 5.7:

- An **unacceptable**-tier system is banned.
- A **high-risk** system (hiring, healthcare, law enforcement) is allowed only with documentation, testing, and human oversight.
- A **limited-risk** system (like a chatbot) mainly owes transparency.
- A **minimal-risk** system (a spam filter) carries almost no special rules.

So classification is a two-step move: first confirm a framework applies (Question 1), then place your system in its risk levels to see how heavy the obligations are (Question 2) [1][2].

### Frameworks are not mutually exclusive

A common beginner mistake is to assume exactly one framework applies. It does not work that way. **More than one framework can apply to the same system at the same time** — they are **not mutually exclusive** [2][3]. Check every framework against your system, not just the first that fits. The worked example below makes this concrete.

## Worked Example

Imagine a startup based in India that builds an AI hiring tool. Run the two questions on it:

1. **It is an online service in India.** So the **MEITY advisories** (5.12) about platform due diligence speak to it.
2. **It is sold to employers in the EU.** So its **output is used in the EU**, which means the **EU AI Act** (5.7) applies through extraterritorial reach [1].
3. **Hiring is high-risk.** Under the EU AI Act, that triggers the heavier obligations — documentation, testing, and human oversight [1].
4. **The team also chooses NIST.** It follows the **NIST AI RMF** (5.10) voluntarily to organize its risk work, even though no law forces it.

That is three frameworks touching one product at once: a binding law, an advisory, and a voluntary standard. Recognizing the overlap *is* the skill this topic teaches.

## In Practice

This is where ethics becomes a build decision. You met the four pillars in 5.4 as ethical goals; knowing the applicable framework turns them into things you must engineer [3]:

- **Documentation.** A high-risk system under the EU AI Act needs written records of how it was built and tested. Those are files you create at design time, not an afterthought.
- **Testing.** The framework tells you what testing to plan, including the red-teaming from 5.5 for the most-watched systems.
- **Human oversight.** High-risk rules require a person who can review and override the AI. That is a feature you architect in, not bolt on later.

A few habits keep you honest:

- **Ask "where does it operate?" before "what does it do?"** Jurisdiction picks the frameworks; risk level sets how hard they bite.
- **Never assume being outside the EU lets you off** — if your system's output is used in the EU, the EU AI Act can still apply [1].
- **Expect overlap.** Check every framework against your system, not just the first.
- **Decide at design time**, like a security standard, because documentation, testing, and oversight all flow from the framework.

Two limits are worth naming. First, the soft frameworks are reversible or quickly changed: EO 14110 (5.11) was an order a later President revoked, and MEITY advisories (5.12) are guidance a ministry can revise — unlike the binding EU AI Act (5.7). Second, "applies to" is not the same as "fully compliant." The detailed legal compliance procedures and the certification bodies that sign off on conformity are specialist work — named here only so you know they exist. Engineers identify the applicable framework; lawyers confirm the fine print.

## Key Takeaways

- Choosing the applicable governance framework is a **design-time engineering decision**, not just an ethics discussion — it shapes the documentation, testing, and human oversight you must build [3].
- Two questions do most of the work: **where does your system operate / whose users does it touch** (jurisdiction), and **what does it do** (risk level) [1][2].
- The **EU AI Act** has **extraterritorial reach** — it can apply even if you are based outside the EU, as long as your system's output is used in the EU [1].
- Frameworks are **not mutually exclusive**: a single system can fall under a binding law (EU AI Act, 5.7), an advisory (MEITY, 5.12), and a voluntary standard (NIST, 5.10) all at once [2][3].
- The EU AI Act is the binding end of the scale; EO 14110 (5.11) and MEITY advisories (5.12) are the soft, reversible end, and NIST (5.10) is opt-in anywhere.

## References

[1] European Union. *EU Artificial Intelligence Act, Article 2 (Scope)*. https://artificialintelligenceact.eu/article/2/
[2] European Commission. *Regulatory framework on AI*. https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai
[3] Legiscope. *EU AI Act Compliance Guide*. https://www.legiscope.com/blog/eu-ai-act-compliance-guide.html

---
<!-- nav:bottom:start -->
[⬅ Previous: 5.12 — India AI governance](../../5-12-india-ai-governance-meity-advisory-guidelines/artifacts/reading.md)&emsp;·&emsp;[⬆ Table of Contents](../../../../../../../README.md#curriculum-topic-index)&emsp;·&emsp;[Next: 6.1 — Why every AI system is built on numbers ➡](../../../../../m3-applied-maths-for-ai/week-6/1-why-numbers-matter-in-ai/6-1-why-every-ai-system-is-built-on-numbers/artifacts/reading.md)
<!-- nav:bottom:end -->
