def printRev(n):
    if(n > 0):
        print("printed first", n)
        print(n)
        printRev(n-1)

printRev(5)