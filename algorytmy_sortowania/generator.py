import random

n = int(input("wygeneruj n liczb: "))
min_value = int(input("Podaj minimalną wartość losowanych elementów: "))
max_value = int(input("Podaj maksymalną wartość losowanych elementów: "))

def generate(n,min_value, max_value):
    if(min_value > max_value):
        print("minimalna wartość nie powinna być większa od maksymalnej.")
        return []

    output = [random.randint(min_value,max_value) for _ in range(n)]

    choice = int(input("Wybierz sposób sortowania wygenerowanych liczb \n 1) losowo\n 2) rosnąco\n 3) malejąca\n 4) A-shaped\n 5) V-shape"))

    if choice == 1:
        print(output)
        return output
    if choice == 2:
        output.sort()
        return output
    if choice == 3:
        output.sort()
        output.reverse()
        return output
    if choice == 4:
        half = round(n/2)
        output.sort()
        first_half = [output[x] for x in range(half)]
        second_half = [output[x] for x in range(half, n)]
        second_half.reverse()
        return first_half + second_half
    if choice == 5:
        half = round(n/2)
        output.sort()
        first_half = [output[x] for x in range(half)]
        second_half = [output[x] for x in range(half, n)]
        first_half.reverse()
        return first_half + second_half
    
    print("wybierz właściwą opcje")
    return []
    