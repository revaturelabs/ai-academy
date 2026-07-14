---
topic_id: "2.1"
title: "What makes a good specification — testable, bounded, observable, actionable"
position_in_module: 1
generated_at: "2026-06-16T00:00:00Z"
resource_count: 3
---

# 1. What Makes a Good Specification — Testable, Bounded, Observable, Actionable — Topic Corpus

## 2. Prerequisites

This topic builds directly on Week 1 concepts:

- **1.1 What is computation** — the idea that a computer (or AI) follows instructions exactly as given.
- **1.9 Algorithmic thinking** — the understanding that a set of steps must be unambiguous to produce a reliable result.
- **1.7 Pseudocode** — experience writing step-by-step instructions in plain language.

No programming knowledge is needed. Everything in this topic can be understood through everyday examples.

## 3. Learning Objectives

By the end of this topic you will be able to:

- Define what a **specification** is and explain why it matters when working with AI.
- Describe each of the four properties of a good specification: testable, bounded, observable, and actionable.
- Identify whether a given specification is missing one or more of those four properties.
- Rewrite a weak specification to make it stronger by applying all four properties.
- Explain why AI systems need stricter specifications than human workers do.
- Evaluate a specification you have written against a four-property checklist.

## 4. Introduction

Imagine you ask a friend to "make the report better." Your friend is a smart person. They know you, they know the context, and they will probably make a reasonable improvement. Now imagine you give that same instruction to an AI tool. What does "better" mean to it? Shorter? Longer? More formal? More pictures? The AI has no shared context with you. It will do *something* — but there is a good chance it will not do the *something* you wanted.

This gap between what you said and what you meant is the core problem that a **specification** solves. A specification is a clear, written description of exactly what you want done, how you want it done, and how you will know when it is done correctly. Good specifications are the difference between getting a useful result from an AI tool and getting a frustrating guess [1].

In Week 1 you learned that algorithms are unambiguous sets of steps. A specification is the step that comes before the algorithm — it tells the AI (or any system) what goal to achieve and what the boundaries of that goal are. Without a good specification, even a powerful AI will produce unreliable results [2].

This week you will learn four properties that every good specification must have: it must be **testable**, **bounded**, **observable**, and **actionable**. These four properties are your checklist. Each one closes a specific gap between a vague wish and a useful instruction [3].

## 5. Core Concepts

### 5.1 What Is a Specification?

A **specification** (also called a "spec") is a written description of a task that is detailed enough for a system — human or AI — to carry it out without guessing what you meant.

Think of it like a recipe. A recipe does not say "cook the chicken until it tastes good." It says "bake at 180 °C for 45 minutes until the internal temperature reaches 75 °C." Every detail is pinned down: the method, the temperature, the time, and the success test [1].

When you write a specification for an AI tool, you are doing the same thing. You are replacing guesswork with precision.

A weak specification leaves gaps. A strong specification closes them. The four properties below are how you close those gaps.

---

### 5.2 Property 1 — Testable

**Testable** means you can check, after the AI has finished, whether the output is correct or not. There is a clear yes/no answer to the question "did it work?" [1].

**Why this matters for AI.** AI systems are probabilistic — they do not always give the same answer twice. You learned in Week 1 that AI gives different answers to the same question. Because of that variation, you need a way to check each output independently. A testable specification gives you that check [2].

**Example of a non-testable specification:**
> "Write a good summary of this article."

"Good" is not testable. Two people (or two AI runs) could produce very different summaries and both call them "good." You have no way to check one against a fixed standard.

**Example of a testable specification:**
> "Write a summary of this article in exactly 3 bullet points. Each bullet point must be one sentence of no more than 20 words. The summary must not include any information that is not in the original article."

Now you can test the output:
1. Count the bullets — should be 3.
2. Count the words in each bullet — should be 20 or fewer.
3. Check that no new information was added.

Either it passes or it does not [1].

**The testability check:** After writing a specification, ask yourself: "If an AI gave me two different outputs, could I compare them to my spec and pick the better one — without relying on my gut?" If yes, your spec is testable.

---

### 5.3 Property 2 — Bounded

**Bounded** means the specification has clear limits. It tells the AI what is inside the task and, just as importantly, what is outside it [2].

**Why this matters for AI.** Without boundaries, an AI tool fills the gaps with its own assumptions. It may go too broad (adding topics you did not want) or too narrow (leaving out something you needed). Boundaries remove those assumptions [3].

Think of a bounded specification like a fence around a garden. Everything inside the fence is the job. Everything outside is not. Without the fence, the AI might start tending the neighbour's garden too — or leave half of yours untouched.

**Example of an unbounded specification:**
> "Explain machine learning."

Machine learning is a vast subject. The AI could write two sentences or two hundred pages. It could start from the very beginning or assume advanced knowledge. There is no fence.

**Example of a bounded specification:**
> "Explain machine learning in plain English, as if talking to someone who has never studied computers. Cover only what supervised learning is and give one real-world example. Do not cover unsupervised learning, reinforcement learning, or any mathematical formulas. Keep your answer under 150 words."

The fence is now clear. The AI knows what to include and what to leave out [2].

**Common bounding dimensions to consider:**

| Dimension | Example bound |
|---|---|
| Length | "Under 100 words" / "Exactly 5 bullet points" |
| Audience | "For a 12-year-old" / "For a senior manager" |
| Scope | "Cover only X, not Y or Z" |
| Format | "Use a numbered list" / "Use a table" |
| Tone | "Formal and professional" / "Friendly and conversational" |

---

### 5.4 Property 3 — Observable

**Observable** means the output of the task is something you can actually see, read, or measure. The result exists in a form you can inspect [1].

**Why this matters for AI.** An AI cannot hand you a feeling or an experience — it can only produce text, a file, a number, or some other concrete artifact. If your specification describes a result that is invisible or internal — like "make the user feel confident" — the AI has nowhere to go. Observable specifications ask for concrete outputs [3].

This property is closely related to testability, but they are not the same thing. A result can be visible (you can see the AI produced *something*) but still not testable (you cannot tell if what it produced is *correct*). Both properties are needed.

**Example of a non-observable specification:**
> "Help me understand this contract better."

"Understanding" is internal to you. The AI cannot produce your understanding. It will guess at what might help, but it has no concrete target to aim at.

**Example of an observable specification:**
> "Identify every clause in this contract that could be interpreted as limiting my right to cancel the service. List each clause number and quote the relevant sentence. Then write one plain-English sentence explaining the risk each clause creates."

Now the output is observable: a numbered list of clauses, exact quotes, and plain-English risk statements. You can read and inspect every part of it [1].

**The observability check:** Ask yourself: "What will I actually receive? Can I put it in a document, read it aloud, or count it?" If yes, your spec is observable.

---

### 5.5 Property 4 — Actionable

**Actionable** means the specification gives the AI enough information to start working immediately — without needing to ask you follow-up questions or make additional assumptions [3].

**Why this matters for AI.** A human worker can ask for clarification. An AI tool, in most workflows, will not stop and ask — it will make a choice and keep going. If your specification is missing a critical piece of information, the AI fills the gap with a default assumption, which may be wrong [2].

An actionable specification answers the questions the AI would need answered before it could begin:
- What exactly is the task?
- Who is the audience?
- What format should the result take?
- What source material should it use?
- What constraints apply?

**Example of a non-actionable specification:**
> "Write a lesson plan."

What subject? What age group? How long? What prior knowledge does the audience have? The AI will guess — and its guesses may not match your context at all.

**Example of an actionable specification:**
> "Write a 45-minute lesson plan for teaching 14-year-olds what a spreadsheet formula is. Assume students have used spreadsheets before but have never written a formula. The plan should include: a 5-minute warm-up, a 20-minute explanation with two worked examples, a 15-minute hands-on activity, and a 5-minute reflection question. Use simple language with no jargon."

Everything the AI needs is there. It can start immediately [3].

**The actionability check:** Read your specification as if you are the AI and know nothing else about the situation. Do you have everything needed to begin? If you would need to ask a question first, the spec is not yet fully actionable.

---

### 5.6 The Four Properties Together

The four properties reinforce each other. A specification that is bounded is easier to test. A specification that is observable is easier to make actionable. When all four are satisfied, the specification is complete — no gap remains for the AI to fill with a guess.

A specification that passes all four checks is ready to use with an AI tool. One that fails even one check will produce unreliable results — not because the AI is broken, but because the instruction was incomplete [1][2][3].

## 6. Implementation

Use this four-step process every time you write a specification for an AI tool.

1. **Draft the raw task.** Write what you want in plain language — no filtering yet. Example: "I want a summary of this report."

2. **Add testability.** Define the success criteria. What does "done correctly" look like? Add measurable targets: word count, number of items, specific information that must or must not appear. Example: "Summarise in exactly 5 bullet points. Each bullet must cover one key finding. Total length must be under 120 words."

3. **Add bounds.** Define the scope limits. What is in? What is out? Add audience, format, and topic constraints. Example: "Cover only the financial findings on pages 3–7. Do not include methodology or appendices. Write for a non-specialist reader."

4. **Check observability and actionability.** Read the specification aloud. Ask: "What will I receive?" (observable) and "Does the AI have everything it needs?" (actionable). Fill any remaining gaps. If you catch yourself thinking "the AI will figure it out," that is a gap — fill it explicitly [3].

After step 4, run the four-property checklist:

- [ ] **Testable** — I can check the output against a clear standard.
- [ ] **Bounded** — Scope, format, and limits are explicit.
- [ ] **Observable** — The output is concrete and inspectable.
- [ ] **Actionable** — No follow-up questions needed before the AI can start.

If any box is unchecked, revise before sending [1].

## 7. Real-World Patterns

The four properties appear in professional contexts beyond AI prompting.

**Software development.** Developers write specifications (often called "requirements" or "acceptance criteria") before building a feature. A well-known format is: "Given [context], when [action], then [observable result]." This maps directly onto testable, observable, and actionable [2].

**Data analysis.** An analyst specifying a report for a dashboard tool must define exactly which data range to use (bounded), what chart type to produce (observable), and what counts as an anomaly to highlight (testable). Vague data specs produce wrong charts [1].

**Workplace delegation.** A manager giving a task to a new employee uses the same principles: "By Friday, send me a two-page summary of the client calls from this week. Cover only calls about Project X. Include the date, the client name, and one sentence on the outcome of each call." That instruction is bounded, observable, testable, and actionable — even without AI involved.

The four properties are useful any time you need to communicate a task precisely to any system or person that cannot read your mind [3].

## 8. Best Practices

**Do:**
- Write specifications in writing, not just in your head. The act of writing forces clarity.
- Start specific, then relax. It is easier to loosen a tight spec than to tighten a vague one.
- Test your spec on a simple case before applying it to your real task.
- Treat the AI's output as feedback on your spec. If the result is wrong, the spec probably had a gap [1].

**Do not:**
- Use adjectives that describe quality without defining it: "good," "better," "appropriate," "clear." Replace each with a measurable criterion.
- Assume the AI knows your context. Every relevant fact must be stated in the specification.
- Write a one-line specification for a multi-part task. Complex tasks need detailed specs.
- Rely on the AI to ask follow-up questions. Some tools do; many do not. Write specs that do not require them [2][3].

**Common anti-patterns:**

| Vague phrase | The problem | Better alternative |
|---|---|---|
| "Keep it short" | "Short" is not bounded | "Under 100 words" |
| "Generate ideas" | Not observable — no topic, format, or count | "List 5 product-name ideas for a healthy-food delivery service, each under 15 characters" |
| "Summarise this for me" | Not actionable — missing audience and format | "Summarise for a non-technical manager in 3 bullet points, each under 25 words" |

## 9. Hands-On Exercise

Choose one real task from your own life or work — something you might ask an AI tool to help with. Write a first draft of the specification in one sentence. Then apply the four-step implementation process from Section 6. For each of the four properties, write down the specific change you made (or confirm the property was already satisfied in your draft). Finally, compare your final specification to your original one-sentence draft. Notice how many gaps the checklist reveals — the goal is to practise finding gaps, not to judge yourself for having them.

## 10. Key Takeaways

- A **specification** is a written description of a task detailed enough that the system carrying it out does not need to guess what you meant.
- AI tools require stricter specifications than human workers because AI cannot ask for clarification the way a person can and does not share your context.
- The four properties of a good specification are: **testable** (you can check whether it worked), **bounded** (scope and limits are explicit), **observable** (the output is concrete and inspectable), and **actionable** (the AI has everything it needs to begin without asking follow-up questions).
- A specification that fails even one of the four properties will produce unreliable results — not because the AI is broken, but because the instruction was incomplete.
- The four-step drafting process — draft, add testability, add bounds, check observability and actionability — gives you a repeatable method for building strong specifications for any AI task.

## 11. Next Steps

_System-derived from the next entry in curriculum/sequence.md._
