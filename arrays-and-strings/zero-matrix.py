"""
Write an algorithm such that if an element in an M * N matrix is 0, its entire row and column are set to 0.
"""
def setZeroes(matrix):
    row = len(matrix)
    col = len(matrix[0])
    is_col= False
    for i in range(row):
        if matrix[i][0] == 0:
            is_col= True
        for j in range(1,col):
            if matrix[i][j] == 0:
                matrix[0][j] = 0
                matrix[i][0] = 0
                
    for i in range(1,row):
        for j in range(1,col):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0
    if matrix[0][0] == 0:
        for j in range(col):
            matrix[0][j] = 0
    if is_col:
        for i in range(row):
            matrix[i][0] = 0