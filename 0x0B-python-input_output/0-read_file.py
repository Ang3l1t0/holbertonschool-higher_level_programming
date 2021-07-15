#!/usr/bin/python3
"""Read File.
"""


def read_file(filename=""):
    """Read File function

    Keyword Arguments:
        filename {str} -- [name of the file] (default: {""})
    """
    with open(filename, encoding="UTF8") as f:
        for line in f:
            print(line, end="")
    f.closed
