def matrix():
    n = 3
    m = 4
    a = [0] * n
    for i in range(n):
        a[i] = [0] * m
    print(a)
#matrix()

from numpy import * 

x = range(16)

x = reshape(x,(4,4)) 

print(x) 

