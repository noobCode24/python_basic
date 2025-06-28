# File: dict_methods.py
# Thao tác với kiểu dữ liệu từ điển (dict) trong Python

d = {"a": 1, "b": 2}
print("1. get():", d.get("a"))           # Lấy giá trị của key "a": 1
print("2. keys():", list(d.keys()))      # Danh sách các key: ['a', 'b']
print("3. values():", list(d.values()))  # Danh sách các value: [1, 2]
print("4. items():", list(d.items()))    # Danh sách cặp (key, value): [('a', 1), ('b', 2)]
print("5. update():", d.update({"c": 3}) or d)  # Cập nhật từ điển với cặp mới: {"a": 1, "b": 2, "c": 3}
print("6. pop():", d.pop("b"))           # Xóa và trả về giá trị của "b": 2, d = {"a": 1, "c": 3}
print("7. popitem():", d.popitem())      # Xóa và trả về cặp cuối: ("c", 3), d = {"a": 1}
print("8. clear():", d.clear() or d)     # Xóa toàn bộ từ điển: {}