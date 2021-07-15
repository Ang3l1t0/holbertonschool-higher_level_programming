#!/usr/bin/python3
"""save to object
"""
import json


def save_to_json_file(my_obj, filename):
    """save_to_json_file - method

    Arguments:
        my_obj {object} -- object to save
        filename {} -- filename or path
    """
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
    f.closed
