def printMatrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j],end=" ")
        print()

def matrixMutiply(A,B):
    m = len(A)#row
    na = len(A[0])#colum
    nb = len(B)#row
    p =  len(B[0])#colum
    if na != nb:
        print("Error")
        return
    C = [[None] * p for row in range(m)]
    for i in range(m):
        for j in range(p):
            tmp = 0
            for k in range(na):
                tmp += A[i][k] * B[k][j]
            C[i][j] = tmp
    return C
matrixA = [[6,3,5], [8,9,7]]
matrixB = [[5,10], [14,7], [6,8]]
matrixC = matrixMutiply(matrixA,matrixB)
printMatrix(matrixC)

