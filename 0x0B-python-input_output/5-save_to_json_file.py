#!/usr/bin/python3
"""
JSON representation of an object
"""


def save_to_json_file(my_obj, filename):
    """JSON representation of an object"""
    import json
    with open(filename, 'w') as f:
        f.write(json.dumps(my_obj))
