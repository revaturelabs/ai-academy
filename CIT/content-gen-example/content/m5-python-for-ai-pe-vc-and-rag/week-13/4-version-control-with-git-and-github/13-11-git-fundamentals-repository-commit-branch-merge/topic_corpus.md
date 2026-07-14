---
topic_id: "13.11"
title: "Git fundamentals — repository, commit, branch, merge"
position_in_module: 2
generated_at: "2026-06-14T00:00:00Z"
resource_count: 3
---

# 1. Git fundamentals — repository, commit, branch, merge — Topic Corpus

## 2. Prerequisites

This topic builds directly on **13.10 — Why version control matters**. Topic 13.10 introduced the concept of a version control system as a tool that tracks changes to files over time. It covered version history, manual versioning, and the idea of distributed version control. Those concepts are assumed here. No other prior topics contribute vocabulary to this topic.

## 3. Learning Objectives

By the end of this topic, you will be able to:

- Explain what a Git repository is and describe what it contains.
- Describe what a commit is and explain why each commit should carry a clear commit message.
- Explain what a branch is and state why developers create separate branches instead of working directly on the main branch.
- Describe what merging does and identify when you would merge a branch.
- Trace the state of a simple project through the create-branch → commit → merge sequence.
- Distinguish between a repository, a commit, and a branch in your own words.

## 4. Introduction

In topic 13.10 you learned *why* version control matters: it keeps your working code safe and gives you a full history of every change. Now you need to learn *how* Git actually organises that history. Git uses four building blocks to do its job: the **repository**, the **commit**, the **branch**, and the **merge**.

Think of writing a novel. The folder on your desk that holds every draft page is like a repository. Every time you finish a chapter and staple it together, you are making a commit — a saved checkpoint of the whole manuscript at that moment. When your editor asks you to write an experimental alternate ending without touching the main story, you photocopy the manuscript and work on the copy — that is a branch. When the new ending is approved and you want to fold it back into the main story, you merge the copy back in.

Git follows exactly this pattern for your code. Each of the four concepts plays a specific role. You will use all four every time you work on a real project.

## 5. Core Concepts

### 5.1 Repository

**Repository** — the folder that Git uses to store all versions of your project. [1]

A repository (often shortened to "repo") contains two things:

1. **Your project files** — the Python scripts, text files, or any other files you are working on. This area is called the **working directory** — the place where you view and edit files normally.
2. **A hidden history database** — a special folder named `.git` that Git creates and manages automatically. You do not need to open or edit it. It holds every saved snapshot of your project since the repository was created.

When you run `git init` inside a folder, Git creates that `.git` folder and the folder becomes a repository. From that moment, Git can start tracking changes. [1]

**Key distinctions:**

| Term | What it means |
|---|---|
| Repository | The whole managed project folder, including history |
| Working directory | The part of the repository you can see and edit — your actual files |
| `.git` folder | The hidden database Git uses internally — leave it alone |

You work in the working directory. Git manages the `.git` folder for you.

> **Why does this matter?** Without a repository, Git has nowhere to store history. Every other concept in this topic — commits, branches, merges — only exists inside a repository.

### 5.2 Commit

**Commit** — a saved snapshot of every file in your project at a specific moment in time. [1]

Think of a commit the way you think of pressing "Save" in a document editor — except Git saves the complete state of all your files, not just the current one, and it keeps *every* save permanently. You can always go back to any earlier commit.

A commit carries three things:

- **A unique ID** — a long string of letters and numbers (called a hash) that identifies this exact snapshot. Git generates this automatically.
- **A commit message** — a short note *you* write that describes what changed and why.
- **A pointer to the previous commit** — so Git can show the full history as a connected chain.

**The commit message is important.** It is the human-readable label for this snapshot. A message like `"fixed it"` tells your future self nothing. A message like `"Add input validation to the user login function"` tells you exactly what changed and why. [1][2]

**Example of a poor vs. good commit message:**

| Quality | Example message |
|---|---|
| Poor | `"stuff"` |
| Poor | `"update"` |
| Good | `"Add chain-of-thought prompt to AI summary function"` |
| Good | `"Fix KeyError when API response is empty"` |

**How commits chain together.** Each new commit points back to the commit before it. This forms a timeline — Git calls it the **commit history** — the complete record of every save you have ever made. [1]

```
  commit A  →  commit B  →  commit C  →  (HEAD — most recent)
```

`HEAD` is Git's name for the commit you are currently on. It usually points to the latest commit.

> **One commit = one logical change.** The professional rule of thumb is: each commit should represent one coherent unit of work. You will practise this in the lab activity for this week.

### 5.3 Branch

**Branch** — a separate, independent line of development inside the same repository. [1][2]

When you create a repository, Git automatically creates one branch called **`main`** (or `master` on older systems). Think of `main` as the official, clean copy of your project.

A branch is like making a photocopy of your manuscript so you can experiment without touching the original. The important point: **the original does not change while you work on the copy.** You can make as many commits on the branch as you want. The `main` branch is completely unaffected until you decide to merge.

**Why create a branch instead of working directly on `main`?**

- You might break something while experimenting. A branch contains the breakage; `main` stays clean.
- You might want to try two different approaches to the same problem. Each gets its own branch.
- In a team, every developer works on their own branch so they do not overwrite each other's work. [1][2]

**Creating a branch.** When you create a branch, Git creates a new label that points to the current commit. New commits you make from this point go onto this branch only — `main` does not move. [1]

```
main:    A → B → C
                  ↘
feature:            D → E
```

In this diagram:

- Commits A, B, C are on `main`.
- You created a branch called `feature` after commit C.
- Commits D and E are on `feature` only. `main` still sits at C.

**Switching between branches.** You can switch back to `main` at any time. When you do, your working directory changes to show the files as they were at commit C. The D and E files are not lost — they are still on the `feature` branch, ready when you switch back. [1]

> **Branch = isolation.** A branch gives you a safe space to work. Nothing you do on a branch can damage `main` until you choose to merge.

### 5.4 Merge

**Merge** — the act of combining the commits from one branch into another branch. [1][2][3]

When your work on a branch is finished and tested, you merge it back into `main`. Git takes the commits from your branch and applies them to `main`, so `main` now contains all the changes.

```
main:    A → B → C ─────────────────→ F  (merge commit)
                  ↘                 ↗
feature:            D → E ──────────
```

After the merge, `main` contains the history of A, B, C, D, E, and the new merge point F. The feature branch still exists, but its work is now part of `main`. [1]

**What Git does during a merge.** Git looks at three things:

1. The common starting point — the commit where the branch was created (C in the diagram).
2. The changes on `main` since that point (none in this example).
3. The changes on the branch since that point (D and E).

Git combines them. In simple cases this happens automatically. [1][2]

**A "merge commit"** is a special commit Git creates to record the joining of two branches. It has two parent commits instead of one — one from each branch. [1]

> **What about conflicts?** If two branches changed the *same line* of the same file in different ways, Git cannot decide which version to keep. This is called a merge conflict. Resolving conflicts is a separate skill — you will encounter them as you practise Git further.

**The full cycle at a glance:**

| Step | What you do | Git action |
|---|---|---|
| 1 | Create a repository | Git initialises the `.git` folder |
| 2 | Edit files | You change files in the working directory |
| 3 | Commit the changes | Git saves a snapshot with your message |
| 4 | Create a branch | Git creates a new label pointing at the current commit |
| 5 | Make commits on the branch | Snapshot chain grows on the branch only |
| 6 | Merge the branch into main | Git combines the two histories |

## 6. Implementation

The four fundamental Git commands that map to these concepts are short and straightforward. [1][2][3]

**Step 1 — Create a repository.**

```
git init
```

Run this once inside your project folder. Git creates the `.git` folder and begins tracking. Your folder is now a repository.

**Step 2 — Stage and commit changes.**

```
git add .
git commit -m "Your commit message here"
```

- `git add .` tells Git which files to include in the next snapshot. The dot means "all changed files".
- `git commit -m "..."` saves the snapshot and attaches your message.

You run this pair of commands every time you want to save a checkpoint.

**Step 3 — Create and switch to a new branch.**

```
git branch feature-login
git checkout feature-login
```

Or, as a single shortcut:

```
git checkout -b feature-login
```

This creates a branch called `feature-login` and moves you onto it. Any commits you make now go on this branch only.

**Step 4 — Merge a branch into `main`.**

```
git checkout main
git merge feature-login
```

First switch back to `main`. Then run `merge` to bring in the branch commits. [1][2]

**Step 5 — Check your status and history.**

```
git status
git log --oneline
```

- `git status` shows which branch you are on and which files have changed since the last commit.
- `git log --oneline` shows the commit history as a compact list — one commit per line, ID and message.

> Note: Working with GitHub — clone, push, pull — is not covered here. You will cover that in the next topic.

## 7. Real-World Patterns

**Feature branches in AI projects.** When you are building an AI pipeline, you often experiment with different prompt templates or model parameters. A clean pattern is to create one branch per experiment:

- `main` holds the version that is working and tested.
- A branch named `experiment-few-shot` holds your few-shot prompting attempt.
- A branch named `experiment-chain-of-thought` holds your chain-of-thought version.

You commit progress on each branch. When one approach proves better, you merge it into `main`. The others remain as archived branches — you can always look back at what you tried. [2]

**Commit messages as a project diary.** In a real project, the commit history is the first place a new team member looks to understand what changed and why. Well-written commit messages mean the history is readable. Poor messages mean the history is noise. Professional teams treat a good commit message as a discipline, not optional housekeeping. [1]

**Capstone connection.** For Assessment 4 (Python and Prompt Engineering Portfolio, due this week), you will create a GitHub repository for your Capstone project. The repository, commit, branch, and merge concepts you are learning now are exactly what you will use. Each meaningful change to your Capstone code should become a commit with a clear message.

## 8. Best Practices

**Commit discipline.**

| Do | Don't |
|---|---|
| Commit one logical change at a time | Commit ten unrelated changes at once |
| Write a clear, specific commit message | Write `"fix"` or `"update"` |
| Commit working code | Avoid committing broken work to `main` — use branches for work-in-progress |

**Branch naming.**

- Use short, descriptive names: `add-validation`, `fix-api-error`, `experiment-rag-prompt`.
- Avoid spaces and special characters. Use hyphens to separate words.
- The name should say what the branch is *for*.

**When to merge.**

- Merge when the branch's goal is complete and the code on the branch works.
- Do not merge a broken branch into `main`. Test on the branch first.
- After merging, you can keep the branch or delete it. Deleting a merged branch is safe — its commits are now in `main`. [1][2]

**Frequency of commits.** Commit whenever you have completed a small, self-contained piece of work that you would not want to redo from scratch. [1]

## 9. Hands-On Exercise

This short exercise prepares you for the Capstone lab activity.

1. Create a new folder on your computer called `git-practice`.
2. Open a terminal, navigate to that folder, and run `git init`.
3. Create a file called `notes.txt` and write one sentence in it.
4. Run `git add .` then `git commit -m "Add initial notes file"`.
5. Create a branch called `experiment`: `git checkout -b experiment`.
6. Add a second sentence to `notes.txt`.
7. Commit the change with a descriptive message.
8. Switch back to `main`: `git checkout main`. Open `notes.txt` — notice it shows only the original sentence. The branch change is isolated.
9. Merge your experiment branch: `git merge experiment`. Open `notes.txt` again — it now has both sentences.
10. Run `git log --oneline` to see the full commit history.

## 10. Key Takeaways

- A **repository** is the folder Git manages. It contains your files (the working directory) and a hidden `.git` database that stores every saved snapshot.
- A **commit** is a permanent snapshot of all your files at a point in time. Every commit carries a message you write — that message is the human-readable record of what changed.
- A **branch** is a separate line of development inside the same repository. Creating a branch lets you experiment or build a new feature without touching the `main` branch.
- A **merge** combines the commits from one branch into another. After a merge, the target branch contains all the work from both lines of development.
- The standard cycle is: create a branch → make commits → merge back into `main`. This cycle keeps `main` clean and gives you a safe space to work.

## 11. Next Steps

_System-derived from the next entry in curriculum/sequence.md._
