import time
from datetime import timedelta
import random
import sys

sys.setrecursionlimit(100000)

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
    def __show__(self):
        print(f"{self.key} - {self.data}") 

    ## dodawanie elementu do drzewa
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
    
    ##wypisywanie preorder
    def preOrder(self):
        print(self.key)
        if self.left:
            self.left.preOrder()
        if self.right:
            self.right.preOrder()


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
Tree.insert(22)
Tree.insert(1)
Tree.insert(8)
Tree.insert(12)
Tree.insert(3)
Tree.insert(120)
Tree.insert(222)
Tree.levelFind(222)





