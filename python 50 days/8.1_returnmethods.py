
# Python Function Types – Based on Parameters and Return Values

# 1. Function WITH parameters and WITH return value
# --------------------------------------------------
def add(a, b):
    return a + b

# Example:
print(add(5, 3))  # Output: 8


# 2. Function WITH parameters and WITHOUT return value
# -----------------------------------------------------
def greet(name):
    print(f"Hello, {name}!")

# Example:
greet("Alice")  # Output: Hello, Alice!


# 3. Function WITHOUT parameters and WITH return value
# -----------------------------------------------------
def get_pi():
    return 3.14159

# Example:
print(get_pi())  # Output: 3.14159


# 4. Function WITHOUT parameters and WITHOUT return value
# --------------------------------------------------------
def say_hello():
    print("Hello!")

# Example:
say_hello()  # Output: Hello!
