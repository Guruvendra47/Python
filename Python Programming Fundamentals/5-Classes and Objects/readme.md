# Python Objects and Classes

## Overview

This repository introduces **Python Objects and Classes**, the foundation of Object-Oriented Programming (OOP). It explains how Python treats everything as an object, how to create custom classes, define data attributes and methods, initialize objects using constructors, and interact with objects through methods.

Understanding objects and classes allows developers to organize code efficiently, improve reusability, and model real-world entities.

---

## Topics Covered

### Introduction to Objects

In Python, everything is an object, including:

- Integers
- Floats
- Strings
- Lists
- Dictionaries
- Booleans

Every object has:

- A type
- An internal representation
- Methods that operate on the object's data

Example:

```python
number = 10
text = "Python"
items = [1, 2, 3]
```

---

### Object Types

An object is an instance of a particular type (class).

Topics include:

- Integer objects
- String objects
- List objects
- Dictionary objects
- Boolean objects

Example:

```python
type(10)

type("Hello")

type([1, 2, 3])

type({"A": 1})
```

---

### The `type()` Function

The `type()` function identifies the type of an object.

Example:

```python
print(type(5))

print(type("Python"))

print(type([1, 2, 3]))
```

---

### Object Methods

Methods are functions associated with an object that operate on its data.

Topics include:

- Calling methods
- Modifying object state
- Working with list methods

Examples:

```python
numbers = [4, 1, 3]

numbers.sort()

numbers.reverse()
```

---

### Introduction to Classes

A class is a blueprint used to create objects.

Topics include:

- Creating custom classes
- Class definition
- Object instantiation
- Blueprints for objects

Example:

```python
class Circle(object):
    pass
```

---

### Data Attributes

Data attributes store information that defines an object.

Examples:

For a **Circle**:

- Radius
- Color

For a **Rectangle**:

- Height
- Width
- Color

---

### Constructors (`__init__()`)

The constructor initializes an object's data attributes when it is created.

Topics include:

- `__init__()`
- Object initialization
- Constructor parameters

Example:

```python
class Circle(object):

    def __init__(self, radius, color):
        self.radius = radius
        self.color = color
```

---

### The `self` Parameter

`self` refers to the current object instance.

It is used to access and modify the object's attributes inside the class.

Example:

```python
self.radius

self.color
```

---

### Creating Objects

Objects are created by calling the class constructor.

Example:

```python
red_circle = Circle(3, "red")

blue_circle = Circle(10, "blue")
```

---

### Accessing Data Attributes

Object attributes can be accessed using dot notation.

Example:

```python
print(red_circle.radius)

print(red_circle.color)
```

---

### Updating Data Attributes

Attributes can be modified directly.

Example:

```python
red_circle.color = "green"
```

---

### Methods

Methods define behaviors that operate on an object's data.

Example:

```python
class Circle(object):

    def add_radius(self, value):
        self.radius += value
```

---

### Calling Methods

Methods are called using dot notation.

Example:

```python
red_circle.add_radius(5)
```

---

### Default Constructor Parameters

Constructors can provide default values for attributes.

Example:

```python
class Circle(object):

    def __init__(self, radius=3, color="red"):
        self.radius = radius
        self.color = color
```

---

### Rectangle Class

The module also demonstrates creating a `Rectangle` class.

Topics include:

- Height
- Width
- Color
- Rectangle objects

Example:

```python
rectangle = Rectangle(2, 4, "blue")
```

---

### Object Inspection with `dir()`

The `dir()` function lists an object's available attributes and methods.

Example:

```python
dir(red_circle)
```

---

## Examples Included

- Creating custom classes
- Creating objects
- Using constructors
- Initializing object attributes
- Accessing attributes
- Updating attributes
- Creating methods
- Calling methods
- Using default constructor values
- Creating Circle objects
- Creating Rectangle objects
- Inspecting objects with `dir()`

---

## Skills Learned

- Understanding objects in Python
- Identifying object types
- Creating custom classes
- Using constructors (`__init__`)
- Working with `self`
- Creating and modifying object attributes
- Defining and calling methods
- Creating reusable object-oriented code
- Inspecting objects using `dir()`

---

## Technologies Used

- Python 3
- Jupyter Notebook

---

## Repository Structure

```text
Python-Objects-and-Classes/
│
├── Introduction to Objects
├── Object Types
├── The type() Function
├── Classes
├── Constructors
├── Data Attributes
├── Methods
├── Circle Class
├── Rectangle Class
├── Object Inspection
├── Practice Examples
└── README.md
```

---

## Author

**Guruvendra Singh**

Data Engineering | Python | SQL | Snowflake | AWS