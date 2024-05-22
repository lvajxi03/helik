#!/usr/bin/env python3

"""
Settings board handler
"""

import pygame
from pygame import Rect
from helik.boards.standard import Board
from helik.hdefs import ARENA_WIDTH, ARENA_HEIGHT
from helik.htypes import BoardType


class BoardSettings(Board):
    """
    Settings board class
    """
    def __init__(self, parent):
        """
        Create settings object
        :param parent: parent object handle
        """
        super().__init__(parent)
        self.labels = ["sound", "music"]
        self.pos = 0
        self.maxpos = 1
        self.rectangles = [Rect(180, 130, 400, 85), Rect(180, 230, 400, 85)]
        self.rshadows = [Rect(175, 125, 400, 85), Rect(175, 225, 400, 85)]

    def on_paint(self):
        """
        Paint event handler
        """
        self.buffer.blit(self.resman.images["default-background"], (0, 0))
        self.buffer.blit(self.resman.surfaces["status"], (0, ARENA_HEIGHT - 60))

        # Lang flags
        self.buffer.blit(self.resman.images["flag-pl"], self.resman.rectangles["lang-rectangles"]["pl"])
        self.buffer.blit(self.resman.images["flag-en"], self.resman.rectangles["lang-rectangles"]["en"])

        l, _ = self.resman.labels[self.arena.config["lang"]]["settings"]["settings-title"]
        self.buffer.blit(l, (55, 45))

        l, r = self.resman.labels[self.arena.config["lang"]]["general"]["status-line-select"]
        self.buffer.blit(l, (ARENA_WIDTH - r.width - 200 , ARENA_HEIGHT - 50))

        l, _ = self.resman.labels[self.arena.config["lang"]]["settings"]["setting-sound"]
        self.buffer.blit(l, (200, 150))
        l, _ = self.resman.labels[self.arena.config["lang"]]["settings"]["setting-music"]
        self.buffer.blit(l, (200, 250))

        if self.arena.config["sound"] == 1:
            self.buffer.blit(self.resman.images["checkbox-checked"], (500, 150))
        else:
            self.buffer.blit(self.resman.images["checkbox-unchecked"], (500, 150))

        if self.arena.config["music"] == 1:
            self.buffer.blit(self.resman.images["checkbox-checked"], (500, 250))
        else:
            self.buffer.blit(self.resman.images["checkbox-unchecked"], (500, 250))
        pygame.draw.rect(self.buffer, pygame.Color(16, 16, 16),
                         self.rshadows[self.pos], width=5, border_radius=20)
        pygame.draw.rect(self.buffer, pygame.Color(207, 229, 32),
                         self.rectangles[self.pos], width=5, border_radius=20)

    def on_keyup(self, key):
        """
        Key release event handler
        Key code does not matter. Always return to main menu
        :param key: any key pressed
        """
        if key == pygame.K_DOWN:
            if self.pos < self.maxpos:
                self.audio.play_sound("arrow")
                self.pos += 1
        elif key == pygame.K_UP:
            if self.pos > 0:
                self.pos -= 1
                self.audio.play_sound("arrow")
        elif key == pygame.K_RETURN:
            self.arena.config[self.labels[self.pos]] = 1 if self.arena.config[self.labels[self.pos]] == 0 else 0
            self.audio.play_sound("closing-tape")
        elif key == pygame.K_q or key == pygame.K_ESCAPE or key == pygame.K_LEFT:
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
                    ch_lang = True
            if not ch_lang:
                i = 0
                for rect in self.rectangles:
                    if rect.collidepoint(pos):
                        self.pos = i
                        self.on_keyup(pygame.K_RETURN)
                    i += 1

        if button == 2 or button == 3:
            self.arena.change_board(BoardType.MENU)
