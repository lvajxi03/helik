#!/usr/bin/env python3

"""
Mode paused handler module
"""


import pygame
from helik.htypes import GameMode, BoardType
from helik.hdefs import ARENA_WIDTH, ARENA_HEIGHT
from helik.modes.standard import Mode


class ModePaused(Mode):
    """
    Mode paused handle class
    """
    def on_paint(self):
        """
        Paint event handler
        """
        self.buffer.blit(self.res_man.images["default-background"], (0, 0))
        label, rect = self.res_man.get_label(
            BoardType.GAME,
            "paused-shadow",
            self.arena.config['lang'])
        rect.center = (ARENA_WIDTH // 2, ARENA_HEIGHT // 2)
        rect.x += 5
        rect.y += 5
        self.buffer.blit(label, rect)
        label, rect = self.res_man.get_label(BoardType.GAME, "paused", self.arena.config['lang'])
        rect.center = (ARENA_WIDTH // 2, ARENA_HEIGHT // 2)
        self.buffer.blit(label, rect)
        label, rect = self.res_man.get_label(BoardType.GAME, "continue", self.arena.config['lang'])
        rect.center = (ARENA_WIDTH // 2, ARENA_HEIGHT // 2)
        rect.y += 100
        self.buffer.blit(label, rect)

    def on_keyup(self, key):
        """
        Key release event handler
        :param key: key code
        """
        if key == pygame.K_SPACE:
            self.game.change_mode(GameMode.PLAY)
