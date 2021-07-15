#!/usr/bin/python3
"""Append
"""


def append_write(filename="", text=""):
    """append_write method

    Keyword Arguments:
        filename {str} -- file name or path (default: {""})
        text {str} -- text to append (default: {""})

    Returns:
        [str] -- text that will append
    """
    with open(filename, 'a', encoding="UTF8") as f:
        out = f.write(text)
    f.closed
    return (out)
