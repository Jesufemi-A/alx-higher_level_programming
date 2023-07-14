#!/usr/bin/python3
"""
contain class Base
"""


class Base:
    """
    Base class for other classes in this project
    """
    
    __nb_object == 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            __nb_object += 1
            id = __nb_object
