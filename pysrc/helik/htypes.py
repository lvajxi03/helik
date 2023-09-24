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
    NEWLEVEL = 3
    PLAY = 4
    PAUSED = 5
    KILLED = 6
    GAMEOVER = 7


@enum.unique
class TimerType(enum.IntEnum):
    WELCOME_STOP = pygame.USEREVENT + 1
    PREPARE_MINOR = pygame.USEREVENT + 2
    PREPARE_STOP = pygame.USEREVENT + 3
    COPTER = pygame.USEREVENT + 4
    SECONDS = pygame.USEREVENT + 5


@enum.unique
class PlayOptionType(enum.IntEnum):
    TRAINING = 0
    EASY = 1
    NORMAL = 2
    HARD = 3
    EXTREME = 4
