#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    high_key = None
    high_value = float('-inf')
    for k, val in a_dictionary.items():
        if val > high_value:
            high_key = k
            high_value = val
    return high_key
