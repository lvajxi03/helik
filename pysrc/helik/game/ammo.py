#!/usr/bin/env python3

"""
Ammo handler module
"""

import math
import pygame
from helik.hdefs import ARENA_WIDTH


class Ammo:
    """
    Ammo handler class
    """
    def __init__(self, images: list, x: int, y: int):
        """
        Ammo class constructor
        :param images: list of ammo images
        :param x: top-left x coordinate
        :param y: top-left y coordinate
        """
        self.x = x
        self.base_y = y
        self.y = y
        self.images = images
        self.current = 0
        self.masks = [pygame.mask.from_surface(x) for x in self.images]
        self.rects = [x.get_rect() for x in self.images]

        self.w = self.rects[0].w
        self.h = self.rects[0].h
        if self.x > ARENA_WIDTH:
            self.visible = False
        else:
            self.visible = True
        self.valid = True

    def next(self):
        """
        Switch to a next frame
        """
        self.current += 1
        self.current %= len(self.images)

    def on_paint(self, canvas):
        """
        Paint event handler
        """
        canvas.blit(self.images[self.current], (self.x, self.y))

    def collide(self, other):
        """
        Check for collision between this object and the other one
        :param other: the other object
        :return: tuple of intersection or None
        """
        return self.masks[self.current].overlap(other.mask, (other.x - self.x, other.y - self.y))

    def move(self, speed=1):
        """
        Move ammo object according to its policy
        """
        self.x -= speed
        if self.x - self.w < 0:
            self.valid = False
            self.visible = False
        elif self.x < ARENA_WIDTH:
            self.visible = True
        self.y = self.base_y + 30 * math.sin(self.x/15)


def ammos_from_factory(resman, alist: list):
    """
    Populate a list of ammo marks for given level
    :param resman: ResourceManager handle
    :param alist: ammos list (scenario)
    :return: list of ammos
    """
    ammos = []
    images = [resman.images["ammos"][0],
              resman.images["ammos"][1],
              resman.images["ammos"][0],
              resman.images["ammos"][2]]
    for oa in alist:
        am = Ammo(images, oa[0], oa[1])
        ammos.append(am)
    return ammos
