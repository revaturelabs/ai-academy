<!-- GENERATED FILE — DO NOT EDIT BY HAND.
     Cresent view of 9.3 — Specifying for AI.
     Source of truth: CIT 1.12, CIT 2.1, CIT 2.2, CIT 2.3, CIT 2.5, CIT 2.6, CIT 2.7, CIT 2.8, CIT 2.9.
     Regenerate: python Cresent/Technical/tools/generate_shared_readings.py -->
<!-- nav:top:start -->
Previous: [⬅ 9.2 — Expressing Logic](../9-2-expressing-logic/reading.md)&emsp;·&emsp;[⬆ Table of Contents](../../../../../../README.md#part-b)&emsp;·&emsp;[10.1 — History of AI ➡](../../../../m2-introduction-to-ai-systems/week-10/1-what-ai-is-and-isnt/10-1-history-of-ai/reading.md)
<!-- nav:top:end -->

---

# Choosing your domain — writing a 3-sentence problem statement

## Overview

Before you write a single line of pseudocode or draw a flowchart, you need to know exactly what problem you are solving. Jumping straight to solutions is the most common mistake in computing — and the hardest to recover from later. A **problem statement** is a short, focused piece of writing — exactly three sentences — that pins down the problem before any solution thinking begins [1]. Getting this right gives you a stable foundation to decompose and abstract from throughout the rest of the course.

## Key Concepts

Every problem statement has two building blocks: a **problem domain** and the statement itself. These are easy to confuse, so let's take them one at a time.

### 1. Problem domain

A **problem domain** is the specific area of real-world activity your project addresses. It is not a technology or a tool — it is a slice of real life.

- Examples of domains: healthcare, student revision, local transport, food waste, personal finance.
- A domain is the setting. The problem is what goes wrong inside that setting.
- You pick one domain and return to it all semester — so choose something you find genuinely interesting.

**Why it matters:** a domain that is too broad ("technology in society") gives you nowhere to stand. A specific domain ("secondary school exam revision") gives you a real group of people and a real situation to study [2].

### 2. Problem statement

A **problem statement** is a short written description of who is affected, what specifically goes wrong, and why it matters. It is not a solution proposal — it must not mention apps, systems, or fixes of any kind [1].

Three rules before you write a single word:

- **Specific, not general.** "Elderly patients living alone" is a group. "Everyone" is not.
- **One problem, not a list.** If you wrote "and also…" in your draft, split it into two and pick the stronger one.
- **No solution embedded.** If your sentence says "I will build an app that…", stop and rewrite it as a problem [3].

### 3. The 3-sentence format

Each sentence does exactly one job. Nothing more.

![3-sentence problem statement format](../../../../../../../../CIT/content-gen-example/content/m1-computational-thinking/week-1/5-applying-it-to-your-domain/1-12-choosing-your-domain-writing-a-3-sentence-problem-statement/artifacts/diagram.png)
*Three-slot pipeline: each sentence carries one piece of information — context, specific problem, impact.*

| Sentence | Job | Question it answers |
|---|---|---|
| **Sentence 1 — Context** | Sets the scene | Who is affected, and in what situation? |
| **Sentence 2 — Specific problem** | Names what goes wrong | What exactly is the problem? |
| **Sentence 3 — Impact** | States the consequence | What real-world harm or cost does this cause? |

Think of it as three slots. Each slot holds one idea. A sentence that tries to fill two slots usually does neither well [2].

## Worked Example

Here is a complete problem statement for a student revision domain:

> "Secondary school students preparing for public examinations often have no reliable way to know which topics they understand well and which they are still weak on. As a result, they frequently over-revise familiar material and under-revise the areas that would most improve their grade. A solution to this problem would need to track understanding across topics and surface the weakest areas for a student without requiring a teacher to be present."

Apply the three quality tests:

- Specific group? **Yes** — "secondary school students preparing for public examinations."
- One problem? **Yes** — the inability to judge their own topic-level understanding.
- No solution named? **Yes** — Sentence 3 describes what a solution would need to do, not what it is.

Now look at a counter-example:

> "Healthcare has a lot of problems. Technology could help make things better for everyone."

What is wrong?

- No specific group — "everyone" is not a group.
- No specific problem — "a lot of problems" names nothing.
- No consequence — nothing about what harm this causes.

This is two vague sentences, not a problem statement. It fails all three quality tests [3].

## In Practice

Use this five-step checklist each time you write a problem statement [1][2]:

1. **Choose your domain.** Pick one area of real life that genuinely interests you — you will work with it all semester.
2. **Name who is specifically affected.** Identify a real group of people, not "everyone" or "society."
3. **State what exactly goes wrong.** One problem only — be precise enough that someone outside your domain would understand it.
4. **State the consequence.** What harm, cost, or frustration does this problem cause?
5. **Write the three sentences, then run the quality tests.**

**Quality test checklist:**

- Is the affected group specific enough to picture? (Not "people" — which people, where, when?)
- Is there exactly one problem in Sentence 2? (If "and" appears, split and pick one.)
- Does any sentence name or imply a technology fix? (If yes, cut it.)

A strong problem statement is not a long one. Three sentences that pass all three tests are worth far more than a paragraph that drifts into solutions [3].

## Key Takeaways

- **Problem domain** = the real-world area you are working in; **problem statement** = three sentences covering context, specific problem, and impact.
- Each sentence does exactly one job — mixing jobs into one sentence weakens both.
- Three quality tests: specific group, one problem only, no solution embedded [1].
- A problem statement that passes all three tests gives you a stable base to apply decomposition (breaking the problem into sub-tasks) and abstraction (focusing on what matters, ignoring what does not).
- Vague problem statements produce vague designs — precision here saves rework at every stage that follows [2].

## References

1. National University LibGuides, "Structured Problem Statement Guide." <https://resources.nu.edu/c.php?g=1013602&p=7638573>
2. BetterUp, "How to Write a Problem Statement." <https://www.betterup.com/blog/problem-statement>
3. Notion, "How to Write Problem Statements." <https://www.notion.com/blog/problem-statements>

---

# What makes a good specification — testable, bounded, observable, actionable

## Overview

A specification is the instruction you give before work begins — it tells a system, a person, or an AI tool exactly what result you want. In Week 1, you learned that algorithms must be unambiguous and that AI does not always give the same answer twice. A vague instruction given to a regular program produces the same wrong result every time, but given to an AI it produces a different wrong result every time — which is much harder to fix [1]. That is why a good specification must have four properties — testable, bounded, observable, and actionable — to turn a vague request into an instruction clear enough to check, repeat, and improve [2].

## Key Concepts

Think of these four properties as four checks you run before giving an AI any instruction. Missing even one is usually why AI output does not turn out the way you hoped — not because the AI is broken, but because the instruction was not clear enough [3].

### 1. Testable

A **testable** specification means you can check — after the AI finishes — whether the output is correct or not. You need a clear pass or fail condition.

- **Good:** "List 3 camping essentials, one per bullet, each under 10 words." You can count the bullets and check the length.
- **Bad:** "Tell me what to bring camping." How many items? How much detail? There is no way to know if it gave you enough.

After writing any specification, ask: "If the AI gave me two different outputs, could I compare them to my spec and pick the better one without relying on gut feeling?" If yes, the spec is testable [1].

### 2. Bounded

A **bounded** specification sets clear limits so the AI only works on what you asked for — nothing more, nothing less.

- **Good:** "Fix only the spelling mistakes in the first paragraph; do not change any words or sentences." The AI knows exactly what to fix and what to leave alone.
- **Bad:** "Fix my paragraph." The AI might rewrite sentences, change your tone, or restructure things you never wanted touched.

Think of a bounded specification like a fence around a garden. Everything inside the fence is the job. Everything outside is not [2]. Common bounding dimensions include:

| Dimension | Example |
|---|---|
| Length | "Under 100 words" / "Exactly 5 bullets" |
| Audience | "For a 12-year-old" / "For a senior manager" |
| Scope | "Cover only X, not Y or Z" |
| Format | "Use a numbered list" / "Use a table" |

### 3. Observable

An **observable** specification produces output you can read and verify straight away — no guessing or extra work needed to figure out whether the task succeeded.

- **Good:** "Give me 3 reasons why students procrastinate, one reason per line." You can read the three lines immediately and check if it answered the question.
- **Bad:** "Explain why students procrastinate." The AI might write three paragraphs of general advice and you are left wondering whether it actually answered what you asked.

Observable is related to testable, but the two are not the same. A result can be visible — you can see the AI produced *something* — but still not testable if you cannot tell whether what it produced is *correct*. Both properties are needed [1].

Ask yourself: "What will I actually receive? Can I put it in a document, read it aloud, or count it?" If yes, the spec is observable.

### 4. Actionable

An **actionable** specification gives the AI enough detail to start the task immediately, without having to guess what you mean.

- **Good:** "Rewrite this sentence in simple English so a 10-year-old can understand it, and keep it under 20 words." The AI knows exactly what to do and where to stop.
- **Bad:** "Make this sentence better." Better how? Shorter? Simpler? More formal? The AI will guess — and its guess may not match what you wanted [3].

A human worker can ask for clarification. An AI tool, in most workflows, will not stop and ask — it will make a choice and keep going. If a critical detail is missing, the AI fills the gap with a default assumption, which may be wrong [2].

Read your specification as if you are the AI and know nothing about the situation. Do you have everything needed to begin? If you would need to ask a question first, the spec is not yet fully actionable.

## Worked Example

Let's take a poor instruction and fix it step by step.

**Starting point:** "Make this email better." — you cannot check if it worked, there are no limits on what to change, and the AI has no idea what "better" means to you.

Here is how to fix it, one step at a time:

1. **Give it a direction** — "Rewrite this email to sound more professional."
2. **Set a limit** — "...keep it under 100 words."
3. **Add a clear rule** — "...do not change the deadline date."
4. **Tell it what to give back** — "...output only the rewritten email, no extra explanation."

**Final specification:** "Rewrite this email to sound more professional, keep it under 100 words, do not change the deadline date, and output only the rewritten email with no extra explanation."

Now you can check the output with four yes/no questions:

- Does it sound professional? ✓
- Is it under 100 words? ✓
- Is the deadline date unchanged? ✓
- Is it just the email text, nothing extra? ✓

If any answer is no, you know exactly what went wrong and how to fix it [1].

## In Practice

Before submitting any specification to an AI tool, run it against these four questions:

- Can I tell if this worked or not? **(testable)**
- Did I set clear limits on what the AI should and should not touch? **(bounded)**
- Can I read the output and know straight away whether it worked? **(observable)**
- Does the AI have everything it needs to start without guessing? **(actionable)**

Missing any one of these is the most common reason AI output disappoints. Three mistakes students frequently make:

- **A longer instruction is not always a better one.** Only add words if they help with one of the four properties above. Extra words that do not serve any property make the instruction harder to follow [3].
- **One good result does not mean your specification is reliable.** Because AI can give a different answer each time, getting a good output once does not mean it will work again. Test your specification more than once before trusting it [2].
- **AI will not stop and ask you what you meant.** Unlike a classmate, it will silently fill in the gaps with its own guess — and you will have no idea it did that [1].

The four-property approach is not limited to AI. Software developers write "acceptance criteria" before building a feature — a well-known format is "Given [context], when [action], then [observable result]" — which maps directly onto testable, observable, and actionable. The same discipline turns up in data analysis, workplace delegation, and any situation where you need to communicate a task precisely to someone who cannot read your mind [2].

## Key Takeaways

- **Testable:** after every run, you should be able to say clearly — did this pass or fail? Include a condition you can check.
- **Bounded:** always set clear limits on what the AI should and should not touch so it stays within the task you gave it.
- **Observable:** the output should be something you can read and check straight away — no digging through vague responses or guessing required.
- **Actionable:** give enough detail so the AI can start the task immediately without filling in the gaps itself.
- All four properties work together — a specification needs to satisfy all four to produce a reliable result every time, not just once.

## References

1. MIT Sloan Educational Technology, "Effective Prompts for AI: The Essentials." <https://mitsloanedtech.mit.edu/ai/basics/effective-prompts/>
2. Lakera, "The Ultimate Guide to Prompt Engineering in 2026." <https://www.lakera.ai/blog/prompt-engineering-guide>
3. Project Management Institute, "A Simple Framework for Writing Better AI Prompts." <https://www.pmi.org/blog/how-to-write-better-prompts-framework>

---

# Bad spec vs good spec — 'make it better' vs 'rewrite at Grade 8 level, max 80 words'

## Overview

You now know the four properties a good specification must have: testable, bounded, observable, and actionable. The next question is what to do when a specification fails one or more of them. This topic gives you two repair strategies — a quick targeted fix for minor problems, and a full rewrite for specifications that are broken at their core — so you can turn a bad specification into a reliable one before the AI ever sees it [1].

## Key Concepts

### Diagnosing which property fails

Before you repair anything, you need to know exactly what is broken. A bad specification almost always fails one or more of the four properties. Use this table as a diagnostic tool [2]:

| Property | The question it asks | What a failure looks like |
|---|---|---|
| **Testable** | Can you check whether the output is correct? | "Write something good" — "good" has no measurable threshold |
| **Bounded** | Is the scope limited enough? | "Explain machine learning" — covers an entire field with no end |
| **Observable** | Is the output format specified? | "Give me feedback" — feedback as a list? As prose? On what? |
| **Actionable** | Can the AI start immediately? | "Help me" — no task, no subject, no direction |

Run the diagnostic in four questions, in order:

1. Can I write a simple test to check the output? (Testable)
2. Is there a clear finish line — a limit on length, scope, or topic? (Bounded)
3. Does the spec say what form the answer should take? (Observable)
4. Is there a concrete task the AI can start on right now? (Actionable)

Every "no" is a defect to repair [2].

### Strategy 1 — Incremental fix ("make it better")

The **incremental fix** means keeping the existing specification and adding specific words to address each failing property — one property at a time.

Use it when:
- Only **one or two** of the four properties fail.
- The core task is correct — only a constraint or a format is missing.
- The repair is an addition, not a structural change.

**How to apply it:**

1. Run the four-question diagnostic and mark each property pass or fail.
2. For each failing property, add the missing constraint directly to the specification.
3. Re-run the diagnostic on the revised version to confirm all four now pass.

One warning: adding vague words does not count as a fix. Changing "Write an email" to "Write a good email" adds a word but does not fix the testable property — "good" is still unmeasurable. Every fix must be concrete [1][2].

### Strategy 2 — Full rewrite (Grade 8 level, max 80 words)

Sometimes the specification is not just missing a constraint — the task itself is unclear, the vocabulary is too complex, or so many properties fail that patching them one by one takes longer than starting fresh [3].

The **Grade 8 / 80-word rewrite** is a complete replacement. You set aside the original wording entirely and write a new specification from scratch, following two hard constraints:

- **Grade 8 reading level** — plain words, short sentences. Imagine explaining the task to a capable 13-year-old. Avoid jargon and words that carry multiple possible meanings.
- **Maximum 80 words** — brevity forces clarity. If you cannot say what you want in 80 words, you have not finished thinking about what you want.

These two constraints work together: short sentences force you to be specific, and plain words force you to name the actual task rather than hiding behind vague verbs like "help," "discuss," or "address" [3].

**When to use the full rewrite:**

| Situation | Strategy |
|---|---|
| One or two properties fail, core task is clear | Incremental fix |
| Three or four properties fail | Full rewrite |
| Wording is ambiguous beyond repair | Full rewrite |
| Two rounds of incremental fixing have not produced a passing spec | Full rewrite |

The full rewrite is not an admission of failure — it is the faster path when the foundation is unsound [3].

### The decision rule

The choice between strategies comes down to one question: **how many of the four properties fail?**

- 0 failures — the specification is good. No repair needed.
- 1–2 failures — use the incremental fix: add the missing constraint or format.
- 3–4 failures — use the full rewrite: Grade 8 level, max 80 words.

## Worked Example

This example shows both strategies applied to real specifications, with the diagnostic step made visible.

**Incremental fix — two properties fail**

Original: *"Summarise the article."*

Diagnostic:
- Testable? No — "summarise" has no length or accuracy threshold.
- Bounded? No — no word limit.
- Observable? Partly — output is prose, but length is unknown.
- Actionable? Yes — clear verb, clear subject.

Two properties fail (testable, bounded). The core task is correct. An incremental fix is appropriate [1].

Fix: *"Summarise the article in no more than 50 words."*

Re-check: all four properties now pass. One targeted addition fixed two properties at once.

---

**Full rewrite — all four properties fail**

Original: *"Help me with my project."*

Diagnostic:
- Testable? No — "help" has no measurable outcome.
- Bounded? No — "project" could be anything.
- Observable? No — no output format.
- Actionable? No — no concrete task.

All four properties fail. Patching each one in turn would mean rewriting nearly every word — a full rewrite is faster [1][3].

Rewrite: *"List five steps to plan a 10-minute presentation for a school science project. Each step should take no more than two sentences to describe."*

Grade 8 check: short words, one idea per sentence, no jargon. Pass.
80-word check: the rewrite is 31 words. Pass.

All four properties pass:
- Testable — you can count five steps.
- Bounded — "10-minute presentation," "no more than two sentences."
- Observable — numbered list.
- Actionable — "List five steps to plan…"

## In Practice

Vague specifications cause problems in professional settings too — not just in student work. The same diagnostic and repair strategies apply wherever you are giving instructions to an AI tool [3].

**Content summarisation.** A marketing team asked an AI to "make the article shorter" and got outputs ranging from one sentence to ten paragraphs. Only one property failed (bounded). Incremental fix: "Reduce the article to 200 words, keeping the headline and the three main points." [1]

**Customer support prompts.** A support team's chatbot gave inconsistent answers because its system prompt said "be helpful and friendly." That fails testable (no accuracy threshold), bounded (no topic limit), and observable (no response format). Three properties fail — a full rewrite to "Answer customer questions about returns only. Give one direct answer in three sentences or fewer" was the right call [2][3].

**Common traps to avoid:**

- Do not use words like "comprehensive," "thorough," or "in-depth" — they are untestable by definition.
- Do not stack multiple tasks in one specification. Each task should be its own specification.
- Do not assume that adding more words makes a specification clearer. Length and clarity are not the same thing [3].
- Do not keep patching a specification that has already failed two rounds of incremental fixes. At that point, a rewrite is faster [2].

## Key Takeaways

- A bad specification almost always fails one or more of the four properties. Diagnosing which property fails is the first step of any repair.
- Use the **incremental fix** when one or two properties fail and the core task is correct — add the missing constraint without rewriting the whole specification.
- Use the **full rewrite** when three or four properties fail, when the wording is ambiguous beyond repair, or when two rounds of incremental fixing have not produced a passing specification.
- The **Grade 8 / 80-word rule** enforces precision: plain language removes ambiguity, and the 80-word limit forces you to have one clear task, one constraint, and one output format.
- The decision rule is simple: count the failures. 1–2 failures → incremental fix. 3–4 failures → full rewrite.

## References

1. Sai Charan Kummetha, "Few Examples of Bad Prompts and How to Improve Them." <https://saicharankummetha.medium.com/few-examples-of-bad-prompts-and-how-to-improve-them-e717a1087735>
2. MyGreatLearning, "5 Common Prompt Engineering Mistakes Beginners Make." <https://www.mygreatlearning.com/blog/prompt-engineering-beginners-mistakes/>
3. DigitalOcean, "Prompt Engineering Best Practices." <https://www.digitalocean.com/resources/articles/prompt-engineering-best-practices>

---

# How to identify the inputs, expected outputs, and failure conditions of a task

## Overview

You have learned that a good specification must be testable, bounded, observable, and actionable. Those four properties tell you how to judge a specification. This topic teaches you how to build one — specifically, how to find the three pieces a specification needs most: the inputs, the expected outputs, and the failure conditions. Most weak specifications are not wrong; they are incomplete. A key piece of information is missing, and the AI fills the gap with a guess [1].

## Key Concepts

A complete specification has six named parts. Each part answers one specific question about the task. This topic teaches three of those parts at full depth — the three that most directly determine whether an AI task succeeds or fails.

| Component | The question it answers |
|---|---|
| Task description | What is the AI supposed to do? |
| **Inputs** | What raw material does the AI need to start? |
| **Expected outputs** | What should the result look like? |
| Format and constraints | How should the result be structured and bounded? |
| **Failure conditions** | What counts as a problem, and how should the AI handle it? |
| Success criteria | How will I know the output is correct? |

Task description, format and constraints, and success criteria are each covered in companion topics in this module. The three in bold are the focus here.

---

### Component 1 — Inputs

**Inputs** are everything the AI needs to have — or needs to know — before it can start the task. An input is any piece of raw material, context, or data the AI will work with or work from.

Without clearly stated inputs, the AI either makes up material or applies the task to the wrong thing [1]. Both outcomes waste your time.

**Types of inputs you might specify:**

| Input type | Example |
|---|---|
| A document or text | "The email thread pasted below" |
| A data set or list | "The five product names listed here: ..." |
| Context about the audience | "The reader is a first-year university student" |
| A constraint on what to use | "Use only the paragraph above — do not use outside knowledge" |
| Background the AI needs | "The deadline is Friday. The client expects a draft, not a final version." |

An AI tool does not automatically know what document or context you mean. If you say "summarise this," the AI infers what "this" means from whatever is in front of it — which may not be what you intended. Naming the input removes that inference [2].

---

### Component 2 — Expected Outputs

**Expected outputs** describe what the AI should produce. They answer the question: "What will I actually receive when the task is done?"

Specifying the output makes the result **observable** — a property you learned in topic 2.1. An observable output is something you can read, count, or measure. An unobservable output is vague and unmeasurable [2].

Every expected output has three dimensions. All three should be explicit:

1. **Type** — What kind of thing is it? A numbered list? A paragraph? A table? A single sentence?
2. **Content** — What must the output contain? What must it not contain?
3. **Amount** — How many items, sentences, or words?

If any one dimension is left open, the AI will make a choice for you.

**A common mistake — specifying type but not content:**

*"Give me a list of ideas."*

Type is specified (a list). Content is not (ideas about what?). Amount is not (how many?). The output is still mostly unobservable because you cannot check whether the content is correct [2].

---

### Component 3 — Failure Conditions

**Failure conditions** are the situations in which the AI cannot — or should not — complete the task as specified, and what it should do instead.

This is the component most beginners leave out. Omitting it is one of the most common reasons AI outputs are unreliable in practice [3].

**Why failure conditions matter.** A human worker, when they hit a problem, stops and asks a question: "I cannot find that file — can you send it again?" An AI tool does not stop. It produces something anyway. Without failure conditions, the AI may:

- Make up missing information — a behaviour called **hallucination** (producing plausible-sounding but incorrect content).
- Silently skip a part of the task without telling you.
- Produce an output that looks complete but is based on wrong assumptions [3].

Specifying failure conditions gives the AI explicit instructions for those situations. Instead of guessing, it follows your rule.

**Three categories of failure conditions to cover:**

1. **Missing input** — What should the AI do if the input is incomplete or absent?
   - Example: *"If the product description is missing, write 'No description provided' and stop — do not invent a description."*

2. **Input outside scope** — What should the AI do if the input does not match what the task assumes?
   - Example: *"If the text is not in English, translate it first before summarising. If you cannot identify the language, state 'Language not recognised' and stop."*

3. **Ambiguous or conflicting content** — What should the AI do if the input contains contradictions or unclear information?
   - Example: *"If the complaint refers to two different orders, address only the most recent one. Flag the second by writing 'Note: a second order was mentioned but not addressed.'"*

In topic 2.1 you learned that AI tools are probabilistic — they do not always give the same answer twice. Failure conditions reduce that variability at the edges of a task, where the input is messy or incomplete [2][3].

## Worked Example

**Task:** You want an AI to write a brief summary of a job applicant's cover letter for a hiring manager to read before an interview.

Here is how you identify and write the three components step by step.

---

**Step 1 — Identify the inputs.**

Ask: "What does the AI need to have before it can start?"

- The full text of the cover letter (pasted below the specification).
- Context: the role is a junior data analyst position. The hiring manager has 3 minutes to read the summary before the interview.

Both pieces are included because the AI needs the raw material (the letter) and the context (the role and time constraint) to do the task correctly [1].

---

**Step 2 — Describe the expected output.**

Ask: "What will I actually receive — type, content, and amount?"

- **Type:** three bullet points.
- **Content:** each bullet covers one thing in order — (1) the applicant's relevant experience, (2) their stated motivation for applying, (3) one specific skill or achievement they highlight.
- **Amount:** each bullet is one sentence.

All three dimensions are named, so the output is observable and checkable [2].

---

**Step 3 — Write the failure conditions.**

Ask: "What could go wrong with the input?"

- If the cover letter does not mention relevant experience, write "No relevant experience mentioned" for bullet 1.
- If the cover letter is fewer than 50 words, write "Cover letter too short to summarise reliably" and stop.
- If the cover letter is not in English, state "Cover letter is not in English — translation required" and stop.

Each failure condition names a concrete situation and a concrete response. The AI cannot guess when any of these situations occurs [3].

---

With these three components identified and written, the specification has no gaps in the areas that most directly affect whether the task succeeds or fails.

## In Practice

The six-component approach is used by professional software teams, data science teams, and AI product teams — not just for individual prompts, but for building the instructions that run AI systems continuously [1].

**Common anti-patterns to avoid:**

| Anti-pattern | The problem | The fix |
|---|---|---|
| No inputs stated | AI guesses what to work with | Name every piece of raw material explicitly |
| Output type only, no content | "A list" without specifying what it must contain | Add content and amount alongside type |
| No failure conditions | AI hallucinates or silently skips steps | Add at least one rule per failure category |

**Do:**

- Write inputs, expected outputs, and failure conditions every time — even for small tasks. Skipping a component because the task "seems simple" is how gaps appear.
- Write failure conditions *before* you send the specification. It is easier to think about what could go wrong when you are not yet looking at a bad output.
- Re-read your specification as if you are the AI and know nothing else. Every question you find yourself asking is a gap to fill [1].

**Don't:**

- Do not assume the AI will ask for clarification when inputs are missing. Most AI tools will proceed and guess. Write the failure condition yourself [3].
- Do not leave expected outputs vague — "give me a list" without specifying content or length is still incomplete.

Production AI systems — customer-service assistants, summarisation tools, classification systems — use explicit failure conditions as a reliability mechanism. Without them, a system handling thousands of queries per day will encounter unusual inputs, missing data, or off-topic questions and produce unpredictable outputs [2]. Research into AI agent failures shows that many trace back to missing inputs, no rule for when to stop, and outputs that look correct but violate an unstated constraint [3].

## Key Takeaways

- A complete specification has six components. This topic focuses on the three that most directly determine success: **inputs**, **expected outputs**, and **failure conditions**.
- Inputs tell the AI what raw material to work with. Without them, the AI guesses — often incorrectly.
- Expected outputs make the result observable. Specify the type, content, and amount of what you expect to receive.
- Failure conditions are the most commonly skipped component and the one most directly responsible for AI unreliability. An AI without failure conditions will guess when inputs are missing, ambiguous, or out of scope.
- Writing all three components together closes the most common gaps that cause AI tasks to produce wrong or unpredictable outputs [1][2][3].

## References

1. Mohit Wani, "Specification-Driven Development." <https://medium.com/@wanimohit1/specification-driven-development-how-ai-is-transforming-software-engineering-c01510ea03e3>
2. LaunchDarkly, "Prompt Engineering Best Practices." <https://launchdarkly.com/blog/prompt-engineering-best-practices/>
3. Galileo AI, "AI Agent Failure Modes Guide." <https://galileo.ai/blog/agent-failure-modes-guide>

---

# The 70/30 rule — AI implements, you specify and verify

## Overview

When you work with an AI tool, the work does not split evenly. Roughly 70 percent of an AI-assisted task is implementation — producing the draft, running the calculation, generating the summary. AI does that part. The remaining 30 percent is specification and verification — deciding exactly what you need and then checking that you got it. That part belongs to you [1]. This split matters because speed is not the same as correctness: an AI can produce a polished-looking output in seconds that still fails to meet your actual requirements. Understanding this division of responsibility is what separates a reliable AI workflow from a lucky one [2].

## Key Concepts

### What the 70/30 rule says

The **70/30 rule** is a professional guideline for working with AI tools [1]. It divides every AI-assisted task into two parts:

- **The 70 percent — implementation.** This is where output is actually produced: text is drafted, data is sorted, information is retrieved. AI handles this part. It is fast, consistent, and tireless at generating content at scale.
- **The 30 percent — specification and verification.** This is where a human decides what the task is, sets the quality bar, sends the instruction, and then checks the result. You handle this part.

The name "70/30" is a label, not an exact measurement. Some tasks split 80/20; others 60/40. The exact numbers are not the point. The principle is: **AI does the bulk of the producing; the human does all of the deciding and checking** [2].

This pattern holds whether you are using AI to draft an email, summarise a document, generate a quiz question, or analyse a dataset. In every case: you specify, AI implements, you verify.

---

### Your role 1 — Specify

**Specification** — deciding exactly what you need before you prompt the AI — is the first human role in the rule [1].

You already know from Topics 2.1 and 2.3 what a good specification contains: it is testable, bounded, observable, and actionable, and it names inputs, expected outputs, and failure conditions. In the context of the 70/30 rule, the key insight is this: **the quality of the AI's output is almost entirely determined by the quality of your specification**. A vague instruction produces a vague result. A precise instruction gives the AI a clear target [2].

Specifying well means four things, in order:

1. **Decide what you actually need.** Not "have AI help me with the report" — but "summarise the key financial findings from pages 4–9 in five bullet points, each under 30 words, for a non-specialist reader."
2. **Set the constraints.** What format? What length? What should be excluded?
3. **Define the success condition.** What does a correct output look like? This is testability from Topic 2.1 applied directly to AI work.
4. **Write it down.** A specification in your head is not a specification. It cannot be checked, shared, or improved.

When you complete these four steps before opening the AI tool, you have done the first half of your 30 percent [3].

---

### Your role 2 — Verify

**Verification** — checking whether the AI's output actually meets your specification — is the second human role [1].

This step is not optional. Here is why: AI systems are probabilistic (from Topic 1.3). They produce outputs that are statistically likely to match the patterns they were trained on — not outputs guaranteed to match your specific requirements. An output can look polished and confident while still being wrong for your purpose [2].

**Verification is not the same as reading the output.** Reading is passive — your eye moves over the text. Verification is active — you check each part of the output against each part of your specification.

Here is what verification looks like in practice:

1. **Check against your success condition.** Did the output meet the testable criterion you set? Count the bullet points. Measure the word count. Confirm the format.
2. **Check scope.** Is everything that should be included, present? Is everything that should be excluded, absent?
3. **Check factual accuracy.** AI can state incorrect facts with total confidence. If your task involves names, dates, figures, or references — check them against a reliable source.
4. **Check for failure conditions.** In Topic 2.3 you learned to define failure conditions in advance. Now is when you look for them in the actual output.
5. **Decide: accept, revise the output, or revise the specification.** If the output is wrong because the AI made an error, ask for a correction. If the output is wrong because your specification had a gap, fix the specification and resubmit. Either way, this is still your 30 percent [3].

---

### Why the split matters

Why does it matter who does which part? The answer comes down to what AI is good at — and what it is not good at.

**What AI is good at:**

- Producing large amounts of text quickly.
- Following an explicit format.
- Retrieving and recombining information from patterns it was trained on.
- Being consistent across many repetitions of the same task.

**What AI is not good at:**

- Knowing what you actually need (it cannot read your mind).
- Knowing your audience, your standards, or your context (those are not in the training data).
- Guaranteeing factual accuracy (it generates statistically likely text, not verified facts).
- Detecting its own errors (it has no self-awareness of mistakes).

The 70/30 rule puts each capability where it belongs. AI handles the volume of production it is fast and consistent at. You handle the judgment, context, and accountability that only you can provide [1][2].

| Responsibility | Who does it | Why |
|---|---|---|
| Decide what the task is | Human | AI does not know your context or goals |
| Write the specification | Human | AI cannot set its own quality bar |
| Produce the output | AI | Fast, consistent, tireless at generation |
| Check the output against the spec | Human | AI cannot reliably audit its own output |
| Accept, reject, or revise | Human | Accountability rests with the person, not the tool |

---

### The verification loop

![The 70/30 rule — Human: Specify and Verify vs AI: Implement, with loop-back on failure](../../../../../../../../CIT/content-gen-example/content/m1-computational-thinking/week-2/3-the-professional-rules-of-ai-use/2-5-the-70-30-rule-ai-implements-you-specify-and-verify/artifacts/diagram.png)
*The full 70/30 workflow: your 30% (write spec → verify → revise) wraps around the AI's 70% (implement), looping back until the output meets the specification.*

In practice, the 70/30 rule is not a straight line — it is a loop [3].

1. You write a specification.
2. AI produces an output.
3. You verify the output against your specification.
4. If the output does not meet the specification, you either:
   - **Revise the output** — ask the AI to correct a specific part.
   - **Revise the specification** — the gap was in your original instruction, so you fix that part and resubmit.
5. You verify again.
6. When the output meets every criterion in the specification, the loop ends.

Each pass through the loop is still your 30 percent doing its job. A well-written specification typically takes one to three iterations. A vague one takes many more — which is exactly why investing time in specification up front saves time overall [1].

## Worked Example

Here is the full process applied to a real task: summarising customer feedback.

**The task:** You have a list of customer feedback from one week and you need a summary for your manager.

**Step 1 — Define the task.**
Write one sentence naming what you need: "I need a summary of customer feedback received this week."

**Step 2 — Write the full specification.**
Apply the four properties from Topic 2.1:

- **Testable:** "Each piece of feedback must be categorised as positive, neutral, or negative."
- **Bounded:** "Cover only feedback received Monday through Friday this week. Do not include previous weeks."
- **Observable:** "Produce a table with three columns: date, feedback quote (under 20 words), category."
- **Actionable:** Paste the actual feedback text into the prompt, or specify clearly where the AI should find it.

**Step 3 — Send the specification and receive the output.**
This is the AI's 70 percent. Do not edit the output yet — receive it as-is first.

**Step 4 — Verify the output against your specification.**
Go through every criterion:

- Is every row categorised? (testable)
- Are all dates within Monday–Friday this week? (bounded)
- Are all feedback quotes under 20 words? (observable)
- Does the table have exactly three columns? (observable)

**Step 5 — Accept, revise the output, or revise the specification.**

Suppose you find two feedback quotes that are 25 words, not 20. You have two options:

- Ask the AI to shorten those two quotes (revise output).
- Decide that "under 25 words" is actually fine and update your specification accordingly (revise specification).

Either way, you verify once more before accepting [2][3].

**What changed:** the first output had two quotes over length. After one revision loop, all quotes met the criterion. That is the loop in action — and the specification is what made the error detectable.

## In Practice

**Do:**

- Write your specification before you open the AI tool — not while you are typing in the prompt box.
- Treat every piece of AI output as a draft that requires verification, not a finished product.
- When the AI output is wrong, ask first: "Is this a specification gap or an AI error?" The answer determines your next step.
- Keep a record of your specification alongside your final output — you may need to explain your process later [1].

**Do not:**

- Skip verification because the output "looks right." Looking right is not the same as being right.
- Run the same prompt a second time and expect it to catch the errors from the first run — it may produce different errors instead.
- Outsource the specification to AI. Asking the AI "tell me what to ask you" transfers your 30 percent to the system that cannot perform it reliably [2][3].

| Do | Do not |
|---|---|
| Write the spec before prompting | Wing it and fix later |
| Verify output against each criterion | Skim for plausibility |
| Revise the spec when you find a gap | Blame the AI and give up |
| Own the final output as yours | Treat AI output as automatically authoritative |

**Where you will see this pattern outside AI tools:**

- **Software testing.** Engineers use automated tools to run thousands of test cases (the AI-equivalent 70 percent). But a human writes the test cases, defines pass and fail, and decides whether the results are acceptable [1].
- **Data journalism.** A journalist uses a tool to process a large dataset and generate charts. The tool does the number-crunching. The journalist specifies which data to include, verifies the charts are accurate, and decides whether the findings tell the expected story [2].
- **Healthcare support tools.** An AI diagnostic assistant flags potential conditions based on patient data. A qualified clinician specifies the parameters, reviews the flags, and makes the final medical judgment. The AI handles scale; the clinician handles accountability [3].

In every case, the pattern is identical: a human sets the standard, a system does the production, and the human checks the result. The technology changes; the division of responsibility does not.

## Key Takeaways

- The **70/30 rule** says AI handles roughly 70 percent of an AI-assisted task (implementation — generating output), while the human handles roughly 30 percent (specification and verification — deciding what is needed and checking the result).
- Your two roles are **specifying** (writing a clear, bounded, testable instruction before you prompt the AI) and **verifying** (checking each part of the output against that specification after you receive it).
- Verification is not optional. AI output looks confident even when it is wrong. Only a human checking against a specification can reliably catch the gap [1].
- The 70/30 split is not about reducing your effort — it is about placing human judgment and accountability exactly where AI cannot substitute for it [2].
- The process is a **loop**: specify → AI implements → verify → revise specification or output → verify again. A strong specification shortens the loop; a vague one lengthens it [3].

## References

1. Generative Inc., "What is the 30 Rule in AI." <https://www.generative.inc/what-is-the-30-rule-in-ai>
2. Alta HQ, "Mastering the 30 Rule for AI: A Comprehensive Guide to Human-AI Collaboration in 2026." <https://www.altahq.com/post/mastering-the-30-rule-for-ai-a-comprehensive-guide-to-human-ai-collaboration-in-2026>
3. Intersog, "What is the 30 Rule in AI." <https://intersog.co.il/blog/what-is-the-30-rule-in-ai/>

---

# When NOT to use AI — privacy, precision, legal accountability

## Overview

AI is genuinely useful — it can draft text, summarise long documents, and suggest ideas quickly. But there are tasks where using AI is the wrong choice, not because AI is broken, but because the situation has constraints that AI cannot satisfy. Knowing when *not* to use a tool is just as important as knowing how to use it well. This topic gives you three specific reasons to say "no" to AI — privacy, precision, and legal accountability — and a quick three-question check you can apply to any professional task.

## Key Concepts

### Reason 1: Privacy — when data is sensitive or confidential

**Sensitive data** is any information that could harm a person, an organisation, or a relationship if it became known to others. Examples include:

- A patient's medical history
- A client's legal case details
- A student's academic records
- A company's financial plans not yet made public

When you type information into an AI tool — a chat interface, a writing assistant, a summarisation tool — that information typically leaves your device. It travels to a server run by the company that built the tool. Depending on the tool's settings, that information may be [1][2]:

- stored temporarily or permanently on that server,
- used to improve the AI model for future users, or
- accessible to the tool provider's staff under certain conditions.

This is the core privacy risk: **you do not control what happens to the data once it leaves your hands** [2]. The moment you press "send", you have transferred something to a third party — and you cannot take it back.

**Consumer tools vs. professional tools.** Consumer AI tools (the free or low-cost tools anyone can sign up for) are not designed to protect confidential professional data [1]. They carry the same privacy risks as typing a client's name and case details into a public discussion forum [1]. Professional-grade AI tools — sometimes called enterprise or business-tier tools — may offer stronger data-handling contracts. But even a professional tool does not automatically make sensitive data safe; the organisation's own data-handling policy must be checked first [2].

**The rule of thumb.** Before using any AI tool, ask: "Would I be comfortable if this data were visible to a stranger?" If no, do not paste it into the tool [2].

Two laws that define what "sensitive" means in specific industries:

- **HIPAA** (Health Insurance Portability and Accountability Act, pronounced "HIP-ah") — a United States law governing how health information may be stored, shared, and handled.
- **GDPR** (General Data Protection Regulation) — the European equivalent. You will study these regulations in later topics.

---

### Reason 2: Precision — when a plausible-but-wrong answer causes serious harm

You learned in topic 2.4 that AI produces **probabilistic output** — an answer that represents the most likely response based on patterns, not a guaranteed correct answer. The same question asked twice can produce slightly different answers.

For many tasks, a "usually right" answer is fine. If an AI helps you brainstorm project name ideas and three out of five are good, the stakes are low. But some tasks require **exact precision** — an answer that is either completely correct or must not be acted upon.

**What counts as high-precision-required?**

| Task type | Why exactness matters |
|---|---|
| Drug dosage calculation | A wrong dose — too high or too low — directly harms the patient. |
| Financial audit figures | A rounding error carries legal and financial consequences. |
| Navigation coordinates for aviation | A small error means a dangerous course deviation. |
| Legal contract clause interpretation | Misreading a clause can create binding obligations the client never agreed to. |
| Medical diagnosis | An incorrect diagnosis leads to the wrong treatment, causing harm. |
| Structural load calculations | An error in engineering figures can make a building or bridge unsafe. |

What makes AI specifically dangerous in these situations is that it produces its wrong answers **confidently** [3]. An AI does not say "I am not sure" — it says "The dosage is 500 mg" in the same tone whether it is correct or not. This is called **hallucination** — a term you will encounter more in later topics — where an AI produces a plausible-sounding but factually incorrect output without signalling any uncertainty.

This connects directly to the verification loop from topic 2.5: when precision is required, the human verification step is not optional — it is what prevents a confident-but-wrong AI answer from causing harm.

**The rule of thumb.** Ask: "If the AI's answer is 5% wrong, would that cause serious harm?" If yes, do not use AI as the source of the final answer. A human expert must verify it against a reliable, auditable source.

---

### Reason 3: Legal accountability — when a human must be legally responsible

**Legal accountability** means that a specific person or organisation is formally responsible — in the eyes of the law — for a decision and its consequences. If the decision causes harm, that responsible person can face legal action: a fine, a lawsuit, or professional sanction such as losing their licence to practise.

AI tools cannot be held legally accountable. An AI system is software [1]. It does not hold a professional licence. It cannot appear before a court. It cannot be fined, imprisoned, or struck off a professional register (removed from the official list of people licensed to practise their profession). Because it cannot be held responsible, it cannot fulfil the role that law and professional regulation have created for licensed humans [1].

Some professions exist inside a framework of legal responsibility:

- A licensed doctor is accountable for clinical decisions.
- A licensed solicitor (lawyer) is accountable for the legal advice they give a client.
- A certified financial adviser is accountable for investment recommendations.

When someone uses AI to produce an output and presents that output as their own professional advice, the legal responsibility still falls on the human [1]. There is no way for a professional to transfer their accountability to a piece of software. But here is the deeper problem: **if the AI's output is wrong and a human relied on it without verifying it, the harm has already occurred** — and the human professional faces the consequences [1][3]. The AI cannot be sanctioned. Only the human can.

**The rule of thumb.** Ask: "Could I — or my organisation — face legal consequences if this AI output is wrong?" If yes, a qualified human must review and own the final decision. The AI can assist with drafting or research, but the human must be the accountable last step.

---

### Putting the three reasons together: the three-question check

Before using AI on any professional task, run this quick check:

1. **Privacy check** — Does this task involve sensitive or confidential data? If yes, use only an approved, data-compliant platform — one that meets your profession's data-privacy rules — or stop. Do not use a consumer AI tool [1][2].

2. **Precision check** — Does this task require an exact, verified answer where a plausible-but-wrong answer would cause serious harm? If yes, do not rely on AI as the final source of truth. A human expert must verify the output against an authoritative, auditable source [3].

3. **Legal accountability check** — Does this task require a person to be legally responsible for the output? If yes, a qualified human must own and sign off on the final decision. AI can assist in drafting and research only [1].

If the answer to any question is "yes", either (a) do not use AI, or (b) use AI only as a drafting aid with a mandatory human verification step [1][2][3].

The diagram below shows how the three checks form a decision path for any task:

![Three-Question AI Use Check](../../../../../../../../CIT/content-gen-example/content/m1-computational-thinking/week-2/3-the-professional-rules-of-ai-use/2-6-when-not-to-use-ai-privacy-precision-legal-accountability/artifacts/diagram.png)
*The three-question check as a decision tree: each gate checks one dimension (privacy, precision, legal accountability); a YES at any gate triggers a specific constraint; only three NOs together mean AI use is appropriate.*

Notice that the three checks can overlap. A clinical diagnosis involves all three: the data is sensitive (patient health information), the output requires precision (the wrong diagnosis causes harm), and a licensed physician must be legally accountable for the diagnosis. When two or more checks apply simultaneously, the constraint on AI use is even stronger.

## Worked Example

**Scenario: the fabricated case citation**

A junior lawyer is preparing a legal brief. She asks an AI tool to research relevant court precedents — past rulings that could support her client's argument. The AI returns a list of cases with confident summaries. She incorporates three of them into the brief without individually checking whether the cases exist.

When the opposing counsel and the judge review the brief, they discover that one of the cited cases does not exist. The AI had hallucinated it — constructed a plausible-sounding case name, court, date, and ruling from patterns in its training data.

Here is what the three-question check would have caught before she started:

| Check | Answer | What it means |
|---|---|---|
| Privacy check — sensitive data? | **Yes** — client's legal strategy and confidential details are in the research query | Consumer AI tool is not appropriate; use a data-compliant platform or research manually |
| Precision check — serious harm if wrong? | **Yes** — a fabricated citation in a filed brief exposes the client and the lawyer | AI output must be verified against official legal databases before use |
| Legal accountability check — licensed human responsible? | **Yes** — the lawyer, not the AI, is accountable for every document filed | The lawyer must actively review every cited case and formally sign off |

The AI produced the error. The lawyer — not the AI — faces the consequences: potential reprimand by the bar association (the professional body that regulates lawyers), a costs order (a court ruling requiring one party to pay the other's legal costs), or in serious cases, suspension [1].

The output quality of the AI's other citations does not change this. Even if nine out of ten citations were accurate, the failure to run the check — and to verify each result — is what turns AI from a useful drafting aid into a professional liability.

## In Practice

The three checks apply consistently across professional domains:

**Healthcare**

- All three checks typically apply simultaneously in clinical settings [3].
- Hospitals using AI for appointment scheduling or note summarisation must use HIPAA-compliant platforms.
- Any AI-generated clinical content requires physician review before it becomes part of a patient's record [3].
- AI-generated clinical recommendations can appear plausible while containing factual errors a trained clinician would catch [3].

**Legal practice**

- The ABA (American Bar Association) has issued formal guidance warning lawyers that using consumer AI tools with client information creates real privacy and confidentiality risks [1][2].
- A lawyer's professional duty of confidentiality extends to third-party tools: pasting client data into a consumer AI tool may itself constitute a breach of that duty [2].
- The lawyer remains responsible for the accuracy of every document filed; AI assistance does not reduce that responsibility [1][2].

**Financial services**

- Regulatory frameworks in most jurisdictions require that any investment recommendation given to a retail client be reviewed and approved by a licensed human adviser [1].
- An AI-generated portfolio recommendation cannot be handed directly to a client as professional advice.
- Financial data — account balances, transaction histories, personal financial circumstances — is also sensitive data under privacy regulations, so the privacy check applies alongside the accountability check.

**Safety-critical engineering and software**

- A software team using AI to auto-generate code for a safety-critical system (such as medical device firmware) must have a qualified engineer review every line — a precision error in safety-critical code can be catastrophic.
- An AI-generated error in a load-bearing structural calculation, if acted on without expert verification, creates physical risks that no disclaimer in an AI tool's terms of service would mitigate.

**Quick reference: when AI is and is not appropriate**

| Situation | Appropriate AI use? |
|---|---|
| Drafting an internal memo with no client names | Yes — low privacy risk, low stakes |
| Summarising a client's confidential contract | No — privacy risk [1][2] |
| Generating a rough estimate for a non-critical budget | Yes, if treated as a draft for review |
| Calculating a medication dosage for a patient | No — precision and accountability risk [3] |
| Brainstorming ideas for a marketing campaign | Yes — no sensitive data, low stakes |
| Writing a legal opinion for a client | No — accountability; needs licensed human review [1] |

## Key Takeaways

- AI is inappropriate when the task involves **sensitive or confidential data** — sharing that data with a consumer tool removes your control over it [1][2].
- AI is inappropriate when the task demands **exact precision** and a plausible-but-wrong answer would cause serious harm — AI's probabilistic output does not guarantee correctness [3].
- AI is inappropriate as the final decision-maker when the task requires **legal accountability** — only a licensed human professional can own that responsibility [1].
- The **three-question check** (privacy, precision, legal accountability) gives you a quick, repeatable way to decide whether AI is appropriate for any given task.
- Saying "no" to AI for certain tasks is not a failure — it is the professional judgment that your specification and verification skills are designed to support.

## References

1. Thomson Reuters. "The Consumer vs. Professional AI Privacy Standards for Legal Work." <https://legal.thomsonreuters.com/blog/the-consumer-vs-professional-ai-privacy-standards-for-legal-work/>
2. American Bar Association. "Privacy Risks of AI: Your Data, Their Knowledge." *GPSolo Magazine*, Mar–Apr 2025. <https://www.americanbar.org/groups/gpsolo/resources/magazine/2025-mar-apr/privacy-risks-ai-your-data-their-knowledge/>
3. National Institutes of Health / PubMed Central. "HIPAA Liability in the Age of Generative AI." PMC12859502. <https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12859502/>

---

# Writing Specifications Across Five Domains — Health, Transport, Education, Food, Scheduling

## Overview

You have learned what makes a specification good: it must be testable, bounded, observable, and actionable. Now it is time to put those properties to work across real tasks. This reading walks through five everyday domains — health, transport, education, food, and scheduling — showing how the same four-part structure applies in each one. What changes from domain to domain is not the structure itself, but the *type* of constraint that makes a spec bounded and the *type* of output that makes it observable [1].

## Key Concepts

### The Four-Part Structure Every Strong Specification Shares

Before looking at the five domains, here is the one template that covers all of them. Every strong specification contains four parts — no more, no less [1]:

| Part | What it does | Signal words |
|---|---|---|
| **Task statement** | Names the action and its subject | "Summarise…", "Generate…", "List…", "Identify…", "Create…" |
| **Context** | Gives the background the AI needs to act correctly for *your* situation | "for a 12-year-old", "using only the attached timetable", "based on UK supermarket ingredients" |
| **Constraints** | Sets the fences — what is in, what is out, how long, what format | "no more than 3 items", "do not include X", "under 150 words", "use a numbered list" |
| **Expected output format** | Describes the concrete thing you will receive | "a table with columns A and B", "a plain-English paragraph", "a numbered list of steps" |

These four parts map directly onto the properties you already know:

- Task statement + context → **actionable** (the AI has enough to start without guessing)
- Constraints → **bounded** (scope and limits are explicit)
- Expected output format → **observable** (you know what you will receive and can check it)
- All four together → **testable** (you can verify the output against what you asked for)

If any part is missing, the AI fills the gap with a guess — and that guess usually does not match your situation [3].

---

### Domain 1 — Health

Health tasks often involve personal numbers: step counts, blood pressure readings, calorie totals, medication schedules. A spec in this domain must be precise about the **metric** (which number), the **time range** (which days or period), and the **output shape** (a list, a table, a set of sentences).

- "Bounded" in health usually means: which metric, over which time period, for which population.
- "Observable" in health means: a concrete list, table, or set of reported data points — not "health advice" or a vague "overview."

**Weak specification:**
> "Help me understand my health data."

**Strong specification:**
> "I have a table of my daily step counts for the last 14 days (attached). Identify the three days with the lowest step counts. For each of those days, write one sentence stating the date and the count. Do not give health advice or suggest causes — just report the three data points."

| Part | What it provides |
|---|---|
| Task statement | "Identify the three days with the lowest step counts" |
| Context | "daily step counts for the last 14 days (attached)" |
| Constraints | three days only; one sentence per day; no health advice; no suggested causes |
| Expected output format | three sentences, each stating a date and a count |

**What changed:** "Understand" is not observable — it describes a mental state, not a deliverable. The strong spec replaces it with a specific action (identify, report). The data source is named. The output is limited to three data points in a fixed sentence format. The constraint "do not give health advice" keeps the AI from producing output that requires professional judgment [2].

---

### Domain 2 — Transport

Transport tasks involve routes, times, distances, and comparisons between options. Getting them right depends on fixing the journey completely before the AI acts.

- "Bounded" in transport means: start point, end point, date and time, mode of travel, and number of options.
- "Observable" in transport means: a route, a schedule table, or a comparison — not a general discussion of travel options.

**Weak specification:**
> "Tell me how to get to the airport."

**Strong specification:**
> "I need to travel from Liverpool Street Station, London, to Heathrow Airport Terminal 2 on a weekday morning, arriving by 07:30. List the two fastest public transport options that arrive by 07:30. For each option, state: the route name or number, the departure time from Liverpool Street, the arrival time at Terminal 2, and the number of changes required. Present this as a table with those four columns."

| Part | What it provides |
|---|---|
| Task statement | "List the two fastest public transport options" |
| Context | "Liverpool Street to Heathrow Terminal 2, weekday morning, arrive by 07:30" |
| Constraints | two options only; public transport only; arrival by 07:30 |
| Expected output format | a table: route name, departure time, arrival time, number of changes |

**What changed:** The weak spec gives the AI no journey details at all — it will either ask follow-up questions or pick defaults that may not match your situation. The strong spec names the exact origin, destination, terminal, day type, arrival deadline, and number of options. The table format means you can compare results directly the moment you read them [1].

---

### Domain 3 — Education

Education tasks involve explaining, assessing, or teaching content. The most common failure here is leaving the **audience** undefined — the AI then picks a default age and knowledge level that may not fit.

- "Bounded" in education means: the audience's age or knowledge level, the subject, the length of the output, and what should be excluded (such as advanced content or technical formulas).
- "Observable" in education means: a set of questions, an explanation in plain text, a lesson plan with named sections — not "an engaging lesson."

**Weak specification:**
> "Explain photosynthesis."

**Strong specification:**
> "Explain photosynthesis for a 12-year-old who has no prior science knowledge. Cover only these three points: (1) what photosynthesis is in one plain-English sentence, (2) what the plant needs as inputs (sunlight, water, carbon dioxide), and (3) what the plant produces (glucose and oxygen). Do not use chemical formulas or scientific terminology beyond these terms. Keep the total response under 150 words."

| Part | What it provides |
|---|---|
| Task statement | "Explain photosynthesis" |
| Context | "for a 12-year-old with no prior science knowledge" |
| Constraints | three points only; no formulas; no extra terminology; under 150 words |
| Expected output format | three numbered points in plain English |

**What changed:** The audience was defined precisely — same subject, very different output for a biology student versus a 12-year-old. The scope was limited to exactly three conceptual points. Advanced content was explicitly excluded. A word limit was set. The AI now has no room to expand beyond what was asked [3].

---

### Domain 4 — Food

Food tasks include recipe generation, meal planning, and ingredient substitution. The word "healthy" is one of the most common sources of vague food specs — it means different things to different people.

- "Bounded" in food means: dietary requirements (vegetarian, nut-free, low-sodium), serving size, preparation time, and ingredient source.
- "Observable" in food means: a recipe with an ingredients list and numbered steps, a shopping list, or a meal plan table — not a discussion of nutrition.

**Weak specification:**
> "Give me a healthy dinner recipe."

**Strong specification:**
> "Generate one dinner recipe that: (1) is vegetarian with no nuts, (2) serves two people, (3) takes no more than 30 minutes to prepare and cook, (4) uses only ingredients commonly found in a UK supermarket. Write the recipe as a numbered list of steps. Include a separate ingredients list at the top with quantities. Do not include a nutritional breakdown."

| Part | What it provides |
|---|---|
| Task statement | "Generate one dinner recipe" |
| Context | "vegetarian, no nuts, serves two, UK supermarket ingredients" |
| Constraints | 30 minutes max; no nuts; one recipe only; no nutritional breakdown |
| Expected output format | ingredients list first, then numbered steps |

**What changed:** "Healthy" was replaced with measurable criteria (vegetarian, no nuts, 30-minute limit). The serving size was fixed. The ingredient source was bounded to a specific context — this prevents the AI from suggesting exotic items that are hard to find. The explicit exclusion of the nutritional breakdown stops the output from expanding beyond what is needed [2].

---

### Domain 5 — Scheduling

Scheduling tasks organise time: timetables, task allocation, meeting slots, to-do prioritisation. The common failure is giving the AI the task name without the time information it needs to produce anything usable.

- "Bounded" in scheduling means: the time window, each task with its duration, fixed commitments already in the calendar, and the deadline.
- "Observable" in scheduling means: a timetable, a calendar block list, or a prioritised task table — not a general recommendation about time management.

**Weak specification:**
> "Help me plan my week."

**Strong specification:**
> "I have the following five tasks to complete before Friday 5pm: (A) write a 500-word report — 2 hours; (B) respond to 10 emails — 1 hour; (C) prepare a 10-slide presentation — 3 hours; (D) attend a 1-hour team meeting on Wednesday at 14:00 (fixed); (E) review a contract document — 1.5 hours. I work 09:00–17:00 Monday to Friday with a 1-hour lunch break each day. Create a day-by-day schedule that fits all five tasks into my available working hours. Present it as a table with columns: Day, Time slot, Task."

| Part | What it provides |
|---|---|
| Task statement | "Create a day-by-day schedule" |
| Context | "five named tasks with durations, Mon–Fri 09:00–17:00, 1-hour lunch, deadline Friday 17:00" |
| Constraints | all five tasks must fit; 1-hour lunch each day; meeting D is fixed Wednesday 14:00 |
| Expected output format | table with columns: Day, Time slot, Task |

**What changed:** Every task was named and given a duration. Working hours and lunch were defined. A hard deadline was set. A fixed event was identified so the AI knows it cannot move it. The table format makes the schedule directly usable. The AI now has a complete picture of the constraints and can produce a concrete, checkable result [1].

---

### What Stays the Same — and What Changes

After reading the five examples above, the pattern becomes clear.

**What does not change across domains:**

- The four-part structure (task statement, context, constraints, expected output format) appears in every domain.
- A strong spec always replaces vague quality words — "healthy," "best," "appropriate," "fast" — with measurable, domain-specific criteria.
- A strong spec always names a concrete output format so you know exactly what you will receive.

**What does change across domains:**

| Domain | What "bounded" means here | What "observable" means here |
|---|---|---|
| Health | Which metric, which time range | A reported list or table of data points |
| Transport | Origin, destination, date/time, mode, number of options | A route or comparison table |
| Education | Audience level, subject scope, excluded content | A numbered explanation, a set of questions |
| Food | Dietary restrictions, serving size, prep time, ingredient source | An ingredients list + numbered steps |
| Scheduling | Time window, task durations, fixed commitments, deadline | A timetable or calendar table |

A useful habit: after writing a spec in any domain, ask "What could go wrong if I left one of my constraints vague?" That question turns a reasonable spec into a strong one [3].

## Worked Example

Here is the four-part process applied step by step to a scheduling task — the same process works for any domain.

**Situation:** You have three pieces of work to finish by end of day Thursday, and you are free 10:00–16:00 Tuesday and Wednesday.

**Step 1 — Write the task statement.**
Name the action and the subject. "Create a time-block schedule for three tasks."

**Step 2 — Add domain context.**
Answer: "What background does the AI need to produce the right result for *my* situation?"
- Tasks: (A) draft a project proposal — 2 hours; (B) read 30 pages of a report — 1.5 hours; (C) write 10 follow-up emails — 1 hour.
- Available time: Tuesday 10:00–16:00 and Wednesday 10:00–16:00 (both days have a 30-minute break at 12:30).
- Deadline: Thursday end of day.

**Step 3 — Add constraints.**
"All three tasks must be scheduled. Each block must be at least 30 minutes (no splitting into tiny fragments). Do not schedule anything during the 12:30–13:00 break."

**Step 4 — Specify the output format.**
"Present the schedule as a table with columns: Day, Time slot, Task, Duration."

**Full specification:**
> "Create a time-block schedule for three tasks. Available time: Tuesday 10:00–16:00 and Wednesday 10:00–16:00 (30-minute break at 12:30 each day). Tasks: (A) draft a project proposal — 2 hours; (B) read 30 pages of a report — 1.5 hours; (C) write 10 follow-up emails — 1 hour. All three tasks must be scheduled. Do not split any task into blocks shorter than 30 minutes. Do not schedule during the 12:30–13:00 break. Present the result as a table: Day, Time slot, Task, Duration."

**Quick four-property check:**
- [x] **Testable** — you can check every task against the table and verify it fits within the stated hours.
- [x] **Bounded** — two specific days, named time windows, named tasks with durations, one explicit exclusion.
- [x] **Observable** — the output is a table you can read immediately.
- [x] **Actionable** — the AI has everything it needs; no follow-up questions required [1].

## In Practice

**Common anti-patterns and fixes:**

| Domain | Weak phrase | Why it fails | Stronger replacement |
|---|---|---|---|
| Health | "tell me if my results are normal" | Asks for medical judgment | "report the value and whether it is above or below the stated reference range" |
| Transport | "find me the best route" | "best" is undefined | "find the route with the fewest changes that arrives before 09:00" |
| Education | "make it age-appropriate" | Age not specified | "write for an 11-year-old with no prior knowledge of the topic" |
| Food | "make it healthy" | "healthy" is not measurable | "keep total calories under 600 and include at least 25g of protein" |
| Scheduling | "fit it into my schedule" | No schedule information given | "I am free 09:00–12:00 Mon–Fri; allocate all five tasks within those windows" |

**Three habits that improve every spec regardless of domain:**

1. **Include at least one explicit exclusion.** Naming one thing the AI should not do ("do not give health advice", "do not include a nutritional breakdown") eliminates a large proportion of out-of-scope outputs [2].
2. **Name the output format before you finish writing.** If you cannot name a concrete object — a table, a numbered list, a set of sentences — your spec is not observable yet.
3. **Do not assume the AI knows your local context.** Your city, your dietary rules, your organisation's calendar format — state all of it explicitly. The AI will default to common global assumptions if you do not [3].

Professional frameworks from MIT Sloan, Harvard HUIT, and Atlassian all describe versions of the same four-part structure used in this reading — the pattern holds across beginner practice and professional AI workflows alike [1][2][3].

## Key Takeaways

- Every domain — health, transport, education, food, scheduling — uses the same four-part structure: task statement, context, constraints, and expected output format.
- What changes across domains is the *type* of constraint that makes a spec bounded and the *type* of output that makes it observable — the principle is constant; the detail is domain-specific.
- A strong specification always replaces vague quality words ("healthy," "best," "appropriate") with measurable, domain-specific criteria.
- Including at least one explicit exclusion ("do not include X") in every specification is the single most effective habit for reducing out-of-scope AI output.
- After writing any spec, run the four-property check: testable, bounded, observable, actionable — if any box is unchecked, identify which of the four parts is missing the needed information and add it.

## References

1. MIT Sloan Educational Technology. "How to Write Effective AI Prompts." MIT Sloan EdTech, https://mitsloanedtech.mit.edu/ai/basics/effective-prompts/
2. Harvard University Information Technology. "Getting Started with AI Prompts." Harvard HUIT, https://www.huit.harvard.edu/news/ai-prompts
3. Atlassian. "The Ultimate Guide to Writing AI Prompts." Atlassian Blog, https://www.atlassian.com/blog/artificial-intelligence/ultimate-guide-writing-ai-prompts

---

# Testing a specification — how to verify the AI did exactly what you asked

## Overview

You have learned how to write a clear, detailed specification — one that is testable, bounded, and observable. You know how to name the inputs, expected outputs, and failure conditions of a task. The next question is a practical one: after you send the specification and the AI gives you a result, how do you actually check whether it did what you asked? This topic gives you a three-question check, a pass/fail table, and a simple classification that turns a vague "looks about right" into a precise, recorded finding [1].

## Key Concepts

### What "testing a specification" means

**Testing a specification** means comparing the AI's actual output to what you wrote in your specification, part by part, and recording whether each part was met.

It is not an opinion. You are not asking "do I like this?" You are asking a precise question: "Does this output match what I specified?"

Two things are being compared:

- **The specification** — what you wrote: the task statement, constraints, and expected output format.
- **The actual output** — what the AI produced in response.

This step is called a **verification**. You are *verifying* — confirming — that the output matches the instruction. Verification sits between writing the specification and deciding what to do next [2].

**Why it matters.** A powerful AI will nearly always produce output that *looks* reasonable. "Looks reasonable" can hide real gaps. Without a check, you might miss an AI that:

- Followed most of your constraints but quietly ignored one.
- Used the right format but drifted off-topic partway through.
- Produced the right number of items but included content you explicitly excluded.

With a verification step, you catch these gaps immediately — before you act on a flawed output [1][3].

---

### The three-question verification check

Every time you receive an AI output, run three questions against it in order. Each question checks a different part of your specification [1][2][3].

**Question 1 — Did I get the format I asked for?**

Look at the *structure* of the output. Does it match what you specified?

- If you asked for a numbered list, is it a numbered list?
- If you asked for three bullet points, are there exactly three?
- If you asked for a table with two columns, does it have two columns?
- If you asked for a response under 80 words, is it under 80 words?

Format requirements are the easiest to check — they are visible at a glance. If the output has a different shape from what you specified, that is called **format drift**.

**Question 2 — Did it stay within the constraints?**

Look at the *content* of the output. Does it respect the limits you set?

- If you specified a topic boundary ("cover only X, not Y"), did the AI stay within that boundary?
- If you included an exclusion ("do not include Z"), does Z appear in the output?
- If you set a domain or audience constraint, does the content match?

If the output includes content outside your specified scope, that is called **constraint overflow**.

**Question 3 — Does the output match the task statement?**

Step back from the details and look at the big picture. Did the AI do the *task* you asked for?

- If you asked for a summary, does the output summarise?
- If you asked for a set of instructions, does the output instruct?
- If you asked for a recommendation for a specific domain, is the recommendation actually for that domain?

This question catches the case where the output looks correct in format and follows some constraints, but the core task has shifted. That shift is called **task drift** — the hardest failure to catch, because a drifted output can look polished while still being the wrong thing [3].

**All three questions together:**

| Question | What part of the spec it checks | The failure it catches |
|---|---|---|
| Q1 — Format | Format and output structure | Format drift |
| Q2 — Constraints | Constraints and exclusions | Constraint overflow |
| Q3 — Task statement | Core task description | Task drift |

A complete verification always runs all three — not just the easiest one [1].

---

### Pass, partial pass, and full fail

After running the three questions, classify the result [1][2]:

**Full pass** — All three questions answered "yes." Format is correct, every constraint is respected, and the output matches the task statement. You can act on the output as-is.

**Partial pass** — One or two questions answered "yes" and one or two answered "no." A partial pass is *not* a pass — it means the specification was not fully met. It is still useful: you know exactly which parts were and were not met.

**Full fail** — All three questions answered "no," or the output is so far from the specification that it cannot be categorised part by part.

An important point: acting on a partial pass as if it were a full pass means working with a known problem. Recording a partial pass gives you a specific, fixable finding [3].

---

### Recording the result — the pass/fail table

A test result is only useful if you write it down. Noticing a problem is not the same as documenting it. A recorded test tells you exactly what passed, what failed, and where to focus [1].

**The pass/fail table** is a simple grid. Each row is one component of your specification. The columns are: the component name, what you specified, what the output contained, and the result (Pass / Fail).

Template:

| Spec component | What I specified | What the output contained | Result |
|---|---|---|---|
| Task statement match | [your task] | [what the output actually did] | Pass / Fail |
| Format | [your format requirement] | [the format of the output] | Pass / Fail |
| Constraint 1 | [your constraint] | [whether it was respected] | Pass / Fail |
| Constraint 2 | [your constraint] | [whether it was respected] | Pass / Fail |

You only fill in the rows that your specification included. If your specification had two constraints, you have two constraint rows [3].

**How to read the table:** All Pass entries → full pass. Any Fail entries → partial pass. All Fail entries → full fail. The table turns a vague impression into a row-by-row account [1].

---

### The three common failure patterns

When a result is a partial pass or full fail, one of three patterns is usually responsible [2][3]:

**Format drift** — The AI produced content that is correct in substance but in the wrong shape.

- You asked for a numbered list; the AI produced paragraphs.
- You asked for three bullet points; the AI produced five.
- You asked for a response under 100 words; the AI produced 180.

Format drift is caught by Q1. It is the most common pattern — the AI optimises for clarity in its own terms, not for your explicit format instruction.

**Constraint overflow** — The AI crossed a boundary you drew in your specification. The format may be correct and the task may be right, but content appears that you explicitly excluded.

- You specified "cover only the health benefits"; the AI included cost and side effects too.
- You specified a domain (scheduling); the AI drifted into general productivity advice.

Constraint overflow is caught by Q2. It often happens when a constraint conflicts with what the AI naturally produces for a topic.

**Task drift** — The output drifted away from the core task you described, even though it looks well-formed.

- You asked for a set of evaluation questions; the AI produced a general overview instead.
- You asked for a failure-condition analysis; the AI rewrote the spec instead.

Task drift is caught by Q3. The output can look thorough and polished while completely missing the stated task [3].

| Failure pattern | Which question catches it | What it looks like |
|---|---|---|
| Format drift | Q1 — Format | Right content, wrong shape |
| Constraint overflow | Q2 — Constraints | Right task, content crossed a boundary |
| Task drift | Q3 — Task statement | Well-formed output, wrong task |

## Worked Example

Two complete specification tests are shown below — one in the health domain and one in scheduling.

---

### Example 1 — Health domain

**Specification:**

> **Task statement:** Generate a five-item daily hydration checklist for an adult who works at a desk.
>
> **Inputs:** No external document needed. Use general health guidance only.
>
> **Constraints:** Each item must be one sentence starting with a verb. Do not include advice about food, supplements, or medication. Maximum five items — no more, no fewer.
>
> **Expected output format:** A numbered list of exactly five sentences.

**AI output received:**

> 1. Drink a glass of water first thing in the morning before checking your phone.
> 2. Keep a refillable water bottle on your desk and aim to refill it twice before lunch.
> 3. Set a reminder on your phone every two hours to take a short hydration break.
> 4. Eating water-rich foods like cucumber and watermelon can help you stay hydrated throughout the day.
> 5. Reduce your intake of caffeinated drinks, which can contribute to dehydration over long periods.

**Applying the three-question check:**

- **Q1 — Format:** Numbered list of five sentences. ✓ Format matches.
- **Q2 — Constraints:** Item 4 starts with "Eating" — it is about food, which the constraint excluded. Item 5 advises reducing caffeine — another food/drink boundary issue.
- **Q3 — Task statement:** The list is about daily hydration for a desk worker. ✓ Core task matches.

**Classification: Partial pass.** Q1 and Q3 pass. Q2 fails.

**Pass/fail table:**

| Spec component | What I specified | What the output contained | Result |
|---|---|---|---|
| Task statement match | Five-item hydration checklist for desk worker | Five-item hydration checklist for desk worker | Pass |
| Format | Numbered list, exactly five sentences | Numbered list, exactly five sentences | Pass |
| Constraint: verb-first sentences | Each sentence starts with a verb | Items 1–3 start with a verb; item 4 starts with "Eating" (not a command) | Fail |
| Constraint: no food or supplement advice | No food advice | Item 4 is about food; item 5 is about caffeine intake | Fail |
| Constraint: max five items | Exactly five | Exactly five | Pass |

**Result: Partial pass — two constraint failures (items 4 and 5 include food-related content; item 4 does not use a direct-action verb).**

---

### Example 2 — Scheduling domain

**Specification:**

> **Task statement:** Write a Monday morning briefing agenda for a team of four, covering a one-hour meeting.
>
> **Inputs:** The team is working on a software project. The meeting is the first of the week.
>
> **Constraints:** Exactly four sections, each with a name and a time allocation. Total time must add up to exactly 60 minutes. No social or warm-up activities.
>
> **Expected output format:** A numbered list of four items: [Section name] — [time in minutes]. Nothing else.

**AI output received:**

> **Monday Morning Team Briefing**
>
> 1. Team check-in and weekend highlights — 10 minutes
> 2. Sprint progress review — 20 minutes
> 3. Blockers and escalations — 15 minutes
> 4. Goals for the week — 15 minutes
>
> *Note: Starting with a brief check-in helps set a positive tone for the week.*

**Applying the three-question check:**

- **Q1 — Format:** The spec said "a numbered list of four items. Nothing else." The output added a title heading and a footnote. Format drift present.
- **Q2 — Constraints:** Item 1 is "Team check-in and weekend highlights" — a social warm-up. The footnote confirms the AI included it deliberately. Time total: 10+20+15+15 = 60. ✓ Time constraint passes, but warm-up constraint fails.
- **Q3 — Task statement:** A Monday briefing agenda, four people, one hour. ✓ Core task matches.

**Classification: Partial pass.** Q3 passes. Q1 and Q2 fail.

**Pass/fail table:**

| Spec component | What I specified | What the output contained | Result |
|---|---|---|---|
| Task statement match | Monday briefing agenda, four people, one hour | Monday briefing agenda, four people, one hour | Pass |
| Format | Numbered list of four items, nothing else | Numbered list plus a title heading and a footnote | Fail |
| Constraint: exactly four sections | Four sections | Four sections | Pass |
| Constraint: time adds to 60 minutes | Exactly 60 minutes | 10+20+15+15 = 60 | Pass |
| Constraint: no social or warm-up activities | No warm-up | Item 1 is "Team check-in and weekend highlights" | Fail |

**Result: Partial pass — format drift (unexpected heading and footnote) and constraint overflow (item 1 is a social warm-up that was explicitly excluded).**

## In Practice

The six-step process, applied every time you test a specification [1][2][3]:

1. **Re-read your specification before looking at the output.** If you read the output first, you anchor to what the AI said and find it harder to notice what is missing.
2. **Run the three-question check** — Q1 (format), Q2 (constraints), Q3 (task statement) — in order. Note your answer before moving to the next question.
3. **Build the pass/fail table.** One row per specification component. Fill in what you specified, what the output contained, and the result.
4. **Classify.** All Pass → full pass. Any Fail → partial pass. All Fail → full fail.
5. **Name the failure pattern.** Format drift, constraint overflow, or task drift? One test can show more than one pattern — both examples above had two at once.
6. **Record and stop.** Verification tells you *what happened*. What to do next — revise, re-run, or accept with a known gap — is covered in the next topic.

**Common mistakes to avoid:**

| Anti-pattern | The problem | The fix |
|---|---|---|
| "Looks good to me" review | Opinion without comparison to the spec | Run all three questions against each spec component |
| Checking Q1 only | Q2 and Q3 go unchecked | Always run all three in order |
| No recorded table | Finding noticed but not documented | Even a two-row table is a record — write it down |
| Calling a partial pass a pass | "Most of it was right" | Partial pass means the spec was not met — record it accurately |

University library guides for evaluating AI-generated content recommend checking the output against the original question as the *first* step before judging accuracy or depth [1][2]. Teams deploying AI tools in real products use the same three questions — format, constraints, task match — as the basis of structured output validation [3].

## Key Takeaways

- **Testing a specification** means comparing the AI's actual output to what you specified, part by part. It is a comparison against a written record — not an opinion about the output.
- The **three-question verification check** asks: (1) Did I get the format I asked for? (2) Did it stay within the constraints? (3) Does the output match the task statement? All three must be checked every time.
- A test result is classified as **full pass** (all three pass), **partial pass** (one or more fail), or **full fail** (all fail). A partial pass is not a pass — the specification was not fully met.
- The **pass/fail table** maps each specification component to what the output contained, with a Pass or Fail for each row. It turns a vague impression into a specific, actionable finding.
- The three common failure patterns are: **format drift** (right content, wrong shape), **constraint overflow** (content crossed an explicit boundary), and **task drift** (well-formed output, wrong task).

## References

1. CSUN University Library, "Artificial Intelligence: Evaluating AI-Generated Content." <https://libguides.csun.edu/c.php?g=1377855&p=11076059>
2. St. Catherine University Library, "Generative AI: Evaluating AI." <https://libguides.stkate.edu/generativeai/evaluatingAI>
3. VerifyWise, "AI Output Validation." <https://verifywise.ai/lexicon/ai-output-validation>

---

# Iterating a specification based on output gaps

## Overview

You have written a specification and run the three-question verification check from topic 2.8. The result came back as a partial pass or a full fail. The most common mistake at this point is to throw the whole specification away and write a new one from scratch. That wastes time and usually produces the same gap in a different place — because the root cause was never identified [1]. A smarter move is to look at exactly what went wrong and fix only that part. This topic gives you a four-step repeatable loop — test, name the gap, patch the right part, retest — that turns a failing specification into a passing one in two or three focused cycles, without discarding the work that is already correct.

## Key Concepts

### What "iterating" means

**Iteration** — making one focused change to a specific part of a specification, based on a specific gap found in a test result, then retesting to see whether the change worked [1].

The word "iterating" simply means "going through something again." You go through the test-and-fix cycle again — but not from scratch. You go through it with new information: the exact gap your last test revealed.

Think of it like adjusting a recipe. If your soup is too salty, you do not tear up the entire recipe and start over. You find the one step that added too much salt and change only that step. The rest of the recipe stays exactly as it was. The same logic applies to a specification: the parts that produced a correct result are already doing their job — leave them alone.

Two things make an iteration valid:

1. **Targeted** — you change the part of the spec that caused the failure. You leave the parts that passed completely alone.
2. **Grounded** — the change is driven by evidence from the test output, not by a hunch or a guess [2].

An iteration that changes three things at once is not a valid iteration. If the second test passes, you cannot tell which of the three changes actually fixed the problem. If it fails, you have made the problem harder to trace. Change one thing. Retest. Repeat.

### The three gap types and their fixes

A failing test result usually falls into one of three patterns. Each pattern — called a **gap type** — has a name and a targeted fix [1][2][3].

| Gap type | What it means | Which spec part caused it | The fix |
|---|---|---|---|
| **Format drift** | Right content, wrong shape or length | Format instruction (missing or too loose) | Add or tighten the format instruction |
| **Constraint overflow** | Output included content you did not ask for or explicitly forbid | A constraint was missing or too vague | Add a new constraint, or make an existing one more specific |
| **Task drift** | Output solved a different task than you intended | The task statement was too vague or ambiguous | Rewrite the task statement to remove the ambiguity |

Each fix targets a different part of the spec. Naming the gap type first points you straight to which part needs changing — so you do not accidentally rewrite the wrong section and introduce a new problem.

Here is what each gap type looks like in practice:

- **Format drift — format fix.** The AI gave you the right information but presented it in the wrong shape. For example: you asked for a numbered list and got one long paragraph. The fix is not to re-explain the task — it is to add or tighten a format instruction: "Present the output as a numbered list with exactly three items." [2]
- **Constraint overflow — constraint fix.** The AI included something you did not want. For example: you asked for a three-sentence summary and got five sentences with extra commentary you did not request. The fix is to add or tighten a constraint: "Do not include commentary or explanation. Stop after exactly three sentences." [1][3]
- **Task drift — task statement fix.** The AI solved a different problem than you intended. For example: you asked it to "describe the process" and it described a different process because "the process" was ambiguous — it could mean more than one thing. The fix is to rewrite the task statement to remove the ambiguity: "Describe only the four-step order-fulfilment process defined above." [1][2]

### The minimum viable patch principle

**Minimum viable patch** — the smallest change to the specification that directly addresses the gap you found, without touching any part that is already working [1][2].

This principle has three rules:

1. **Change one part only.** If the gap is in the format instruction, change the format instruction — do not also rewrite the task statement "just in case."
2. **Make the change as small as possible.** If adding four words to a constraint fixes the problem, do not rewrite the whole constraint.
3. **Leave passing parts untouched.** If two out of three test questions passed, the spec parts behind those passes are already doing their job. Do not disturb them.

Why does this matter? A specification is a connected set of parts. Changing one part can affect another. If you rewrite more than you need to, you risk breaking something that was already working [2][3]. You also make it harder to trace: if three things changed and the next test still fails, you cannot tell which of the three changes caused the new failure.

A common reaction to a bad test result is to rewrite the entire spec. It feels productive — you are "starting fresh." But almost always it makes things harder: you lose the parts that were correct, you cannot trace what changed, and you may introduce new gaps that were not there before.

### The iteration cycle

The iteration cycle is a four-step loop [1][2][3]:

1. **Test.** Run your current spec through the three-question verification check (from topic 2.8). Record the result for each question: full pass, partial pass, or full fail. If the overall result is a full pass — stop. You are done.
2. **Name the gap.** Look at the question that failed or partially passed. Decide which gap type it is — format drift, constraint overflow, or task drift. Write the gap type down as a phrase before you touch the spec. Do not start editing yet.
3. **Patch the right part.** Apply the minimum viable patch to the spec part that caused the gap. Leave everything else exactly as it was.
4. **Retest.** Run the three-question check again on the updated spec. Record the new result. If full pass — stop. If not, return to step 2 with the new test result.

Each time through the loop, the spec improves by exactly one patch. After two or three cycles, most specifications reach a full pass.

![Iteration Cycle — fix one gap, retest, repeat](../../../../../../../../CIT/content-gen-example/content/m1-computational-thinking/week-2/4-writing-and-testing-specifications/2-9-iterating-a-specification-based-on-output-gaps/artifacts/diagram.png)
*The iteration cycle: start with a spec, test it, branch to the matching gap fix (format drift, constraint overflow, or task drift) when it does not pass, patch only that part, retest, and repeat until full pass.*

### When to stop iterating

You stop iterating when one of two conditions is met [1][2]:

**Condition 1 — Full pass.** The spec passes all three verification questions with no partial results. This is the target. Stop here and document the final spec as your finished version.

**Condition 2 — Diminishing returns.** You have run two or three iteration cycles and the spec is still not reaching a full pass. Each new cycle is producing smaller improvements, or the remaining gap is in something you cannot control within a specification — for example, a very specific domain detail the AI consistently misses. In this case:

- Document the remaining limitation in one sentence: state what the spec does not fully control and why.
- Accept the spec as-is with the known limitation recorded.
- Do not keep iterating in hope of a perfect result that may not be achievable [3].

A spec with a clearly documented limitation is more useful than a spec that is never finished because it never reached 100%. The signal to stop is not the cycle count — it is whether each new cycle still produces meaningful improvement. If the remaining gap is a small format detail that does not affect the core task, accept it. If the remaining gap means the spec still does the wrong job entirely, keep iterating or reconsider the task statement from the beginning.

## Worked Example

The following three-cycle example shows the full iteration loop applied to a real task: asking an AI to produce study tips for an exam.

---

**Version 1 — first draft:**

> "Give me tips for studying for an exam."

**Cycle 1 test result:**

| Question | Result | What the output showed |
|---|---|---|
| Q1 — Did the output match what was expected? | Partial pass | Tips about studying — but there are seven of them, with no count specified |
| Q2 — Did the AI respect all constraints? | Fail | One tip mentioned "pulling an all-nighter" — no constraint was set to forbid this |
| Q3 — Is the output in the right format? | Fail | Output is a paragraph; no format was specified |

**Named gap:** The root cause is the task statement — it specified almost nothing. Three gaps are visible: task drift (no count or audience specified), constraint overflow (forbidden content appeared), and format drift (no list format). When multiple gap types appear at once, fix the task statement first because it is the root cause — the missing count, audience, and format all trace back to it.

**Minimum viable patch — cycle 1:** Rewrite the task statement to add a count, audience, format, and the key exclusion constraint.

---

**Version 2 — after cycle 1 patch:**

> "Give me exactly 3 tips for studying for an exam, written for a teenager, as a numbered list. Do not include any tips about staying up late or pulling an all-nighter."

**Cycle 2 test result:**

| Question | Result | What the output showed |
|---|---|---|
| Q1 — Did the output match what was expected? | Pass | Three tips, appropriate for a teenager |
| Q2 — Did the AI respect all constraints? | Pass | No all-nighter tip appeared |
| Q3 — Is the output in the right format? | Partial pass | Numbered list — but each item is 3–4 sentences long, not a short one-sentence tip |

**Named gap:** Format drift — the items are too long. The fix is to tighten the format instruction only. Q1 and Q2 both passed, so the task statement and the constraint are not touched.

**Minimum viable patch — cycle 2:** Add one sentence to the format instruction: "Each tip must be one sentence only."

---

**Version 3 — after cycle 2 patch:**

> "Give me exactly 3 tips for studying for an exam, written for a teenager, as a numbered list. Each tip must be one sentence only. Do not include any tips about staying up late or pulling an all-nighter."

**Cycle 3 test result:**

| Question | Result | What the output showed |
|---|---|---|
| Q1 — Did the output match what was expected? | Pass | Three tips, correct audience |
| Q2 — Did the AI respect all constraints? | Pass | No forbidden content |
| Q3 — Is the output in the right format? | Pass | Numbered list, one sentence per item |

**Result: Full pass. Iteration complete.**

**Iteration log:**

- Cycle 1: task drift + constraint overflow + format drift — rewrote task statement (root cause).
- Cycle 2: format drift (items too long) — added "Each tip must be one sentence only."
- Cycle 3: full pass. Final spec is version 3.

Notice what never changed: once the task statement was fixed in cycle 1, it was not touched in cycle 2. Only the format instruction was updated in cycle 2, because that was the only remaining gap. This is the minimum viable patch principle in action — change only what failed, leave everything that passed exactly as it was [1][2][3].

## In Practice

The test-name-patch-retest cycle is exactly how professionals refine AI instructions in real work. IBM's guide on iterative prompting describes it as an "assess → identify gap → modify" loop [1]. The vocabulary differs — they say "prompt" where we say "specification" — but the structure is identical.

What separates an experienced AI user from a beginner is not that the experienced person writes a perfect specification on the first try. It is that they diagnose gaps faster and make more precise, targeted patches [2].

One structured approach used in educational settings is the REFINE framework [3]: Review the output, Evaluate where it diverged from your intent, Focus on the specific part that caused the divergence, Iterate by patching only that part, and Note the change before evaluating again. The underlying logic is the same four-step loop from this topic.

**Do this:**

| Action | Why it matters |
|---|---|
| Name the gap type before touching the spec | Diagnosis first — fixing without diagnosis is guessing |
| Change one part per cycle | You cannot learn which fix worked if you change three things at once |
| Write the old version and the new version side by side | Creates a traceable change log and shows deliberate iteration |
| Record every test result in a pass/fail table | Turns iteration into visible evidence you can point to |
| Stop at full pass | Iterating beyond a full pass introduces new, unnecessary risk |

**Avoid this:**

| Mistake | What goes wrong |
|---|---|
| Rewriting the whole spec because one part failed | You break the parts that were working and cannot trace what changed |
| Fixing a format-drift gap by rewriting the task statement | Wrong part — the format gap will likely remain and you may add new ones |
| Accepting a known limitation on a task-drift failure | The spec still does the wrong job — that is not a small limitation, it is a fundamental one |
| Running more than three cycles without re-reading the full spec | After three failures, the root cause may be in the task statement even if earlier gaps looked like format issues |

## Key Takeaways

- **Iteration means one targeted change.** When a spec fails, identify the exact part that caused the failure and fix only that — do not rewrite the whole spec from scratch.
- **Three gap types, three matching fixes.** Format drift (wrong shape) — fix the format instruction. Constraint overflow (unwanted content) — add or tighten a constraint. Task drift (wrong task) — rewrite the task statement.
- **Minimum viable patch.** Change only what caused the failure. Leave every passing part untouched. If adding four words fixes the problem, do not rewrite the paragraph.
- **The four-step loop.** Test → name the gap → patch the right part → retest. Each cycle produces one improvement. Repeat until full pass.
- **Know when to stop.** Full pass is the target. If further cycles produce no meaningful improvement, document the remaining limitation and accept the spec — a spec with a documented limitation is more useful than one that is never finished.

## References

1. IBM, "Iterative Prompting." <https://www.ibm.com/think/topics/iterative-prompting>
2. Whitebeard Strategies, "AI Prompt Debugging: Fixing Issues Through Iteration." <https://whitebeardstrategies.com/blog/ai-prompt-debugging-fixing-issues-through-iteration/>
3. Catlin Tucker, "REFINE: A Framework for AI Prompting." <https://catlintucker.com/2025/08/refine-ai-prompting/>

---
<!-- nav:bottom:start -->
Previous: [⬅ 9.2 — Expressing Logic](../9-2-expressing-logic/reading.md)&emsp;·&emsp;[⬆ Table of Contents](../../../../../../README.md#part-b)&emsp;·&emsp;[10.1 — History of AI ➡](../../../../m2-introduction-to-ai-systems/week-10/1-what-ai-is-and-isnt/10-1-history-of-ai/reading.md)
<!-- nav:bottom:end -->
