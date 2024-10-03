#!/usr/bin/python3

# Pascals Triangle using Python

def pascal_triangle(n):

    """
    Calculate pascals triangle
    """
    if n <= 0:
        return []

    triangle = [[1], [1, 1]]
    for i in range(2, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)
    return triangle
