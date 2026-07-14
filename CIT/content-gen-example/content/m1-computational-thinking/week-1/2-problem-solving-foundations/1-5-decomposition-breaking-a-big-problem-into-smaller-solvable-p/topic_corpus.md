---
topic_id: "1.5"
title: "Decomposition — breaking a big problem into smaller solvable parts"
position_in_module: 1
generated_at: "2026-06-20T00:00:00Z"
resource_count: 3
---

# 1. Decomposition — breaking a big problem into smaller solvable parts — Topic Corpus

## 2. Prerequisites

This topic builds on **Topic 1.1 — What is computation** (the input / process / output model and the idea of defined steps). The concept of computational thinking introduced there is the broader framework that decomposition belongs to. Topics 1.2–1.4 (deterministic systems, probabilistic systems, and why AI gives different answers) are assumed knowledge but are not directly required for this topic.

## 3. Learning Objectives

By the end of this topic, you will be able to:

- Define decomposition in plain language as a problem-solving strategy.
- Explain why large problems are difficult to solve all at once and how breaking them down helps.
- Identify the parts of a real-world problem and arrange them into a task tree — a diagram that shows how smaller parts connect to the whole.
- Distinguish between a problem that has been well decomposed and one that has not.
- Describe at least three real-world situations in which decomposition is used to make a complex task manageable.
- Apply decomposition to a problem of your own choosing, producing a written or visual list of sub-tasks.

## 4. Introduction

Imagine you are asked to "plan a party." Those three words hide dozens of decisions and actions: picking a date, choosing a venue, inviting guests, buying food, organising entertainment, and much more. If you try to think about all of those at once, the task feels overwhelming. So what do most people do? They split it up. They write a list. They tackle one piece at a time.

That instinct — breaking a big problem into smaller, more manageable pieces — is exactly what computer scientists mean when they say **decomposition** [1].

Now imagine giving that same "plan a party" task to a computer program. The program cannot act on a vague instruction. It needs every step to be specific and unambiguous (you saw in Topic 1.1 that computation requires defined steps). Decomposition is how you — the person designing the program — figure out what those steps are before writing a single line of code [1][2].

Decomposition is one of the four pillars of **computational thinking** — the style of problem-solving that makes problems approachable by both humans and computers [1]. You have already worked with one pillar — the input / process / output model. Decomposition is the next. Later topics will cover abstraction, pattern recognition, and algorithm design — those are forward pointers only; this topic stays on decomposition.

## 5. Core Concepts

### 5.1 What decomposition means

**Decomposition** — breaking a large, complex problem into smaller parts that are easier to understand, plan, and solve [1][2][3].

The word itself comes from Latin: *de-* (down, apart) + *componere* (to put together). Decomposition literally means "taking apart." You take a big problem apart into pieces you can handle one at a time.

A decomposed problem has three properties:

- Each smaller part is **focused** — it deals with one clear thing, not everything at once.
- Each smaller part is **manageable** — a person or program can work on it without holding the entire original problem in mind.
- When all the smaller parts are completed, the original problem is solved.

Here is a plain definition:

> **Decomposition** is the process of identifying the distinct parts of a problem and describing each part clearly enough to be solved on its own [1].

### 5.2 Why big problems are hard without decomposition

Think about trying to read every word on every page of a textbook at the same time. You cannot — your brain can only focus on one thing at a moment. You read a page, then the next. Reading one page at a time is natural decomposition.

Complex problems are hard for similar reasons. When a problem is large:

- It involves too many things to keep in mind at once.
- It is not clear where to start.
- One part becomes tangled with another, making progress on either difficult.
- Errors in one part affect everything, and finding those errors is hard [1][2].

Decomposition solves all of these. When you break a problem into parts:

- Each part is small enough to focus on.
- You have a natural starting point — the parts that do not depend on anything else.
- Progress on one part does not require finishing every other part first.
- If something goes wrong, you know which part caused it [2][3].

This is not only useful for programmers. Builders use decomposition when constructing a house (foundation, walls, roof, plumbing, electrics — each separately). Doctors use it when diagnosing a patient (gather history, run tests, rule out causes — one at a time). Teams use it when planning projects (split work into tasks, assign each task) [3].

### 5.3 The task tree — showing decomposition visually

When you decompose a problem, the result is often shown as a **task tree** — a diagram that looks like an upside-down tree. The original problem sits at the top. Below it, the first level of sub-tasks branches out. Each sub-task can branch further into smaller sub-tasks, and so on, until every item at the bottom is concrete and doable [1][2].

Here is a simple example using "Plan a party":

```
Plan a party
├── Choose a date and venue
│   ├── Check everyone's availability
│   └── Book the location
├── Invite guests
│   ├── Write the invitation
│   └── Send invitations
├── Organise food
│   ├── Decide on menu
│   ├── Buy ingredients
│   └── Prepare food
└── Set up entertainment
    ├── Choose activities
    └── Gather equipment
```

Each item at the bottom — "Check everyone's availability," "Write the invitation," "Buy ingredients" — is something specific. You can act on it directly. None of them is "plan a party" — they are concrete, finite pieces [2][3].

**Key terms in a task tree:**

| Term | Plain meaning |
|---|---|
| **Root** | The original, big problem at the top of the tree |
| **Sub-task** | A smaller part that the root or a higher-level task breaks into |
| **Leaf** | A task at the bottom with no further breakdown — something you can act on directly |
| **Level** | One row of the tree; tasks at the same level are roughly the same size |

### 5.4 What makes a good decomposition

Not every breakdown of a problem is a good decomposition. A good decomposition has specific qualities [1][2][3].

**A good decomposition:**

- **Covers everything.** No part of the original problem is left out. If you completed every leaf task, the whole problem would be solved.
- **Has no significant overlap.** Each sub-task handles its own piece. Two sub-tasks should not both try to do the same thing.
- **Produces parts that are the right size.** Parts still too big need further breakdown. Parts so tiny they are trivial probably do not need their own entry.
- **Is ordered sensibly.** Some parts depend on others (you cannot write an invitation before knowing the date). A good decomposition makes these dependencies visible.

**A poor decomposition:**

- Leaves out an important piece (e.g., forgetting to budget for food).
- Has vague sub-tasks that are not much clearer than the original ("deal with the logistics" is not useful).
- Groups unrelated things together (food and legal paperwork should not be in the same sub-task).
- Ignores dependencies (listing "send invitations" before "choose a date").

### 5.5 Decomposition is iterative — you refine as you go

You will rarely get decomposition right on the first try. That is normal and expected [1][2].

**Iterative** means you do something, review the result, adjust it, and repeat. With decomposition:

1. Make your first attempt at breaking down the problem.
2. Look at each sub-task and ask: "Is this clear enough to act on? Is this small enough?"
3. If the answer is no, break that sub-task down further.
4. Repeat until every item is concrete and doable.

This refinement process is part of good problem-solving, not a sign you did something wrong the first time. Even experienced software engineers revise their decomposition as they learn more about a problem [1][3].

### 5.6 Decomposition and computation — why computers need it

You learned in Topic 1.1 that computation requires defined steps. A computer program cannot act on "plan a party" — it needs every step to be precise and unambiguous.

Decomposition is the bridge between a human idea and a computer process. When you decompose a problem, you are working out what a computer would need to do, step by step, to solve it. You are not yet writing pseudocode (a later topic). You are simply figuring out the parts [1][2].

This is why decomposition is taught before programming. If you cannot describe a problem in small, clear pieces, you cannot write a program to solve it. The program is only as clear as your decomposition [1][3].

## 6. Implementation

Decomposition is a thinking and planning activity, not a programming one. The steps here are the steps you take as a problem-solver [1][2].

**How to decompose a problem — a repeatable process:**

1. **Write the problem at the top.** State it in one sentence. If you cannot state it in one sentence, the problem may not yet be clear enough [1].

2. **Ask: "What are the major parts of this problem?"** List the highest-level sub-tasks. Aim for two to five. More than five at one level often means you are jumping to detail too fast [1][2].

3. **For each sub-task, ask: "Is this small enough to act on directly?"** If yes, it is a leaf — you are done with that branch. If no, treat it as a new mini-problem and repeat from step 2 [1].

4. **Check for completeness.** Look at the full tree and ask: "If I completed every leaf task, would the original problem be solved?" If there is a gap, add the missing sub-task [2].

5. **Check for overlap.** Look for any two sub-tasks doing the same thing. If you find them, merge or re-divide [2].

6. **Order the tasks.** Identify which sub-tasks must be completed before others can start. Note those dependencies [1][3].

**Worked decomposition — step by step:**

Problem: "Build a simple website for a local library." [2]

Step 1 — Write the problem:
> Build a simple website for a local library.

Step 2 — Major parts:
> - Decide what the website needs to do
> - Design the layout and look
> - Write the content (text, images)
> - Build the site technically
> - Test and publish the site

Step 3 — "Decide what the website needs to do" is still big. Break it further:
> - Talk to library staff about what they need
> - List the features the site must have
> - Decide what the site will NOT include

Step 4 — Completeness check: Does completing all parts result in a published, working library website? Yes [1].

Step 5 — Overlap check: "Write the content" and "Design the layout" might overlap on images. Clarify: design handles placement; content writing handles what text and which images to use [2].

Step 6 — Order: "Decide what the website needs to do" must happen first. "Test and publish" must happen last. The others can overlap [1].

You now have a decomposed plan you could hand to a team of people — or use as the structure for a program [1][2].

## 7. Real-World Patterns

### Software development teams

Professional software developers almost never start coding without a decomposition step. A project is broken into features. Each feature is broken into user stories — descriptions of what a user wants to do. Each user story is broken into tasks. Each task goes to one developer. The entire practice of project management in software is applied decomposition [1][2].

### Recipe writing

A recipe is a worked example of decomposition. "Make a chocolate cake" becomes: make the batter, bake the batter, make the frosting, assemble the cake. "Make the batter" breaks down further: measure ingredients, combine dry ingredients, combine wet ingredients, mix together. Each step at the bottom is a concrete, doable action [3].

### Medical procedures

Surgeons decompose complex operations into stages. An operation on the knee is not one undifferentiated activity. It has a sequence of sub-tasks: anaesthesia, incision, working on the joint, closure, recovery plan. Each sub-task has its own specialist, checklist, and success criterion [2][3].

### Emergency response planning

Emergency services decompose a disaster response into parallel workstreams: search and rescue, medical triage, evacuation, communications, and logistics. Each workstream is managed independently and can proceed while others are ongoing. Without decomposition, the response would be chaos — everyone trying to do everything at once [2].

### AI system design

When engineers design an AI system (like the language models from Topic 1.4), they do not build the whole thing at once. They decompose it: data collection, data cleaning, model training, evaluation, deployment, monitoring. Each stage has its own team, tools, and success criteria. The final working system is the result of completing all the decomposed parts [1][3].

## 8. Best Practices

- **Start with the problem statement, not the solution.** Decomposition is about understanding the problem clearly before thinking about how to solve it. A vague problem gives a vague decomposition. Make the problem crisp before you break it down [1].

- **Stop when a task is concrete and doable.** You do not need to decompose forever. When a sub-task is clear enough that a person (or program) could act on it without further clarification, it is a leaf. Over-decomposing into trivially small pieces adds noise without clarity [2][3].

- **Name tasks with verbs.** A sub-task should describe an action: "Choose a venue," not "Venue." Verb-first naming makes it obvious what needs to be done and when you are done [2].

- **Make dependencies explicit.** If task B cannot start until task A is done, write that down. Dependencies shape the order of work and help you avoid bottlenecks [1][3].

- **Revisit and revise.** As you learn more about a problem, your decomposition will change. That is expected. A decomposition is a working document, not a contract [1].

## 9. Hands-On Exercise

This exercise connects to the lab activity for this session.

1. Choose one real-world task you are familiar with — cooking a meal, organising a study group, or setting up a social media profile.

2. Write the task at the top of a blank page (or open Excalidraw). This is your root.

3. Ask: "What are the two to five major parts of this task?" Write each as a branch below the root.

4. For each branch, ask again: "Can I act on this directly?" If yes, stop. If no, break it down one more level.

5. Swap your task tree with a partner. Can they understand every leaf task without asking you a question? If they need to ask, that sub-task needs to be clearer.

The goal is a tree where every item at the bottom is something a person could start doing immediately, with no further instruction needed.

## 10. Key Takeaways

- **Decomposition is the strategy of breaking a large problem into smaller parts.** Each part is focused, manageable, and solvable on its own — and completing all the parts solves the original problem [1][2].
- **Task trees make decomposition visible.** The original problem sits at the root; sub-tasks branch below it; leaf tasks at the bottom are concrete enough to act on directly [1][3].
- **A good decomposition covers everything, avoids overlap, and makes dependencies clear.** A poor decomposition leaves gaps, uses vague sub-tasks, or groups unrelated things together [2].
- **Decomposition is iterative.** You refine it as you learn more about the problem. Getting it wrong on the first try is normal and expected [1][2].
- **Computers require defined steps.** Decomposition is the thinking work that produces those steps before any program is written [1].

## 11. Next Steps

_System-derived from the next entry in curriculum/sequence.md._
