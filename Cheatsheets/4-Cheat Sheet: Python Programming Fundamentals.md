# Python Programming Fundamentals Cheat Sheet

---

## Equal (==)

**Description:** Checks if two values are equal.

**Syntax**

```python
value1 == value2
```

**Example**

```python
5 == 5

age = 25
age == 30
```

---

## Not Equal (!=)

**Description:** Checks if two values are not equal.

**Syntax**

```python
value1 != value2
```

**Example**

```python
10 != 20

count = 0
count != 0
```

---

## Greater Than (>)

**Description:** Checks if the left value is greater than the right value.

**Syntax**

```python
value1 > value2
```

**Example**

```python
9 > 6

age > max_age
```

---

## Greater Than or Equal (>=)

**Description:** Checks if the left value is greater than or equal to the right value.

**Syntax**

```python
value1 >= value2
```

**Example**

```python
5 >= 5

quantity >= minimum
```

---

## Less Than (<)

**Description:** Checks if the left value is less than the right value.

**Syntax**

```python
value1 < value2
```

**Example**

```python
4 < 6

score < passing_score
```

---

## Less Than or Equal (<=)

**Description:** Checks if the left value is less than or equal to the right value.

**Syntax**

```python
value1 <= value2
```

**Example**

```python
5 <= 5

size <= max_size
```

---

## AND

**Description:** Returns **True** if both conditions are True.

**Syntax**

```python
condition1 and condition2
```

**Example**

```python
marks >= 80 and attendance >= 85
```

---

## OR

**Description:** Returns **True** if at least one condition is True.

**Syntax**

```python
condition1 or condition2
```

**Example**

```python
grade == 11 or grade == 12
```

---

## NOT

**Description:** Reverses a Boolean value.

**Syntax**

```python
not condition
```

**Example**

```python
not isLocked
```

---

## if Statement

**Description:** Execute code when a condition is True.

**Syntax**

```python
if condition:
    # code
```

**Example**

```python
if temperature > 30:
    print("Hot day")
```

---

## if-else Statement

**Description:** Execute one block if True, another if False.

**Syntax**

```python
if condition:
    # code
else:
    # code
```

**Example**

```python
if age >= 18:
    print("Adult")
else:
    print("Minor")
```

---

## if-elif-else Statement

**Description:** Check multiple conditions.

**Syntax**

```python
if condition1:
    # code
elif condition2:
    # code
else:
    # code
```

**Example**

```python
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
else:
    print("C")
```

---

## range()

**Description:** Generate a sequence of numbers.

**Syntax**

```python
range(stop)

range(start, stop)

range(start, stop, step)
```

**Example**

```python
range(5)

range(1,10)

range(1,11,2)
```

---

## for Loop

**Description:** Iterate over a sequence.

**Syntax**

```python
for variable in sequence:
    # code
```

**Example**

```python
for i in range(5):
    print(i)
```

---

## while Loop

**Description:** Repeat while condition is True.

**Syntax**

```python
while condition:
    # code
```

**Example**

```python
count = 0

while count < 5:
    print(count)
    count += 1
```

---

## Loop Controls

### break

**Syntax**

```python
break
```

### continue

**Syntax**

```python
continue
```

**Example**

```python
for i in range(5):
    if i == 3:
        break
```

```python
for i in range(5):
    if i == 3:
        continue
```

---

## Define Function

**Description:** Create a reusable function.

**Syntax**

```python
def function_name(parameters):
    # code
```

**Example**

```python
def greet(name):
    print(name)
```

---

## Function Call

**Description:** Execute a function.

**Syntax**

```python
function_name(arguments)
```

**Example**

```python
greet("Alice")
```

---

## return

**Description:** Return a value from a function.

**Syntax**

```python
return value
```

**Example**

```python
def add(a,b):
    return a+b
```

---

## try-except

**Description:** Handle exceptions.

**Syntax**

```python
try:
    # code
except ExceptionType:
    # code
```

**Example**

```python
try:
    num = int(input())
except ValueError:
    print("Invalid")
```

---

## try-except-else

**Description:** Execute else if no exception occurs.

**Syntax**

```python
try:
    # code
except ExceptionType:
    # code
else:
    # code
```

**Example**

```python
try:
    num = int(input())
except ValueError:
    print("Invalid")
else:
    print(num)
```

---

## try-except-finally

**Description:** finally always executes.

**Syntax**

```python
try:
    # code
except ExceptionType:
    # code
finally:
    # code
```

**Example**

```python
try:
    file = open("data.txt")
except FileNotFoundError:
    print("Not Found")
finally:
    file.close()
```

---

## Class Definition

**Description:** Define a class.

**Syntax**

```python
class ClassName:

    def __init__(self, parameters):
        self.attribute = value
```

**Example**

```python
class Person:

    def __init__(self, name):
        self.name = name
```

---

## Object Creation

**Description:** Create an object from a class.

**Syntax**

```python
object_name = ClassName(arguments)
```

**Example**

```python
person = Person("Alice")
```

---

# Quick Summary

| Topic | Syntax |
|--------|--------|
| Equal | `==` |
| Not Equal | `!=` |
| Greater Than | `>` |
| Less Than | `<` |
| Greater/Equal | `>=` |
| Less/Equal | `<=` |
| AND | `and` |
| OR | `or` |
| NOT | `not` |
| If | `if` |
| Loop | `for`, `while` |
| Function | `def` |
| Return | `return` |
| Exception | `try...except` |
| Class | `class` |
| Object | `ClassName()` |