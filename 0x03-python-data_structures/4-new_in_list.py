#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if my_list is not None:
        if idx < 0 or idx > len(my_list):
            list_copy = my_list
            return list_copy
        else:
            my_list = my_list[:idx] + my_list[idx + 1:]
            my_list.insert(idx, element)
            return my_list
