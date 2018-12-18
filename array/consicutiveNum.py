a= [83,78,80,81,79,82]
def maxMin():
    max =0
    min=100
    for i in range(len(a)):
        if a[i] > max:
            max = a[i]
        for i in range(len(a)):
            if a[i]<min:
                min  = a[i]
    print(min, max)

maxMin()

def consecutiveNum():

   min = 78
   max = 83
   k = max-min
   set_a = set(a)
   for i in range(len(a)):
       if min+k in set_a:
           print("yes", a[i])
       k = k-1

consecutiveNum()

