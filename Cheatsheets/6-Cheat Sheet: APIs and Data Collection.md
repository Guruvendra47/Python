# Cheat Sheet: APIs and Data Collection

---

## Import Libraries

Import the required libraries for API requests and web scraping.

**Syntax**

```python
import requests
from bs4 import BeautifulSoup
```

**Example**

```python
import requests
from bs4 import BeautifulSoup
```

---

## requests.get()

Send a GET request to retrieve data from an API or website.

**Syntax**

```python
response = requests.get(url)

response = requests.get(url, params=params)

response = requests.get(url, headers=headers)
```

**Example**

```python
response = requests.get("https://api.example.com/data")
```

---

## requests.post()

Send data to a server.

**Syntax**

```python
response = requests.post(url, data=data)
```

**Example**

```python
payload = {"name": "John"}

response = requests.post(
    "https://api.example.com/submit",
    data=payload
)
```

---

## requests.put()

Update an existing resource.

**Syntax**

```python
response = requests.put(url, data=data)
```

**Example**

```python
payload = {"name": "John"}

response = requests.put(
    "https://api.example.com/update",
    data=payload
)
```

---

## requests.delete()

Delete a resource.

**Syntax**

```python
response = requests.delete(url)
```

**Example**

```python
response = requests.delete(
    "https://api.example.com/delete"
)
```

---

## Headers

Send custom HTTP headers.

**Syntax**

```python
headers = {
    "HeaderName": "Value"
}

requests.get(url, headers=headers)
```

**Example**

```python
headers = {
    "Authorization": "Bearer YOUR_TOKEN"
}

response = requests.get(
    "https://api.example.com/data",
    headers=headers
)
```

---

## Query Parameters

Send parameters in the URL.

**Syntax**

```python
params = {
    "key": "value"
}

requests.get(url, params=params)
```

**Example**

```python
params = {
    "page": 1,
    "per_page": 10
}

response = requests.get(
    "https://api.example.com/data",
    params=params
)
```

---

## response.status_code

Returns the HTTP status code.

**Syntax**

```python
response.status_code
```

**Example**

```python
response = requests.get("https://api.example.com/data")

print(response.status_code)
```

---

## response.json()

Converts JSON response into a Python dictionary or list.

**Syntax**

```python
response.json()
```

**Example**

```python
response = requests.get(
    "https://api.example.com/data"
)

data = response.json()
```

---

## BeautifulSoup()

Parses HTML into a BeautifulSoup object.

**Syntax**

```python
soup = BeautifulSoup(html, "html.parser")
```

**Example**

```python
html = response.text

soup = BeautifulSoup(html, "html.parser")
```

---

## soup.find()

Returns the first matching HTML element.

**Syntax**

```python
soup.find(tag)

soup.find(tag, attrs={})
```

**Example**

```python
title = soup.find("h1")

link = soup.find(
    "a",
    {"class": "link"}
)
```

---

## soup.find_all()

Returns all matching HTML elements.

**Syntax**

```python
soup.find_all(tag)

soup.find_all(tag, attrs={})
```

**Example**

```python
links = soup.find_all("a")

rows = soup.find_all("tr")
```

---

## findChildren()

Returns all child elements.

**Syntax**

```python
element.findChildren()
```

**Example**

```python
children = parent_div.findChildren()
```

---

## find_next_sibling()

Returns the next sibling element.

**Syntax**

```python
element.find_next_sibling()
```

**Example**

```python
next_item = current_element.find_next_sibling()
```

---

## parent

Returns the parent element.

**Syntax**

```python
element.parent
```

**Example**

```python
parent = paragraph.parent
```

---

## Accessing Element Attributes

Returns the value of an HTML attribute.

**Syntax**

```python
element["attribute"]
```

**Example**

```python
href = link["href"]

src = image["src"]
```

---

## element.text

Returns the text inside an HTML element.

**Syntax**

```python
element.text
```

**Example**

```python
title = title_element.text
```

---

## soup.select()

Selects elements using CSS selectors.

**Syntax**

```python
soup.select(selector)
```

**Example**

```python
titles = soup.select("h1")

links = soup.select("a.link")
```

---

## HTML Tags Used with find() and find_all()

Common HTML tags used during web scraping.

**Syntax**

```python
soup.find("tag")

soup.find_all("tag")
```

**Examples**

```python
soup.find("a")       # Anchor

soup.find("p")       # Paragraph

soup.find("h1")      # Heading

soup.find("table")   # Table

soup.find_all("tr")  # Table Rows

soup.find_all("td")  # Table Cells

soup.find_all("th")  # Table Headers

soup.find("img")     # Images

soup.find("form")    # Forms

soup.find("button")  # Buttons
```

---

## Common HTTP Status Codes

| Code | Meaning |
|------:|---------|
| 200 | OK |
| 201 | Created |
| 400 | Bad Request |
| 401 | Unauthorized |
| 403 | Forbidden |
| 404 | Not Found |
| 500 | Internal Server Error |

---

## Common HTTP Methods

| Method | Purpose |
|---------|---------|
| GET | Retrieve data |
| POST | Create new data |
| PUT | Update existing data |
| DELETE | Delete data |

---

## Common Response Attributes

```python
response.status_code

response.headers

response.text

response.json()

response.url
```

---

## URL Structure

```
https://api.example.com/users?id=10
│
├── Scheme      → https
├── Base URL    → api.example.com
├── Route       → /users
└── Query       → ?id=10
```

---

## Typical API Workflow

```python
import requests

url = "https://api.example.com/users"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(data)
```