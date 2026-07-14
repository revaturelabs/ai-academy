---
topic_id: "2.3"
title: "How to identify the inputs, expected outputs, and failure conditions of a task"
position_in_module: 3
generated_at: "2026-06-16T00:00:00Z"
resource_count: 3
---

# 1. How to Identify the Inputs, Expected Outputs, and Failure Conditions of a Task — Topic Corpus

## 2. Prerequisites

This topic builds directly on:

- **2.1 — What makes a good specification — testable, bounded, observable, actionable.** You should be comfortable with the four-property checklist. Those properties appear throughout this topic as the quality bar for every component you write.
- **2.2 — Bad spec vs good spec.** The diagnostic and repair strategies from topic 2.2 are referenced by name. You do not need to re-learn them here.

From Week 1, the concept of **inputs and outputs** (covered in 1.1 What is computation and 1.5 Algorithms) is reused directly — an algorithm takes inputs and produces outputs. This topic extends that idea into the context of writing specifications for AI tools.

## 3. Learning Objectives

By the end of this topic you will be able to:

- Name all six components of a complete specification and describe the purpose of each one.
- Identify the inputs of a task by asking what raw material the AI needs before it can begin.
- Describe expected outputs precisely — format, length, and content — so the result is observable and testable.
- Write failure conditions for a task by thinking through what could go wrong and how the AI should respond.
- Apply the three core components (inputs, expected outputs, failure conditions) to a real-world task.
- Explain why specifying failure conditions matters for AI reliability.

## 4. Introduction

You have already learned that a good specification must be testable, bounded, observable, and actionable. Those four properties tell you *how to judge* a specification. This topic teaches you *how to build* one — specifically, how to find the three most critical pieces a specification needs before you write a single word.

Think about ordering a custom-made cake. You would not just say "make me a cake." You would specify: the flavour (input), what it should look like when it arrives (expected output), and what happens if the baker cannot get a certain ingredient (failure condition). Every piece of information you supply closes one more gap between your expectation and the result you receive.

Writing a specification for an AI task works the same way. Most weak specifications are not wrong — they are *incomplete*. A key piece of information is missing, and the AI fills the gap with a guess [1]. This topic gives you a six-component checklist to make sure nothing is missing, with deep focus on the three components that most directly affect whether an AI task succeeds or fails: **inputs**, **expected outputs**, and **failure conditions**.

The six components are: task description, inputs, expected outputs, format and constraints, failure conditions, and success criteria. Work through all six and your specification is complete. Skip one and you leave a gap the AI will fill for you — often in a way you did not intend [2].

## 5. Core Concepts

### 5.1 The Six-Component Specification Checklist

A complete specification has six named parts. Each part answers one specific question about the task. Together they leave no guesswork for the AI [1].

| Component | The question it answers |
|---|---|
| Task description | What is the AI supposed to do? |
| **Inputs** | What raw material does the AI need to start? |
| **Expected outputs** | What should the result look like? |
| Format and constraints | How should the result be structured and bounded? |
| **Failure conditions** | What counts as a problem, and how should the AI handle it? |
| Success criteria | How will you know the output is correct? |

This topic teaches **inputs**, **expected outputs**, and **failure conditions** at full depth — these three components most directly determine whether an AI task succeeds or fails. The other three components — task description (§5.2), format and constraints (§5.5), and success criteria (§5.7) — are introduced in the sections below.

---

### 5.2 Component 1 — Task Description

The **task description** is the action statement — a verb paired with a subject that tells the AI what to do. Examples: "Summarise [the article]," "Translate [this paragraph]," "List [five causes]," "Evaluate [this argument]."

A precise verb matters. "Identify and list" is more specific than "find"; "rewrite in plain English" is more specific than "improve." A vague task description fails the **actionable** property from topic 2.1: the AI cannot take a first step when the action itself is unclear [1][2].

When writing a task description, ask: "Could a stranger read this one sentence and know exactly what to produce?" If not, tighten the verb or the subject before adding the other five components.

---

### 5.3 Component 2 — Inputs

**Inputs** are everything the AI needs to have — or needs to know — before it can start the task. An input is any piece of raw material, context, or data the AI will work with or work from.

Without clearly stated inputs, the AI either makes up material or applies the task to the wrong thing. Both outcomes waste your time [1].

**Types of inputs you might specify:**

| Input type | Example |
|---|---|
| A document or text | "The email thread in the box below" |
| A data set or list | "The five product names listed here: ..." |
| Context about the audience | "The reader is a first-year university student" |
| A constraint on what to use | "Use only the information in the paragraph above — do not use outside knowledge" |
| Background the AI needs | "The project deadline is Friday. The client is expecting a draft, not a final version." |

**Why specifying inputs matters for AI.** An AI tool does not automatically know what document, text, or context you are referring to. If you say "summarise this," the AI infers what "this" means from whatever is in front of it — which may not be what you intended. Naming the input removes that inference [2].

**Worked example — before and after:**

Before: *"Summarise this."*

After: *"Summarise the product description in the paragraph labelled 'Description' below. Do not include information from any other part of the page."*

The after version names the exact input and explicitly excludes other possible inputs. The AI now knows exactly what raw material to use [1].

---

### 5.4 Component 3 — Expected Outputs

**Expected outputs** describe what the AI should produce. They answer the question: "What will I actually receive when the task is done?"

Specifying the output makes the result **observable** — a property from topic 2.1. An observable output is something you can read, count, or measure. An unobservable output is vague and unmeasurable [2].

**Three dimensions of an expected output:**

1. **Type** — What kind of thing is it? A numbered list? A paragraph? A table? A single sentence? A yes/no answer?
2. **Content** — What must the output contain? What must it not contain?
3. **Amount** — How many items, sentences, words, or examples?

All three dimensions should be explicit. If any one is left open, the AI will make a choice for you.

**Example — all three dimensions specified:**

Task: rewrite a customer complaint response.

- Type: a single paragraph of continuous prose.
- Content: must acknowledge the problem, offer a solution, and end with a next step for the customer. Must not include any apology stronger than "we are sorry for the inconvenience."
- Amount: between 60 and 80 words.

With all three dimensions named, the output is fully observable. You can check each one [1][3].

**A common mistake — specifying type but not content:**

*"Give me a list of ideas."*

Type is specified (a list). Content is not (ideas about what?). Amount is not (how many?). The output is still mostly unobservable because you cannot check whether the content is correct [2].

---

### 5.5 Component 4 — Format and Constraints

**Format** specifies the shape of the output — a numbered list, a table, a single paragraph, a yes/no answer. **Constraints** draw the boundaries — maximum word count, topic limits, exclusions, audience, tone.

Together they enforce the **bounded** and **observable** properties from topic 2.1: format makes the output observable (you know what you will receive); constraints make the task bounded (the AI knows what to include and what to leave out) [2][3].

Example: "Produce a table with two columns — Product Name and Price — with exactly five rows. Do not include products priced above £50." The format (table, two columns, five rows) and the constraint (price ceiling) can both be checked at a glance.

---

### 5.6 Component 5 — Failure Conditions

**Failure conditions** are the situations in which the AI cannot or should not complete the task as specified — and what it should do instead.

This is the component most beginners leave out. Omitting it is also one of the most common reasons AI outputs are unreliable in practice [3].

**Why failure conditions matter for AI reliability.**

A human worker, when they hit a problem, stops and asks a question: "I cannot find that file — can you send it again?" An AI tool, in most workflows, does not stop. It produces something anyway. Without failure conditions in the specification, the AI may:

- Make up missing information to fill a gap (called a **hallucination** — producing plausible-sounding but incorrect content).
- Silently skip a part of the task without telling you.
- Produce an output that looks complete but is based on wrong assumptions [3].

Specifying failure conditions gives the AI explicit instructions for those situations. Instead of guessing, it follows your rule.

**Three categories of failure conditions:**

1. **Missing input.** What should the AI do if the input is incomplete or absent?
   - Example: *"If the product description is missing, write 'No description provided' and stop — do not invent a description."*

2. **Input outside scope.** What should the AI do if the input does not match what the task assumes?
   - Example: *"If the text is not in English, translate it first before summarising. If you cannot identify the language, state 'Language not recognised' and stop."*

3. **Ambiguous or conflicting content.** What should the AI do if the input contains contradictions or unclear information?
   - Example: *"If the customer's complaint refers to two different orders, address only the most recent one. Flag the second order by writing 'Note: a second order was mentioned but not addressed.'"*

**Why this component is specific to AI.** In topic 2.1, you learned that AI tools are probabilistic — they do not always give the same answer twice. Failure conditions reduce that variability at the edges of the task, where the input is messy or incomplete. They do not fix the AI; they tell the AI what to do when things go wrong [2][3].

---

### 5.7 Component 6 — Success Criteria

**Success criteria** state what a correct output looks like — the specific conditions under which you would accept the output without change. They are the concrete expression of the **testable** property from topic 2.1 [1].

Writing success criteria before you send the specification is a useful discipline: if you cannot state what a passing output looks like, your specification is probably not yet fully testable.

Example: if the task asks for "exactly three bullet points, each under 20 words, covering only the findings on pages 3–7," the success criteria are: three bullets present, each under 20 words, no content from outside pages 3–7. Each criterion can be checked in under a minute [1][2].

---

### 5.8 How the Six Components Work Together

The six components are not six separate documents. They are six lenses on the same task. Writing all six produces one unified specification where every question has been answered.

Here is how they connect:

- Task description + **Inputs** together answer: "What are we doing, and with what?"
- **Expected outputs** + Format and constraints together answer: "What will I receive, and what are the rules it must follow?"
- **Failure conditions** + Success criteria together answer: "What happens when things go wrong, and how do I know when things are right?"

A specification with all six components satisfies the four-property checklist introduced in topic 2.1 [1][2][3].

### 5.9 Worked Example — Identifying the Three Core Components

**Task:** You want an AI tool to help you write a brief summary of a job applicant's cover letter for a hiring manager to read before an interview.

Here is how you identify and write the three components taught in this topic.

---

**Inputs:**

Ask: "What does the AI need to have before it can start?"

- The full text of the cover letter (pasted below the specification).
- Context: the role being applied for is a junior data analyst position. The hiring manager has 3 minutes to read the summary before the interview starts.

Both pieces are included because the AI needs the raw material (the letter) and the context (the role and time constraint) to do the task correctly [1].

---

**Expected outputs:**

Ask: "What will I actually receive — type, content, and amount?"

- Type: three bullet points.
- Content: each bullet covers one of the following in order — (1) the applicant's relevant experience, (2) their stated motivation for applying, (3) one specific skill or achievement they highlight.
- Amount: each bullet is one sentence.

All three dimensions are named, so the output is observable and checkable [2].

---

**Failure conditions:**

Ask: "What could go wrong with the input?"

- If the cover letter does not mention relevant experience, write "No relevant experience mentioned" for bullet 1.
- If the cover letter is fewer than 50 words, write "Cover letter too short to summarise reliably" and stop.
- If the cover letter is not in English, state "Cover letter is not in English — translation required" and stop.

Each failure condition names a concrete situation and a concrete response. The AI cannot guess when any of these situations occurs [3].

---

With these three components identified and written, the specification has no gaps in the areas that most directly affect whether the task succeeds or fails [1][2][3].

## 6. Implementation

Use the following steps to identify and write the three core components — inputs, expected outputs, and failure conditions — for any AI task. (The remaining three components are covered in companion topics.)

**Step 1 — List all the inputs.**
Ask: "What does the AI need to have before it can start?" List every piece of raw material, context, or background information. For each input, decide whether it will be provided in the specification directly (pasted in) or referenced by name.

**Step 2 — Describe the expected output.**
Specify the type (list, paragraph, table, sentence), the required content (what must be in it and what must not), and the amount (how many items, words, or examples).

**Step 3 — Write the failure conditions.**
Ask: "What could go wrong with the input?" Then write one explicit instruction for each answer. Cover at minimum: missing input, out-of-scope input, and ambiguous content. For each failure, state what the AI should produce instead of guessing.

**Before sending: the three-component check.**

- [ ] Inputs — all raw material and context named explicitly.
- [ ] Expected outputs — type, content, and amount all specified.
- [ ] Failure conditions — at least one rule for each type of problem (missing, out-of-scope, ambiguous).

If any box is unchecked, fill it before sending the specification to the AI [1][2].

## 7. Real-World Patterns

The six-component approach is used in professional software development, data science, and AI product teams — not just for individual prompts, but for building the instructions that run AI systems continuously [1].

**Specification-driven development.** In professional software teams, writing formal specifications before building is standard practice. Developers write "acceptance criteria" that map directly onto expected outputs and success criteria. Teams that skip this step spend more time fixing defects than teams that write specifications first. The same principle applies when the system carrying out the work is an AI tool [1].

**AI prompt engineering in production systems.** Teams that build AI-powered tools for real users — customer-service assistants, summarisation tools, classification systems — use explicit failure conditions as a reliability mechanism. Without failure conditions, a system handling thousands of queries per day will encounter edge cases (unusual inputs, missing data, off-topic questions) and produce unpredictable outputs. Specifying failure conditions in the system instructions is a standard practice in production AI deployment [2].

AI agents can fail silently when specifications are incomplete. Research into these systems shows that many failures trace back to missing inputs, no failure condition for when to stop, and outputs that look correct but violate an unstated constraint [3]. All three of these failures are prevented by writing complete inputs, expected outputs, and failure conditions.

## 8. Best Practices

**Do:**

- Write inputs, expected outputs, and failure conditions every time — even for small tasks. Skipping a component because the task "seems simple" is how gaps appear.
- Write failure conditions before you send the specification. It is easier to think about what could go wrong when you are not yet looking at a bad output.
- Specify all three dimensions of expected outputs: type, content, and amount.
- Re-read your specification as if you are the AI and know nothing else. Every question you find yourself asking is a gap to fill [1].

**Don't:**

- Do not assume the AI will ask for clarification when inputs are missing. Most AI tools will proceed and guess. Write the failure condition yourself.
- Do not leave expected outputs vague — "give me a list" without specifying content or length is still incomplete.
- Do not treat failure conditions as optional. They are the component that most directly affects AI reliability [3].

**Common anti-patterns:**

| Anti-pattern | The problem | The fix |
|---|---|---|
| No inputs stated | AI guesses what to work with | Name every piece of raw material explicitly |
| Expected output type only, no content | "A list" without specifying what the list must contain | Add content and amount alongside type |
| No failure conditions | AI hallucinates or silently skips steps | Add at least one rule per failure category |

## 9. Hands-On Exercise

Choose one task you might realistically ask an AI tool to help with — for example: writing an email, summarising a document, translating a paragraph, or generating a to-do list.

Work through the three core components:

1. List every input the AI needs (raw material, context, background).
2. Describe the expected output — type, content, and amount.
3. Write at least one failure condition for each of the three categories: missing input, out-of-scope input, ambiguous content.

When you are done, compare your inputs and failure conditions to the worked example in Section 5.9. Check whether your failure conditions are specific — they should each name a concrete situation and a concrete response.

**Extension — connecting to the lab activity:**

Now apply the same three-component approach to one task from this week's lab. The lab asks you to write specifications for tasks in five domains. Pick one domain (health, transport, education, food, or scheduling) and choose a realistic AI task within it — for example, in the health domain: *"Summarise a patient's medication list for a GP appointment summary."*

Write the three components:

1. Inputs: what does the AI need before it can start?
2. Expected outputs: type, content, and amount.
3. Failure conditions: what should the AI do if an input is missing, out of scope, or ambiguous?

Then send the specification to an AI tool and check whether the output matches what you described in your expected outputs. This is the full specification-writing cycle you will repeat for all five lab domains.

## 10. Key Takeaways

- A complete specification has six components; this topic focuses on the three that most directly determine success: **inputs**, **expected outputs**, and **failure conditions**.
- Inputs tell the AI what raw material to work with. Without them, the AI guesses — often incorrectly.
- Expected outputs make the result observable. Specify the type, content, and amount of what you expect to receive.
- Failure conditions are the most commonly skipped component and the one most directly responsible for AI unreliability. An AI without failure conditions will guess when inputs are missing, ambiguous, or out of scope.
- Writing all three components together closes the most common gaps that cause AI tasks to produce wrong or unpredictable outputs [1][2][3].

## 11. Next Steps

_System-derived from the next entry in curriculum/sequence.md._
