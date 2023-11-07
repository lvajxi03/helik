#!/usr/bin/env python3

"""
Game board for HeliK
"""


import pygame
from helik.boards.standard import Board
from helik.game.player import Player
from helik.game.level import Level
from helik.htypes import BoardType, GameMode
from helik.modes.init import ModeInit
from helik.modes.killed import ModeKilled
from helik.modes.paused import ModePaused
from helik.modes.play import ModePlay
from helik.modes.prepare import ModePrepare
from helik.modes.standard import Mode
from helik.modes.newlevel import ModeNewLevel
from helik.modes.selectplayer import SelectPlayer


class BoardGame(Board):
    """
    Game board class for HeliK
    """
    def __init__(self, parent):
        """
        Game board constructor
        """
        super().__init__(parent)
        self.mode = GameMode.NONE
        self.player = None
        self.data = {
            'points': 0,
            'level': -1,
            'option': 2,
            'seconds': 0,
            'bullets-available': 20,
            'lives': 5
        }
        self.modes = {
            GameMode.NONE: Mode(self),
            GameMode.SELECTPLAYER: SelectPlayer(self),
            GameMode.INIT: ModeInit(self),
            GameMode.PREPARE: ModePrepare(self),
            GameMode.PLAY: ModePlay(self),
            GameMode.PAUSED: ModePaused(self),
            GameMode.KILLED: ModeKilled(self),
            GameMode.NEWLEVEL: ModeNewLevel(self)
            }
        self.explosions = []

        self.level = None

    def new_level(self):
        """
        Initialize new level data
        """
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
        self.change_mode(GameMode.INIT)

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
