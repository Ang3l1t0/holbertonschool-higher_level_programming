#!/usr/bin/python3
"""create a Object from json
"""
import json


def load_from_json_file(filename):
    """load_from_json_file method

    Arguments:
        filename  -- filename or path
    """
    with open(filename) as f:
        out = json.load(f)
    f.closed
    return (out)
