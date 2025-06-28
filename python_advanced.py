# File: python_advanced.py
# Kỹ năng lập trình Python nâng cao

# 1. Hàm với tham số mặc định
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"
print("1. Function:", greet("Alice"))  # Hello, Alice!

# 2. Xử lý lỗi
try:
    result = 10 / 0
except ZeroDivisionError:
    print("2. Try-Except:", "Cannot divide by zero")  # Cannot divide by zero

# 3. Collections - Counter
from collections import Counter
print("3. Counter:", Counter("hello"))  # Counter({'l': 2, 'h': 1, 'e': 1, 'o': 1})

# 4. Collections - defaultdict
from collections import defaultdict
d = defaultdict(int)
d["a"] += 1
print("4. defaultdict:", dict(d))  # {'a': 1}

# 5. Itertools - permutations
from itertools import permutations
print("5. Permutations:", list(permutations([1, 2], 2)))  # [(1, 2), (2, 1)]