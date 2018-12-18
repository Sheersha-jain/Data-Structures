a = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
b = [[1,0,2,3],[5,2,3,4],[2,1,2,1],[1,0,1,0]]

def matrixOperations():
    row = len(a)
    col = len(a[0])
    for i in range(row):
        for j in range(col):
            print(a[i][j], end=" ")
        print("\n")

    for i in range(len(b)):
        for j in range(len(b[0])):
            print(b[i][j], end=" ")
        print("\n")

    for i in range(len(a[0])):
        for j in range(len(b[0])):
            print(sum(a[i], b[i]), end=" ")
        print("\n")

matrixOperations()