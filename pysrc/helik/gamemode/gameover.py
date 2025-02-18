#!/usr/bin/env python3

"""
GameOver handler module
"""


import pygame
from helik.types import BoardType
from helik.hdefs import ARENA_WIDTH, ARENA_HEIGHT
from helik.platform import ButtonType
from .standard import Mode


class ModeGameOver(Mode):
    """
    GaneOver handler class
    """
    def on_paint(self):
        """
        Paint event handler
        """
        self.buffer.blit(self.resman.images["default-background"], (0, 0))

        l, r = self.resman["game"]["gameover-shadow"]
        r.x = (ARENA_WIDTH - r.w) // 2 + 5
        r.y = (ARENA_HEIGHT - r.h) // 2 + 5
        self.buffer.blit(l, r)
        l, r = self.resman["game"]["gameover"]
        r.x = (ARENA_WIDTH - r.w) // 2
        r.y = (ARENA_HEIGHT -r.h) // 2
        self.buffer.blit(l, r)
        l, r = self.resman["game"]["gameover-2"]
        r.x = (ARENA_WIDTH - r.w) // 2
        r.y = (ARENA_HEIGHT - r.h) // 2 + 170
        self.buffer.blit(l, r)

    def on_keyup(self, key):
        """
        Key release event handler
        :param key: key code
        """
        if key == pygame.K_F3:
            self.arena.config.toggle_lang()
        elif key == pygame.K_ESCAPE:
            if self.arena.config.is_hiscore(self.game.data['points']):
                self.game.arena.change_board(BoardType.NEWSCORE)
            else:
                self.game.arena.change_board(BoardType.HISCORES)

    def on_joybuttonup(self, button):
        """
        Joy Button Up event handler
        :param button: button number
        """
        if button == ButtonType.B:
            self.arena.config.toggle_lang()

    def on_joyaxismotion(self, axis, value):
        """
        Joy Axis Motion event handler
        :param axis: axis number
        :param value: axis value
        """
        if self.arena.config.is_hiscore(self.game.data['points']):
            self.game.arena.change_board(BoardType.NEWSCORE)
        else:
            self.game.arena.change_board(BoardType.HISCORES)
