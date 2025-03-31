
from collections import deque
from node import Node

class HeapMinTree:
    def __init__(self, root_key=None):
        if root_key is not None:
            self.root = Node(root_key)
        else:
            self.root = None

    def insert(self, value):
        if not self.root:
            self.root = Node(value)
            return

        queue = deque([self.root])

        while queue:
            node = queue.popleft()

            if node.left:
                queue.append(node.left)
            else:
                node.left = Node(value)
                node.left.parent = node
                self._bubble_up(node.left)
                return

            if node.right:
                queue.append(node.right)
            else:
                node.right = Node(value)
                node.right.parent = node
                self._bubble_up(node.right)
                return

    def _bubble_up(self, node):
        while node.parent and node.parent.key > node.key:
            node.parent.key, node.key = node.key, node.parent.key
            node = node.parent

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
