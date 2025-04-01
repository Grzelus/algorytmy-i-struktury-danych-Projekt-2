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
            print(node.key,end=" ")
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
                print(f"\nLevel {level}:")
            print(node.key, end=" ")
            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))
        print("\n")

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
        root.right = temp.left    
        temp.left = root          
        return temp               

    def _rotate_right(self, root):
        temp = root.left          
        root.left = temp.right     
        temp.right = root         
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