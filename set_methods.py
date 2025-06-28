# File: set_methods.py
# Thao tác với kiểu dữ liệu tập hợp (set) trong Python

s = {1, 2, 3}
print("1. add():", s.add(4) or s)        # Thêm 4 vào tập hợp: {1, 2, 3, 4}
print("2. update():", s.update({5, 6}) or s)  # Thêm nhiều phần tử từ {5, 6}: {1, 2, 3, 4, 5, 6}
print("3. remove():", s.remove(6) or s)  # Xóa 6 (ném lỗi nếu không có): {1, 2, 3, 4, 5}
print("4. discard():", s.discard(10) or s)  # Xóa 10 (không ném lỗi nếu không có): {1, 2, 3, 4, 5}
print("5. pop():", s.pop())              # Xóa và trả về phần tử ngẫu nhiên: ví dụ 1, s = {2, 3, 4, 5}
print("6. clear():", s.clear() or s)     # Xóa toàn bộ tập hợp: set()
s = {1, 2, 3}
print("7. union():", s.union({4, 5}))    # Hợp tập hợp: {1, 2, 3, 4, 5}
print("8. intersection():", s.intersection({2, 3, 4}))  # Giao tập hợp: {2, 3}
print("9. difference():", s.difference({2}))  # Hiệu tập hợp: {1, 3}