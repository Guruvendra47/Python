# Python File Handling, Pandas & NumPy Cheat Sheet

## Overview

This repository provides a quick reference to essential **Python File Handling**, **Pandas**, and **NumPy** operations. It covers commonly used methods, syntax, and examples for reading and writing files, manipulating DataFrames, and performing numerical computations with NumPy arrays.

This cheat sheet serves as a practical reference for Python programming, data analysis, and data engineering tasks.

---

## Topics Covered

### Python File Handling

Topics include:

- File opening modes
- Reading files
- Writing files
- Appending files
- Iterating through files
- Opening and closing files
- Using the `with` statement

---

### File Opening Modes

Common file modes:

| Mode | Description |
|------|-------------|
| `r` | Read |
| `w` | Write (Overwrite) |
| `a` | Append |
| `r+` | Read & Write |
| `b` | Binary Mode |

---

### File Reading Methods

Methods covered:

- `read()`
- `readline()`
- `readlines()`

---

### File Writing Methods

Methods covered:

- `write()`
- `writelines()`

---

### File Iteration

Topics include:

- Reading files line by line
- Using loops with files

---

### File Management

Topics include:

- `open()`
- `close()`
- `with open()`

---

## Pandas

Topics include:

- Importing Pandas
- Reading CSV files
- Reading Excel files
- Creating DataFrames
- Selecting columns
- Filtering rows
- Grouping data
- Merging DataFrames
- Data cleaning
- Saving DataFrames

---

### Importing Pandas

```python
import pandas as pd
```

---

### Reading Data

Methods covered:

- `read_csv()`
- `read_excel()`

---

### DataFrame Operations

Topics include:

- Column selection
- Multiple column selection
- `head()`
- `tail()`
- `info()`
- `describe()`

---

### Data Cleaning

Methods covered:

- `drop()`
- `dropna()`
- `replace()`
- `duplicated()`

---

### Data Analysis

Topics include:

- Conditional filtering
- `groupby()`
- `merge()`

---

### Exporting Data

Method covered:

- `to_csv()`

---

## NumPy

Topics include:

- Importing NumPy
- Creating arrays
- One-dimensional arrays
- Two-dimensional arrays
- Array operations

---

### Importing NumPy

```python
import numpy as np
```

---

### Creating Arrays

Methods covered:

- `np.array()` (1D)
- `np.array()` (2D)

---

### Array Operations

Methods covered:

- `np.mean()`
- `np.sum()`
- `np.min()`
- `np.max()`
- `np.dot()`

---

## Examples Included

- Reading text files
- Writing and appending files
- Using `with open()`
- Loading CSV and Excel files
- Creating DataFrames
- Selecting and filtering data
- Cleaning datasets
- Grouping and merging data
- Saving processed data
- Creating NumPy arrays
- Performing mathematical operations

---

## Skills Learned

- Working with Python file operations
- Reading and writing files
- Using Pandas for data manipulation
- Cleaning and analyzing datasets
- Working with NumPy arrays
- Performing numerical computations
- Building efficient data processing workflows

---

## Technologies Used

- Python 3
- Pandas
- NumPy
- Jupyter Notebook

---

## Repository Structure

```text
Python-File-Handling-Pandas-NumPy/
│
├── File Handling
├── Pandas
├── NumPy
├── Cheat Sheet
├── Practice Examples
└── README.md
```

---

## Author

**Guruvendra Singh**

Data Engineering | Python | SQL | Snowflake | AWS