#!/usr/bin/python3
"""text_indentation"""


def text_indentation(text):
    """text_indentation

    Arguments:
        text {str} -- text that will be indent

    Raises:
        TypeError: text must be a string
    """
    ch = [".", "?", ":"]
    if type(text) is not str:
        raise TypeError("text must be a string")
    else:
        for element in range(len(text)):
            if text[element] is not " ":
                print(text[element], end="")
            if text[element] in ch:
                print("\n")
