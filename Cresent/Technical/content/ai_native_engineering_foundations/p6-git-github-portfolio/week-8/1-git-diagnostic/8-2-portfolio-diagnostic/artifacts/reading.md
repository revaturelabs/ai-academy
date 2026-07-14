# Portfolio & Diagnostic

## Overview

Every repo you've touched so far was a scoped GitHub Classroom assignment. It got created, graded, and then forgotten. Your **portfolio repository** is different. It's the one repo in this program meant to outlive the course. It's the repo you point a hiring manager, or your future self, toward when someone asks "what have you built?" That single change in audience changes what "good" looks like. An assignment repo only has to make sense to an instructor who already knows the context. A portfolio repo has to make sense to a stranger who has none of that context. It has to do that in under a minute. This topic is also the close of Part A. Before Part B, you sit an end-of-Part-A diagnostic. It checks two things at once: your Python foundation from Parts 1–5, and whether the Git habits from 8.1 hold up under real, graded work. A faculty member signs off once it clears the bar. _This contributes to A3 — Python Foundations Diagnostic (due W8). The diagnostic checks that you can model data with classes, handle files and errors robustly, and maintain a professional Git portfolio. It confirms you're ready to begin the AI modules._

## Key Concepts

**A portfolio repo is built for a reader who wasn't in the room.** GitHub's own repository guidance frames structure and documentation as something designed for exactly that reader. It's meant for someone encountering the work cold, with zero shared context[1]. A Classroom repo can afford to look rough, because the grader already knows the assignment. A portfolio repo has no such safety net. File names, folder layout, and the README aren't tidiness for your own benefit. They're the entire explanation a visitor gets, and they get it before reading a single line of actual code[1]. Concretely, your portfolio is where you collect the strongest Python work from Parts 1–5. Organize it so it reads as a coherent body of work rather than a folder dump. In practice, that might mean three or four polished projects rather than every exercise you've ever submitted. It's also the same repo the diagnostic ultimately checks. The diagnostic grades whether your 8.1 repo, commit, and push habits hold up on something meant to be shown, not just submitted.

**Structure: a small number of predictable, well-named pieces.** GitHub's guidance describes good repo structure as a handful of clearly named top-level pieces, rather than files scattered with no organization[1]. Community guidance on project structure converges on the same shape. It calls for separate, clearly named directories for source code and documentation. Keep that layout flat enough that a visitor understands the whole structure at a glance, instead of clicking through nested folders first[3]. Applied to a beginner's portfolio, this means one top-level `README.md` and one folder per project or exercise set, each named for its contents. Keep naming consistent across the whole repo, so a reader can predict where something lives before opening it. A folder named `csv_summary_tool` tells a reader what to expect before they open it. A folder named `stuff` or `misc` tells them nothing, and forces a click just to find out. The same logic applies to individual files — `csv_reader.py` tells a reader what to expect; `final2.py` does not[1][3]. This is the same principle that made commit messages matter in 8.1: a name is information a reader gets for free. A vague one wastes that opportunity[1][3].

**The README's job, made concrete.** 8.1 established the README as a repo's front door. For a portfolio, that door needs a specific set of rooms behind it. Community README guidance describes a small, repeatable set of sections that cover almost everything a reader needs. It calls for a clear title and a short description of what the project is and why it exists. It also calls for a quick-start section showing how to actually run it. Where relevant, it calls for a demo or sample output too[2]. Mapped onto a portfolio as a whole:

- **Title and description** — state plainly whose portfolio this is and what it collects (e.g., "Python exercises and projects from Parts 1–5 of the AI-Native Engineering program"). A reader should know what they're looking at from the first sentence, not by inferring it from folder names[2].
- **Quick start** — for each highlighted project, a couple of lines on what command to run, what input it expects, and what it produces. This is what turns a passive reader into someone who actually tries the project[2].
- **Demo or example output** — showing a printed summary, small report, or sample output directly in the README lets a reader evaluate the work without setting anything up. A single line like "Rows processed: 240, malformed rows skipped: 3" tells a reader more about the tool in five seconds. That beats a paragraph of description. For a portfolio, the README is often the *entire* interaction a visitor has with your work[2].
- **A short index of what's inside** — a portfolio holds multiple projects, not one. A brief list — project name, one-line description, link to its folder — lets a reader choose what to look at instead of guessing. This extends the same principle GitHub's guidance gives for any repo: documentation should orient a reader before they start exploring structure[1].

Community guidance is explicit that the target is clarity and completeness, not length. A short README covering title, description, quick start, and demo beats a long one that rambles without covering any of them properly[2].

**The end-of-Part-A diagnostic and faculty sign-off.** The diagnostic is a short, practical assessment. It confirms two things together, in one artifact. It checks that you can do the Python work Part A built toward, and that you can commit and push that work with 8.1-level discipline. The Python side covers modeling data with classes, reading and writing files, and handling errors instead of crashing on bad input. Concretely, the task has a recognizable shape: read a CSV file and print a summary of it. That summary has to come from class-based modeling and error handling that survives malformed rows or missing files. In practice that means catching a missing-file error instead of letting the program crash. It also means skipping or flagging a malformed row instead of letting one bad line stop the whole summary. This topic doesn't re-teach classes or file handling — Parts 1–5 already built that. The diagnostic is where those skills are checked, not where they're introduced. What this topic adds is the Git half: the work has to live in your repo, committed the way 8.1 describes. That means real, described commits, not one last-minute dump, pushed so a reviewer can see it on GitHub. **Faculty sign-off** is the literal gate between Part A and Part B. A faculty member reviews the code — does it run, does it handle messy input — and the repo it lives in. They sign off once both clear the bar. Until then, Part B doesn't start. A reviewer examining your commit history is forming a judgment about your readiness from that history. That is exactly the first thing GitHub's own guidance says a reader actually looks at[1], not only whether the final version happens to work.

## Worked Example

Walk through building the portfolio repo end to end, reusing 8.1's mechanics and the concepts above:

1. **Create a dedicated repository** for your portfolio, separate from any single Classroom assignment repo — this is the one that outlives the course.
2. **Add `README.md` first**, before much else exists. Draft the title and one-paragraph description before adding project folders, so the reader is oriented from commit one[2].
3. **Create one folder per project or exercise set**, named for its contents — `data_class_exercises`, not `week3` or `misc` — per the structure guidance above[1][3].
4. **Move your strongest Parts 1–5 work into those folders**, keeping each project's files together rather than interleaved with unrelated work.
5. **Add a quick-start note per highlighted project**, in the top-level README or a per-project README[2]. Keep it concrete rather than generic: state the exact command a reader would type, such as `python summary.py transactions.csv`, name the one argument it needs (the CSV path), and describe the output in one line — a row count, a count of skipped or malformed rows, and a short summary statistic. A reader who sees that before opening the file already knows what the project does and whether it's worth a closer look.
6. **Commit in small, described steps** as each project is added — not one commit dumping everything at once — and push, exactly as 8.1 taught.
7. **Read the repo as a stranger would**: open the top-level README first, follow it into a project folder, and check whether "front door" to "understand what this does" actually holds together in under a minute.
8. **Separately, complete the diagnostic task**: read a CSV file, print a summary, and demonstrate class-based modeling and error handling against malformed rows or a missing file.
9. **Commit and push the diagnostic work** with the same discipline as step 6 — the reviewer checks history, not only the final file.
10. **Submit for faculty review** and wait for sign-off before starting any Part B material.

The most common failure mode here is treating steps 1–7 (the portfolio) and steps 8–9 (the diagnostic) as two unrelated chores finished back to back under time pressure. That approach tends to produce a rushed README and one oversized commit for each. Both are graded partly on 8.1 habits. Treat steps 6 and 9 with the same care you gave your very first 8.1 commit — a reviewer's first impression from commit history is the same signal a hiring manager will look at later.

## In Practice

This exercise is a smaller version of what already happens in professional hiring, not a classroom-only ritual:

- A reviewer with limited time forms a judgment from structure and documentation before ever reading actual code[1][3]. They typically open the README first. If it's missing, thin, or clearly copy-pasted, that absence itself becomes part of the judgment, whether or not the underlying code is strong[2].
- Disorganized structure carries the same weight at scale: a reader trying to figure out where anything lives, with no naming convention to rely on, gives up faster than one who can predict the layout from a handful of top-level folder names[3].
- Code review in industry exists for the same reason faculty sign-off does here: before work moves forward — merges, ships, or unlocks the next part of a program — someone with more context checks it against a bar, using both the work and the history behind it as evidence[1]. The same bar applies whether the reviewer is a senior engineer approving a pull request or a faculty member approving a diagnostic.

Do:
- Write the portfolio README's title and description before adding project folders[2].
- Give every project folder a name that describes its contents, and keep the convention consistent[1][3].
- Show what each project does — quick-start note, sample output, or a short demo description — rather than assuming a reader will run your code[2].
- Commit portfolio and diagnostic work in small, described steps, as in 8.1[1].
- Handle messy CSV input deliberately — a missing file or malformed row should produce a clear error, not a crash.
- Read your own repo as a first-time visitor before submitting; if you can't follow it cold, a reviewer can't either.

Don't:
- Leave the README as a placeholder or one-line stub — community guidance treats this as a real defect, not a minor gap[2].
- Dump every exercise you've ever written into the portfolio unsorted; a smaller, well-organized set of strong projects reads better than a large, disorganized one[1][3].
- Submit the diagnostic as a single last-minute commit — the reviewer is checking your Git habits as part of sign-off, not only whether the code runs.
- Treat faculty sign-off as a formality to route around — it's the actual gate between Part A and Part B.

## Key Takeaways

- A portfolio repository is built for a reader with no prior context, which makes structure and documentation the whole first impression, not a formality.
- Consistent, descriptive folder and file names let a stranger predict a repo's layout without opening every file.
- A strong portfolio README states what the collection is, describes each highlighted project, shows how to run it, and gives a reader a way to preview what it produces.
- The end-of-Part-A diagnostic checks two things together: your Python foundation from Parts 1–5, and whether the Git habits from 8.1 hold up on graded, reviewed work.
- Faculty sign-off is a real gate, not a formality — earned through both working code and a repo history that reflects the habits this program has built since 8.1.

## References

[1] GitHub Docs — *Best practices for repositories*. https://docs.github.com/en/repositories/creating-and-managing-repositories/best-practices-for-repositories

[2] freeCodeCamp — *How to Write a Good README File*. https://www.freecodecamp.org/news/how-to-write-a-good-readme-file/

[3] Medium (Code Factory Berlin) — *GitHub Repository Structure Best Practices*. https://medium.com/code-factory-berlin/github-repository-structure-best-practices-248e6effc405
