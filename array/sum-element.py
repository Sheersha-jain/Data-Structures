# Python program to find if there are two elements wtih given sum 

def element_Finder(array, array_size, sum ):
    s = set()
    for i in range(0, array_size):
        temp = sum - array[i]
        if (temp>0 and temp in s):
            print("Pair for sum is", temp,array[i])
        s.add(array[i])

element_Finder([10,15,3,7],4, 17)