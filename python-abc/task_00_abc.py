#!/usr/bin/python3
"""
Module task_00_abc
"""
from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract class Animal"""

    @abstractmethod
    def sound(self):
        """Abstract method sound"""
        pass


class Dog(Animal):
    """Class Dog"""

    def sound(self):
        """Returns Bark"""
        return "Bark"


class Cat(Animal):
    """Class Cat"""

    def sound(self):
        """Returns Meow"""
        return "Meow"
