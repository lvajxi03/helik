#!/usr/bin/env python

"""
Level handler module
"""

import pygame
from helik.game.buildings import buildings_from_factory, Building
from helik.hdefs import ARENA_WIDTH, ARENA_HEIGHT, STATUS_HEIGHT


class Level:
    """
    Level handler class
    """
    def __init__(self, resman, index: int):
        """
        :param resman: resource manager handle
        :param index: level number
        """
        self.res_man = resman
        self.index = index
        self.width = 0
        self.x = 0
        self.current = None
        self.image = None
        self.buildings = []
        self.clouds = []
        self.bullets_from = []
        self.planes = []

    def create_buildings(self):
        buildings_data = self.res_man.levels[self.index]["buildings"]
        self.buildings = buildings_from_factory(self.res_man, buildings_data, self.res_man.levels[self.index]["buildings-amount"])
        self.width = self.buildings[-1].x + self.buildings[-1].w

    def make_bullet_from(self, copter):
        """
        Make new BulletFrom
        :param copter: copter instance handle
        """
        bullet = Bullet(self.res_man.images["bullet-1"], self.copter.x + self.copter.w, self.copter.y + self.copter.h // 2)
        self.bullets_from.append(bullet)

    def move(self, speed=-1):
        """
        Move all the objects
        """
        for building in self.buildings:
            building.move(speed)

        for cloud in self.clouds:
            cloud.move(speed)

    def on_paint(self, canvas):
        """
        Paint event handler
        :param canvas: canvas to paint images into
        """
        for building in self.buildings:
            if building.visible:
                building.on_paint(canvas)

        for cloud in self.clouds:
            if cloud.visible:
                cloud.paint(canvas)

        for plane in self.planes:
            if plane.visible:
                plane.paint(canvas)

        for bullet in self.bullets_from:
            if bullet.visible:
                bullet.paint(canvas)
