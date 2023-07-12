#!/usr/bin/python3
"""
contains the function
load_from_json_file(filename)
"""
import json


def load_from_json_file(filename):
    """
    create an object from a JSON file
    """

    with open(filename, "r", encoding="utf-8") as file_o:
        json_file_read = file_o.read()
        file_obj_rep = json.loads(json_file_read)
        return file_obj_rep
