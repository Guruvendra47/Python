# Python Basics Cheat Sheet

---

## Comments

**Description:**  
Ignored by the Python interpreter.

**Syntax**

```python
# comment
```

**Example**

```python
# This is a comment
```

---

## Variable Assignment

**Description:**  
Assign a value to a variable.

**Syntax**

```python
variable_name = value
```

**Example**

```python
name = "John"
age = 25
```

---

## Data Types

**Description:**  
Common Python data types.

**Syntax**

```python
variable = value
```

**Example**

```python
x = 7              # int
y = 12.5           # float
is_valid = True    # bool
name = "John"      # string
```

---

## print()

**Description:**  
Display output.

**Syntax**

```python
print(value)
```

**Example**

```python
print("Hello World")
print(x)
```

---

## String Concatenation

**Description:**  
Join two or more strings.

**Syntax**

```python
string1 + string2
```

**Example**

```python
result = "Hello " + "John"
```

---

## Python Operators

**Description:**  
Basic arithmetic operators.

| Operator | Description |
|----------|-------------|
| + | Addition |
| - | Subtraction |
| * | Multiplication |
| / | Division |
| // | Floor Division |
| % | Modulus |
| ** | Exponent |

**Syntax**

```python
result = value1 operator value2
```

**Example**

```python
x = 9
y = 4

x + y
x - y
x * y
x / y
x // y
x % y
x ** y
```

---

## Indexing

**Description:**  
Access a character by its position.

**Syntax**

```python
string[index]
```

**Example**

```python
text = "Hello"

text[0]
text[4]
```

---

## Slicing

**Description:**  
Extract part of a string.

**Syntax**

```python
string[start:end]
```

**Example**

```python
text = "Hello"

text[0:2]
text[1:4]
```

---

## len()

**Description:**  
Returns the length of a string.

**Syntax**

```python
len(string)
```

**Example**

```python
text = "Hello"

len(text)
```

---

## upper()

**Description:**  
Convert text to uppercase.

**Syntax**

```python
string.upper()
```

**Example**

```python
text = "Hello"

text.upper()
```

---

## lower()

**Description:**  
Convert text to lowercase.

**Syntax**

```python
string.lower()
```

**Example**

```python
text = "Hello"

text.lower()
```

---

## strip()

**Description:**  
Remove leading and trailing spaces.

**Syntax**

```python
string.strip()
```

**Example**

```python
text = "  Hello  "

text.strip()
```

---

## replace()

**Description:**  
Replace part of a string.

**Syntax**

```python
string.replace(old, new)
```

**Example**

```python
text = "Hello"

text.replace("Hello", "Hi")
```

---

## split()

**Description:**  
Split a string into a list.

**Syntax**

```python
string.split(separator)
```

**Example**

```python
text = "Apple,Banana,Mango"

text.split(",")
```

---

# Summary

- `#` → Comment
- `=` → Assign value
- `print()` → Display output
- `+` → Concatenate strings
- `len()` → Length of string
- `[]` → Indexing & Slicing
- `upper()` → Uppercase
- `lower()` → Lowercase
- `strip()` → Remove spaces
- `replace()` → Replace text
- `split()` → Convert string to list