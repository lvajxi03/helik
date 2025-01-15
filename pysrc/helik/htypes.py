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


@enum.unique
class SoundPlayState(enum.IntEnum):
    """
    SoundPlayState enum
    Tells you what state is the particular sound object
    """
    STOPPED = 0
    PLAYING = 1
    PAUSED = 2


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


@enum.unique
class SettingsModeId(enum.IntEnum):
    """
    Settings board can have multiple modes:
    1. Main settings menu
    2. Keyboard layout
    3. Keyboard input
    4. Gamepad layout
    5. Gamepad input
    """
    MAIN = 0
    KLAYOUT = 1
    KINPUT = 2
    GLAYOUT = 3
    GINPUT = 4
