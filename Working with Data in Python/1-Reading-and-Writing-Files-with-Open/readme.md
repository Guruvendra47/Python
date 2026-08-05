# Python File Handling

## Overview

This repository introduces **Python File Handling**, which enables programs to read, write, append, and manage files efficiently. It covers file operations using the built-in `open()` function, different file modes, reading file contents, writing data to files, appending new content, and copying files.

File handling is an essential skill for working with text files, logs, configuration files, datasets, and many real-world applications.

---

## Topics Covered

### Opening Files

Python uses the built-in `open()` function to create a file object.

Topics include:

- Opening existing files
- Creating new files
- File paths
- File objects

Example:

```python
file = open("Example1.txt", "r")
```

---

### File Modes

Python supports different modes for opening files.

Common modes include:

| Mode | Description |
|------|-------------|
| `r` | Read |
| `w` | Write (overwrite) |
| `a` | Append |

---

### Reading Files

Python provides multiple methods to read file contents.

Topics include:

- Reading the entire file
- Reading individual lines
- Reading multiple lines
- Reading specific characters

Methods covered:

- `read()`
- `readline()`
- `readlines()`

Example:

```python
with open("Example1.txt", "r") as file:
    content = file.read()
```

---

### Using the `with` Statement

The `with` statement automatically closes the file after operations are completed.

Benefits include:

- Automatic file closing
- Cleaner code
- Better resource management

Example:

```python
with open("Example1.txt", "r") as file:
    content = file.read()
```

---

### File Attributes

Python provides useful file attributes.

Topics include:

- File name
- File mode

Example:

```python
file.name

file.mode
```

---

### Writing Files

Files can be created or overwritten using write mode.

Topics include:

- Creating files
- Overwriting files
- Writing text
- New line characters (`\n`)

Example:

```python
with open("Example2.txt", "w") as file:
    file.write("Hello World\n")
```

---

### Writing Multiple Lines

Multiple lines can be written using loops.

Example:

```python
lines = ["Line A\n", "Line B\n", "Line C\n"]

with open("Example2.txt", "w") as file:
    for line in lines:
        file.write(line)
```

---

### Appending to Files

Append mode allows new content to be added without overwriting existing data.

Example:

```python
with open("Example2.txt", "a") as file:
    file.write("New Line\n")
```

---

### Copying Files

A file can be copied by reading from one file and writing to another.

Example:

```python
with open("Example1.txt", "r") as readfile:
    with open("Example3.txt", "w") as writefile:
        for line in readfile:
            writefile.write(line)
```

---

## Examples Included

- Opening files
- Reading complete files
- Reading line by line
- Reading specific characters
- Using `read()`
- Using `readline()`
- Using `readlines()`
- Writing files
- Appending data
- Writing lists to files
- Copying files
- Using the `with` statement

---

## Skills Learned

- Opening and closing files
- Using different file modes
- Reading text files
- Writing and appending data
- Managing files safely with `with`
- Accessing file attributes
- Copying file contents
- Working with text data in Python

---

## Technologies Used

- Python 3
- Jupyter Notebook

---

## Repository Structure

```text
Python-File-Handling/
│
├── Reading Files
├── Writing Files
├── Appending Files
├── Copying Files
├── File Operations
├── Practice Examples
└── README.md
```

---

## Author

**Guruvendra Singh**

Data Engineering | Python | SQL | Snowflake | AWS