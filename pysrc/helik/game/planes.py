#!/usr/bin/env python3

"""
Planes handler module
"""

import pygame
from helik.hdefs import ARENA_WIDTH


class Plane:
    """
    Plane hander class
    """
    def __init__(self, image, x, y):
        self.image = image
        self.mask = pygame.mask.from_surface(image)
        r = self.image.get_rect()
        self.x = x
        self.y = y
        self.w = r.w
        self.h = r.h
        self.valid = True
        if self.x > ARENA_WIDTH:
            self.visible = False
        else:
            self.visible = True

    def collide(self, other):
        """
        Check for collision between this object and the other
        :param other: other object
        :return tuple of intersection of None
        """
        return self.mask.overlap(other.mask, (other.x - self.x, other.y - self.y))

    def move(self, speed=1):
        """
        Move plane
        """
        self.x -= speed
        if self.x + self.w < 0:
            self.valid = False
            self.visible = False
        elif self.x < ARENA_WIDTH:
            self.visible = True

    def on_paint(self, canvas):
        """
        Paint event handler
        :param canvas: canvas to blit cloud image into
        """
        canvas.blit(self.image, (self.x, self.y))
