# Lists & Tuples Cheat Sheet

---

# Lists

## Create a List

**Description:** Create an ordered, mutable collection.

**Syntax**

```python
list_name = [item1, item2, item3]
```

**Example**

```python
fruits = ["apple", "banana", "orange"]
```

---

## Indexing

**Description:** Access elements by index.

**Syntax**

```python
list_name[index]
```

**Example**

```python
numbers = [10, 20, 30]

numbers[0]
numbers[-1]
```

---

## Slicing

**Description:** Access a range of elements.

**Syntax**

```python
list_name[start:end:step]
```

**Example**

```python
numbers = [1,2,3,4,5]

numbers[1:4]
numbers[:3]
numbers[2:]
numbers[::2]
```

---

## append()

**Description:** Add an element to the end.

**Syntax**

```python
list_name.append(element)
```

**Example**

```python
fruits = ["apple", "banana"]

fruits.append("mango")
```

---

## extend()

**Description:** Add multiple elements.

**Syntax**

```python
list_name.extend(iterable)
```

**Example**

```python
fruits = ["apple"]

fruits.extend(["banana", "orange"])
```

---

## insert()

**Description:** Insert an element at a specific position.

**Syntax**

```python
list_name.insert(index, element)
```

**Example**

```python
numbers = [1,2,3]

numbers.insert(1,100)
```

---

## remove()

**Description:** Remove the first matching value.

**Syntax**

```python
list_name.remove(value)
```

**Example**

```python
numbers = [1,2,3,2]

numbers.remove(2)
```

---

## pop()

**Description:** Remove and return an element.

**Syntax**

```python
list_name.pop(index)
```

or

```python
list_name.pop()
```

**Example**

```python
numbers = [10,20,30]

numbers.pop()

numbers.pop(1)
```

---

## del

**Description:** Delete an element by index.

**Syntax**

```python
del list_name[index]
```

**Example**

```python
numbers = [10,20,30]

del numbers[1]
```

---

## copy()

**Description:** Create a shallow copy.

**Syntax**

```python
new_list = list_name.copy()
```

**Example**

```python
numbers = [1,2,3]

new_numbers = numbers.copy()
```

---

## count()

**Description:** Count occurrences.

**Syntax**

```python
list_name.count(value)
```

**Example**

```python
numbers = [1,2,2,3]

numbers.count(2)
```

---

## sort()

**Description:** Sort a list.

**Syntax**

```python
list_name.sort()
```

Descending

```python
list_name.sort(reverse=True)
```

**Example**

```python
numbers = [5,2,9]

numbers.sort()

numbers.sort(reverse=True)
```

---

## reverse()

**Description:** Reverse list order.

**Syntax**

```python
list_name.reverse()
```

**Example**

```python
numbers = [1,2,3]

numbers.reverse()
```

---

## Modify List

**Description:** Change an existing element.

**Syntax**

```python
list_name[index] = value
```

**Example**

```python
numbers = [10,20,30]

numbers[1] = 100
```

---

# Tuples

## Create a Tuple

**Description:** Create an ordered, immutable collection.

**Syntax**

```python
tuple_name = (item1, item2, item3)
```

**Example**

```python
fruits = ("apple", "banana", "orange")
```

---

## Indexing

**Description:** Access tuple elements.

**Syntax**

```python
tuple_name[index]
```

**Example**

```python
numbers = (10,20,30)

numbers[0]
```

---

## Slicing

**Description:** Access a range of elements.

**Syntax**

```python
tuple_name[start:end:step]
```

**Example**

```python
numbers = (1,2,3,4,5)

numbers[1:4]
```

---

## count()

**Description:** Count occurrences.

**Syntax**

```python
tuple_name.count(value)
```

**Example**

```python
fruits = ("apple","banana","apple")

fruits.count("apple")
```

---

## index()

**Description:** Find first occurrence.

**Syntax**

```python
tuple_name.index(value)
```

**Example**

```python
fruits = ("apple","banana","orange")

fruits.index("banana")
```

---

## len()

**Description:** Number of elements.

**Syntax**

```python
len(tuple_name)
```

**Example**

```python
numbers = (1,2,3)

len(numbers)
```

---

## sum()

**Description:** Sum numeric values.

**Syntax**

```python
sum(tuple_name)
```

**Example**

```python
numbers = (10,20,30)

sum(numbers)
```

---

## min()

**Description:** Smallest value.

**Syntax**

```python
min(tuple_name)
```

**Example**

```python
numbers = (10,5,20)

min(numbers)
```

---

## max()

**Description:** Largest value.

**Syntax**

```python
max(tuple_name)
```

**Example**

```python
numbers = (10,5,20)

max(numbers)
```

---

# Quick Summary

| Lists | Tuples |
|--------|---------|
| Mutable | Immutable |
| Uses `[]` | Uses `()` |
| Can add/remove items | Cannot modify items |
| More methods available | Limited methods |
| append(), extend(), insert(), remove(), pop(), sort(), reverse() | count(), index() |