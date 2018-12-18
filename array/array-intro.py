import array

arr = array.array('i', [1,2,3])
print "arr = ",  arr
print "array.array", array.array

arr.append(4)
print arr
arr.insert(2,5)
print arr

arr.pop(2)
print arr

arr.append(1)
print arr

arr.remove(1)
print arr

print arr.index(2)
