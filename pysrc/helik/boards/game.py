#!/usr/bin/env python3

"""
Game board for HeliK
"""

from helik.board.standard import Board
from helik.htypes import TimerType
from helik.hdefs import ARENA_WIDTH, ARENA_HEIGHT


class BoardGame(Board):
    """
    Game board class for HeliK
    """
    def __init__(self, parent):
        """
        Game board constructor
        """
        super().__init__(parent)

    def activate(self):
        """
        """

    def deactivate(self):
        """
        """

    def on_paint(self):
        """
        """

    def on_keydown(self, key):
        """
        """

    def on_timer(self, timer):
        """
        """
