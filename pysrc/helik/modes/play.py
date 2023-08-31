#!/usr/bin/env python3

"""
Mode play handler module
"""


import pygame
from helik.modes.standard import Mode
from helik.htypes import TimerType


class ModePlay(Mode):
    """
    Mode play handle class
    """
    def __init__(self, parent):
        """
        Mode play class constructor
        """
        super().__init__(parent)

    def activate(self):
        """
        Activate event handler
        """
        pygame.time.set_timer(TimerType.PLAY_MOVE, 10)

    def deactivate(self):
        pygame.time.set_timer(TimerType.PLAY_MOVE, 0)

    def on_timer(self, timer):
        """
        Timer event handler
        """
        self.game.copter.on_timer(timer)

    def on_keyup(self, key):
        """
        Key release event handler
        :param key: key code
        """
        self.game.copter.on_keyup(key)

    def on_paint(self):
        """
        Paint event handler
        """
        self.res_man.get("surfaces", "buffer").blit(self.res_man.get("images", "default-background"), (0, 0))
        self.game.copter.on_paint()
