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
    KILLED = 5
    GAMEOVER = 6


@enum.unique
class TimerType(enum.IntEnum):
    WELCOME = pygame.USEREVENT + 1
    WELCOME_STOP = pygame.USEREVENT + 2
    PREPARE = pygame.USEREVENT + 3
    PREPARE_MINOR = pygame.USEREVENT + 4
    PREPARE_STOP = pygame.USEREVENT + 5
    COPTER = pygame.USEREVENT + 6
    MOVABLES = pygame.USEREVENT + 7
    SECONDS = pygame.USEREVENT + 8
    BULLETS = pygame.USEREVENT + 9


@enum.unique
class PlayOptionType(enum.IntEnum):
    TRAINING = 0
    EASY = 1
    NORMAL = 2
    HARD = 3
    EXTREME = 4
