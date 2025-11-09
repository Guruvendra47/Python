# Python Fundamentals — Assignment 1
**Repository / File:** `Python_Fundamentals_Assignment_1.md`  
**Contents:** Detailed, GitHub-ready answers and runnable code for each question. Format: **Question → Explanation → Answer/Code → Sample Output**.

---

## Table of Contents
- [Q1 — Basic: Variable Assignment](#q1---basic-variable-assignment)
- [Q2 — Data Types Identification (Short answers)](#q2---data-types-identification-short-answers)
- [Q3 — Keywords Check](#q3---keywords-check)
- [Q4 — Literals Classification](#q4---literals-classification)
- [Q5 — Type Casting Basics](#q5---type-casting-basics)
- [Q6 — Mixed Types Arithmetic](#q6---mixed-types-arithmetic)
- [Q7 — Temperature Converter](#q7---temperature-converter)
- [Q8 — Variables & Mutability](#q8---variables--mutability)
- [Q9 — Input Validation (type casting + condition)](#q9---input-validation-type-casting--condition)
- [Q10 — Keywords & Identifiers](#q10---keywords--identifiers)
- [Q11 — Advanced: Expression Parser](#q11---advanced-expression-parser)

---

## Q1 — Basic: Variable Assignment

**Question.** Assign values to variables (`age`, `name`, `is_student`, `gpa`, `courses`) and print their types using `type()`.

**Explanation.** Python variables are dynamically typed. Use `type()` to inspect the runtime type. Good practice: choose realistic example values.

**Answer / Code:**
```python
# q1_variables.py
age = 21                  # integer
name = "Aisha Khan"       # string
is_student = True         # boolean
gpa = 3.75                # float
courses = ["CS101", "MA101", "ENG201"]  # list of strings

print("age:", age, "type:", type(age))
print("name:", name, "type:", type(name))
print("is_student:", is_student, "type:", type(is_student))
print("gpa:", gpa, "type:", type(gpa))
print("courses:", courses, "type:", type(courses))
```

**Sample Output:**
```
age: 21 type: <class 'int'>
name: Aisha Khan type: <class 'str'>
is_student: True type: <class 'bool'>
gpa: 3.75 type: <class 'float'>
courses: ['CS101', 'MA101', 'ENG201'] type: <class 'list'>
```

---

## Q2 — Data Types Identification (Short answers)

**Question.** For each Python literal, state its data type: `100`, `3.14`, `'c'`, `'Hello'`, `True`, `None`, `(1,2,3)`, `{'a':1}`.

**Explanation.** Identify built-in literal types: integers, floats, strings, booleans, NoneType, tuples, dictionaries.

**Answer (mapping):**
- `100` → `int`
- `3.14` → `float`
- `'c'` → `str` (single-character string)
- `'Hello'` → `str`
- `True` → `bool`
- `None` → `NoneType`
- `(1,2,3)` → `tuple`
- `{'a':1}` → `dict`

**Short code to verify:**
```python
literals = [100, 3.14, 'c', 'Hello', True, None, (1,2,3), {'a':1}]
for x in literals:
    print(x, "->", type(x))
```

**Sample Output:**
```
100 -> <class 'int'>
3.14 -> <class 'float'>
c -> <class 'str'>
Hello -> <class 'str'>
True -> <class 'bool'>
None -> <class 'NoneType'>
(1, 2, 3) -> <class 'tuple'>
{'a': 1} -> <class 'dict'>
```

---

## Q3 — Keywords Check

**Question.** Import the `keyword` module and write a program that checks if a word is a Python keyword.

**Explanation.** Python `keyword` module exposes a list and a helper `iskeyword()` to test a string. Useful for validating identifiers.

**Answer / Code:**
```python
# q3_keywords_check.py
import keyword

def check_keyword(word: str) -> bool:
    return keyword.iskeyword(word)

# Example usage
words = ["for", "lambda", "myvar", "class", "async", "await", "True"]
for w in words:
    print(w, "is keyword?" , check_keyword(w))
```

**Sample Output:**
```
for is keyword? True
lambda is keyword? True
myvar is keyword? False
class is keyword? True
async is keyword? True
await is keyword? True
True is keyword? False
```

> Note: `True` is a constant, not classified as a keyword by `keyword.iskeyword()` in some Python versions; it's recommended to avoid using it as an identifier regardless.

---

## Q4 — Literals Classification

**Question.** Given a literal as string input, classify it as Integer, Float, String, Boolean, None, or Other.

**Explanation.** The input is a string; we must attempt to parse it. Use a sequence of checks: `None`, boolean literals, integer parse, float parse, else treat as string/other. Always handle exceptions.

**Answer / Code:**
```python
# q4_literal_classify.py
def classify_literal(s: str) -> str:
    s_strip = s.strip()
    # None literal
    if s_strip == "None":
        return "NoneType"
    # Boolean literals
    if s_strip == "True" or s_strip == "False":
        return "bool"
    # Integer
    try:
        int(s_strip)
        return "int"
    except ValueError:
        pass
    # Float
    try:
        float(s_strip)
        return "float"
    except ValueError:
        pass
    # Strings that are quoted: '...' or "..."
    if (s_strip.startswith("'") and s_strip.endswith("'")) or (s_strip.startswith('"') and s_strip.endswith('"')):
        return "str (quoted)"
    # Default: treat as string / other
    return "str/other"

# Examples
examples = ["100", "3.14", "'hello'", '"world"', "True", "None", "abc123"]
for ex in examples:
    print(f"{ex} -> {classify_literal(ex)}")
```

**Sample Output:**
```
100 -> int
3.14 -> float
'hello' -> str (quoted)
"world" -> str (quoted)
True -> bool
None -> NoneType
abc123 -> str/other
```

---

## Q5 — Type Casting Basics

**Question.** Demonstrate explicit casting between `int`, `float`, `str`, and `bool` with valid and invalid cases.

**Explanation.** Casting (conversion) functions: `int()`, `float()`, `str()`, `bool()`. Some conversions raise `ValueError` (e.g., `int("3.14")`), others succeed (e.g., `int(3.0)` → `3`). `bool()` follows truthiness rules.

**Answer / Code:**
```python
# q5_type_casting.py
cases = [
    ("int from float", lambda: int(3.7)),
    ("int from string int", lambda: int("42")),
    ("int from string float (invalid)", lambda: int("3.14")),
    ("float from int", lambda: float(5)),
    ("float from string", lambda: float("2.718")),
    ("str from int", lambda: str(100)),
    ("bool from 0", lambda: bool(0)),
    ("bool from ''", lambda: bool("")),
    ("bool from 'False' (non-empty string)", lambda: bool("False")),
]

for desc, fn in cases:
    try:
        print(f"{desc}: {fn()}")
    except Exception as e:
        print(f"{desc}: Error ->", repr(e))
```

**Sample Output:**
```
int from float: 3
int from string int: 42
int from string float (invalid): Error -> ValueError("invalid literal for int() with base 10: '3.14'")
float from int: 5.0
float from string: 2.718
str from int: 100
bool from 0: False
bool from '': False
bool from 'False' (non-empty string): True
```

**Key takeaways:**
- `int("3.14")` fails because the string is not an integer literal. Use `float()` first then `int()` if appropriate.
- `bool()` converts values by truthiness: empty containers, `0`, `0.0`, `None` → `False`; everything else → `True`.

---

## Q6 — Mixed Types Arithmetic

**Question.** Perform addition based on input type: numeric addition or string concatenation.

**Explanation.** If both operands are numeric (int/float), perform numeric addition. If either is a pure string that cannot be parsed to number, perform concatenation. Avoid implicit errors by explicit checks and exception handling.

**Answer / Code:**
```python
# q6_mixed_add.py
def add_mixed(a: str, b: str):
    # try numeric interpretation
    try:
        if '.' in a or 'e' in a.lower():
            aval = float(a)
        else:
            aval = int(a)
        if '.' in b or 'e' in b.lower():
            bval = float(b)
        else:
            bval = int(b)
        return aval + bval
    except Exception:
        # fallback: string concatenation
        return a + b

examples = [("2", "3"), ("2.5", "1.5"), ("hello", " world"), ("2", "three"), ("100", "0.5")]
for a,b in examples:
    print(f"{a} + {b} -> {add_mixed(a,b)}")
```

**Sample Output:**
```
2 + 3 -> 5
2.5 + 1.5 -> 4.0
hello +  world -> hello world
2 + three -> 2three
100 + 0.5 -> 100.5
```

---

## Q7 — Temperature Converter

**Question.** Convert between Celsius and Fahrenheit using user input and type conversion.

**Explanation.** Use standard formulas: `C = (F - 32) * 5/9`, `F = C * 9/5 + 32`. Validate numeric input and allow user to select direction.

**Answer / Code:**
```python
# q7_temp_converter.py
def c_to_f(c):
    return c * 9/5 + 32

def f_to_c(f):
    return (f - 32) * 5/9

# Sample usage (replace input() with constants in unit tests)
print("0°C ->", c_to_f(0), "°F")
print("32°F ->", f_to_c(32), "°C")
print("100°C ->", c_to_f(100), "°F")
```

**Sample Output:**
```
0°C -> 32.0 °F
32°F -> 0.0 °C
100°C -> 212.0 °F
```

---

## Q8 — Variables & Mutability

**Question.** Explain mutable vs immutable with code showing list (mutable) and tuple (immutable) behavior.

**Explanation.** Mutable objects can be changed in place (lists, dicts, sets). Immutable objects cannot be altered once created (ints, floats, strings, tuples). Understanding this affects function design and side-effects.

**Answer / Code:**
```python
# q8_mutability.py
# List is mutable
lst = [1, 2, 3]
print("Before:", lst, "id:", id(lst))
lst.append(4)  # modifies in place
print("After:", lst, "id:", id(lst))

# Tuple is immutable
tup = (1, 2, 3)
print("Tuple before:", tup, "id:", id(tup))
try:
    tup[0] = 10  # raises TypeError
except TypeError as e:
    print("Trying to modify tuple resulted in:", repr(e))
```

**Sample Output:**
```
Before: [1, 2, 3] id: 140421234567456
After: [1, 2, 3, 4] id: 140421234567456
Tuple before: (1, 2, 3) id: 140421234567000
Trying to modify tuple resulted in: TypeError('...')
```

> Note: `id()` values vary per run; list `id` remains the same before/after append showing in-place mutation.

---

## Q9 — Input Validation (type casting + condition)

**Question.** Take age as input, validate numeric, and classify into Child, Teenager, Adult, or Senior.

**Explanation.** Validate using `int()` with exception handling. Accept only reasonable range (0–120). Use conditionals for classification.

**Answer / Code:**
```python
# q9_age_classify.py
def classify_age(age_input: str) -> str:
    try:
        age = int(age_input)
    except ValueError:
        return "Invalid input: not an integer"
    if age < 0 or age > 120:
        return "Invalid age range"
    if age <= 12:
        return "Child"
    elif age <= 17:
        return "Teenager"
    elif age <= 64:
        return "Adult"
    else:
        return "Senior"

# Examples
for v in ["10", "15", "30", "80", "-1", "abc"]:
    print(v, "->", classify_age(v))
```

**Sample Output:**
```
10 -> Child
15 -> Teenager
30 -> Adult
80 -> Senior
-1 -> Invalid age range
abc -> Invalid input: not an integer
```

---

## Q10 — Keywords & Identifiers

**Question.** Explain valid Python identifiers and write code to check invalid ones or keywords.

**Explanation.** Identifiers must start with a letter (A–Z, a–z) or underscore `_`, followed by letters, digits, or underscores. They cannot be a Python keyword or contain spaces or special characters.

**Answer / Code:**
```python
# q10_identifiers.py
import keyword
import re

identifier_re = re.compile(r'^[A-Za-z_][A-Za-z0-9_]*$')

def is_valid_identifier(name: str) -> (bool, str):
    if keyword.iskeyword(name):
        return False, "is a Python keyword"
    if not identifier_re.match(name):
        return False, "does not match identifier pattern"
    return True, "valid identifier"

tests = ["_var", "2cool", "class", "my var", "valid_name2", "def"]
for t in tests:
    ok, reason = is_valid_identifier(t)
    print(t, "->", ok, reason)
```

**Sample Output:**
```
_var -> True valid identifier
2cool -> False does not match identifier pattern
class -> False is a Python keyword
my var -> False does not match identifier pattern
valid_name2 -> True valid identifier
def -> False is a Python keyword
```

---

## Q11 — Advanced: Expression Parser

**Question.** Accept simple expressions like `'12 * 3.5'` and evaluate using type casting and exception handling.

**Explanation.** Using `eval()` is dangerous if input is untrusted. We'll implement a safe parser that supports two operands and one operator from the allowed set `+ - * /`. This handles numeric literals (int/float) and avoids arbitrary code execution.

**Answer / Code:**
```python
# q11_expression_parser.py
import operator

ops = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
}

def parse_and_eval(expr: str):
    # simple split: find operator position (space-separated or not)
    for sym in ops:
        if sym in expr:
            parts = expr.split(sym)
            if len(parts) != 2:
                raise ValueError("Expression must be two operands and one operator")
            left, right = parts[0].strip(), parts[1].strip()
            # attempt numeric conversion (int then float)
            def to_number(s):
                try:
                    return int(s)
                except ValueError:
                    return float(s)
            try:
                lnum = to_number(left)
                rnum = to_number(right)
            except ValueError:
                raise ValueError("Operands must be numeric")
            # division by zero check
            if sym == '/' and rnum == 0:
                raise ZeroDivisionError("division by zero")
            return ops[sym](lnum, rnum)
    raise ValueError("No supported operator found. Supported: + - * /")

# Examples
examples = ["12 * 3.5", "10 + 5", "7/0", "3.14-1.14", "bad + 3"]
for e in examples:
    try:
        print(e, "->", parse_and_eval(e))
    except Exception as exc:
        print(e, "-> Error:", exc)
```

**Sample Output:**
```
12 * 3.5 -> 42.0
10 + 5 -> 15
7/0 -> Error: division by zero
3.14-1.14 -> 2.0
bad + 3 -> Error: Operands must be numeric
```

---

## How to use these files on GitHub
1. Create a repository called `Python_Fundamentals_Assignment_1` (or upload this single Markdown file as `README.md`).  
2. If you prefer separate `.py` files, copy each code block into its own file (filenames suggested in the headers).  
3. Add `requirements.txt` if you add external test frameworks (not required here).

---

## Notes & Best Practices (mini-tutorial recap)
- Prefer explicit conversions and handle exceptions when parsing user input.  
- Avoid `eval()` on untrusted inputs — implement safe parsers or use `ast` for structured parsing.  
- Use `keyword.iskeyword()` to protect identifier names.  
- Keep functions small and testable; write unit tests for validators and parsers.  

---
