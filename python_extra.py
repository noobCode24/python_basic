# File: python_extra.py
# Một số tính năng nâng cao của Python

# 1. Generator
def gen_squares(n):
    for i in range(n):
        yield i**2
print("1. Generator:", list(gen_squares(3)))  # [0, 1, 4]

# 2. Decorator
def log(func):
    def wrapper(*args):
        print(f"Calling {func.__name__}")
        return func(*args)
    return wrapper

@log
def add(a, b):
    return a + b
print("2. Decorator:", add(2, 3))  # Calling add, 5

# 3. Collections - Counter
from collections import Counter
print("3. Counter:", Counter([1, 1, 2, 3]))  # Counter({1: 2, 2: 1, 3: 1})

# 4. Threading
import threading
def print_numbers():
    for i in range(3):
        print(i, end=" ")
t = threading.Thread(target=print_numbers)
t.start()
t.join()  # Chờ thread hoàn thành
print("\n4. Threading done")

# 5. Regular Expression
import re
print("5. Regex:", re.sub(r"\d+", "X", "abc123xyz"))  # abcXxyz