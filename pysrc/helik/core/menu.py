#!/usr/bin/env pythom3

"""
Menu module
"""


class MenuItem:
    """
    MenuItem
    """
    def __init__(self):
        """
        MenuItem constructor
        """

    def paint(self, canvas):
        """
        Paint menu
        :param canvas: target canvas
        """


class Menu:
    """
    Menu
    """
    def __init__(self):
        """
        Menu constructor
        """
        self.items = []

    def append(self, item):
        """
        Append MenuItem object
        """
        self.items.append(item)

    def paint(self, canvas):
        """
        Paint menu
        :param canvas: target canvas
        """
