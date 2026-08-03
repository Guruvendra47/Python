# Python Data Types

## Project Overview

This repository provides a comprehensive introduction to **Python Data Types**, one of the core concepts in Python programming. It explains how Python represents different kinds of data, how to identify data types, and how to convert values between different types using type casting.

The repository includes practical examples demonstrating integers, floating-point numbers, strings, Booleans, and the `type()` function, helping learners build a solid foundation for Python programming.

The objective of this repository is to understand Python's built-in data types and develop the ability to work with different forms of data efficiently.

---

# Business Problem

Every Python application processes data in different formats such as numbers, text, and logical values. Understanding data types is essential because each type behaves differently and supports different operations.

Without a proper understanding of Python data types, developers may encounter unexpected errors, incorrect calculations, and inefficient code. Learning data types and type conversion enables developers to write accurate, reliable, and maintainable Python applications.

---

# Project Objectives

The primary objectives of this repository are to:

- Understand Python's built-in data types
- Identify the data type of an object using the `type()` function
- Differentiate between integers, floating-point numbers, strings, and Booleans
- Perform type conversion (type casting)
- Understand data representation in Python
- Build a strong programming foundation for advanced Python concepts

---

# Topics Covered

## Introduction to Python Data Types

This repository introduces the concept of data types and explains how Python classifies different kinds of data.

Topics include:

- What is a data type?
- Why data types are important
- Python's dynamic typing system

---

## Integer (`int`)

Integers represent whole numbers without decimal values.

Examples:

```python
10
-25
1000
0
```

Topics covered:

- Positive integers
- Negative integers
- Integer representation
- Integer range

---

## Float (`float`)

Floating-point numbers represent real numbers containing decimal values.

Examples:

```python
3.14
10.5
0.25
-7.89
```

Topics covered:

- Decimal numbers
- Precision
- Real number representation

---

## String (`str`)

Strings are ordered sequences of characters used to represent text.

Examples:

```python
"Python"
'Data Engineering'
"123"
```

Topics covered:

- Creating strings
- Character sequences
- Text representation

---

## Boolean (`bool`)

Boolean values represent logical outcomes.

Possible values:

```python
True
False
```

Topics covered:

- Boolean values
- Logical representation
- Boolean operations

---

## Identifying Data Types

Python provides the built-in `type()` function to determine the data type of an object.

Example:

```python
x = 100
print(type(x))
```

Output:

```python
<class 'int'>
```

---

## Type Casting

The repository demonstrates converting values from one data type to another.

Supported conversions include:

- Integer to Float
- Float to Integer
- Integer to String
- Float to String
- String to Integer
- Integer to Boolean
- Float to Boolean
- Boolean to Integer
- Boolean to Float

---

## Integer to Float

Example:

```python
int_value = 2
float_value = float(int_value)

print(float_value)
```

Output:

```
2.0
```

---

## Float to Integer

Example:

```python
number = 1.9
integer = int(number)
```

Output:

```
1
```

**Note:** The decimal portion is discarded during conversion.

---

## String to Integer

Example:

```python
value = "100"
number = int(value)
```

If the string does not contain a valid integer, Python raises an exception.

Example:

```python
int("Python")
```

Result:

```
ValueError
```

---

## Numeric to String

Examples:

```python
str(100)

str(15.5)
```

These conversions are useful when displaying numbers as text.

---

## Boolean Conversion

Python allows conversion between numeric values and Boolean values.

Examples:

```python
bool(1)
```

Output:

```python
True
```

```python
bool(0)
```

Output:

```python
False
```

Similarly,

```python
int(True)
```

Output:

```
1
```

```python
int(False)
```

Output:

```
0
```

---

# Repository Structure

```
Python-Data-Types/
│
├── Introduction to Data Types
├── Integer Data Type
├── Float Data Type
├── String Data Type
├── Boolean Data Type
├── Type Identification
├── Type Casting
├── Practical Examples
│
└── README.md
```

---

# Technologies Used

| Category | Technology |
|-----------|------------|
| Programming Language | Python 3 |
| Development Environment | Jupyter Notebook |
| Concepts | Python Data Types |

---

# Key Concepts

The repository demonstrates:

- Built-in Python data types
- Data representation
- Type checking
- Type conversion
- Numeric data handling
- Text data representation
- Boolean logic
- Safe type casting practices

---

# Skills Demonstrated

This project demonstrates proficiency in:

- Python Fundamentals
- Data Types
- Type Casting
- Data Conversion
- Boolean Logic
- Problem Solving
- Basic Python Programming

---

# Learning Outcomes

After completing this repository, learners will be able to:

- Understand Python's built-in data types
- Identify object types using the `type()` function
- Convert values between different data types
- Work confidently with integers, floats, strings, and Booleans
- Recognize common type conversion errors
- Apply data type concepts in real-world Python programs

---

# Applications

The concepts covered in this repository are applicable to:

- Software Development
- Data Engineering
- Data Analysis
- Automation
- Machine Learning
- Web Development
- Scripting
- Scientific Computing

---

# Future Enhancements

Future repositories will expand on these concepts by covering:

- Variables
- Operators
- Expressions
- Conditional Statements
- Loops
- Functions
- Collections (Lists, Tuples, Sets, Dictionaries)
- Object-Oriented Programming
- Exception Handling

---

# Author

**Guruvendra Singh**

Data Engineering | Python | SQL | Snowflake | AWS | ETL | Automation
