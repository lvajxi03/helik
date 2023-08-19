#!/usr/bin/env python3

"""
Menu board handler
"""

import random
import pygame
from helik.boards.standard import Board
from helik.htypes import TimerType


class BoardMenu(Board):
    """
    Menu board
    """
    def __init__(self, parent):
        super().__init__(parent)
        font = pygame.font.Font('freesansbold.ttf', 256)
        self.text1 = pygame.transform.rotate(font.render('HeliK!', True, pygame.Color(0, 0, 0, a=128)), 90)
        self.text2 = pygame.transform.rotate(font.render('HeliK!', True, pygame.Color(224, 223, 74, a=128)), 90)
        self.r1 = self.text1.get_rect()
        self.r1.left, self.r1.top = 10, 10
        self.r2 = self.text2.get_rect()
        self.r2.left, self.r2.top = 15, 15        
        self.color = pygame.Color(219, 219, 219)

    def on_paint(self):
        """
        Paint event handler
        """
        self.buffer.fill(self.color)
        #self.screen.fill(self.color)
        self.buffer.blit(self.text1, self.r1)
        self.buffer.blit(self.text2, self.r2)

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
