def rooks_are_safe(chessboard):
    n = len(chessboard)
    for row_index in range(n):
        row_count = 0
        #print("row_index", row_index)
        for col_index in range(n):
            #print("col index", col_index)

            row_count = chessboard[row_index][col_index]
            #print("row count is",row_count)


#rooks_are_safe([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])


def print_2d(chessboard):
    n = len(chessboard)
    """
    for row in range(n):
        #print("row is ",row)
        for col in range(n):
            #print("column is", col)
            print(chessboard[row][col])
    """

    for col in range(n):
        for row in range(n) :
            print(chessboard[col][row])
print_2d([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])


