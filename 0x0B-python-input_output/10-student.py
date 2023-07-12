#!/usr/bin/python3
"""
module contain class student
"""


class Student:
    """
    class Student
    """

    def __init__(self, first_name, last_name, age):
        """
        constructor
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        convert json
        """

        if attrs is None or not isinstance(attrs, list):
            return self.__dict__

        result = {}
        for attr in attrs:
            if hasattr(self, attr):
                value = getattr(self, attr)
                if isinstance(value, (list, dict, str, int, bool)):
                    result[attr] = value
        return result
