#!/usr/bin/env python3

"""
Help board handler
"""


from helik.htypes import BoardType
from helik.boards.standard import Board
from helik.hdefs import ARENA_HEIGHT, ARENA_WIDTH


class BoardHelp(Board):
    """
    Help board class
    """
    def on_paint(self):
        """
        Paint event handler
        """
        self.buffer.blit(self.resman.images["default-background"], (0, 0))
        self.buffer.blit(self.resman.surfaces["status"], (0, ARENA_HEIGHT - 60))

        # Lang flags
        self.buffer.blit(self.resman.images["flag-pl"], self.resman.rectangles["lang-rectangles"]["pl"])
        self.buffer.blit(self.resman.images["flag-en"], self.resman.rectangles["lang-rectangles"]["en"])

        l, _ = self.resman.labels[self.arena.config["lang"]]["help"]["help-title"]
        self.buffer.blit(l, (55, 45))

        l, r = self.resman.labels[self.arena.config["lang"]]["general"]["status-line-no-select"]
        self.buffer.blit(l, (ARENA_WIDTH - r.width - 200 , ARENA_HEIGHT - 50))

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
            rects = self.resman.rectangles["lang-rectangles"]
            for lang in rects:
                if rects[lang].collidepoint(pos):
                    self.arena.config['lang'] = lang
                    ch_lang = True
        if not ch_lang:
            self.arena.change_board(BoardType.MENU)
