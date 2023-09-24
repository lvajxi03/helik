#!/usr/bin/env python

"""
Level handler module
"""

import pygame
from helik.game.buildings import buildings_from_factory, Building
from helik.game.clouds import clouds_from_factory, Cloud
from helik.game.bullets import Bullet
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
        self.bullets = []
        self.planes = []
        # Buildings and clouds total widths:
        self.b_width = 0
        self.c_width = 0

    def create_buildings(self):
        """
        Create buildings for this given level
        """
        buildings_data = self.res_man.levels[self.index]["buildings"]
        self.buildings = buildings_from_factory(self.res_man, buildings_data, self.res_man.levels[self.index]["buildings-amount"])
        self.b_width = self.buildings[-1].x + self.buildings[-1].w

    def create_clouds(self):
        """
        Create clouds for this given level
        """
        clouds_data = self.res_man.levels[self.index]["clouds"]
        self.clouds = clouds_from_factory(self.res_man, clouds_data, self.res_man.levels[self.index]["clouds-amount"])
        self.c_width = self.clouds[-1].x + self.clouds[-1].w

    def make_bullet(self, copter):
        """
        Make new BulletFrom
        :param copter: copter instance handle
        """
        bullet = Bullet(self.res_man.images["bullet"], copter.x + copter.w, copter.y + copter.h // 2)
        self.bullets.append(bullet)

    def move(self, speed):
        """
        Move all the objects
        """
        for building in self.buildings:
            if building.valid:
                building.move(speed)

        for cloud in self.clouds:
            if cloud.valid:
                cloud.move(speed)

        for bullet in self.bullets:
            if bullet.valid:
                bullet.move(speed)

    def on_paint(self, canvas):
        """
        Paint event handler
        :param canvas: canvas to paint images into
        """
        for building in self.buildings:
            if building.visible and building.valid:
                building.on_paint(canvas)

        for cloud in self.clouds:
            if cloud.visible and cloud.valid:
                cloud.on_paint(canvas)

        for plane in self.planes:
            if plane.visible and plane.valid:
                plane.on_paint(canvas)

        for bullet in self.bullets:
            if bullet.visible and bullet.valid:
                bullet.on_paint(canvas)
