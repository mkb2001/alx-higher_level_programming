#!/usr/bin/python3
""" Base Module """


class Base:
    """ Base Class """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Constructor """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """ Returns the JSON string representation of list_dictionaries """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return '[]'
        return str(list_dictionaries)

    def save_to_file(cls, list_objs):
        """ Writes the JSON string representation of list_objs to a file """
        filename = cls.__name__ + '.json'
        with open(filename, 'w') as file:
            if list_objs is None:
                file.write('[]')
            else:
                list_dicts = [obj.to_dictionary() for obj in list_objs]
                file.write(cls.to_json_string(list_dicts))

    def from_json_string(json_string):
        """ Returns the list of the JSON string representation json_string """
        if json_string is None or len(json_string) == 0:
            return []
        return eval(json_string)

    def create(cls, **dictionary):
        """ Returns an instance with all attributes already set """
        if cls.__name__ == 'Rectangle':
            new = cls(1, 1)
        elif cls.__name__ == 'Square':
            new = cls(1)
        new.update(**dictionary)
        return new

    def load_from_file(cls):
        """ Returns a list of instances """
        filename = cls.__name__ + '.json'
        try:
            with open(filename, 'r') as file:
                list_dicts = cls.from_json_string(file.read())
                return [cls.create(**dict) for dict in list_dicts]
        except FileNotFoundError:
            return []

    def save_to_file_csv(cls, list_objs):
        """ Writes the CSV string representation of list_objs to a file """
        filename = cls.__name__ + '.csv'
        with open(filename, 'w') as file:
            if list_objs is None:
                file.write('')
            else:
                for obj in list_objs:
                    file.write(obj.to_csv())
                    file.write('\n')

    def draw(list_rectangles, list_squares):
        """
        Update the class Base by adding the static method def draw(list_rectangles, list_squares): that opens a window and draws all the Rectangles and Squares:

        You must use the Turtle graphics module
        To install it: sudo apt-get install python3-tk
        To make the GUI available outside your vagrant machine, add this line in your Vagrantfile: config.ssh.forward_x11 = true
        No constraints for color, shape etc… be creative!
        :param list_squares:
        :return:
        """
