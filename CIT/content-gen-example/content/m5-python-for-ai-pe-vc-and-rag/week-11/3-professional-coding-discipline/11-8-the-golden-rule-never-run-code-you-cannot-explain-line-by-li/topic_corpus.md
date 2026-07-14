---
topic_id: "11.8"
title: "The golden rule — never run code you cannot explain line by line"
position_in_module: 2
generated_at: "2026-06-13T00:00:00Z"
resource_count: 4
---

# 1. The Golden Rule — Never Run Code You Cannot Explain Line by Line — Topic Corpus

## 2. Prerequisites

This topic builds directly on 11.7 (Spec-first discipline). The spec-first workflow — specify, prompt, explain, test — established that you must understand your own requirements before asking AI to write code. This topic installs the discipline that comes immediately after: reading and understanding every line of the code AI hands back to you, before you run a single cell.

## 3. Learning Objectives

- Explain in plain language why the golden rule exists and what problem it prevents.
- Describe the risks of running AI-generated code you have not read and understood.
- Apply the explain-every-line habit to a short code block, narrating what each line does.
- Identify at least two signs that a piece of code contains logic you cannot yet account for.
- Distinguish between "the code ran without errors" and "I understand what the code does."
- Connect the golden rule to the A4 portfolio requirement for independent code ownership.

## 4. Introduction

Imagine a classmate hands you a completed essay to submit. You hand it in. Later, your lecturer asks you to explain your argument. You cannot — you never read it. The essay may have been correct, or it may have contained errors you would have caught if you had read it. Either way, you cannot stand behind work you do not understand.

AI tools like Claude, GitHub Copilot, and ChatGPT can produce Python code in seconds. This is genuinely useful. The risk is not that the code is always wrong — the risk is that you may run code you never read, code that could be mostly correct but silently wrong in ways that matter.

The golden rule is the single habit that separates a professional from someone who pastes and hopes: **never run code you cannot explain line by line.** This rule does not mean you must have written the code yourself. It means you must be able to look at every line and say, in plain words, what that line does and why it is there. If you cannot, you stop, read, and ask until you can. Only then do you run it.

This topic explains the rule in full. It defines what "explain line by line" actually means in practice, shows what goes wrong when the rule is broken, and gives you a concrete method for applying it every time AI hands you code. This rule also applies directly to your A4 portfolio — the assessment requires you to own your code, not just produce it.

## 5. Core Concepts

### 5.1 What "explain line by line" actually means

**Explaining a line of code** means being able to say, in plain English, what that one line does — what value it creates, what condition it checks, what function it calls, and why that step is needed at this point in the program.

This is not the same as reading the code aloud. Reading `score = score + 10` aloud gives you the syntax. Explaining it means saying: "This line takes the current value stored in the variable `score`, adds 10 to it, and writes the new total back into `score`. I expect this to happen when a student passes a round."

Notice the last sentence: "I expect this to happen when." That expectation is important. Explaining a line means you know not just what it does, but when and why it does it. That link — between the line and the intent behind it — is what the golden rule is protecting.

An easy test: if you can explain a line to a classmate who has never seen the code, and your explanation makes them nod, you understand that line. If you find yourself saying "I think it does something with the score…" — you do not yet understand it, and the rule says to stop and find out before running.

### 5.2 Why this rule exists: the risk of silent failure

Code can fail in two ways. **Loud failure** is when an error message appears — Python stops and tells you something went wrong. You know there is a problem. **Silent failure** is when the code runs without errors, produces output, and the output is wrong — but you do not realise it.

Silent failures are much more dangerous, because everything appears fine [2]. A loop might iterate one time too many. A calculation might use the wrong variable. An average might be computed on the wrong set of numbers. If you do not understand the code, you have no way to notice that the output is subtly wrong. You will trust it.

Research on AI-assisted coding shows that this is a real, documented pattern: developers who accept AI-generated code without reviewing it ship code with subtle logic errors at higher rates than those who read and verify each line [2]. The code compiled and ran — but it was wrong, and no error message announced the problem.

When you run code you cannot explain, you are in the position of the student who submitted the unread essay. The output might be correct, or it might be quietly wrong. Without understanding the code, you have no way to tell the difference [1].

### 5.3 AI generates code you did not write — and that changes your responsibility

Earlier in the course you were introduced to the four-layer model and Python's role as the orchestration layer. You have seen how a spec-first discipline (11.7) turns your plain-English requirements into a prompt, and AI turns that prompt into code.

The critical point is this: AI generates code **you did not write.** The code may look like it belongs to you once it appears in your notebook. But unless you read and understand every line, it is effectively borrowed — and you are responsible for it.

Addy Osmani, an engineering director at Google, makes this point directly in the context of professional code review: accepting AI-generated code without understanding it transfers the risk from the AI to you [1]. When the code is in your project, it is yours. If it does something wrong, you are accountable — not the tool that generated it.

For students, this matters in two practical ways. First, if an assessor asks you to explain your code and you cannot, that is a problem regardless of whether the code ran. Second, and more importantly, building the habit now means you will be a reliable professional later — one who can stand behind every line in a codebase, including lines you did not personally author.

### 5.4 "It ran without errors" is not the same as "I understand it"

This distinction is worth its own section because it is the most common confusion beginners make.

When you run a cell in Google Colab and see output instead of a red error message, it is natural to feel that the code is correct. "It worked" is the phrase people use. But "ran without errors" and "I understand what it does" are two completely different statements.

Consider this short code block:

```python
names = ["Ana", "Bo", "Cara"]
total = 0
for name in names:
    total = total + len(name)
average = total / len(names)
print(average)
```

This code runs without errors. It prints `3.6666666666666665`. Now consider what you need to be able to explain:

- Line 1: Creates a list called `names` holding three string values.
- Line 2: Creates a variable `total` and sets it to 0. This is the accumulator pattern from 11.6.
- Lines 3–4: Loops through each name. For each one, adds the length of that name (number of characters) to `total`.
- Line 5: Divides `total` by the number of names to get the average.
- Line 6: Prints the result.

Now: is this the code you wanted? It computes the average *length of names in characters* — not the average of any marks. If you asked for average marks and got this, the code ran cleanly but produced the completely wrong answer. If you had not read it, you would have trusted that output.

"It ran" is a technical fact. "I understand it" is a professional standard. The golden rule requires the professional standard, every time [3].

### 5.5 The four-question test for each line

When reading AI-generated code, apply these four questions to each line, in order:

1. **What does this line create or change?** Every line either creates a new variable or value, updates an existing one, or calls a function that produces some effect. Name exactly what is being affected.
2. **Where did the input come from?** Every value on the right side of an assignment was either hard-coded, received from the user, or computed earlier in the program. Trace it.
3. **Why is this line here at this point?** Does the order make sense? Would it break if this line came earlier or later?
4. **Does this match my spec?** Does what this line does correspond to something you wrote in your plain-English specification from 11.7?

If you cannot answer any of these four questions for a line, that is the line to investigate. You are not blocked — you can ask the AI to explain itself, you can search the Python documentation, you can ask a classmate. You just do not run the code until you have the answer [1] [4].

The fourth question is particularly powerful. If you have written a spec and the AI has generated code, every line in the code should be traceable to something in the spec. A line with no corresponding spec entry is either unnecessary, or it is covering something you forgot to specify. Either way, you need to know which.

### 5.6 How AI can produce plausible-looking wrong code

AI models generate code by predicting what code typically follows a given prompt. They are trained on enormous amounts of code, and they are very good at producing code that looks correct. "Looking correct" means: valid syntax, sensible variable names, comments that sound reasonable.

But there are categories of errors that AI generates with some frequency and that are hard to spot unless you read carefully [2]:

- **Off-by-one errors.** A loop that runs one iteration too many or too few. The code runs, but processes a boundary case incorrectly.
- **Wrong variable used.** Two variables with similar names; the AI uses the wrong one in a calculation. Everything looks right at a glance.
- **Wrong default assumption.** You meant for a value to start at 0 and the AI initialised it at 1, or vice versa. Subtle difference, wrong result.
- **Missing edge case handling.** The code works for typical inputs but fails or produces nonsense when the input is unusual — for example, when a list is empty, or a mark is 0.

None of these categories produce error messages. They produce wrong answers quietly. The only defence is reading every line before running.

This is also why 8th Light, a professional software consultancy, frames the obligation this way: using AI-assisted coding tools does not reduce your accountability for code quality — it changes *where* in the process you exercise that accountability [4]. You move from writing to reviewing, but reviewing is not optional. If anything, reviewing AI-generated code requires more careful attention than reviewing code you wrote yourself, because you did not make the choices and may not immediately see their implications.

### 5.7 The golden rule and your A4 portfolio

Your A4 Python and Prompt Engineering Portfolio is due in week 13 and counts for 20% of the course. The requirement explicitly includes:

- An original plain-English spec (spec-first discipline from 11.7).
- Independently working code.
- Edge-case tests, minimum three per notebook (covered in 11.9).
- A reflection.

"Independently working code" does not mean code you typed from scratch — using AI tools is expected and legitimate. It means code you can independently explain, defend, and modify. If an assessor asks "what does line 8 do?", the expected answer is an explanation — not "I'm not sure, the AI wrote it."

Applying the golden rule now, on every exercise, is what makes the A4 requirement achievable. By the time A4 is due, you will have explained hundreds of lines of code. Each time you do, you are building ownership of the language and the logic — not just producing output.

## 6. Implementation

### How to apply the golden rule: a step-by-step method

This procedure applies every time AI generates code for you, starting from the moment the code appears in your notebook.

**Step 1: Do not run the code yet.**
The temptation to run immediately is strong. Resist it. The code is not going anywhere. Run it only after completing the steps below.

**Step 2: Read the entire code block top to bottom.**
Before analysing individual lines, read the whole block once. Ask yourself: at a high level, does this code look like it is solving the problem from my spec? If something immediately does not look right, note it before diving into line-by-line analysis.

**Step 3: Work through each line using the four questions.**
For each line, ask: What does it create or change? Where did the input come from? Why is it here at this point? Does it match my spec? Write your answers as comments in the code cell or in the text cell above. This creates a record of your understanding — exactly what Journal Entry #6 and the A4 reflection will ask you to show [3].

**Step 4: If you cannot answer a question for any line, stop and investigate.**
- Ask the AI: "Explain what line 5 does and why it is needed here."
- Search the Python documentation for the function being used.
- Ask a classmate or your lecturer.

Do not guess and run. A guess does not become knowledge just because the code produced output.

**Step 5: Once you can explain every line, run the code.**
At this point, running is a confirmation, not a discovery. You already know — from your line-by-line explanation — what the output should be. If the output surprises you, that surprise is useful: something in your explanation was incomplete, and you now know exactly which line to revisit.

**Step 6: Note any lines you found hard to explain.**
These are exactly the lines most likely to harbour a silent failure. Mark them, come back to them, and revisit the spec to confirm they implement what you intended.

## 7. Real-World Patterns

### Where professionals encounter this discipline

The golden rule is not unique to students. It is a standard expectation in professional software teams, adapted to the AI-assisted era.

**Code review** — the practice of one engineer reading another's code line by line before it enters a shared codebase — exists in virtually every professional software organisation. Addy Osmani describes this process in the context of AI-generated code: the reviewer is responsible for understanding what was generated, not just checking that it compiled [1]. AI has sped up code authorship but has not eliminated — and has arguably intensified — the need for careful human review.

IEEE Spectrum's reporting on AI coding tools documents specific failure categories that appear when developers skip the understanding step: bugs that survive into production because reviewers did not read the code carefully, security vulnerabilities introduced silently, and logic errors that only surface in edge cases [2]. These are not theoretical risks. They are documented failure patterns in working professional systems.

8th Light frames it in terms of professional accountability: an AI tool is not a professional peer who can share responsibility for the outcome [4]. The tool generates a suggestion. You decide whether that suggestion is correct. That decision requires understanding, not just execution.

For you, right now, the real-world pattern is simpler: every time you complete an exercise or build something for A4, you are practicing the same habit professionals depend on. The difference between a junior developer who earns trust quickly and one who does not often comes down to this single question: can you explain what your code does?

## 8. Best Practices

**Do:**

- **Read before you run.** Every time. Without exception. The rule is not "read when you are unsure" — it is "read before every run."
- **Write line-by-line explanations as comments.** Place a comment above or after each non-obvious line. This forces you to articulate your understanding and creates a record.
- **Trace every value back to its source.** For any variable on the right side of an assignment, ask where its current value came from.
- **Compare code to your spec line by line.** Every line should correspond to something in your spec. If it does not, find out why.
- **Use the AI to explain itself.** If a line puzzles you, ask: "Explain what this line does in plain English." The AI is a tool for understanding as well as generation.

**Do not:**

| Anti-pattern | Why it fails |
|---|---|
| Running code immediately after AI generates it | Skips the only check against silent failure. |
| Assuming "no error = correct" | Confuses technical execution with logical correctness. |
| Explaining code only at the block level ("this block computes the average") | Misses line-level errors hiding inside correct-looking blocks. |
| Marking a line "understood" when you can only paraphrase the syntax | Syntax tells you what was written; semantics tells you what it does. Only the second counts. |
| Asking "does this look right?" instead of "can I explain this?" | Appearance is not understanding. Plausible-looking wrong code is a documented failure mode [1] [2]. |

## 9. Hands-On Exercise

This exercise maps directly to Journal Entry #6 and the lab activity for this session.

**Setup.** Write a plain-English spec for the following program: given a student's name and three marks, print the average and a grade (A = 90+, B = 80–89, C = 70–79, F = below 70). Use the spec-first workflow from 11.7: list inputs, outputs, constraints, and two or three examples showing expected inputs and correct outputs.

1. Paste your spec as a prompt to an AI tool. Receive the generated code — do not run it yet.
2. Go line by line through the generated code. For each line, write a plain-English comment explaining what it does and why it is there.
3. If any line puzzles you, ask the AI to explain it before continuing.
4. Once you can explain every line, run the code and confirm the output matches your spec examples.
5. In a text cell below the code, write a short journal paragraph: which line was hardest to explain? What did you do to understand it? Did the AI's code match your spec exactly, or did you find differences?

This pattern — spec, prompt, explain every line, run, reflect — is the template for every notebook in A4.

## 10. Key Takeaways

- The golden rule — never run code you cannot explain line by line — is the single most important professional habit this course teaches. The rule holds for every line, every time, with no exceptions.
- "The code ran without errors" is a technical fact. "I understand what the code does" is a professional standard. Only the second one protects you from silent failure.
- AI-generated code is your responsibility the moment it enters your notebook. You did not write it, but you own it. Ownership requires understanding, not just execution.
- The four-question test — What does it create or change? Where did the input come from? Why is it here now? Does it match my spec? — gives you a concrete, repeatable method for applying the rule to any line of code.
- For A4, you are not just assessed on whether your code runs. You are assessed on whether you can explain and defend it. Every time you apply the golden rule in your exercises, you are building that capability.

## 11. Next Steps

_System-derived from the next entry in curriculum/sequence.md._
