from node import Node
from avl import AVL
from bst import BST
from heapmin import HeapMinTree

import time
from datetime import timedelta
import random

def read_from_file(filename):
    with open(filename, 'r') as f:
        content = f.read()
    numbers = list(map(int, content.strip().split()))
    return numbers

def generate(n,min_value, max_value):
    if(min_value > max_value):
        print("minimalna wartość nie powinna być większa od maksymalnej.")
        return []
    
    output = [random.randint(min_value,max_value) for _ in range(n)]

    choice = int(input("Wybierz sposób sortowania wygenerowanych liczb \n 1) losowo\n 2) rosnąco "))

    if choice == 1:
        return output
    if choice == 2:
        output.sort()
        return output
    print("wybierz właściwą opcje")
    return []

def create_input_data(choice):
    if choice == 1:
        file_name = input("podaj nazwę pliku")
        data = read_from_file(file_name)
    elif choice == 2:
        n = int(input("Ile liczb chcesz wygenerować?"))
        min_value = int(input("Podaj wartość minimalną losowanych liczb:"))
        max_value = int(input("Podaj wartość maksymalną losowanych liczb:"))
        data = generate(n, min_value, max_value)
    else:
        print("Wybierz właściwą opcję.")
        data = []

    return data
    


tree_type = int(input("Jaki rodzaj drzewa chcesz zbudować:\n1) BST\n2) AVL\n 3) Heap Min"))
input_type = int(input("Skąd chcesz pobrać dane:\n1) Z pliku tekstowego\n2) generowane losowo"))

data = create_input_data(input_type)

tree = None

if tree_type == 1:
    tree = BST()
    for num in data:
        tree.insert(num)

elif tree_type == 2:
    tree = AVL()
    data.sort()
    tree.build_from_sorted_list(data)

elif tree_type == 3:
    tree = HeapMinTree()
    for num in data:
        tree.insert(num)

else:
    print("niepoprawny wybór drzewa")




