#!/usr/bin/env python3

"""
Menu board handler
"""

import pygame
from helik.hdefs import ARENA_WIDTH, ARENA_HEIGHT
from helik.platform import ButtonType, AxisType, AxisValue
from helik.types import BoardType
from .standard import Board


def menupos2board(menu_pos: int) -> BoardType:
    """
    Calculate board id from menu pos
    :param menu_pos: menu position number
    :return: board id
    """
    ids = [BoardType.GAME, BoardType.OPTIONS, BoardType.HISCORES,
           BoardType.SETTINGS, BoardType.HELP, BoardType.ABOUT,
           BoardType.QUIT]
    try:
        return ids[menu_pos]
    except IndexError:
        return BoardType.QUIT  # Because, erm, why not? ;)


class BoardMenu(Board):
    """
    Menu board
    """
    def __init__(self, parent):
        """
        Create menu object
        :param parent: parent object handle
        """
        super().__init__(parent)
        self.menu_pos = 0
        self.rect_pos = None
        self.rect_pos_t = None
        self.color = pygame.Color(76, 76, 76)
        self.rectangles = []
        self.rectangles_s = []
        self.create_rectangles()

    def recalculate_pos(self):
        """
        Re-calculate current selection rectangle
        """
        _, self.rect_pos = self.rectangles[self.menu_pos]
        self.rect_pos = self.rect_pos.inflate(40, 40)

    def create_rectangles(self):
        """
        Create labels and rectangles based on locale
        """
        self.rectangles = []
        self.rectangles_s = []
        i = 0
        for elem in self.resman.locale[self.arena.config['lang']]["menu"]["items"]:
            label, rect = elem
            rect.left = 400
            rect.top = 100 + i * 80
            self.rectangles.append((label, rect))
            i += 1

        i = 0
        for elem in self.resman.locale[self.arena.config['lang']]["menu"]["items-shadow"]:
            label, rect = elem
            rect.left = 405
            rect.top = 105 + i * 80
            self.rectangles_s.append((label, rect))
            i += 1
        self.recalculate_pos()

    def on_paint(self):
        """
        Paint event handler
        """
        self.paint_default_bg()
        la, re = self.resman.locale[self.arena.config["lang"]]["common"]["menu-status"]
        self.buffer.blit(la, (ARENA_WIDTH - re.width - 200, ARENA_HEIGHT - 55))

        la, _ = self.resman.locale[self.arena.config["lang"]]["menu"]["title-shadow"]
        self.buffer.blit(la, (220, 50))

        la, _ = self.resman.locale[self.arena.config["lang"]]["menu"]["title"]
        self.buffer.blit(la, (215, 45))

        for re in self.rectangles_s:
            label, rect = re
            self.buffer.blit(label, rect)
        for re in self.rectangles:
            label, rect = re
            self.buffer.blit(label, rect)

        self.rect_pos_t = self.rect_pos.move(5, 5)
        pygame.draw.rect(self.buffer, pygame.Color(16, 16, 16),
                         self.rect_pos_t, width=5, border_radius=20)
        pygame.draw.rect(self.buffer, pygame.Color(207, 229, 32),
                         self.rect_pos, width=5, border_radius=20)

    def activate(self, **kwargs):
        """
        Activate board event handler
        :param kwargs: additional parameters, like help or previous board
        """
        self.create_rectangles()
        self.arena.audio.enable_background_music("background-music")

    def on_keyup(self, key):
        """
        Key release event handler
        :param key: key code
        """
        if key == pygame.K_DOWN:
            if self.menu_pos < 6:
                self.audio.play_sfx("poom")
                self.menu_pos += 1
        elif key == pygame.K_UP:
            if self.menu_pos > 0:
                self.menu_pos -= 1
                self.audio.play_sfx("poom")
        elif key == pygame.K_RETURN:
            bid = menupos2board(self.menu_pos)
            self.audio.play_sfx("closing-tape")
            self.arena.change_board(bid)
        elif key == pygame.K_F3:
            self.arena.config.toggle_lang()
            self.create_rectangles()
        self.recalculate_pos()

    def on_mouseup(self, button, pos):
        """
        Mouse up event handler
        :param button: button number
        :param pos: cursor position
        """
        ch_lang = False
        if button == 1:
            rects = self.resman.rectangles["lang-rectangles"]
            for lang in rects:
                if rects[lang].collidepoint(pos):
                    self.arena.config['lang'] = lang
                    ch_lang = True
                    self.audio.play_sfx("poom")
                    self.create_rectangles()
            if not ch_lang:
                tpos = -1
                for elem in self.rectangles:
                    _, rect = elem
                    tpos += 1
                    if rect.collidepoint(pos):
                        self.menu_pos = tpos
                        self.recalculate_pos()
                        bid = menupos2board(self.menu_pos)
                        self.audio.play_sfx("closing-tape")
                        self.arena.change_board(bid)
        elif button == 4:
            self.on_keyup(pygame.K_UP)
        elif button == 5:
            self.on_keyup(pygame.K_DOWN)

    def on_joyaxismotion(self, axis, value):
        """
        Joy Axis Motion event handler
        :param axis: axis number
        :param value: axis value
        """
        if axis == AxisType.VERT:
            if value == AxisValue.HIGHER:
                self.on_keyup(pygame.K_DOWN)
            elif value == AxisValue.LOWER:
                self.on_keyup(pygame.K_UP)

    def on_joybuttonup(self, button):
        """
        Joy Button Up event handler
        :param button: button number
        """
        if button == ButtonType.B:
            self.arena.config.toggle_lang()
            self.create_rectangles()
        elif button == ButtonType.SELECT:
            self.on_keyup(pygame.K_RETURN)
