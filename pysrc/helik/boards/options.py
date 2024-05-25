#!/usr/bin/env python3

"""
Options board handler
"""

import pygame
from helik.boards.standard import Board
from helik.hdefs import ARENA_WIDTH, ARENA_HEIGHT
from helik.htypes import BoardType

class BoardOptions(Board):
    """
    Options board class
    """
    def __init__(self, parent):
        super().__init__(parent)
        self.option = 0
        self.menu_pos = 0
        self.rect_pos = None
        self.rect_pos_t = None
        self.color = pygame.Color(76, 76, 76)
        self.rectangles = []
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
        i = 0
        for elem in self.resman.labels[self.arena.config['lang']]["options-items"]:
            label, rect = elem
            rect.left = 400
            rect.top = 100 + i * 80
            self.rectangles.append((label, rect))
            i += 1
        self.recalculate_pos()

    def on_paint(self):
        """
        Paint event handler
        """
        self.buffer.blit(self.resman.images["default-background"], (0, 0))
        self.buffer.blit(self.resman.surfaces["status"], (0, ARENA_HEIGHT - 60))

        # Lang flags
        self.buffer.blit(self.resman.images["flag-pl"], self.resman.rectangles["lang-rectangles"]["pl"])
        self.buffer.blit(self.resman.images["flag-en"], self.resman.rectangles["lang-rectangles"]["en"])

        l, _ = self.resman.labels[self.arena.config['lang']]["options"]["options-title"]
        self.buffer.blit(l, (275, 95))

        l, r = self.resman.labels[self.arena.config["lang"]]["general"]["status-line-select"]
        self.buffer.blit(l, (ARENA_WIDTH - r.width - 200 , ARENA_HEIGHT - 50))

        for re in self.rectangles:
            label, rect = re
            self.buffer.blit(label, rect)

        self.rect_pos_t = self.rect_pos.move(5, 5)
        pygame.draw.rect(self.buffer, pygame.Color(16, 16, 16),
                         self.rect_pos_t, width=5, border_radius=20)
        pygame.draw.rect(self.buffer, pygame.Color(207, 229, 32),
                         self.rect_pos, width=5, border_radius=20)

    def activate(self):
        """
        Activate event handler
        """
        self.option = self.arena.config['option']
        self.menu_pos = self.option
        self.create_rectangles()

    def on_keyup(self, key):
        """
        Key release event handler
        :param key: key code
        """
        if key == pygame.K_DOWN:
            if self.menu_pos < 5:
                self.menu_pos += 1
                self.audio.play_sound("arrow")
        elif key == pygame.K_UP:
            if self.menu_pos > 0:
                self.menu_pos -= 1
                self.audio.play_sound("arrow")
        elif key == pygame.K_RETURN:
            self.option = self.menu_pos
            self.arena.config['option'] = self.menu_pos
            self.arena.change_board(BoardType.MENU)
        elif key == pygame.K_ESCAPE:
            self.arena.change_board(BoardType.MENU)
        elif key == pygame.K_q:
            self.arena.change_board(BoardType.MENU)
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
                    self.audio.play_sound("arrow")
                    self.create_rectangles()
            if not ch_lang:
                tpos = -1
                for elem in self.rectangles:
                    _, rect = elem
                    tpos += 1
                    if rect.collidepoint(pos):
                        self.menu_pos = tpos
                        self.option = tpos
                        self.arena.config['option'] = self.menu_pos
                        self.recalculate_pos()
                        self.audio.play_sound("closing-tape")
                self.arena.change_board(BoardType.MENU)
        elif button == 4:
            self.on_keyup(pygame.K_UP)
        elif button == 5:
            self.on_keyup(pygame.K_DOWN)
