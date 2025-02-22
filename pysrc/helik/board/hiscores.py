#!/usr/bin/env python3

"""
Hiscores board handler
"""


import pygame
from helik.platform import AxisType, AxisValue, ButtonType
from helik.datatypes import BoardType
from .standard import Board


SCORES_DX = 200
SCORES_DY = 90

SCORES_DY_SPACE = 65

SHADOW_DX = 5
SHADOW_DY = 5


class BoardHiscores(Board):
    """
    Hiscores board class
    """
    def __init__(self, parent):
        """
        Hiscores board class constructor
        """
        super().__init__(parent)
        self.rectangles = []
        self.rectangles_s = []

    def activate(self, **kwargs):
        """
        Activate event handler
        :param kwargs: additional parameters, like help or previous board
        """
        self.arena.audio.enable_background_music("background-music")
        self.rectangles = []
        self.rectangles_s = []
        dl = 0
        try:
            _, po = self.arena.config["hiscores"][0]
            dl = len(f"{po}")
        except IndexError:
            pass
        for i in range(0, 10):
            try:
                nick, points = self.arena.config["hiscores"][i]
                self.rectangles.append(self.resman.fonts["menu"].render(
                    f"{i+1: >2}. {points: >{dl}} {nick}",
                    True,
                    self.resman.colors["snowy-white"]))
                self.rectangles_s.append(self.resman.fonts["menu"].render(
                    f"{i+1: >2}. {points: >{dl}} {nick}",
                    True,
                    self.resman.colors["shadow-default"]))
            except IndexError:
                self.rectangles.append(self.resman.fonts["menu"].render(
                    f"{i+1: >2}.",
                    True,
                    self.resman.colors["snowy-white"]))
                self.rectangles_s.append(self.resman.fonts["menu"].render(
                    f"{i+1: >2}.",
                    True,
                    self.resman.colors["shadow-default"]))

    def on_paint(self):
        """
        Paint event handler
        """
        self.paint_default_bg()
        self.paint_default_title("hiscores")
        self.paint_default_status()

        if len(self.arena.config['hiscores']) == 0:
            pass
        else:
            for i in range(0, 10):
                self.buffer.blit(self.rectangles_s[i],
                           (SCORES_DX + SHADOW_DX, SCORES_DY + SHADOW_DY + i * SCORES_DY_SPACE))
                self.buffer.blit(self.rectangles[i],
                           (SCORES_DX, SCORES_DY + i * SCORES_DY_SPACE))

    def on_keyup(self, key):
        """
        Key release event handler
        Key code does not matter. Always return to main menu
        :param key: any key pressed
        """
        match key:
            case pygame.K_F1:
                self.arena.change_board(BoardType.HELP, help=BoardType.HISCORES)
            case pygame.K_F3:
                self.arena.toggle_lang()
            case pygame.K_ESCAPE:
                self.arena.change_board(BoardType.MENU)

    def on_mouseup(self, button, pos):
        """
        Mouse up event handler
        :param button: button number
        :param pos: cursor position
        """
        if button == 1:
            rects = self.resman.rectangles["lang-rectangles"]
            for lang in rects:
                if rects[lang].collidepoint(pos):
                    self.arena.set_lang(lang)

    def on_joyaxismotion(self, axis, value):
        """
        JoyAxisMotion event handler
        :param axis: axis number
        :param value: axis value
        """
        if axis == AxisType.HORIZ and value == AxisValue.LOWER:
            self.arena.change_board(BoardType.MENU)

    def on_joybuttonup(self, button):
        """
        Joy Button Up event handler
        :param button: button number
        """
        if button == ButtonType.B:
            self.arena.toggle_lang()
