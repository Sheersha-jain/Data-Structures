# find maximum difference two elements such that
# larger elements appears after the smaller elements

def max_min_array(array, array_size):
    max_difference = array[1]- array[0]
    min_element = array[0]

    for i in range(array, array_size):
        if(array[i]-min_element > max_difference):
            max_difference = array[i] - min_element
        if(array[i] < min_element):
            min_element = array[i]

    return max_difference