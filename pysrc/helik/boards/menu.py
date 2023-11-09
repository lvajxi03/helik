#!/usr/bin/env python3

"""
Menu board handler
"""

import pygame
from helik.boards.standard import Board
from helik.htypes import BoardType
from helik.hdefs import ARENA_WIDTH, ARENA_HEIGHT, STATUS_HEIGHT
from helik.locale import locale


def menupos2board(menu_pos: int) -> BoardType:
    """
    Calculate board id from menu pos
    :param menu_pos: menu position number
    :return: board id
    """
    ids = [BoardType.GAME, BoardType.OPTIONS, BoardType.HISCORES,
           BoardType.SETTINGS, BoardType.HELP, BoardType.ABOUT,
           BoardType.QUIT]
    try:
        return ids[menu_pos]
    except IndexError:
        return BoardType.QUIT # Because, erm, why not? ;)


class BoardMenu(Board):
    """
    Menu board
    """
    def __init__(self, parent):
        super().__init__(parent)
        self.locale = locale[BoardType.MENU]
        self.menu_pos = 0
        self.rect_pos = None
        self.rect_pos_t = None
        self.color = pygame.Color(76, 76, 76)
        self.rectangles = []
        self.create_rectangles()

    def recalculate_pos(self):
        """
        Re-calculate current selection rectangle
        """
        _, self.rect_pos = self.rectangles[self.menu_pos]
        self.rect_pos = self.rect_pos.inflate(40, 40)

    def create_rectangles(self):
        """
        Create labels and rectangles based on locale
        """
        self.rectangles = []
        i = 0
        elems = self.res_man.get_label(BoardType.MENU, "menu", self.arena.config['lang'])
        for elem in elems:
            label, rect = elem
            rect.left = 400
            rect.top = 100 + i * 80
            self.rectangles.append((label, rect))
            i += 1
        self.recalculate_pos()

    def on_paint(self):
        """
        Paint event handler
        """
        self.buffer.blit(self.res_man.images["default-background"], (0, 0))
        self.buffer.blit(self.res_man.surfaces["status"], (0, ARENA_HEIGHT - STATUS_HEIGHT))
        self.buffer.blit(self.res_man.images["pl-status-1"],
                         ((ARENA_WIDTH - 892 - 160) // 2, ARENA_HEIGHT - 50))

        # Lang flags
        self.buffer.blit(self.res_man.images["flag-pl"], self.res_man.get("lang-rectangles", "pl"))
        self.buffer.blit(self.res_man.images["flag-en"], self.res_man.get("lang-rectangles", "en"))

        self.buffer.blit(self.res_man.images["helik-main"], (215, 45))

        for re in self.rectangles:
            label, rect = re
            self.buffer.blit(label, rect)
        self.rect_pos_t = self.rect_pos.move(5, 5)
        pygame.draw.rect(self.buffer, pygame.Color(16, 16, 16),
                         self.rect_pos_t, width=5, border_radius=20)
        pygame.draw.rect(self.buffer, pygame.Color(207, 229, 32),
                         self.rect_pos, width=5, border_radius=20)

    def activate(self):
        """
        Activate board event handler
        """
        self.create_rectangles()

    def on_keyup(self, key):
        """
        Key release event handler
        :param key: key code
        """
        if key == pygame.K_DOWN:
            if self.menu_pos < 6:
                self.audio.play_sound("arrow")
                self.menu_pos += 1
        elif key == pygame.K_UP:
            if self.menu_pos > 0:
                self.menu_pos -= 1
                self.audio.play_sound("arrow")
        elif key == pygame.K_RETURN:
            bid = menupos2board(self.menu_pos)
            self.audio.play_sound("closing-tape")
            self.arena.change_board(bid)
        elif key == pygame.K_q:
            self.arena.change_board(BoardType.QUIT)
        self.recalculate_pos()

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
                    self.audio.play_sound("arrow")
                    self.create_rectangles()
        if not ch_lang:
            # TODO
            pass
