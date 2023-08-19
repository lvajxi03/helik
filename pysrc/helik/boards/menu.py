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
        random.seed()
        font = pygame.font.Font('freesansbold.ttf', 256)
        self.text1 = pygame.transform.rotate(font.render('HeliK!', True, pygame.Color(0, 0, 0, a=129)), 90)
        self.text2 = pygame.transform.rotate(font.render('HeliK!', True, pygame.Color(255, 128, 64, a=192)), 90)
        self.r1 = self.text1.get_rect()
        self.r1.left, self.r1.top = 10, 10
        self.r2 = self.text2.get_rect()
        self.r2.left, self.r2.top = 15, 15        
        self.color = pygame.Color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        pygame.time.set_timer(TimerType.WELCOME, 200)

    def on_paint(self):
        """
        Paint event handler
        """
        self.screen.fill(self.color)
        self.parent.screen.blit(self.text1, self.r1)
        self.parent.screen.blit(self.text2, self.r2)

    def on_timer(self, timer):
        """
        Handle timer event(s)
        """
        if timer == TimerType.WELCOME:
            self.generate_color()
            

    def on_activate(self):
        """
        """

    def on_deactivate(self):
        """
        """

    def generate_color(self):
        """
        Temporary.
        """
        self.color = pygame.Color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
