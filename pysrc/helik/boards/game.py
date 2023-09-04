#!/usr/bin/env python3

"""
Game board for HeliK
"""


import pygame
from helik.boards.standard import Board
from helik.htypes import BoardType, TimerType, GameType
from helik.hdefs import ARENA_WIDTH, ARENA_HEIGHT
from helik.game.objects import Copter
from helik.modes.standard import Mode
from helik.modes.init import ModeInit
from helik.modes.prepare import ModePrepare
from helik.modes.play import ModePlay
from helik.modes.paused import ModePaused
from helik.modes.killed import ModeKilled


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
        self.modes = {
            GameType.NONE: Mode(self),
            GameType.INIT: ModeInit(self),
            GameType.PREPARE: ModePrepare(self),
            GameType.PLAY: ModePlay(self),
            GameType.PAUSED: ModePaused(self),
            GameType.KILLED: ModeKilled(self)
            }
        self.game_data = {
            'points': 0
            }

    def change_mode(self, newmode):
        """
        Change to new game mode.
        Mode is changed only if differs from current mode:
        1. Old mode runs its `deactivate` method
        2. Mode is changed
        3. New mode runs its `activate` method
        :param mode: new mode
        """
        if newmode != self.mode:
            self.modes[self.mode].deactivate()
            self.mode = newmode
            self.modes[self.mode].activate()

    def activate(self):
        """
        Activate event handler
        """
        self.change_mode(GameType.INIT)

    def deactivate(self):
        """
        """
        pygame.time.set_timer(TimerType.PLAY_MOVE, 0)

    def on_paint(self):
        """
        Paint event handler
        """
        self.modes[self.mode].on_paint()

    def on_keyup(self, key):
        """
        Key release event handler
        :param key: key code
        """
        if key == pygame.K_q:
            self.parent.change_board(BoardType.MENU)
        else:
            self.modes[self.mode].on_keyup(key)

    def on_timer(self, timer):
        """
        """
        self.modes[self.mode].on_timer(timer)
