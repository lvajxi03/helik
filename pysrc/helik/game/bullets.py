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
    def __init__(self, x, y, image):
        super().__init__(x, y, GameObjectType.BULLET, image)

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
