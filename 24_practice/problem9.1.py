# Combine a decorator with *args and **kwargs support so it can wrap any function regardless of its parameters

from functools import wraps

def universal_decorator(func):
    @wraps(func)  # preserves function name and docstring
    def wrapper(*args, **kwargs):
        print(f"calling function: {func.__name__}")
        print(f"Arguments: args={args}, kwargs={kwargs}")

        result = func(*args, **kwargs)  # call original function
        print(f"Result: {result}")
        return result
    return wrapper


# Example usage
@universal_decorator
def add(a, b):
    return a + b

@universal_decorator
def greet(name, msg="Hello"):
    return f"{msg}, {name}!"

print(add(3, 5))
print(greet("Rosan"))
print(greet("Rosan", msg="Good Morning"))