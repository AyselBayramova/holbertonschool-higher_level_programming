#!/usr/bin/python3
"""
This module provides a function to divide all elements of a matrix.
It handles error checking for types, sizes, and division by zero.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given divisor.

    Args:
        matrix (list of lists): Matrix containing integers or floats.
        div (int, float): The number to divide the matrix elements by.

    Returns:
        list of lists: A new matrix with the results rounded to 2 decimal places.

    Raises:
        TypeError: If matrix is not a list of lists of numbers,
                   or if rows have different sizes, or if div is not a number.
        ZeroDivisionError: If div is 0.
    """
    msg = "matrix must be a matrix (list of lists) of integers/floats"

    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(msg)

    row_size = None
    for row in matrix:
    
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError(msg)
        
    
        if row_size is None:
            row_size = len(row)
        elif len(row) != row_size:
            raise TypeError("Each row of the matrix must have the same size")

        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError(msg)

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(x / div, 2) for x in row] for row in matrix]
