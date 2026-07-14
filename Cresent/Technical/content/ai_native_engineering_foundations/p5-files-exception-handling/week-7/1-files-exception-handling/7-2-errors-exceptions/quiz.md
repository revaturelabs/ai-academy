$CATEGORY: CIT/ai_native_engineering_foundations/week-7/7.2-errors-exceptions

::q1:: Which statement best distinguishes a syntax error from an exception in Python? {
~Both are reported before the program runs; the difference is only in the wording of the message Python prints to the screen.
=A syntax error is caught before the program runs and is fixed by editing code; an exception is a runtime event you can plan for and handle.#Correct — syntax errors are write-time bugs; exceptions occur while valid code is executing (corpus §5, Key Takeaways).
~An exception is caught before the program runs, while a syntax error only appears later while the program is actively executing.#No — this reverses the two; syntax errors are the ones caught before running.
~A syntax error can always be handled with try/except, whereas an exception must be fixed by editing the source code first.#No — try/except handles exceptions, not syntax errors; this swaps their remedies.
#### Tests the syntax-error vs exception distinction (corpus §5, "Errors vs exceptions").
}

::q2:: Given the hierarchy where IndexError and KeyError both inherit from LookupError, what does `except LookupError:` catch? {
~Only KeyError, because dictionary lookups are the canonical form of a lookup failure in Python.#No — LookupError is the parent of both; it is not limited to dict lookups.
~Neither one, because you must name IndexError and KeyError explicitly to catch either of them.#No — catching a parent class also catches its children automatically.
=Both IndexError and KeyError, because catching a parent class also catches all of its child classes.#Correct — LookupError is the parent of IndexError and KeyError (corpus §5, "The exception hierarchy").
~Only IndexError, because list indexing errors are more specific than dictionary key errors in the tree.#No — both are children of LookupError, so both are caught.
#### Tests catch-parent-catches-children with the LookupError family (corpus §5).
}

::q3:: In a basic `try` / `except ValueError:` block wrapping `int(input(...))`, what happens when the user types `hello`? {
=int() raises a ValueError, Python skips the rest of the try, and the except block runs so the program keeps going.#Correct — the exception diverts execution to the matching except and the program does not crash (corpus §5, "Handling exceptions").
~The program crashes immediately with a traceback because ValueError cannot be caught by a try/except statement.#No — that is exactly the error this except block catches; the program does not crash.
~The try block finishes normally and the except is skipped, since int() converts any input into a number.#No — int("hello") cannot convert non-numeric text, so it raises rather than succeeding.
~Python re-runs the try block repeatedly until the user finally enters a value that converts successfully.#No — try/except does not loop; it runs the except once and moves on.
#### Tests basic try/except catch behavior (corpus §5, "Handling exceptions: try / except").
}

::q4:: In a `try` statement with both `else` and `finally` clauses, when does each clause run? {
~else runs whether or not an exception occurred, and finally runs only when the try block raised no exception at all.#No — this swaps them; else is success-only and finally is unconditional.
~else runs only when an exception was caught, and finally runs only when no exception was ever raised in the try.#No — else is the success path, not the error path; finally always runs.
~Both else and finally run only when the try block completes with no exception; neither runs if an error occurred.#No — finally runs in every case, including when an error occurred.
=else runs only if the try finished with no exception, and finally runs no matter what happened.#Correct — else is the success-only path; finally is guaranteed cleanup (corpus §5, "else and finally").
#### Tests else vs finally semantics (corpus §5, "else and finally").
}

::q5:: A single `try` has several `except` blocks. When more than one could match a raised exception, which one runs? {
~The most specific matching block, since Python scans every except and picks the narrowest exception type.#No — Python does not search for the narrowest; it stops at the first textual match.
~The last matching block, because Python evaluates all except clauses and keeps the final one that matches.#No — matching stops at the first hit, not the last.
=The first matching block in top-to-bottom order, because Python stops at the first except that matches.#Correct — Python checks top to bottom and runs the first match (corpus §5, "Handling multiple exceptions").
~All matching blocks run in sequence, so several except bodies can execute for one raised exception.#No — only one except body runs per raised exception.
#### Tests multiple-except first-match-wins rule (corpus §5, "Handling multiple exceptions").
}

::q6:: Why must more specific exceptions be ordered before their parent classes in a chain of `except` blocks? {
=Because the first match wins, a broad parent listed first would catch the child, so the child block could never run.#Correct — a parent placed above its child shadows it since matching stops at the first hit (corpus §5, Best Practices).
~Because Python raises a SyntaxError at import time if any parent exception is written above one of its own child classes.#No — the ordering compiles fine; the child block is simply unreachable, not a syntax error.
~Because parent classes run slower than child classes, so listing children first is purely a performance optimization.#No — this is about reachability from first-match, not speed.
~Because child exceptions must always be caught before the program starts, while parents are only checked at runtime.#No — all except matching happens at runtime; there is no pre-run ordering rule like this.
#### Tests specific-to-general ordering rationale (corpus §5 and Best Practices).
}

::q7:: What does the grouped clause `except (IndexError, ValueError):` do? {
~It catches an error only if IndexError and ValueError are raised together at the same time in the try block.#No — the tuple is an OR, not an AND; either one alone triggers the block.
~It creates a brand-new exception type named after both classes that must be raised explicitly with raise.#No — the tuple groups existing types for one handler; it defines nothing new.
~It catches IndexError but silently ignores ValueError, because only the first type listed in the tuple is active.#No — every type in the tuple is caught, not just the first.
=It runs the same except body when either an IndexError or a ValueError is raised, giving both the one response.#Correct — a tuple of types gives several errors one shared handler (corpus §5, "Handling multiple exceptions").
#### Tests grouped except (A, B) semantics (corpus §5).
}

::q8:: Which pairing correctly describes the difference between ValueError and TypeError? {
~TypeError means right type but wrong value, while ValueError means an operation received a value of the wrong type.#No — this reverses the two definitions.
=ValueError means right type but wrong value, e.g. int("cat"); TypeError means wrong type entirely, e.g. len(5).#Correct — ValueError is right-type/wrong-content; TypeError is wrong-type (corpus §5, "Common built-in exceptions").
~Both mean the value had the wrong type, so int("cat") and len(5) raise exactly the same exception class.#No — int("cat") is ValueError and len(5) is TypeError; they are distinct.
~ValueError is raised only for numbers and TypeError only for strings, regardless of the operation involved.#No — neither is tied to a single data type; the distinction is type vs value.
#### Tests ValueError vs TypeError distinction (corpus §5, "Common built-in exceptions").
}

::q9:: You call `record["units"]` on a dictionary that has no `"units"` key. Which exception is raised? {
~IndexError, because Python treats the missing dictionary entry the same as indexing past the end of a list.#No — dictionaries raise KeyError; IndexError is for out-of-range sequence indexes.
~AttributeError, because the dictionary object is missing the units attribute the code tried to read.#No — bracket key access raises KeyError, not AttributeError.
~ValueError, because "units" is a valid type of key but simply holds no acceptable value yet.#No — a missing key is a lookup failure (KeyError), not a value-content problem.
=KeyError, because you looked up a dictionary key that does not exist in that dictionary.#Correct — missing dict key raises KeyError (corpus §5, "Common built-in exceptions").
#### Tests KeyError trigger (corpus §5).
}

::q10:: In modern Python, what is the relationship between `IOError` and `OSError`? {
=IOError is an alias for OSError, the same family that FileNotFoundError belongs to.#Correct — IOError is an alias for OSError, and FileNotFoundError is an OSError subclass (corpus §5, "Common built-in exceptions").
~IOError is the parent of OSError, so catching IOError will also catch every OSError raised.#No — they are the same class via alias, not a parent-child pair in that direction.
~IOError and OSError are unrelated classes, so a handler for one will never catch the other.#No — they are aliases of one another, so either name catches the same errors.
~IOError is a subclass of ValueError used specifically for reporting bad file content during reads.#No — IOError relates to I/O failures and aliases OSError, not ValueError.
#### Tests the IOError = OSError alias relationship (corpus §5).
}

::q11:: What does the `raise` statement do in `raise ValueError("age cannot be negative")`? {
~It catches any ValueError already in flight and replaces its message with the friendlier text supplied here.#No — raise signals a new exception; it does not catch or edit one already being handled.
=It signals an error from your own code, stopping execution and raising a ValueError a caller can catch.#Correct — raise lets your code signal bad data, catchable like a built-in (corpus §5, "Raising exceptions").
~It permanently disables ValueError for the rest of the program so negative ages pass through silently.#No — raise triggers the error; it does not turn a type off.
~It logs the message to the console as a warning but lets the function continue running normally afterward.#No — raise halts the normal flow and propagates the exception, it is not a warning.
#### Tests the raise statement (corpus §5, "Raising exceptions").
}

::q12:: What is the minimum needed to define a custom exception like `InvalidRecordError`? {
~Register the new class with Python's exception system by calling a special sys function before raising it.#No — no registration call is needed; subclassing Exception is sufficient.
~Override the built-in __raise__ method so Python knows how to propagate the new exception type correctly.#No — there is no such requirement; inheriting from Exception provides all the behavior.
=Define a class that inherits from Exception; its body can be as little as a docstring.#Correct — a custom exception is just a class subclassing Exception (corpus §5, "Custom exceptions").
~Define a function decorated with @exception that returns the error message string when it is called.#No — custom exceptions are classes subclassing Exception, not decorated functions.
#### Tests custom-exception definition by subclassing Exception (corpus §5, "Custom exceptions").
}

::q13:: The clause of a try statement that runs no matter what — whether an exception happened, was caught, or was not raised — is the ____ clause (one word). {
=finally
=Finally
}
