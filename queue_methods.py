# File: queue_methods.py
# Thao tác với hàng đợi (Queue) trong Python - FIFO (First In First Out)

from collections import deque
queue = deque()
print("1. enqueue (append):", queue.append(1) or queue)  # Thêm 1 vào cuối: deque([1])
print("2. enqueue (append):", queue.append(2) or queue)  # Thêm 2 vào cuối: deque([1, 2])
print("3. dequeue (popleft):", queue.popleft())          # Lấy và xóa phần tử đầu: 1, queue = deque([2])
print("4. front:", queue[0])                             # Xem phần tử đầu mà không xóa: 2
print("5. is_empty:", not queue)                         # Kiểm tra queue rỗng: False
print("6. size:", len(queue))                            # Kích thước queue: 1