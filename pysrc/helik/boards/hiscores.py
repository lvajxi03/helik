#!/usr/bin/env python3

"""
Hiscores board handler
"""


from helik.boards.standard import Board
from helik.hdefs import ARENA_HEIGHT
from helik.htypes import BoardType

class BoardHiscores(Board):
    """
    Hiscores board class
    """
    def on_paint(self):
        """
        Paint event handler
        """
        self.buffer.blit(self.res_man.images["default-background"], (0, 0))
        self.buffer.blit(self.res_man.surfaces["status"], (0, ARENA_HEIGHT - 60))

        # Lang flags
        self.buffer.blit(self.res_man.images["flag-pl"], self.res_man.get("lang-rectangles", "pl"))
        self.buffer.blit(self.res_man.images["flag-en"], self.res_man.get("lang-rectangles", "en"))
        l, r = self.res_man.get_label(BoardType.HISCORES, "title-shadow", self.arena.config['lang'])
        self.buffer.blit(l, (55, 45))
        l, r = self.res_man.get_label(BoardType.HISCORES, "title", self.arena.config['lang'])
        self.buffer.blit(l, (50, 50))

    def on_keyup(self, key):
        """
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
                    self.arena.config['lang'] = lang
                    ch_lang = True
                    # TODO: hiscores-related ops here
        if not ch_lang:
            # TODO
            self.arena.change_board(BoardType.MENU)
