#!/usr/bin/python3
import sys
from sys import argv
if __name__ == "__main__":
    # leng argv starts in 1 with the name of the function
    # 1 = function name
    if len(argv) == 1:
        print("{:d} arguments.".format(len(sys.argv) - 1))
    # 2 = first argument if is equal to 2 it means just one arg
    elif len(argv) == 2:
        print("{:d} argument:".format(len(sys.argv) - 1))
    else:
        print("{:d} arguments:".format(len(sys.argv) - 1))
    # range start in 1 because range start counting at 0
    for i in range(1, len(argv)):
        print("{:d}: {:s}".format(i, argv[i]))
