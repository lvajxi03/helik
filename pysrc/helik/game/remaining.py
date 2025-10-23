#!/usr/bin/env python3

"""
Remaining Game Object
--
Special game object used for testing and level design.
Displayed as an elephant
"""

from helik.game.objects import ImageGameObject, GameObjectType
from helik.hdefs import ARENA_HEIGHT


class RemainingObject(ImageGameObject):
    """
    Remaining Object main class
    """
    def __init__(self, x, y, image):
        """
        Class constructor
        :param x: x coordinate of bottom left corner
        :param y: y coordinate of bottom left corner
        :param image: object image
        """
        super().__init__(x, y, GameObjectType.REMAINING, image)


def remaining_from_image(image, x, y=-1):
    """
    Create remaining object from image
    :param x: x coordinate of bottom left corner
    :param y: y coordinate of bottom left corner (will be recalculated if less than 0)
    :param image: object image
    """
    _, h = image.get_size()
    if y < 0:
        y = ARENA_HEIGHT - h - 60
    return RemainingObject(x, y, image)
