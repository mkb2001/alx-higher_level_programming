#!/usr/bin/python3
def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except ValueError as e:
        print("Exception: Unknown format code 'd' for object of type 'str' School is not an integer")
        return False
