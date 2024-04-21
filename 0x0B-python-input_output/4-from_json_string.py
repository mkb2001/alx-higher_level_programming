#!/usr/bin/python3
"""
JSON representation of an object
"""


def from_json_string(my_str):
    """JSON representation of an object"""
    import json
    return json.loads(my_str)
