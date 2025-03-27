class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


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
    

    class AVL:
        def __init__(self):
             self.root = None

        def build_from_sorted_list(self, list):
            def build(low, high):
                if low > high:
                    return None
                mid = (low + high) // 2
                node = Node(list[mid])
                node.left = build(low, mid-1)
                node.right = build(mid+1, high)
                return node
            self.root = build(0, len(list)-1)

        def preorder(self, node):
            if node:
                print(node.key, end=" ")
                self.preorder(node.left)
                self.preorder(node.right)

        def search(self, node, key):
            if node is None or node.key == key:
                return node
            if key < node.key:
                return self.search(node.left, key)
            else:
                return self.search(node.right, key)
            
        def get_height(self, node):
            if not node:
                return 0
            return node.height


        def get_balance(self, node):
            if not node:
                return 0
            return self.get_height(node.left) - self.get_height(node.right)

        def rotate_left(self, z):
            y = z.right
            T2 = y.left

            y.left = z
            z.right = T2

            z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
            y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

            return y

        def rotate_right(self, y):
            x = y.left
            T2 = x.right

            x.right = y
            y.left = T2

            y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
            x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))

            return x