#!/usr/bin/python3
"""
Contains function that reads text file
"""


def read_file(filename=""):
    """
    read text file and print to
    stdout
    """

    with open(filename, "r", encoding="utf-8") as file_a:
        file_content = file_a.read()
        return file_content
