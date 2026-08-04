# Python Dictionaries

## Overview

This repository introduces **Python Dictionaries**, a built-in data structure used to store data as **key-value pairs**. It covers creating dictionaries, accessing values, adding and removing entries, checking for keys, and using common dictionary methods.

Dictionaries provide an efficient way to organize and retrieve data using unique keys instead of numeric indexes.

---

## Topics Covered

### Introduction to Dictionaries

A dictionary is a collection of key-value pairs enclosed in curly braces `{}`.

Topics include:

- Creating dictionaries
- Key-value pairs
- Dictionary syntax
- Assigning dictionaries to variables

Example:

```python
album = {
    "Back in Black": 1980,
    "Thriller": 1982,
    "The Bodyguard": 1992
}
```

---

### Dictionary Keys

Keys uniquely identify values stored in a dictionary.

Topics include:

- Unique keys
- Immutable keys
- String keys
- Accessing data using keys

Example:

```python
album["Back in Black"]
```

---

### Dictionary Values

Values store the information associated with each key.

Topics include:

- Immutable values
- Mutable values
- Duplicate values

Example:

```python
{
    "Album": "Thriller",
    "Year": 1982
}
```

---

### Accessing Dictionary Elements

Dictionary values are retrieved using their corresponding keys.

Example:

```python
album["The Bodyguard"]
```

---

### Adding Items

New key-value pairs can be added by assigning a value to a new key.

Example:

```python
album["Graduation"] = 2007
```

---

### Updating Items

Existing values can be modified by assigning a new value to an existing key.

Example:

```python
album["Thriller"] = 1983
```

---

### Removing Items

Dictionary entries can be removed using the `del` statement.

Example:

```python
del album["Thriller"]
```

---

### Checking Keys

The `in` operator checks whether a key exists in a dictionary.

Example:

```python
"Thriller" in album
```

Returns:

```python
True
```

or

```python
False
```

---

### Dictionary Methods

Common built-in methods include:

#### Retrieve All Keys

```python
album.keys()
```

#### Retrieve All Values

```python
album.values()
```

---

## Examples Included

- Creating dictionaries
- Accessing values using keys
- Adding key-value pairs
- Updating existing values
- Removing dictionary entries
- Checking if a key exists
- Retrieving all keys
- Retrieving all values

---

## Skills Learned

- Creating Python dictionaries
- Working with key-value pairs
- Accessing dictionary elements
- Updating and deleting dictionary entries
- Using dictionary methods
- Checking dictionary membership
- Organizing structured data efficiently

---

## Technologies Used

- Python 3
- Jupyter Notebook

---

## Repository Structure

```text
Python-Dictionaries/
│
├── Dictionary Basics
├── Accessing Elements
├── Dictionary Methods
├── Dictionary Operations
├── Practice Examples
└── README.md
```

---

## Author

**Guruvendra Singh**

Data Engineering | Python | SQL | Snowflake | AWS