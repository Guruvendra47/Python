# Basic Python syntax examples

def greet(name: str) -> str:
    return f"Hello, {name}!"

# Variables and types
x = 10            # int
y = 3.14          # float
msg = "Python"    # str
is_ready = True   # bool

# Arithmetic & strings
sum_xy = x + y
msg_caps = msg.upper()

# Lists, tuples, sets, dicts
nums = [1, 2, 3, 4]
coords = (10.0, 20.0)
tags = {"python", "data", "python"}  # set removes duplicates
user = {"id": 1, "name": "Alice", "roles": ["admin", "editor"]}

# Control flow
for n in nums:
    if n % 2 == 0:
        print(f"{n} is even")
    else:
        print(f"{n} is odd")

print(greet("World"))
print("sum_xy:", sum_xy)
print("msg_caps:", msg_caps)
print("tags:", tags)
print("user name:", user["name"])
