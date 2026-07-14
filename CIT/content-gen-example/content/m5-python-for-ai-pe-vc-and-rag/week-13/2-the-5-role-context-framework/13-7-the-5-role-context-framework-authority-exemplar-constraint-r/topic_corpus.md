---
topic_id: "13.7"
title: "The 5-role context framework — Authority, Exemplar, Constraint, Rubric, Metadata"
position_in_module: 1
generated_at: "2026-06-14T00:00:00Z"
resource_count: 3
---

# The 5-Role Context Framework — Authority, Exemplar, Constraint, Rubric, Metadata — Topic Corpus

## Section 1 — Topic Summary

You have already learned individual prompt engineering techniques — system prompts, role assignment, few-shot examples, constraints, and output format control. This topic shows you how to combine all of those into one organised structure called the **5-role context framework**. The framework, defined in peer-reviewed research [1], names five distinct roles that different parts of your prompt play: Authority, Exemplar, Constraint, Rubric, and Metadata. Learning this framework matters right now because your A4 portfolio requires you to write multiple structured prompt versions and compare their accuracy — and this framework gives you a repeatable template for doing that.

## Section 2 — Prerequisites

This topic builds directly on techniques introduced in topics 13.1 through 13.6. Specific dependencies are:

- **13.1** — System prompt vs user prompt (the concept of static authority context)
- **13.2** — Role assignment (persona and tone calibration)
- **13.3** — Few-shot examples (in-context learning with example pairs)
- **13.5** — Constraints (negative instructions and guardrails)
- **13.6** — Output format control (format specification and template echo)

Topic 13.4 (chain-of-thought prompting) is also relevant background: chain-of-thought instructions often appear inside the Rubric role.

## Section 3 — Learning Objectives

By the end of this topic you will be able to:

1. **Name** each of the five roles in the context framework and state in one sentence what each role does.
2. **Map** a prompt you have already written onto the five roles, identifying which parts belong to which role.
3. **Assemble** a complete 5-role prompt in Python using an f-string or a dictionary structure.
4. **Apply** the priority rule (Authority > Exemplar > Constraint > Rubric > Metadata) to resolve a conflict when two roles give contradictory instructions.
5. **Evaluate** a prompt for missing roles and explain what output problem each missing role is likely to cause.

## Section 4 — Introduction

Imagine a new employee's first day. Their manager hands them five documents:

1. A **company policy manual** — the rules that override everything else.
2. A **sample report** from a top performer — showing what good work looks like.
3. A **list of things never to do** — legal and compliance restrictions.
4. A **marking rubric** — how their work will be graded.
5. A **cover sheet** — date, project code, their name, and the task number.

Each document plays a different role. Together, they give the employee everything they need to do the job correctly. A large language model (LLM) needs the same thing. When you write a prompt, you are handing the model those five documents — even if you do not realise it. The 5-role context framework makes that structure explicit and intentional [1].

Before this topic, you learned each of those documents separately. Now you learn how they fit together as a single **context package** — a complete set of information you give the model before it generates a response.

## Section 5 — Core Concepts

### What is a context package?

A **context package** is all the information you pass to a model in a single interaction, assembled so the model has everything it needs to produce the right output. Research defines a structured way to build this package using five roles [1].

Think of the context package as a folder. Each role is a tab in that folder. You do not have to fill every tab every time — but knowing which tabs exist helps you notice when one is missing.

### The five roles

#### Role 1 — Authority

**Authority** is the part of your prompt that states who the model is and what its highest-level purpose is. It overrides everything else if there is a conflict.

- **Analogy:** The company's founding mission statement. No individual project instruction can contradict it.
- **In a prompt:** This is the system prompt you learned in topic 13.1, plus the role assignment from topic 13.2. It answers: "What kind of assistant are you, and what is your primary job?"
- **Example snippet:** `"You are a customer-support assistant for a bank. Your primary goal is to help customers resolve account issues accurately and safely."`

Authority sits at the **top of the priority stack**. If anything else in the prompt conflicts with Authority, Authority wins [1].

#### Role 2 — Exemplar

**Exemplar** is the part of your prompt that shows the model what a good response looks like. It uses concrete examples.

- **Analogy:** The sample report from a top performer. The employee does not just read instructions — they see a finished example.
- **In a prompt:** These are the few-shot examples you learned in topic 13.3. One or more example input-output pairs.
- **Example snippet:**
  ```
  User: My card was declined.
  Assistant: I'm sorry to hear that. The most common reasons are insufficient funds,
  an expired card, or a block placed for security. Which would you like me to investigate first?
  ```

Exemplar sits **second in the priority stack** [1]. If an example seems to conflict with a constraint, the constraint (Role 3) wins.

#### Role 3 — Constraint

**Constraint** is the part of your prompt that tells the model what it must NOT do, and what limits apply.

- **Analogy:** The legal and compliance restrictions. The employee may want to help, but some things are simply off limits.
- **In a prompt:** These are the negative instructions and guardrails you learned in topic 13.5. They can also include positive-reframe constraints ("always respond in English," "never mention competitor products").
- **Example snippet:** `"Never share internal account numbers in your response. Do not speculate about reasons for a decline without checking account data."`

Constraint sits **third in the priority stack** [1]. It overrides Rubric and Metadata if they conflict.

#### Role 4 — Rubric

**Rubric** is the part of your prompt that describes how the output should be structured and what quality looks like. It is the scoring guide.

- **Analogy:** The marking rubric a teacher gives a student — "your answer must have a greeting, a diagnosis, and a next step."
- **In a prompt:** This combines output format control from topic 13.6 with any quality criteria you want the model to follow. It answers: "What does a correct, well-formed response look like?"
- **Example snippet:** `"Your response must: (1) acknowledge the customer's issue, (2) state one likely cause, (3) offer one concrete next step. Keep your response under 80 words."`

Rubric sits **fourth in the priority stack** [1]. It shapes output quality but cannot override safety constraints.

#### Role 5 — Metadata

**Metadata** is supporting information about the context — things like the date, the user's account tier, the session ID, or the language preference. Metadata does not give instructions; it gives facts the model can use while following instructions.

- **Analogy:** The cover sheet — date, project code, employee name. It does not change the rules; it fills in the blanks the rules reference.
- **In a prompt:** Injected facts such as `"Today is 14 June 2026. Customer tier: Gold. Preferred language: English."` You will often build this programmatically in Python.
- **Example snippet:** `"[Context: date=2026-06-14, customer_tier=Gold, language=en]"`

Metadata sits **last in the priority stack** [1]. It informs the model without overriding anything.

### Priority order and conflict resolution

When two roles seem to contradict each other, the model (and you as the designer) should resolve the conflict using this order:

| Priority | Role | Wins over |
|---|---|---|
| 1 (highest) | Authority | Everything |
| 2 | Exemplar | Constraint, Rubric, Metadata |
| 3 | Constraint | Rubric, Metadata |
| 4 | Rubric | Metadata |
| 5 (lowest) | Metadata | Nothing — purely informational |

This priority order is defined in [1]. **Practical rule:** If your example (Exemplar) shows the model doing something your constraint forbids, the constraint wins. Fix the example so it does not conflict — the priority rule is a safety net, not an excuse to leave contradictions in your prompt [1].

### Why does this matter?

Before you had this framework, you were adding prompt components one at a time and hoping they worked together. The 5-role framework gives you a mental checklist [1]:

- Missing Authority → the model has no stable identity; tone shifts randomly.
- Missing Exemplar → the model guesses at output style; quality is inconsistent.
- Missing Constraint → the model may produce things you did not want.
- Missing Rubric → output structure varies; your output validator has nothing to check against.
- Missing Metadata → the model may give generic answers when it could give personalised ones.

## Section 6 — Worked Example

Below is a complete, annotated 5-role prompt for a **recipe assistant**. Each label marks exactly which role that block belongs to.

```
[AUTHORITY]
You are a healthy-eating recipe assistant. Your primary purpose is to suggest
simple, nutritious recipes for home cooks with no professional culinary training.

[EXEMPLAR]
Example:
User: I have chicken, broccoli, and rice. What can I make?
Assistant: Try a simple stir-fry. Cook the rice first. Slice the chicken into
strips and fry for 5 minutes. Add broccoli for 3 more minutes. Season with
soy sauce and serve over rice. Total time: 20 minutes.

[CONSTRAINT]
Never suggest recipes that require more than 30 minutes of active cooking time.
Do not recommend deep frying. Do not suggest recipes with peanuts unless the
user explicitly confirms no nut allergy.

[RUBRIC]
Your response must:
(1) Name the dish.
(2) List the steps as a numbered list.
(3) State total active cooking time.
(4) Keep the response under 150 words.

[METADATA]
[Context: date=2026-06-14, user_skill_level=beginner, dietary_restriction=none]
```

**What each role does in this example:**

| Role | What it controls | What goes wrong if it is missing |
|---|---|---|
| Authority | The model knows it is a recipe helper, not a general chatbot | Without it, the model might give financial advice or tell jokes |
| Exemplar | The model sees that steps should be short and conversational | Without it, the model might write a 500-word academic cooking essay |
| Constraint | The model will not suggest 45-minute deep-fried meals | Without it, the user might get a recipe they cannot safely make |
| Rubric | Every response has a name, numbered steps, and a time estimate | Without it, output structure varies per request |
| Metadata | The model knows the user is a beginner | Without it, it might assume professional equipment or techniques |

**Assembled in Python:**

```python
authority  = (
    "You are a healthy-eating recipe assistant. Your primary purpose is to suggest "
    "simple, nutritious recipes for home cooks with no professional culinary training."
)
exemplar   = (
    "Example:\n"
    "User: I have chicken, broccoli, and rice. What can I make?\n"
    "Assistant: Try a simple stir-fry. Cook the rice first. Slice the chicken into "
    "strips and fry for 5 minutes. Add broccoli for 3 more minutes. Season with "
    "soy sauce and serve over rice. Total time: 20 minutes."
)
constraint = (
    "Never suggest recipes that require more than 30 minutes of active cooking time. "
    "Do not recommend deep frying. "
    "Do not suggest peanut-containing recipes unless the user confirms no nut allergy."
)
rubric     = (
    "Your response must: "
    "(1) Name the dish. "
    "(2) List the steps as a numbered list. "
    "(3) State total active cooking time. "
    "(4) Keep the response under 150 words."
)
metadata   = "[Context: date=2026-06-14, user_skill_level=beginner, dietary_restriction=none]"

system_prompt = "\n\n".join([authority, exemplar, constraint, rubric, metadata])
```

This is a complete, runnable context package [3]. Every role is present, labelled, and in priority order.

## Section 7 — Common Mistakes and Misconceptions

**Mistake 1 — Treating Authority and Constraint as the same thing.**
Authority tells the model *who it is and what its purpose is*. Constraint tells the model *what it must not do*. These are different roles with distinct positions in the priority stack [1]. A model can have a clear identity (Authority) and still violate boundaries if there are no Constraints. Fix: write both. Authority sets the identity; Constraint sets the fences.

**Mistake 2 — Putting everything in one block of text and calling it a prompt.**
Beginners often write one long paragraph that mixes identity, examples, rules, and format instructions. The model can still understand this, but it becomes hard to debug and hard to version. Fix: split your prompt into the five named keys in a Python dictionary. You can then change one role at a time and see the effect on output.

**Mistake 3 — Skipping Rubric because the format "seems obvious."**
Without a Rubric, the model chooses its own format every time [2]. Some responses will be bullet lists; others will be paragraphs; others will be JSON. Fix: always write a Rubric, even if it is one sentence: "Respond in plain prose, under 100 words."

**Mistake 4 — Putting changing facts into Authority instead of Metadata.**
Authority should be stable across requests [1]. If you put today's date or the user's name into Authority, that block changes every request and is harder to maintain. Fix: put dynamic, per-request facts into Metadata. Keep Authority static.

**Mistake 5 — Ignoring conflict between Exemplar and Constraint.**
If your example shows the model doing something your Constraint forbids, the model gets a mixed signal. The priority rule says Constraint wins, but the model may still follow the example some of the time. Fix: review every example against your Constraint list. Remove or rewrite any example that violates a constraint [2].

## Section 8 — Implementation Notes

Follow these steps to build a 5-role prompt in Python.

1. **Create a Python dictionary** with one key per role. This makes each role easy to inspect, update, and version independently.

   ```python
   context_package = {
       "authority":   "",
       "exemplar":    "",
       "constraint":  "",
       "rubric":      "",
       "metadata":    "",
   }
   ```

2. **Fill in the Authority key.** Write who the model is and its primary purpose.

   ```python
   context_package["authority"] = (
       "You are a customer-support assistant for a bank. "
       "Your primary goal is to help customers resolve account issues accurately and safely."
   )
   ```

3. **Fill in the Exemplar key.** Paste in one or more example input-output pairs.

   ```python
   context_package["exemplar"] = (
       "Example:\n"
       "User: My card was declined.\n"
       "Assistant: I'm sorry to hear that. Common reasons include insufficient funds, "
       "an expired card, or a security block. Which would you like me to check first?"
   )
   ```

4. **Fill in the Constraint key.** List what the model must never do.

   ```python
   context_package["constraint"] = (
       "Never share full account numbers. "
       "Do not speculate without checking data. "
       "Always respond in English."
   )
   ```

5. **Fill in the Rubric key.** Describe the required output structure and length.

   ```python
   context_package["rubric"] = (
       "Your response must: "
       "(1) acknowledge the customer's issue, "
       "(2) state one likely cause, "
       "(3) offer one concrete next step. "
       "Keep your response under 80 words."
   )
   ```

6. **Fill in the Metadata key** using an f-string so dynamic facts update automatically per request.

   ```python
   customer_tier = "Gold"
   today = "2026-06-14"

   context_package["metadata"] = (
       f"[Context: date={today}, customer_tier={customer_tier}, language=en]"
   )
   ```

7. **Assemble the system prompt** by joining the roles in priority order, separated by blank lines.

   ```python
   system_prompt = "\n\n".join([
       context_package["authority"],
       context_package["exemplar"],
       context_package["constraint"],
       context_package["rubric"],
       context_package["metadata"],
   ])
   ```

8. **Pass the assembled prompt to the model** as the system message, then send the user's question as the user message.

   ```python
   import anthropic

   client = anthropic.Anthropic()

   response = client.messages.create(
       model="claude-haiku-4-5-20251001",
       max_tokens=256,
       system=system_prompt,
       messages=[
           {"role": "user", "content": "My card was declined."},
       ]
   )
   print(response.content[0].text)
   ```

This structure is directly reusable across your three A4 prompt versions — change one role per version and compare the results [3].

## Section 9 — Connections to Prior Topics

The 5-role framework is not a new set of techniques. It is a naming and ordering system for techniques you already know. Here is the mapping:

| Role | Prior topic | What you already learned |
|---|---|---|
| Authority | 13.1 (system prompt), 13.2 (role assignment) | The system prompt is the natural home for Authority. The role assignment from 13.2 is the first sentence of Authority. |
| Exemplar | 13.3 (few-shot examples) | Few-shot examples *are* Exemplars. The framework gives this a formal name and a position in the priority order. |
| Constraint | 13.5 (constraints) | Every negative instruction, guardrail, and scope limit from 13.5 belongs in the Constraint role. |
| Rubric | 13.6 (output format control) | Format specifications and template echoes from 13.6 all live in the Rubric. Chain-of-thought instructions from 13.4 also often appear here ("think step by step before answering"). |
| Metadata | 13.1 (static vs dynamic split) | The "dynamic" half of the context split from 13.1 — per-request injected facts — is what Metadata formalises. |

**What is new in 13.7** is the priority stack and the concept of a complete context package. Before now, you had individual techniques but no rule for resolving contradictions between them. The priority order (Authority > Exemplar > Constraint > Rubric > Metadata) is the key new concept this topic adds [1].

## Section 10 — Assessment Alignment

Your A4 portfolio (Python and Prompt Engineering Portfolio, 20%, due Week 13) requires three prompt versions for the same task with an accuracy comparison table. The 5-role context framework gives you a principled way to build those three versions. For Version 1, start with only Authority and a basic user message. For Version 2, add Exemplar and Constraint. For Version 3, add Rubric and Metadata. Because each version adds exactly one or two roles, your comparison table can attribute accuracy differences to specific roles — which is more rigorous than changing everything at once. The framework also makes the A4 output validator easier to write, because the Rubric role explicitly defines the format the validator should check against. This topic directly feeds the "three iteration versions" and "accuracy comparison table" deliverables in A4.

## Section 11 — Vocabulary List

**5-role context framework** — a structured approach to building prompts that organises every piece of context into one of five named roles: Authority, Exemplar, Constraint, Rubric, and Metadata.

**context package** — the complete set of information passed to a model in a single interaction, assembled from all five roles.

**authority role** — the part of a prompt that defines the model's identity and primary purpose; the highest priority in conflict resolution.

**exemplar role** — the part of a prompt that shows the model what a good output looks like, using one or more example input-output pairs.

**constraint role** — the part of a prompt that specifies what the model must not do or what limits apply; overrides Rubric and Metadata.

**rubric role** — the part of a prompt that describes the required structure and quality criteria for the output; shapes format and length.

**metadata role** — the part of a prompt that supplies per-request facts (date, user tier, language) that inform the model without overriding any instruction.

**priority stack** — the ordered rule (Authority > Exemplar > Constraint > Rubric > Metadata) used to resolve contradictions when two roles give conflicting instructions.

**conflict resolution** — the process of deciding which role's instruction to follow when two roles disagree.

---

## Concepts Introduced (for sequence.index.json)

- `5-role context framework`
- `context package`
- `authority role`
- `exemplar role`
- `constraint role`
- `rubric role`
- `metadata role`
- `priority stack`

## Prerequisites (JSON)

```json
["13.1", "13.2", "13.3", "13.5", "13.6"]
```

---

## Depth Profile and Diagram Assessment

**Depth profile recommendation:**
- Signals checked: five named sub-concepts each requiring individual definition; a priority/conflict-resolution table; an implementation section with 8 ordered steps; a full worked example with annotation table; a prior-topic mapping table.
- Recommended: **standard**
- Rationale: The topic coordinates five sub-concepts with a procedural implementation section, but each role is atomic in isolation. Standard depth (3000–4400 words) is appropriate; deep signals such as algorithmic complexity or multi-stage architecture are absent.

**Diagram assessment:**
- `requires_diagram`: true
- Signals checked: the concept is a hierarchy (five roles with a priority order); conflict resolution involves a directional decision rule; the implementation section has 8 ordered steps; a side-by-side role comparison is central to understanding; the priority table is a natural candidate for a visual stack.
- `diagram_intent`: A vertically stacked diagram showing the five roles in priority order from top (Authority) to bottom (Metadata), with a left-side arrow labelled "conflict wins upward" and right-side labels showing what each role controls.

---

_System-derived from the next entry in curriculum/sequence.md._
