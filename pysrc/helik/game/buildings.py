#!/usr/bin/env python3

"""
Buildings module
"""

from helik.game.objects import ImageGameObject, GameObjectType
from helik.hdefs import ARENA_HEIGHT


class Building(ImageGameObject):
    """
    Building handler class
    """
    def __init__(self, x, y, image):
        super().__init__(x, y, GameObjectType.BUILDING, image)


def building_from_image(image, x, y=-1):
    """
    Create a building via its image
    :param image: building image
    :param x: x coordinate
    :param y: y coordinate, if < 0 then aligned to bottom edge
    :return: Building object
    """
    _, h = image.get_size()
    if y < 0:
        y = ARENA_HEIGHT - h - 60
    return Building(x, y, image)
