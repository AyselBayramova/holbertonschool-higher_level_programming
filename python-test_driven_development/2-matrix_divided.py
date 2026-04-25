#!/usr/bin/python3
"""
This module provides a function that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given divisor.

    Args:
        matrix (list of lists): A matrix containing integers or floats.
        div (int/float): The number to divide the matrix by.

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats.
        TypeError: If each row of the matrix does not have the same size.
        TypeError: If div is not a number.
        ZeroDivisionError: If div is 0.

    Returns:
        list: A new matrix with the result of the division.
    """

    # 1. Matrix validation
    msg = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list) or not matrix:
        raise TypeError(msg)
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError(msg)
    if not all(len(row) > 0 for row in matrix):
        raise TypeError(msg)
    
    for row in matrix:
        if not all(isinstance(el, (int, float)) for el in row):
            raise TypeError(msg)

    # 2. Row size validation
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # 3. Divisor validation
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # 4. Zero division check
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # 5. Calculation
    return [[round(el / div, 2) for el in row] for row in matrix]
