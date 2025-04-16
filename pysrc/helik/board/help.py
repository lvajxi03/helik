#!/usr/bin/env python3

"""
Help board handler
"""


import pygame
from helik.datatypes import BoardType
from helik.hdefs import ARENA_HEIGHT, ARENA_WIDTH
from helik.core.pages import Pager
from helik.platform import ButtonType, AxisType, AxisValue
from .standard import Board


class BoardHelp(Board):
    """
    Help board class
    """
    def __init__(self, parent):
        super().__init__(parent)
        self.pager = Pager(self.resman.pages["help"], self.resman)

    def activate(self, **kwargs):
        """
        Activate event handler
        :param kwargs: additional parameters, like previous board or help
        """
        self.pager.change_lang(self.arena.config["lang"])
        self.pager.activate()

        if 'help' in kwargs:
            self.pager.activate(kwargs['help'])

    def on_paint(self):
        """
        Paint event handler
        """
        self.paint_default_bg()
        self.paint_default_title("help")

        self.pager.on_paint(self.buffer)

        if self.pager.has_next() and self.pager.has_prev():
            la = self.resman["pager-status-full"]
            la.paint_at(self.buffer, ARENA_WIDTH - la.w - 200, ARENA_HEIGHT - 55)
        elif self.pager.has_next():
            la = self.resman["pager-status-next"]
            la.paint_at(self.buffer, ARENA_WIDTH - la.w - 200, ARENA_HEIGHT - 55)
        elif self.pager.has_prev():
            la = self.resman["pager-status-prev"]
            la.paint_at(self.buffer, ARENA_WIDTH - la.w - 200, ARENA_HEIGHT - 55)
        else:
            la = self.resman["pager-status-none"]
            la.paint_at(self.buffer, ARENA_WIDTH - la.w - 200, ARENA_HEIGHT - 55)

    def on_keyup(self, key):
        """
        Key release event handler
        Key code does not matter. Always return to main menu
        :param key: any key pressed
        """
        match key:
            case pygame.K_ESCAPE:
                self.arena.change_board(BoardType.MENU)
            case pygame.K_LEFT:
                self.pager.prev()
            case pygame.K_F3:
                self.arena.toggle_lang()
                self.pager.change_lang(self.arena.config["lang"])
            case pygame.K_RIGHT:
                self.pager.next()

    def on_mouseup(self, button, pos):
        """
        Mouse up event handler
        :param button: button number
        :param pos: cursor position
        """
        ch_lang = False
        match button:
            case 1:
                rects = self.resman.rectangles["lang-rectangles"]
                for lang in rects:
                    if rects[lang].collidepoint(pos):
                        self.arena.set_lang(lang)
                        self.pager.change_lang(lang)
                        ch_lang = True
                if not ch_lang:
                    if not self.pager.on_click():
                        self.pager.next()
            case 5:
                self.pager.next()
            case 4:
                self.pager.prev()

    def on_joybuttonup(self, button):
        """
        Joy Button Up event handler
        :param button: button number
        """
        match button:
            case ButtonType.B:
                self.arena.toggle_lang()
                self.pager.change_lang(self.arena.config["lang"])
            case ButtonType.A:
                self.arena.change_board(BoardType.MENU)

    def on_joyaxismotion(self, axis, value):
        """
        Joy Axis Motion event handler
        :param axis: axis number
        :param value: axis value
        """
        if axis == AxisType.HORIZ:
            if value == AxisValue.LOWER:
                self.pager.prev()
            elif value == AxisValue.HIGHER:
                self.pager.next()
