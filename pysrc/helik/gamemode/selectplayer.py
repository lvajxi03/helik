#!/usr/bin/env python3

"""
SelectPlayer handler module
"""

import pygame
from helik.datatypes import BoardType, HelpChapter
from helik.game import Player
from helik.hdefs import ARENA_WIDTH, ARENA_HEIGHT
from helik.platform import AxisValue, AxisType, ButtonType
from .standard import Mode
from .types import GameMode


class SelectPlayer(Mode):
    """
    SelectPlayer handler class
    """
    def __init__(self, parent):
        """
        Class constructor
        """
        super().__init__(parent)
        self.viewpos = 0
        self.rects = []
        self.view_x = 0
        self.view_y = 0
        self.vehicles = [self.images["vehicles"][0],
                       self.images["vehicles"][2],
                       self.images["vehicles"][4]]
        x = ARENA_WIDTH // 4
        for image in self.vehicles:
            r = image.get_rect()
            r.center = (x, ARENA_HEIGHT // 2)
            x += ARENA_WIDTH // 4
            self.rects.append(r)

    def on_paint(self):
        """
        Paint event handler
        """
        self.buffer.blit(self.resman.images["default-background"], (0, 0))
        for counter, rx in enumerate(self.rects):
            self.buffer.blit(self.vehicles[counter], rx)
        r = self.images["viewport"].get_rect()
        r.center = ((self.viewpos + 1) * ARENA_WIDTH // 4, ARENA_HEIGHT // 2)
        self.buffer.blit(self.images["viewport"], r)

        la = self.resman["game"]["choose-vehicle"]
        la.center(ARENA_WIDTH // 2, ARENA_HEIGHT // 4)
        la.paint(self.buffer)

    def on_mouseup(self, button, pos):
        """
        Mouse up event handler
        :param button: button number
        :param pos: cursor position
        """
        selected = False
        if button == 1:
            vpos = -1
            for r in self.rects:
                vpos += 1
                if r.collidepoint(pos):
                    selected = True
                    self.viewpos = vpos
                    self.on_keyup(pygame.K_RETURN)
            if not selected:
                self.on_keyup(pygame.K_ESCAPE)
        elif button == 4:
            self.on_keyup(pygame.K_LEFT)
        elif button == 5:
            self.on_keyup(pygame.K_RIGHT)

    def on_keyup(self, key):
        """
        Key release event handler
        :param key: key code
        """
        match key:
            case pygame.K_F1:
                self.arena.change_board(BoardType.HELP, help=HelpChapter.VEHICLESELECTION)
            case pygame.K_F3:
                self.arena.toggle_lang()
            case pygame.K_LEFT:
                if self.viewpos > 0:
                    self.viewpos -= 1
                    self.audio.play_sfx("arrow")
            case pygame.K_RIGHT:
                if self.viewpos < len(self.vehicles) - 1:
                    self.viewpos += 1
                    self.audio.play_sfx("arrow")
            case pygame.K_RETURN:
                self.game.player = Player(self.game, self.viewpos)
                self.audio.play_sfx("closing-tape")
                self.game.change_mode(GameMode.PREPARE)
            case pygame.K_ESCAPE:
                self.arena.change_board(BoardType.MENU)
            case pygame.K_q:
                self.arena.change_board(BoardType.MENU)

    def on_joyaxismotion(self, axis, value):
        """
        Joy Axis Motion event handler
        :param axis: axis number
        :param value: axis value
        """
        if axis == AxisType.HORIZ:
            if value == AxisValue.HIGHER:
                self.on_keyup(pygame.K_RIGHT)
            elif value == AxisValue.LOWER:
                self.on_keyup(pygame.K_LEFT)
        else:
            self.arena.change_board(BoardType.MENU)

    def on_joybuttonup(self, button):
        """
        Joy Button Up event handler
        :param button: button number
        """
        if button == ButtonType.SELECT:
            self.on_keyup(pygame.K_RETURN)
        elif button == ButtonType.B:
            self.arena.toggle_lang()
