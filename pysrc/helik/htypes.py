#!/usr/bin/env python3

"""
HeliK types
"""

import enum
import pygame


@enum.unique
class BoardType(enum.IntEnum):
    """
    BoardType enum
    """
    WELCOME = 0
    MENU = 1
    OPTIONS = 2
    GAME = 3
    HISCORES = 4
    SETTINGS = 5
    HELP = 6
    ABOUT = 7
    NEWSCORE = 8
    GAMEOVER = 9
    QUIT = 10


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


@enum.unique
class TimerType(enum.IntEnum):
    """
    TimerType enum
    There are only like 7-8 user events available,
    thus all the timers shall be reusable and have
    weird names
    """
    FIRST = pygame.USEREVENT + 1
    SECOND = pygame.USEREVENT + 2
    THIRD = pygame.USEREVENT + 3
    FOURTH = pygame.USEREVENT + 5
    FIFTH = pygame.USEREVENT + 6


@enum.unique
class DirCType(enum.IntEnum):
    """
    DirCType enum
    Tells you what's the copter direction right now.
    """
    DOWN = 0
    UP = 1
