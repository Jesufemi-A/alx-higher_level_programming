#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arguments = sys.argv[1:]
    arg_num = len(arguments)
    if arg_num == 0:
        print("0 arguments.")
    elif arg_num == 1:
        print("1 arguments:")
    else:
        print("{} arguments:".format(arguments))
        for num, argument in enumerate(arguments):
            print("{}: {}".format(num + 1, argument))
