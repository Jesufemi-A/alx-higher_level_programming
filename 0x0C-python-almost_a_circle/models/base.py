#!/usr/bin/python3
"""
contain class Base
"""
import json
import os


class Base:
    """
    Base class for other sub classes in this project
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        initialise the attributes
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        return the JSON representation of
        list_dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        json_rep = json.dumps(list_dictionaries)
        return json_rep

    @classmethod
    def save_to_file(cls, list_objs):
        """
        writes the JSON string representation
        of list_objs to a file
        """
        filename = "{}.json".format(cls.__name__)
        with open(filename, "w", encoding="utf-8") as file_w:
            list_dict = []
            if list_objs is None or len(list_objs) == 0:
                file_w.write("[]")
            else:
                for i in list_objs:
                    a = i.to_dictionary()
                    list_dict.append(a)
                file_w.write(Base.to_json_string(list_dict))

    @staticmethod
    def from_json_string(json_string):
        """
        returns the list of the JSON string representation json_string
        """
        if json_string is None or len(json_string) == 0:
            return []
        json_to_dict = json.loads(json_string)
        return json_to_dict

    @classmethod
    def create(cls, **dictionary):
        """
        returns an instance with all attributes already set
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 2, 3, 4)
        elif cls.__name__ == "Square":
            dummy = cls(1, 1)
        else:
            dummy = None

        if dummy is not None:
            dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        load json from file
        """
        filename = "{}.json".format(cls.__name__)
        if not os.path.exists(filename):
            return []
        with open(filename, 'r') as file:
            json_data = file.read()
            list_dicts = cls.from_json_string(json_data)
            instances = [cls.create(**data) for data in list_dicts]
            return instances
