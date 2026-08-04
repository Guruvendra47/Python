# Python Functions

## Overview

This repository introduces **Python Functions**, one of the fundamental building blocks of Python programming. It covers built-in functions, creating custom functions, function parameters, return values, documentation strings, variable scope, variadic arguments, and the distinction between global and local variables.

Functions improve code readability, reduce repetition, and promote reusable, modular programming.

---

## Topics Covered

### Introduction to Functions

Functions are reusable blocks of code that perform a specific task. They accept input (parameters), process data, and optionally return a result.

Topics include:

- Function definition
- Function calls
- Inputs and outputs
- Code reusability

Example:

```python
def greet():
    print("Hello, World!")

greet()
```

---

### Built-in Functions

Python provides many built-in functions for common operations.

Functions covered:

- `len()`
- `sum()`
- `sorted()`
- `help()`

Examples:

```python
numbers = [10, 20, 30]

len(numbers)

sum(numbers)

sorted(numbers)
```

---

### `sorted()` vs `sort()`

Python provides two ways to sort data.

#### `sorted()`

Returns a **new sorted list** without modifying the original.

Example:

```python
numbers = [5, 2, 8]

new_numbers = sorted(numbers)
```

---

#### `sort()`

Sorts the original list **in place**.

Example:

```python
numbers = [5, 2, 8]

numbers.sort()
```

---

### Creating Custom Functions

Functions are created using the `def` keyword.

Example:

```python
def add_one(number):
    return number + 1
```

---

### Function Parameters

Functions can accept one or more parameters.

Example:

```python
def multiply(a, b):
    return a * b
```

---

### Return Values

The `return` statement sends a result back to the caller.

Example:

```python
def square(number):
    return number ** 2
```

---

### Documentation Strings (Docstrings)

Functions should include documentation to explain their purpose.

Example:

```python
def multiply(a, b):
    """
    Returns the product of two numbers.
    """
    return a * b
```

Documentation can be viewed using:

```python
help(multiply)
```

---

### Functions Without `return`

If a function does not include a `return` statement, Python automatically returns `None`.

Example:

```python
def display():
    print("Hello")
```

---

### The `pass` Statement

The `pass` keyword acts as a placeholder for future code.

Example:

```python
def future_feature():
    pass
```

---

### Functions with Loops

Functions can include loops to process collections.

Example:

```python
def print_items(items):
    for item in items:
        print(item)
```

---

### Variadic Parameters (`*args`)

Variadic parameters allow a function to accept a variable number of arguments.

Example:

```python
def display_names(*names):
    for name in names:
        print(name)
```

---

### Variable Scope

Variable scope determines where a variable can be accessed.

Topics include:

- Local variables
- Global variables
- Function scope
- Variable lookup

Example:

```python
x = 10

def demo():
    y = 5
```

---

### Local Variables

Local variables exist only inside a function.

Example:

```python
def movie():
    year = 1982
    print(year)
```

---

### Global Variables

Global variables are accessible throughout the program.

Example:

```python
rating = 9

def show_rating():
    print(rating)
```

---

### Using the `global` Keyword

The `global` keyword allows a function to modify a global variable.

Example:

```python
def update_sales():
    global sales
    sales = "45 Million"
```

---

## Examples Included

- Using built-in functions
- Sorting lists
- Creating custom functions
- Returning values
- Functions without return statements
- Using `pass`
- Writing documentation strings
- Calling `help()`
- Functions with multiple parameters
- Using loops inside functions
- Variadic parameters (`*args`)
- Working with local variables
- Working with global variables
- Using the `global` keyword

---

## Skills Learned

- Using Python built-in functions
- Creating reusable functions
- Passing arguments to functions
- Returning values
- Writing function documentation
- Using `help()`
- Working with variable-length arguments
- Understanding local and global scope
- Managing variables inside functions

---

## Technologies Used

- Python 3
- Jupyter Notebook

---

## Repository Structure

```text
Python-Functions/
│
├── Built-in Functions
├── User-Defined Functions
├── Function Parameters
├── Return Statements
├── Docstrings
├── Variable Scope
├── Variadic Parameters
├── Practice Examples
└── README.md
```

---

## Author

**Guruvendra Singh**

Data Engineering | Python | SQL | Snowflake | AWS