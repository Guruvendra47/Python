# Python Pandas

## Overview

This repository introduces **Pandas**, one of the most popular Python libraries for data manipulation and analysis. It covers creating **Series** and **DataFrames**, importing datasets, selecting and filtering data, accessing rows and columns, and saving processed data.

Pandas provides powerful tools for working with structured data and is widely used in data analysis, data engineering, machine learning, and business intelligence.

---

## Topics Covered

### Introduction to Pandas

Pandas is an open-source library for data manipulation and analysis.

Topics include:

- Importing Pandas
- Library aliases
- Structured data processing
- Working with tabular data

Example:

```python
import pandas as pd
```

---

### Loading Data

Pandas supports loading data from multiple file formats.

Topics include:

- CSV files
- Excel files
- Reading datasets

Examples:

```python
df = pd.read_csv("employees.csv")
```

```python
df = pd.read_excel("employees.xlsx")
```

---

### Pandas Series

A Series is a one-dimensional labeled array.

Topics include:

- Creating Series
- Custom indexes
- Accessing values
- Series attributes

Example:

```python
import pandas as pd

numbers = pd.Series([10, 20, 30, 40])
```

---

### Working with Series

Topics include:

- Indexing
- Slicing
- Labels
- Positions

Examples:

```python
numbers[2]

numbers.iloc[1]

numbers[1:4]
```

---

### Series Methods

Common methods include:

- `values`
- `index`
- `shape`
- `size`
- `mean()`
- `sum()`
- `min()`
- `max()`
- `unique()`
- `nunique()`
- `sort_values()`
- `sort_index()`
- `isnull()`
- `notnull()`
- `apply()`

---

### DataFrames

A DataFrame is a two-dimensional table consisting of rows and columns.

Topics include:

- Creating DataFrames
- Reading datasets
- Rows and columns
- Column labels
- Indexes

Example:

```python
data = {
    "Name": ["Alice", "Bob"],
    "Age": [25, 30]
}

df = pd.DataFrame(data)
```

---

### Selecting Columns

Topics include:

- Single column selection
- Multiple column selection
- Creating new DataFrames

Examples:

```python
df["Name"]
```

```python
df[["Name", "Age"]]
```

---

### Accessing Rows

Rows can be accessed using position or labels.

Topics include:

- `iloc[]`
- `loc[]`

Examples:

```python
df.iloc[2]
```

```python
df.loc[1]
```

---

### DataFrame Slicing

Topics include:

- Row slicing
- Column slicing
- Creating filtered DataFrames

Examples:

```python
df[1:3]
```

```python
df.loc[:, "Name":"Age"]
```

---

### Finding Unique Values

The `unique()` method returns distinct values from a column.

Example:

```python
df["Department"].unique()
```

---

### Conditional Filtering

Filter records using comparison operators.

Example:

```python
employees = df[df["Age"] > 25]
```

---

### Saving DataFrames

Processed DataFrames can be saved in different formats.

Example:

```python
df.to_csv("employees.csv", index=False)
```

---

### Common DataFrame Methods

Topics include:

- `head()`
- `tail()`
- `shape`
- `info()`
- `describe()`
- `mean()`
- `sum()`
- `min()`
- `max()`
- `sort_values()`
- `groupby()`
- `fillna()`
- `drop()`
- `rename()`
- `apply()`

---

## Examples Included

- Importing Pandas
- Loading CSV files
- Loading Excel files
- Creating Series
- Creating DataFrames
- Selecting rows and columns
- Using `iloc()` and `loc()`
- DataFrame slicing
- Finding unique values
- Filtering datasets
- Saving DataFrames
- Exploring DataFrame methods

---

## Skills Learned

- Importing and using Pandas
- Creating Series and DataFrames
- Reading CSV and Excel files
- Selecting and filtering data
- Working with rows and columns
- Using DataFrame methods
- Performing data analysis
- Saving processed datasets

---

## Technologies Used

- Python 3
- Pandas
- Jupyter Notebook

---

## Repository Structure

```text
Python-Pandas/
│
├── Pandas Basics
├── Pandas Series
├── DataFrames
├── Data Selection
├── Data Filtering
├── Data Analysis
├── Practice Examples
└── README.md
```

---

## Author

**Guruvendra Singh**

Data Engineering | Python | SQL | Snowflake | AWS