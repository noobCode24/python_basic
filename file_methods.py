# File: file_methods.py
# Thao tác với file trong Python

# Ghi file
with open("test.txt", "w") as f:
    print("1. write():", f.write("Hello") or "Đã ghi 'Hello' vào test.txt")  # Ghi chuỗi "Hello": 5 (số byte)

# Đọc file
with open("test.txt", "r") as f:
    print("2. read():", f.read())        # Đọc toàn bộ nội dung: "Hello"
with open("test.txt", "w") as f:
    f.write("Line1\nLine2")
with open("test.txt", "r") as f:
    print("3. readline():", f.readline())  # Đọc dòng đầu tiên: "Line1\n"
    print("4. readlines():", f.readlines())  # Đọc tất cả dòng thành list: ["Line2"]