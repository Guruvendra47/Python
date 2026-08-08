# Cheat Sheet: Working with Data in Python

---

# Reading and Writing Files

## File Opening Modes

Different modes to open files for specific operations.

**Syntax**

```python
"r"   # Read
"w"   # Write
"a"   # Append
"r+"  # Read and Write
"b"   # Binary Mode
```

---

## File Reading Methods

Different methods to read file content in various ways.

**Syntax**

```python
file.read()

file.readline()

file.readlines()
```

**Example**

```python
with open("data.txt", "r") as file:
    content = file.read()
    line = file.readline()
    lines = file.readlines()
```

---

## File Writing Methods

Different write methods to write content to a file.

**Syntax**

```python
file.write(content)

file.writelines(lines)
```

**Example**

```python
lines = ["Hello\n", "World\n"]

with open("output.txt", "w") as file:
    file.writelines(lines)
```

---

## Iterating Over Lines

Iterates through each line in a file using a loop.

**Syntax**

```python
for line in file:
    # code
```

**Example**

```python
with open("data.txt", "r") as file:
    for line in file:
        print(line)
```

---

## open() and close()

Opens a file and explicitly closes it.

**Syntax**

```python
file = open(filename, mode)

file.close()
```

**Example**

```python
file = open("data.txt", "r")
content = file.read()
file.close()
```

---

## with open()

Automatically closes the file after use.

**Syntax**

```python
with open(filename, mode) as file:
    # code
```

**Example**

```python
with open("data.txt", "r") as file:
    content = file.read()
```

---

# Pandas

## Import pandas

Imports the Pandas library.

**Syntax**

```python
import pandas as pd
```

**Example**

```python
import pandas as pd
```

---

## read_csv()

Reads a CSV file.

**Syntax**

```python
df = pd.read_csv("file.csv")
```

**Example**

```python
df = pd.read_csv("employees.csv")
```

---

## read_excel()

Reads an Excel file.

**Syntax**

```python
df = pd.read_excel("file.xlsx")
```

**Example**

```python
df = pd.read_excel("employees.xlsx")
```

---

## to_csv()

Writes a DataFrame to a CSV file.

**Syntax**

```python
df.to_csv("output.csv", index=False)
```

**Example**

```python
df.to_csv("output.csv", index=False)
```

---

## Access Columns

Access one or more columns.

**Syntax**

```python
df["column"]

df[["column1", "column2"]]
```

**Example**

```python
df["Age"]

df[["Name", "Age"]]
```

---

## describe()

Displays summary statistics.

**Syntax**

```python
df.describe()
```

**Example**

```python
df.describe()
```

---

## drop()

Removes rows or columns.

**Syntax**

```python
df.drop(columns=["column_name"])

df.drop(index=[0, 1])
```

**Example**

```python
df.drop(columns=["Salary"], inplace=True)

df.drop(index=[5], inplace=True)
```

---

## dropna()

Removes missing values.

**Syntax**

```python
df.dropna(axis=0, inplace=True)
```

**Example**

```python
df.dropna(inplace=True)
```

---

## duplicated()

Checks duplicate rows.

**Syntax**

```python
df.duplicated()
```

**Example**

```python
duplicates = df[df.duplicated()]
```

---

## Filter Rows

Returns rows matching a condition.

**Syntax**

```python
filtered_df = df[condition]
```

**Example**

```python
filtered_df = df[df["Age"] > 30]
```

---

## groupby()

Groups data for aggregation.

**Syntax**

```python
df.groupby("column")

df.groupby("column").agg({"column":"function"})
```

**Example**

```python
df.groupby("Department").agg({"Salary":"mean"})
```

---

## head()

Displays first rows.

**Syntax**

```python
df.head(n)
```

**Example**

```python
df.head(5)
```

---

## info()

Displays DataFrame information.

**Syntax**

```python
df.info()
```

**Example**

```python
df.info()
```

---

## merge()

Joins two DataFrames.

**Syntax**

```python
pd.merge(df1, df2, on="column")
```

**Example**

```python
merged_df = pd.merge(customers, orders, on="CustomerID")
```

---

## print DataFrame

Displays the DataFrame.

**Syntax**

```python
print(df)

df
```

**Example**

```python
print(df)

df
```

---

## replace()

Replaces values.

**Syntax**

```python
df["column"].replace(old_value, new_value)
```

**Example**

```python
df["Status"].replace("Pending", "Complete", inplace=True)
```

---

## tail()

Displays the last rows.

**Syntax**

```python
df.tail(n)
```

**Example**

```python
df.tail(5)
```

---

# NumPy

## Importing NumPy

Imports the NumPy library.

**Syntax**

```python
import numpy as np
```

**Example**

```python
import numpy as np
```

---

## np.array()

Creates NumPy arrays.

**Syntax**

```python
np.array([values])

np.array([[row1], [row2]])
```

**Example**

```python
arr1 = np.array([1, 2, 3])

arr2 = np.array([[1, 2], [3, 4]])
```

---

## NumPy Array Attributes & Operations

Common numerical operations.

**Syntax**

```python
np.mean(array)

np.sum(array)

np.min(array)

np.max(array)

np.dot(array1, array2)
```

**Example**

```python
np.mean(arr)

np.sum(arr)

np.min(arr)

np.max(arr)

np.dot(arr1, arr2)
```