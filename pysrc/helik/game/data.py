#!/usr/bin/env python3

"""
Game data module
"""


class GameData:
    """
    Main game data class
    """
    def __init__(self):
        self.level = 0
        self.points = 0
        self.option = 1

    def reset(self):
        self.level = 0
        self.points = 0
        self.option = 1

    def score(self):
        self.points += self.option
