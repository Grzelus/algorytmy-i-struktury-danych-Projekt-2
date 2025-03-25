class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert_rec(self.root, key)

    def _insert_rec(self, node, key):
        if node is None:
            return Node(key)
        if key < node.key:
            node.left = self._insert_rec(node.left, key)
        if key > node.key:
            node.right = self._insert_rec(node.right, key)
        return node

    def search(self,key):
        return self._search_rec(self.root,key)
    
    def _search_rec(self, node, key):
        if node is None or node.key == key:
            return node
        if key < node.key:
            return self._search_rec(node.left, key)
        else:
            return self._search_rec(node.right, key)
    
    def inorder(self):
        self._inorder_rec(self.root)
        print()

    def _inorder_rec(self, node):
        if node:
            self._inorder_rec(node.left)
            print(node.key,end=' ')
            self._inorder_rec(node.right)

    def delete(self, key):
        self.root = self._delete_rec(self.root, key)

    def _delete_rec(self, node, key):
        if node is None:
            return None
        if key < node.key:
            node.left = self._delete_rec(node.left,key)
        elif key > node.key:
            node.right = self._delete_rec(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            min_larger_node = self._min_value_node(node.right)
            node.key = min_larger_node.key
            node.right = self._delete_rec(node.right, min_larger_node.key)

        return node

    def _min_value_node(self,node):
        current = node
        while current.left:
            current = current.left
        return current
        

tree = BST()
for key in [50, 30, 70, 20, 40, 60, 80]:
    tree.insert(key)

print("In-order traversal:")
tree.inorder()  # Powinno wypisać: 20 30 40 50 60 70 80

print("Szukam 60:", "Znaleziono" if tree.search(60) else "Nie znaleziono")

tree.delete(70)
print("Po usunięciu 70:")
tree.inorder()  # 20 30 40 50 60 80
        