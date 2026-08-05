---

# Cheat Sheet

## Import Libraries

```python
import requests
import pandas as pd
from bs4 import BeautifulSoup
```

---

## GET Request

Retrieve data from an API.

```python
response = requests.get(url)
```

Example

```python
response = requests.get("https://api.example.com/data")
```

---

## POST Request

Send data to the server.

```python
response = requests.post(url, data=data)
```

Example

```python
payload = {"name": "Guru"}

response = requests.post(
    "https://api.example.com/submit",
    data=payload
)
```

---

## PUT Request

Update existing data.

```python
response = requests.put(url, data=data)
```

Example

```python
response = requests.put(
    "https://api.example.com/update",
    data={"id":1}
)
```

---

## DELETE Request

Delete a resource.

```python
response = requests.delete(url)
```

Example

```python
response = requests.delete(
    "https://api.example.com/delete"
)
```

---

## Query Parameters

```python
params = {
    "page":1,
    "per_page":10
}

response = requests.get(url, params=params)
```

---

## Custom Headers

```python
headers = {
    "Authorization":"Bearer TOKEN"
}

response = requests.get(
    url,
    headers=headers
)
```

---

## Response Status Code

```python
response.status_code
```

---

## JSON Response

```python
data = response.json()
```

---

## BeautifulSoup

Create a BeautifulSoup object.

```python
soup = BeautifulSoup(
    html,
    "html.parser"
)
```

---

## Find First Element

```python
element = soup.find(
    "a",
    class_="link"
)
```

---

## Find All Elements

```python
elements = soup.find_all(
    "a"
)
```

---

## CSS Selector

```python
titles = soup.select("h1")
```

---

## Parent Element

```python
parent = element.parent
```

---

## Next Sibling

```python
next_element = element.find_next_sibling()
```

---

## Child Elements

```python
children = element.findChildren()
```

---

## Get Text

```python
text = element.text
```

---

## Get Attribute

```python
href = element["href"]
```

---

## Common HTML Tags

| Tag | Purpose |
|------|----------|
| `<a>` | Hyperlink |
| `<p>` | Paragraph |
| `<h1>`-`<h6>` | Headings |
| `<table>` | Table |
| `<tr>` | Table Row |
| `<td>` | Table Cell |
| `<th>` | Table Header |
| `<img>` | Image |
| `<form>` | Form |
| `<button>` | Button |

---

## Pandas Read HTML Table

```python
tables = pd.read_html(url)

df = tables[0]
```

---

## Read CSV

```python
df = pd.read_csv("data.csv")
```

---

## Read Excel

```python
df = pd.read_excel("data.xlsx")
```

---

## Save CSV

```python
df.to_csv(
    "output.csv",
    index=False
)
```

---

## Time Series

```python
df["date"] = pd.to_datetime(
    df["timestamp"],
    unit="ms"
)
```

---

## DataFrame Methods

```python
df.head()

df.mean()

df.info()

df.describe()

df.tail()
```

---

## HTTP Methods Summary

| Method | Description |
|---------|-------------|
| GET | Retrieve Data |
| POST | Create Data |
| PUT | Update Data |
| DELETE | Delete Data |

---

## HTTP Status Codes

| Code | Meaning |
|------|---------|
| 100 | Informational |
| 200 | Success |
| 201 | Created |
| 400 | Bad Request |
| 401 | Unauthorized |
| 404 | Not Found |
| 500 | Server Error |
