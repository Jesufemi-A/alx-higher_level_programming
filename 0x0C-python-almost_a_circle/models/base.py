#!/usr/bin/python3
"""
contain class Base
"""


class Base:
    """
    Base class for other sub classes in this project
    """
    
    __nb_objects = 0

    def __init__(self, id=None):
        """
        initialise the attributes
        """

        if id != None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
