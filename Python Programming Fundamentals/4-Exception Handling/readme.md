# Python Exception Handling

## Overview

This repository introduces **Python Exception Handling**, a mechanism used to detect and handle runtime errors without terminating a program unexpectedly. It covers the `try`, `except`, `else`, and `finally` statements, along with best practices for handling exceptions effectively.

Exception handling helps create more reliable and user-friendly applications by allowing programs to respond gracefully to errors.

---

## Topics Covered

### Introduction to Exception Handling

Exception handling enables Python programs to continue running even when runtime errors occur.

Topics include:

- Runtime errors
- Error handling
- Preventing program crashes
- Graceful program execution

---

### The `try` Statement

The `try` block contains code that may raise an exception.

Example:

```python
try:
    file = open("data.txt")
```

---

### The `except` Statement

The `except` block executes when an exception occurs in the `try` block.

Topics include:

- Catching exceptions
- Handling errors
- Responding to runtime failures

Example:

```python
try:
    file = open("data.txt")
except IOError:
    print("Unable to open or read the data in the file.")
```

---

### Handling Specific Exceptions

It is recommended to catch specific exception types instead of using a generic `except`.

Example:

```python
try:
    file = open("data.txt")
except IOError:
    print("Unable to open or read the data in the file.")
```

---

### Generic Exception Handling

A generic `except` block catches all exceptions but provides less information for debugging.

Example:

```python
try:
    file = open("data.txt")
except:
    print("An unexpected error occurred.")
```

> **Note:** Using generic exceptions should be avoided whenever possible because they make debugging more difficult.

---

### The `else` Statement

The `else` block executes only if no exception occurs.

Example:

```python
try:
    file = open("data.txt")
except IOError:
    print("Unable to open the file.")
else:
    print("The file was written successfully.")
```

---

### The `finally` Statement

The `finally` block always executes, regardless of whether an exception occurs.

It is commonly used for cleanup operations such as closing files or releasing resources.

Example:

```python
try:
    file = open("data.txt")
except IOError:
    print("Unable to open the file.")
finally:
    file.close()
    print("File is now closed.")
```

---

### Exception Handling Workflow

The execution flow follows this order:

1. Execute the `try` block.
2. If an exception occurs, execute the matching `except` block.
3. If no exception occurs, execute the `else` block.
4. Execute the `finally` block regardless of the outcome.

---

## Examples Included

- Basic `try` statements
- Catching `IOError`
- Handling specific exceptions
- Generic exception handling
- Using `else`
- Using `finally`
- Closing files safely
- Complete exception handling workflow

---

## Skills Learned

- Understanding runtime exceptions
- Using `try` and `except`
- Handling specific exceptions
- Applying `else` for successful execution
- Using `finally` for cleanup tasks
- Following exception handling best practices
- Writing more reliable Python programs

---

## Technologies Used

- Python 3
- Jupyter Notebook

---

## Repository Structure

```text
Python-Exception-Handling/
│
├── Introduction
├── Try Statement
├── Except Statement
├── Else Statement
├── Finally Statement
├── Exception Handling Workflow
├── Practice Examples
└── README.md
```

---

## Author

**Guruvendra Singh**

Data Engineering | Python | SQL | Snowflake | AWS