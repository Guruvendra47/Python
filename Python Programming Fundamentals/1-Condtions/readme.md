# Python Conditions and Branching

## Overview

This repository introduces **Python Conditions and Branching**, which enable programs to make decisions and execute different blocks of code based on Boolean expressions and comparison results. It covers comparison operators, conditional statements, and logical operators used to control program flow.

These concepts are fundamental for building interactive and decision-based Python applications.

---

## Topics Covered

### Comparison Operators

Comparison operators compare two values and return a Boolean result (`True` or `False`).

Operators covered:

| Operator | Description |
|----------|-------------|
| `==` | Equal to |
| `!=` | Not equal to |
| `>` | Greater than |
| `<` | Less than |
| `>=` | Greater than or equal to |
| `<=` | Less than or equal to |

Example:

```python
a = 6

print(a == 6)
print(a != 7)
print(a > 5)
print(a < 10)
```

---

### Comparing Different Data Types

Comparison operators can be used with different data types.

Topics include:

- Integer comparison
- Float comparison
- String comparison

Example:

```python
"Python" == "Python"

"Python" != "Java"
```

---

### The `if` Statement

The `if` statement executes a block of code only when a specified condition evaluates to `True`.

Example:

```python
age = 19

if age >= 18:
    print("You can enter.")
```

---

### The `else` Statement

The `else` statement executes when the condition in the `if` statement evaluates to `False`.

Example:

```python
age = 17

if age >= 18:
    print("You can enter.")
else:
    print("Move on.")
```

---

### The `elif` Statement

The `elif` statement allows multiple conditions to be checked sequentially.

Example:

```python
age = 18

if age > 18:
    print("Go to AC/DC concert")
elif age == 18:
    print("Go to Pink Floyd concert")
else:
    print("Go to Meat Loaf concert")
```

---

### Boolean Logic Operators

Logical operators combine multiple Boolean expressions.

Topics include:

- `and`
- `or`
- `not`

---

### The `not` Operator

Reverses the Boolean value of an expression.

Example:

```python
not True
```

---

### The `or` Operator

Returns `True` if at least one condition is `True`.

Example:

```python
album_year = 1990

if album_year < 1980 or album_year > 1989:
    print("Album released outside the 80s")
```

---

### The `and` Operator

Returns `True` only when all conditions are `True`.

Example:

```python
album_year = 1983

if album_year >= 1980 and album_year <= 1989:
    print("Album released in the 80s")
```

---

## Examples Included

- Comparing integers
- Comparing floating-point numbers
- Comparing strings
- Using comparison operators
- Writing `if` statements
- Using `if-else`
- Using `if-elif-else`
- Combining conditions with logical operators
- Decision-making using Boolean expressions

---

## Skills Learned

- Using comparison operators
- Evaluating Boolean expressions
- Writing conditional statements
- Creating branching logic
- Combining multiple conditions
- Applying logical operators
- Controlling program flow

---

## Technologies Used

- Python 3
- Jupyter Notebook

---

## Repository Structure

```text
Python-Conditions-and-Branching/
│
├── Comparison Operators
├── Boolean Expressions
├── If Statements
├── If-Else Statements
├── If-Elif-Else Statements
├── Logical Operators
├── Practice Examples
└── README.md
```

---

## Author

**Guruvendra Singh**

Data Engineering | Python | SQL | Snowflake | AWS