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
        self.x = 600
        self.y = ARENA_HEIGHT

    def activate(self):
        """
        Activate event handler
        """
        self.y = ARENA_HEIGHT
        pygame.time.set_timer(TimerType.FIRST, 30)
        pygame.time.set_timer(TimerType.SECOND, 1000)

    def deactivate(self):
        pygame.time.set_timer(TimerType.SECOND, 0)
        pygame.time.set_timer(TimerType.FIRST, 0)

    def on_timer(self, timer):
        """
        Timer event handler
        :param timer: timer type code
        """
        if timer == TimerType.SECOND:
            self.game.change_mode(GameType.PLAY)
        elif timer == TimerType.FIRST:
            self.y -= 10

    def on_paint(self):
        """
        Paint event handler
        """
        self.buffer.blit(self.res_man.images["default-background"], (0, 0))
        self.buffer.blit(self.res_man.images["krzyk"], (self.x, self.y))
