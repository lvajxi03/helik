#!/usr/bin/env python3

"""
Mode prepare handler module
"""


import pygame
from helik.modes.standard import Mode
from helik.htypes import TimerType, BoardType, GameType


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
            TimerType.PREPARE: self.on_prepare,
            TimerType.PREPARE_MINOR: self.on_prepare_minor,
            TimerType.PREPARE_STOP: self.on_prepare_stop
        }
        self.alpha = 255
        self.labels = ["3", "2", "1"]
        self.index = 0

    def on_timer(self, timer):
        """
        Timer event handler
        :param timer: timer identifier
        """
        try:
            self.timers[timer]()
        except KeyError:
            pass

    def on_prepare(self):
        """
        Handle PREPARE timer
        """
        self.index += 1
        self.alpha = 255

    def on_prepare_minor(self):
        """
        Handle PREPARE_MINOR timer
        """
        self.alpha -= 5
        self.res_man.set_alpha(BoardType.GAME, self.labels[self.index], self.arena.lang, self.alpha)

    def on_prepare_stop(self):
        """
        Handle PREPARE_STOP timer
        """
        self.game.change_mode(GameType.PLAY)

    def activate(self):
        """
        Activate event handler
        """
        self.alpha = 255
        self.index = 0
        pygame.time.set_timer(TimerType.PREPARE, 1000)
        pygame.time.set_timer(TimerType.PREPARE_MINOR, 20)
        pygame.time.set_timer(TimerType.PREPARE_STOP, 3000)

    def deactivate(self):
        """
        Deactivate event handler
        """
        pygame.time.set_timer(TimerType.PREPARE, 0)
        pygame.time.set_timer(TimerType.PREPARE_MINOR, 0)
        pygame.time.set_timer(TimerType.PREPARE_STOP, 0)

    def on_paint(self):
        """
        Paint event handler
        """
        self.res_man.get("surfaces", "buffer").blit(
            self.res_man.get("images", "default-background"), (0, 0))
        try:
            label, rect = self.res_man.get_label(
                BoardType.GAME, self.labels[self.index], self.arena.lang)
            self.res_man.get("surfaces", "buffer").blit(label, rect)
        except KeyError:
            pass
        
