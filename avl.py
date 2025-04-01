
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
            print(node.key)
            return node
        else:
            print(f"{node.key} -> ", end="")
            return self.find_min(node.left)
        
    def find_max(self, node):
        if node.right is None:
            print(node.key)
            return node
        else:
            print(f"{node.key} -> ", end="")
            return self.find_max(node.right)

    def decreasing(self):
        self._decreasing(self.root)

    def _decreasing(self, node):
        if node:
            self._decreasing(node.right)
            print(node.key,end=" ")
            self._decreasing(node.left)

    def _preorder(self, node):
        if node:
            print(node.key)
            self._preorder(node.left)
            self._preorder(node.right)

    def _search(self, node, key):
        if not node or node.key == key:
            return node
        if key < node.key:
            return self._search(node.left, key)
        else:
            return self._search(node.right, key)
        
    def _height(self, node):
        if not node:
            return - 1
        return 1 + max(self._height(node.left), self._height(node.right))

    def _delete_subtree(self, node, key):
        if not node:
            return None
        if node.key == key:
            self._postorder_delete(node)
            return None  # usuń cały podwęzeł
        node.left = self._delete_subtree(node.left, key)
        node.right = self._delete_subtree(node.right, key)
        return node

    def _postorder_delete(self, node):
        if not node:
            return
        self._postorder_delete(node.left)
        self._postorder_delete(node.right)
        print(f"Usuwanie węzła: {node.key}")
        node.left = None
        node.right = None
        node.parent = None

    def print_and_delete_subtree(self, key):
        node = self._search(self.root, key)
        if node:
            print(f"Poddrzewo o korzeniu {key} (preorder):")
            self._preorder(node)
            print(f"Wysokość poddrzewa: {self._height(node)}")
            self.root = self._delete_subtree(self.root, key)
        else:
            print(f"Nie znaleziono węzła o kluczu {key}.")