#!/usr/bin/env python3

"""
Standard boards for Helik
"""

class Board():
    """
    Generic board class for Helik
    """
    def __init__(self, parent):
        """
        Class constructor
        """
        self.parent = parent
        self.res_man = self.parent.res_man

    def activate(self):
        """
        Board activator
        """

    def deactivate(self):
        """
        Board deactivator
        """

    def on_keyup(self, key):
        """
        Key release handler
        :param key: key code
        """

    def on_paint(self):
        """
        Paint handler
        """

    def on_timer(self, timer):
        """
        Timer handler
        """


class BoardAbout(Board):
    """
    About board
    """
