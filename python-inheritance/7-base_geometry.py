#!/usr/bin/python3
"""
Module 5-base_geometry
Defines a class BaseGeometry
"""


class BaseGeometry:
    """Class BaseGeometry"""

    def area(self):
        """Method that raises an Exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates value as an integer greater than 0.

        Args:
            name (str): The name of the value (always a string).
            value (int): The value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
