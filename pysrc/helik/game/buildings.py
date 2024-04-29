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


def building_from_image(x, image):
    """
    Create a building via its image
    :param x: x coordinate
    :param image: building image
    """
    w, h = image.get_size()
    y = ARENA_HEIGHT - h
    return Building(x, y, image)
