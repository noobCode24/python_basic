# File: function_methods.py
# Thao tác với hàm trong Python

# 1. Hàm cơ bản
def add(a, b):
    return a + b
print("1. Hàm cơ bản:", add(2, 3))  # Gọi hàm và trả về 5

# 2. Tham số mặc định
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"
print("2. Tham số mặc định:", greet("Alice"))  # Hello, Alice!
print("   Với tham số:", greet("Bob", "Hi"))  # Hi, Bob!

# 3. Tham số không xác định (*args)
def sum_all(*args):
    return sum(args)  # args là tuple chứa các tham số
print("3. *args:", sum_all(1, 2, 3, 4))  # 10

# 4. Tham số từ khóa không xác định (**kwargs)
def print_info(**kwargs):
    for key, value in kwargs.items():  # kwargs là dict chứa cặp key-value
        print(f"{key}: {value}")
print("4. **kwargs:")
print_info(name="Alice", age=25)  # name: Alice, age: 25

# 5. Lambda (hàm ẩn danh)
square = lambda x: x**2
print("5. Lambda:", square(4))  # 16

# 6. Hàm lồng nhau (nested function)
def outer(x):
    def inner(y):
        return x + y
    return inner
add_five = outer(5)
print("6. Nested function:", add_five(3))  # 8

# 7. Truyền hàm làm tham số
def apply(func, x):
    return func(x)
print("7. Truyền hàm:", apply(lambda x: x * 2, 5))  # 10

# Lưu ý
print("\nLưu ý: Hàm giúp tái sử dụng code và tổ chức logic rõ ràng.")