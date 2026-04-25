#!/usr/bin/python3
"""Module for a singly linked list."""


class Node:
    """Defines a node of a singly linked list."""

    def __init__(self, data, next_node=None):
        """Initialize the node."""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Get data."""
        return self.__data

    @data.setter
    def data(self, value):
        """Set data."""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Get next_node."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Set next_node."""
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Defines a singly linked list."""

    def __init__(self):
        """Initialize the list."""
        self.__head = None

    def __str__(self):
        """Print the entire list, one node per line."""
        values = []
        tmp = self.__head
        while tmp is not None:
            values.append(str(tmp.data))
            tmp = tmp.next_node
        return "\n".join(values)

    def sorted_insert(self, value):
        """Insert a new Node into the correct sorted position."""
        new_node = Node(value)
        if self.__head is None or self.__head.data >= value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            tmp = self.__head
            while tmp.next_node is not None and tmp.next_node.data < value:
                tmp = tmp.next_node
            new_node.next_node = tmp.next_node
            tmp.next_node = new_node
