#!/usr/bin/env python3

"""
Copter handler module
"""

import enum
import pygame
from helik.hdefs import ARENA_HEIGHT, STATUS_HEIGHT


@enum.unique
class CopterDirection(enum.IntEnum):
    DOWN = 0
    UP = 1


class Copter:
    """
    Copter player class
    """
    def __init__(self, game):
        self.game = game
        self.direction = CopterDirection.DOWN
        self.arena = game.arena
        self.res_man = self.game.arena.res_man
        self.buffer = game.buffer
        self.image = self.res_man.images["helik-white"]
        self.mask = pygame.mask.from_surface(self.image)
        self.x, self.y = 200, 200
        r = self.image.get_rect()
        self.w, self.h = r.w, r.h

    def on_paint(self):
        """
        Paint event handler
        """
        self.buffer.blit(self.image, (self.x, self.y))

    def on_keyup(self, key):
        """
        Key release event handler
        :param key: key code
        """
        if key == pygame.K_SPACE:
            if self.direction == CopterDirection.DOWN:
                if self.y > 30:
                    self.y -= 30
                elif self.y <= 30:
                    self.y = 0
            else:
                if self.y + self.h < ARENA_HEIGHT - STATUS_HEIGHT - 30:
                    self.y += 30
                elif self.y + self.h >= ARENA_HEIGHT - STATUS_HEIGHT - 30:
                    self.y = ARENA_HEIGHT - STATUS_HEIGHT - self.h

    def on_timer(self, timer):
        """
        Timer event handler
        """
        if timer == TimerType.COPTER:
            if self.direction == CopterDirection.DOWN:
                if self.y < ARENA_HEIGHT - STATUS_HEIGHT:
                    self.y += 1
                else:
                    # TODO: collision!
                    pass
            else:
                if self.y > 0:
                    self.y -= 1
                else:
                    # TODO: collision!
                    pass

    def on_update(self, delta):
        """
        TODO
        """
        pass
