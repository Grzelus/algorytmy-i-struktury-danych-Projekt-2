
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
                
    def minVal(self):
        print(self.root.key)

    def maxVal(self):
        if not self.root:
            return
        maks=Node(0)
        queue = deque([(self.root)])
        while queue:
            node= queue.popleft()
            if node.left:
                queue.append(node.left)
            else:
                if maks.key< node.key:
                    maks=node
            if node.right:
                queue.append(node.right)
            else:
                if maks.key<node.key:
                    maks=node
        queue.clear()
        node=maks
        while node is not self.root:
            queue.appendleft(node.key)
            node=node.parent
        print(f"{self.root.key} ",end="")
        while queue:
            actual=queue.popleft()
            print(f" -> {actual}",end="")
        print()

    def _search(self,value):
        if not self.root:
            return
        if self.root.key>value:
            print("Nie ma takiego elementu")
            return
        queue = deque([(self.root)])
        while queue:
          #  print(queue[0].key)
            node= queue.popleft()
            if node.key==value:
                return node
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return None


    def _postorder_delete(self, node):
        if not node:
            return
        self._postorder_delete(node.left)
        self._postorder_delete(node.right)
        
        if node.parent:
            if node.parent.left == node:
                node.parent.left = None
            elif node.parent.right == node:
                node.parent.right = None
        else:
            self.root = None 
        node.left = node.right = node.parent = None

    def _height(self, node):
        if not node:
            return -1
        return 1 + max(self._height(node.left), self._height(node.right))
    
    def _preorder(self, node):
        if node:
            print(node.key, end=" ")
            self._preorder(node.left)
            self._preorder(node.right)

    
    def print_and_delete_subtree(self, key):
        node = self._search(key)
        if node:
            print(f"Poddrzewo o korzeniu {key} (preorder):")
            self._preorder(node)
            print(f"\nWysokość poddrzewa: {self._height(node)}")

            if node.parent:
                if node.parent.left == node:
                    node.parent.left = None
                elif node.parent.right == node:
                    node.parent.right = None
            else:
                self.root = None

            self._postorder_delete(node)

            print("\nDrzewo po usunięciu (preorder):")
            self._preorder(self.root)
        else:
            print(f"Nie znaleziono węzła o kluczu {key}.")