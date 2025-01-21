#!/usr/bin/env python3

"""
About board module
"""
import pygame
from helik.htypes import BoardType
from helik.boards.standard import Board
from helik.hdefs import ARENA_WIDTH, ARENA_HEIGHT
from helik.core.pages import Pager


class BoardAbout(Board):
    """
    About board class
    """
    def __init__(self, parent):
        super().__init__(parent)
        self.pager = Pager(self.resman.pages["about"], self.resman)

    def activate(self):
        """
        Activate event handler
        """
        self.pager.change_lang(self.arena.config["lang"])
        self.pager.activate()

    def on_paint(self):
        """
        Paint event handler
        """
        self.paint_default_bg()
        self.paint_default_title("about")

        self.pager.on_paint(self.buffer)

        if self.pager.has_next() and self.pager.has_prev():
            la, re = self.resman.locale[self.arena.config["lang"]]["common"]["pager-status-full"]
            self.buffer.blit(la, (ARENA_WIDTH - re.width - 200, ARENA_HEIGHT - 55))
        elif self.pager.has_next():
            la, re = self.resman.locale[self.arena.config["lang"]]["common"]["pager-status-next"]
            self.buffer.blit(la, (ARENA_WIDTH - re.width - 200, ARENA_HEIGHT - 55))
        elif self.pager.has_prev():
            la, re = self.resman.locale[self.arena.config["lang"]]["common"]["pager-status-prev"]
            self.buffer.blit(la, (ARENA_WIDTH - re.width - 200, ARENA_HEIGHT - 55))
        else:
            la, re = self.resman.locale[self.arena.config["lang"]]["common"]["pager-status-none"]
            self.buffer.blit(la, (ARENA_WIDTH - re.width - 200, ARENA_HEIGHT - 55))

    def on_keyup(self, key):
        """
        Key release event handler
        Key code does not matter. Always return to main menu
        :param key: any key pressed
        """
        if key in [pygame.K_ESCAPE, pygame.K_q]:
            self.arena.change_board(BoardType.MENU)
        elif key == pygame.K_LEFT:
            self.pager.prev()
        else:
            if self.pager.has_next():
                self.pager.next()
            else:
                self.arena.change_board(BoardType.MENU)

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
                    self.pager.change_lang(lang)
                    ch_lang = True
            if not ch_lang:
                if not self.pager.on_click():
                    if self.pager.has_next():
                        self.pager.next()
                    else:
                        self.arena.change_board(BoardType.MENU)
        elif button == 4:
            if self.pager.has_next():
                self.pager.next()
            else:
                self.arena.change_board(BoardType.MENU)
        elif button == 5:
            self.pager.prev()
        elif not ch_lang:
            self.arena.change_board(BoardType.MENU)
