#!/usr/bin/env python3

"""
Game types
"""

import enum


@enum.unique
class GameMode(enum.IntEnum):
    """
    GameMode enum
    """
    NONE = 0
    INIT = 1
    SELECTPLAYER = 2
    PREPARE = 3
    NEWLEVEL = 4
    PLAY = 5
    PAUSED = 6
    KILLED = 7
    GAMEOVER = 8
