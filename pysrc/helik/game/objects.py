#!/usr/bin/env python3

"""
Game objects
"""


import enum
import pygame
from helik.htypes import TimerType
from helik.hdefs import ARENA_WIDTH, ARENA_HEIGHT


@enum.unique
class CopterDirection(enum.IntEnum):
    """
    Copter direction enum
    """
    LEFT = 0
    RIGHT = 1


class Copter:
    """
    Copter player class
    """
    def __init__(self, parent):
        self.parent = parent
        self.res_man = parent.parent.res_man
        self.x = 200
        self.y = 200
        self.direction = CopterDirection.RIGHT

    def on_paint(self):
        """
        Paint event handler
        """
        if self.direction == CopterDirection.RIGHT:
            self.res_man.get("surfaces", "buffer").blit(
                self.res_man.get("images", "helik-small-right"), (self.x, self.y))
        else:
            self.res_man.get("surfaces", "buffer").blit(
                self.res_man.get("images", "helik-small-left"), (self.x, self.y))

    def on_keyup(self, key):
        """
        Key release event handler
        :param key: key code
        """
        if key == pygame.K_LEFT:
            self.direction = CopterDirection.LEFT
        elif key == pygame.K_RIGHT:
            self.direction = CopterDirection.RIGHT
        elif key == pygame.K_SPACE:
            if self.y > 30:
                self.y -= 30

    def on_timer(self, timer):
        """
        Timer event handler
        """
        if timer == TimerType.PLAY_MOVE:
            if self.y <= ARENA_HEIGHT-60:
                self.y += 1
            else:
                # TODO
                self.y = -30
