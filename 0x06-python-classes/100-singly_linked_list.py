#!/usr/bin/python3

"""Module to define a Class Node"""


class Node:
    """Class to define a Node"""

    def __init__(self, data, next_node=None):
        if isinstance(data, int):
            self.__data = data
        else:
            raise TypeError("data must be an integer")

        if next_node is None or isinstance(next_node, Node):
            self.__next_node = next_node
        else:
            raise TypeError("next_node must be a Node object")

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if not (isinstance(value, int)):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        return self.__data

    @next_node.setter
    def next_node(self, value):
        if not (isinstance(value, Node) or value is None):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """" Class to define a linked list and insert a Node"""

    def __init__(self):
        self.__head = None

    def __str__(self):
        current = self.__head
        nodes = []
        while current:
            nodes.append(current)
            current = current.next_node
        if nodes:
            return "\n".join(nodes)
        else:
            return ""

    def sorted_insert(self, value):
        new_node = Node(value)

        if self.__head is None:
            self.__head = new_node
            return

        if value < self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
            return

        current = self.__head
        while current.next_node is not None and value > current.next_node.value.data:
            current = current.next_node

        new_node.next_node = current.next_node
        current.next_node = new_node
