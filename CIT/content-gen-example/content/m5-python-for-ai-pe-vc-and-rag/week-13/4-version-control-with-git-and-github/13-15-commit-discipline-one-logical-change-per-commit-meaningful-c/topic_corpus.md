---
topic_id: "13.15"
title: "Commit discipline — one logical change per commit, meaningful commit messages"
position_in_module: 6
generated_at: "2026-06-15T00:00:00Z"
resource_count: 3
---

# 1. Commit Discipline — One Logical Change per Commit, Meaningful Commit Messages — Topic Corpus

## 2. Prerequisites

- **13.11** — Git fundamentals — repository, commit, branch, merge (introduces: repository, commit, snapshot, commit message, commit history, HEAD)
- **13.12** — GitHub workflow — clone, add, commit, push (introduces: staging area, git add, git commit, git push, commit hash)
- **13.10** — Why version control matters (introduces: version history, change log)

## 3. Learning Objectives

By the end of this topic you will be able to:

- Define what an **atomic commit** is and explain why mixing changes into one commit is a problem.
- Write a commit message that follows the imperative-mood subject + body convention.
- Distinguish a good commit message from a poor one using concrete criteria.
- Apply the 50-character subject and 72-character body-wrap rules when writing messages.
- Stage and commit a single logical change using `git add` and `git commit`.
- Explain how good commit discipline makes your project history readable to others (and to future you).

## 4. Introduction

Imagine you are reading someone's diary. Each page covers one clear event: "Bought groceries," "Had a job interview," "Cooked dinner for the first time." That diary is easy to follow. Now imagine every page says "Stuff happened." You would have no idea what the person actually did.

Your project's commit history is that diary. Every time you run `git commit`, you leave a note in your project's permanent record. That note is called a **commit message** — the short label attached to a snapshot of your work. If the note says something vague like "fixed stuff" or "changes," it tells nobody — including future you — what actually happened.

This topic teaches two habits that make that history useful:

1. **Commit one logical change at a time** — keep each snapshot focused.
2. **Write a commit message that explains what changed and why** — make each note meaningful.

These habits matter now because your Assessment 4 portfolio requires multiple meaningful commits. Reviewers (and employers) will read your commit history. A tidy, well-labeled history is a professional signal.

## 5. Core Concepts

### 5.1 Atomic Commits

**Atomic commit** — a commit that contains exactly one logical change. [1][2]

The word "atomic" comes from the Greek word for "indivisible." In chemistry, an atom cannot be split into smaller pieces and still be that element. An atomic commit follows the same idea: the change inside it cannot be split further without losing meaning.

**What counts as one logical change?**

One logical change is one *reason* to change the code. Examples:

| One logical change (atomic) | Mixed changes (not atomic) |
|---|---|
| Add a `README.md` with project description | Add README + fix a typo in `main.py` + add `.gitignore` |
| Fix a bug where the chatbot crashes on empty input | Fix the crash + refactor the response formatter |
| Add `.gitignore` to exclude the `.env` file | Add `.gitignore` + update requirements + rename a function |

Every row on the left side has one reason to exist. Every row on the right side has two or more.

**Why does this matter?**

Three concrete reasons:

1. **Easier to understand.** When you read a commit with one change, you know exactly what was done. When you read a commit with five changes tangled together, you have to untangle them mentally before you understand any of them. [2]

2. **Easier to undo.** Git lets you reverse a single commit later. If a commit is atomic, reversing it undoes exactly one thing. If a commit mixes five changes, reversing it undoes all five — even the ones you want to keep. [2]

3. **Cleaner history for your team (and reviewers).** The person reviewing your Assessment 4 portfolio will scan your commit history. A series of focused, labeled commits tells a clear story of how you built the project. A series of "misc changes" commits tells no story at all.

**The simple test for atomicity:**

Ask yourself: "Can I describe this commit in one short sentence without the word 'and'?"

- "Add .gitignore" → passes.
- "Add .gitignore and fix README typos and rename main function" → fails. Split it.

### 5.2 Meaningful Commit Messages

A **commit message** is the text you provide when you run `git commit`. It is stored permanently in your commit history. Every collaborator — and every future version of you — will read it. [1]

#### The anatomy of a commit message

A well-formed commit message has two parts [1]:

```
<subject line>
<blank line>
<body>
```

**Subject line** — the short summary. Rules:

- Keep it under **50 characters**. This is the headline; short headlines are easier to scan. [1][3]
- Start with a **verb in the imperative (command) mood**: "Add", "Fix", "Remove", "Update", "Rename". Not "Added", "Fixes", "I added".
- Do **not** end it with a period.
- Capitalize the first word.

Why imperative mood? Because the subject line completes the sentence: "If applied, this commit will \_\_\_\_." "If applied, this commit will *Add login validation*" — that reads naturally. "If applied, this commit will *Added login validation*" — that does not. [1]

**Body** — the explanation. Rules:

- Leave one blank line between the subject and the body. [1]
- Wrap each line at **72 characters**. Long lines are hard to read in many terminals and code-review tools. [1][3]
- Explain **what changed and why** — not how (the code already shows how). [1]
- The body is optional for trivial changes (e.g., "Fix typo in README") but strongly encouraged whenever the reason for the change is not obvious.

#### Good vs bad message comparison

| Poor message | Good message |
|---|---|
| `fixed stuff` | `Fix crash when user submits empty prompt` |
| `update` | `Update README with setup instructions` |
| `wip` | `Add .gitignore to exclude .env and __pycache__` |
| `changes to main.py` | `Remove hardcoded API key from main.py` |
| `final version!!` | `Add requirements.txt with all project dependencies` |

Notice: every good message starts with a verb, tells you *what* changed, and is short enough to read at a glance. [1][3]

#### What belongs in the body

The body answers questions the subject line cannot:

- Why was this change necessary?
- What problem does it solve?
- Is there anything surprising or non-obvious about the approach?

Example of a complete message:

```
Add .gitignore to exclude .env and __pycache__

.env contains API keys that must never be committed to a public
repository. __pycache__ is auto-generated by Python and adds no
value to version history.
```

Subject: 47 characters, imperative verb, no period.
Body: explains *why* — the information the code itself cannot show you.

## 6. Implementation

### How to make an atomic commit with a meaningful message

Follow these steps each time you are ready to commit:

1. **Check what you have changed.**

   ```bash
   git status
   ```

   This lists every modified file in your working directory. Review it. If you see files from different tasks (e.g., a bug fix AND a new feature), you will need to commit them separately.

2. **Stage only the files for this one logical change.**

   Use `git add` to place specific files onto the staging area (also called the index — the area you already learned in topic 13.12):

   ```bash
   git add README.md
   ```

   Do *not* use `git add .` (add everything) when you have mixed changes. That puts unrelated files into the same commit.

3. **Write your commit message.**

   ```bash
   git commit -m "Add README with project description"
   ```

   The `-m` flag lets you supply the subject line directly. For a longer message with a body, omit `-m` and Git opens your default text editor so you can write the full message.

4. **Verify the commit was created.**

   ```bash
   git log --oneline
   ```

   This shows your recent commits in one line each. Your new commit should appear at the top with the subject you wrote.

5. **Repeat for each logical change.**

   Go back to step 1 for the next change. Each trip through the loop creates one clean, labeled snapshot.

### Staging parts of a file (advanced tip — name only)

In some situations you may have two unrelated changes inside the same file. `git add -p` lets you stage individual chunks. You will encounter this naturally as you build more complex projects; it is not required for your Assessment 4 portfolio.

## 7. Real-World Patterns

Open-source projects and professional teams treat commit discipline as a non-negotiable standard. The OpenStack project — a large cloud computing platform used by major companies — publishes explicit commit message guidelines for all contributors. Their rules match what you learned here: imperative subject line, 50-character limit, 72-character body wrap, and one logical change per commit. [2]

Why do teams enforce this? Because on a project with hundreds of contributors, a badly labeled commit wastes everyone's time. A clear commit history acts like a structured change log (a concept from topic 13.10) — you can scroll backward through history and understand what changed, when, and why, without reading the actual code.

For your Capstone project: your commit history is part of the deliverable. A reviewer who sees:

```
abc1234 Add .gitignore to exclude .env and __pycache__
d3e5678 Add README with project description and usage guide
f9a0123 Initialize repository with main.py scaffold
```

…understands your project's development story instantly. A reviewer who sees three commits all labeled "update" learns nothing. [1][3]

## 8. Best Practices

**Do:**

- Write the subject line as a command: "Fix", "Add", "Remove", "Update", "Rename".
- Keep the subject under 50 characters.
- Add a body when the reason for the change is not obvious from the subject alone.
- Commit one logical change at a time — one reason, one snapshot.
- Stage files selectively with `git add <filename>` rather than `git add .` when you have mixed work.
- Read your subject line back to yourself as: "If applied, this commit will \_\_\_\_." If it sounds right, it is right.

**Avoid:**

- Vague messages: "fix", "update", "stuff", "wip", "final", "changes". These tell future readers nothing. [1][3]
- Mixing unrelated changes: fixing a bug and adding a feature in the same commit. They belong in separate commits. [2]
- Ending the subject with a period.
- Writing a novel in the subject: if you need more than ~50 characters, put the extra detail in the body.
- Committing everything at once at the end of a session. Commit as you go, at logical stopping points.

**The "squint test":** Imagine reading your commit history six months from now. Can you understand the project's story from the subject lines alone? If yes, you have good commit discipline. If you have to open each commit to understand what it did, the messages need work. [1]

## 9. Hands-On Exercise

For your Assessment 4 Capstone repository, practice this workflow:

1. Create a new repository on GitHub (you learned this in topics 13.11 and 13.12).
2. Make your first commit with only a `README.md`. Message: "Add README with project overview".
3. Make a second commit adding only a `.gitignore`. Message: "Add .gitignore to exclude .env and __pycache__".
4. Make a third commit adding `requirements.txt`. Message: "Add requirements.txt with project dependencies".
5. Run `git log --oneline` and read your history. Each line should tell a clear, one-sentence story.

You now have at least three atomic commits with meaningful messages — satisfying the lab requirement and demonstrating the habit assessors will look for.

## 10. Key Takeaways

- An **atomic commit** holds exactly one logical change. The test: can you describe it in one sentence without "and"?
- A **commit message subject line** should be under 50 characters, start with an imperative verb (Add, Fix, Remove), and not end with a period.
- Add a **body** (separated by a blank line, wrapped at 72 characters) when the reason for the change is not obvious from the subject alone.
- **Avoid vague messages** ("update", "fix", "wip") — they destroy the value of your commit history.
- Good commit discipline makes your project history readable, your bugs easier to reverse, and your portfolio more professional.

## 11. Next Steps

_System-derived from the next entry in curriculum/sequence.md._
