#!/usr/bin/python3
for num in range(ord('z'), ord('a') - 1, -1):
    if num % 2 == 0:
        result = chr(num)
    elif num % 2 != 0:
        result = chr(num - 32)
    print("{}".format(result), end="")
