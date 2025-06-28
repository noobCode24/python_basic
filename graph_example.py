# File: graph_example.py
# Ví dụ cơ bản về đồ thị trong Python (dùng dict)

graph = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "D"],
    "D": ["B", "C"]
}

def dfs(graph, start, visited=None):  # Duyệt đồ thị theo chiều sâu (DFS)
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=" ")             # In: A B D C
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

print("1. DFS traversal:")
dfs(graph, "A")
print()