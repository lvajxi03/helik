#!/usr/bin/env python3

"""
Standard and abstract game objects
"""

import pygame
from helik.hdefs import ARENA_WIDTH
from .types import GameObjectType


class GameObject:
    """
    GameObject class
    """
    def __init__(self, x: int, y: int, go_type: GameObjectType):
        """
        GameObject constructor
        :param x: top-left x coordinate
        :param y: top-left y coordinate
        :param go_type: type of game object (see GameObjectType)
        """
        self.x = x
        self.y = y
        self.base_y = y
        self.valid = True
        self.visible = True
        self.go_type = go_type

    def on_paint(self, canvas):
        """
        Paint event handler
        """

    def collide(self, other):
        """
        Check for collision between this object and the other one
        :param other: the other object
        :return: tuple of intersection or None
        """
        return False

    def move(self, speed):
        """
        Move game object according to its policy
        :param speed: move object by <speed> pixels left
        """


class ImageGameObject(GameObject):
    """
    ImageGameObject class
    This class represents an object with assigned single image
    """
    def __init__(self, x: int, y: int, go_type: GameObjectType, image):
        """
        ImageGameObject class constructor
        """
        super().__init__(x, y, go_type)
        self.image = image
        self.mask = pygame.mask.from_surface(image)
        r = self.image.get_rect()
        self.w = r.w
        self.h = r.h

    def on_paint(self, canvas):
        """
        Paint event handler
        """
        canvas.blit(self.image, (self.x, self.y))

    def move(self, speed):
        """
        Move image object according to its policy
        """
        self.x -= speed
        if self.x + self.w < 0:
            self.visible = False
            self.valid = False
        elif self.x > ARENA_WIDTH:
            self.visible = False

    def collide(self, other):
        """
        Check if current object collides the other one
        :param other: other object
        """
        return self.mask.overlap(other.mask, (other.x - self.x, other.y - self.y))


class ImageListGameObject(ImageGameObject):
    """
    ImageListGameObject class
    This class represents an object with multiple frames
    """
    def __init__(self, x, y, go_type: GameObjectType, images: list):
        super().__init__(x, y, go_type, images[0])
        self.images = images
        self.rects = [image.get_rect() for image in self.images]
        self.masks = [pygame.mask.from_surface(image) for image in self.images]
        self.current = 0
        self.max_frame = len(self.images)
        # Internal counter
        self.ic = 0

    def next(self):
        """
        Calculate next frame
        """
        self.ic += 1
        if self.ic == 7:
            self.current += 1
            self.current %= self.max_frame
            self.image = self.images[self.current]
            self.mask = self.masks[self.current]
            self.w = self.rects[self.current].w
            self.h = self.rects[self.current].h
            self.ic = 0
