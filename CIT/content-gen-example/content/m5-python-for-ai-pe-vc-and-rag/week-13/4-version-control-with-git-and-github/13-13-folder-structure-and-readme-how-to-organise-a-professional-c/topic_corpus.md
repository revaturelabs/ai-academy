---
topic_id: "13.13"
title: "Folder structure and README — how to organise a professional codebase"
position_in_module: 4
generated_at: "2026-06-15T00:00:00Z"
resource_count: 3
---

# 1. Folder structure and README — how to organise a professional codebase — Topic Corpus

## 2. Prerequisites

This topic builds directly on the three preceding topics in module 4:

- **13.10** — Why version control matters (version control system, version history, working code safety)
- **13.11** — Git fundamentals (repository, commit, branch, main branch, commit history)
- **13.12** — GitHub workflow — clone, add, commit, push (local repository, remote repository, staging area, git add, git commit, git push, git clone, origin)

## 3. Learning Objectives

By the end of this topic, you will be able to:

- Describe the standard folder layout used in a professional Python project and explain why each part exists.
- Explain the purpose of a `README` file and write one using the five-section template.
- Explain what a `.gitignore` file does and why it must contain API (Application Programming Interface) key files before any commit is made.
- Create a minimal but complete project folder structure for a Python script or Capstone project.
- Identify the most common folder-organisation mistakes and describe the correct alternatives.
- Connect folder organisation and README quality to professional presentation of a portfolio repository.

## 4. Introduction

Think about the last time you walked into a well-organised kitchen. Everything has a place. Pots go in one cupboard. Spices go in a rack. Knives go in the knife block. You can find what you need in seconds, even if it is not your kitchen. Now imagine a kitchen where everything is piled on one counter — pots, spices, cleaning products, and raw food all mixed together. You would spend more time searching than cooking.

A software project is exactly the same problem. Your Python script is the meal you are cooking. Every supporting file — your data, your configuration, your notes — is an ingredient or a tool. If they are all piled in one folder with no organisation, you (and anyone else looking at your project) spend more time searching than building.

Professional developers solve this by following a standard folder layout. That layout is not a rigid rule imposed by a governing body. It is a shared convention — an agreement across the Python community about where things should live — so that any developer can open any project and immediately know where to look. [1]

This topic is the last in module 4. You have already learned why version control exists (topic 13.10), how Git tracks changes (topic 13.11), and how to push code to GitHub (topic 13.12). This topic adds the final layer: how to organise what you push so that it looks and behaves like professional work.

This matters urgently right now. Assessment A4 — your Python and Prompt Engineering Portfolio — is due this week. A reviewer will open your GitHub repository. The first things they see are your folder layout and your `README`. Those two elements communicate your level of care and professionalism before they read a single line of Python. This topic gives you a concrete checklist so your repository makes the right first impression. [2]

## 5. Core Concepts

### 5.1 What is a project folder structure?

A **folder structure** — also called a project layout or directory structure — is the arrangement of files and folders (also called directories) inside your project. [1]

Every file you create belongs to a category. Some files contain Python code. Some contain data. Some contain configuration. Some contain documentation. A folder structure places each category in its own dedicated folder so that related files are always together and unrelated files are always separated.

Here is an example of a disorganised project — everything in one flat folder:

```
my_project/
    script.py
    data.csv
    notes.txt
    output.csv
    config.txt
    api_key.txt
    old_script.py
    old_script_v2.py
    final_script.py
    test.py
    IGNORE THIS.py
```

This is the default state for many beginner projects. It works in the sense that Python can run the scripts. But it has several serious problems:

- A reviewer opening this folder cannot tell what the main script is.
- Files named `old_script.py` and `final_script.py` mean the author was using filenames instead of Git commits to track versions — the exact problem topic 13.10 introduced version control to solve.
- A file called `api_key.txt` in plain sight will be committed and pushed to GitHub unless something explicitly prevents it.
- There is no document explaining what the project does or how to run it.

A well-organised project fixes every one of these problems. [1]

### 5.2 The standard Python project layout

The Hitchhiker's Guide to Python — one of the most widely cited references in the Python community — describes a project layout that professional teams across the industry follow. [1] Here is the standard structure, annotated to explain each part:

```
my_project/               <- root folder — same name as your GitHub repository
├── README.md             <- the front page: describes what the project is and how to use it
├── .gitignore            <- tells Git which files to skip (never push to GitHub)
├── requirements.txt      <- lists the Python packages this project depends on
├── src/                  <- source folder: all Python code lives here
│   └── main.py           <- your main script (entry point)
├── data/                 <- data folder: CSV files, JSON files, any input/output data
├── tests/                <- test folder: scripts that verify your code works (covered in later courses)
└── docs/                 <- documentation folder: optional for small projects
```

Take each part in turn.

**The root folder** is the outermost container. Its name is also the name you give the repository on GitHub. Using the same name in both places avoids confusion. [1]

**`README.md`** lives at the top level of the root folder — not inside any subfolder. GitHub displays this file as the formatted homepage of your repository. Every visitor sees it first.

**`.gitignore`** also lives at the top level. It is a hidden file on most systems (the leading dot signals "hidden" on Linux and macOS). Git reads this file before deciding which files to track. Files and folders listed here are invisible to `git add` and `git push`. [1]

**`requirements.txt`** lives at the top level. It is a plain list of Python packages. Anyone who clones your repository runs one command to install them all.

**`src/`** (short for "source") is the folder where your Python code lives. Keeping code in its own folder separates it from data, documentation, and configuration. [2]

**`data/`** is where you keep files that your scripts read from or write to — for example, a CSV (Comma-Separated Values) file of prompts, or a JSON (JavaScript Object Notation) file of API responses.

**`tests/`** contains scripts that verify your code produces correct results. You will explore testing in later courses. For your Capstone, you can include this folder as empty or with a placeholder file, or omit it entirely. [3]

**`docs/`** is for extended documentation — long explanations, diagrams, user guides. For a small Capstone project it is optional.

**You do not need every folder from the start.** A minimal Capstone might look like this:

```
capstone-ai-tool/
├── README.md
├── .gitignore
├── requirements.txt
└── src/
    └── main.py
```

Add `data/` when you have data files. Add `tests/` if you write test scripts. Start with what you need; grow the structure as the project grows. [2]

### 5.3 What is a README file?

A **README** is a plain-text file, always named `README.md`, that sits at the very top level of your project folder. [1]

The `.md` file extension stands for **Markdown**. Markdown is a lightweight formatting language — a way to write structured text using simple symbols. A line starting with `#` becomes a large heading. A line starting with `##` becomes a smaller heading. A line starting with `-` becomes a bullet point. Text wrapped in backticks (\`) renders as code. You do not need to learn all of Markdown for this topic. The symbols you need for a professional README are just `#`, `##`, `-`, and backticks.

GitHub automatically detects any file named `README.md` in the root folder of a repository and renders it as the formatted homepage of that repository. This means your README is the first thing every visitor sees. [1]

**What a README must answer**

A README answers one central question: *What is this project and how do I use it?*

Every professional README answers this with five sections:

1. **Project title and description.** One or two sentences stating what the project does. Be specific. "A Python script" is not a description. "A Python script that sends a list of test prompts to the OpenAI API and saves the responses to a CSV file" is a description.

2. **Installation / Setup.** The exact steps a new person needs to take to run the project on their machine. This typically includes cloning the repository, installing packages, and setting up any environment variables (you will see what this means in section 5.4).

3. **Usage.** How to run the main script. Include the exact command, for example `python src/main.py`. If the script accepts arguments or needs a specific file in the `data/` folder, say so here.

4. **File structure.** A brief list of the main files and folders and what each one does. This helps the reviewer understand the layout at a glance without exploring every folder.

5. **Author and licence.** Your name, your cohort or organisation, and — optionally — the licence under which others may use your code. For a learning project, "All rights reserved" or no licence statement is fine.

**A worked example for a Capstone project**

```markdown
# AI Prompt Tester

A Python script that reads a list of prompts from a CSV file, sends each one
to the OpenAI API, and writes the responses back to a new CSV file.

### Setup

1. Clone this repository.
2. Install dependencies:

       pip install -r requirements.txt

3. Create a `.env` file in the root folder and add your API key:

       OPENAI_API_KEY=sk-your-key-here

### Usage

Run the main script from the project root:

    python src/main.py

The output file `data/responses.csv` is created automatically.

### File Structure

    capstone-ai-tool/
    ├── README.md             this file
    ├── .gitignore            files Git ignores (including .env)
    ├── requirements.txt      Python dependencies
    └── src/
        └── main.py           main script

### Author

Your Name — Revature CIT Cohort 2026
```

This README is concise, complete, and professional. A reviewer can read it in under two minutes and know exactly what the project does, how to set it up, and how to run it. [2]

**Common README mistakes to avoid**

- Leaving the README as a placeholder with only the repository name.
- Writing "This project does stuff with AI" — vague descriptions signal a project the author does not understand.
- Forgetting the Setup section — a reviewer who cannot run your code cannot evaluate it.
- Never updating the README after adding features — a README that describes a different project than the one in the repository is worse than no README.

### 5.4 What is a `.gitignore` file?

A **`.gitignore` file** is a plain-text configuration file that lives in the root folder of your project. It contains a list of file names and patterns. Git reads this file and treats every matching file or folder as if it does not exist — Git will never stage it, never commit it, and never push it to GitHub. [1]

**Why does this exist?**

When you run `git add .` (the `.` means "everything in this folder and all subfolders"), Git would normally stage every file it finds. But not every file should go to GitHub. Three categories of files should almost always be excluded:

1. **Secret credentials** — API keys, passwords, database connection strings. These are private. Publishing them on GitHub exposes them to the entire internet.

2. **Generated files** — Python creates `.pyc` files (compiled versions of your `.py` files) automatically. These are large, numerous, and machine-specific. They add noise to your repository without adding value.

3. **Virtual environments** — When you create a virtual environment (a folder, usually called `venv/`, that contains an isolated copy of Python and your installed packages), that folder can contain hundreds of megabytes of files. Committing it would make your repository enormous, and it would not even work on another machine because paths are hard-coded to your machine.

**API keys — the most critical case**

An **API key** is a secret string that identifies you to an external service. When your Python script calls an AI service's API (Application Programming Interface), it sends the API key with every request. The service uses it to confirm who you are, to track your usage, and — for paid services — to bill you.

API keys work like passwords. You would not write your password in a file and put it on a public website. An API key must receive the same protection.

If you commit an API key to a public GitHub repository, two things happen almost immediately:

1. GitHub's automated security scanning detects patterns that look like API keys and notifies the service provider.
2. Automated bots that scrape GitHub for credentials find the key and attempt to use it.

Many services revoke (disable) a key the moment it appears in a public repository. You then have to generate a new key, update your code, and investigate whether the key was used without your permission. This process is time-consuming and sometimes costly. Prevention is a single line in `.gitignore`. [1]

**The safe pattern for API keys**

Step 1 — Store the key in a file. The conventional name is `.env` (pronounced "dot env"). The file format is one variable per line:

```
OPENAI_API_KEY=sk-your-actual-key-here
```

Step 2 — Add `.env` to your `.gitignore` before your first `git add`. Open `.gitignore` and add the line `.env`. This is the critical order: `.gitignore` must be in place before any `git add` touches the project.

Step 3 — In your Python script, load the key from the `.env` file at runtime using a library called `python-dotenv`. The library reads the file and makes the values available through Python's standard `os` module:

```python
import os
from dotenv import load_dotenv

load_dotenv()                              # reads .env and loads its values
api_key = os.getenv("OPENAI_API_KEY")     # retrieves the key by name
```

Your Python file never contains the key itself. The key lives only in `.env`, which Git never sees. [1]

**What a `.gitignore` looks like**

Here is a practical `.gitignore` for a Python Capstone project, with comments explaining each section:

```gitignore
# ── Secret credentials ──────────────────────────────────────────
.env
secrets.env
*.key
api_key.txt

# ── Python generated files ──────────────────────────────────────
__pycache__/
*.py[cod]
*.pyo

# ── Virtual environment ─────────────────────────────────────────
venv/
env/
.venv/

# ── Operating system clutter ────────────────────────────────────
.DS_Store
Thumbs.db
```

Lines that begin with `#` are comments — Git ignores them. They are for human readers only.

`__pycache__/` is a folder Python creates automatically. The trailing `/` tells Git to ignore the entire folder and everything inside it.

`*.py[cod]` is a pattern. The `*` means "any filename". `.py[cod]` means "ending in `.pyc`, `.pyo`, or `.pyd`". Square brackets in a pattern mean "any one of these characters".

**A ready-made `.gitignore` for Python** is available in GitHub's official gitignore repository at `github.com/github/gitignore` — the file called `Python.gitignore`. It covers far more edge cases than the minimal example above. For a Capstone project, the minimal version is sufficient.

**Critical ordering rule:** Create `.gitignore` in your project folder before you run `git init` or before your first `git add`. If you add `.env` to `.gitignore` after it has already been committed, the file is still in Git's history. Anyone who has cloned the repository can retrieve earlier commits and read the key. Git has commands to rewrite history and remove a committed file, but they are complex and not always effective. Prevention by correct ordering is the only reliable protection. [1]

### 5.5 The `requirements.txt` file

A **`requirements.txt`** file is a plain-text list of Python packages (also called libraries or dependencies) that your project needs in order to run. [1]

When you install a package with `pip install openai`, the package is installed into your Python environment on your computer. It is not stored inside your project folder (unless you have a virtual environment, which `.gitignore` excludes). When someone else clones your repository, they get your code but none of your installed packages. Without a `requirements.txt`, they have to guess which packages to install — and they will get errors until they guess correctly.

The `requirements.txt` file solves this by recording the exact list. A new user runs one command:

```
pip install -r requirements.txt
```

The `-r` flag tells `pip` (Python's package installer, short for "pip installs packages") to read the list from a file and install everything on it. This is a universally understood convention. Any Python developer who sees a `requirements.txt` in a repository knows exactly what to do with it. [2]

**Creating a `requirements.txt` by hand**

For a small project, write the file yourself. List one package name per line:

```
openai
python-dotenv
requests
```

This is the simplest form. It installs the latest available version of each package.

**Creating a `requirements.txt` automatically**

If you have been installing packages as you built your project and want to capture the current state of your environment, run:

```
pip freeze > requirements.txt
```

`pip freeze` lists every installed package along with its exact version number, for example:

```
openai==1.30.1
python-dotenv==1.0.1
requests==2.31.0
```

The `>` symbol redirects that output into the file instead of printing it on screen. [2]

The version-pinned format (`package==version`) ensures anyone installing from this file gets exactly the same version you used, which prevents subtle bugs caused by version differences. For a Capstone project at this stage, either format (with or without version numbers) is acceptable.

**Where `requirements.txt` fits in the layout**

`requirements.txt` lives in the root folder alongside `README.md` and `.gitignore`. It is not inside `src/` or any subfolder. When someone clones your repository and navigates to the root folder, all three of these essential files are immediately visible. [1][2]

### 5.6 Naming conventions for files and folders

File and folder names are part of the professional presentation of your project. The Python community has settled on a small set of conventions. [1][3]

**Use lowercase letters.** Folder names like `Source Code/` or `My Data/` look informal and cause problems on Linux-based servers (where `Main.py` and `main.py` are two different files). Use `src/` and `data/`.

**Use hyphens or underscores, not spaces.** Spaces in file or folder names cause issues at the command line. A path like `my project/main.py` must be written as `"my project/main.py"` or `my\ project/main.py` in a terminal. Hyphens are conventional for folder names (`capstone-ai-tool/`). Underscores are conventional for Python file names (`main_script.py`). Either works; pick one and be consistent.

**Use meaningful names.** A file called `script.py` says nothing. A file called `prompt_tester.py` says exactly what it does. A folder called `stuff/` is not a folder; it is a sign that the project is not organised.

**Do not use version suffixes in file names.** Files named `final.py`, `final_v2.py`, `final_ACTUALLY_FINAL.py` mean the author was using filenames to track versions instead of Git commits. This is exactly the manual versioning anti-pattern that topic 13.10 described. Use meaningful commit messages instead. [1]

## 6. Implementation

This section walks you through building a professional project structure for your Capstone from scratch. Follow these steps in order.

**Step 1 — Create the root folder.**

Choose a short, descriptive name for your project. Use lowercase letters and hyphens. Create the folder. On the command line:

```
mkdir capstone-ai-tool
cd capstone-ai-tool
```

Or use your operating system's file explorer. The folder name you choose here will become the name of your GitHub repository.

**Step 2 — Create `.gitignore` immediately.**

Before you create any other file — especially before any file that will contain an API key — create `.gitignore`. This ordering is mandatory. [1]

Create a file called exactly `.gitignore` (with a leading dot and no extension). Add the minimum required content:

```
# Credentials — never commit
.env
secrets.env
*.key

# Python generated files
__pycache__/
*.py[cod]

# Virtual environment
venv/
env/
.venv/

# OS files
.DS_Store
Thumbs.db
```

Save the file. It now lives in the root folder.

**Step 3 — Create the `.env` file for your API key.**

Create a file called `.env` in the root folder. Add your API key:

```
OPENAI_API_KEY=sk-your-actual-key-here
```

Open your `.gitignore` file and confirm `.env` is listed. If it is not, add it now.

Verify Git will ignore it. If you have already run `git init`, run `git status` in the terminal. The `.env` file should NOT appear in the list of files Git wants to track. If it appears as "Untracked files: .env", that is normal — "untracked" and "ignored" are different statuses in Git. Actually, once a file is in `.gitignore`, it will not show in `git status` at all. If `.env` does appear, check that your `.gitignore` has the correct content.

**Step 4 — Create the subfolder structure.**

Create the folders you need:

```
mkdir src
mkdir data
```

Inside `src/`, create your main Python script:

```
src/main.py
```

For now it can be an empty file or a placeholder comment.

**Step 5 — Write the Python script to load the API key safely.**

In `src/main.py`, load the API key from `.env` using `python-dotenv`:

```python
import os
from dotenv import load_dotenv

load_dotenv()   # reads .env from the current working directory
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    print("Error: OPENAI_API_KEY not found. Check your .env file.")
else:
    print("API key loaded successfully.")
    # your prompt-sending code goes here
```

The key is never written in `main.py`. If someone reads your Python source file — on GitHub or anywhere else — they see only `os.getenv("OPENAI_API_KEY")`, not the actual key value. [1]

**Step 6 — Create `requirements.txt`.**

List the packages your project uses:

```
openai
python-dotenv
```

Save as `requirements.txt` in the root folder. If you have already installed your packages and want to capture exact versions, run `pip freeze > requirements.txt` instead.

**Step 7 — Write `README.md`.**

Create `README.md` in the root folder. Use the five-section template from section 5.3. Write:

- **Title and description** — the name of your project and one or two sentences explaining what it does.
- **Setup** — how to install dependencies and set up the `.env` file.
- **Usage** — the exact command to run your script.
- **File structure** — a brief listing of the main files.
- **Author** — your name and cohort.

Take your time on this section. It is the face of your project.

**Step 8 — Initialise Git and make the first commit.**

From the root folder of your project:

```
git init
git status
```

`git status` shows you what Git sees. Check that `.env` does NOT appear in the list. You should see `README.md`, `.gitignore`, `requirements.txt`, and `src/main.py` listed as untracked files — ready to be added. You should NOT see `.env`.

If `.env` does appear, stop. Do not run `git add`. Fix your `.gitignore` first.

When `git status` looks correct, stage and commit:

```
git add .
git commit -m "Initial commit: project structure, README, .gitignore"
```

This first commit establishes the baseline. From here, every change you make gets its own commit with a meaningful message describing what changed. [1]

**Step 9 — Push to GitHub.**

Create a new repository on GitHub. Give it the same name as your local root folder (`capstone-ai-tool`). Do not initialise it with any files — create it completely empty.

Then connect your local repository to GitHub and push:

```
git remote add origin https://github.com/your-username/capstone-ai-tool.git
git push -u origin main
```

Open your repository on GitHub. You should see:

- Your folder structure displayed as a file tree.
- Your `README.md` rendered as a formatted page below the file tree.
- No `.env` file anywhere in the repository.

If all three conditions are true, your project is professionally presented and your API key is safe. [1]

## 7. Real-World Patterns

### Pattern 1 — The portfolio repository

Professional Python developers keep their projects in public GitHub repositories. Hiring managers and technical interviewers routinely look at a candidate's GitHub profile before or during an interview. A repository with a clear, navigable folder structure and a polished README demonstrates professionalism regardless of the project's complexity. [2]

For most candidates at the start of their careers, the code in their portfolio is similar in complexity. What differentiates candidates is how that code is organised and documented. A recruiter or reviewer who can understand your project in 90 seconds without asking you a single question is a reviewer who forms a positive impression of your work.

Your Capstone repository is your first real portfolio entry. Treat it accordingly.

### Pattern 2 — The exposed API key incident

Exposed API keys are one of the most common security incidents in software development, and they are almost entirely preventable. [1]

GitHub and other code-hosting platforms run automated scanners that continuously scan every public commit for patterns that look like API keys, passwords, and credentials. These scanners operate at the moment of push — within seconds of your `git push`, the scan is running.

Many service providers (including major AI API providers) are notified immediately when their key format is detected in a public repository. Their automated response is to revoke the key — permanently deactivate it. The developer whose key was exposed must:

1. Generate a new key.
2. Update their code to use the new key.
3. Audit API usage logs to check whether anyone used the key while it was exposed.
4. If the service is paid, check the billing statements for unexpected charges.

This process takes time and creates stress. The entire incident is prevented by one line in `.gitignore` and correct ordering (`.gitignore` before first commit).

A corollary: do not assume your repository is safe because it is private. Private repositories can become public, organisations sometimes change their privacy settings, and repository access can be misconfigured. Treat API key protection as non-negotiable regardless of repository visibility. [1]

### Pattern 3 — The `requirements.txt` as a collaboration contract

In teams, the `requirements.txt` file is an implicit contract: "if you install everything in this file, the code will run". [2][3]

Without this contract, a new team member cloning a repository must read through the source files looking for `import` statements, guess which packages to install, install them, encounter errors because they guessed wrong, search the error messages for the right package names, and repeat. This process can take hours for a complex project.

With a correct `requirements.txt`, the entire process takes one command and under a minute.

The `requirements.txt` pattern is so fundamental that more advanced project management tools (such as `pyproject.toml`, which you will encounter in later courses) exist partly to improve on it. But for any project at this stage, a `requirements.txt` is all you need.

### Pattern 4 — README as living documentation

A README that accurately describes the project at launch and is never updated afterwards quickly becomes misleading. New features, changed setup steps, renamed files — any of these make the README partially false. A false README is worse than no README, because it wastes the reviewer's time when the instructions do not work.

Professional teams treat the README as a living document. It is updated in the same commit as the code change that makes the old README wrong. For your Capstone, updating the README when you add a feature or change how the script is run is exactly what "meaningful commits" means: code change + documentation change together, in one commit, with a message that describes both. [3]

### Pattern 5 — The standard layout as a communication tool

When a developer opens a repository and sees `src/`, `data/`, `requirements.txt`, `README.md`, and `.gitignore` at the top level, they know the project before they read a single file. They know where the code is, where the data is, how to install dependencies, and that the author has thought about what should and should not be committed. [1]

When a developer opens a repository and sees `script.py`, `data.csv`, `temp.py`, `test2.py`, and `notes.txt` in a flat pile, they know nothing except that the project will take time to understand. The layout itself communicates competence.

## 8. Best Practices

### Do

- Create `.gitignore` as the very first file in your project, before anything else.
- Add `.env` (and any other secrets file) to `.gitignore` before you create those files.
- Run `git status` before every `git add .` to verify no secrets are staged.
- Name your root folder the same as your GitHub repository name.
- Use lowercase letters and hyphens for folder names (`my-project`, not `My Project`).
- Write a README with all five sections before the project is considered complete.
- Update the README in the same commit as any change that makes the old README incorrect.
- Use `requirements.txt` so anyone can replicate your environment.

### Don't

- Don't put all files in the root folder with no subfolders — separate code, data, and configuration.
- Don't name files `final.py`, `final_v2.py`, or `FINAL_FINAL.py` — that is what commit history is for.
- Don't hardcode an API key in a `.py` file, not even in a comment — use `.env` and `os.getenv()`.
- Don't leave the README as a default template with only the project name and nothing else.
- Don't commit the `venv/` or `env/` folder — it is large, machine-specific, and belongs in `.gitignore`.
- Don't run `git add .` before verifying `.gitignore` is correct.
- Don't create `.gitignore` after your first commit — the `.env` file will already be in Git's history.

### Summary comparison table

| Situation | Correct approach | Common mistake |
|---|---|---|
| Storing an API key | `.env` file, listed in `.gitignore` | Pasted into `main.py` |
| Organising Python code | `src/main.py` | All files in root folder |
| Describing the project | `README.md` with 5 sections | No README or empty README |
| Recording dependencies | `requirements.txt` | Nothing — reviewer guesses |
| Tracking version changes | Git commits with messages | `final.py`, `final_v2.py` |
| Virtual environment | In `.gitignore`, not committed | Committed and pushed |

## 9. Hands-On Exercise

This exercise produces your Capstone repository for A4 submission. Work through it step by step.

1. Create a root folder with your project name (lowercase, hyphens). Open a terminal inside it.
2. Create `.gitignore` first. Add at minimum: `.env`, `venv/`, `__pycache__/`, `*.py[cod]`.
3. Create the subfolder `src/`. Inside it, create `main.py` with a placeholder comment.
4. Create `.env` and add one line: `OPENAI_API_KEY=sk-your-key-here`.
5. Create `requirements.txt` and list at minimum `openai` and `python-dotenv`.
6. Write `README.md` with all five sections: title/description, setup, usage, file structure, author.
7. Run `git init`, then `git status`. Verify that `.env` does not appear as a file Git wants to track.
8. Run `git add .` and `git commit -m "Initial commit: project structure"`.
9. Create an empty repository on GitHub with the same name. Add the remote and push.
10. Open your repository on GitHub. Confirm: README renders, file tree is visible, `.env` is absent.
11. Make at least two more meaningful commits — each commit adds one logical change (a working prompt loop, a data output function, an update to the README describing the new feature).

## 10. Key Takeaways

- A **folder structure** organises your project files by purpose. Code goes in `src/`, data goes in `data/`, and root-level files (`README.md`, `.gitignore`, `requirements.txt`) describe and configure the project. A clear layout communicates professionalism before anyone reads your code.
- A **README** is the homepage of your repository. It must answer: what does this project do, how do I set it up, and how do I run it. The five-section template (title and description, setup, usage, file structure, author) is a reliable starting point for any project.
- A **`.gitignore`** file tells Git which files to skip entirely. It must list `.env` and any other secrets files. It must be created before your first `git add` — once a secret is in Git history, it is very difficult to fully remove.
- An **API key** is a private credential that identifies you to an external service. Committing an API key to a public GitHub repository exposes it to the internet. Store keys in `.env`, load them with `os.getenv()`, and keep `.env` in `.gitignore`.
- A **`requirements.txt`** file lets anyone clone your repository and replicate your Python environment with one command: `pip install -r requirements.txt`. Without it, collaborators and reviewers cannot run your code without guessing.

## 11. Next Steps

_System-derived from the next entry in curriculum/sequence.md._
