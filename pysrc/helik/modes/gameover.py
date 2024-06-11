#!/usr/bin/env python3

"""
GameOver handler module
"""


import pygame
from helik.modes.standard import Mode
from helik.htypes import BoardType
from helik.hdefs import ARENA_WIDTH, ARENA_HEIGHT


class ModeGameOver(Mode):
    """
    GaneOver handler class
    """
    def __init__(self, parent):
        """
        Create GameOver instance
        """
        super().__init__(parent)

    def on_paint(self):
        """
        Paint event handler
        """
        self.buffer.blit(self.resman.images["default-background"], (0, 0))
        l, r = self.resman.labels[self.arena.config['lang']]["game"]["gameover"]
        r.x = (ARENA_WIDTH - r.w) // 2
        r.y = (ARENA_HEIGHT -r.h) // 2
        self.buffer.blit(l, r)
        l, r = self.resman.labels[self.arena.config['lang']]["game"]["gameover-2"]
        r.x = (ARENA_WIDTH - r.w) // 2
        r.y = (ARENA_HEIGHT - r.h) // 2 + 70
        self.buffer.blit(l, r)

    def on_keyup(self, key):
        """
        Key release event handler
        :param key: key code
        """
        # self.game.arena.change_board(BoardType.HISCORES)
        if self.arena.config.is_hiscore(self.game.data['points']):
            self.game.arena.change_board(BoardType.NEWSCORE)
        else:
            self.game.arena.change_board(BoardType.HISCORES)

    def on_mouseup(self, button, pos):
        """
        Mouse up event handler
        :param button: button number
        :param pos: cursor position
        """
        self.on_keyup(pygame.K_RETURN)
