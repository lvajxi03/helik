#!/usr/bin/env python3

"""
Buildings module
"""

from itertools import cycle, islice
import pygame
from helik.hdefs import ARENA_WIDTH, ARENA_HEIGHT, STATUS_HEIGHT
from helik.game.distance import Distance


class Building:
    """
    Building handler class
    """
    def __init__(self, image, x):
        self.image = image
        self.mask = pygame.mask.from_surface(image)
        r = image.get_rect()
        self.x = x
        self.w = r.w
        self.h = r.h
        self.y = ARENA_HEIGHT - STATUS_HEIGHT - r.h
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

    def move(self, speed=1):
        """
        Move building
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
        :param canvas: surface to blit building into
        """
        if self.visible and self.valid:
            canvas.blit(self.image, (self.x, self.y))


def buildings_from_factory(resman, blist: list, amount: int):
    """
    Populate a list of buildings for given level.
    :param resman: ResourceManager handle
    :param blist: buildings list (scenario)
    :return: list of buildings
    """
    buildings = []
    x = ARENA_WIDTH
    gen = cycle(blist)
    be = list(islice(gen, amount))
    for ob in be:
        if ob[0] == -1:
            distance = Distance(x, ob[1])
            buildings.append(distance)
            x += ob[1]
        else:
            building = Building(resman.buildings[ob[0]], x)
            buildings.append(building)
            x += building.w
    return buildings
