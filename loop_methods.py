# File: loop_methods_complete.py
# Thao tác toàn diện với vòng lặp trong Python

# 1. for với danh sách
print("1. for với list:")
lst = [1, 2, 3]
for x in lst:                            # Duyệt từng phần tử trong danh sách
    print(x, end=" ")                    # In: 1 2 3
print()

# 2. for với range()
print("2. for với range():")
for i in range(3):                       # Duyệt từ 0 đến 2
    print(i, end=" ")                    # In: 0 1 2
print()

# 3. for với range(start, stop, step)
print("3. for với range(start, stop, step):")
for i in range(1, 6, 2):                 # Duyệt từ 1 đến 5, bước nhảy 2
    print(i, end=" ")                    # In: 1 3 5
print()

# 4. for với enumerate()
print("4. for với enumerate():")
lst = ["a", "b", "c"]
for index, value in enumerate(lst):      # Lấy cả chỉ số và giá trị
    print(f"Index {index}: {value}")     # In: Index 0: a, Index 1: b, Index 2: c

# 5. while
print("5. while:")
count = 0
while count < 3:                         # Lặp khi count < 3
    print(count, end=" ")                # In: 0 1 2
    count += 1
print()

# 6. break
print("6. break:")
for i in range(5):                       # Thoát khi i = 2
    if i == 2:
        break
    print(i, end=" ")                    # In: 0 1
print()

# 7. continue
print("7. continue:")
for i in range(5):                       # Bỏ qua i = 2
    if i == 2:
        continue
    print(i, end=" ")                    # In: 0 1 3 4
print()

# 8. else trong vòng lặp
print("8. else trong for:")
for i in range(3):                       # Hoàn tất vòng lặp
    print(i, end=" ")                    # In: 0 1 2
else:
    print("Hoàn tất")                    # In: Hoàn tất

# 9. nested loop
print("9. nested loop:")
for i in range(2):                       # Vòng lặp ngoài
    for j in range(2):                   # Vòng lặp trong
        print(f"({i}, {j})", end=" ")    # In: (0, 0) (0, 1) (1, 0) (1, 1)
print()

# 10. for với chuỗi
print("10. for với chuỗi:")
for char in "hello":                     # Duyệt từng ký tự trong chuỗi
    print(char, end=" ")                 # In: h e l l o
print()

# 11. for với từ điển
print("11. for với dict:")
d = {"a": 1, "b": 2}
for key, value in d.items():             # Duyệt qua cặp key-value
    print(f"{key}: {value}", end=" ")    # In: a: 1 b: 2
print()

# 12. for với zip()
print("12. for với zip():")
a = [1, 2]
b = ["x", "y"]
for x, y in zip(a, b):                   # Kết hợp hai danh sách để lặp đồng thời
    print(f"{x}-{y}", end=" ")           # In: 1-x 2-y
print()

# 13. while True (vòng lặp vô hạn)
print("13. while True:")
count = 0
while True:                              # Lặp vô hạn cho đến khi break
    if count == 3:
        break
    print(count, end=" ")                # In: 0 1 2
    count += 1
print()

# 14. try-except trong vòng lặp
print("14. try-except trong for:")
lst = [1, "a", 3]
for x in lst:                            # Duyệt danh sách có lỗi tiềm ẩn
    try:
        print(x + 1, end=" ")            # Cộng 1, lỗi nếu x không phải số
    except TypeError:
        print("Lỗi", end=" ")            # In: 2 Lỗi 4
print()

# 15. List comprehension
print("15. list comprehension:")
squares = [x**2 for x in range(4)]       # Tạo danh sách bình phương từ 0-3
print(squares)                           # In: [0, 1, 4, 9]

# Lưu ý
print("\nLưu ý: Đây là các trường hợp chính của vòng lặp trong Python.")