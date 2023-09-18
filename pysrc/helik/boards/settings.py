#!/usr/bin/env python3

"""
Settings board handler
"""

import pygame
from helik.boards.standard import Board
from helik.hdefs import ARENA_WIDTH, ARENA_HEIGHT
from helik.htypes import BoardType

class BoardSettings(Board):
    """
    Settings board class
    """
    def __init__(self, parent):
        super().__init__(parent)

    def on_paint(self):
        """
        Paint event handler
        """
        self.buffer.blit(self.res_man.images["default-background"], (0, 0))
        self.buffer.blit(self.res_man.get("surfaces", "status"), (0, ARENA_HEIGHT - 60))

        # Lang flags
        self.buffer.blit(self.res_man.images["flag-pl"], self.res_man.get("lang-rectangles", "pl"))
        self.buffer.blit(self.res_man.images["flag-en"], self.res_man.get("lang-rectangles", "en"))

        l, r = self.res_man.get_label(BoardType.SETTINGS, "title-shadow", self.arena.lang)
        self.buffer.blit(l, (55, 45))
        l, r = self.res_man.get_label(BoardType.SETTINGS, "title", self.arena.lang)
        self.buffer.blit(l, (50, 50))

    def activate(self):
        """
        """

    def deactivate(self):
        """
        """

    def on_keyup(self, key):
        """
        # TODO
        Key release event handler
        Key code does not matter. Always return to main menu
        :param key: any key pressed
        """
        self.arena.change_board(BoardType.MENU)

    def on_mouseup(self, button, pos):
        """
        Mouse up event handler
        :param button: button number
        :param pos: cursor position
        """
        ch_lang = False
        if button == 1:
            rects = self.res_man.get_section("lang-rectangles")
            for lang in rects:
                if rects[lang].collidepoint(pos):
                    self.arena.lang = lang
                    ch_lang = True
        if not ch_lang:
            # TODO: settings-related ops here
            self.arena.change_board(BoardType.MENU)
