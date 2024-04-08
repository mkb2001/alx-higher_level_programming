#!/usr/bin/python3
""" This class is a Square class"""


class Square:
    """ This is the first method in the class to be run at initialization"""

    def __init__(self, size=0):
        if isinstance(size, int):
            if size >= 0:
                self.__size = size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    """This function calculates the area of a square"""

    def area(self):
        return (self.__size ** 2)

    """This Function gets the size"""

    def size(self):
        return self.__size

    """This Function sets the"""

    def size(self, value):
        if isinstance(value, int):
            if value >= 0:
                self.__size = value
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    """This Function prints the class"""

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for i in range(0, self.__size):
                for j in range(0, self.__size):
                    print('#', end="")
                print()
