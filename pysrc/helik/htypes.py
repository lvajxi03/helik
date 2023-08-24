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
    NONE = 0
    INIT = 1
    PREPARE = 2
    PLAY = 3
    PAUSED = 4


@enum.unique
class TimerType(enum.IntEnum):
    WELCOME = pygame.USEREVENT + 1
    WELCOME_STOP = pygame.USEREVENT + 2
    PLAY_MOVE = pygame.USEREVENT + 3
