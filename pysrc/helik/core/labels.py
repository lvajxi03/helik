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
        """
        :param label: a string to display
        :param font: Pygame font definition
        :param color: Pygame color description
        :param x: top-left x coordinate
        :param y: top-left y coordinate
        :param rotate: how to rotate the label (in degrees)
        """
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
        """
        Top-left x coordinate
        :return: top-left x coordinate
        """
        return self._x

    @x.setter
    def x(self, value: int):
        """
        Top-left x coordinate
        :param value: new x coordinate value
        """
        self._x = value
        self.r.x = value

    @property
    def y(self):
        """
        Top-left y coordinate
        :return: top-left y coordinate
        """
        return self._y

    @y.setter
    def y(self, value: int):
        """
        Top-left y coordinate
        :param value: new y coordinate value
        """
        self._y = value
        self.r.y = value

    @property
    def w(self):
        """
        Label width
        :return: label width
        """
        return self._w

    @w.setter
    def w(self, value: int):
        """
        Label width
        :return: label width
        """
        self._w = value
        self.r.w = value

    @property
    def h(self):
        """
        Label height
        :return: label height
        """
        return self._h

    @h.setter
    def h(self, value: int):
        """
        Label height
        :return: label height
        """
        self._h = value
        self.r.h = value

    def move(self, newx: int, newy: int):
        """
        Set new label location
        :param newx: new top-left x coordinate
        :param newy: new top-left y coordinate
        """
        self._x = newx
        self._y = newy
        self.r.x = newx
        self.r.y = newy

    def center(self, spot_x: int, spot_y: int):
        """
        Set new label center (spot)
        :param spot_x: new center x coordinate
        :param spot_y: new center y coordinate
        """
        self._x = spot_x - self.r.w // 2
        self._y = spot_y - self.r.h // 2
        self.r.x = self._x
        self.r.y = self._y

    def paint(self, canvas):
        """
        Paint the label
        :param canvas: where to paint
        """
        canvas.blit(self.surface, (self._x, self._y))

    def paint_at(self, canvas, x, y):
        """
        Paint the label at the given location
        :param canvas: where to paint
        :param x: top-left x coordinate
        :param y: top-left y coordinate
        """
        canvas.blit(self.surface, (x, y))

    def set_alpha(self, newalpha: int):
        """
        Set label's alpha value
        :param newalpha: new alpha value
        """
        self.surface.set_alpha(newalpha)
