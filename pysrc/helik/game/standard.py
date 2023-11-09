#!/usr/bin/env python3

"""
Standard and abstract game objects
"""

import enum


@enum.unique
class GameObjectType(enum.IntEnum):
    """
    Game object type enum
    """
    DISTANCE = 0
    BUILDING = 1
    CLOUD = 2
    AMMO = 3
    DIRC = 4
    BIRD = 5


class GameObject:
    """
    GameObject class
    """
    def __init__(self, x: int, y: int, gotype: GameObjectType):
        """
        GameObject constructor
        :param x: top-left x coordinate
        :param y: top-left y coordinate
        :param gotype: type of game object (see GameObjectType)
        """
        self.x = x
        self.y = y
        self.valid = True
        self.visible = True
        self.gotype = gotype

    def on_paint(self, canvas):
        """
        Paint event handler
        """

    def collide(self, other):
        """
        Check for collision between this object and the other
        :param other: the other object
        :return: tuple of intersection or None
        """
        return False

    def move(self, speed):
        """
        Move game object according to its policy
        """
