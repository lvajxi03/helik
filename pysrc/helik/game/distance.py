#!/usr/bin/env python3

"""
Distance handler class
"""


class Distance:
    """
    Empty distance flying object.
    Useful when you need fake object between two real ones.
    """
    def __init__(self, x, w):
        self.x = x
        self.w = w
        self.valid = True
        self.visible = False

    def move(self, speed=1):
        """
        Move object according to its policy
        """
        self.x -= speed
        if self.x + self.w < 0:
            self.valid = False

    def on_paint(self, canvas):
        """
        No paint
        """
        pass

    def collide(self, other):
        """
        No collision
        """
        return None
