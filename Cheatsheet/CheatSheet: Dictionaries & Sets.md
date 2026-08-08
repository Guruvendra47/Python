# Dictionaries & Sets Cheat Sheet

---

# Dictionaries

## Creating a Dictionary

**Description:**  
A dictionary stores data as **key-value pairs**.

**Syntax**

```python
dictionary_name = {
    key1: value1,
    key2: value2
}
```

**Example**

```python
student = {
    "name": "John",
    "age": 22,
    "city": "Toronto"
}
```

---

## Accessing Values

**Description:**  
Access a value using its key.

**Syntax**

```python
dictionary_name[key]
```

**Example**

```python
student["name"]
student["age"]
```

---

## Add or Modify

**Description:**  
Add a new key-value pair or update an existing value.

**Syntax**

```python
dictionary_name[key] = value
```

**Example**

```python
student["grade"] = "A"

student["age"] = 23
```

---

## del

**Description:**  
Delete a key-value pair.

**Syntax**

```python
del dictionary_name[key]
```

**Example**

```python
del student["city"]
```

---

## Key Existence

**Description:**  
Check whether a key exists.

**Syntax**

```python
key in dictionary_name
```

**Example**

```python
"name" in student

"salary" in student
```

---

## keys()

**Description:**  
Return all dictionary keys.

**Syntax**

```python
dictionary_name.keys()
```

**Example**

```python
student.keys()
```

---

## values()

**Description:**  
Return all dictionary values.

**Syntax**

```python
dictionary_name.values()
```

**Example**

```python
student.values()
```

---

## items()

**Description:**  
Return all key-value pairs.

**Syntax**

```python
dictionary_name.items()
```

**Example**

```python
student.items()
```

---

# Sets

## Defining Sets

**Description:**  
Create a set that stores **unique** values.

**Syntax**

```python
set_name = {value1, value2, value3}
```

or

```python
set_name = set(iterable)
```

**Example**

```python
fruits = {"apple", "banana", "orange"}

numbers = set([1,2,2,3,4])
```

---

## add()

**Description:**  
Add an element to a set.

**Syntax**

```python
set_name.add(element)
```

**Example**

```python
fruits.add("mango")
```

---

## remove()

**Description:**  
Remove an element from a set.

**Syntax**

```python
set_name.remove(element)
```

**Example**

```python
fruits.remove("banana")
```

---

## in

**Description:**  
Check if an element exists.

**Syntax**

```python
element in set_name
```

**Example**

```python
"apple" in fruits

"grape" in fruits
```

---

## issubset()

**Description:**  
Check whether one set is a subset of another.

**Syntax**

```python
set1.issubset(set2)
```

**Example**

```python
A = {1,2}
B = {1,2,3}

A.issubset(B)
```

---

## issuperset()

**Description:**  
Check whether one set is a superset of another.

**Syntax**

```python
set1.issuperset(set2)
```

**Example**

```python
B = {1,2,3}
A = {1,2}

B.issuperset(A)
```

---

## Set Operations

### Union

**Syntax**

```python
set1.union(set2)

# or

set1 | set2
```

**Example**

```python
A.union(B)

A | B
```

---

### Intersection

**Syntax**

```python
set1.intersection(set2)

# or

set1 & set2
```

**Example**

```python
A.intersection(B)

A & B
```

---

### Difference

**Syntax**

```python
set1.difference(set2)

# or

set1 - set2
```

**Example**

```python
A.difference(B)

A - B
```

---

### Symmetric Difference

**Syntax**

```python
set1.symmetric_difference(set2)

# or

set1 ^ set2
```

**Example**

```python
A.symmetric_difference(B)

A ^ B
```

---

# Quick Summary

| Dictionaries | Sets |
|--------------|------|
| Store key-value pairs | Store unique values |
| Mutable | Mutable |
| Ordered (Python 3.7+) | Unordered |
| Access by key | No indexing |
| Duplicate keys not allowed | Duplicate values removed |
| Common methods: `keys()`, `values()`, `items()` | Common methods: `add()`, `remove()`, `union()`, `intersection()` |