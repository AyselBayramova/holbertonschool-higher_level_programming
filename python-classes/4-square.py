#!/usr/bin/python3
"""Module that defines a Square class with getter and setter."""

class Square:
    """This class represents a square."""

    def __init__(self, size=0):
        """This sets the size of the square.

        Args:
            size (int): The size of the square.
        """
        self.size = size

    @property
    def size(self):
        """This method gets the size.

        Returns:
            int: The size of the square.
        """

        return self.__size

    @size.setter
    def size(self, value):
        """This method sets the size with checks.

        Args:
            value (int): The new size.
        """

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """This method returns the area of the square."""
        return self.__size * self.__size
