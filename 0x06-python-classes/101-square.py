#!/usr/bin/python3
""" This class is a Square class"""


class Square:
    """ This is the first method in the class to be run at initialization"""

    def __init__(self, size=0, position=(0, 0)):
        self.__position = position
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

    @property
    def size(self):
        return self.__size

    """This Function sets the"""

    @size.setter
    def size(self, value):
        if isinstance(value, int):
            if value >= 0:
                self.__size = value
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    """this returns the position value"""

    @property
    def position(self):
        return self.__position

    """This sets the position value"""

    @position.setter
    def position(self, value):
        if not (isinstance(value[0], int) or isinstance(value[1], int)):
            raise TypeError("position must be a tuple of 2 positive integers")

        if isinstance(value, tuple):
            if len(value) == 2:
                self.__position = value
            else:
                raise TypeError("position must be a tuple of 2 positive integers")
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    """This Function prints the class"""

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            i = 0
            while i < self.__size:
                j = 0
                while j < self.__position[0]:
                    if self.__position[1] > 0:
                        print("_", end="")
                    else:
                        print(" ", end="")
                    j += 1
                j = 0
                while j < self.size:
                    print("#", end="")
                    j += 1
                print()
                i += 1
