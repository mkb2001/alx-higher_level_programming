#!/usr/bin/python3
def raise_exception():
    try:
        raise Exception("Exception has been raised")
    except Exception as e:
        raise e
