#!/usr/bin/python3
import sys

def print_arguments(argv):
    num_arguments = len(argv)
    if num_arguments == 0:
        print("0 argument(s).")
        print(".")
        return

    if num_arguments == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(num_arguments))

    for i, arg in enumerate(argv, 1):
        print("{}: {}".format(i, arg))

if __name__ == "__main__":
    print_arguments(sys.argv[1:])
