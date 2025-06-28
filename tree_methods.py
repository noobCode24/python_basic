# File: tree_example.py
# Ví dụ cơ bản về cây nhị phân trong Python

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Tạo cây:    1
#           / \
#          2   3
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

def inorder(node):  # Duyệt cây theo thứ tự giữa (inorder)
    if node:
        inorder(node.left)
        print(node.val, end=" ")  # In: 2 1 3
        inorder(node.right)

print("1. Inorder traversal:")
inorder(root)
print()