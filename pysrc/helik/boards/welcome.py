#!/usr/bin/env python3

"""
Welcome board handler
"""

import random
import pygame
from helik.boards.standard import Board
from helik.htypes import TimerType
from helik.hdefs import ARENA_WIDTH, ARENA_HEIGHT


class BoardWelcome(Board):
    """
    Welcome board
    """
    def __init__(self, parent):
        super().__init__(parent)
        self.rectangles = []
        self.colors = []
        for i in range (0, ARENA_WIDTH // 40):
            self.rectangles.append(
                pygame.Rect(i * 40, 0, 40, ARENA_HEIGHT))
            comp = random.randint(64, 255)
            self.colors.append(
                pygame.Color(comp, comp, comp))
        pygame.time.set_timer(TimerType.WELCOME, 100)

    def on_paint(self):
        """
        Paint event handler
        """
        for i in range(0, ARENA_WIDTH // 40):
            pygame.draw.rect(self.buffer,
                             self.colors[i],
                             self.rectangles[i])

    def on_timer(self, timer):
        """
        Handle timer event(s)
        """
        if timer == TimerType.WELCOME:
            self.generate_colors()

    def generate_colors(self):
        """
        Re-generate welcome screen colors
        """
        for i in range(0, ARENA_WIDTH // 40):
            comp = random.randint(64, 255)
            self.colors[i] = pygame.Color(comp, comp, comp)
            
