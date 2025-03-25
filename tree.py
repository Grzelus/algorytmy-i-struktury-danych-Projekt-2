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

def merge(Tab,left,mid,right):
    L=[0 for x in range(mid-left+1)]
    R=[0 for x in range(right-mid)]
    for i in range(mid-left+1):
        L[i]=Tab[left+i]
    for j in range(right-mid):
        R[j]=Tab[mid+1+j]
    l=0
    r=0
    i=left
    while(l<mid-left+1 and r<right-mid):
        if(L[l]>R[r]):
            Tab[i]=L[l]
            l+=1
            i+=1
        else:
            Tab[i]=R[r]
            r+=1
            i+=1
    while(l<mid-left+1):
        Tab[i]=L[l]
        i+=1
        l+=1
    while(r<right-mid):
        Tab[i]=R[r]
        i+=1
        r+=1

def merge_sort(Tab, left, right):
    if(left<right):
        mid=(left+right)//2
        merge_sort(Tab,left,mid)
        merge_sort(Tab,mid+1,right)
        merge(Tab,left,mid,right)