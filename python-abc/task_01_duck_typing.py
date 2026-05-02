#!/usr/bin/python3
"""
Module task_01_duck_typing: Defines Shape, Circle, Rectangle, and shape_info.
"""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract class representing a geometric shape."""

    @abstractmethod
    def area(self):
        """Calculates area."""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculates perimeter."""
        pass


class Circle(Shape):
    """Class representing a Circle."""

    def __init__(self, radius):
        """Initializes with radius."""
        self.radius = radius

    def area(self):
        """Returns area of the circle."""
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """Returns perimeter of the circle."""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Class representing a Rectangle."""

    def __init__(self, width, height):
        """Initializes with width and height."""
        self.width = width
        self.height = height

    def area(self):
        """Returns area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Returns perimeter of the rectangle."""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Prints area and perimeter using Duck Typing.
    """
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
