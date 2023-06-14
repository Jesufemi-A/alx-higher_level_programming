#!/usr/bin/python3
def uniq_add(my_list=[]):
    new = []
    for num in my_list:
        if num not in new:
            new.append(num)
    sum = 0
    for num in new:
        sum += num
    return sum
