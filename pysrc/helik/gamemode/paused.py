#!/usr/bin/env python3

"""
Mode paused handler module
"""


import pygame
from helik.hdefs import ARENA_WIDTH, ARENA_HEIGHT
from helik.platform import ButtonType
from .standard import Mode
from .types import GameMode


class ModePaused(Mode):
    """
    Mode paused handle class
    """
    def on_paint(self):
        """
        Paint event handler
        """
        self.buffer.blit(self.resman.images["default-background"], (0, 0))
        im = self.resman["game"]["paused-shadow"]
        im.paint_at(self.buffer, (ARENA_WIDTH - im.w) // 2 + 5,
                    (ARENA_HEIGHT // 2 - im.h) // 2 + 5)
        im = self.resman["game"]["paused"]
        im.paint_at(self.buffer, (ARENA_WIDTH - im.w) // 2,
                    (ARENA_HEIGHT // 2 - im.h) // 2)
        im = self.resman["game"]["continue"]
        im.paint_at(self.buffer, (ARENA_WIDTH - im.w) // 2,
                    (3 * ARENA_HEIGHT // 2 - im.h) // 2)

    def on_keyup(self, key):
        """
        Key release event handler
        :param key: key code
        """
        if key == pygame.K_ESCAPE:
            self.game.change_mode(GameMode.PLAY)

    def on_joybuttonup(self, button):
        """
        Joy Button Up event handler
        :param button: button number
        """
        if button == ButtonType.START:
            self.on_keyup(pygame.K_ESCAPE)

    def on_mouseup(self, button, pos):
        """
        Mouse up event handler
        :param button: button number
        :param pos: cursor position
        """
        if button == 1:
            self.on_keyup(pygame.K_SPACE)
