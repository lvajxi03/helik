#!/usr/bin/env python3

"""
Welcome board handler
"""

import random
import pygame
from helik.boards.standard import Board
from helik.htypes import TimerType, BoardType
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

    def activate(self):
        pygame.time.set_timer(TimerType.WELCOME_STOP, 3000)

    def on_update(self, delta):
        """
        Update event handler
        :param delta: delta time from last frame
        """
        self.shuffle_colors()

    def deactivate(self):
        """
        Board deactivate handler
        """
        pygame.time.set_timer(TimerType.WELCOME_STOP, 0)

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
        if timer == TimerType.WELCOME_STOP:
            self.arena.change_board(BoardType.MENU)

    def on_keyup(self, key):
        """
        Key release event handler
        :param key: kedy code
        """
        self.arena.change_board(BoardType.MENU)

    def shuffle_colors(self):
        """
        Shuffle welcome screen colors
        """
        c = self.colors.pop(0)
        self.colors.append(c)
        pygame.time.delay(50)
