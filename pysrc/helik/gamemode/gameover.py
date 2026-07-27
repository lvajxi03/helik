#!/usr/bin/env python3

"""
GameOver handler module
"""


import pygame
from helik.datatypes import BoardType
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

        la = self.resman["game"]["gameover-shadow"]
        la.paint_at(self.buffer, (ARENA_WIDTH - la.w) // 2 + 5, (ARENA_HEIGHT - la.h) // 2 + 5)
        la = self.resman["game"]["gameover"]
        la.paint_at(self.buffer, (ARENA_WIDTH - la.w) // 2, (ARENA_HEIGHT - la.h) // 2)
        la = self.resman["game"]["gameover-2"]
        la.paint_at(self.buffer, (ARENA_WIDTH -la .w) // 2, (ARENA_HEIGHT - la.h) // 2 + 170)

    def on_keyup(self, key):
        """
        Key release event handler
        :param key: key code
        """
        match key:
            case pygame.K_F3:
                self.arena.toggle_lang()
            case pygame.K_ESCAPE:
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
            self.arena.toggle_lang()

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
