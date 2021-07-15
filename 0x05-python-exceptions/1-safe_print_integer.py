#!/usr/bin/python3
def safe_print_integer(value):
    b = True
    try:
        print("{:d}".format(value))
    except:
        b = False
    return (b)
