#!/usr/bin/env python3

"""
DirChanger handler module
"""


import pygame


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
        self.rects = []
        self.masks = []
        for image in self.images:
            r = image.get_rect()
            self.rects.append(r)
            m = pygame.mask.from_surface(image)
            self.masks.append(m)

        self.w = self.rects[0].w
        self.h = self.rects[1].h
