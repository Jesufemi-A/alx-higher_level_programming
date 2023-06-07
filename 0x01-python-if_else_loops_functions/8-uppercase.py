#!/usr/bin/python3
def uppercase(str):
    final = ""
    for alpha in str:
        if ord(alpha) >= ord('a') and ord(alpha) <= ord('z'):
            final += chr(ord(alpha) - 32)
        else:
            final += chr(ord(alpha))
    print(final)
