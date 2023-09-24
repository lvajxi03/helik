#!/usr/bin/env python3

"""
Game board for HeliK
"""


import pygame
from helik.boards.standard import Board
from helik.game.copter import Copter
from helik.game.level import Level
from helik.hdefs import ARENA_WIDTH, ARENA_HEIGHT
from helik.htypes import BoardType, TimerType, GameType
from helik.modes.init import ModeInit
from helik.modes.killed import ModeKilled
from helik.modes.paused import ModePaused
from helik.modes.play import ModePlay
from helik.modes.prepare import ModePrepare
from helik.modes.standard import Mode
from helik.modes.newlevel import ModeNewLevel


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
        self.data = {
            'points': 0,
            'level': -1,
            'option': 1,
            'seconds': 0,
            'bullets-available': 20,
            'lives': 5
        }
        self.modes = {
            GameType.NONE: Mode(self),
            GameType.INIT: ModeInit(self),
            GameType.PREPARE: ModePrepare(self),
            GameType.PLAY: ModePlay(self),
            GameType.PAUSED: ModePaused(self),
            GameType.KILLED: ModeKilled(self),
            GameType.NEWLEVEL: ModeNewLevel(self)
            }
        self.collisions = []

        self.level = None

    def new_level(self):
        self.level = Level(self.res_man, self.data['level'])

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
            self.arena.change_board(BoardType.MENU)
        else:
            self.modes[self.mode].on_keyup(key)

    def on_timer(self, timer):
        """
        Timer event handler
        :param timer: timer identifier
        """
        self.modes[self.mode].on_timer(timer)

    def on_update(self, delta):
        """
        Update event handler
        :param delta: delta time from last frame
        """
        self.modes[self.mode].on_update(delta)
