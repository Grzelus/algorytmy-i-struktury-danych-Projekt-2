def quick_sort_r(array):
    if len(array)<=1:
        return array

    pivot = array[len(array)-1]

    left = [x for x in array if x > pivot]
    middle = [x for x in array if x == pivot]
    right = [x for x in array if x < pivot]

    return quick_sort_r(left) + middle + quick_sort_r(right)

