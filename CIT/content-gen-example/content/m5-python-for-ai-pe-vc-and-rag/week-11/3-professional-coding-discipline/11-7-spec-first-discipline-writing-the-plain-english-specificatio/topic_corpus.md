---
topic_id: "11.7"
title: "Spec-first discipline — writing the plain-English specification before writing or prompting code"
position_in_module: 1
generated_at: "2026-06-13T04:35:00Z"
resource_count: 5
---

# 1. Spec-first discipline — Topic Corpus

## 2. Prerequisites

This topic uses the grade-average script built across 11.3–11.6 as a running example. You should be comfortable with variables (11.3), data types (11.4), if/elif/else (11.5), and for loops with lists (11.6). No new Python syntax is introduced here; the skill introduced is a way of thinking about programs before writing them.

In 11.5 (§7 In Practice) you saw a brief mention: *"The discipline of sketching the decision diamond on paper first — and then translating each diamond into an if/elif line — is the core of the spec-first approach introduced in 11.7."* This topic makes that discipline explicit.

## 3. Learning Objectives

By the end of this topic you will be able to:

1. Explain what a plain-English specification is and why writing it before any code — or before any AI prompt — reduces errors.
2. Write a specification for a simple program, naming the inputs, their types and constraints, the expected output, and at least two concrete examples.
3. Identify the four-step spec-first workflow: specify → prompt → explain every line → test edge cases.
4. Explain why you cannot verify AI-generated code unless you can predict its output from the specification before running it.
5. Map the grade-average lab script to each part of a specification (inputs, outputs, constraints, examples).

## 4. Introduction

You now know enough Python to implement the full grade-average script. You could ask an AI assistant to write it for you right now. But how would you know if the code it gave you was correct? [2]

If you cannot answer that question before you run the code, you have a problem — not with the AI, but with your own understanding of what the program is supposed to do. A program that "looks right" is not the same as a program that *is* right [1][2].

The solution is simple: write down what the program should do in plain English *before* writing — or prompting — any code. This written description is a **specification** (or **spec**). The spec is both the blueprint for the code and the yardstick against which you measure whether the code is correct [1][2][3].

This practice — spec first, code second — is not new. Professional software engineers have followed it for decades. What is new is that with AI-assisted coding, the spec also becomes the raw material for your prompt. The clearer your spec, the cleaner your prompt, the less the AI hallucinates [3][5].

## 5. Core Concepts

### 5.1 What is a specification?

A **specification** is a written description of a program's intended behaviour [1][2]. It has four parts:

| Part | Question it answers | Example (grade-average script) |
|---|---|---|
| **Inputs** | What goes in? What type? What range? | Student name (string), 3 marks (integer, 0–100 each) |
| **Outputs** | What comes out? What format? | One line: `"Alice averaged 83.7 — Grade: B"` |
| **Constraints** | What rules govern the behaviour? | A≥90, B≥80, C≥70, D≥60, F<60; average rounded to 1 decimal place |
| **Examples** | What are 2–3 concrete input→output pairs? | Alice 88,72,91 → B; Bob 45,50,55 → F |

The spec does not mention variables, loops, or if-statements. It describes *what* the program does, not *how* it does it. How is the code's job; what is your job [1][2].

### 5.2 Why write the spec before the code?

**Reason 1: Clarity of thought.** Writing forces precision. "The program takes marks and prints the grade" is vague — what if there are two marks? What if a mark is 150? Completing the spec table forces you to answer these questions before they become bugs [1][2].

**Reason 2: A spec you cannot write means a problem you do not understand.** If you find yourself unable to fill in the Inputs, Outputs, or Constraints columns, the program is not ready to be written. No amount of code — human or AI-generated — can fix an under-specified problem [1][2].

**Reason 3: The spec is your verification standard.** When the code runs and produces output, you check it against the spec's examples. If `Bob 45,50,55` gives `"Bob averaged 50.0 — Grade: F"` and your spec said it should, the code passes — for that case. If the output differs, the code (not the spec) is wrong [2][4].

**Reason 4: With AI, the spec is also the prompt.** You cannot write a good prompt without a clear spec. Paste the spec table directly into your prompt: *"Write Python code that takes a student name (string) and three marks (integers 0–100). It should compute the average rounded to 1dp and print `[name] averaged [avg] — Grade: [letter]`, where A≥90, B≥80, C≥70, D≥60, F otherwise."* That prompt produces better code than *"write a grade calculator"* [3][5].

### 5.3 The four-step spec-first workflow

The workflow has four steps. Steps 1 and 2 are this topic. Steps 3 and 4 are introduced in 11.8 and 11.9 respectively:

```
Step 1: Write the spec     ← this topic
Step 2: Prompt the AI      ← this topic (the spec IS the prompt)
Step 3: Explain every line ← 11.8 (the golden rule)
Step 4: Test edge cases    ← 11.9
```

You should not move from step 1 to step 2 until the spec is complete. You should not move from step 2 to step 3 until you can explain what each line of the generated code should do *from the spec alone*. You should not move from step 3 to step 4 until every line is understood [1][2][3].

This ordering protects you from the most common AI-assisted coding mistake: running code you do not understand because it "looks reasonable" [2][5].

### 5.4 What a good spec looks like — and what a bad one looks like

**Good spec (complete):**
```
Program: Grade Average Calculator
Inputs:  - student_name (string, non-empty)
         - mark1, mark2, mark3 (integer, 0–100 inclusive)
Outputs: One print line: "[name] averaged [X.X] — Grade: [letter]"
         where X.X is the arithmetic mean rounded to 1 decimal place
Constraints:
         - A if avg >= 90; B if >= 80; C if >= 70; D if >= 60; F otherwise
         - marks outside 0–100 are assumed valid in this version
Examples:
         Input:  Alice, 88, 72, 91  → Output: Alice averaged 83.7 — Grade: B
         Input:  Bob, 45, 50, 55    → Output: Bob averaged 50.0 — Grade: F
         Input:  Carol, 90, 90, 90  → Output: Carol averaged 90.0 — Grade: A
```

**Bad spec (vague):**
```
Program: Grade calculator
Input: some marks
Output: print the grade
```

The bad spec gives the AI — and you — nothing to verify against. Any output the code produces could be claimed to be "correct" because "correct" was never defined [1][2].

### 5.5 The spec as a prompt template

The good spec above translates directly into an AI prompt by adding a sentence asking for implementation [3][5]:

*"Write Python code that does the following: [paste the spec]. Use variables, if/elif/else, and a for loop. Show the code in a single cell, no libraries."*

When the AI responds, read the code and ask: *"If I run this with Alice, 88, 72, 91, will I get 'Alice averaged 83.7 — Grade: B'?"* If you cannot answer that question by reading — not running — the code, you need to apply 11.8's golden rule before proceeding [4][5].

## 6. Implementation

**Writing the spec before opening Colab:**

The lab activity for this week is a grade-average script. The spec-first approach means your first deliverable is a text document, not a code cell.

Here is the grade-average spec mapped to each spec element:

```
Spec: Grade Average Calculator (Week 11 Lab)

Inputs:
  - student_name: string, typed by the user via input()
  - Three marks: integers, entered via input() and converted with int()
  - Assumption: user types valid integers in the range 0–100

Outputs:
  - Single line printed to the console:
    "[student_name] averaged [average] — Grade: [letter]"
  - average is the arithmetic mean of the three marks, rounded to 1dp
  - letter is assigned by the following thresholds:
      A if average >= 90
      B if average >= 80
      C if average >= 70
      D if average >= 60
      F if average < 60

Constraints:
  - Use only Python constructs from 11.1–11.6
  - No third-party libraries
  - Input must be converted to int before arithmetic

Examples:
  Alice, 88, 72, 91  →  Alice averaged 83.7 — Grade: B
  Bob,   45, 50, 55  →  Bob averaged 50.0  — Grade: F
  Carol, 90, 90, 90  →  Carol averaged 90.0 — Grade: A
```

This spec can be pasted verbatim into a Claude or ChatGPT prompt. The AI will return code. You then apply steps 3 and 4 (11.8 and 11.9) before considering the task complete [3][5].

**Spec-to-prompt mapping:**

The Inputs row becomes the part of the prompt that says *"accept student_name via input() and three marks via input(), converting each with int()."* The Constraints row tells the AI which Python constructs are in scope. The Examples row lets the AI check its own output for a sample case [3][5].

## 7. Real-World Patterns

**Product requirement documents.** Every professional software feature begins with a written description before anyone writes code. These documents go by different names (PRD, functional spec, design doc), but the structure is the same: inputs, outputs, constraints, examples [1][2]. A codebase without a spec is a liability; reviewers cannot tell whether the code is correct because "correct" was never written down.

**AI pipeline specifications.** Before building a pipeline that classifies student essays or filters customer support tickets, a data engineer writes down: what goes in (the text), what comes out (a label and a confidence score), what the constraints are (response must be JSON, must complete in under 2 seconds), and what a sample input-output pair looks like. Without this, there is no way to tell if the pipeline is working [3][5].

**Prompt = distilled spec.** The quality of an AI prompt is bounded by the quality of the spec behind it. A vague spec produces a vague prompt, which produces vague code, which cannot be verified. A precise spec produces a precise prompt, which produces precise code, which can be verified against the examples in the spec [3][5].

## 8. Best Practices

- **Write the spec before opening the code editor or the chat window.** The act of writing forces clarity; the act of typing code (or prompting) encourages skipping ahead while requirements are still fuzzy [1][2].
- **Include at least two examples with exact expected output.** One example can be an accident. Two diverging examples (e.g., one pass and one fail) reveal edge cases you may not have considered [2].
- **Do not write "the program should handle invalid input" without specifying how.** Vague constraints are no constraints. Either say "invalid input raises ValueError and is caught" or "invalid input is assumed not to occur in this version" — both are valid; vagueness is not [1].
- **The spec is a live document.** If the code reveals a constraint you forgot, update the spec first, then update the code. Never let the code drift ahead of the spec [1][2].

## 9. Hands-On Exercise

1. Open a blank document (or a Colab text cell).
2. Without looking at the worked example above, write the full spec for the grade-average script: Inputs, Outputs, Constraints, Examples.
3. Compare your spec to the worked example in §6. List any element you missed.
4. Paste your spec into an AI assistant with the instruction: *"Implement this specification in Python using only variables, if/elif/else, and a for loop."*
5. Receive the code. Before running it: read each line and verify that it will produce the output your spec examples predict.

## 10. Key Takeaways

- A **specification** is a written description of a program's inputs, outputs, constraints, and examples — written before any code or prompt [1][2].
- Writing the spec forces clarity: a spec you cannot complete means a problem you do not understand [1][2].
- The spec is the **verification standard**: when the code runs, you check its output against the spec's examples, not your intuition [2][4].
- The spec is also the **prompt ingredient**: paste it directly into an AI prompt for more precise, verifiable code generation [3][5].
- The four-step workflow is: **specify → prompt → explain every line (11.8) → test edge cases (11.9)** [1][2][3].

## 11. References

1. Fowler, M. *On the Nature of Software*. martinfowler.com. https://martinfowler.com/articles/on-the-nature-of-software.html
2. Spolsky, J. *Painless Functional Specifications — Part 1: Why Bother?* Joel on Software. https://www.joelonsoftware.com/2000/10/02/painless-functional-specifications-part-1-why-bother/
3. Prompt Engineering Guide. *Introduction — Basics*. https://www.promptingguide.ai/introduction/basics
4. Real Python. *Writing Comments in Python*. https://realpython.com/python-comments-guide/
5. Anthropic. *Prompt Engineering Overview*. https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview
