#!/usr/bin/python3
"""json to python
"""
import json


def from_json_string(my_str):
    """from_json_string method
    Arguments:
        my_str {str}
    """
    return json.loads(my_str)
