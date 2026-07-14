<!-- nav:top:start -->
[⬅ Previous: 1.5 — Decomposition](../../1-5-decomposition-breaking-a-big-problem-into-smaller-solvable-p/artifacts/reading.md)&emsp;·&emsp;[⬆ Table of Contents](../../../../../../../README.md#curriculum-topic-index)&emsp;·&emsp;[Next: 1.7 — Pseudocode ➡](../../../3-expressing-logic/1-7-pseudocode-writing-logic-in-plain-english-before-writing-cod/artifacts/reading.md)
<!-- nav:top:end -->

---

# Abstraction — hiding complexity at the right level

## Overview

When you press the accelerator in a car, the car speeds up. You do not need to know anything about fuel injectors, pistons, or exhaust valves. The designers hid all of that detail behind a single pedal. That hiding of unnecessary detail is called **abstraction** — and it is one of the four pillars of computational thinking. Abstraction works alongside decomposition (Topic 1.5): decomposition breaks a problem into parts, and abstraction keeps each part simple enough to work with by hiding the detail you do not need right now [1][3].

## Key Concepts

### What abstraction means

**Abstraction** — the practice of removing or hiding details that are not needed for a particular purpose, so you can focus on what matters [1].

The key phrase is "for a particular purpose." There is no single right level of detail. The level that is right depends on who is asking and what they need to do [2][3].

Here is a plain test you can use: ask yourself, "What does this person need to know to do their job? What would slow them down or confuse them?" Hide the second thing. Show the first [1].

### Why layers of abstraction make complex systems manageable

Real systems are complicated. A modern city has millions of pipes, cables, and roads. A large software system has millions of lines of code. No one can hold all of that in mind at once.

Abstraction solves this by creating **layers**. Each layer hides the detail of the one below it and exposes only a clean, simple surface to the layer above [1][2].

The diagram below shows how this works — and how it differs from decomposition.

```mermaid
---
title: "Abstraction — hiding complexity at the right level"
config:
  theme: base
  themeVariables:
    primaryColor: "#a5d8ff"
    primaryBorderColor: "#4a9eed"
    lineColor: "#555"
  flowchart:
    htmlLabels: true
    curve: basis
---
flowchart TB

  subgraph LAYERS["Abstraction: hides detail"]
    direction TB
    USER["<b>You (the user)</b><br/><span style='font-size:11px;color:#6d28d9'>Sees: "cheese sandwich please"</span>"]
    IFACE["<b>Interface layer</b><br/><span style='font-size:11px;color:#6d28d9'>Passes the order — hides the kitchen</span>"]
    INTERN["<b>Hidden internals</b><br/><span style='font-size:11px;color:#6d28d9'>How bread is baked, kitchen workflow</span>"]

    USER -->|"clean surface ↓"| IFACE
    IFACE -->|"detail hidden ↓"| INTERN
  end

  subgraph DECOMP["Decomposition: breaks apart"]
    direction TB
    ROOT["<b>Big problem</b>"]
    SUBA["<b>Sub-task A</b>"]
    SUBB["<b>Sub-task B</b>"]

    ROOT --> SUBA
    ROOT --> SUBB
  end

  classDef primary fill:#a5d8ff,stroke:#4a9eed,color:#1a1a2e
  classDef secondary fill:#d0bfff,stroke:#8b5cf6,color:#1a1a2e
  classDef hidden fill:#F0F0F0,stroke:#999,color:#555,stroke-dasharray: 5 5
  classDef done fill:#b2f2bb,stroke:#22c55e,color:#1a1a2e

  class USER primary
  class IFACE secondary
  class INTERN hidden
  class ROOT,SUBA,SUBB done
```

*Abstraction stacks layers — each layer hides detail from the one above it — while decomposition splits a problem sideways into sub-tasks.*

### The "right level" — not too much detail, not too little

Choosing the right level is the hardest part of abstraction. Both extremes cause problems.

| Situation | What goes wrong |
|---|---|
| **Too much detail** | You explain semiconductor physics to a driver who just wants to know when to stop. Accurate, but useless. |
| **Too little detail** | You tell an electrical engineer "red means stop, green means go." They needed circuit diagrams and fault conditions. |
| **Right level** | You match the detail you show to the question being asked and the person asking it [1][3]. |

### How abstraction produces a model

A useful way to think about what abstraction creates: it produces a **model**.

**Model** — a simplified version of something real, built to be useful for a particular purpose.

A map is a model of a city. It does not show every tree or drainpipe. It shows what you need to navigate. A weather forecast is a model of the atmosphere — it cannot predict every gust of wind, but it can tell you to bring an umbrella [1][3].

A model hides detail on purpose. That is not a flaw — it is the model's job. The test of a good model is whether it is useful for its stated purpose, not whether it is complete [2].

### What a leaky abstraction looks like

**Leaky abstraction** — an abstraction that promises to hide detail but forces that detail back on the user in practice.

Here is an everyday example. A travel booking site promises "one-click booking." You click once. Then it asks for your passport number, seat preference, meal choice, emergency contact, and frequent flyer number — one page at a time. The promise ("one click") did not hold. The hidden complexity leaked back through.

A good abstraction hides details the user genuinely does not need. It does not hide things the user will immediately need to supply anyway [1][3].

### How abstraction and decomposition work together

You met **decomposition** in Topic 1.5. The two ideas do different jobs and work best together [1][2].

| | Decomposition | Abstraction |
|---|---|---|
| **The question it answers** | "What are the parts of this problem?" | "What details matter for this purpose?" |
| **The output** | A task tree — a list of sub-tasks | A model — fewer details, same essential shape |
| **When you use it** | To understand the structure of a problem | To manage the complexity of each part |

Decompose first, then abstract. Before you have broken the problem into parts, you do not yet know what the parts are — and you cannot hide detail inside a part you have not identified yet [1][2].

## Worked Example

Here is a step-by-step example of choosing the right level of abstraction [1][2][3].

**Situation:** You are writing a guide to using a library's online catalogue.

1. **Name the user and the task.** A student who wants to find a book by title and check whether it is available.

2. **List all the details involved.** The database query language, how records are indexed, what "on loan" means, how to reserve a book, how late fees work, the library's acquisition process.

3. **For each detail, ask: "Does the user need this to complete their task?"**
   - "What does 'on loan' mean?" — yes, the student needs this. Keep it.
   - "Database query language" — no. Hide it.
   - "How to reserve a book" — yes. Keep it.
   - "How late fees work" — a short summary is useful. Keep a summary.
   - "Library's acquisition process" — no. Hide it.

4. **Write the abstraction.** A guide that shows how to search by title, read availability status, and place a hold request. No mention of database internals.

5. **Check for leaks.** Walk through the guide as the student. Is there any moment you reach for a hidden detail? If not, the abstraction holds.

6. **Revisit when the audience changes.** If the audience were a librarian configuring the system, the right level would be completely different [1][2][3].

## In Practice

Abstraction shows up everywhere — not just in computing.

- **Maps.** A road map hides building floor-plans and underground utilities. A tube or metro map distorts distances deliberately, because what a passenger needs is the sequence of stations, not exact geography [1][3].
- **Recipes.** "Bring to a boil" hides the molecular physics of water at 100°C. It shows the cook exactly what they need: a visual cue and an action [3].
- **App buttons.** The "Delete" button hides a sequence of background operations. The designer chose the right level so you can use the app without being a software engineer [1][2].
- **Scientific models.** The school-level model of the atom — nucleus with electrons orbiting it — is an abstraction. It is not physically complete, but it is useful for understanding chemical bonding at a beginner level. Advanced chemistry requires a more detailed model [1][3].

When you design any abstraction — a guide, a form, a checklist — ask yourself:

- Am I truly hiding detail the user does not need?
- Or am I just deferring it until they hit a wall?

If you find yourself hiding something the user will immediately need, that is a leak to fix [2].

## Key Takeaways

- **Abstraction means hiding detail that is not needed for the current purpose.** It is not oversimplifying — it is focusing on what matters for a specific task and audience [1][2].
- **The "right level" depends on who is asking and what they need to do.** Too much detail overwhelms; too little leaves people unable to act [1][3].
- **Abstraction produces a model.** A model is intentionally incomplete — its job is to be useful for its stated purpose, not to be a complete replica [2][3].
- **Abstraction and decomposition work together.** Decomposition identifies the parts; abstraction keeps each part manageable by hiding unnecessary internal detail [1][2].
- **A leaky abstraction forces hidden details back on the user.** Good abstractions hold — users never need to reach behind the curtain to get their job done [1][2].

## References

1. Learning.com, "Abstraction in Computational Thinking." <https://www.learning.com/blog/abstraction-in-computational-thinking/>
2. ERIC / Journal of Computer Science Education, "Abstraction as a threshold concept in CS education." <https://files.eric.ed.gov/fulltext/EJ1329311.pdf>
3. Teaching London Computing (CAS London), "Abstraction — Developing Computational Thinking." <https://teachinglondoncomputing.org/resources/developing-computational-thinking/abstraction/>

---
<!-- nav:bottom:start -->
[⬅ Previous: 1.5 — Decomposition](../../1-5-decomposition-breaking-a-big-problem-into-smaller-solvable-p/artifacts/reading.md)&emsp;·&emsp;[⬆ Table of Contents](../../../../../../../README.md#curriculum-topic-index)&emsp;·&emsp;[Next: 1.7 — Pseudocode ➡](../../../3-expressing-logic/1-7-pseudocode-writing-logic-in-plain-english-before-writing-cod/artifacts/reading.md)
<!-- nav:bottom:end -->
