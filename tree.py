import time
from datetime import timedelta
import random
import sys
sys.setrecursionlimit(100000)
from collections import deque


def generate(n,min_value, max_value):
    if(min_value > max_value):
        print("minimalna wartość nie powinna być większa od maksymalnej.")
        return []
    output = [random.randint(min_value,max_value) for _ in range(n)]
    output = [random.randint(min_value,max_value) for _ in range(n)]

    choice = int(input("Wybierz sposób sortowania wygenerowanych liczb \n 1) losowo\n 2) rosnąco "))

    if choice == 1:
        return output
    if choice == 2:
        output.sort()
        return output
    print("wybierz właściwą opcje")
    return []

class Node:
    def __init__(self,key):
        self.key=key
        self.right=None
        self.left=None
        self.parent=None
    def __show__(self):
        print(f"{self.key} - {self.data}") 

    ## dodawanie elementu do drzewa BST
    def insert(self,value):
        if self.key>value:
            if self.left is None:
                self.left = Node(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right=Node(value)
            else:
                self.right.insert(value)

    ## dodawanie wartości na koniec kopca(Heap)
    def childrenCheck(self):
        actual=Node(0)
        actual=self
        if actual.parent and actual.parent.key>actual.key:
            [actual.parent.key,actual.key]=[actual.key,actual.parent.key]
            actual.parent.childrenCheck()
    
    def HeapMinInsert(self,value):
        if not self:
            self.key=value
    
        queue = deque([self])  # Kolejka przechowująca węzły do zwiedzenia
    
        while queue:
            node = queue.popleft()  # Pobieramy pierwszy węzeł
        
            if node.left:
                queue.append(node.left)  # Dodajemy lewego potomka
            else:
                node.left=Node(value)
                node.left.parent=node
                node.left.childrenCheck()
                return
            if node.right:
                queue.append(node.right)  # Dodajemy prawego potomka
            else:
                node.right=Node(value)
                node.right.parent=node
                node.right.childrenCheck()
                return
    

    
    ##wypisywanie preorder
    def preOrder(self):
        print(self.key)
        if self.left:
            self.left.preOrder()
        if self.right:
            self.right.preOrder()
            
    ##wypisywanie w porządku malejącym
    def decreasing(self):
        if self.right:
            self.right.decreasing()
        print(self.key)
        if self.left:
            self.left.decreasing()

    ##znajdywanie min
    def inOrderTraversalMin(self):
        print(self.key)
        if self.left:
            return self.left.inOrderTraversalMin()
    
    ##znajdywanie max
    def inOrderTraversalMax(self):
        print(self.key)
        if self.right:
            self.right.inOrderTraversalMax()  
    ## wypisywanie poziomu drzewa
    def printLevel(self,level):
        if(level==0):
            print(self.key)
        else:
            level-=1
            if self.right:
                self.right.printLevel(level)
            if self.left:
                self.left.printLevel(level)
    ##znajdowanie konkretnej wartości klucza
    def findKey(self,value,level):
        level+=1
        if self.key>value:
            if self.left.key == value:
                return level
            else:
                return self.left.findKey(value,level)
        else:
            if self.right.key == value:
                return level
            else:
                return self.right.findKey(value,level)
    ##znajdowanie poziomu i wypisanie go 
    def levelFind(self,value):
        level=0
        if self.key!=value:
            level=self.findKey(value,0)
            self.printLevel(level)
        else:
            print(self.key)


##tworzenie drzewa AVL
def AVL (Tab, Tree):
    if len(Tab)==0:
        return
    if len(Tab)==1:
        Tree.insert(Tab[0])
        return
    mid=len(Tab)//2
    Tree.insert(Tab[mid])
    left=Tab[0:mid]
    right=Tab[mid+1:len(Tab)]
    AVL(left,Tree)
    AVL(right,Tree)


Tree=Node(10)
Tree.HeapMinInsert(22)
Tree.HeapMinInsert(1)
Tree.HeapMinInsert(8)
Tree.HeapMinInsert(12)
Tree.HeapMinInsert(3)
Tree.HeapMinInsert(120)
Tree.HeapMinInsert(222)
Tree.printLevel(0)
Tree.printLevel(1)
Tree.printLevel(2)
Tree.printLevel(3)





