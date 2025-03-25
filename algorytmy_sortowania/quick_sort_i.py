def quick_sort_i(array):
    stack = [(0, len(array)- 1)]
    while stack:
        left, right = stack.pop()

        if left >= right:
            continue

        pivot = array[right]
        i = left - 1

        for j in range(left, right):
            if array[j] > pivot:
                i += 1
                array[i], array[j] = array[j], array[i]
        
        array[i+1], array[right] = array[right], array[i+1]
        pivot_index = i+1

        stack.append((left, pivot_index - 1))
        stack.append((pivot_index + 1, right))

    return array