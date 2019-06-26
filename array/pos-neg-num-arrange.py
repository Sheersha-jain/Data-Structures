# rearrange positive and negative numbers
# like : array= [1,-2,3,-4,5,6,7]

def rearrange(array, n):
    i = -1
    for j in range(n):
        if array[j]<0:
            i = i+1
            array[i], array[j] = array[j], array[i]

    positive, negetive = i+1, 0

    while(positive< n and negetive < positive, array[negetive]<0):
        array[negetive], array[positive] = array[positive], array[negetive]
        positive += 1
        negetive += 2

def printArray(array, n):
    for i in range(n):
        print(array[i])