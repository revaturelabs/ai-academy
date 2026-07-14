---
topic_id: "2.7"
title: "Writing specifications across five domains — health, transport, education, food, scheduling"
position_in_module: 1
generated_at: "2026-06-17T00:00:00Z"
resource_count: 3
---

# 1. Writing Specifications Across Five Domains — Health, Transport, Education, Food, Scheduling — Topic Corpus

## 2. Prerequisites

This topic applies concepts introduced in earlier topics this week:

- **2.1 What makes a good specification — testable, bounded, observable** — the four properties (testable, bounded, observable, actionable) that every specification must have.
- **2.2 Bad spec vs good spec — make it better vs rewrite** — practice identifying vague language and rewriting it into a constrained, precise instruction.
- **2.3 How to identify the inputs, expected outputs, and failure conditions** — the three-part template: what goes in, what comes out, and what counts as a failure.
- **2.5 The 70/30 rule — AI implements, you specify and verify** — the accountability split: you write the spec and verify the result; AI does the implementation.

No programming knowledge is needed. All examples in this topic use everyday situations.

## 3. Learning Objectives

By the end of this topic you will be able to:

- Apply the specification template (task statement + context + constraints + expected output format) to a task in any of the five domains: health, transport, education, food, and scheduling.
- Identify what "bounded" and "observable" mean differently in each domain.
- Write a good specification and a weak specification for the same task, and explain the specific gap the weak version leaves.
- Recognise the shared four-part structure that appears across all five domains.
- Connect each domain example to the Specification Portfolio assessment (A1) you will submit in Week 3.

## 4. Introduction

You have spent this week learning what makes a specification good: testable, bounded, observable, and actionable. You have practised spotting vague language and rewriting it. Now comes the part that actually matters — writing real specifications for real tasks you might do with AI.

Here is the truth: the principles do not change from domain to domain. A good specification for a health task looks structurally identical to a good specification for a scheduling task. What *does* change is what counts as "bounded" and what counts as "observable" in each context. A word-count limit bounds a writing task. A time window bounds a scheduling task. A numerical threshold bounds a health metric. The principle is the same; the detail is domain-specific [1].

This topic walks through five domains: health, transport, education, food, and scheduling. For each one, you will see a weak specification, a strong specification, and an annotation explaining exactly what changed. These five domains are also the exact scope of the Specification Portfolio (Assessment A1, due Week 3, worth 10%). By the end of this topic, you will have seen at least one worked example per domain — your portfolio task is to write your own [2].

## 5. Core Concepts

### 5.1 The Shared Four-Part Structure

Every strong specification — regardless of domain — contains four parts. You met these parts in topics 2.1–2.3. Here they are gathered into one reusable template [1]:

| Part | What it does | Example signal words |
|---|---|---|
| **Task statement** | Names the action and the subject | "Summarise…", "Generate…", "List…", "Identify…" |
| **Context** | Provides the background the AI needs to act correctly | "for a 10-year-old", "using only the attached timetable", "based on a 1500-calorie daily budget" |
| **Constraints** | Sets the fences — what is in, what is out, how long, what format | "no more than 3 items", "do not include X", "use a numbered list" |
| **Expected output format** | Describes what you will actually receive | "a table with columns A and B", "a plain-English paragraph", "a bullet list" |

When you write a specification in any domain, check that all four parts are present. If any part is missing, the AI will fill the gap with a guess [3].

The four-part structure maps directly onto the properties you learned earlier:
- Task statement + context → **actionable** (the AI has enough to start)
- Constraints → **bounded** (the fences are explicit)
- Expected output format → **observable** (you know what you will receive)
- All four parts together → **testable** (you can check the result against what you asked for)

---

### 5.2 Domain 1 — Health

Health tasks often involve personal information, numbers (weight, blood pressure, calories, medication doses), and time-sensitive decisions. A good specification in this domain must be precise about the metric being tracked, the time period, and the format of the output. "Bounded" here usually means limiting the metric, the date range, or the population. "Observable" means a concrete list, table, or summary — not general advice [1].

**Weak specification:**
> "Help me understand my health data."

What is wrong: "understand" is not observable — the AI cannot produce your understanding. There is no metric specified, no time range, no source of data mentioned. The AI will guess at all of these.

**Strong specification:**
> "I have a table of my daily step counts for the last 14 days (attached). Identify the three days with the lowest step counts. For each of those days, write one sentence stating the date and the count. Do not give health advice or suggest causes — just report the three data points."

| Part | What it provides |
|---|---|
| Task statement | "Identify the three days with the lowest step counts" |
| Context | "daily step counts for the last 14 days (attached)" |
| Constraints | "three days only", "one sentence per day", "no health advice, no suggested causes" |
| Expected output format | "three sentences, each stating date and count" |

**What changed:** The vague "understand" was replaced with a specific action (identify, report). The data source was named. The output was limited to three data points in a fixed sentence format. The constraint "do not give health advice" keeps the AI from overstepping into territory that requires professional judgment [2].

> **Reminder from topic 2.6.** Health decisions involving diagnosis or medication dosage are cases where AI should not be used without professional oversight. This specification avoids that risk by asking for data reporting only, not advice.

---

### 5.3 Domain 2 — Transport

Transport tasks often involve routes, times, distances, and comparison between options. "Bounded" in transport means fixing the journey (start point, end point, date/time, mode of travel). "Observable" means a concrete route, schedule, or comparison table — not a general discussion of travel options [3].

**Weak specification:**
> "Tell me how to get to the airport."

What is wrong: Which airport? From where? By what time? By what means — walking, driving, public transport? The AI will pick defaults that may not match your situation at all.

**Strong specification:**
> "I need to travel from Liverpool Street Station, London, to Heathrow Airport Terminal 2 on a weekday morning, arriving by 07:30. List the two fastest public transport options available with arrival by 07:30. For each option, state: the route name or number, the departure time from Liverpool Street, the arrival time at Terminal 2, and the number of changes required. Use a table with those four columns."

| Part | What it provides |
|---|---|
| Task statement | "List the two fastest public transport options" |
| Context | "Liverpool Street to Heathrow Terminal 2, weekday morning, arrive by 07:30" |
| Constraints | "two options only", "public transport only", "arrival by 07:30" |
| Expected output format | "a table: route name, departure time, arrival time, number of changes" |

**What changed:** The origin, destination, terminal, day type, and arrival deadline were all specified. The number of options was fixed at two. The output was shaped into a four-column table so you can compare results directly [1].

---

### 5.4 Domain 3 — Education

Education tasks involve teaching, explaining, assessing, or summarising learning content. "Bounded" in education means fixing the audience's age or knowledge level, the subject, the length of the output, and what should not be included (such as advanced concepts). "Observable" means a lesson plan, a set of questions, an explanation in plain text — not "an engaging lesson" (which is not observable) [2].

**Weak specification:**
> "Explain photosynthesis."

What is wrong: For whom — a 7-year-old or a biology student? In how much detail? Should it include the chemical formula? Should it use analogies? The AI will pick a default audience and depth that may not fit your context.

**Strong specification:**
> "Explain photosynthesis for a 12-year-old who has no prior science knowledge. Cover only these three points: (1) what photosynthesis is in one plain-English sentence, (2) what the plant needs as inputs (sunlight, water, carbon dioxide), and (3) what the plant produces (glucose and oxygen). Do not use chemical formulas or scientific terminology beyond these terms. Keep the total response under 150 words."

| Part | What it provides |
|---|---|
| Task statement | "Explain photosynthesis" |
| Context | "for a 12-year-old with no prior science knowledge" |
| Constraints | "three points only", "no formulas", "no extra terminology", "under 150 words" |
| Expected output format | "three numbered points in plain English" |

**What changed:** The audience was defined precisely. The scope was limited to exactly three conceptual points. Advanced content (chemical formulas) was explicitly excluded. A word limit was set. The AI now has no room to expand beyond what you asked for [3].

---

### 5.5 Domain 4 — Food

Food tasks include recipe generation, meal planning, nutritional analysis, and ingredient substitution. "Bounded" in food means fixing dietary requirements, ingredient availability, number of servings, preparation time, and any exclusions. "Observable" means a recipe, a shopping list, or a meal plan table — not a general discussion of nutrition [1].

**Weak specification:**
> "Give me a healthy dinner recipe."

What is wrong: "Healthy" means different things to different people (low-calorie? high-protein? low-sodium?). How many people? What ingredients are available? Any allergies or restrictions? The AI will default to a common interpretation that may not match your situation.

**Strong specification:**
> "Generate one dinner recipe that: (1) is vegetarian with no nuts, (2) serves two people, (3) takes no more than 30 minutes to prepare and cook, (4) uses only ingredients commonly found in a UK supermarket. Write the recipe as a numbered list of steps. Include a separate ingredients list at the top with quantities. Do not include a nutritional breakdown."

| Part | What it provides |
|---|---|
| Task statement | "Generate one dinner recipe" |
| Context | "vegetarian, no nuts, serves two, UK supermarket ingredients" |
| Constraints | "30 minutes max", "no nuts", "one recipe only", "no nutritional breakdown" |
| Expected output format | "ingredients list first, then numbered steps" |

**What changed:** Dietary restrictions were made explicit (vegetarian, no nuts). The serving size was fixed. A time constraint was set. The ingredient source was bounded to a specific context. The output format was specified precisely so there is no ambiguity about what you will receive [2].

---

### 5.6 Domain 5 — Scheduling

Scheduling tasks involve organising time: creating timetables, allocating tasks to time slots, finding available meeting times, or prioritising a to-do list. "Bounded" in scheduling means fixing the time window, the tasks involved with their durations, and any hard constraints (conflicts, priorities, breaks). "Observable" means a timetable, a calendar block list, or a prioritised task list — not a general recommendation about time management [3].

**Weak specification:**
> "Help me plan my week."

What is wrong: Which week? What tasks need to be scheduled? How many hours per day are available? Are there fixed commitments already in the calendar? The AI will make up a generic template that bears no relation to your actual situation.

**Strong specification:**
> "I have the following five tasks to complete before Friday 5pm: (A) write a 500-word report — 2 hours, (B) respond to 10 emails — 1 hour, (C) prepare a 10-slide presentation — 3 hours, (D) attend a 1-hour team meeting on Wednesday at 14:00 (fixed), (E) review a contract document — 1.5 hours. I work 09:00–17:00 Monday to Friday with a 1-hour lunch break each day. Create a day-by-day schedule that fits all five tasks into my available working hours. Present it as a table with columns: Day, Time slot, Task."

| Part | What it provides |
|---|---|
| Task statement | "Create a day-by-day schedule" |
| Context | "five named tasks with durations, Mon–Fri 09:00–17:00, 1-hour lunch, deadline Friday 17:00" |
| Constraints | "all five tasks must fit", "1-hour lunch each day", "meeting D is fixed Wednesday 14:00" |
| Expected output format | "table: Day, Time slot, Task" |

**What changed:** Every task was named and given a duration. Working hours and lunch were defined. A hard deadline was set. A fixed event (the meeting) was identified. The output was shaped into a table with named columns. The AI now has a complete picture of the constraints and can produce a concrete, checkable schedule [1].

---

### 5.7 What Changes Across Domains — and What Does Not

Reading the five examples above, you will notice a pattern.

**What does not change:**
- The four-part structure (task statement, context, constraints, expected output format) appears in every domain.
- A strong spec always replaces vague quality words ("healthy", "good", "fast") with measurable criteria.
- A strong spec always names a concrete output format so you know what you will receive.

**What does change:**
- The *type* of constraint that makes a spec "bounded" is domain-specific. In health, it is the metric and the time range. In transport, it is the journey endpoints and the arrival time. In education, it is the audience level and the excluded content. In food, it is dietary restrictions and serving size. In scheduling, it is the time window and the fixed commitments.
- The *type* of failure that matters most is also domain-specific. A health spec that asks for advice could produce unsafe output. A scheduling spec without a deadline could produce a plan that ignores urgency. Knowing the domain helps you anticipate what failure looks like [2].

This is why a useful habit is to ask after writing a spec: "In this domain, what could go wrong if I left this constraint vague?" That question is what turns a reasonable spec into a strong one [3].

## 6. Implementation

Use this four-part process each time you write a specification for any domain:

1. **Write the task statement.** Name the action (generate, identify, list, explain, create) and the subject. Be specific about what kind of output you want. Bad: "help me with food." Better: "generate a shopping list."

2. **Add domain context.** Ask: "What background does the AI need to produce the right result for *my* situation?" In health: the metric, the data source, the time range. In transport: origin, destination, date/time, mode. In education: audience age and knowledge level, the subject, the purpose. In food: dietary requirements, servings, available ingredients. In scheduling: time window, tasks with durations, fixed commitments.

3. **Add constraints.** Ask: "What is in scope? What is out? What limits apply?" Set a limit on length, number of items, time, or detail. Name at least one thing the AI should *not* do or include. Pick an output format.

4. **Check the output description.** Ask: "What will I actually receive — and can I check it?" If the answer is vague ("something useful"), rewrite it as a concrete object: a table, a numbered list, a set of sentences, a schedule.

After completing all four steps, run the quick four-property check:

- [ ] **Testable** — I can check the output against what I asked for.
- [ ] **Bounded** — Scope, format, and limits are explicit.
- [ ] **Observable** — The output is a concrete thing I can read or count.
- [ ] **Actionable** — The AI has everything it needs; no follow-up questions needed.

If any checkbox is unchecked, identify which part (task statement, context, constraints, or output format) is missing the needed information, and add it [1].

## 7. Real-World Patterns

The four-part structure you are practising here is the same structure used by professionals who write specifications for AI systems at scale.

MIT Sloan's framework for writing effective AI prompts is built on four components that map directly onto the template above: the task, the context, the format, and the constraints [1]. Harvard HUIT's guide for institutional AI use emphasises giving the AI explicit context and format instructions so the output is usable in professional workflows — not just "an answer" [2]. Atlassian's practitioner guide documents how teams writing specifications for AI-assisted workflows apply domain-specific constraints to scheduling, documentation, and communication tasks [3].

In each of these professional contexts, the pattern is the same: vague instructions produce inconsistent results; structured, domain-aware specifications produce reliable ones. The five domains covered in this topic represent a cross-section of the kinds of tasks people bring to AI tools in everyday professional and personal life.

## 8. Best Practices

**Do:**
- Use the four-part template as a checklist before every specification you write.
- Name the output format explicitly — table, numbered list, paragraph, schedule — so you can recognise immediately whether what you received is what you asked for.
- Include at least one explicit exclusion in every specification ("do not include X"). This single habit eliminates a large proportion of out-of-scope outputs.
- In health contexts, add "do not give advice" or "do not make recommendations" unless advice from a professional tool is explicitly appropriate [2].

**Do not:**
- Use domain-specific jargon in your specification without defining it. A specification that says "use the GI index" assumes the AI will interpret that term correctly — which it may or may not do.
- Assume the AI knows your local context (your city, your dietary rules, your organisation's calendar format). State it explicitly.
- Write one specification and assume it will work perfectly for every similar task in that domain. The context part of the template changes every time the situation changes [3].

**Common domain-specific anti-patterns:**

| Domain | Weak phrase | Problem | Better alternative |
|---|---|---|---|
| Health | "tell me if my results are normal" | Asks for medical judgment | "report the value and whether it is above or below the stated reference range" |
| Transport | "find me the best route" | "best" is not defined | "find the route with the fewest changes that arrives before 09:00" |
| Education | "make it age-appropriate" | Age not specified | "write for an 11-year-old with no prior knowledge of the topic" |
| Food | "make it healthy" | "healthy" is not measurable | "keep total calories under 600 and include at least 25g of protein" |
| Scheduling | "fit it into my schedule" | No schedule information provided | "I am free 09:00–12:00 Mon–Fri; allocate all five tasks within those windows" |

## 9. Hands-On Exercise

Choose one domain from the five covered in this topic — pick the one that feels most relevant to your own life or studies. Write a weak specification for a task in that domain (one sentence, deliberately vague). Then apply the four-part process from Section 6 to turn it into a strong specification. Write down each of the four parts separately (task statement, context, constraints, output format) and then combine them. Compare your strong spec to the worked example for that domain in Section 5. Identify one thing you did the same and one thing you would do differently after seeing the example. This mirrors exactly what you will do for Assessment A1.

## 10. Key Takeaways

- Every domain — health, transport, education, food, scheduling — uses the same four-part structure: task statement, context, constraints, and expected output format.
- What changes across domains is the *type* of constraint that makes a specification "bounded" and the *type* of output that makes it "observable" — the principle is constant, the detail is domain-specific.
- A strong specification always replaces vague quality words ("healthy", "best", "appropriate") with measurable, domain-specific criteria.
- Including at least one explicit exclusion ("do not include X") in every specification dramatically reduces out-of-scope AI output.
- The five domains covered here — health, transport, education, food, scheduling — are the exact scope of Assessment A1, the Specification Portfolio, due in Week 3.

## 11. Next Steps

_System-derived from the next entry in curriculum/sequence.md._
