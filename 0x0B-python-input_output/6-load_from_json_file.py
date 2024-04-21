#!/usr/bin/python3
"""
Create an object from a JSON file
"""


def load_from_json_file(filename):
    """Create an object from a JSON file"""
    import json
    with open(filename, 'r') as f:
        return json.load(f)
