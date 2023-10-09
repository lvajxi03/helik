#!/usr/bin/env python3

"""
Birds handler module
"""

import pygame
from helik.hdefs import ARENA_WIDTH


class Bird:
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
        self.x = x
        self.y = y
        self.frames = []
        self.images = images
        self.frame = frame
        self.frame %= len(self.images)
        self.masks = []
        for img in self.images:
            r = img.get_rect()
            self.frames.append(r)
            mask = pygame.mask.from_surface(img)
            self.masks.append(mask)
        self.valid = True
        if self.x > ARENA_WIDTH:
            self.visible = False
        else:
            self.visible = True

    def on_paint(self, canvas):
        """
        Paint event handler
        """
        canvas.blit(self.images[self.frame], (self.x, self.y))

    def collide(self, other):
        """
        Check if the bird collides with the other object
        :param other: other object
        :return: True if collides, False otherwise
        """
        return self.masks[self.frame].overlap(other.mask, (other.x - self.x, other.y - self.y))

    def next(self):
        """
        Change bird's frame
        """
        self.frame += 1
        self.frame %= len(self.images)

    def move(self, speed=1):
        """
        Move bird
        """
        self.x -= speed
        r  = self.frames[self.frame]
        if self.x + r.w < 0:
            self.valid = False
            self.visible = False
        elif self.x < ARENA_WIDTH:
            self.visible = True
