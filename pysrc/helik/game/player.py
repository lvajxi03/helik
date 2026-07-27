#!/usr/bin/env python3

"""
Copter handler module
"""

import enum
import pygame
from helik.hdefs import ARENA_HEIGHT, STATUS_HEIGHT, JUMP


@enum.unique
class PlayerDirection(enum.IntEnum):
    """
    Player direction enum
    """
    DOWN = 0
    UP = 1


class Player:
    """
    Copter player class
    """
    def __init__(self, game, index: int):
        self.game = game
        self.direction = PlayerDirection.DOWN
        self.arena = game.arena
        self.resman = self.game.arena.resman
        self.buffer = game.buffer
        self.images = [self.resman.images["vehicles"][2 * index],
                       self.resman.images["vehicles"][2 * index + 1]]
        self.masks = [pygame.mask.from_surface(self.images[0]),
                      pygame.mask.from_surface(self.images[1])]
        self.mask = self.masks[self.direction]
        self.x, self.y = 200, 200
        r = self.images[self.direction].get_rect()
        self.w, self.h = r.w, r.h
        self.jump = JUMP[self.arena.config['option']]

    def toggle_direction(self):
        """
        Toggle copter direction.
        Happens every time a dir changer pill was consumed
        """
        if self.direction == PlayerDirection.DOWN:
            self.direction = PlayerDirection.UP
        else:
            self.direction = PlayerDirection.DOWN

        r = self.images[self.direction].get_rect()
        self.mask = self.masks[self.direction]
        self.w, self.h = r.w, r.h

    def on_paint(self):
        """
        Paint event handler
        """
        self.buffer.blit(self.images[self.direction], (self.x, self.y))

    def on_jump(self):
        """
        Jump event
        """
        if self.direction == PlayerDirection.DOWN:
            self.y -= self.jump
        else:
            self.y += self.jump

    def move(self, delta) -> bool:
        """
        Move the copter
        :param delta: delta time from last frame
        :return: True if collided to top or bottom, False otherwise
        """
        if self.direction == PlayerDirection.DOWN:
            if self.y < ARENA_HEIGHT - STATUS_HEIGHT:
                self.y += 1
            else:
                return True
        else:
            if self.y > 0:
                self.y -= 1
            else:
                return True
        return False
