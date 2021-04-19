#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    # the name of the function is the first arg, so it needs to be -1 to get 0
    if len(argv) == 1:
        print("{:d} arguments.".format(len(argv) - 1))
    # if function length counts 2 arguments really we have the function name and 1st arg.
    elif len(argv) == 2:
        print("{:d} argument:".format(len(argv) - 1))
    else:
        print("{:d} arguments:".format(len(argv) - 1))
    # using for loop we are goig to get the number of argumnets and print the desired output
    for i in range(1, len(argv)):
        print("{:d}: {:s}".format(i, argv[i]))
