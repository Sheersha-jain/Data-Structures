# python program to sort 0, 1 and 2
# Dutch national algorithm or 3 way partitioning

def sort(array, array_size):
    low = 0
    mid = 0
    high = array_size -1
    while(mid <= high):
        if array[mid] == 0:
            array[mid], array[low] = array[low], array[mid]
            low = low +1
            mid = mid + 1

        if array[mid] == 1:
            mid = mid + 1

        if array[mid] == 2:
            array[mid], array[high] = array[high], array[mid]
            high = high-1