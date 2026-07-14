---
topic_id: 13.12
title: "GitHub workflow — clone, add, commit, push"
position_in_module: 3
generated_at: 2026-06-15T00:00:00Z
resource_count: 3
---

# 1. GitHub Workflow — Clone, Add, Commit, Push — Topic Corpus

## 2. Prerequisites

This topic builds directly on:

- **13.10 — Why version control matters — never lose working code.** You should understand what a version control system is, why it exists, and what a change log is.
- **13.11 — Git fundamentals — repository, commit, branch, merge.** You should be comfortable with the terms: repository, working directory, commit, snapshot, commit message, commit history, HEAD, branch, and main branch.

## 3. Learning Objectives

By the end of this topic you will be able to:

- Explain the difference between a local repository and a remote repository on GitHub.
- Use `git clone` to copy a remote repository onto your own computer.
- Use `git add` to stage one or more changed files for inclusion in a commit.
- Use `git commit` to record a named snapshot of staged changes in your local repository.
- Use `git push` to upload your local commits to GitHub so others (and the grader) can see them.
- Trace the path a file change travels — from your editor, through staging, through committing, to GitHub — in the correct order.

## 4. Introduction

You now know that Git tracks changes and GitHub stores them in the cloud. But knowing *what* these tools are is not the same as knowing *how to use them*. In this topic you will learn the exact four-step sequence every developer uses to get their work from their own computer up onto GitHub: **clone, add, commit, push**.

Think of it like editing a shared document. You download a copy (clone), mark the paragraphs you changed (add), save a named version (commit), and upload the updated copy back to the server (push). After these four steps, your changes are visible to your instructor, your teammates, and anyone else with access to the repository.

This sequence matters right now because your Assessment A4 — the Python and Prompt Engineering Portfolio — requires a GitHub repository with a proper README, a `.gitignore` file, and at least three meaningful commits. Every step in this topic maps directly onto that deliverable. By the time you finish here, you will be able to create that repository and populate it yourself.

## 5. Core Concepts

### 5.1 Local repository vs. remote repository

In topic 13.11 you learned that a **repository** is a folder that Git watches. What you did not need to distinguish yet is *where* that folder lives.

A **local repository** is the repository that lives on *your* computer — your laptop, your desktop, or whatever machine you are working on. Only you can see it (until you share it). All your day-to-day work happens here: you edit files, run code, and make commits [1].

A **remote repository** is a copy of that same repository that lives on a server somewhere — in our case, on **GitHub** (github.com). GitHub (GitHub, Inc., owned by Microsoft) is a web platform that hosts Git repositories and makes them accessible over the internet. The remote is the "shared" or "published" version of your work [1][2].

The relationship is simple: your local repository and the remote repository are copies of each other. Git lets you send commits back and forth between them. The four commands in this topic — clone, add, commit, push — move your work from local to remote (and clone does the reverse, setting up the local copy from the remote).

> **Acronym note.** "Git" is the version control *tool* (runs on your computer). "GitHub" is the *website/service* that hosts Git repositories. They are related but different — you can use Git without GitHub, and GitHub hosts other things too. In this course we always use them together.

Why does having two copies matter? Because it gives you resilience and collaboration at the same time. If your laptop breaks, your work is still safe on GitHub. If a teammate wants to contribute, they clone the same remote and work in parallel. The separation between local and remote is not a complication — it is a feature.

### 5.2 `git clone` — copy a remote repository to your computer

**`git clone`** is the command you run when you want to download a remote repository from GitHub onto your local machine [1].

After you (or a teammate, or your instructor) create a repository on GitHub, it lives only on GitHub. To work on it locally, you run:

```bash
git clone <URL>
```

Where `<URL>` is the address of the GitHub repository. You can copy this URL from the green **Code** button on any GitHub repository page.

What clone does, step by step:
1. Creates a new folder on your computer with the same name as the repository.
2. Downloads all the files that are in the repository.
3. Downloads the full commit history (every snapshot ever saved).
4. Automatically tells your local repository, "the remote counterpart of this repo is at that URL." Git names that remote counterpart `origin` by default [2].

After cloning, you have a fully functional local repository. You can open the files, edit them, run Python scripts, and so on — just like a normal folder.

> **`origin`** is just a nickname Git gives to the remote repository you cloned from. It is not a special place; it is simply a label. When you later run `git push`, Git will look up what `origin` means and send your work there.

An important detail: you only clone once per project per machine. After that, your local folder is connected to the remote automatically — Git remembers the connection. If you switch to a different computer and want to work on the same project, you clone again on that machine.

### 5.3 `git add` — stage your changes

After you edit one or more files in your local repository, those changes exist only in your **working directory** (the normal file system, as introduced in 13.11). Git sees them but has not been told to include them in the next commit.

**`git add`** moves a changed file into a special waiting area called the **staging area** (also called the **index**). Think of the staging area as a loading dock. You pick which changes go on the truck (the commit) by placing them on the dock first [1][2].

```bash
git add <filename>        # stage one specific file
git add .                 # stage ALL changed files in the current folder
```

Why does staging exist? Because sometimes you have edited five files but only want to commit three of them together as one logical change. Staging lets you be precise about what goes into each commit [3].

Key mental model:

| Zone | What it means |
|---|---|
| Working directory | Files as they exist on your disk right now |
| Staging area | Changes you have told Git to include in the next commit |
| Commit history | Permanent snapshots that have already been committed |

After `git add`, your changes are "staged" but not yet saved as a snapshot. That is the next step.

Consider a concrete example. Imagine you have been working on your portfolio project and you edited three files: `README.md`, `analysis.py`, and a rough notes file called `scratch.txt`. You want to commit only the meaningful work — `README.md` and `analysis.py` — and leave `scratch.txt` alone. Using `git add README.md` followed by `git add analysis.py` puts exactly those two files on the dock. `scratch.txt` stays in your working directory and will not appear in the commit. This precision is one of the things that makes your commit history clean and readable over time [1][3].

### 5.4 `git commit` — save a snapshot

**`git commit`** takes everything in the staging area and saves it as a permanent snapshot in your local commit history [1][2].

```bash
git commit -m "Add README with project description"
```

The `-m` flag lets you write your **commit message** inline (in quotes). A commit message is a short description of what changed and why — you learned in 13.11 that these messages become your commit history, the record you can look back on later.

What happens when you run `git commit`:
- Git bundles all staged changes into one snapshot.
- It records who made the change (your name and email from your Git config), when, and the commit message you wrote.
- It generates a unique identifier for the commit — a long string of letters and numbers called a **commit hash** (sometimes called a **SHA**). The commit hash uniquely identifies that snapshot forever [2].
- HEAD (introduced in 13.11) moves forward to point at this new commit.

After committing, the staging area is empty again and your working directory is "clean" (nothing waiting to be staged or committed).

> **Commit hash (SHA):** Every commit gets an automatically generated ID like `a3f9b21c`. You rarely need to type it in full — Git can usually recognize the first 7 characters. The hash is how Git tracks which commit is which. You will see these on GitHub's commit history page.

The commit exists *only on your computer* at this point. Think of committing as pressing "Save" in a word processor, except Git saves the entire project state, not just one file. The change does not reach GitHub until you run the next command.

### 5.5 `git push` — upload your commits to GitHub

`git commit` saves your snapshot *locally*. The remote repository on GitHub does not know about it yet. **`git push`** sends your local commits to GitHub [1][2][3].

```bash
git push origin main
```

Breaking this down:
- `push` — send commits from local to remote.
- `origin` — the nickname for the remote repository (set automatically by `git clone`).
- `main` — the name of the branch you want to push. After completing topic 13.11 you know that `main` is the default primary branch [2].

After `git push` succeeds, you can open your repository on github.com, refresh the page, and see your new files and commits listed there.

You may push multiple commits at once. If you made three commits locally before running `git push`, all three arrive on GitHub in one push. GitHub stores them individually with their original messages and timestamps — your full history arrives intact [1][2].

### 5.6 The full workflow — how the four steps connect

These four commands are always used in the same order. Here is the mental picture [1]:

```
GitHub (remote)
      |
      |  git clone  (one-time setup)
      v
Local repository  <----  your working directory
                               |
                          git add
                               |
                         (staging area)
                               |
                          git commit
      |
      |  git push
      v
GitHub (remote)  <-- your changes are now here
```

1. **Clone** — bring the repo from GitHub to your machine (done once per project).
2. **Edit** — make changes to files in your working directory.
3. **Add** — stage the changes you want to commit.
4. **Commit** — save a snapshot locally with a message.
5. **Push** — send the snapshot to GitHub.

Steps 2 through 5 repeat every time you have a meaningful unit of work to save. Step 1 is done only once (when you first set up the project on a new machine).

## 6. Implementation

The following steps walk you through the complete workflow from a fresh GitHub repository to a pushed commit. You will do exactly this sequence for Assessment A4 [1].

### Step 1 — Create a repository on GitHub (one-time setup)

1. Log in to github.com.
2. Click the **+** icon (top right) and select **New repository**.
3. Give the repository a name (e.g., `my-ai-portfolio`).
4. Check **Add a README file** (this gives you something to clone right away).
5. Click **Create repository**.

You now have a remote repository on GitHub with one file (`README.md`) and one commit.

### Step 2 — Clone the repository to your computer

1. On your new GitHub repository page, click the green **Code** button.
2. Copy the HTTPS (HyperText Transfer Protocol Secure) URL — it looks like `https://github.com/your-username/my-ai-portfolio.git`. HTTPS is the standard secure way browsers and tools like Git transfer data over the internet; the URL you copy from GitHub uses it by default.
3. Open a terminal (or VS Code's integrated terminal).
4. Navigate to the folder where you want the project to live, e.g.:
   ```bash
   cd Documents
   ```
5. Run clone:
   ```bash
   git clone https://github.com/your-username/my-ai-portfolio.git
   ```
6. A new folder named `my-ai-portfolio` appears. Move into it:
   ```bash
   cd my-ai-portfolio
   ```

You are now inside your local repository.

### Step 3 — Make a change

1. Open `README.md` in any text editor or VS Code.
2. Add a line, for example:
   ```
   ## About
   This repository contains my Python and Prompt Engineering work.
   ```
3. Save the file.

### Step 4 — Stage the change with `git add`

```bash
git add README.md
```

Or, to stage everything you changed:
```bash
git add .
```

You can run `git status` at any time to see which files are staged — you'll use this more as you build your git habits.

### Step 5 — Commit the change with `git commit`

```bash
git commit -m "Update README with project description"
```

Git prints a short confirmation, for example:
```
[main 4c2a1b3] Update README with project description
 1 file changed, 3 insertions(+)
```

The code in brackets (`4c2a1b3`) is the beginning of your commit hash.

### Step 6 — Push to GitHub with `git push`

```bash
git push origin main
```

Git may ask for your GitHub username and a personal access token (PAT). A personal access token is a password alternative generated in your GitHub settings — you use it instead of your account password when pushing from the command line. GitHub stopped accepting your regular account password for git operations in 2021; a PAT is the secure replacement you create once in your GitHub account settings and paste when prompted [2][3].

After the push completes, the terminal shows something like:

```
To https://github.com/your-username/my-ai-portfolio.git
   a1b2c3d..4c2a1b3  main -> main
```

### Step 7 — Confirm on GitHub

Open your repository on github.com. Click on `README.md`. You will see your new lines. Click on **Commits** (usually shown as "2 commits" near the top of the file listing). You will see both commits: the original "Initial commit" and your new one.

You have completed the full clone to add to commit to push cycle.

### Step 8 — Repeating the cycle

Every time you want to save more work to GitHub, you only repeat steps 3 through 6 (edit, add, commit, push). You do not clone again — the local repository already exists and knows where `origin` is.

## 7. Real-World Patterns

### How teams use this workflow daily

The clone, add, commit, push cycle is the foundation of professional software development. Every developer on every project runs these commands, typically multiple times per day [3].

A typical working session looks like this:
- Open the terminal, navigate to the project folder.
- Edit one or two files to implement a small feature or fix.
- Run `git add` on the changed files.
- Run `git commit -m "Fix typo in error message"` or `git commit -m "Add input validation to login form"`.
- Run `git push origin main`.

Over a week this produces a clean, readable commit history that tells the story of the project: what changed, who changed it, and why [2].

### Why instructors and employers look at your commit history

When your instructor grades your portfolio (A4), they will open your GitHub repository and read your commit history. Three things they check:

1. **Are there at least three commits?** A single "dump everything" commit suggests the work was not tracked progressively.
2. **Are the commit messages meaningful?** Messages like "update" or "stuff" are a red flag. Messages like "Add .gitignore to exclude API key" tell the story clearly.
3. **Does the repository contain a README and .gitignore?** These are the professional minimum for any shared project.

The same scrutiny applies in job interviews: hiring managers routinely look at a candidate's GitHub profile to understand how they work, not just what they built [3].

### Keeping secrets out of GitHub

You will also create a `.gitignore` file to keep secrets out of GitHub — that is covered in topic 13.14.

## 8. Best Practices

### Commit often — use small, logical units

Do not wait until a feature is "completely done" to commit. Commit every time you complete a small, self-contained piece of work. This makes it easy to undo a mistake: instead of losing hours of work, you can return to the last commit that worked [1].

Commit after each of the following natural stopping points:
- You add a new function and it works.
- You fix a bug.
- You write or update a README section.
- You add a new file to the project.

Small, frequent commits also make your history readable. A history of twenty focused commits is far more useful than two giant ones when you need to find out when and why something changed [2].

### Always pull before you push when collaborating

When you are working with teammates on the same repository, someone else may have pushed commits to GitHub while you were working locally. If you try to push without incorporating their changes first, Git will refuse and ask you to reconcile. The habit is simple: before you start a new round of edits, run `git pull origin main` to bring any remote changes into your local copy first [3].

Even when working solo, forming the pull-first habit prepares you for team environments from day one.

### Write a meaningful commit message every time

Convention in most teams: commit messages start with a capital verb in the imperative mood.

| Good | Avoid |
|---|---|
| `Add README with project overview` | `added readme` |
| `Fix import error in main.py` | `fixed stuff` |
| `Remove API key from config file` | `update` |

A good commit message answers two questions in one line: *what* changed, and *why* (when the why is not obvious). Your future self (and your grader) will thank you [2][3].

### Do not commit large binary files or secrets

- Large binary files (video, audio, trained model weights) slow down the repository and are difficult to undo.
- Secrets (API keys, passwords) pushed to a public GitHub repository are publicly visible immediately. Use a `.gitignore` file (covered in topic 13.14) to prevent this [3].

### Never force-push without understanding what it does

A command exists called `git push --force` that can overwrite the remote history. As a beginner you should never need it. If you find yourself looking up how to force push, stop and ask your instructor what went wrong — there is almost always a safer fix.

## 9. Hands-On Exercise

Before your next session:

1. Create a new GitHub repository named `ai-portfolio` (check "Add a README file").
2. Clone it to your computer using `git clone`.
3. Add a line to `README.md` describing your project in one sentence. Save the file.
4. Stage it with `git add README.md`, commit with a meaningful message (`git commit -m "Add one-line project description"`), and push with `git push origin main`.
5. Open the repository on GitHub and confirm your commit appears in the commit history.

This is exactly the first commit required for A4. Doing it now means you have one of the three required commits complete.

## 10. Key Takeaways

- **Clone copies a GitHub repository to your computer.** You run it once per project to create your local repository from the remote one.
- **Add stages the files you want in your next commit.** Only staged changes become part of the snapshot — unstaged edits are left out.
- **Commit creates a permanent, named snapshot in your local history.** It does not touch GitHub; the commit lives only on your machine until you push.
- **Push sends your local commits to GitHub.** After a successful push, your changes are visible on github.com and to anyone who has access to the repository.
- **The cycle is edit, add, commit, push — repeated.** Clone is the one-time setup; the rest forms the loop you will use every single working session.

## 11. Next Steps

_System-derived from the next entry in curriculum/sequence.md._
