### Find the index of array where RHS of array is equal to LHS considering index point is not being added.

def equate():
    a = [4,3,-1,3,-2,1,7]

    for i in range(len(a)):
         if sum(a[0:i]) == sum(a[i+1:]):
            print "found", i

equate()
