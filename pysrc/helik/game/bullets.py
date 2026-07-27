#!/usr/bin/env python3

"""
Bullets handler module
"""

from helik.hdefs import ARENA_WIDTH
from helik.game.objects import GameObjectType, ImageGameObject


class Bullet(ImageGameObject):
    """
    Bullet handler class
    """
    def __init__(self, image, x, y):
        """
        Create bullet object
        :param image: bullet image
        :param x: x coordinate
        :param y: y coordinate
        """
        super().__init__(x, y, GameObjectType.BULLET, image)
        self.valid = True
        self.visible = True

    def move(self, speed):
        """
        Move bullet
        :param speed: distance to move per frame
        """
        if self.valid:
            self.x += speed
            if self.x > ARENA_WIDTH:
                self.valid = False
                self.visible = False
