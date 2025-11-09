# Conditional Statements in Python

---

## Table of Contents
- [Introduction to Conditional Statements](#introduction-to-conditional-statements)
- [The `if` Statement](#the-if-statement)
- [The `else` Statement](#the-else-statement)
- [The `elif` Statement](#the-elif-statement)
- [Nested Conditionals](#nested-conditionals)
- [Ternary / Conditional Expressions](#ternary--conditional-expressions)
- [Common Pitfalls & Best Practices](#common-pitfalls--best-practices)
- [Practice Problems & Solutions](#practice-problems--solutions)
- [Business Examples](#business-examples)
- [Quick Start (Repo Structure)](#quick-start-repo-structure)
- [Attribution](#attribution)

---

## Introduction to Conditional Statements

Conditional statements let programs make decisions. They evaluate expressions that resolve to `True` or `False` and run code accordingly. You'll use them for validation, branching logic, and implementing business rules.

**Core concepts:** boolean expressions, comparison operators (`==`, `!=`, `<`, `>`), and logical operators (`and`, `or`, `not`).

---

## The `if` Statement

Use `if` to execute code when a condition is true.

```python
age = 20
if age >= 18:
    print("Adult access granted")
```

**Tip:** Prefer clear, descriptive conditions (e.g., `if user.is_active:`) rather than complex inline expressions.

---

## The `else` Statement

`else` runs when the `if` condition is false.

```python
age = 15
if age >= 18:
    print("Adult")
else:
    print("Minor")
```

`else` always complements an `if` and has no condition of its own.

---

## The `elif` Statement

`elif` allows checking additional mutually-exclusive conditions without deep nesting.

```python
score = 82
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"
```

Remember: evaluation stops at the first matching branch.

---

## Nested Conditionals

Nesting is when conditionals appear inside other conditionals. Useful for dependent checks, but keep readability in mind.

```python
user = {"active": True, "role": "editor"}

if user["active"]:
    if user["role"] == "admin":
        print("Admin dashboard")
    else:
        print("Editor view")
else:
    print("Activate your account")
```

**Refactor tip:** Use guard clauses or helper functions to reduce nesting depth.

---

## Ternary / Conditional Expressions

Compact assignment based on a condition — good for short, readable choices.

```python
status = "active" if user_is_active else "inactive"
```

Avoid complex logic in ternaries; prefer standard `if` blocks when clarity suffers.

---

## Common Pitfalls & Best Practices

- **Indentation errors:** Use consistent 4-space indentation (PEP 8).  
- **Assignment vs comparison:** `=` assigns, `==` compares. Mistakes cause syntax or logic errors.  
- **Truthiness surprises:** Empty lists, strings, `0`, and `None` are `False` in conditionals—use explicit checks where needed.  
- **Order matters:** Put the most likely or cheapest checks first in `elif` chains.  
- **Avoid deep nesting:** Prefer `elif`, functions, or early returns (guard clauses).

---

## Practice Problems & Solutions

**Problems (implement in `solutions/`):**
1. `sign(n)` — return `"positive"`, `"negative"`, or `"zero"`.
2. Grade calculator using `if/elif/else`.  
3. Age classifier: child, teen, adult, senior.  
4. Login flow that handles wrong password, inactive account, and success.
5. Convert a simple `if/else` to a ternary expression.

**Sample solution — `sign(n)`**
```python
def sign(n: int) -> str:
    if n > 0:
        return "positive"
    elif n < 0:
        return "negative"
    else:
        return "zero"
```

---

## Business Examples

### Personalization & Feature Flags
Show or hide features based on user attributes and environment flags.

```python
if user.is_paying and feature_flag_enabled("new_dashboard"):
    show_new_dashboard(user)
else:
    show_legacy_dashboard(user)
```

### Approval Routing
Route transactions depending on amount and user role.

```python
def route_request(request):
    if request.amount > 50000 and request.role != "director":
        escalate_to_finance(request)
    elif request.amount <= 50000:
        auto_approve(request)
    else:
        require_additional_review(request)
```

### Data Validation in ETL
Drop or mark rows that fail validation rules during ingestion.

```python
def valid_row(row):
    if not row.get("email"):
        return False
    if "@" not in row["email"]:
        return False
    return True
```

---

## Next Lesson - 4
