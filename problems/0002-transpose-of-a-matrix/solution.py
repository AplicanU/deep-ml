def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    """
    Transpose a 2D matrix by swapping rows and columns.
    
    Args:
        a: A 2D matrix of shape (m, n)
    
    Returns:
        The transposed matrix of shape (n, m)
    """
    # Your code here
    row = len(a)
    
    if row == 0:
        return -1

    col = len(a[0])


    b = [[0 for _ in range(row)] for _ in range(col)]

    for n in range(row):
        for m in range(col):
            b[m][n] = a[n][m]
    
    return b
