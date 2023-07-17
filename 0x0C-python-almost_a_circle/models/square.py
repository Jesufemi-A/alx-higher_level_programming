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
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

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

    def update(self, *args, **kwargs):
        """
        method to update attributes
        """
        if args is not None or len(args) != 0
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        return dictionary representation of class Square
        """
        return {
                "id": self.id,
                "size": self.size,
                "x": self.x,
                "y": self.y
                }
