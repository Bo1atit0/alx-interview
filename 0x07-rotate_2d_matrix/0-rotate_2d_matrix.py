def rotate_2d_matrix(matrix):
    """
    Rotates a given n x n 2D matrix 90 degrees clockwise in-place.

    Args:
        matrix (list of list of int): The n x n 2D matrix to rotate.
    """
    # Step 1: Transpose the matrix
    n = len(matrix)
    for i in range(n):
        # Only traverse upper triangle(above diagonal)
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Step 2: Reverse each row
    for row in matrix:
        row.reverse()
