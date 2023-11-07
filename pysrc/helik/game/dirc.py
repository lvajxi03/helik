#!/usr/bin/env python3

"""
DirChanger handler module
"""

import math
import pygame
from helik.hdefs import ARENA_WIDTH
from helik.htypes import DirCType


class DirChanger:
    """
    DirChanger handler class
    """
    def __init__(self, images: list, x: int, y: int):
        """
        DirChanger instance constructor
        :param images: images of dirchanger animation
        :param x: x coordinate
        :param y: y coordinate
        """
        self.images = images
        self.x = x
        self.y = y
        self.base_y = y
        self.rects = []
        self.masks = []
        for image in self.images:
            r = image.get_rect()
            self.rects.append(r)
            m = pygame.mask.from_surface(image)
            self.masks.append(m)

        self.w = self.rects[0].w
        self.h = self.rects[0].h
        if self.x > ARENA_WIDTH:
            self.visible = False
        else:
            self.visible = True
        self.current = 0
        self.valid = True

    def next(self):
        """
        Switch to a next frame
        """
        self.current += 1
        self.current %= len(self.images)

    def move(self, speed=1):
        """
        Move dir-changer according to its policy
        """
        self.x -= speed
        if self.x + self.w < 0:
            self.valid = False
            self.visible = False
        elif self.x < ARENA_WIDTH:
            self.visible = True
        self.y = self.base_y + 30 * math.sin(self.x/15)

    def on_paint(self, canvas):
        """
        Paint event handler
        :param canvas: canvas to blit dir-changer image into
        """
        canvas.blit(self.images[self.current], (self.x, self.y))

    def collide(self, other):
        """
        Check for collision between this object and the other one
        :param other: the other object
        :return tuple of intersection or None
        """
        return self.masks[self.current].overlap(other.mask, (other.x - self.x, other.y - self.y))


def dircs_from_factory(resman, dlist: list):
    """
    Populate a list of dir-changers for given level
    :param resman: ResourceManager handle
    :param dlist: dircs list (scenario)
    :return: list of dircs
    """
    dircs = []
    for od in dlist:
        dc = DirChanger(resman.dircs, od[0], od[1])
        dircs.append(dc)
    return dircs
