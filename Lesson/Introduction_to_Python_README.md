# Introduction to Python — Data-Driven Foundations

A practical, beginner-friendly guide to Python for data careers. This project converts your presentation into an actionable GitHub-ready repository with clear explanations, runnable examples, and a mini project to showcase skills.

---

## Table of Contents
- [Why Learn Python?](#why-learn-python)
- [Installing Python](#installing-python)
- [Python in the Real World](#python-in-the-real-world)
- [Python vs Other Data Tools](#python-vs-other-data-tools)
- [Core Features for Data Work](#core-features-for-data-work)
- [Basic Python Syntax](#basic-python-syntax)
- [Working with Data in Python](#working-with-data-in-python)
- [Python’s Role in Data Engineering](#pythons-role-in-data-engineering)
- [Python in a Data Workflow](#python-in-a-data-workflow)
- [Best Practices for Writing Python Code](#best-practices-for-writing-python-code)
- [Quick Start Project Example](#quick-start-project-example)
- [Project Structure](#project-structure)
- [Attribution](#attribution)

---

## Why Learn Python?

Python is widely used across industries for data analysis, engineering, automation, and machine learning. It’s beginner-friendly and supported by a large ecosystem of libraries that speed up development.

**Benefits**
- Readable syntax and fast prototyping.
- Extensive libraries for data work: `pandas`, `numpy`, `matplotlib`, `scikit-learn`.
- Strong community and learning resources.

---

## Installing Python

1. Download from the official site: https://www.python.org/downloads/  
2. Install for your OS (Windows / macOS / Linux). On Windows, check **Add Python to PATH** during setup.  
3. Verify installation:

```bash
python --version
pip --version
```

### Recommended tools
- VS Code or PyCharm (IDE)
- Jupyter Notebook / JupyterLab for interactive data work
- Google Colab for quick cloud-based notebooks

---

## Python in the Real World

Python powers many production systems and data workflows:

- **Data Analysis:** used to build analytics and recommendation systems.
- **Data Engineering:** ETL pipelines, transformations, and data orchestration.
- **Automation:** scripts for reports, monitoring, and repetitive tasks.

---

## Python vs Other Data Tools

| Use case | Python | Excel | SQL |
|---|---:|:---:|:---:|
| Large datasets | ✅ | ❌ | ✅ |
| Automation & scripting | ✅ | ⚠️ | ❌ |
| Data manipulation | ✅ (`pandas`) | ✅ (manual) | ⚠️ (querying) |
| Integration with ML/Cloud | ✅ | ❌ | ✅ |

**Summary:** Python complements SQL and Excel — use SQL for querying databases, Excel for quick ad-hoc analysis, and Python for scalable data manipulation and automation.

---

## Core Features for Data Work

- Built-in data structures: lists, dicts, tuples, sets.
- Libraries: `pandas`, `numpy`, `matplotlib`, `seaborn`.
- Interoperability with databases (SQLAlchemy), big data tools (Spark), and cloud (AWS/GCP).

```python
# simple example with list comprehension
numbers = [1, 2, 3, 4]
squares = [n**2 for n in numbers]
print(squares)
```

---

## Basic Python Syntax

```python
# variables and types
name = "Alex"
age = 28
height = 1.75
is_active = True

# functions
def greet(user):
    return f"Hello, {user}!"

print(greet(name))
```

---

## Working with Data in Python

### Pandas (DataFrames)
```python
import pandas as pd

data = {'name': ['A','B','C'], 'score': [90, 85, 88]}
df = pd.DataFrame(data)
print(df.head())
```

### NumPy
```python
import numpy as np
arr = np.array([1,2,3,4])
print(np.mean(arr))
```

### Matplotlib
```python
import matplotlib.pyplot as plt
df.plot(kind='bar', x='name', y='score', title='Scores')
plt.show()
```

---

## Python’s Role in Data Engineering

Python is commonly used to:
- Extract data from APIs and databases.
- Clean and transform data for analytics.
- Load processed datasets into databases or data lakes.
- Schedule and automate workflows (Airflow, cron).

Example ETL snippet:
```python
import pandas as pd

df = pd.read_csv('raw_sales.csv')
df['total'] = df['price'] * df['quantity']
df.to_parquet('clean_sales.parquet')
```

---

## Python in a Data Workflow

Typical stages:
1. Data collection (APIs, databases, files)  
2. Data cleaning (missing values, types)  
3. Data transformation (joins, aggregations)  
4. Data storage (databases, cloud)  
5. Data analysis and visualization

---

## Best Practices for Writing Python Code

- Follow PEP8 for style.
- Write clear functions and docstrings.
- Test small units (unit tests).
- Use Git for version control and branches for features.
- Document with README and inline comments.

---

## Quick Start Project Example

**Goal:** Analyze a small sales dataset and visualize top products.

```python
# quick_start.py
import pandas as pd
import matplotlib.pyplot as plt

sales = pd.read_csv('data/sales_data.csv')
sales = sales.dropna(subset=['Product', 'Revenue'])
top = sales.groupby('Product')['Revenue'].sum().nlargest(5)

top.plot(kind='bar', title='Top 5 Products by Revenue')
plt.tight_layout()
plt.savefig('outputs/top_products.png')
```

Add `data/sales_data.csv` with columns: `Product,Revenue,Date,Quantity`.

---

## Project Structure

```
introduction-to-python/
├── data/                # sample CSVs used in examples
├── notebooks/           # Jupyter notebooks for exploration
├── scripts/             # runnable python scripts (quick_start.py)
├── outputs/             # generated charts and results
├── README.md            # this file
└── requirements.txt     # pip install -r requirements.txt
```

Example `requirements.txt`
```
pandas
numpy
matplotlib
jupyter
```

---

## Attribution

This README was written freshly from your slides and rephrased to be original, practical, and ready for a GitHub repository. Use it as `README.md` in a new repo named `introduction-to-python`.

---

### Next steps
If you want, I can:
- Create the full folder structure and example files (`scripts/quick_start.py`, `data/sample_sales.csv`, `requirements.txt`) and package them as a ZIP for download.
- Or directly push these files to a GitHub repo if you provide repository access/token.

