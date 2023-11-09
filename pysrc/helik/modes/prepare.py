#!/usr/bin/env python3

"""
Mode prepare handler module
"""


import pygame
from helik.modes.standard import Mode
from helik.htypes import TimerType, GameMode
from helik.hdefs import ARENA_WIDTH, ARENA_HEIGHT


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
            TimerType.SECOND: self.on_prepare,
            TimerType.THIRD: self.on_prepare_stop
        }
        self.alpha = 255
        self.index = 0
        self.rect = self.res_man.images["big"][0].get_rect()
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

    def on_update(self, delta):
        """
        Update event handler
        :param delta: delta time from last frame
        """
        self.alpha -= 5
        self.res_man.images["big"][self.index].set_alpha(self.alpha)

    def on_prepare(self):
        """
        Handle PREPARE timer
        """
        self.index += 1
        self.alpha = 255

    def on_prepare_stop(self):
        """
        Handle PREPARE_STOP timer
        """
        self.game.change_mode(GameMode.NEWLEVEL)

    def activate(self):
        """
        Activate event handler
        """
        self.audio.play_sound("countdown")
        self.alpha = 255
        self.index = 0
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
            self.res_man.images["default-background"], (0, 0))
        self.buffer.blit(self.res_man.images["big"][self.index], self.rect)
