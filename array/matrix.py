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
    print("len a",len(a))
    print("len a0",len(a[0]))
    for j in range(col):
        print("j", j)
        for i in range(row):
            print("i", i)
            print(a[i][j], end= " ")
        print("\n")

transposeMat()