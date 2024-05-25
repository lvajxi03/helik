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


def ammo_from_images(images: list, x, y):
    """
    Create Ammo object from a list of images
    :param images: list of ammo frames
    :param x: x coordinate
    :param y: y coordinate
    :return Ammo object"
    """
    return Ammo(x, y, images)
