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
        self.arena = parent
        self.res_man = self.arena.res_man
        self.buffer = self.res_man.surfaces["buffer"]
        self.images = self.res_man.images

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

    def on_mouseup(self, button, pos):
        """
        Mouse up event handler
        :param button: button number
        :param pos: cursor position
        """

    def on_paint(self):
        """
        Paint handler
        """

    def on_timer(self, timer):
        """
        Timer handler
        """

    def on_update(self, delta):
        """
        Update event handler
        :param delta: delta time from last frame
        """
