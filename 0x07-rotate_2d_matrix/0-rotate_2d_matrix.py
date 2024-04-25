#!/usr/bin/python3
"""
Rotate 2D Matrix
"""


def rotate_2d_matrix(matrix):
    """
    Rotate a 2D matrix 90 degrees clockwise.
    
    Args:
        matrix (list of list): The input 2D matrix.
        
    Returns:
        None. The matrix is modified in-place.
    """
    n = len(matrix)
    for layer in range(n // 2):
        first = layer
        last = n - 1 - layer
        for i in range(first, last):
            # Save top
            top = matrix[first][i]
            # Move left to top
            matrix[first][i] = matrix[-i - 1][first]
            # Move bottom to left
            matrix[-i - 1][first] = matrix[-first - 1][-i - 1]
            # Move right to bottom
            matrix[-first - 1][-i - 1] = matrix[i][-first - 1]
            # Move top to right
            matrix[i][-first - 1] = top
