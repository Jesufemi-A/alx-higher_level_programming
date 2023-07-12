#!/usr/bin/python3
"""
a script that add arguement to a list
and save to them to a file
"""
from sys import argv


load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file.py').load_from_json_file

try:
    a_list = load_from_json_file('add_item.json')
except Exception:
    a_list = []

for i in range(1, len(argv)):
    a_list.append(argv[i])
save_to_json_file(a_list, 'add_item.json')
