# Python Loops

## Overview

This repository introduces **Python Loops**, which allow repetitive tasks to be performed efficiently. It covers the `range()` function, `for` loops, `while` loops, iterating through sequences, and the `enumerate()` function for accessing both indexes and values during iteration.

Loops are fundamental to automating repetitive operations and processing collections such as lists, tuples, strings, and dictionaries.

---

## Topics Covered

### The `range()` Function

The `range()` function generates a sequence of numbers commonly used in loops.

Topics include:

- Single argument
- Start and stop values
- Sequence generation
- Loop iteration

Examples:

```python
range(5)

range(10, 15)
```

---

### For Loops

A `for` loop iterates over a sequence and executes a block of code for each element.

Topics include:

- Iterating through lists
- Iterating through tuples
- Fixed number of iterations
- Updating list elements

Example:

```python
colors = ["Red", "Yellow", "Green"]

for color in colors:
    print(color)
```

---

### Using `range()` with `for`

The `range()` function is commonly used with `for` loops to iterate using indexes.

Example:

```python
colors = ["Red", "Yellow", "Green"]

for i in range(len(colors)):
    print(colors[i])
```

---

### Iterating Directly Through a Sequence

Python allows direct iteration over elements without using indexes.

Example:

```python
colors = ["Red", "Yellow", "Green"]

for color in colors:
    print(color)
```

---

### Using `enumerate()`

The `enumerate()` function returns both the index and the corresponding element during iteration.

Topics include:

- Accessing indexes
- Accessing values
- Indexed iteration

Example:

```python
colors = ["Red", "Yellow", "Green"]

for index, color in enumerate(colors):
    print(index, color)
```

---

### While Loops

A `while` loop repeatedly executes a block of code as long as a specified condition remains `True`.

Topics include:

- Conditional iteration
- Updating loop variables
- Loop termination
- Appending elements

Example:

```python
count = 0

while count < 5:
    print(count)
    count += 1
```

---

### Loop Control Using Conditions

A `while` loop continues until its condition becomes `False`.

Example:

```python
colors = ["Orange", "Orange", "Purple"]
new_colors = []

i = 0

while colors[i] == "Orange":
    new_colors.append(colors[i])
    i += 1
```

---

## Examples Included

- Generating sequences using `range()`
- Iterating through lists
- Iterating through tuples
- Using indexes with `range()`
- Direct iteration over elements
- Using `enumerate()`
- Updating list values
- Writing `while` loops
- Processing data until a condition changes

---

## Skills Learned

- Using the `range()` function
- Writing `for` loops
- Writing `while` loops
- Iterating over sequences
- Using indexes during iteration
- Accessing both indexes and values with `enumerate()`
- Controlling repetitive execution using conditions

---

## Technologies Used

- Python 3
- Jupyter Notebook

---

## Repository Structure

```text
Python-Loops/
│
├── Range Function
├── For Loops
├── While Loops
├── Enumerate
├── Loop Operations
├── Practice Examples
└── README.md
```

---

## Author

**Guruvendra Singh**

Data Engineering | Python | SQL | Snowflake | AWS