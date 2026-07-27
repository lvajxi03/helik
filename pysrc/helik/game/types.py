#!/usr/bin/env python3

"""
Various game-related types
"""

import enum


@enum.unique
class GameObjectType(enum.IntEnum):
    """
    GameObjectType enum
    Tells you what to create from json level data
    """
    NONE = 0
    BUILDING = 1
    CLOUD = 2
    DIRC = 3
    AMMO = 4
    HEART = 5
    BIRD = 6
    BULLET = 7
    REMAINING = 8
