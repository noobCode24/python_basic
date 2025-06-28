# File: string_methods.py
# Tóm tắt và kiểm chứng các phương thức thao tác chuỗi trong Python

# Định dạng chữ
print("1. upper():", "hello".upper())              # Chuyển toàn bộ chuỗi thành chữ in hoa: "HELLO"
print("2. lower():", "HELLO".lower())              # Chuyển toàn bộ chuỗi thành chữ thường: "hello"
print("3. capitalize():", "hello world".capitalize())  # Viết hoa chữ cái đầu tiên của chuỗi: "Hello world"
print("4. title():", "hello world".title())        # Viết hoa chữ cái đầu mỗi từ trong chuỗi: "Hello World"

# Cắt và thay thế
print("5. strip():", "  hello  ".strip())          # Xóa khoảng trắng ở đầu và cuối chuỗi: "hello"
print("6. lstrip():", "  hello".lstrip())          # Xóa khoảng trắng ở đầu chuỗi: "hello"
print("7. rstrip():", "hello  ".rstrip())          # Xóa khoảng trắng ở cuối chuỗi: "hello"
print("8. replace():", "hi world".replace("world", "py"))  # Thay thế chuỗi con "world" bằng "py": "hi py"
print("9. split():", "a,b,c".split(","))           # Chia chuỗi thành danh sách dựa trên dấu phân cách ",": ['a', 'b', 'c']

# Tìm kiếm/Kiểm tra
print("10. find():", "hello".find("lo"))           # Tìm vị trí đầu tiên của "lo" trong chuỗi, trả về chỉ số: 3
print("11. find() (không thấy):", "hello".find("x"))  # Tìm "x" không có trong chuỗi, trả về -1
print("12. index():", "hello".index("lo"))         # Tìm vị trí đầu tiên của "lo", trả về chỉ số: 3 (ném lỗi nếu không thấy)
print("13. startswith():", "hello".startswith("he"))  # Kiểm tra chuỗi có bắt đầu bằng "he" không: True
print("14. endswith():", "hello".endswith("lo"))   # Kiểm tra chuỗi có kết thúc bằng "lo" không: True
print("15. isalpha():", "abc".isalpha())           # Kiểm tra chuỗi chỉ chứa chữ cái: True
print("16. isdigit():", "123".isdigit())           # Kiểm tra chuỗi chỉ chứa số: True
print("17. isspace():", "   ".isspace())           # Kiểm tra chuỗi chỉ chứa khoảng trắng: True

# Nối chuỗi
print("18. join():", " ".join(["hi", "world"]))    # Nối các phần tử trong danh sách bằng dấu cách: "hi world"

# Định dạng
name, age = "Alice", 25
print("19. format():", "Hi, {} is {}".format(name, age))  # Định dạng chuỗi bằng cách thay {} bằng giá trị: "Hi, Alice is 25"
print("20. f-string:", f"Hi, {name} is {age}")     # Định dạng chuỗi bằng f-string (Python 3.6+): "Hi, Alice is 25"

# Khác
print("21. count():", "hello hello".count("hello"))  # Đếm số lần xuất hiện của "hello" trong chuỗi: 2
print("22. len():", len("hello"))                  # Trả về độ dài chuỗi (hàm, không phải phương thức): 5

# Lưu ý
print("\nLưu ý: Chuỗi trong Python là immutable (không thể thay đổi trực tiếp).")