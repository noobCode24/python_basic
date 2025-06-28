# File: algorithms_basic.py
# Các thuật toán cơ bản trong Python

# 1. Tìm kiếm nhị phân (Binary Search)
def binary_search(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
print("1. Binary Search:", binary_search([1, 2, 3, 4, 5], 3))  # 2

# 2. Sắp xếp nổi bọt (Bubble Sort)
def bubble_sort(nums):
    n = len(nums)
    for i in range(n):
        for j in range(0, n - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums
print("2. Bubble Sort:", bubble_sort([5, 2, 9, 1]))  # [1, 2, 5, 9]

# 3. Đệ quy - Tính giai thừa
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)
print("3. Factorial (Recursion):", factorial(5))  # 120

# 4. Hai con trỏ (Two Pointers) - Tìm cặp số tổng bằng target
def two_sum_pointers(nums, target):
    left, right = 0, len(nums) - 1
    while left < right:
        if nums[left] + nums[right] == target:
            return [left, right]
        elif nums[left] + nums[right] < target:
            left += 1
        else:
            right -= 1
    return []
print("4. Two Pointers:", two_sum_pointers([2, 7, 11, 15], 9))  # [0, 1]