---
topic_id: 8.2
title: Portfolio & Diagnostic
position_in_module: 2
generated_at: 2026-07-14T00:00:00Z
resource_count: 3
---

# 1. Portfolio & Diagnostic — Topic Corpus

## 2. Prerequisites
This topic builds directly on **8.1 Version Control Basics**. It assumes you already know what a repository, commit, and push are; that you've accepted at least one GitHub Classroom assignment; that you've edited a file and read commit history from the browser; and that you already treat a README as a repo's front door and a `.gitignore` as the place secrets get kept out of history. None of that is re-taught here — this topic is about applying those habits to one specific repo (your portfolio) and then proving, in a graded diagnostic, that both your Python foundation and your Git habits are solid enough to move on.

## 3. Learning Objectives

- Explain what a portfolio repository is for and who its real audience is.
- Structure a portfolio repo's folders and a project README so a stranger can understand it in under a minute.
- Describe what the end-of-Part-A diagnostic actually checks, in both Python and Git terms.
- Distinguish a diagnostic submission that is ready for faculty sign-off from one that is not.
- Apply README and repo-structure conventions to build (or clean up) your own portfolio repo before submitting the diagnostic.

## 4. Introduction

Up to this topic, every repo you've touched has been a scoped, disposable assignment repo — created by GitHub Classroom, graded, and then largely forgotten. Your **portfolio repository** is different on purpose: it's the one repo in this program that's meant to outlive the course. It's what you'll point a hiring manager, a mentor, or your own future self toward when someone asks "what have you built?" That changes what "good" looks like. A Classroom assignment repo only has to satisfy an instructor who already knows the assignment's context. A portfolio repo has to make sense to someone who has none of that context and who, realistically, will look at it for well under a minute before deciding whether to keep reading.

This topic also marks the end of Part A of the program. Before moving into Part B, you sit an end-of-Part-A diagnostic: a short, practical check that you can model data with Python classes, read and write files, handle errors instead of letting a program crash on bad input, and — the part this topic is specifically about — that your Git habits from 8.1 hold up under a real, graded task. The diagnostic isn't a new skill to learn from scratch; it's a checkpoint that asks you to show work you're already capable of, committed and pushed the way a professional would do it. A faculty member reviews the result and signs off before you're cleared for Part B. Getting that sign-off is the concrete goal of this topic.

Put simply: 8.1 taught you the mechanics of committing and pushing. This topic is about using those mechanics to build something that represents you, and then using them one more time, under evaluation, to prove you're ready to move forward.

## 5. Core Concepts

### 5.1 What a Portfolio Repository Is, and Who It's For

A **portfolio repository** is a GitHub repo whose purpose is to represent your work to an outside reader, rather than to satisfy a single graded assignment. GitHub's own guidance on repository best practices frames a repo's structure and documentation as something to design *for a reader who wasn't in the room when the work happened*[1] — and a portfolio repo takes that idea to its logical extreme, because its reader might genuinely be a stranger encountering your work for the first time, with zero shared context. That reframes almost every decision you make about the repo: file names, folder layout, and the README aren't just organizational tidiness for your own benefit — they're the entire explanation a visitor gets, and they get it before reading a single line of your actual code.

This is a different job than the Classroom repos from 8.1. An assignment repo can afford to look rough, because the person grading it already knows what the assignment was and what "done" looks like. A portfolio repo has no such safety net. GitHub's guidance is explicit that clear structure and documentation are what make a repository approachable to people encountering it cold[1] — and "people encountering it cold" is the default condition for anyone who looks at a portfolio.

Concretely, your portfolio repo is where you collect and present the strongest pieces of Python work you've produced across Parts 1 through 5 of this program, structured well enough that the collection reads as a coherent body of work rather than a folder dump. It's also the repo the end-of-Part-A diagnostic ultimately checks, since the diagnostic is graded partly on whether your Git habits — the same repo/commit/push loop from 8.1 — hold up on a repo meant to be shown, not just submitted.

### 5.2 Repo and Folder Structure Conventions

A portfolio repo benefits from the same underlying idea GitHub's repository guidance describes for any project: a small number of predictable, well-named top-level pieces, rather than files scattered with no discernible organization[1]. Community guidance on repository structure converges on a similar shape for project folders — separate, clearly named directories for source code, for documentation, and for anything a reader would want without digging, kept flat enough that a visitor can understand the whole layout at a glance rather than having to click through several nested levels first[3].

Applied to a beginner's portfolio, that means something like: a top-level `README.md` (covered in 5.3), a folder per project or per exercise set with a name that describes its contents rather than a generic label like `stuff` or `misc`, and consistent naming across those folders so a reader can predict where something lives before opening it. This guidance also applies to naming individual files: a script named `summary.py` or `csv_reader.py` tells a reader what to expect; a script named `final2.py` does not[1][3]. The specific point both the official guidance and community structure guidance make is the same one that mattered for commit messages in 8.1 — a name is a piece of information a reader gets for free, before they open anything, and a vague name wastes that opportunity[1][3].

None of this requires elaborate tooling. It requires the same discipline already built in 8.1: naming things so their purpose is visible, and keeping the repo's surface — its file and folder names — honest about what's actually inside.

### 5.3 README Sections for a Portfolio

8.1 established the README as a repo's front door. For a portfolio repo specifically, "front door" has a more concrete shape. Community guidance on writing a good README describes a small, repeatable set of sections that cover almost everything a reader needs: a clear title, a short description of what the project is and why it exists, a "quick start" section showing how to actually run or use it, and — where relevant — a demo, such as a screenshot or a short description of the tool in action[2].

Mapped onto a portfolio repo as a whole (not just one project inside it), those same sections do real work:

- **Title and description.** State plainly whose portfolio this is and what it collects — for example, "Python exercises and projects from Parts 1–5 of the AI-Native Engineering program." A reader should know what they're looking at in the first sentence, without inferring it from folder names[2].
- **Quick start.** For each project worth highlighting, a reader should be able to find, in a couple of lines, how to run it — what command, what input it expects, what it produces. Community README guidance treats this as the section that turns a passive reader into someone who actually tries the project, rather than one who reads a description and moves on[2].
- **Demo or example output.** Where a project produces visible output — a printed summary, a small report, a chart — showing that output directly in the README (or describing it precisely) lets a reader evaluate the work without setting anything up themselves[2]. This matters especially for a portfolio, where most readers won't run your code at all; the README is often the entire interaction.
- **A short index of what's inside.** Since a portfolio repo holds multiple projects rather than one, a brief list — project name, one-line description, link to its folder — lets a reader choose what to look at instead of guessing from folder names alone. This is the portfolio-specific extension of the general repository-documentation principle GitHub's own guidance describes: documentation should orient a reader before they start exploring the repo's structure[1].

None of these sections needs to be long. Community README guidance is explicit that the goal is clarity and completeness, not length — a short README that actually covers title, description, quick start, and demo outperforms a long one that rambles without covering any of them properly[2].

### 5.4 The End-of-Part-A Diagnostic and Faculty Sign-Off

The **Part A diagnostic** is a short, practical assessment that closes out Parts 1 through 5 of the program. It exists to confirm two things at once, together, in one artifact: that you can do the Python work Part A was building toward, and that you can commit and push that work the way 8.1 and this topic describe. The lab-activity brief for this week frames the diagnostic concretely as a task with a recognizable shape — reading a CSV file and printing a summary of it — sitting alongside the broader expectation, carried over from Parts 1–5, that you can model data with classes and handle files and errors without letting bad input crash your program.

This topic does not re-teach classes, file handling, or error handling — that Python foundation was built across Parts 1–5, and the diagnostic is where it gets checked, not where it's introduced. What this topic adds is the Git half of the bar: the diagnostic work has to actually live in your repo, committed with the same discipline from 8.1 — real, described commits, not one giant last-minute dump — and pushed so a faculty reviewer can see it on GitHub.

**Faculty sign-off** is the literal gate between Part A and Part B. A faculty member reviews your diagnostic submission — the code itself, whether it runs and handles the kind of messy input real CSV files contain, and the state of the repo it lives in — and signs off once it clears the bar. Until that sign-off happens, you don't move into Part B. This is why the habits from 8.1 aren't cosmetic at this point in the program: a reviewer looking at your repo's commit history, exactly as GitHub's guidance frames a repository's history and structure as the first thing a reader actually examines[1], is forming a judgment about your readiness from that history, not just from whether the final version of the code happens to work.

## 6. Implementation

Building a portfolio repo and clearing the diagnostic gate follows a sequence that reuses everything from 8.1 and 5.1–5.4 above:

1. Create a new repository dedicated to your portfolio, separate from any single Classroom assignment repo — this is the repo that persists past this course.
2. Add a top-level `README.md` before adding much else. Draft its title and one-paragraph description first, following the sections in 5.3[2].
3. Create one folder per project or exercise set you want to include, using names that describe the contents rather than generic labels, per the structure guidance in 5.2[1][3].
4. Move or recreate your strongest Python work from Parts 1–5 into those folders, keeping each project's files together rather than interleaved with unrelated work.
5. For each highlighted project, add a short "quick start" note in the README (or a per-project README) explaining how to run it and what it produces, per 5.3[2].
6. Commit this work the way 8.1 describes — small, described commits as you add each project, not one commit dumping everything at once — and push.
7. Read through the repo as a stranger would: open the top-level README first, then follow it into a project folder, and check whether the path from "front door" to "understand what this does" actually holds together.
8. Separately, complete the diagnostic task itself: read a CSV file, print a summary of it, and demonstrate the class-based modeling and error handling built across Parts 1–5, guarding against the kind of malformed rows or missing files a real CSV can contain.
9. Commit and push the diagnostic work into the appropriate repo with the same commit discipline from 8.1 — the reviewer is checking the history, not only the final file.
10. Submit for faculty review and wait for sign-off before starting any Part B material.

A common mistake at this stage is treating the portfolio repo and the diagnostic submission as unrelated chores completed back to back under time pressure, which tends to produce a rushed README and a single oversized commit for each. Since both are graded partly on the repo habits from 8.1, it's worth treating step 6 and step 9 with the same care given to the very first commit in 8.1 — a reviewer forming a first impression from your commit history is looking at exactly the same signal a hiring manager would look at later.

## 7. Real-World Patterns

The portfolio repo you build for this diagnostic is not a throwaway exercise — it's a smaller version of exactly what happens in professional hiring. Community guidance on repository structure and README quality is written for working engineers, not students, precisely because a real GitHub profile functions the same way a portfolio repo does here: a reviewer with limited time forms a judgment from structure and documentation before ever reading actual code[1][3]. A reviewer scanning a candidate's repositories typically opens the README first, and if it's missing, thin, or clearly copy-pasted, that absence itself becomes part of the judgment — not because the underlying code is necessarily weak, but because the reviewer has no way to tell without spending time they usually don't have[2].

Repo structure carries the same weight at a larger scale. Community guidance on structuring project folders describes exactly the problem a disorganized portfolio repo creates: a reader trying to figure out where anything lives, with no naming convention to rely on, gives up faster than a reader who can predict the layout from a handful of top-level folder names[3]. The habit built in 5.2 — descriptive folders, no generic dumping-ground names — is the same discipline professional teams enforce on much larger codebases, for the same reason: someone unfamiliar with the project has to be able to orient themselves without asking anyone.

The faculty sign-off gate itself has a direct professional analogue. Code review in industry exists for a similar reason: before work moves forward — merges into a shared branch, ships, or in this case, unlocks the next part of the program — someone with more context checks that it meets a bar, using both the work itself and the history behind it as evidence[1]. Treating the diagnostic's review as a real, if small-scale, version of that gate is accurate, not just a teaching device.

## 8. Best Practices

- Do write your portfolio README's title and description before adding any project folders — orient the reader first, per 5.3[2].
- Do give every project folder a name that describes its contents, and keep that convention consistent across the whole repo[1][3].
- Do show what each project actually does — a quick-start note, sample output, or a short demo description — rather than assuming a reader will run the code themselves[2].
- Do commit your portfolio and diagnostic work in small, described steps, exactly as in 8.1, rather than one large commit at the end[1].
- Do handle messy CSV input in the diagnostic deliberately — a missing file or a malformed row should produce a clear error, not a crash, since that's part of what the diagnostic checks.
- Do read your own repo as a first-time visitor would before submitting it for sign-off; if you can't follow it cold, a reviewer can't either.
- Don't leave a portfolio repo's README as a placeholder or a one-line stub — community guidance treats this as a real defect, not a minor gap[2].
- Don't dump every exercise you've ever written into the portfolio unsorted; a smaller, well-organized set of strong projects reads better than a large, disorganized one[1][3].
- Don't submit the diagnostic as a single last-minute commit; the reviewer is checking your Git habits from 8.1 as part of the sign-off, not only whether the code runs.
- Don't treat faculty sign-off as a formality to route around — it's the actual gate between Part A and Part B, and it exists to confirm the same readiness this whole topic is about.

## 9. Hands-On Exercise

Labs P6.3–P6.4 (gated): create your dedicated portfolio repository and write its top-level README following 5.3 (title, description, quick-start notes, and a short index of the projects it holds). Organize your strongest Parts 1–5 work into clearly named folders per 5.2, then complete the diagnostic task — read a CSV file and print a summary of it, using the class-based modeling and file/error handling built earlier in the program. Commit both the portfolio structure and the diagnostic work in small, described commits, push, and submit for faculty sign-off before continuing to Part B.

## 10. Key Takeaways

- A portfolio repository is built for a reader with no prior context, which makes structure and documentation the whole first impression, not a formality.
- Consistent, descriptive folder and file names let a stranger predict a repo's layout without opening every file.
- A strong portfolio README states what the collection is, describes each highlighted project, shows how to run it, and gives a reader a way to preview what it produces.
- The end-of-Part-A diagnostic checks two things together: your Python foundation from Parts 1–5, and whether the Git habits from 8.1 hold up on graded, reviewed work.
- Faculty sign-off is a real gate, not a formality — it's earned through both working code and a repo history that reflects the habits this program has been building since 8.1.

## 11. Next Steps
_System-derived from the next entry in curriculum/sequence.md._
