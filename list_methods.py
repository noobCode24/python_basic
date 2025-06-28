# File: list_methods.py
# Thao tác với kiểu dữ liệu danh sách (list) trong Python

lst = [1, 2, 3]
print("1. append():", lst.append(4) or lst)  # Thêm 4 vào cuối danh sách: [1, 2, 3, 4]
print("2. insert():", lst.insert(0, 0) or lst)  # Chèn 0 vào vị trí 0: [0, 1, 2, 3, 4]
print("3. extend():", lst.extend([5, 6]) or lst)  # Mở rộng danh sách bằng [5, 6]: [0, 1, 2, 3, 4, 5, 6]
print("4. remove():", lst.remove(0) or lst)  # Xóa phần tử 0 đầu tiên: [1, 2, 3, 4, 5, 6]
print("5. pop():", lst.pop(1))           # Xóa và trả về phần tử tại chỉ số 1: 2, lst = [1, 3, 4, 5, 6]
print("6. clear():", lst.clear() or lst)  # Xóa toàn bộ danh sách: []
lst = [3, 1, 2]
print("7. sort():", lst.sort() or lst)    # Sắp xếp danh sách: [1, 2, 3]
print("8. reverse():", lst.reverse() or lst)  # Đảo ngược danh sách: [3, 2, 1]
print("9. index():", lst.index(2))        # Tìm chỉ số của 2: 1
print("10. count():", [1, 2, 2].count(2))  # Đếm số lần xuất hiện của 2: 2