#!/usr/bin/env python3

"""
Cloud handler module
"""

from itertools import cycle, islice
import pygame
from helik.hdefs import ARENA_WIDTH
from helik.game.distance import Distance
from helik.game.planes import Plane


class Cloud:
    """
    Cloud handler class
    """
    def __init__(self, image, x, y):
        self.x = x
        self.y = y
        self.image = image
        self.mask = pygame.mask.from_surface(image)
        r = self.image.get_rect()
        self.w = r.w
        self.h = r.h
        self.valid = True
        if self.x > ARENA_WIDTH:
            self.visible = False
        else:
            self.visible = True

    def move(self, speed=1):
        """
        Move cloud according to its policy
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

    def collide(self, other):
        """
        Check for collision between this object and the other
        :param other: other object
        :return: tuple of intersection or None
        """
        return self.mask.overlap(other.mask, (other.x - self.x, other.y - self.y))

def clouds_from_factory(resman, clist: list, amount: int, lang: str, levelidx: int):
    """
    Populate a list of clouds for given level. Plus leading plane.
    :param resman: ResourceManager handle
    :param clist: clouds list (scenario)
    :param lang: language (2-chars) identifier
    :param levelidx: level index
    :return: list of clouds (and leading plane)
    """
    clouds = []
    x = ARENA_WIDTH
    gen = cycle(clist)
    ce = list(islice(gen, amount))
    p = Plane(resman.plane_levels[lang][levelidx], x, 50)
    clouds.append(p)
    x += p.w
    distance = Distance(x, 100)
    clouds.append(distance)
    x += distance.w
    for oc in ce:
        if oc[0] == -1:
            distance = Distance(x, oc[1])
            clouds.append(distance)
            x += oc[1]
        else:
            cloud = Cloud(resman.clouds[oc[0]], x, oc[1])
            clouds.append(cloud)
            x += cloud.w
    return clouds
