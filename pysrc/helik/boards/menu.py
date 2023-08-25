#!/usr/bin/env python3

"""
Menu board handler
"""

import random
import pygame
from helik.boards.standard import Board
from helik.htypes import TimerType, BoardType
from helik.hdefs import ARENA_WIDTH, ARENA_HEIGHT
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
        self.status = pygame.Rect(0, 0, ARENA_WIDTH, 60)
        self.status_color = pygame.Color(128, 128, 128, 128)

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
        elems = self.res_man.get_label(BoardType.MENU, "menu", self.parent.lang)
        for elem in elems:
            label, rect = elem
            rect.left = 400
            rect.top = 100 + i * 80
            self.rectangles.append((label, rect))
            i += 1

        # for pos in self.locale["menu"][self.parent.lang]:
        #     label, rect = self.
        #     label = self.res_man.get("fonts", "menu").render(pos, True, pygame.Color(224, 224, 224, a=255))
        #     rect = label.get_rect()
        #     rect.left = 400
        #     rect.top = 100 + i * 80
        #     self.rectangles.append((label, rect))
        #     i += 1
        self.recalculate_pos()
        
    def on_paint(self):
        """
        Paint event handler
        """
        self.res_man.get("surfaces", "buffer").blit(self.res_man.get("images", "default-background"), (0, 0))
        pygame.draw.rect(self.res_man.get("surfaces", "status"), self.status_color, self.status)
        self.res_man.get("surfaces", "buffer").blit(self.res_man.get("surfaces", "status"), (0, ARENA_HEIGHT - 60))
        label, rect = self.res_man.get_label(BoardType.MENU, "title_shadow", "pl")
        self.res_man.get("surfaces", "buffer").blit(label, (225, 55))
        label, rect = self.res_man.get_label(BoardType.MENU, "title", "pl")
        self.res_man.get("surfaces", "buffer").blit(label, (220, 50))
        
        for re in self.rectangles:
            label, rect = re
            self.res_man.get("surfaces", "buffer").blit(label, rect)
        self.rect_pos_t = self.rect_pos.move(5, 5)
        pygame.draw.rect(self.res_man.get("surfaces", "buffer"), pygame.Color(16, 16, 16), self.rect_pos_t, width=5, border_radius=20)
        pygame.draw.rect(self.res_man.get("surfaces", "buffer"), pygame.Color(207, 229, 32), self.rect_pos, width=5, border_radius=20)

    def on_timer(self, timer):
        """
        Handle timer event(s)
        """

    def activate(self):
        """
        """

    def deactivate(self):
        """
        """

    def on_keyup(self, key):
        """
        Key release event handler
        :param key: kedy code
        """
        if key == pygame.K_DOWN:
            if self.menu_pos < 6:
                self.menu_pos += 1
            else:
                self.menu_pos = 0
        elif key == pygame.K_UP:
            if self.menu_pos > 0:
                self.menu_pos -= 1
            else:
                self.menu_pos = 6
        elif key == pygame.K_RETURN:
            bid = menupos2board(self.menu_pos)
            self.parent.change_board(bid)
        elif key == pygame.K_q:
            self.parent.change_board(BoardType.QUIT)
        self.recalculate_pos()
