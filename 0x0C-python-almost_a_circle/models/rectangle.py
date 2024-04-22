#!/usr/bin/python3
""" Rectangle Module """

from models.base import Base


class Rectangle(Base):
    """ Rectangle Class """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Constructor """
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """ Getter """
        return self.__width

    @width.setter
    def width(self, value):
        """ Setter """
        self.__width = value

    @property
    def height(self):
        """ Getter """
        return self.__height

    @height.setter
    def height(self, value):
        """ Setter """
        self.__height = value

    @property
    def x(self):
        """ Getter """
        return self.__x

    @x.setter
    def x(self, value):
        """ Setter """
        self.__x = value

    @property
    def y(self):
        """ Getter """
        return self.__y

    @y.setter
    def y(self, value):
        """ Setter """
        self.__y = value
