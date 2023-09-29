#!/usr/bin/env python

"""
Level handler module
"""

import pygame
from helik.game.buildings import buildings_from_factory, Building
from helik.game.clouds import clouds_from_factory, Cloud
from helik.game.bullets import Bullet
from helik.game.dirc import DirChanger, get_dirc_images, dircs_from_factory
from helik.hdefs import ARENA_WIDTH, ARENA_HEIGHT, STATUS_HEIGHT
from helik.htypes import DirCType


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
        self.dircs = []
        # Buildings and clouds total widths:
        self.b_width = 0
        self.c_width = 0

    def get_ready(self):
        """
        """

    def rewind_by(self, dx: int):
        """
        Rewind buildings, planes, clouds etc by dx pixels to the right
        """

    def create_buildings(self):
        """
        Create buildings for this given level
        """
        buildings_data = self.res_man.levels[self.index]["buildings"]
        self.buildings = buildings_from_factory(self.res_man, buildings_data, self.res_man.levels[self.index]["buildings-amount"])
        self.b_width = self.buildings[-1].x + self.buildings[-1].w

    def create_clouds(self, lang):
        """
        Create clouds for this given level
        :param lang: language (2-chars) identifier
        """
        clouds_data = self.res_man.levels[self.index]["clouds"]
        self.clouds = clouds_from_factory(self.res_man,
                                          clouds_data,
                                          self.res_man.levels[self.index]["clouds-amount"],
                                          lang,
                                          self.index)
        self.c_width = self.clouds[-1].x + self.clouds[-1].w

    def create_dircs(self):
        """
        Create dircs for this given level
        """
        self.dircs = dircs_from_factory(self.res_man, self.res_man.levels[self.index]["dircs"])

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

        for dirc in self.dircs:
            if dirc.valid:
                dirc.move(speed)

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

        for dirc in self.dircs:
            if dirc.visible and dirc.valid:
                dirc.on_paint(canvas)

    def rotate(self):
        """
        Rotate all game elements if not valid
        """
        self.bullets = [x for x in self.bullets if x.valid]
        self.buildings = [x for x in self.buildings if x.valid]
        self.clouds = [x for x in self.clouds if x.valid]
        self.planes = [x for x in self.planes if x.valid]
        self.dircs = [x for x in self.dircs if x.valid]

    def is_empty(self):
        if len(self.buildings) == 0 and len(self.clouds) == 0 and len(self.planes) == 0:
            return True
        return False
