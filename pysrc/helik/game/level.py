#!/usr/bin/env python

"""
Level handler module
"""


from helik.game.buildings import buildings_from_factory
from helik.game.clouds import clouds_from_factory
from helik.game.bullets import Bullet
from helik.game.dirc import dircs_from_factory
from helik.hdefs import ARENA_WIDTH
from helik.game.birds import Bird


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
        self.birds = []
        self.dircs = []
        self.birds = []
        # New approach?
        self.lane_upper = []
        self.lane_lower = []

    def rewind(self):
        """
        Rewind buildings, planes, clouds etc to the right
        (behind right window edge)
        """
        xf = []
        if len(self.buildings) > 0:
            xf.append(self.buildings[0].x)
        if len(self.clouds) > 0:
            xf.append(self.clouds[0].x)
        if len(self.birds) > 0:
            xf.append(self.birds[0].x)
        if len(self.dircs) > 0:
            xf.append(self.dircs[0].x)
        if len(xf) > 0:
            xfd = ARENA_WIDTH - min(xf)
        else:
            xfd = ARENA_WIDTH

        # Rewind everything:
        for building in self.buildings:
            building.x += xfd
        for cloud in self.clouds:
            cloud.x += xfd
        for bird in self.birds:
            bird.x += xfd
        for dirc in self.dircs:
            dirc.x += xfd

    def create_lane_upper(self):
        """
        Upper lane contains mostly clouds, ammos,
        """

    def create_lane_lower(self):
        """
        Lower lane contains buildings, coins, etc.
        """

    def create_buildings(self):
        """
        Create buildings for this given level
        """
        buildings_data = self.res_man.levels[self.index]["buildings"]
        self.buildings = buildings_from_factory(
            self.res_man,
            buildings_data,
            self.res_man.levels[self.index]["buildings-amount"])

    def create_clouds(self):
        """
        Create clouds for this given level
        """
        clouds_data = self.res_man.levels[self.index]["clouds"]
        self.clouds = clouds_from_factory(self.res_man,
                                          clouds_data,
                                          self.res_man.levels[self.index]["clouds-amount"])

    def create_dircs(self):
        """
        Create dircs for this given level
        """
        self.dircs = dircs_from_factory(self.res_man, self.res_man.levels[self.index]["dircs"])

    def create_birds(self):
        """
        Create birds for this given level
        TODO.
        """
        birds_data = self.res_man.levels[self.index]["birds"]
        for bdata in birds_data:
            bird = Bird(bdata[0], bdata[1], self.res_man.birds, bdata[2])
            self.birds.append(bird)

    def make_bullet(self, copter):
        """
        Make new BulletFrom
        :param copter: copter instance handle
        """
        bullet = Bullet(self.res_man.images["rocket-1"],
                        copter.x + copter.w, copter.y + copter.h // 2)
        self.bullets.append(bullet)

    def move(self, speed):
        """
        Move all the objects
        """
        for cloud in self.clouds:
            if cloud.valid:
                cloud.move(speed)

        for bullet in self.bullets:
            if bullet.valid:
                bullet.move(8 * speed)

        for dirc in self.dircs:
            if dirc.valid:
                dirc.move(speed)

        for bird in self.birds:
            if bird.valid:
                bird.move(speed)

    def move_buildings(self, speed=1):
        """
        Move buildings according to their speed
        :param speed: speed of buildings
        """
        for building in self.buildings:
            if building.valid:
                building.move(speed)

    def on_paint(self, canvas):
        """
        Paint event handler
        :param canvas: canvas to paint images into
        """
        for cloud in self.clouds:
            if cloud.visible and cloud.valid:
                cloud.on_paint(canvas)

        for building in self.buildings:
            if building.visible and building.valid:
                building.on_paint(canvas)

        for plane in self.planes:
            if plane.visible and plane.valid:
                plane.on_paint(canvas)

        for bullet in self.bullets:
            if bullet.visible and bullet.valid:
                bullet.on_paint(canvas)

        for dirc in self.dircs:
            if dirc.visible and dirc.valid:
                dirc.on_paint(canvas)

        for bird in self.birds:
            if bird.visible and bird.valid:
                bird.on_paint(canvas)

    def rotate(self):
        """
        Rotate all game elements if not valid
        """
        self.bullets = [x for x in self.bullets if x.valid]
        self.buildings = [x for x in self.buildings if x.valid]
        self.clouds = [x for x in self.clouds if x.valid]
        self.planes = [x for x in self.planes if x.valid]
        self.dircs = [x for x in self.dircs if x.valid]
        self.birds = [x for x in self.birds if x.valid]

    def is_empty(self):
        """
        Check if level is empty (no opbjects to collide)
        :return: True if empty, False otherwise
        """
        if len(self.buildings) == 0 \
        and len(self.clouds) == 0 \
        and len(self.planes) == 0 \
        and len(self.birds) == 0 \
        and len(self.dircs) == 0:
            return True
        return False
