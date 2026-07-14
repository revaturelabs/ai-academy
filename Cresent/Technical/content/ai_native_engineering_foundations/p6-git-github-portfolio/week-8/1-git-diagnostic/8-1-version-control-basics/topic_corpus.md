---
topic_id: 8.1
title: Version Control Basics
position_in_module: 1
generated_at: 2026-07-14T00:00:00Z
resource_count: 5
---

# 1. Version Control Basics — Topic Corpus

## 2. Prerequisites
_No formal prerequisites._

## 3. Learning Objectives

- Explain what version control is and why professional engineers never ship code without it.
- Describe the basic Git loop — repository, commit, push — and what each step actually does to your files.
- Accept a GitHub Classroom assignment and locate the resulting cohort repository.
- Edit a file and inspect commit history using GitHub's web interface, without a local Git install.
- Apply good repo habits: a README as the front door, small descriptive commits, and a starter `.gitignore`.
- Distinguish the light difference between `main` and a feature branch at a beginner level.

## 4. Introduction

Every learner in this program has already lost work. A script got overwritten, a "final" version turned out not to be, or a working file got pasted over by an experiment that failed. Up to this point in the program, the safety net has been careful copy-pasting and file names like `analysis_v2_FINAL.py`. That doesn't scale past a single person working alone for an afternoon, and it completely falls apart the moment two people touch the same project.

Version control solves this by treating every saved snapshot of a project as a permanent, labeled point you can return to. Git is the version control tool nearly every professional software team uses, and GitHub is the most common place teams host their Git repositories so people can collaborate on them. From this point in the program forward, every diagnostic, lab, and portfolio piece lives in a Git repository — so the habits in this topic aren't optional background knowledge, they're the mechanism through which your work gets submitted, reviewed, and eventually shown to employers.

This topic covers the minimum a working engineer needs on day one: what a repository actually is, the repo → commit → push loop, how your cohort's assignments arrive through GitHub Classroom, how to make changes entirely from the browser (no terminal required yet), and the handful of habits — a real README, small commits, `.gitignore` — that separate a repo that looks professional from one that doesn't.

## 5. Core Concepts

### 5.1 What Git Is, and Why It Matters

Git is a **version control system**: a tool that records the history of a project as a series of snapshots, so you can see what changed, when, and by whom, and can recover any prior state[1]. The official Git documentation describes this at the tooling level — Git exists specifically so that history isn't just kept, it's meant to be inspected and reasoned about later[1]. Unlike relying on file names or a cloud sync tool, Git tracks *changes*, not just files — it knows that a specific line of `main.py` was edited, not merely that the file got replaced by a newer copy[1][2].

The reason professionals never work without it is not nostalgia for a tool — it's that software is written by teams, over time, and mistakes are guaranteed. Version control gives you three things simultaneously: a backup (nothing is ever truly lost once committed), a history (you can see exactly what changed and why), and a collaboration mechanism (multiple people can work on the same project without overwriting each other)[2]. Pro Git's introductory material frames this as the core value proposition of any version control system, Git included: the ability to revert files or an entire project back to a previous state, compare changes over time, see what changed and when, and recover cleanly if something goes wrong[2].

Consider a concrete version of the failure this solves. Two learners in a cohort are both asked to edit the same shared exercise file over the course of a week, on their own schedules. Without version control, whichever person saves last simply overwrites the other's work — there is no record that the first person's changes ever existed, and no way to recover them. With Git, both edits become separate, timestamped commits; nothing is silently destroyed, and the full sequence of who-changed-what-and-when is preserved and inspectable after the fact[1][2]. This is the entire reason "just email me the file" or "just use a shared folder" stop working once more than one person, or one point in time, is involved.

Git specifically is *distributed*: every copy of a repository carries the entire project history, not just a pointer to a central server[1][2]. That's part of why it became the industry standard — you can work offline, inspect history, and make progress without any network connection at all, and no single machine is a single point of failure[2]. This is a meaningfully different design from older version-control approaches where the history lived only on one central server, and losing that server meant losing the history. Under Git's model, your own machine already holds a full, independent copy of everything that has ever been committed, which is one reason recovering from a mistake is almost always possible[1][2].

It's worth pausing on why this matters *now*, specifically, rather than as abstract background. In this program, "the assignment" and "the repository" become the same object starting with this topic. There is no separate submission step to remember or a file to email — the repository *is* the submission, continuously, from your first commit onward[2]. That also means the habits you build in this topic aren't graded once and forgotten; they compound, because the same repo, and the same history inside it, keeps growing for the rest of the course.

### 5.2 The Basic Loop: Repository, Commit, Push

Three vocabulary words carry almost all of the beginner workload:

- **Repository ("repo")** — a project folder that Git is tracking. It contains your files plus a hidden history of every snapshot ever recorded[1][2]. A repo can live only on your machine, or it can also exist on GitHub as a *remote* — a copy hosted online that others (and you, from another machine) can reach. Pro Git's walkthrough of "Getting a Git Repository" describes the two ways a repository comes into existence: you turn an existing folder into one, or you obtain a copy of one that already exists elsewhere[2].
- **Commit** — a saved snapshot of the repo at a point in time, paired with a short message describing what changed. A commit is not "saving the file" — it's a deliberate checkpoint you create when a chunk of work is worth remembering. Pro Git's getting-started material frames this as the core habit to build first: treat a meaningful, describable chunk of work as one commit, rather than committing every keystroke, and rather than saving up an entire day of unrelated changes into a single giant commit[2]. Community best-practice guidance agrees: a commit should represent one logical unit of work, so that later, each individual entry in the history tells a complete, understandable story on its own[3].
- **Push** — sending your local commits up to the remote repository (typically on GitHub) so they become visible and available to anyone else with access[1][2]. Until you push, your commits exist only on your machine — they are recorded, safe, and real, but invisible to a collaborator, an instructor, or a grading system looking at the GitHub-hosted copy.

Put together, the loop looks like: **make a change → commit it (with a message describing what and why) → push it to GitHub.** Everything else in this topic — Classroom, the web editor, branching — is a variation on getting through that same loop[2].

It's worth being explicit about why this is three separate steps rather than one. Separating "commit" from "push" means you can make several small, well-described checkpoints on your own machine — trying something, backing it out, trying again — without any of that in-progress churn being visible to anyone else, and then push only once you're ready for it to be seen[2][3]. This is part of why professional commit history tends to read as a clean narrative of finished thoughts rather than a live feed of every keystroke a person typed.

The difference between a helpful and an unhelpful commit is easiest to see side by side. A commit message reading `"stuff"` or `"changes"` requires a reader to open the diff and reconstruct the intent themselves, every single time. A commit message reading `"Add data-cleaning function for missing timestamps"` tells the reader what happened without opening anything at all, and if they do open it, the diff confirms rather than replaces the message[2][3]. Community best-practice guidance is explicit that the second style is not a stylistic nicety — it is what makes a commit history searchable and trustworthy months after it was written[3].

### 5.3 GitHub Classroom

**GitHub Classroom** is the tool instructors use to distribute assignments as individual GitHub repositories to every student in a cohort, without manually creating one repo per learner[4][5]. When your instructor shares an assignment link, **accepting the assignment** does two things automatically: it creates a new repository under your GitHub account (or your organization, depending on setup), seeded with any starter files the instructor provided, and it grants you — and usually the instructor, for grading — access to that repo[4][5]. That repo is now yours: it's where your diagnostic work, labs, and portfolio pieces for this course live.

Under the hood, Classroom is doing repository-provisioning work that would otherwise be manual and error-prone at cohort scale: for every student who clicks the assignment link, it copies a template repository's starter content into a brand-new repo scoped to that one student, names it according to the assignment and the student's identity, and configures access so the student can push to it while the instructor can see it[4]. A step-by-step instructor-side walkthrough of setting up Classroom documents this same pipeline from the other direction: an instructor configures one assignment and one starter template, and Classroom fans that single configuration out into a correctly permissioned repo per student automatically, which is exactly why your accept-link click "just works" without anyone on the teaching side touching your repo by hand[5].

Student-facing documentation on the accept flow also describes what to expect in the minute or two right after clicking: Classroom shows a short "creating your repository" status, then redirects you to the finished repo once provisioning completes, at which point the repo's name typically combines the assignment name with your GitHub username or student identifier so that an instructor scanning a list of dozens of repos can immediately tell whose is whose[4]. If you click the link again later, Classroom recognizes you've already accepted and takes you straight back to your existing repo rather than creating a second one[4][5].

This matters practically because it removes an entire category of setup friction: you don't manually create a copy of the instructor's repository under your own account, you don't configure who can see or push to it, and you don't guess at folder structure[4][5]. You click the assignment link, accept it, and a correctly-scoped repo appears under your account, ready for you to commit to. Everything you push to that repo is what your instructor sees when they check your progress or grade a diagnostic — Classroom's whole design point is that whether a student has pushed something is directly and automatically visible to the instructor without any extra step on either side[4][5].

One practical detail worth internalizing early: because the repo Classroom creates is genuinely yours in the access-and-push sense, everything from 5.2's loop applies to it exactly as described — you commit and push into that same repo for the rest of this course. The very first commit you make there is worth treating as real practice, not throwaway, since it's the same repo your later diagnostics and portfolio pieces will build on.

### 5.4 Working via the Web Interface

You do not need a terminal or a local Git installation to get started. GitHub's website lets you do real, committed work directly in the browser, and this program deliberately starts here[4][5]:

- **Editing files in the browser.** Opening any file in a repo shows a pencil/edit icon. Editing there and clicking "Commit changes" performs an entire commit — and, because the file already lives on GitHub, effectively a push too — without ever leaving the page[4]. This is the same underlying operation described in 5.2, a described snapshot of a change, just performed through a form instead of a command line[2][4].
- **Reading commit history.** Every repo has a commits view listing every snapshot ever pushed, in order, each with its message, author, and timestamp[1][2]. Opening any single commit shows exactly which lines changed and which didn't. This is the same history mechanism described in 5.2 — the web page is simply a viewer on top of the same underlying record that the official Git documentation treats as a first-class, inspectable part of a repository[1][2].
- **Why this order, pedagogically.** Student-facing Classroom guidance walks new students through browser-based edits before introducing a terminal, precisely because it isolates the *concept* of a commit and its history from the *mechanics* of a command line[4]. A companion instructor-side walkthrough makes a parallel point from the teaching side: for a cohort's first assignment, being able to verify that a student produced a real, timestamped commit matters more than which tool they used to produce it[5].

This browser-first path is deliberately how this course begins: it lets you build the mental model of commit history and repo structure — the same repository, commit, and push concepts from 5.2 — before adding the complexity of local Git commands and a terminal[4][5]. Nothing about a browser-made commit is a "lesser" commit; it lands in the exact same history, visible in exactly the same way, as one made from a terminal later in the program[1][2]. Practically, this also means the good habits introduced in 5.5 — a real README, a focused commit message, a `.gitignore` before you need one — apply from your very first browser edit, not just once you graduate to a terminal[3][4].

It also means there is no "practice mode" distinct from the real thing here: the commit box you type into in the browser is the exact same commit-message field that a terminal-based workflow fills in later, and the discipline of writing a specific, honest description of the change is being built starting with your very first edit, not deferred until it "counts"[3][4].

### 5.5 Good Habits: README, Commit Hygiene, Branching, `.gitignore`

Four habits separate a repo that reads as professional from one that doesn't, and they're worth building from your very first commit rather than retrofitting later.

**README as the front door.** Every repo should have a `README.md` at its root, because GitHub renders it automatically on the repo's main page — it's the first, and often only, thing a visitor, grader, or future employer sees[3][4]. A good README states what the project is, how to use or run it if that's relevant, and — for a portfolio repo — why it exists. Community best-practice guidance treats a missing or one-line README as a genuine defect in a repository, not a cosmetic gap, precisely because it's the artifact that gives every other file its context before anyone reads a single line of code[3]. A weak README ("This is my project") and a strong one ("A command-line tool that summarizes CSV survey data into a single readable report; run it with one argument, the input file path") both take about the same amount of typing — the difference is entirely in whether the author thought about the reader at all[3].

**Small, descriptive commits.** A commit message like `"fix"` or `"stuff"` tells a reader nothing six months later, including future you. Community best-practice guidance converges on the same two rules: keep each commit focused on one logical change, and write a message that explains *what* changed and *why*, not just that something changed[3]. Small, frequent commits also make history genuinely useful: if something breaks, you can pinpoint exactly which commit introduced the problem by reading messages and comparing snapshots, which is nearly impossible if one commit rewrites twenty files at once[2][3]. Pro Git's getting-started material reinforces the same discipline from the tooling side — Git's history-inspection tools are only as useful as the commits they're inspecting are small and clearly labeled to begin with[1][2].

**Branching basics — `main` vs. a feature branch (light intro).** `main` is the default branch and is conventionally treated as the stable, working version of the project[2]. A **feature branch** is a copy of the project made to try something — an experiment, a fix, a new piece of work — without touching `main` until it's ready[2][3]. At this stage you only need the concept: `main` is "the real thing," a feature branch is "a sandboxed attempt." Combining a feature branch's work back into `main` is itself a deliberate, reviewed step with its own tools and vocabulary — that's a later topic in this program. For now, the important habit is scope discipline: professional repos rarely have everyone committing directly and permanently to `main`, because that turns the one branch everyone depends on into a place where half-finished experiments can break things for the whole team[2][3].

**`.gitignore` for secrets (intro).** A `.gitignore` file tells Git which files or patterns to *never* track or push — for example, files containing API keys, passwords, or personal credentials[1][3]. This isn't cosmetic: a committed API key is visible in the repo's permanent history forever, even if you delete the file in a later commit, because Git's whole design point from 5.1 is that old snapshots are preserved, not overwritten[1][2]. Public repos get scraped by automated bots looking for exactly this pattern of leaked credentials, often within minutes of a push[3]. The habit to build now is simple: before you ever add a real credential to a project, make sure a `.gitignore` covers it, because "I'll remove it later" does not undo a commit that already happened[1][3].

## 6. Implementation

The end-to-end loop for this topic, done entirely through the browser, walks through every concept introduced in 5.2 through 5.4 in order:

1. Open the GitHub Classroom assignment link your instructor provides.
2. Accept the assignment — GitHub creates your personal copy of the repo and adds you as a collaborator, exactly as described in 5.3[4][5].
3. Confirm the repo exists under your account and open it; note the starter files your instructor seeded it with, if any, and the repo's name, which typically combines the assignment and your identity as described in 5.3[4].
4. Open `README.md` (or create one if it's missing) and click the pencil icon to edit the file directly in the browser[4].
5. Make a small, meaningful change — for example, add a two- or three-sentence project description, following the README habit from 5.5[3][4].
6. Scroll down to the commit box, write a short, specific commit message describing exactly what you changed (not "update"), and click "Commit changes." This both commits and pushes in one step, since you're editing the hosted copy directly, collapsing the loop from 5.2 into a single browser action[2][4].
7. Click the commits (or history) view on the repo to confirm your commit appears with your message and timestamp, matching the history mechanism described in 5.4[1][2].
8. Open the commit you just made and confirm the diff view shows exactly the lines you changed — nothing more — which is the practical check that your commit was small and scoped, per the habit in 5.5[3].
9. Repeat steps 4–7 for a second, unrelated small change — for example, adding a `.gitignore` with a placeholder entry — so you can see two distinct, separately-messaged commits in the history[1][3].
10. Compare the two commits side by side in the history view: each should read, on its own, as a complete explanation of one change. This is the pattern you'll repeat, with real code and eventually a terminal, for the rest of the program[2][3].
11. Before moving on to your next diagnostic, skim the repo's file list once more and confirm nothing that looks like a real credential or personal detail is sitting in a tracked file; if it is, address it via `.gitignore` now rather than after it's already been pushed, per the secrets habit in 5.5[1][3].

A common early mistake is worth flagging here: making one large commit at the end of a working session that bundles the README edit, a `.gitignore`, and unrelated changes together. It will still push successfully — Git doesn't stop you — but it defeats the purpose described in 5.2 and 5.5, because a single commit message now has to describe several unrelated things at once, and none of them can be inspected independently later[2][3]. If you notice you've drifted into this pattern mid-session, it's worth stopping and committing what you have before continuing, rather than letting the bundle grow further. A second common mistake is the opposite failure: never committing at all until the very end of an assignment, out of a sense that a commit should only happen once something is "finished." Nothing about the loop in 5.2 requires that — a commit is a checkpoint, not a finish line, and Classroom-based grading generally looks at the whole history, not just the last snapshot[4][5].

## 7. Real-World Patterns

Professional teams live inside this loop dozens of times a day, just at larger scale, and every habit introduced in 5.5 exists because of a real failure mode it prevents.

A production codebase's `main` branch is typically protected — nobody pushes to it directly; changes arrive as small commits on a feature branch, get reviewed, and only then join `main` through a deliberate, gated process[2][3]. This is the industrial-scale version of the light branching intro in 5.5: the reason `main` is guarded so carefully is that it's usually the version actually running for real users, so an untested or half-finished change landing there directly can break a live system, not just inconvenience the author[2].

Commit history is treated as documentation, not just as a backup mechanism. Engineers routinely inspect the history — the exact mechanism described in 5.2 and 5.4 — to answer "why is this line here?" months or years after it was written, which only works because someone wrote a real, specific commit message at the time[1][2][3]. This is the exact payoff the commit-hygiene habit in 5.5 is building toward: a commit message written today is read by a stranger, often a future version of the same engineer, long after the context that made the change obvious has been forgotten[3]. Open-source projects make this especially visible: a well-known project's public commit history is routinely the only documentation of *why* a particular design decision was made, since the original discussion may have happened once and never been written down anywhere else[2][3].

A repo's README is frequently a hiring manager's or reviewer's first, and sometimes only, exposure to a candidate's work when browsing a GitHub profile, exactly as described in 5.5 — which is exactly why this program treats your portfolio repo's README as a real deliverable, not decoration[3][4]. A blank or one-line README on an otherwise solid project routinely costs that project the benefit of the doubt, because the reader has no framing for what they're about to look at before they start reading code[3].

`.gitignore` discipline is taken seriously industry-wide for a concrete reason: leaked API keys and credentials from committed configuration files are one of the most common, and most preventable, real-world security incidents[1][3]. Because Git preserves every historical snapshot, as described in 5.1, a leaked credential doesn't just need to be removed from the current version of a file — the leak persists in the repo's history even after a later commit deletes it, meaning the credential typically has to be treated as fully compromised and replaced, rather than merely cleaned up[1][2][3]. Public repositories are actively scraped by bots looking for exactly this pattern, and organizations have had systems accessed or cloud costs run up within minutes of a secret being pushed publicly — which is why the habit in 5.5 is framed as "before you need it," not "after"[3]. This is precisely why the very first `.gitignore` entry many real projects add is for the file format that typically holds local credentials, well before there's any actual secret in the repo to protect[1][3].

Finally, the browser-first workflow from 5.4 has a real-world analogue too: GitHub's own web-based editing and commit tools are commonly used by working engineers for small, low-risk changes — fixing a typo in documentation, updating a single configuration value — precisely because for a change that small, opening a full local development environment is more overhead than the change itself[4]. The skill this topic builds, recognizing when a change is small enough to make confidently through the web interface, doesn't stop being useful once you have a terminal; it stays a real, ongoing part of how experienced engineers work[4][5].

## 8. Best Practices

- Do commit early and often — a commit is cheap; losing an afternoon of work is not, and Git's whole value from 5.1 depends on work actually being committed, not just saved to disk[1][2].
- Do write commit messages as a sentence describing the change ("Add CSV summary function"), not a single vague word like "fix" or "update"[2][3].
- Do keep each commit scoped to one logical change, so that reading the history one commit at a time later actually tells a coherent story[2][3].
- Do keep secrets — API keys, tokens, passwords — out of tracked files from the very first commit; add `.gitignore` entries before you need them, not after a leak, because a committed secret persists in history even after deletion[1][3].
- Do treat your README as the first thing a reader sees, because for most repos, it is[3][4].
- Do use the browser editor for genuinely small changes even after you have a terminal available — it's a real professional habit, not just a beginner's crutch[4].
- Do check, before you push, that a change is actually what your commit message says it is — the message and the diff should always agree[2][3].
- Don't treat `main` as a scratchpad for half-finished experiments once branching is in play — that's what feature branches are for, and production teams protect `main` for exactly this reason[2][3].
- Don't wait until a project is "done" to make your first commit; there is no such thing as too early, and an empty or near-empty first commit costs nothing[1][2].
- Don't bundle unrelated changes into a single commit just to save time — it defeats the purpose of having a history at all[2][3].
- Don't assume deleting a leaked secret in a later commit removes it from the repo; treat any committed secret as compromised and replace it[1][3].
- Don't rely on remembering which repo is "the real one" if you ever end up with more than one copy of an assignment — Classroom's accept-link flow is designed so there is exactly one repo of record per student per assignment; if something looks off, re-open the original assignment link rather than guessing[4][5].

## 9. Hands-On Exercise

Using your GitHub Classroom repo for this course (Lab P6.1–P6.2): accept the assignment, edit `README.md` in the browser to describe the repo in two sentences, commit with a specific message, then make one more small edit and commit it separately. Open the commits view and confirm you can see both commits, each with a distinct, readable message — this is the artifact your instructor checks before sign-off on Part B.

## 10. Key Takeaways

- Version control (Git) exists because software mistakes and multi-person collaboration are guaranteed; it gives you backup, history, and collaboration in one tool.
- The core loop is repository → commit → push: a repo holds tracked history, a commit is a described snapshot, and a push sends commits to a remote like GitHub.
- GitHub Classroom turns an assignment link into your own ready-to-use repo, with no manual setup.
- You can do real, committed work entirely from GitHub's web interface — edit a file, commit it, and read the resulting history — before ever touching a terminal.
- A strong repo has a real README, small and descriptive commits, an early `.gitignore` for secrets, and (as a light intro) treats `main` as the stable line with experiments kept off it.

## 11. Next Steps
_System-derived from the next entry in curriculum/sequence.md._
