#!/usr/bin/env python3

"""
Cloud handler module
"""

from helik.game.objects import ImageGameObject, GameObjectType


class Cloud(ImageGameObject):
    """
    Cloud handler class
    """
    def __init__(self, x, y, image):
        super().__init__(x, y, GameObjectType.CLOUD, image)

def cloud_from_image(x, y, image):
    """
    Create a cloud object from an image
    :param x: x coordinate of upper left corner
    :param y: y coordinate of upper left corner
    :param image: image of the cloud
    :return: Cloud object
    """
    return Cloud(x, y, image)
