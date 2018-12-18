a = [['a','b','c','d'],['f','g','h','i'],['k','l','m','n'],['p','q','r','s']]
def matrix():
    row = len(a)
    col = len(a[0])
    for i in range(row):
        for j in range(col):
            print(a[i][j], end=" ")
        print("\n")

matrix()

print("=======================")

def transposeMat():
    row = len(a)
    col = len(a[0])
    for j in  range(col):
        for i in range(row):
            print(a[i][j], end= " ")
        print("\n")

transposeMat()