def binarySearch(array, low, high, element):
    while low <= high:
        mid = int (low + (high-low)/2 )
        if array[mid] == element:
            return mid
        elif array[mid] < element:
            # low = mid+1
            return binarySearch(array, mid+1, high , element)
        else:
            # high = mid -1
            return binarySearch(array, low,mid-1 , element)
    return -1
array = [1,2,3,4,5]
element = 1
binary_result = binarySearch(array, 0, len(array)-1, element)

if binary_result != -1:
    print("element index", binary_result)

else:
    print("element not present")
