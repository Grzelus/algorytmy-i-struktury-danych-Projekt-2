from collections import deque
from node import Node

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if node is None:
            return Node(key)
        if key < node.key:
            node.left = self._insert(node.left, key)
        else:
            node.right = self._insert(node.right, key)
        return node

    def decreasing(self):
        self._decreasing(self.root)

    def _decreasing(self, node):
        if node:
            self._decreasing(node.right)
            print(node.key)
            self._decreasing(node.left)

    def preorder(self):
        self._preorder(self.root)

    def _preorder(self, node):
        if node:
            print(node.key)
            self._preorder(node.left)
            self._preorder(node.right)

    def find_level(self, value):
        def find_key(node, value, level):
            if not node:
                return -1
            if node.key == value:
                return level
            elif value < node.key:
                return find_key(node.left, value, level + 1)
            else:
                return find_key(node.right, value, level + 1)

        level = find_key(self.root, value, 0)
        if level != -1:
            self.print_level(level)
        else:
            print("Nie znaleziono klucza.")

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

    def balance_dsw(self):
        dummy = Node(None)
        dummy.right = self.root
        vine_size = self._create_branch(dummy)
        self._vine_to_tree(dummy, vine_size)
        self.root = dummy.right

    def print_levels(self):
        if not self.root:
            return
        queue = deque([(self.root, 0)])
        current_level = 0
        print("Level 0:")
        while queue:
            node, level = queue.popleft()
            if level != current_level:
                current_level = level
                print(f"Level {level}:")
            print(node.key)
            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))

    def _create_branch(self, tail):
        count = 0
        current = tail.right
        while current:
            if current.left:
                rotated = self._rotate_right(current)
                tail.right = rotated
                current = rotated
            else:
                count += 1
                tail = current
                current = current.right
        return count

    def _compress(self, tail, count):
        current = tail.right
        for _ in range(count):
            if current and current.right:
                rotated = self._rotate_left(current)
                tail.right = rotated
                tail = rotated
                current = tail.right

    def _vine_to_tree(self, tail, size):
        leaves = size + 1 - 2 ** (size.bit_length() - 1)
        self._compress(tail, leaves)
        size = size - leaves
        while size > 1:
            self._compress(tail, size // 2)
            size //= 2

    def _rotate_left(self, root):
        temp = root.right
        temp_left = temp.left
        temp.left = root
        root.right = temp_left
        return temp

    def _rotate_right(self, root):
        temp = root.left
        temp.right = temp.right
        temp.right = root
        root.left = temp.right
        return temp
    
    def print_level(self, target_level):
        def _print_level(node, level):
            if not node:
                return
            if level == 0:
                print(node.key)
            else:
                _print_level(node.left, level - 1)
                _print_level(node.right, level - 1)

        _print_level(self.root, target_level)
