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
    def inOrderTraversalMin(self):
        print(self.key)
        if self.left:
            return self.left.inOrderTraversalMin()
        
    def inOrderTraversalMax(self):
        print(self.key)
        if self.right:
            self.right.inOrderTraversalMax()  
        

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


##def insert(parent, child,depth=0):
  ##  if(parent == None):
    ##    child.depth=depth
      ##  return child
    ##elif(child.key==parent.key):
      ##  return parent
   ## elif(child.key>parent.key):
     ##   parent.left=insert(parent.left,child,depth+1)
    ##else:
      ##  parent.right=insert(parent.right,child,depth+1)
    ##return parent

Tree=Node(10)
Tree.insert(22)
Tree.insert(1)
Tree.insert(8)
Tree.insert(12)
Tree.insert(3)
Tree.insert(120)
Tree.inOrderTraversalMin()





