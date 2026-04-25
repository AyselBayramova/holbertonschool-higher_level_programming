#!/usr/bin/python3
"""BaseGeometry class module"""

class BaseGeometry:
    """BaseGeometry class with area and integer validator methods"""
    
    def area(self):
        """Raises an exception indicating area() is not implemented"""
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        """
        Validates that value is an integer greater than 0
        
        Args:
            name (str): The name of the value (always a string)
            value: The value to validate
            
        Raises:
            TypeError: If value is not an integer
            ValueError: If value is less than or equal to 0
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
