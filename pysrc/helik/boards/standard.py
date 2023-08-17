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
        self.screen = parent.screen

    def activate(self):
        """
        Board activator
        """

    def deactivate(self):
        """
        Board deactivator
        """

    def on_keydown(self, key):
        """
        Keydown handler
        """

    def on_paint(self):
        """
        Paint handler
        """


class BoardAbout(Board):
    """
    About board
    """

