#!/usr/bin/python
def new_in_list(my_list, idx, element):
    if my_list is not None:
        if idx < 0 or idx > len(my_list):
            list_copy = my_list
            return list_copy
        else:
            list_copy = my_list
            list_copy = list_copy[:idx] + list_copy[idx + 1:]
            list_copy.insert(idx, element)
            return list_copy
