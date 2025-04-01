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
    

while 1:
    tree_type = int(input("Jaki rodzaj drzewa chcesz zbudować:\n1) BST\n2) AVL\n 3) Heap Min"))
    input_type = int(input("Skąd chcesz pobrać dane:\n1) Z pliku tekstowego\n2) generowane losowo"))

    data = create_input_data(input_type)

    tree = None
    print("1) Wyszukanie najmniejszego elementu wraz ze ścieżką do niego prowadzącą")
    print("2) Wyszukanie najwiekszego elementu wraz ze ścieżką")
    print("3) Wyszukanie elementu i wypisanie całego poziomu drzewa")
    print("4) Wypisanie całego drzewa w porządku malejącym")
    print("5) Wypisanie poddrzewa w porządku pre-order")
    choice=int(input("Wybierz operację"))

    if tree_type == 1:
        tree = BST()
        for num in data:
            tree.insert(num)
        print("Przed równoważeniem:")
        tree.print_levels()    
        tree.balance_dsw
        print("Po równoważeniu:")
        tree.print_levels()

        if choice==1:
            start=time.time()
            tree.find_min()
            end=time.time()
        elif choice==2:
            start=time.time()
            tree.find_max()
            end=time.time()
        elif choice==3:
            key=int(input("Podaj klucz: "))
            start=time.time()
            tree.find_level(key)
            end=time.time()
        elif choice==4:
            start=time.time()
            tree.decreasing(tree)
            end=time.time()
        elif choice==5:
            key=int(input("Podaj klucz: "))
            start=time.time()
            tree.print_and_delete_subtree(key)
            end=time.time()
        else:
            print("Nie ma takiej opcji")
    elif tree_type == 2:

        tree = AVL()
        data.sort()
        tree.build_from_sorted_list(data)
        
        if choice==1:
            start=time.time()
            tree.find_min()
            end=time.time()
        elif choice==2:
            start=time.time()
            tree.find_max()
            end=time.time()
        elif choice==3:
            key=int(input("Podaj klucz: "))
            start=time.time()
            tree.find_level(key)
            end=time.time()
        elif choice==4:
            start=time.time()
            tree.decreasing()
            end=time.time()
        elif choice==5:
            key=int(input("Podaj klucz: "))
            start=time.time()
            tree.print_and_delete_subtree(key)
            end=time.time()
        else:
            print("Nie ma takiej opcji")

    elif tree_type == 3:
        tree = HeapMinTree()
        for num in data:
            tree.insert(num)
        if choice==1:
            start=time.time()
            tree.find_min()
            end=time.time()
        elif choice==2:
            start=time.time()
            tree.find_max()
            end=time.time()
        elif choice==3:
            key=int(input("Podaj klucz: "))
            start=time.time()
            tree.find_level(key)
            end=time.time()
        elif choice==4:
            start=time.time()
            tree.decreasing()
            end=time.time()
        elif choice==5:
            start=time.time()
            tree.
            end=time.time()
        else:
            print("Nie ma takiej opcji")

    else:
        print("niepoprawny wybór drzewa")
    timeDifference=end-start
    print(f"czas operacji wynosi: {timeDifference}")
    
    





