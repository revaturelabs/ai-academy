<!-- nav:top:start -->
[⬅ Previous: 2.6 — When NOT to use AI](../../../3-the-professional-rules-of-ai-use/2-6-when-not-to-use-ai-privacy-precision-legal-accountability/artifacts/reading.md)&emsp;·&emsp;[⬆ Table of Contents](../../../../../../../README.md#curriculum-topic-index)&emsp;·&emsp;[Next: 2.8 — Testing a specification ➡](../../2-8-testing-a-specification-how-to-verify-the-ai-did-exactly-wha/artifacts/reading.md)
<!-- nav:top:end -->

---

# Writing Specifications Across Five Domains — Health, Transport, Education, Food, Scheduling

## Overview

You have learned what makes a specification good: it must be testable, bounded, observable, and actionable. Now it is time to put those properties to work across real tasks. This reading walks through five everyday domains — health, transport, education, food, and scheduling — showing how the same four-part structure applies in each one. What changes from domain to domain is not the structure itself, but the *type* of constraint that makes a spec bounded and the *type* of output that makes it observable [1].

## Key Concepts

### The Four-Part Structure Every Strong Specification Shares

Before looking at the five domains, here is the one template that covers all of them. Every strong specification contains four parts — no more, no less [1]:

| Part | What it does | Signal words |
|---|---|---|
| **Task statement** | Names the action and its subject | "Summarise…", "Generate…", "List…", "Identify…", "Create…" |
| **Context** | Gives the background the AI needs to act correctly for *your* situation | "for a 12-year-old", "using only the attached timetable", "based on UK supermarket ingredients" |
| **Constraints** | Sets the fences — what is in, what is out, how long, what format | "no more than 3 items", "do not include X", "under 150 words", "use a numbered list" |
| **Expected output format** | Describes the concrete thing you will receive | "a table with columns A and B", "a plain-English paragraph", "a numbered list of steps" |

These four parts map directly onto the properties you already know:

- Task statement + context → **actionable** (the AI has enough to start without guessing)
- Constraints → **bounded** (scope and limits are explicit)
- Expected output format → **observable** (you know what you will receive and can check it)
- All four together → **testable** (you can verify the output against what you asked for)

If any part is missing, the AI fills the gap with a guess — and that guess usually does not match your situation [3].

---

### Domain 1 — Health

Health tasks often involve personal numbers: step counts, blood pressure readings, calorie totals, medication schedules. A spec in this domain must be precise about the **metric** (which number), the **time range** (which days or period), and the **output shape** (a list, a table, a set of sentences).

- "Bounded" in health usually means: which metric, over which time period, for which population.
- "Observable" in health means: a concrete list, table, or set of reported data points — not "health advice" or a vague "overview."

**Weak specification:**
> "Help me understand my health data."

**Strong specification:**
> "I have a table of my daily step counts for the last 14 days (attached). Identify the three days with the lowest step counts. For each of those days, write one sentence stating the date and the count. Do not give health advice or suggest causes — just report the three data points."

| Part | What it provides |
|---|---|
| Task statement | "Identify the three days with the lowest step counts" |
| Context | "daily step counts for the last 14 days (attached)" |
| Constraints | three days only; one sentence per day; no health advice; no suggested causes |
| Expected output format | three sentences, each stating a date and a count |

**What changed:** "Understand" is not observable — it describes a mental state, not a deliverable. The strong spec replaces it with a specific action (identify, report). The data source is named. The output is limited to three data points in a fixed sentence format. The constraint "do not give health advice" keeps the AI from producing output that requires professional judgment [2].

---

### Domain 2 — Transport

Transport tasks involve routes, times, distances, and comparisons between options. Getting them right depends on fixing the journey completely before the AI acts.

- "Bounded" in transport means: start point, end point, date and time, mode of travel, and number of options.
- "Observable" in transport means: a route, a schedule table, or a comparison — not a general discussion of travel options.

**Weak specification:**
> "Tell me how to get to the airport."

**Strong specification:**
> "I need to travel from Liverpool Street Station, London, to Heathrow Airport Terminal 2 on a weekday morning, arriving by 07:30. List the two fastest public transport options that arrive by 07:30. For each option, state: the route name or number, the departure time from Liverpool Street, the arrival time at Terminal 2, and the number of changes required. Present this as a table with those four columns."

| Part | What it provides |
|---|---|
| Task statement | "List the two fastest public transport options" |
| Context | "Liverpool Street to Heathrow Terminal 2, weekday morning, arrive by 07:30" |
| Constraints | two options only; public transport only; arrival by 07:30 |
| Expected output format | a table: route name, departure time, arrival time, number of changes |

**What changed:** The weak spec gives the AI no journey details at all — it will either ask follow-up questions or pick defaults that may not match your situation. The strong spec names the exact origin, destination, terminal, day type, arrival deadline, and number of options. The table format means you can compare results directly the moment you read them [1].

---

### Domain 3 — Education

Education tasks involve explaining, assessing, or teaching content. The most common failure here is leaving the **audience** undefined — the AI then picks a default age and knowledge level that may not fit.

- "Bounded" in education means: the audience's age or knowledge level, the subject, the length of the output, and what should be excluded (such as advanced content or technical formulas).
- "Observable" in education means: a set of questions, an explanation in plain text, a lesson plan with named sections — not "an engaging lesson."

**Weak specification:**
> "Explain photosynthesis."

**Strong specification:**
> "Explain photosynthesis for a 12-year-old who has no prior science knowledge. Cover only these three points: (1) what photosynthesis is in one plain-English sentence, (2) what the plant needs as inputs (sunlight, water, carbon dioxide), and (3) what the plant produces (glucose and oxygen). Do not use chemical formulas or scientific terminology beyond these terms. Keep the total response under 150 words."

| Part | What it provides |
|---|---|
| Task statement | "Explain photosynthesis" |
| Context | "for a 12-year-old with no prior science knowledge" |
| Constraints | three points only; no formulas; no extra terminology; under 150 words |
| Expected output format | three numbered points in plain English |

**What changed:** The audience was defined precisely — same subject, very different output for a biology student versus a 12-year-old. The scope was limited to exactly three conceptual points. Advanced content was explicitly excluded. A word limit was set. The AI now has no room to expand beyond what was asked [3].

---

### Domain 4 — Food

Food tasks include recipe generation, meal planning, and ingredient substitution. The word "healthy" is one of the most common sources of vague food specs — it means different things to different people.

- "Bounded" in food means: dietary requirements (vegetarian, nut-free, low-sodium), serving size, preparation time, and ingredient source.
- "Observable" in food means: a recipe with an ingredients list and numbered steps, a shopping list, or a meal plan table — not a discussion of nutrition.

**Weak specification:**
> "Give me a healthy dinner recipe."

**Strong specification:**
> "Generate one dinner recipe that: (1) is vegetarian with no nuts, (2) serves two people, (3) takes no more than 30 minutes to prepare and cook, (4) uses only ingredients commonly found in a UK supermarket. Write the recipe as a numbered list of steps. Include a separate ingredients list at the top with quantities. Do not include a nutritional breakdown."

| Part | What it provides |
|---|---|
| Task statement | "Generate one dinner recipe" |
| Context | "vegetarian, no nuts, serves two, UK supermarket ingredients" |
| Constraints | 30 minutes max; no nuts; one recipe only; no nutritional breakdown |
| Expected output format | ingredients list first, then numbered steps |

**What changed:** "Healthy" was replaced with measurable criteria (vegetarian, no nuts, 30-minute limit). The serving size was fixed. The ingredient source was bounded to a specific context — this prevents the AI from suggesting exotic items that are hard to find. The explicit exclusion of the nutritional breakdown stops the output from expanding beyond what is needed [2].

---

### Domain 5 — Scheduling

Scheduling tasks organise time: timetables, task allocation, meeting slots, to-do prioritisation. The common failure is giving the AI the task name without the time information it needs to produce anything usable.

- "Bounded" in scheduling means: the time window, each task with its duration, fixed commitments already in the calendar, and the deadline.
- "Observable" in scheduling means: a timetable, a calendar block list, or a prioritised task table — not a general recommendation about time management.

**Weak specification:**
> "Help me plan my week."

**Strong specification:**
> "I have the following five tasks to complete before Friday 5pm: (A) write a 500-word report — 2 hours; (B) respond to 10 emails — 1 hour; (C) prepare a 10-slide presentation — 3 hours; (D) attend a 1-hour team meeting on Wednesday at 14:00 (fixed); (E) review a contract document — 1.5 hours. I work 09:00–17:00 Monday to Friday with a 1-hour lunch break each day. Create a day-by-day schedule that fits all five tasks into my available working hours. Present it as a table with columns: Day, Time slot, Task."

| Part | What it provides |
|---|---|
| Task statement | "Create a day-by-day schedule" |
| Context | "five named tasks with durations, Mon–Fri 09:00–17:00, 1-hour lunch, deadline Friday 17:00" |
| Constraints | all five tasks must fit; 1-hour lunch each day; meeting D is fixed Wednesday 14:00 |
| Expected output format | table with columns: Day, Time slot, Task |

**What changed:** Every task was named and given a duration. Working hours and lunch were defined. A hard deadline was set. A fixed event was identified so the AI knows it cannot move it. The table format makes the schedule directly usable. The AI now has a complete picture of the constraints and can produce a concrete, checkable result [1].

---

### What Stays the Same — and What Changes

After reading the five examples above, the pattern becomes clear.

**What does not change across domains:**

- The four-part structure (task statement, context, constraints, expected output format) appears in every domain.
- A strong spec always replaces vague quality words — "healthy," "best," "appropriate," "fast" — with measurable, domain-specific criteria.
- A strong spec always names a concrete output format so you know exactly what you will receive.

**What does change across domains:**

| Domain | What "bounded" means here | What "observable" means here |
|---|---|---|
| Health | Which metric, which time range | A reported list or table of data points |
| Transport | Origin, destination, date/time, mode, number of options | A route or comparison table |
| Education | Audience level, subject scope, excluded content | A numbered explanation, a set of questions |
| Food | Dietary restrictions, serving size, prep time, ingredient source | An ingredients list + numbered steps |
| Scheduling | Time window, task durations, fixed commitments, deadline | A timetable or calendar table |

A useful habit: after writing a spec in any domain, ask "What could go wrong if I left one of my constraints vague?" That question turns a reasonable spec into a strong one [3].

## Worked Example

Here is the four-part process applied step by step to a scheduling task — the same process works for any domain.

**Situation:** You have three pieces of work to finish by end of day Thursday, and you are free 10:00–16:00 Tuesday and Wednesday.

**Step 1 — Write the task statement.**
Name the action and the subject. "Create a time-block schedule for three tasks."

**Step 2 — Add domain context.**
Answer: "What background does the AI need to produce the right result for *my* situation?"
- Tasks: (A) draft a project proposal — 2 hours; (B) read 30 pages of a report — 1.5 hours; (C) write 10 follow-up emails — 1 hour.
- Available time: Tuesday 10:00–16:00 and Wednesday 10:00–16:00 (both days have a 30-minute break at 12:30).
- Deadline: Thursday end of day.

**Step 3 — Add constraints.**
"All three tasks must be scheduled. Each block must be at least 30 minutes (no splitting into tiny fragments). Do not schedule anything during the 12:30–13:00 break."

**Step 4 — Specify the output format.**
"Present the schedule as a table with columns: Day, Time slot, Task, Duration."

**Full specification:**
> "Create a time-block schedule for three tasks. Available time: Tuesday 10:00–16:00 and Wednesday 10:00–16:00 (30-minute break at 12:30 each day). Tasks: (A) draft a project proposal — 2 hours; (B) read 30 pages of a report — 1.5 hours; (C) write 10 follow-up emails — 1 hour. All three tasks must be scheduled. Do not split any task into blocks shorter than 30 minutes. Do not schedule during the 12:30–13:00 break. Present the result as a table: Day, Time slot, Task, Duration."

**Quick four-property check:**
- [x] **Testable** — you can check every task against the table and verify it fits within the stated hours.
- [x] **Bounded** — two specific days, named time windows, named tasks with durations, one explicit exclusion.
- [x] **Observable** — the output is a table you can read immediately.
- [x] **Actionable** — the AI has everything it needs; no follow-up questions required [1].

## In Practice

**Common anti-patterns and fixes:**

| Domain | Weak phrase | Why it fails | Stronger replacement |
|---|---|---|---|
| Health | "tell me if my results are normal" | Asks for medical judgment | "report the value and whether it is above or below the stated reference range" |
| Transport | "find me the best route" | "best" is undefined | "find the route with the fewest changes that arrives before 09:00" |
| Education | "make it age-appropriate" | Age not specified | "write for an 11-year-old with no prior knowledge of the topic" |
| Food | "make it healthy" | "healthy" is not measurable | "keep total calories under 600 and include at least 25g of protein" |
| Scheduling | "fit it into my schedule" | No schedule information given | "I am free 09:00–12:00 Mon–Fri; allocate all five tasks within those windows" |

**Three habits that improve every spec regardless of domain:**

1. **Include at least one explicit exclusion.** Naming one thing the AI should not do ("do not give health advice", "do not include a nutritional breakdown") eliminates a large proportion of out-of-scope outputs [2].
2. **Name the output format before you finish writing.** If you cannot name a concrete object — a table, a numbered list, a set of sentences — your spec is not observable yet.
3. **Do not assume the AI knows your local context.** Your city, your dietary rules, your organisation's calendar format — state all of it explicitly. The AI will default to common global assumptions if you do not [3].

Professional frameworks from MIT Sloan, Harvard HUIT, and Atlassian all describe versions of the same four-part structure used in this reading — the pattern holds across beginner practice and professional AI workflows alike [1][2][3].

## Key Takeaways

- Every domain — health, transport, education, food, scheduling — uses the same four-part structure: task statement, context, constraints, and expected output format.
- What changes across domains is the *type* of constraint that makes a spec bounded and the *type* of output that makes it observable — the principle is constant; the detail is domain-specific.
- A strong specification always replaces vague quality words ("healthy," "best," "appropriate") with measurable, domain-specific criteria.
- Including at least one explicit exclusion ("do not include X") in every specification is the single most effective habit for reducing out-of-scope AI output.
- After writing any spec, run the four-property check: testable, bounded, observable, actionable — if any box is unchecked, identify which of the four parts is missing the needed information and add it.

## References

1. MIT Sloan Educational Technology. "How to Write Effective AI Prompts." MIT Sloan EdTech, https://mitsloanedtech.mit.edu/ai/basics/effective-prompts/
2. Harvard University Information Technology. "Getting Started with AI Prompts." Harvard HUIT, https://www.huit.harvard.edu/news/ai-prompts
3. Atlassian. "The Ultimate Guide to Writing AI Prompts." Atlassian Blog, https://www.atlassian.com/blog/artificial-intelligence/ultimate-guide-writing-ai-prompts

---
<!-- nav:bottom:start -->
[⬅ Previous: 2.6 — When NOT to use AI](../../../3-the-professional-rules-of-ai-use/2-6-when-not-to-use-ai-privacy-precision-legal-accountability/artifacts/reading.md)&emsp;·&emsp;[⬆ Table of Contents](../../../../../../../README.md#curriculum-topic-index)&emsp;·&emsp;[Next: 2.8 — Testing a specification ➡](../../2-8-testing-a-specification-how-to-verify-the-ai-did-exactly-wha/artifacts/reading.md)
<!-- nav:bottom:end -->
