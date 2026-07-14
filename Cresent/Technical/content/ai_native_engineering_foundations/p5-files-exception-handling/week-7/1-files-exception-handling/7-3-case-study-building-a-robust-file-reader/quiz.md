# Quiz — 7.3 Case Study: Building a Robust File Reader

$CATEGORY: CIT/ai-native-engineering-foundations/week-7/7.3-case-study-building-a-robust-file-reader

::q1:: A "robust" file reader is best described as one that ... {
~stops at the first bad row so no corrupted data is ever processed at all#No — that is the fragile all-or-nothing behavior a robust reader is meant to avoid.
=processes every row it can, sets aside the ones it cannot, and keeps going#Correct — robust means keep going: skip-and-log the bad rows and finish the file.
~reads only the rows it is certain are perfect and ignores the rest quietly#No — ignoring the rest quietly loses data without any record of why.
~loads the whole file into memory first and then decides whether to run#No — robustness is about surviving bad rows, not about how much is buffered.
#### Tests the definition of a robust reader vs a fragile one (corpus 5, Key Takeaways).
}

::q2:: Why is skipping-and-logging preferred over crashing on the first bad row in a real data file? {
~because crashing is measurably slower than logging and the batch job must still finish quickly#No — the concern is data loss and reporting, not raw execution speed.
~because the standard library strictly forbids letting an exception propagate out of a read loop#No — nothing forbids it; propagating is exactly the fragile behavior we choose to avoid.
~because an uncaught crash always corrupts the very input data file that the reader was reading from#No — reading does not corrupt the source; the issue is losing the good rows already read.
=because the fault is in the data, so one bad row should not discard good rows#Correct — the fault is in the data, and keep-going preserves the good rows and reports the bad.
#### Tests why keep-going beats fragile all-or-nothing (corpus 5, Introduction).
}

::q3:: To isolate one bad row from the rest, where should the `try`/`except` be placed? {
=inside the `for` loop, wrapping the processing of each individual row#Correct — a per-row try/except sends a failure to that iteration's handler and the loop continues.
~around the entire `for` loop, so the loop is wrapped from the outside#No — the first bad row would break out of the whole loop, losing every remaining row.
~around the `with open(...)` block only, so the file is guarded as a unit#No — that guards opening the file, not the per-row processing where bad data surfaces.
~around the `return` statement, so the caller receives a safe result#No — by return time the loop is over; the guard must sit where each row is processed.
#### Tests correct placement of the per-row guard (corpus 5, Best Practices).
}

::q4:: What happens if you wrap the whole `for` loop from the outside instead of each row? {
~each bad row is silently skipped but the loop still finishes normally#No — that describes per-row handling; wrapping the outside does not skip and continue.
~Python retries the loop from the top each time a row raises an exception#No — there is no automatic retry; the exception breaks out of the loop.
=the first bad row breaks out of the loop and every remaining row is lost#Correct — the exception leaves the loop entirely, so later rows are never read.
~only the offending field is set to `None` and processing continues unaffected#No — that is `restval` behavior for short rows, not what loop placement does.
#### Tests the fragile-placement misconception (corpus 5, Per-row try/except).
}

::q5:: A CSV cell holds the text `thirty` in the `age` column. When does the problem surface? {
=when `int(row["age"])` runs and raises `ValueError`, because CSV values are strings#Correct — CSV reads everything as strings, so type errors appear at int() conversion.
~when `csv.DictReader` parses the line, which rejects any non-numeric field#No — DictReader does not type-check; it hands you the raw string `"thirty"`.
~when the file is opened, because `open()` validates numeric columns up front#No — `open()` performs no content validation of column values.
~never, because Python automatically converts `"thirty"` to a number on use#No — Python does not auto-convert; `int("thirty")` raises `ValueError`.
#### Tests that CSV values are strings and type errors surface at conversion (corpus 5, Validation).
}

::q6:: An `age` of `-5` is a valid integer but not a sensible age. How is this handled? {
~`int("-5")` raises `ValueError` on its own, so no extra check is needed#No — `int("-5")` succeeds; a negative integer is still a valid int.
~`csv.DictReader` flags the value because it falls outside the header's range#No — DictReader has no notion of allowed value ranges.
~the row is accepted, since any value that converts cleanly counts as valid#No — accepting it is exactly the bug; type-valid is not range-valid.
=your code checks the range and calls `raise ValueError("age out of range")` itself#Correct — a business-rule/range failure is something you raise yourself.
#### Tests raising your own ValueError for a range/business-rule failure (corpus 5, Validation).
}

::q7:: Which grouped `except` best fits the three failures `int()` on a non-number, a missing key, and `.lower()` on `None`? {
~`except Exception` — a single broad catch is the safest choice for any loop#No — an over-broad catch also hides real bugs in your own code.
=`except (ValueError, KeyError, AttributeError)` — one for each expected failure#Correct — ValueError from int(), KeyError for a missing column, AttributeError from .lower() on None.
~`except:` — a bare except guarantees the loop can never be interrupted#No — a bare except is discouraged; it swallows unexpected bugs too.
~`except (TypeError, IndexError)` — the standard pair for reading CSV rows#No — those are not the errors these three specific operations raise.
#### Tests naming the specific exceptions per-row processing can raise (corpus 6, Move 2).
}

::q8:: Why does a robust reader return two separate collections rather than one combined list? {
~because Python functions are only ever allowed to append to two separate lists at a time#No — there is no such limit; the split is a design choice, not a rule.
~because valid and invalid rows are automatically stored in two different files by the interpreter#No — the split is in memory, in your own lists; the interpreter does not do it.
=so downstream code can trust every valid record while a human reads the errors#Correct — separating them keeps clean data usable and rejects reportable, never mixed.
~because merging them into one list would roughly double the total memory used by the reader#No — the reason is correctness and clarity, not memory footprint.
#### Tests why valid and invalid records are kept separate (corpus 5, Separating valid from invalid).
}

::q9:: What is the risk of mixing valid and invalid rows into one list? {
~the combined list quickly grows too large for `csv.DictWriter` to ever write to disk#No — writer size is not the concern; the concern is data correctness.
~Python raises a `TypeError` the moment a single list is made to hold both good and bad dicts#No — a list can hold mixed dicts without error; nothing raises here.
~the error entries quietly lose their recorded line numbers the instant they join the valid rows#No — line numbers are lost only if you fail to record them, not by mixing.
=downstream code silently processes garbage, because it can no longer tell good rows from bad#Correct — mixing means callers can no longer trust each item and may process bad data.
#### Tests the mixing misconception (corpus 5, Separating valid from invalid).
}

::q10:: What does `enumerate(reader, start=2)` give you, and why start at 2? {
=a line number per row starting at 2, because line 1 was the header row#Correct — data begins on line 2, so error reports point at the real file line.
~a second copy of each row, so validation can compare the original to the clean one#No — enumerate yields a counter, not a duplicate of the row.
~a running total of valid rows, so the summary count is always accurate#No — enumerate counts iterations regardless of validity, not just valid rows.
~a two-row lookahead, so the loop can peek at the next row before deciding#No — enumerate provides no lookahead; it just pairs an index with each item.
#### Tests line-number tracking with enumerate (corpus 6, Move 2; Best Practices).
}

::q11:: In `people.csv`, the row `Kai,29` has no email value. What does `csv.DictReader` do? {
~it raises a `ValueError` immediately because this particular row simply has too few fields#No — a short row does not raise on its own; the field is quietly filled in.
~it skips the incomplete row automatically and then never even yields it to your loop#No — DictReader still yields the row; it does not silently drop short rows.
=it fills the missing `email` with `restval` (default `None`), which your validation must then catch#Correct — the short row leaves `email` as None, so the presence check is what rejects it.
~it copies the previous row's email value into the empty cell to keep the shape consistent#No — there is no carry-forward; missing values become `restval`, not the prior value.
#### Tests DictReader restval/short-row -> None behavior (corpus 5, DictReader and malformed rows).
}

::q12:: After splitting the data, how should the clean rows be written so downstream code sees only good data? {
~append the valid rows straight back onto the original `people.csv` so both piles live together#No — that re-mixes good and bad data in one file, defeating the split.
=write the valid list to a new CSV with `csv.DictWriter`, calling `writeheader()` then `writerows(valid)`#Correct — DictWriter produces a clean output file containing only the validated rows.
~print the valid rows straight to the screen, since a printed record surely counts as a saved file#No — printing is not persisting; downstream code needs an actual clean file.
~store the errors list to disk and then let downstream code filter out all the bad rows itself#No — that pushes the bad rows downstream, which the reader is meant to prevent.
#### Tests writing clean output with DictWriter (corpus 6, Move 4; Best Practices).
}

::q13:: The pattern where a reader rejects a bad row with a recorded reason and then continues to the next row is called the ____-and-____ pattern (two words). {
=skip-and-log
=skip and log
=skip/log
}

::q14:: A skipped row must always be recorded rather than dropped; the practice of never dropping a failure without writing it down is described as never failing ____ (one word). {
=silently
=silent
}
