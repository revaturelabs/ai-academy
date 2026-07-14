# Special Methods & Dataclasses

<sub>[&#8592; Previous: 6.2 Inheritance & Encapsulation](../../../../../../../content/ai_native_engineering_foundations/p4-classes-objects/week-6/1-classes-objects/6-2-inheritance-encapsulation/artifacts/reading.md)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Go back to TOC](../../../../../../../README.md)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Next: 7.1 File Handling &#8594;](../../../../../../../content/ai_native_engineering_foundations/p5-files-exception-handling/week-7/1-files-exception-handling/7-1-file-handling/reading.md)</sub>

---

## Overview

Every `describe()` method you've written so far exists because Python has no built-in idea how to print a `Task` or compare two `Person` objects meaningfully — `print(t1)` shows a bare memory address, and `t1 == t2` is `False` even when every attribute matches. This topic replaces those hand-rolled workarounds with the formal mechanism Python itself calls automatically: special methods like `__repr__`, `__str__`, and `__eq__`, applied to the same `Task`, `RegulatoryTask`, and `Person` classes built in the prior two topics. It then introduces `@dataclass`, a decorator that generates those same methods for you once a class settles into being mostly a bundle of attributes, and closes with where classes actually live once a program outgrows a single file. _This contributes to A3 — Python Foundations Diagnostic (due W8), by making sure your classes print, compare, and organize the way the diagnostic expects._

## Key Concepts

**Special methods and the data model.** A special method (or "dunder" method, for double underscore) is a method whose name begins and ends with `__` — `__init__`, `__str__`, `__repr__`, `__eq__` — that Python calls implicitly in response to a built-in operation, rather than you calling it by name. `__init__` already works this way: writing `Task(...)` calls it for you. The full set of these methods, and the rules for when each fires, is documented as Python's data model [1]. `mark_complete()` is not a special method — you call it explicitly; `print(t1)` and `t1 == t2`, by contrast, trigger `__str__`/`__repr__` and `__eq__` without you ever writing `t1.__eq__(t2)` directly.

**`__repr__` and `__str__`: controlling how an object prints.** Every object has a default string form inherited from `object`, the base class every class ultimately extends — that's the source of `<__main__.Task object at 0x7f2b...>`, and it's deliberately unhelpful [1]. `__repr__` is the special method for an object's unambiguous, developer-facing representation, conventionally shaped like the code that would recreate the object: `ClassName(field=value, ...)` [1][3]. Using `!r` inside an f-string placeholder (`{self.name!r}`) calls `repr()` on that value instead of `str()`, which is why string fields show quote marks. `__str__` is the human-readable, user-facing form; `print()`, `str()`, and f-strings prefer `__str__` over `__repr__` when both exist [1][3]. Crucially, `object`'s own default `__str__` simply calls `self.__repr__()` — so a class with `__repr__` but no `__str__` still prints something useful through that fallback. Only when both are defined does `print()` choose the friendlier one.

**`__eq__`: value-based equality.** By default, `==` between instances of a custom class behaves exactly like `is` — it checks whether two names refer to the same object in memory, inherited from `object`, the same base class responsible for the default `__repr__` [1]. `__eq__` is the special method `==` calls, and defining it lets you decide what "equal" means: typically, same class and every attribute that matters holds the same value. The body is a single boolean expression chained with `and`:

```python
def __eq__(self, other):
    return (isinstance(other, Task)
            and self.name == other.name
            and self.priority == other.priority
            and self.done == other.done)
```

`and` short-circuits — it evaluates left to right and stops at the first `False` — so `isinstance(other, Task)` goes first: if `other` isn't a `Task` at all, the expression returns `False` immediately without ever touching `other.name`, which might not exist [1]. A subclass like `RegulatoryTask` inherits `Task`'s `__eq__` automatically, but that inherited version never compares `regulation_code` unless `RegulatoryTask` overrides it, extending the parent check with `super().__eq__(other)` the same way `describe()` was extended in the prior topic.

**`@dataclass`: reducing boilerplate.** Once a class is mostly `self.attribute = attribute` assignments, with `__repr__` and `__eq__` that just mechanically list the same attributes, writing all of it by hand invites typos and missed-attribute bugs. The `dataclasses` module's `@dataclass` decorator generates `__init__`, `__repr__`, and `__eq__` from a short list of field declarations — name, type annotation, optional default — written directly in the class body [2]:

```python
from dataclasses import dataclass

@dataclass
class Task:
    name: str
    priority: str
    done: bool = False
```

From those three lines, `@dataclass` builds an `__init__` taking `name` and `priority` as required positional parameters and `done` as optional (defaulting to `False`), a `__repr__` in the same `ClassName(field=value, ...)` shape, and an `__eq__` comparing every field in declaration order [2]. `done: bool = False` is the one place in this course where a default value in a signature is the actual mechanism being taught — it's a property of the field declaration, not a general license to add defaults to ordinary methods, which still take required positional parameters only. That default comes with a firm ordering rule, stated explicitly in the documentation: once a field has a default, every field declared after it must also have one — a required field cannot follow an optional one [2], because the generated `__init__` places fields as parameters in declaration order, and a required parameter cannot legally follow an optional one in the same signature.

A dataclass is still an ordinary class: you can add plain methods to it, and inheritance works the same as always. One nuance worth noting — `@dataclass` generates `__repr__` and `__eq__` but **not** `__str__`. `print()` on a plain dataclass instance shows the same thing `repr()` would, purely because of the fallback rule above, not because the decorator wrote a matching `__str__`. Two optional decorator arguments matter here: `frozen=True` makes every field read-only after construction, and `order=True` additionally generates `__lt__`, `__le__`, `__gt__`, and `__ge__`, comparing instances field-by-field so sorting becomes meaningful [2].

Mixing a plain subclass on top of a dataclass superclass is a normal, supported pattern. `RegulatoryTask`, needing to call `super().__init__(...)` to thread the inherited fields through, keeps its own hand-written `__init__` instead of its own field list:

```python
class RegulatoryTask(Task):
    def __init__(self, name, priority, regulation_code, done):
        super().__init__(name, priority, done)
        self.regulation_code = regulation_code
```

`@dataclass` only changes how `Task` itself builds `__init__`, `__repr__`, and `__eq__` — it places no constraint on classes that inherit from it [2].

**Organizing classes into modules.** A module is a single `.py` file; any class defined at its top level becomes reachable from other files through `import`. `from task import Task` tells Python to locate `task.py`, run it once, and bind the name `Task` into the importing file's own namespace — after which `Task(...)` works there exactly as if it had been defined locally. A module object, itself one of Python's built-in types, carries this namespace as a dictionary mapping each top-level name to the object it refers to [1]. Import the same module again from anywhere else in the program, and Python reuses the already-built module object rather than re-running the file. A package extends this idea one level further: a directory holding several related modules, so other code can import from the group as a unit.

## Worked Example

Start from the `Task` class carried over from the prior topics — `name`, `priority`, `done`, `mark_complete()` — and trace it through both routes: hand-written special methods, then the dataclass equivalent.

**Hand-written version.** Adding `__repr__`, `__str__`, and `__eq__` directly:

```python
class Task:
    def __init__(self, name, priority):
        self.name = name
        self.priority = priority
        self.done = False

    def __repr__(self):
        return f"Task(name={self.name!r}, priority={self.priority!r}, done={self.done!r})"

    def __str__(self):
        return f"{self.name} ({self.priority}) - done={self.done}"

    def __eq__(self, other):
        return (isinstance(other, Task)
                and self.name == other.name
                and self.priority == other.priority
                and self.done == other.done)

t1 = Task("Write topic corpus", "normal")
t2 = Task("Write topic corpus", "normal")
print(t1)            # Write topic corpus (normal) - done=False
print(repr(t1))      # Task(name='Write topic corpus', priority='normal', done=False)
print(t1 == t2)      # True -- same class, same attribute values
```

`print(t1)` calls `__str__` because both `__str__` and `__repr__` are defined; `print(t1 == t2)` calls `__eq__`, which walks the `and`-chained expression, confirms `isinstance` first, then confirms all three attributes match.

**Dataclass version.** The same behavior, generated instead of typed:

```python
from dataclasses import dataclass

@dataclass
class Task:
    name: str
    priority: str
    done: bool = False

    def mark_complete(self):
        self.done = True

t1 = Task("Write topic corpus", "normal")
t2 = Task("Write topic corpus", "normal")
print(t1)            # Task(name='Write topic corpus', priority='normal', done=False)
print(t1 == t2)      # True
```

`mark_complete` is not a field — it has no type annotation at class level and isn't part of the generated methods; it's a plain method exactly as before. Note `print(t1)` here shows the `__repr__`-shaped output, not the friendlier `__str__` sentence from the hand-written version, because `@dataclass` never generated a `__str__` — this is the fallback rule from Key Concepts showing up directly in output.

**Splitting into a module.** Moving `Task` into its own file, `task.py`, containing the code above unchanged, lets a second file reach it without redefining it:

```python
# main.py
from task import Task

t1 = Task("Write topic corpus", "normal")
t1.mark_complete()
print(t1)
```

`from task import Task` locates `task.py`, runs it once (including the `@dataclass` decoration), and binds `Task` into `main.py`'s namespace — after which `main.py` uses `Task` exactly as if it lived in the same file.

Once a class is refactored this way, verifying it end to end matters more than trusting the decorator blindly: print an instance to confirm `__repr__` (or `__str__`) shows what you expect, compare two instances built with identical arguments to confirm `__eq__` reports `True`, and change one attribute on a copy to confirm it now reports `False`.

## In Practice

- **Reliable `__repr__` output pays off in debugging.** A stack trace or log line showing `Task(name='Write topic corpus', priority='normal', done=False)` tells a debugging engineer far more than a bare memory address — treat "give every class a useful `__repr__`" as close to a non-negotiable habit [1][3].
- **Write `__repr__` before `__str__`, and skip `__str__` when it would just repeat `__repr__`.** The fallback rule from Key Concepts means `print()` still works correctly with only `__repr__` defined, so don't write a `__str__` that duplicates it.
- **`__eq__` is what makes automated tests practical.** A test that builds an expected `Task` and compares it to the actual result only works if `==` compares values; without a real `__eq__`, every test would need to check each attribute by hand.
- **`@dataclass` is the standard shape for a small data-carrying object** — often called a DTO or record — whose entire job is holding a fixed set of named values with little behavior beyond what the decorator already generates [2].
- **`order=True` matters whenever records need ranking**, such as sorting tasks by priority or ordering a leaderboard; without it, sorting plain instances with `<` raises an error, because Python doesn't know how to compare two custom objects on its own [2].
- **One class (or a few closely related ones) per module.** Many real projects converge on a single `models.py` or a `models/` package holding data-bearing classes like `Task` and `Person`, separate from the files containing the logic that operates on them.

## Key Takeaways

- `__repr__` and `__str__` control how an object turns into a string — `__repr__` for an unambiguous, developer-facing form, `__str__` for a human-readable one — and Python calls them implicitly through `print()`, `str()`, and f-strings.
- Without `__str__`, `print()` falls back to `__repr__`, because `object`'s default `__str__` calls `self.__repr__()`.
- Without `__eq__`, `==` between custom-class instances falls back to identity comparison, the same check `is` performs; `__eq__` lets you define equality as a single `and`-chained boolean expression instead.
- `@dataclass` generates `__init__`, `__repr__`, and `__eq__` from annotated field declarations, cutting repetitive boilerplate for data-heavy classes — but it does not generate `__str__`, and defaulted fields must all come after non-defaulted ones.
- A dataclass is still an ordinary class: it can hold plain methods and participates in inheritance like any other class, and splitting classes into their own modules with `import` keeps related code organized as a program grows.

## References

[1] Python Software Foundation. "Data Model." *The Python Language Reference*. https://docs.python.org/3/reference/datamodel.html

[2] Python Software Foundation. "dataclasses — Data Classes." *Python Documentation*. https://docs.python.org/3/library/dataclasses.html

[3] Real Python. "Python's `str()` and `repr()` for Custom Classes." https://realpython.com/python-repr-vs-str/

---

<sub>[&#8592; Previous: 6.2 Inheritance & Encapsulation](../../../../../../../content/ai_native_engineering_foundations/p4-classes-objects/week-6/1-classes-objects/6-2-inheritance-encapsulation/artifacts/reading.md)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Go back to TOC](../../../../../../../README.md)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Next: 7.1 File Handling &#8594;](../../../../../../../content/ai_native_engineering_foundations/p5-files-exception-handling/week-7/1-files-exception-handling/7-1-file-handling/reading.md)</sub>
