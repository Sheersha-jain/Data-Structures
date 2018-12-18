def sumIndex(array, start, end):
    sum_array = 0
    for i in range(start,end):
        sum_array += array[i]
    print(sum_array)

arr = [1,2,3,4,5,6,7,8]
sumIndex(arr, 1, 5)
