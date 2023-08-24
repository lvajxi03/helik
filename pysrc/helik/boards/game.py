#!/usr/bin/env python3

"""
Game board for HeliK
"""


import pygame
from helik.boards.standard import Board
from helik.htypes import BoardType, TimerType, GameType
from helik.hdefs import ARENA_WIDTH, ARENA_HEIGHT
from helik.game.objects import Copter


class BoardGame(Board):
    """
    Game board class for HeliK
    """
    def __init__(self, parent):
        """
        Game board constructor
        """
        super().__init__(parent)
        self.mode = GameType.NONE
        self.copter = Copter(self)

    def change_mode(self, newmode):
        """
        """

    def activate(self):
        """
        Activate event handler
        """
        self.change_mode(GameType.INIT)
        pygame.time.set_timer(TimerType.PLAY_MOVE, 12)

    def deactivate(self):
        """
        """
        pygame.time.set_timer(TimerType.PLAY_MOVE, 0)

    def on_paint(self):
        """
        """
        self.res_man.get("surfaces", "buffer").fill("#5b5b5b")
        self.copter.on_paint()

    def on_keyup(self, key):
        """
        Key release event handler
        :param key: key code
        """
        if key == pygame.K_q:
            self.parent.change_board(BoardType.MENU)
        else:
            self.copter.on_keyup(key)

    def on_timer(self, timer):
        """
        """
        self.copter.on_timer(timer)
