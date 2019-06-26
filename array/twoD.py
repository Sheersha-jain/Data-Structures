a_2d = [[1,2,3],[5,6,7]]
print(a_2d)
a_2d[1][1] = "99"
print(a_2d)

for row in a_2d:
    for item in row:
        print("hello")

for i in range(len(a_2d)):
    for item in range(len(a_2d[i])):
        print(a_2d[i][item])