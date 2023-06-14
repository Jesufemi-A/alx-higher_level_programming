#!/usr/bin/python3
def uniq_add(my_list=[]):
    new = []
    for num in my_list:
        if new not in new:
            new.append(num)
    for num in new:
        sum = 0
        sum += num
    return sum
