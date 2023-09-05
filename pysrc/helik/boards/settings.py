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
        self.res_man.get("surfaces", "buffer").blit(self.res_man.get("images", "default-background"), (0, 0))
        self.res_man.get("surfaces", "buffer").blit(self.res_man.get("surfaces", "status"), (0, ARENA_HEIGHT - 60))

        # Lang flags
        self.res_man.get("surfaces", "buffer").blit(self.res_man.get("images", "flag-pl"), self.res_man.get("lang-rectangles", "pl"))
        self.res_man.get("surfaces", "buffer").blit(self.res_man.get("images", "flag-en"), self.res_man.get("lang-rectangles", "en"))

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
        self.parent.change_board(BoardType.MENU)

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
                    self.parent.lang = lang
                    ch_lang = True
                    # TODO: settings-related ops here
        if not ch_lang:
            # TODO
            self.parent.change_board(BoardType.MENU)
