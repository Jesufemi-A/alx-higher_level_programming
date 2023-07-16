#!/usr/bin/python3
"""
contains the class Square
"""
from models.rectangle import Rectangle

class Square(Rectangle):
    """
    defines class Square, inherits from class Rectangle
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        initialises the attributes
        """
        super().__init__(size, size, x, y, id)


    def __str__(self):
        """
        return a string representation
        """
        return "[square] (" + str(self.id) + ") " + str(self.x) + "/" + str(self.y) + " - " + str(self.width)

    @property
    def size(self):
        """
        getter to return size
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        setter to access and modify size
        """
        if type(value) != int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.width = value
        self.width = value
