#!/usr/bin/python3
"""Write file
"""


def write_file(filename="", text=""):
    """Write file function

    Keyword Arguments:
        filename {str} -- file name or path (default: {""})
        text {str} -- text to be added (default: {""})

    Returns:
        [type] -- [description]
    """
    with open(filename, 'w', encoding="UTF8") as f:
        out = f.write(text)
    f.closed
    return (out)
