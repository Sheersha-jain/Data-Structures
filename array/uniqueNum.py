# print unique number from array.
a=[1,2,3,1,2]
def uniqueNum():
    for i in range(len(a)):
        count = 1
        for j in range(len(a)):
            if a[i] == a[j]:
                count = count +1
        if count <= 2:
            print("unique number is :", a[i])

uniqueNum()

a=[1,1,1,1,2,2,3,4,3,3,4]
def oddOccurrence():
    for i in range(len(a)):
        count = 1
        for j in range(len(a)):
            if a[i] == a[j]:
                count = count +1
        if count%2 ==0:
            print("odd occurrence :", a[i])

oddOccurrence()



