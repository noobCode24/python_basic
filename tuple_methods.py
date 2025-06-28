# File: tuple_methods.py
# Thao tác với kiểu dữ liệu tuple trong Python

tup = (1, 2, 2, 3)
print("1. count():", tup.count(2))       # Đếm số lần xuất hiện của 2: 2
print("2. index():", tup.index(3))       # Tìm chỉ số đầu tiên của 3: 3

# Lưu ý: Tuple là immutable, không có phương thức thay đổi nội dung
print("\nLưu ý: Tuple không thể thay đổi sau khi tạo.")