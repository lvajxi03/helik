#!/usr/bin/env python3

"""
Axis and motion types
"""


import enum


@enum.unique
class AxisType(enum.IntEnum):
    """
    Axis type definition
    """
    HORIZ = 0
    VERT = 1


@enum.unique
class AxisValue(enum.IntEnum):
    """
    Axis value definition
    """
    LOWER = -1
    HIGHER = 1
