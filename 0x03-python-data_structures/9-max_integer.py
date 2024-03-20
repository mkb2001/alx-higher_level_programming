#!/usr/bin/python3
def max_integer(my_list=[]):
    max_integer = 0
    for i in range (len(my_list) - 1):
        if max_integer < my_list[i]:
            max_integer = my_list[i]
    return max_integer