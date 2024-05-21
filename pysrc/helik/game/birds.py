#!/usr/bin/env python3

"""
Birds handler module
"""

from helik.game.objects import ImageListGameObject, GameObjectType


class Bird(ImageListGameObject):
    """
    Bird handler class
    """
    def __init__(self, x, y, images: list, frame=0):
        """
        Bird class constructor
        :param x: x coordinate
        :param y: y coordinate
        :param images: bird's images
        """
        super().__init__(x, y, GameObjectType.BIRD, images)
        self.current = frame
        self.current %= len(self.images)


def bird_from_images(images, x, y, frame=0):
    """
    Create Bird object from imagelist
    :param images: bird image list
    :param x: x coordinate
    :param y: y coordinate
    :param frame: current frame
    """
    return Bird(x, y, images, frame)