# Python Programming Fundamentals

## Overview

This repository covers the core programming concepts in Python, including **conditions, branching, loops, functions, exception handling, and object-oriented programming (OOP)**. It demonstrates how to control program flow, create reusable code, handle runtime errors, and build classes and objects.

These concepts form the foundation for writing structured, maintainable, and scalable Python applications.

---

## Topics Covered

### Conditions and Branching

Conditional statements allow programs to make decisions based on comparisons and Boolean expressions.

Topics include:

- `if` statements
- `else` statements
- `elif` statements
- Comparison operators
- Boolean expressions
- Boolean logic operators

Comparison operators covered:

- `==`
- `!=`
- `>`
- `<`
- `>=`
- `<=`

Example:

```python
age = 18

if age >= 18:
    print("Adult")
else:
    print("Minor")
```

---

### Loops

Loops automate repetitive tasks by executing code multiple times.

Topics include:

- `for` loops
- `while` loops
- Iterating through lists
- Iterating through tuples
- Iterating through strings
- Iterating through dictionaries
- Using `range()`

Example:

```python
for i in range(5):
    print(i)
```

---

### Functions

Functions organize reusable blocks of code.

Topics include:

- Defining functions
- Function parameters
- Multiple parameters
- Return values
- Functions returning `None`
- Placeholder functions using `pass`
- Documentation strings (Docstrings)
- Using `help()`

Example:

```python
def add(a, b):
    """Returns the sum of two numbers."""
    return a + b
```

---

### Built-in Functions

Python provides many built-in functions for common tasks.

Topics include:

- `len()`
- `sum()`
- `sorted()`
- `sort()`
- `help()`

Examples:

```python
len(numbers)

sum(numbers)

sorted(numbers)
```

---

### Variable Scope

Variable scope determines where variables can be accessed.

Topics include:

- Local variables
- Global variables
- Scope inside functions
- Scope outside functions

Example:

```python
x = 10

def demo():
    y = 5
```

---

### Exception Handling

Exception handling prevents programs from terminating unexpectedly when errors occur.

Topics include:

- `try`
- `except`
- `else`
- `finally`

Example:

```python
try:
    value = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
finally:
    print("Execution completed")
```

---

### Objects and Classes

Python supports object-oriented programming using classes and objects.

Topics include:

- Classes
- Objects
- Instances
- Attributes
- Methods
- Constructors
- `__init__()`
- `self`
- Object creation
- Using `type()`

Example:

```python
class Car:

    def __init__(self, brand):
        self.brand = brand

    def display(self):
        print(self.brand)
```

---

## Examples Included

- Using conditional statements
- Nested branching
- Boolean logic
- For loops
- While loops
- Using `range()`
- Creating custom functions
- Using built-in functions
- Working with local and global variables
- Handling exceptions
- Creating classes
- Creating objects
- Defining methods
- Initializing objects using `__init__`

---

## Skills Learned

- Writing conditional statements
- Controlling program flow
- Using loops efficiently
- Creating reusable functions
- Understanding variable scope
- Handling runtime exceptions
- Building Python classes
- Creating and using objects
- Applying object-oriented programming concepts

---

## Technologies Used

- Python 3
- Jupyter Notebook

---

## Repository Structure

```text
Python-Programming-Fundamentals/
│
├── Conditions and Branching
├── Loops
├── Functions
├── Variable Scope
├── Exception Handling
├── Objects and Classes
├── Practice Examples
└── README.md
```

---

## Author

**Guruvendra Singh**

Data Engineering | Python | SQL | Snowflake | AWS