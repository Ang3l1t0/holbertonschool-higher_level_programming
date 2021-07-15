#!/usr/bin/python3
"""Json
"""
import json


def to_json_string(my_obj):
    """to_json_string method
    Arguments:
        my_obj {object} -- object to encode
    Returns:
        [type] -- [description]
    """
    return json.dumps(my_obj)
