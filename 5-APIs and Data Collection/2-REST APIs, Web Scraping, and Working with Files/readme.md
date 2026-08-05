# Python APIs, Web Scraping & Data Collection

## Overview

This repository covers **APIs**, **HTTP Protocol**, **Requests Library**, **Web Scraping**, **Beautiful Soup**, and **Working with Different File Formats** in Python. It explains how applications communicate over the internet, retrieve data from APIs, scrape websites, and read data from various file formats for data analysis.

These concepts are essential for **Data Engineering, Data Science, ETL, Automation, and Web Development**.

---

# Topics Covered

## 1. Introduction to APIs

Application Programming Interfaces (APIs) allow different software applications to communicate and exchange data.

### Covered Concepts

- What is an API
- Simple APIs
- API Libraries
- Pandas API
- API Instances
- Request and Response
- REST APIs

---

## 2. Why APIs Matter

APIs help developers:

- Reuse existing services
- Access real-time data
- Integrate different applications
- Connect cloud services
- Reduce development time
- Build scalable applications

---

## 3. Applications of APIs

APIs are used in:

- Social Media
- E-commerce
- Weather Applications
- Payment Gateways
- Maps & Navigation
- AI Applications
- Cryptocurrency Platforms
- Banking Systems
- Messaging Applications

---

## 4. Pandas API

Pandas communicates with internal software components through its API.

Topics include:

- Creating DataFrames
- API Instances
- `head()`
- `mean()`

---

## 5. REST APIs

REST APIs allow applications to communicate over the internet.

Topics include:

- Client
- Server
- Resource
- Endpoint
- Request
- Response
- JSON communication

---

# HTTP Protocol

The HyperText Transfer Protocol (HTTP) transfers data between clients and web servers.

Topics include:

- HTTP Protocol
- HTTP Request
- HTTP Response
- Request Header
- Response Header
- Response Body
- Status Codes

Common Status Codes

| Code | Meaning |
|------|---------|
| 100 | Informational |
| 200 | Success |
| 401 | Unauthorized |
| 404 | Not Found |
| 500 | Server Error |
| 501 | Not Implemented |

---

# URL Structure

A URL contains three parts:

- Scheme (`http://` or `https://`)
- Base URL
- Route (Endpoint)

Example

```
https://www.ibm.com/images/logo.png
```

- Scheme → https
- Base URL → www.ibm.com
- Route → /images/logo.png

---

# HTTP Methods

| Method | Purpose |
|---------|----------|
| GET | Retrieve data |
| POST | Send/Create data |
| PUT | Update existing data |
| DELETE | Remove data |

---

# Requests Library

Python's **Requests** library makes working with HTTP easy.

Topics include:

- GET Requests
- POST Requests
- Query Parameters
- Payload
- Request Body
- Response Body
- Response Headers
- Status Codes
- JSON Responses

---

# JSON

JSON is the standard format used by REST APIs for exchanging data.

Topics include:

- JSON Objects
- JSON Responses
- Python Dictionary Conversion

---

# Query Parameters

GET requests can send data using URL parameters.

Example

```
https://example.com/api?name=Guru&id=101
```

Topics include:

- Parameters
- Values
- Query Strings

---

# Time Series Data

Topics include:

- UNIX Timestamp
- `to_datetime()`
- Pandas Time Series
- Daily Market Data
- Candlestick Charts
- Plotly Visualization

---

# Web Scraping

Web scraping automatically extracts information from websites.

Process:

1. Send HTTP Request
2. Retrieve HTML
3. Parse HTML
4. Extract Data
5. Transform Data
6. Store Data
7. Automate Process

Applications include:

- Price Comparison
- Data Collection
- Machine Learning
- Market Research
- News Aggregation
- Social Media Analysis
- Weather Data

---

# HTML Basics

HTML is the structure of every web page.

Topics include:

- HTML Tags
- HTML Elements
- Attributes
- Opening & Closing Tags
- HTML Document Structure

Basic HTML Structure

```
<html>
    <head></head>
    <body></body>
</html>
```

Important Tags

- `<html>`
- `<head>`
- `<body>`
- `<h1> - <h6>`
- `<p>`
- `<a>`
- `<table>`
- `<tr>`
- `<td>`
- `<th>`
- `<img>`
- `<form>`
- `<button>`

---

# HTML Document Tree

Topics include:

- Parent
- Child
- Descendants
- Siblings
- Tree Structure

---

# HTML Tables

HTML tables consist of:

- `<table>`
- `<tr>`
- `<th>`
- `<td>`

Used for displaying structured data.

---

# Beautiful Soup

Beautiful Soup parses HTML and XML documents.

Topics include:

- BeautifulSoup Object
- HTML Parsing
- Tree Navigation
- Tag Objects
- Navigable Strings

Common Methods

- `find()`
- `find_all()`
- `findChildren()`
- `parent`
- `next_sibling`
- `select()`
- `.text`
- Attribute Access

---

# Web Scraping Workflow

```text
Request Web Page
        │
        ▼
Download HTML
        │
        ▼
BeautifulSoup Parser
        │
        ▼
Find HTML Elements
        │
        ▼
Extract Required Data
        │
        ▼
Store Data
```

---

# Pandas HTML Tables

Pandas can directly extract HTML tables.

Method

```python
pd.read_html(URL)
```

Useful for:

- Wikipedia Tables
- Financial Tables
- Statistical Data
- Reports

---

# Working with Different File Formats

Python supports many data formats for analysis.

Supported Formats

- CSV
- JSON
- XML
- XLSX
- TXT

---

# CSV Files

Read CSV

```python
import pandas as pd

df = pd.read_csv("file.csv")
```

Common Operations

- Read CSV
- Assign Headers
- Display DataFrame
- Analyze Data

---

# JSON Files

JSON stores structured data similar to Python dictionaries.

Read JSON

```python
import json

with open("data.json") as file:
    data = json.load(file)
```

---

# XML Files

XML (Extensible Markup Language) stores structured hierarchical data.

Parse XML

```python
import xml.etree.ElementTree as ET

tree = ET.parse("data.xml")
```

Topics include:

- XML Parsing
- Tree Structure
- Extracting Elements
- Creating DataFrames

---

# Data Collection Workflow

```text
API / Website / Files
          │
          ▼
Requests
          │
          ▼
BeautifulSoup / Pandas
          │
          ▼
Extract Data
          │
          ▼
Clean Data
          │
          ▼
DataFrame
          │
          ▼
Analysis
```

---

# Skills Learned

- Understanding APIs
- Working with REST APIs
- HTTP Communication
- Using Requests Library
- GET & POST Requests
- Query Parameters
- Processing JSON
- Working with URLs
- Using Pandas API
- Working with Time Series Data
- Plotting Candlestick Charts
- Web Scraping
- HTML Parsing
- HTML Document Trees
- Beautiful Soup Navigation
- Extracting HTML Tables
- Reading CSV Files
- Reading JSON Files
- Parsing XML Files
- Working with Different File Formats

---

# Technologies Used

- Python 3
- Requests
- Pandas
- Beautiful Soup (bs4)
- Plotly
- JSON
- HTML
- XML
- Jupyter Notebook

---

# Repository Structure

```text
Python-APIs-Web-Scraping-Data-Collection/
│
├── APIs
├── REST APIs
├── HTTP Protocol
├── Requests Library
├── JSON
├── URL & Query Parameters
├── Time Series
├── Web Scraping
├── HTML Basics
├── Beautiful Soup
├── HTML Tables
├── Working with File Formats
├── CSV Files
├── JSON Files
├── XML Files
├── Practice Exercises
└── README.md
```

---

## Author

**Guruvendra Singh**

**Data Engineering | Python | SQL | Snowflake | AWS | ETL**