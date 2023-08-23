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

class BoardMenu(Board):
    """
    Menu board
    """
    def __init__(self, parent):
        super().__init__(parent)
        self.locale = locale[BoardType.MENU]
        self.fonts = {
            "heading": pygame.font.Font('ehs.ttf', 164),
            "menu": pygame.font.Font('ehs.ttf', 48)
            } 
        self.text1 = pygame.transform.rotate(self.fonts["heading"].render('HeliK!', True, pygame.Color(0, 0, 0, a=128)), 90)
        self.text2 = pygame.transform.rotate(self.fonts["heading"].render('HeliK!', True, pygame.Color(224, 223, 74, a=128)), 90)
        self.menu_pos = 0
        self.rect_pos = None
        self.r1 = self.text1.get_rect()
        self.r1.left, self.r1.top = 210, 40
        self.r2 = self.text2.get_rect()
        self.r2.left, self.r2.top = 215, 45        
        self.color = pygame.Color(76, 76, 76)
        self.rectangles = []
        self.create_rectangles()
        self.status = pygame.Rect(0, ARENA_HEIGHT - 60, ARENA_WIDTH, 60)
        self.status_color = pygame.Color(64, 64, 64, 128)

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
        for pos in self.locale["menu"][self.parent.lang]:
            label = self.fonts["menu"].render(pos, True, pygame.Color(224, 224, 224, a=255))
            rect = label.get_rect()
            rect.left = 400
            rect.top = 100 + i * 80
            self.rectangles.append((label, rect))
            i += 1
        self.recalculate_pos()
        
    def on_paint(self):
        """
        Paint event handler
        """
        self.buffer.blit(self.resources["images"]["default-background"], (0, 0))
        pygame.draw.rect(self.buffer, self.status_color, self.status)
        self.buffer.blit(self.text1, self.r1)
        self.buffer.blit(self.text2, self.r2)
        for re in self.rectangles:
            label, rect = re
            self.buffer.blit(label, rect)
        self.rect_pos_t = self.rect_pos.move(5, 5)
        pygame.draw.rect(self.buffer, pygame.Color(48, 48, 48), self.rect_pos_t, width=5, border_radius=20)
        pygame.draw.rect(self.buffer, pygame.Color(207, 229, 32), self.rect_pos, width=5, border_radius=20)

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

    def on_keydown(self, key):
        """
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
            if self.menu_pos == 6:
                self.parent.running = False
        self.recalculate_pos()
