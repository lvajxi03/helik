#!/usr/bin/env python3

"""
Mode paused handler module
"""


import pygame
from helik.htypes import GameType, BoardType
from helik.hdefs import ARENA_WIDTH, ARENA_HEIGHT
from helik.modes.standard import Mode


class ModePaused(Mode):
    """
    Mode paused handle class
    """
    def __init__(self, parent):
        """
        Mode paused class constructor
        """
        super().__init__(parent)

    def on_paint(self):
        """
        Paint event handler
        """
        self.res_man.get("surfaces", "buffer").blit(
            self.res_man.get(
                "images", "default-background"), (0, 0))
        label, rect = self.res_man.get_label(BoardType.GAME, "paused-shadow", "pl")
        rect.center = (ARENA_WIDTH // 2, ARENA_HEIGHT // 2)
        rect.x += 5
        rect.y += 5
        self.res_man.get("surfaces", "buffer").blit(label, rect)
        label, rect = self.res_man.get_label(BoardType.GAME, "paused", "pl")
        rect.center = (ARENA_WIDTH // 2, ARENA_HEIGHT // 2)
        self.res_man.get("surfaces", "buffer").blit(label, rect)
        label, rect = self.res_man.get_label(BoardType.GAME, "continue", "pl")
        rect.center = (ARENA_WIDTH // 2, ARENA_HEIGHT // 2)
        rect.y += 100
        self.res_man.get("surfaces", "buffer").blit(label, rect)

    def on_keyup(self, key):
        """
        Key release event handler
        :param key: key code
        """
        if key == pygame.K_SPACE:
            self.game.change_mode(GameType.PLAY)
