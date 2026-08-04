# Python Lists and Tuples

## Overview

This repository introduces **Python Lists and Tuples**, two of the most commonly used data structures in Python. It covers creating lists and tuples, accessing elements using indexing and slicing, performing common operations, understanding mutability and immutability, working with nested collections, and using built-in methods.

These concepts provide the foundation for storing, organizing, and manipulating collections of data in Python.

---

## Topics Covered

### Tuples

Tuples are ordered and immutable collections of elements enclosed in parentheses `()`.

Topics include:

- Creating tuples
- Ordered collections
- Immutable objects
- Mixed data types
- Tuple indexing
- Negative indexing
- Tuple concatenation
- Tuple slicing
- Tuple length using `len()`

Example:

```python
ratings = (10, 9.5, 8, 7.5)
```

---

### Tuple Immutability

Tuples cannot be modified after creation.

Topics include:

- Immutable collections
- Creating new tuples
- Assigning new tuples
- Sorting tuples using `sorted()`

Example:

```python
sorted(ratings)
```

---

### Nested Tuples

Tuples can contain other tuples and complex data types.

Topics include:

- Nested tuples
- Multi-level indexing
- Accessing nested elements
- Nested string access

Example:

```python
nested = ("Python", (10, 20), ("A", "B"))
```

---

### Lists

Lists are ordered and mutable collections enclosed in square brackets `[]`.

Topics include:

- Creating lists
- Mutable collections
- Mixed data types
- Nested lists
- Tuple inside lists
- List indexing
- Negative indexing
- List slicing
- List concatenation

Example:

```python
languages = ["Python", "Java", "C++"]
```

---

### List Methods

Python provides built-in methods for modifying lists.

Topics include:

- `append()`
- `extend()`
- Modifying list elements
- Adding multiple elements
- Appending nested lists

Examples:

```python
languages.append("Go")

languages.extend(["JavaScript", "SQL"])
```

---

### Updating and Deleting Elements

Lists can be modified after creation.

Topics include:

- Updating values
- Deleting elements
- Using the `del` statement

Example:

```python
del languages[0]
```

---

### Splitting Strings

The `split()` method converts a string into a list.

Topics include:

- Splitting using spaces
- Splitting using delimiters
- Creating lists from strings

Example:

```python
text = "Python,SQL,AWS"

text.split(",")
```

---

### List Aliasing

Aliasing occurs when multiple variables reference the same list.

Topics include:

- Shared references
- Side effects
- Modifying aliased lists

Example:

```python
a = [1, 2, 3]
b = a
```

---

### Cloning Lists

Creating an independent copy of a list.

Topics include:

- Copying lists
- Avoiding aliasing
- Independent list modification

Example:

```python
b = a[:]
```

---

### Help Function

Using Python's built-in `help()` function to explore available methods and documentation.

Example:

```python
help(list)
```

---

## Examples Included

- Creating tuples
- Tuple indexing
- Tuple slicing
- Nested tuples
- Sorting tuples
- Creating lists
- List indexing and slicing
- Appending elements
- Extending lists
- Updating list values
- Deleting elements
- Splitting strings into lists
- List aliasing
- Cloning lists

---

## Skills Learned

- Working with tuples
- Understanding immutable data structures
- Working with mutable lists
- Using indexing and slicing
- Manipulating lists using built-in methods
- Working with nested data structures
- Avoiding aliasing issues
- Creating independent copies of lists

---

## Technologies Used

- Python 3
- Jupyter Notebook

---

## Repository Structure

```text
Python-Lists-and-Tuples/
│
├── Tuples
├── Nested Tuples
├── Lists
├── List Methods
├── List Operations
├── Aliasing and Cloning
├── Practice Examples
└── README.md
```

---

## Author

**Guruvendra Singh**

Data Engineering | Python | SQL | Snowflake | AWS