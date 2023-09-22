#!/usr/bin/env python3

"""
Bullets handler module
"""

import pygame
from helik.hdefs import ARENA_HEIGHT, ARENA_WIDTH, STATUS_HEIGHT


class Bullet:
    """
    Bullet handler class
    """
    def __init__(self, image, x, y):
        self.x = x
        self.y = y
        self.image = image
        self.mask = pygame.mask.from_surface(self.image)
        r = self.image.get_rect()
        self.w = r.w
        self.h = r.h
        self.y = y
        self.valid = True
        if self.x > ARENA_WIDTH:
            self.visible = False
        else:
            self.visible = True

    def collide(self, other):
        """
        Check for collision between this object and the other
        :param other: other object
        :return: tuple of intersection or None
        """
        return self.mask.overlap(other.mask, (other.x - self.x, other.y - self.y))

    def move(self, delta=1):
        """
        Move bullet
        """
        if self.valid:
            self.x += 10*delta
            if self.x > ARENA_WIDTH:
                self.valid = False
                self.visible = False

    def on_paint(self, canvas):
        """
        Paint event handler
        :param canvas: surface to blit bullet into
        """
        if self.visible and self.valid:
            canvas.blit(self.image, (self.x, self.y))
