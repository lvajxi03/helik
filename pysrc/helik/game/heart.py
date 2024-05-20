#!/usr/bin/env python3

"""
Heart module
"""

from helik.game.objects import ImageListGameObject, GameObjectType


class Heart(ImageListGameObject):
    """
    Heart game object class
    """

    def __init__(self, x: int, y: int, images: list):
        super().__init__(x, y, GameObjectType.HEART, images)


def heart_from_images(images, x, y):
    """
    Create Heart object from images
    :param images: list of heart frames
    :param x: x coordinate
    :param y: y coordinate
    :return Heart object
    """
    return Heart(x, y, images)
