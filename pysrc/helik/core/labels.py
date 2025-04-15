#!/usr/bin/env python3

"""
Labels module
"""

import pygame


class Label:
    """
    Label representation
    """
    def __init__(self, label: str, font, color, x: int, y: int, rotate: int = 0):
        self._x = x
        self._y = y
        self.surface = pygame.transform.rotate(
            font.render(
                label,
                True,
                color),
            rotate)
        self.surface.set_alpha(color.a)
        self.r = self.surface.get_rect()
        self._w = self.r.w
        self._h = self.r.h

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value: int):
        self._x = value
        self.r.x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value: int):
        self._y = value
        self.r.y = value

    @property
    def w(self):
        return self._w

    @w.setter
    def w(self, value: int):
        self._w = value
        self.r.w = value

    @property
    def h(self):
        return self._h

    @h.setter
    def h(self, value: int):
        self._h = value
        self.r.h = value

    def move(self, newx: int, newy: int):
        self._x = newx
        self._y = newy
        self.r.x = newx
        self.r.y = newy

    def center(self, spot_x: int, spot_y: int):
        self._x = spot_x - self.r.w // 2
        self._y = spot_y - self.r.h // 2
        self.r.x = self._x
        self.r.y = self._y

    def paint(self, canvas):
        canvas.blit(self.surface, (self._x, self._y))

    def paint_at(self, canvas, x, y):
        canvas.blit(self.surface, (x, y))

    def set_alpha(self, newalpha: int):
        self.surface.set_alpha(newalpha)
