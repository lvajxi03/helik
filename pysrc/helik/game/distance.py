#!/usr/bin/env python3

"""
Distance handler class
"""

from helik.game.objects import GameObjectType, GameObject


class Distance(GameObject):
    """
    Empty distance flying object.
    Useful when you need fake object between two real ones.
    """
    def __init__(self, x, w):
        super().__init__(x, 0)
        self.w = w

    def move(self, speed=1):
        """
        Move object according to its policy
        """
        self.x -= speed
        if self.x + self.w < 0:
            self.valid = False
