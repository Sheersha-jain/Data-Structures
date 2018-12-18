# Program for array rotation one by one
# TIME COMPLEXITY IS : O(n*d) where d is number of elements to rotate
# Auxiliary Space : O(1)

def rotate(array, d, n):
    # Function to rotate array where d is elements to rotate and n is the size of array
    for i in range(d):
        rotatebyone(array, n)

def rotatebyone(array, n):
    # Logic to perform array rotation by d elements of array of size n
    temp = array[0]
    for i in range(n-1):
        array[i] = array[i+1]
    array[n-1] = temp
    print("ARRAY after rotation is : ")
    print(array)


arr = [1,2,3,4,5,6,7]
rotate(arr, 2, 7)