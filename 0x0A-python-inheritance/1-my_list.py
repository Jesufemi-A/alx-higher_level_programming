#!/usr/bin/python3
"""
Module contains class MyList
"""


class MyList(list):
    """
    a subclass of superclass list
    """

    def __init__(self):
        super().__init__(self)

    def print_sorted(self):
        new_list = sorted(self)
        print(new_list)
