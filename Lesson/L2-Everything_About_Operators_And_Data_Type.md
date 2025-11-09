# Python: Operators, Type Casting, `input()`, and `eval()` — From Slides to GitHub

A practical, hands-on guide that turns your presentation into a GitHub-friendly reference with examples you can copy‑paste and run. Everything is written in clear language and grounded in realistic, business‑style scenarios.

> **What this is:** A single `README.md` you can drop into a repo. It summarizes operators, precedence, type casting, the `input()` function, and `eval()`—with runnable examples and best practices for real projects.

---

## Table of Contents
- [Why Operators Matter (Real Use Case)](#why-operators-matter-real-use-case)
- [Operator Precedence (What Runs First?)](#operator-precedence-what-runs-first)
- [Type Casting (Implicit vs Explicit)](#type-casting-implicit-vs-explicit)
- [Handling Casting Errors (Realistic Patterns)](#handling-casting-errors-realistic-patterns)
- [`input()` in Python (Practical Use)](#input-in-python-practical-use)
- [Validating User Input](#validating-user-input)
- [`eval()` — What It Does and Why It’s Risky](#eval--what-it-does-and-why-its-risky)
- [Business Mini‑Project: Retail Data Standardization](#business-mini-project-retail-data-standardization)
- [Quick Start](#quick-start)
- [Attribution](#attribution)

---

## Why Operators Matter (Real Use Case)

**Scenario:** A company needs to transmit lots of small attributes over a network cheaply and quickly. To save space, we **pack multiple small values into a single byte** using bitwise operators.

**Example attributes**
- Product category: `0–15` (4 bits)
- Region code: `0–3` (2 bits)
- Status flag: `0–1` (1 bit)

That fits into 7 bits, so a single byte is enough.

```python
def pack_record(product_category: int, region: int, status: int) -> int:
    """
    Pack three small integers into a single byte.
    Layout (from most significant to least):
      [ product_category:4 | region:2 | status:1 | reserved:1 ]
    """
    if not (0 <= product_category <= 15 and 0 <= region <= 3 and status in (0, 1)):
        raise ValueError("Out-of-range values")
    return (product_category << 3) | (region << 1) | status

def unpack_record(byte_val: int) -> tuple[int, int, int]:
    """Reverse of pack_record()."""
    if not (0 <= byte_val <= 0xFF):
        raise ValueError("Needs a single byte (0-255)")
    product_category = (byte_val >> 3) & 0b1111
    region = (byte_val >> 1) & 0b11
    status = byte_val & 0b1
    return product_category, region, status

b = pack_record(7, 2, 1)
print(b)                      # e.g., 0b111101 -> 61
print(unpack_record(b))       # (7, 2, 1)
```

**Key operators used:** `<<`, `>>`, `|`, `&`.

---

## Operator Precedence (What Runs First?)

Python follows a fixed precedence when evaluating expressions (like maths). A simple rule of thumb:

1. Parentheses `()` first
2. Exponentiation `**`
3. Unary `+x`, `-x`, `~x`
4. Multiplication, division, modulo `* / // %`
5. Addition and subtraction `+ -`
6. Bitwise shifts `<< >>`
7. Bitwise AND `&`, XOR `^`, OR `|`
8. Comparisons `== != < <= > >= in is`
9. Boolean `not` → `and` → `or`
10. Assignment `=`, `+=`, `-=`, …

**Tip:** When in doubt, add parentheses. It improves readability and avoids bugs.

```python
result = 1 + 2 << 2   # Equivalent to (1 + 2) << 2 == 12
```

---

## Type Casting (Implicit vs Explicit)

### Implicit casting (automatic)
Python may widen types to avoid loss of information.

```python
x = 5      # int
y = 2.0    # float
z = x + y  # 7.0 (float) — x is implicitly converted
```

### Explicit casting (you decide)
Use built‑ins when you need exact control.

```python
s = "123"
n = int(s)      # 123
f = float("3.5")  # 3.5
t = str(42)     # "42"

# Collections
list("abc")   # ['a','b','c']
tuple([1,2])  # (1,2)
```

---

## Handling Casting Errors (Realistic Patterns)

Bad inputs happen. Handle them gracefully and keep context in error messages.

```python
def to_int_or_none(value: str) -> int | None:
    try:
        return int(value)
    except ValueError:
        return None  # or log and return a sentinel

def safe_int(value: str, field_name: str = "value") -> int:
    try:
        return int(value)
    except ValueError as e:
        raise ValueError(f"Invalid {field_name!r}: {value!r}") from e

# Example
print(to_int_or_none("abc"))         # None
print(safe_int("10"))                # 10
# print(safe_int("ten", "age"))     # raises ValueError("Invalid 'age': 'ten'")
```

**Best practices**
- Validate first when possible (e.g., `.isdigit()` for simple integers).
- Use `try/except` for robust flows.
- Don’t silently swallow errors in production—log them.

---

## `input()` in Python (Practical Use)

`input()` reads a line from the console **as a string**.

```python
name = input("Enter your name: ")
print(f"Hello, {name}!")
```

**Converting to a number**

```python
age_str = input("Enter your age: ")
try:
    age = int(age_str)
    print(age * 2)
except ValueError:
    print("Please enter a valid whole number for age.")
```

---

## Validating User Input

Loop until you get a valid value—this is a real‑world pattern.

```python
def ask_int(prompt: str) -> int:
    while True:
        raw = input(prompt)
        try:
            return int(raw)
        except ValueError:
            print("Invalid number. Try again.")

qty = ask_int("Quantity to order: ")
print("Confirmed:", qty)
```

**Tips**
- Always be clear in the prompt about the expected format.
- Consider offering defaults (e.g., empty input → default value).

---

## `eval()` — What It Does and Why It’s Risky

`eval()` executes a string **as Python code**. That means it can run anything—**including malicious commands**—if the string is untrusted.

```python
# DANGEROUS: don't do this with user input
user_expr = input("Enter a Python expression: ")
print(eval(user_expr))  # Can run arbitrary code
```

**Safer alternatives**
- Parse structured data with `json.loads()`.
- For literal Python values (strings, numbers, lists, dicts), use `ast.literal_eval()`.
- Build your own small parser for mini‑languages; never execute raw input.

```python
import ast, json

ast.literal_eval("[1, 2, 3]")      # Safe for Python literals
json.loads('{"a": 1, "b": 2}')     # Safe JSON
```

**Bottom line:** In business apps, favor `input()` with validation and typed parsing. Avoid `eval()` unless you absolutely control the input.

---

## Business Mini‑Project: Retail Data Standardization

Unifying data types across systems for analytics.

**Problem**
- CSV has numbers as strings: `"1500"`
- Database has proper floats: `1500.0`
- Dates come in different formats, and NULLs are `"NaN"`/`"None"` strings

**Approach (pure Python example)**
```python
from datetime import datetime

def to_number(s: str) -> float | None:
    s = (s or "").strip()
    if s.lower() in {"", "none", "nan", "null"}:
        return None
    try:
        return float(s.replace(",", ""))
    except ValueError:
        return None

def to_date(s: str, formats=("%Y-%m-%d", "%d-%m-%Y", "%m/%d/%Y")):
    s = (s or "").strip()
    if not s or s.lower() in {"none", "nan", "null"}:
        return None
    for fmt in formats:
        try:
            return datetime.strptime(s, fmt).date()
        except ValueError:
            continue
    return None

row = {"sales_amount": "1,500", "order_date": "12/31/2024"}
clean = {
    "sales_amount": to_number(row["sales_amount"]),
    "order_date": to_date(row["order_date"]),
}
print(clean)  # {'sales_amount': 1500.0, 'order_date': datetime.date(2024, 12, 31)}
```

**Extends well to:** ETL jobs, data validation layers, and analytics pipelines.

---

## Quick Start

1. Create a new GitHub repo.
2. Add this file as `README.md` in the root.
3. Optionally, add a folder `examples/` and paste the code snippets into runnable `.py` files.
4. Commit and push. Your repo is now a clean, realistic reference for interviews and projects.

---

## Attribution

This README was authored to be original and practical while capturing the teaching goals of your slides on Python operators, precedence, type casting, `input()`, and `eval()`. The examples and wording are newly written to avoid duplication.
