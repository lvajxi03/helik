#!/usr/bin/env python3

"""
Menu board handler
"""

import random
import pygame
from helik.boards.standard import Board
from helik.htypes import TimerType, BoardType
from helik.hdefs import ARENA_WIDTH, ARENA_HEIGHT, STATUS_HEIGHT
from helik.locale import locale
from helik.utils import menupos2board

class BoardMenu(Board):
    """
    Menu board
    """
    def __init__(self, parent):
        super().__init__(parent)
        self.locale = locale[BoardType.MENU]
        self.menu_pos = 0
        self.rect_pos = None
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

        # Lang flags
        self.buffer.blit(self.res_man.images["flag-pl"], self.res_man.get("lang-rectangles", "pl"))
        self.buffer.blit(self.res_man.images["flag-en"], self.res_man.get("lang-rectangles", "en"))

        label, rect = self.res_man.get_label(BoardType.MENU, "title_shadow", self.arena.config['lang'])
        self.buffer.blit(label, (225, 55))
        label, rect = self.res_man.get_label(BoardType.MENU, "title", self.arena.config['lang'])
        self.buffer.blit(label, (220, 50))
        
        for re in self.rectangles:
            label, rect = re
            self.buffer.blit(label, rect)
        self.rect_pos_t = self.rect_pos.move(5, 5)
        pygame.draw.rect(self.buffer, pygame.Color(16, 16, 16), self.rect_pos_t, width=5, border_radius=20)
        pygame.draw.rect(self.buffer, pygame.Color(207, 229, 32), self.rect_pos, width=5, border_radius=20)

    def on_timer(self, timer):
        """
        Handle timer event(s)
        """

    def activate(self):
        """
        Activate board event handler
        """
        self.create_rectangles()

    def deactivate(self):
        """
        """

    def on_keyup(self, key):
        """
        Key release event handler
        :param key: key code
        """
        if key == pygame.K_DOWN:
            if self.menu_pos < 6:
                self.menu_pos += 1
        elif key == pygame.K_UP:
            if self.menu_pos > 0:
                self.menu_pos -= 1
        elif key == pygame.K_RETURN:
            bid = menupos2board(self.menu_pos)
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
                    self.create_rectangles()
        if not ch_lang:
            # TODO
            pass
