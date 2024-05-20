#!/usr/bin/env python3

"""
DirChanger handler module
"""

import math
import pygame
from helik.hdefs import ARENA_WIDTH
from helik.game.objects import GameObjectType, ImageListGameObject


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
