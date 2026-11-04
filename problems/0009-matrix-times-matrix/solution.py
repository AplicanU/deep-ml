def matrixmul(a:list[list[int|float]], b:list[list[int|float]])-> list[list[int|float]]:
    
    if (len(a) == 0 or len(b) == 0):
        return []

    a_col = len(a[0])
    b_row = len(b)
    if a_col != b_row:
        return -1
    
    # manual implementation
    '''
    
    c = [[0 for _ in range(len(b[0]))] for _ in range(len(a))]

    for i in range(len(a)):
        for j in range(len(b[0])):
            add = 0
            for k in range(len(a[0])):
                prod = a[i][k] * b[k][j]
                add += prod
            c[i][j] = add

    return c
    '''

    # Numpy implementation
    import numpy as np

    A = np.array(a)
    B = np.array(b)

    C = np.matmul(A, B) # C = A @ B 

    return C