#!/usr/bin/python3
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
"""
Add all arguments to a Python list, and then save them to a file
"""


def add_item(args):
    """Add all arguments to a Python list, and then save them to a file"""
    try:
        my_list = load_from_json_file("add_item.json")
    except (FileNotFoundError, ValueError):
        my_list = []
    my_list.extend(args)
    save_to_json_file(my_list, "add_item.json")
