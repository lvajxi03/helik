#!/usr/bin/env python

"""
Level handler module
"""


from helik.game.bullets import Bullet
from helik.hdefs import ARENA_WIDTH, ARENA_HEIGHT
from helik.game.lane import Lane


class Level:
    """
    Level handler class
    """
    def __init__(self, resman, index: int, option: int):
        """
        :param resman: resource manager handle
        :param index: level number
        :param option: game option
        """
        self.resman = resman
        data = resman.levels[index]
        self.lanes = []
        self.bullets = []
        # TODO: or make it a const in hdefs module?
        self.bullet_speed = 8
        multiplier = data["multipliers"][option]
        if multiplier < 1:
            multiplier = 1
        for ld in data["lanes"]:
            la = Lane(ld, resman, multiplier)
            self.lanes.append(la)

    def rewind(self):
        """
        Reqind all the objects in all lanes
        (behind right window edge)
        """

        # Calculate maximum margin
        minx = ARENA_WIDTH
        for lane in self.lanes:
            try:
                obj = lane.objects[0]
                if obj.x < minx:
                    minx = obj.x
            except IndexError:
                # Prevents checking empty lanes
                pass
        minx = ARENA_WIDTH - minx

        # Rewind
        for lane in self.lanes:
            lane.rewind(minx)

    def make_bullet(self, copter):
        """
        Make new BulletFrom
        :param copter: copter instance handle
        """
        bullet = Bullet(self.resman.images["rocket-1"],
                        copter.x + copter.w, copter.y + copter.h // 2)
        self.bullets.append(bullet)

    def move(self):
        """
        Move all the objects
        """
        for lane in self.lanes:
            lane.move()

        for bullet in self.bullets:
            if bullet.valid:
                bullet.move(self.bullet_speed)

    def on_paint(self, canvas):
        """
        Paint event handler
        :param canvas: canvas to paint images into
        """
        for lane in self.lanes:
            lane.paint(canvas)

        for bullet in self.bullets:
            bullet.paint(canvas)

    def is_empty(self):
        """
        Check if level is empty (no opbjects to collide)
        :return: True if empty, False otherwise
        """
        for lane in self.lanes:
            if len(lane) > 0:
                return False
        return True
