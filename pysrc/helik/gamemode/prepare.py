#!/usr/bin/env python3

"""
Mode prepare handler module
"""


import pygame
from helik.platform import TimerType
from helik.hdefs import ARENA_WIDTH, ARENA_HEIGHT
from .standard import Mode
from .types import GameMode


class ModePrepare(Mode):
    """
    Mode prepare handle class
    """
    def __init__(self, parent):
        """
        Mode prepare class constructor
        """
        super().__init__(parent)
        self.timers = {
            TimerType.FIRST: self.on_alpha,
            TimerType.SECOND: self.on_prepare,
            TimerType.THIRD: self.on_prepare_stop
        }
        self.alpha = 255
        self.index = 0
        self.rect = self.resman.images["big"][0].get_rect()
        self.rect.center = (ARENA_WIDTH // 2, ARENA_HEIGHT // 2)

    def on_timer(self, timer):
        """
        Timer event handler
        :param timer: timer identifier
        """
        try:
            self.timers[timer]()
        except KeyError:
            pass

    def on_alpha(self):
        """
        Handle TimerType.FIRST,
        Decrease alpha value
        """
        self.alpha -= 20
        self.resman.images["big"][self.index].set_alpha(self.alpha)

    def on_prepare(self):
        """
        Handle PREPARE timer
        """
        self.index += 1
        self.alpha = 255
        self.resman.images["big"][self.index].set_alpha(self.alpha)

    def on_prepare_stop(self):
        """
        Handle PREPARE_STOP timer
        """
        self.game.change_mode(GameMode.NEWLEVEL)

    def activate(self):
        """
        Activate event handler
        """
        self.audio.stop_background_music()
        self.audio.play_sfx("countdown")
        self.alpha = 255
        self.index = 0
        pygame.time.set_timer(TimerType.FIRST, 50)
        pygame.time.set_timer(TimerType.SECOND, 1000)
        pygame.time.set_timer(TimerType.THIRD, 3000)

    def deactivate(self):
        """
        Deactivate event handler
        """
        pygame.time.set_timer(TimerType.FIRST, 0)
        pygame.time.set_timer(TimerType.SECOND, 0)
        pygame.time.set_timer(TimerType.THIRD, 0)

    def on_paint(self):
        """
        Paint event handler
        """
        self.buffer.blit(
            self.resman.images["default-background"], (0, 0))
        self.buffer.blit(self.resman.images["big"][self.index], self.rect)
