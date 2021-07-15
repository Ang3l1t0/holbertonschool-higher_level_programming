#!/usr/bin/python3
"""Read lines
"""


def read_lines(filename="", nb_lines=0):
    """Read lines function

    Keyword Arguments:
        filename {str} -- file name or path (default: {""})
        nb_lines {int} -- number of lines (default: {0})
    """
    count = 0
    with open(filename, 'r', encoding="UTF8") as f:
        for _ in open(filename):
            count += 1
        if nb_lines <= 0 or nb_lines >= count:
            print(f.read(), end="")
        else:
            for _ in range(nb_lines):
                print(f.readline(), end="")
    f.closed
