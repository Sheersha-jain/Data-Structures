# move all negative integers in the end of array.
a = [ 2, 3, -1 , 3 ,4, -3, -4, 6]
def shifter():
    i =0
    j= len(a)-1
    while(i<j):
        while a[i]>0:
            i=i+1

        while a[j]<0:
            j=j-1

        if i<j:
            a[i], a[j] = a[j], a[i]

    print(a)

shifter()
