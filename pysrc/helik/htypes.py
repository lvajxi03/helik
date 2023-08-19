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
class GameType(enum.IntEnum):
    INIT = 0
    PREPARE = 1
    PLAY = 2
    PAUSED = 3


@enum.unique
class TimerType(enum.IntEnum):
    WELCOME = pygame.USEREVENT + 1
    WELCOME_STOP = pygame.USEREVENT + 2
