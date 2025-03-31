
from node import Node

class AVL:
    def __init__(self):
        self.root = None

    def build_from_sorted_list(self, array):
        def build(low, high):
            if low > high:
                return None
            mid = (low + high) // 2
            node = Node(array[mid])
            node.left = build(low, mid - 1)
            node.right = build(mid + 1, high)
            return node

        self.root = build(0, len(array) - 1)

    def find_min(self, node):
        if node.left is None:
            return node
        else:
            print(f"{node.key} -> ", end="")
            return self.find_min(node.left)
        
    def find_max(self, node):
        if node.right is None:
            return node
        else:
            print(f"{node.key} -> ", end="")
            return self.find_max(node.right)

    def preorder(self):
        def _preorder(node):
            if node:
                print(node.key)
                _preorder(node.left)
                _preorder(node.right)

        _preorder(self.root)
