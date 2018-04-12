import numpy as np

a = np.array([[0,1,2,6], [3,2,3,6], [3,1,5,7], [9,2,4,6]])
b = np.array([[2,4,1,7], [3,7,3,7], [9,6,5,6]])
#
# array([[21, 19, 13],
#        [39, 44, 24],
#        [54, 49, 31]])

def matrix_multiply_basic(A,B):
    # let write a normal algo
    n = len(A)   # n = A.rows
    c = np.zeros([n,n])  # let c be a new n by n array
    for i in range(0, n):
        for j in range(0,n):
            c[i][j] = 0
            for k in range(0,n):
                c[i][j] = c[i][j] + (A[i][k] * B[k][j] )
    return c

def matrix_multiply_recursive(A, B):

    n = len(A)

    c = np.zeros([n, n])
    if n == 1:
        c[1][1] = A[1][1] * B[1][1]
    else:
        A_1_1 = 
        c[1][1] = matrix_multiply_recursive(A[1][1], B[1][1]) + matrix_multiply_recursive(A[1][2], B[2][1])
        c[1][2] = matrix_multiply_recursive(A[1][1], B[1][2]) + matrix_multiply_recursive(A[1][2], B[2][2])
        c[2][1] = matrix_multiply_recursive(A[2][1], B[1][1]) + matrix_multiply_recursive(A[2][2], B[2][1])
        c[2][2] = matrix_multiply_recursive(A[2][1], B[1][2]) + matrix_multiply_recursive(A[2][2], B[2][2])

    return c


ans = matrix_multiply_recursive(a, b)