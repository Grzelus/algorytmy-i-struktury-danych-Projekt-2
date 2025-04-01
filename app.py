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

    choice = int(input("Wybierz sposób sortowania wygenerowanych liczb \n 1) losowo\n 2) rosnąco\n"))

    if choice == 1:
        return output
    if choice == 2:
        output.sort()
        return output
    print("Wybierz właściwą opcje: ")
    return []

def create_input_data(choice):
    if choice == 1:
        file_name = input("Podaj nazwę pliku: ")
        data = read_from_file(file_name)
    elif choice == 2:
        n = int(input("Ile liczb chcesz wygenerować: "))
        min_value = int(input("Podaj wartość minimalną losowanych liczb: "))
        max_value = int(input("Podaj wartość maksymalną losowanych liczb: "))
        data = generate(n, min_value, max_value)
    else:
        print("Wybierz właściwą opcję: ")
        data = []

    return data
    

while 1:
    print("1) Wyszukanie najmniejszego elementu wraz ze ścieżką do niego prowadzącą")
    print("2) Wyszukanie najwiekszego elementu wraz ze ścieżką")
    print("3) Wyszukanie elementu i wypisanie całego poziomu drzewa")
    print("4) Wypisanie całego drzewa w porządku malejącym")
    print("5) Wypisanie poddrzewa w porządku pre-order")
    print("6) Quit")
    choice=int(input("Wybierz operację: "))
    if choice == 6:
        break

    tree_type = int(input("Jaki rodzaj drzewa chcesz zbudować:\n1) BST\n2) AVL\n3) Heap Min\n"))
    input_type = int(input("Skąd chcesz pobrać dane:\n1) Z pliku tekstowego\n2) generowane losowo\n"))

    data = create_input_data(input_type)

    tree = None

    start=-1
    end=-1
    if tree_type == 1:
        tree = BST()
        for num in data:
            tree.insert(num)
        print("Przed równoważeniem: ")
        tree.print_levels()    
        balanceSt=time.time()
        tree.balance_dsw()
        balanceEnd=time.time()

        print("Po równoważeniu: ")
        tree.print_levels()
        print(f"Czas równoważenia wynosił: {balanceEnd-balanceSt}")

        if choice==1:
            start=time.time()
            tree.find_min(tree.root)
            end=time.time()
        elif choice==2:
            start=time.time()
            tree.find_max(tree.root)
            end=time.time()
        elif choice==3:
            key=int(input("Podaj klucz: "))

            tree.find_level(key)
        elif choice==4:
            tree.decreasing()
            print("\n")
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
            tree.print_levels()
            start=time.time()
            tree.find_min(tree.root)
            end=time.time()
        elif choice==2:
            tree.print_levels()
            start=time.time()
            tree.find_max(tree.root)
            end=time.time()
        elif choice==3:
            tree.print_levels()
            key=int(input("Podaj klucz: "))
            tree.find_level(key)
        elif choice==4:
            tree.print_levels()
            tree.decreasing()
            print("\n")
        elif choice==5:
            tree.print_levels()
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
            tree.find_min(tree.root)
            end=time.time()
        elif choice==2:
            start=time.time()
            tree.find_max(tree.root)
            end=time.time()
        elif choice==3:
            key=int(input("Podaj klucz: "))
            tree.find_level(key)
        elif choice==4:
            tree.decreasing()

        elif choice==5:

            start=time.time()
            # tree.
            end=time.time()
        else:
            print("Nie ma takiej opcji")

    else:
        print("niepoprawny wybór drzewa")
    if end!=-1  and start!=-1:
        timeDifference=end-start
        print(f"czas operacji wynosi: {timeDifference}")
    
    



