def horizontalMatrix():
   a = [['a','b','c','d'],['f','g','h','i'],['k','l','m','n'],['p','q','r','s']]
   row = len(a)
   col = len(a[0])
   for i in range(row):
      for j in range(col):
         print(a[i][j], end=" ")
      print("\n")

horizontalMatrix()

print("========")

def verticalMatrix():
   a = [['a','b','c','d','e'],['f','g','h','i','j'],['k','l','m','n','o'],['p','q','r','s','t']]
   row = len(a)
   col = len(a[0])
   for j in range(col):
      for i in range(row):
         print(a[i][j], end=" ")
      print("\n")

verticalMatrix()

print("=========")

def lowerMatrix():
   a = [['a','b','c','d'],['f','g','h','i'],['k','l','m','n'],['p','q','r','s']]
   row = len(a)
   col = len(a[0])
   for i in range(row):
      for j in range(i+1):
         print(a[i][j], end=" ")
      print("\n")

lowerMatrix()

print("====== Upper")

def uppermatrix():
   a = [['a','b','c','d'],['f','g','h','i'],['k','l','m','n'],['p','q','r','s']]
   row = len(a)
   col = len(a[0])
   k = col
   for i in range(row):
      for j in range(k):
         print(a[i][j], end=" ")
      k= k-1
      print("\n")

uppermatrix()

print("====== Upper Right")

def upperRightmatrix():
   a = [['a','b','c','d'],['f','g','h','i'],['k','l','m','n'],['p','q','r','s']]
   row = len(a)
   col = len(a[0])
   for i in range(row):
      string =  ""
      for k in range(i):
         string += " "
      for j in range(i, col, +1):
         string += a[i][j]
      print(string)


upperRightmatrix()

print("======")

def lowerRightmatrix():
   a = [['a','b','c','d'],['f','g','h','i'],['k','l','m','n'],['p','q','r','s']]
   row = len(a)
   col = len(a[0])
   k = col
   for i in range(row):
      string = ""
      for s in range(k-1):
         string += " "
      k =k-1
      for j in range(k, col, +1):
         string += a[i][j]
      print(string)

lowerRightmatrix()

print("======")


# print boundary matrix
def boundaryMatrix():
   a = [['a','b','c','d'],['f','g','h','i'],['k','l','m','n'],['p','q','r','s']]
   row = len(a)
   col = len(a[0])
   string = " "
   for j in range(col-1):
      print(a[0][j], end=" ")
   for i in range(row-1):
      print(a[i][col-1], end=" ")
   for j in range(col-1,0,-1):
      print(a[row-1][j], end=" ")
   for i in range(row-1, 0,-1):
      print(a[i][0], end=" ")

   print(string)

boundaryMatrix()

print("=======")
