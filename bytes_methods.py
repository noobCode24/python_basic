# File: bytes_methods.py
# Thao tác với kiểu dữ liệu bytes và bytearray trong Python

b = b"hello"
print("1. decode():", b.decode())        # Chuyển bytes thành chuỗi: "hello"
print("2. hex():", b.hex())              # Chuyển thành chuỗi hexa: "68656c6c6f"

ba = bytearray(b)
print("3. append():", ba.append(33) or ba)  # Thêm byte 33 (!) vào bytearray: bytearray(b"hello!")
print("4. pop():", ba.pop() or ba)       # Xóa và trả về byte cuối: 33, ba = bytearray(b"hello")