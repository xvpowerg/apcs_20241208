def printMatrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end=' ')
        print()
def rotate(matrixA):
    matrixB=[]
    r = len(matrixA)
    c = len(matrixA[0])
    for i in range(c):
        row = []
        for j in range(r-1,-1,-1):
            row.append(matrixA[j][i])
        matrixB.append(row)
    return   matrixB  
m1 = [[3,6],[2,5],[1,4]]
printMatrix(m1)
m2 = rotate(m1)
printMatrix(m2)


