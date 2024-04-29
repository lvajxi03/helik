#!/usr/bin/env python3

"""
Ammo handler module
"""

from helik.game.objects import GameObjectType, ImageListGameObject


class Ammo(ImageListGameObject):
    """
    Ammo handler class
    """
    def __init__(self, x, y, images: list):
        super().__init__(x, y, GameObjectType.AMMO, images)
