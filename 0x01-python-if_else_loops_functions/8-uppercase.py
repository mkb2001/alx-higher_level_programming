#!/usr/bin/python3
def uppercase(str_u):
    strlen = len(str_u)
    i = 0
    while i < strlen:
        char = ord(str_u[i])
        if char < 97 or char > 122:
            print("{}".format(chr(char)), end="" if i < strlen - 1 else "\n")
        elif 97 <= char <= 122:
            char = char - 32
            print("{}".format(chr(char)), end="" if i < strlen - 1 else "\n")
        i += 1
