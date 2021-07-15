#!/usr/bin/python3
"""Number of Lines
"""


def number_of_lines(filename=""):
    """number_of_lines

    Keyword Arguments:
        filename {str} -- file name or path (default: {""})
    """
    count = 0
    with open(filename) as f:
        for _ in f:
            count += 1
    f.closed
    return(count)
