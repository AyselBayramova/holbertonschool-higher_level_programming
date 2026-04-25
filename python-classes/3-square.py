#!/usr/bin/python3
"""This module is for a Square class with area."""

class Square:
    """This class is a square."""
    def __init__(self, size=0):
        """This sets the size of the square.

        Args:
            size (int): The side of the square.
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    
    def area(self):
        """This returns the area of the square."""

        return self.__size * self.__size
