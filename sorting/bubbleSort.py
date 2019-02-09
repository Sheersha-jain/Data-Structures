# Bubble Sort
def bubbleSort(array):
    for i in range(len(array)):
        swapped = False
        for j in range(0, len(array)-1-i):
            if array[j]>array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                swapped = True

        if swapped == False:
            break
    print(array)

bubbleSort([8,1,4,2,5])