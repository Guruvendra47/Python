# Conditional Statements in Python
**Understanding how to control the flow of your programs**

A practical, original guide that turns your slide deck into a GitHub-ready project. The content is rewritten to be realistic, example-driven, and safe to publish (no direct copy-paste of slide text).

---

## Table of Contents
- [Introduction to Conditional Statements](#introduction-to-conditional-statements)
- [The `if` Statement](#the-if-statement)
- [The `else` Statement](#the-else-statement)
- [The `elif` Statement](#the-elif-statement)
- [Nested Conditional Statements](#nested-conditional-statements)
- [If-else vs Nested If](#if-else-vs-nested-if)
- [Conditional Expressions (Ternary Operator)](#conditional-expressions-ternary-operator)
- [Common Mistakes & Gotchas](#common-mistakes--gotchas)
- [Practice Problems](#practice-problems)
- [Business Use Cases](#business-use-cases)
- [Project Ideas & Extensions](#project-ideas--extensions)
- [Attribution](#attribution)

---

## Introduction to Conditional Statements

Conditional statements let your program choose different actions depending on data or state. They are the building blocks of decision-making in code — from simple validations to complex business workflows.

Key ideas:
- Evaluate True/False conditions (booleans).  
- Execute code blocks only when certain conditions are met.  
- Combine conditions using logical operators: `and`, `or`, `not`.

---

## The `if` Statement

Use `if` to run a block of code only when a condition evaluates to `True`.

```python
age = 20
if age >= 18:
    print("You are an adult.")
```

**Tip:** Keep the conditional expression clear — prefer descriptive variables and avoid complicated one-liners when readability suffers.

---

## The `else` Statement

`else` provides an alternate block when the `if` condition is `False`.

```python
age = 16
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")
```

`else` has no condition — it runs when previous `if` (and `elif`) conditions didn't match.

---

## The `elif` Statement

Use `elif` to check additional conditions after an initial `if`. This avoids deep nesting for multiple exclusive branches.

```python
score = 76
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
else:
    grade = 'F'
print("Grade:", grade)
```

**Note:** `elif` chains are evaluated top-to-bottom; once a branch matches, the rest are skipped.

---

## Nested Conditional Statements

Nesting means placing conditionals inside other conditional blocks. It's useful when subsequent checks depend on earlier ones but can reduce readability if overused.

```python
user = {'role': 'admin', 'active': True}

if user['active']:
    if user['role'] == 'admin':
        print("Show admin dashboard")
    else:
        print("Show user dashboard")
else:
    print("Please activate your account")
```

**Best practice:** Flatten nested logic with guard clauses or by combining conditions where it makes sense.

---

## If-else vs Nested If

- **If-else:** Simple two-way decision. Use when there are only two alternatives.  
- **Nested if:** Use when one decision only makes sense after another condition is true (dependent checks).

Whenever possible, prefer `elif` or boolean combinations (`and`, `or`) to avoid deeply nested blocks.

---

## Conditional Expressions (Ternary Operator)

A compact way to assign values depending on a condition — good for short, clear choices.

```python
age = 17
status = "adult" if age >= 18 else "minor"
print(status)
```

**Guideline:** Keep ternary expressions short. If the logic is complex, prefer a normal `if` block for clarity.

---

## Common Mistakes & Gotchas

1. **Indentation errors** — Python uses indentation to mark blocks; inconsistent spaces/tabs cause runtime errors.  
2. **Assignment vs comparison** — `=` assigns, `==` compares. Using `=` in a conditional is a syntax error.  
3. **Truthiness surprises** — Empty containers (`[]`, `''`, `{}`) and `0` are `False` in boolean contexts. Use explicit comparisons when ambiguity matters.  
4. **Over-nesting** — Too many nested `if`s make code hard to read and maintain. Refactor into functions or use `elif`.  
5. **Order of conditions** — Place the most likely/fast checks first for efficiency when conditions are expensive.

---

## Practice Problems

Try these to build muscle memory. Solutions are provided in the `solutions/` folder of this repo.

1. **Sign check:** Write a function `sign(n)` that returns `"positive"`, `"negative"`, or `"zero"`.  
2. **Grade calculator:** Convert numeric scores to letter grades using `if/elif/else`.  
3. **Age category:** Use nested `if` to classify age groups: child (<13), teen (13–17), adult (18–64), senior (65+).  
4. **Login flow:** Given `username`, `password`, and `is_active`, write a conditional flow that handles incorrect credentials, inactive accounts, and successful login.  
5. **Ternary usage:** Re-write a simple `if/else` assignment as a ternary expression.

---

## Business Use Cases

Conditional logic is everywhere in production systems. A few realistic examples:

### 1) Customer Personalization
Show different landing page content based on user segment and recent behavior:

```python
if user.is_logged_in:
    if user.segment == 'premium':
        show_premium_recommendations()
    else:
        show_standard_recommendations()
else:
    show_guest_promotions()
```

### 2) Approval Workflows
Automate multi-step approvals in HR/Finance using condition checks (amount thresholds, user role, department).

```python
if request.amount > 10000 and request.approver_role == 'manager':
    route_to_senior_manager(request)
elif request.amount <= 10000:
    auto_approve(request)
else:
    require_additional_review(request)
```

### 3) Data Validation & ETL
Drop or flag rows during ETL based on validation rules (missing fields, inconsistent data types).

```python
def validate_row(row):
    if not row.get('email'):
        return False
    if '@' not in row['email']:
        return False
    return True
```

---

## Project Ideas & Extensions

- Build a small CLI tool that asks users a series of questions and branches logic based on their answers (e.g., interactive loan eligibility checker).  
- Create unit tests for your practice problems and set up GitHub Actions to run them on push.  
- Integrate conditional rules into a lightweight approval microservice using Flask or FastAPI.

---

## Attribution

This README was created from your slides but rewritten and expanded to be original, practical, and ready for a GitHub repository.  
Save this file as `README.md` in a repository named `conditional-statements-python`.

---

### Download & Next Steps
I can now:
- Create the repo folder structure and add `solutions/` and `scripts/` with example code and tests, then zip it for you to download.  
- Or prepare a `git` script and instructions so you can push this project to GitHub yourself.  
Tell me which one you want and I’ll generate it immediately.