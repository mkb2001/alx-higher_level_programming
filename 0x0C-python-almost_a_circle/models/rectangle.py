#!/usr/bin/python3
""" Rectangle Module """

from models.base import Base


class Rectangle(Base):
    """ Rectangle Class """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Constructor """
        if type(width) is int:
            if width > 0:
                self.__width = width
            else:
                raise ValueError('width must be > 0')
        else:
            raise TypeError('width must be an integer')

        if type(height) is int:
            if height > 0:
                self.__height = height
            else:
                raise ValueError('height must be > 0')
        else:
            raise TypeError('height must be an integer')

        if type(x) is int:
            if x >= 0:
                self.__x = x
            else:
                raise ValueError('x must be >= 0')
        else:
            raise TypeError('x must be an integer')

        if type(y) is int:
            if y >= 0:
                self.__y = y
            else:
                raise ValueError('y must be >= 0')
        else:
            raise TypeError('y must be an integer')

        super().__init__(id)

    def area(self):
        """ Returns the area value of the Rectangle instance """
        return self.__width * self.__height

    def __str__(self):
        """ Returns the string representation of the Rectangle instance """
        return '[Rectangle] ({}) {}/{} - {}/{}'.format(self.id, self.__x, self.__y, self.__width, self.__height)

    def display(self):
        """ Prints in stdout the Rectangle instance with the character # """
        for i in range(self.__y):
            print()
        for i in range(self.__height):
            print(' ' * self.__x + '#' * self.__width)

    def update(self, *args, **kwargs):
        """ Assigns an argument to each attribute """
        if args:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[i]
                elif i == 1:
                    self.width = args[i]
                elif i == 2:
                    self.height = args[i]
                elif i == 3:
                    self.x = args[i]
                elif i == 4:
                    self.y = args[i]
        else:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                elif key == 'width':
                    self.width = value
                elif key == 'height':
                    self.height = value
                elif key == 'x':
                    self.x = value
                elif key == 'y':
                    self.y = value

    @property
    def width(self):
        """ Getter """
        return self.__width

    @width.setter
    def width(self, value):
        """ Setter """
        if type(value) is int:
            if value > 0:
                self.__width = value
            else:
                raise ValueError('width must be > 0')
        else:
            raise TypeError('width must be an integer')

    @property
    def height(self):
        """ Getter """
        return self.__height

    @height.setter
    def height(self, value):
        """ Setter """
        if type(value) is int:
            if value > 0:
                self.__height = value
            else:
                raise ValueError('height must be > 0')
        else:
            raise TypeError('height must be an integer')

    @property
    def x(self):
        """ Getter """
        return self.__x

    @x.setter
    def x(self, value):
        """ Setter """
        if type(value) is int:
            if value >= 0:
                self.__x = value
            else:
                raise ValueError('x must be >= 0')
        else:
            raise TypeError('x must be an integer')

    @property
    def y(self):
        """ Getter """
        return self.__y

    @y.setter
    def y(self, value):
        """ Setter """
        if type(value) is int:
            if value >= 0:
                self.__y = value
            else:
                raise ValueError('y must be >= 0')
        else:
            raise TypeError('y must be an integer')

    def to_dictionary(self):
        """ Returns the dictionary representation of a Rectangle """
        return {'id': self.id, 'width': self.width, 'height': self.height, 'x': self.x, 'y': self.y}
