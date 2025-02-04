#!/usr/bin/env python3

"""
Mode paused handler module
"""


import pygame
from helik.htypes import GameMode
from helik.hdefs import ARENA_WIDTH, ARENA_HEIGHT
from .standard import Mode


class ModePaused(Mode):
    """
    Mode paused handle class
    """
    def on_paint(self):
        """
        Paint event handler
        """
        self.buffer.blit(self.resman.images["default-background"], (0, 0))
        im, r = self.resman.locale[self.arena.config["lang"]]["game"]["paused-shadow"]
        r.x = (ARENA_WIDTH - r.w ) // 2 + 5
        r.y = (ARENA_HEIGHT // 2 - r.h) // 2 + 5
        self.buffer.blit(im, r)
        im, r = self.resman.locale[self.arena.config["lang"]]["game"]["paused"]
        r.x = (ARENA_WIDTH - r.w ) // 2
        r.y = (ARENA_HEIGHT // 2 - r.h) // 2
        self.buffer.blit(im, r)
        im, r = self.resman.locale[self.arena.config["lang"]]["game"]["continue"]
        r.x = (ARENA_WIDTH - r.w) // 2
        r.y = (3 * ARENA_HEIGHT // 2 - r.h) // 2
        self.buffer.blit(im, r)

    def on_keyup(self, key):
        """
        Key release event handler
        :param key: key code
        """
        if key == pygame.K_SPACE:
            self.game.change_mode(GameMode.PLAY)

    def on_mouseup(self, button, pos):
        """
        Mouse up event handler
        :param button: button number
        :param pos: cursor position
        """
        if button == 1:
            self.on_keyup(pygame.K_SPACE)
