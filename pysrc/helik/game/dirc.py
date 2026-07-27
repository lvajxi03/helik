#!/usr/bin/env python3

"""
DirChanger handler module
"""

import enum
from .objects import GameObjectType, ImageListGameObject


@enum.unique
class DirCType(enum.IntEnum):
    """
    DirCType enum
    Tells you what's the copter direction right now.
    """
    DOWN = 0
    UP = 1


class DirChanger(ImageListGameObject):
    """
    DirChanger handler class
    """
    def __init__(self, x: int, y: int, images: list):
        """
        DirChanger instance constructor
        :param x: x coordinate
        :param y: y coordinate
        :param images: images of dirchanger animation
        """
        super().__init__(x, y, GameObjectType.DIRC, images)


def dirc_from_images(images: list, x, y):
    """
    Create DirChanger object from a list of images
    :param images: list of images with DirChanger drawn there
    :param x: x coordinate of upper left corner
    :param y: y coordinate of upper left corner
    :return: DirChanger object
    """
    return DirChanger(x, y, images)
