#!/usr/bin/python3
import sys


def print_arguments(argv):
    arguments = len(argv)
    if arguments == 0:
        print("0 argument(s).")
        print(".")
        return

    if arguments == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(arguments))

    for i, arg in enumerate(argv, 1):
        print("{}: {}".format(i, arg))


if __name__ == "__main__":
    print_arguments(sys.argv[1:])
