# File: stack_methods.py
# Thao tác với ngăn xếp (Stack) trong Python - LIFO (Last In First Out)

stack = []
print("1. push (append):", stack.append(1) or stack)  # Thêm 1 vào đỉnh: [1]
print("2. push (append):", stack.append(2) or stack)  # Thêm 2 vào đỉnh: [1, 2]
print("3. pop:", stack.pop())                         # Lấy và xóa phần tử đỉnh: 2, stack = [1]
print("4. peek (top):", stack[-1])                    # Xem phần tử đỉnh mà không xóa: 1
print("5. is_empty:", not stack)                      # Kiểm tra stack rỗng: False
print("6. size:", len(stack))                         # Kích thước stack: 1

#Day la dong sua doi