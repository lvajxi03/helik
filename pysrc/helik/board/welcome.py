#!/usr/bin/env python3

"""
Welcome board handler
"""

import random
import pygame
from helik.platform import TimerType
from helik.hdefs import ARENA_WIDTH, ARENA_HEIGHT
from helik.datatypes import BoardType
from .standard import Board


class BoardWelcome(Board):
    """
    Welcome board
    """
    def __init__(self, parent):
        super().__init__(parent)
        self.animation_interval = 50
        self.animation_timer = 0
        self.board_timer = 0
        self.board_timeout = 5000

        self.rectangles = []
        self.colors = []
        for i in range (0, ARENA_WIDTH // 40):
            self.rectangles.append(
                pygame.Rect(i * 40, 0, 40, ARENA_HEIGHT))
            comp = random.randint(64, 255)
            self.colors.append(
                pygame.Color(comp, comp, comp))

    def activate(self, **kwargs):
        """
        Activate event handler
        :param kwargs: additional parameters, like help or previous board
        """
        self.animation_timer = self.animation_interval
        self.board_timer = 0

    def on_update(self, delta):
        """
        Update event handler
        :param delta: delta time from last frame
        """
        self.animation_timer += delta
        self.board_timer += delta
        while self.animation_timer >= self.animation_interval:
            self.animation_timer -= self.animation_interval
            self.shuffle_colors()

        if self.board_timer >= self.board_timeout:
            self.arena.change_board(BoardType.MENU)

    def deactivate(self):
        """
        Board deactivate handler
        """
        pygame.time.set_timer(TimerType.FIRST, 0)

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

    def on_mouseup(self, button, pos):
        """
        Mouse up event handler
        :param button: button number
        :param pos: cursor position
        """
        self.arena.change_board(BoardType.MENU)

    def on_joyaxismotion(self, axis, value):
        self.arena.change_board(BoardType.MENU)

    def on_joybuttonup(self, button):
        self.arena.change_board(BoardType.MENU)
