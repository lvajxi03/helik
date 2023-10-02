#!/usr/bin/env python3

"""
Mode killed handler module
"""


import pygame
from helik.modes.standard import Mode
from helik.hdefs import ARENA_HEIGHT
from helik.htypes import GameType, TimerType


class ModeKilled(Mode):
    """
    Mode killed handle class
    """
    def __init__(self, parent):
        """
        Mode killed class constructor
        """
        super().__init__(parent)
        self.previous_y = 0

    def activate(self):
        """
        Activate event handler
        """
        self.previous_y = self.game.copter.y
        pygame.time.set_timer(TimerType.FIRST, 5)

    def deactivate(self):
        pygame.time.set_timer(TimerType.SECOND, 0)

    def on_update(self, delta):
        self.game.level.move(delta)

        for explosion in self.game.explosions:
            explosion.on_update(delta)

    def on_timer(self, timer):
        """
        Timer event handler
        :param timer: timer type code
        """
        if timer == TimerType.FIRST:
            self.game.copter.y += 10
            if self.game.copter.y > ARENA_HEIGHT:
                self.game.copter.y = self.previous_y
                self.game.change_mode(GameType.PLAY)

    def on_paint(self):
        """
        Paint event handler
        """
        self.game.modes[GameType.PLAY].on_paint()
