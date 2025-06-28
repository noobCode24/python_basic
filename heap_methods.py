# File: heap_methods.py
# Thao tác với heap (Priority Queue) trong Python - Min Heap mặc định

import heapq
heap = [3, 1, 4]
heapq.heapify(heap)                                      # Chuyển list thành min-heap: [1, 3, 4]
print("1. heapify:", heap)
print("2. heappush:", heapq.heappush(heap, 2) or heap)   # Thêm 2 vào heap: [1, 2, 4, 3]
print("3. heappop:", heapq.heappop(heap))                # Lấy và xóa phần tử nhỏ nhất: 1, heap = [2, 3, 4]
print("4. top:", heap[0])                                # Xem phần tử nhỏ nhất mà không xóa: 2