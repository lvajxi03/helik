#!/usr/bin/env python3

"""
All the types
"""


import enum


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
class HelpChapter(enum.IntEnum):
    """
    Help chapters definition
    """
    WELCOME = 0
    NAVIGATION = 1
    SETTINGS = 2
    OPTIONS = 3
    HISCORES = 4
    GAMEPLAY = 5
    MAINGOAL = 6
    VEHICLESELECTION = 7
    GAMENAVIGATION = 8
    GAMEOBJECTS = 9
    SCORING = 10
