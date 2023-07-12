#!/usr/bin/python3
"""
contain save_to_json_file function
"""
import json


def save_to_json_file(my_obj, filename):
    """
    write an obj to a text file
    using JSON representation
    """

    json_rep = json.dumps(my_obj)
    with open(filename, 'w', encoding='utf-8') as file_w:
        num_chars_written = file_w.write(json_rep)
