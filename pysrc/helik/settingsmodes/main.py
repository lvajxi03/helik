#!/usr/bin/env python3

"""
Main Settings mode
"""

import pygame
from helik.settingsmodes.standard import SettingsMode
from helik.hdefs import ARENA_HEIGHT, ARENA_WIDTH
from helik.htypes import BoardType, SettingsModeId


class MainSettingsMode(SettingsMode):
    """
    Main settings mode
    """
    def __init__(self, parent, arena):
        """
        Class constructor
        :param parent: Settings board handle
        :param arena: Arena handle
        """
        super().__init__(parent, arena)
        self.labels = ["sound", "music"]
        self.menu_pos = 0
        self.maxpos = 3
        self.rectangles = []
        self.rectangles_s = []
        self.create_rectangles()
        self.rect_pos = None
        self.rect_pos_t = None
        self.create_rectangles()

    def create_rectangles(self):
        """
        Create labels and rectangles based on locale
        """
        self.rectangles = []
        self.rectangles_s = []

        i = 0
        for elem in self.resman.locale[self.arena.config['lang']]["settings"]["items"]:
            label, rect = elem
            rect.left = 400
            rect.top = 100 + i * 80
            rect.width = 750 - rect.left
            self.rectangles.append((label, rect))
            i += 1
        i = 0
        for elem in self.resman.locale[self.arena.config['lang']]["settings"]["items-shadow"]:
            label, rect = elem
            rect.left = 405
            rect.top = 105 + i * 80
            rect.width = 750 - rect.left
            self.rectangles_s.append((label, rect))
            i += 1
        self.recalculate_pos()

    def recalculate_pos(self):
        """
        Re-calculate current selection rectangle
        """
        _, self.rect_pos = self.rectangles[self.menu_pos]
        self.rect_pos = self.rect_pos.inflate(40, 40)

    def on_paint(self):
        """
        Paint event handler
        """
        self.buffer.blit(self.resman.images["default-background"], (0, 0))
        self.buffer.blit(self.resman.surfaces["status"], (0, ARENA_HEIGHT - 60))

        # Lang flags
        self.buffer.blit(self.resman.images["flag-pl"], self.resman.rectangles["lang-rectangles"]["pl"])
        self.buffer.blit(self.resman.images["flag-en"], self.resman.rectangles["lang-rectangles"]["en"])

        la, _ = self.resman.locale[self.arena.config["lang"]]["settings"]["title-shadow"]
        self.buffer.blit(la, (240, 80))
        la, _ = self.resman.locale[self.arena.config["lang"]]["settings"]["title"]
        self.buffer.blit(la, (245, 75))

        la, re = self.resman.locale[self.arena.config["lang"]]["common"]["settings-status"]
        self.buffer.blit(la, (ARENA_WIDTH - re.width - 200, ARENA_HEIGHT - 55))

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

        if self.arena.config["sound"] == 1:
            la, re = self.resman.locale[self.arena.config["lang"]]["settings"]["checked-shadow"]
            self.buffer.blit(la, (705, 100))
            la, re = self.resman.locale[self.arena.config["lang"]]["settings"]["checked"]
            self.buffer.blit(la, (700, 95))
        else:
            la, re = self.resman.locale[self.arena.config["lang"]]["settings"]["unchecked-shadow"]
            self.buffer.blit(la, (705, 100))
            la, re = self.resman.locale[self.arena.config["lang"]]["settings"]["unchecked"]
            self.buffer.blit(la, (700, 95))

        if self.arena.config["music"] == 1:
            la, re = self.resman.locale[self.arena.config["lang"]]["settings"]["checked-shadow"]
            self.buffer.blit(la, (705, 175))
            la, re = self.resman.locale[self.arena.config["lang"]]["settings"]["checked"]
            self.buffer.blit(la, (700, 170))
        else:
            la, re = self.resman.locale[self.arena.config["lang"]]["settings"]["unchecked-shadow"]
            self.buffer.blit(la, (705, 175))
            la, re = self.resman.locale[self.arena.config["lang"]]["settings"]["unchecked"]
            self.buffer.blit(la, (700, 170))

        for i in range(2):
            la, re = self.resman.locale[self.arena.config["lang"]]["settings"]["grip-shadow"]
            self.buffer.blit(la, (705, 260 + i * 80))
            la, re = self.resman.locale[self.arena.config["lang"]]["settings"]["grip"]
            self.buffer.blit(la, (700, 255 + i * 80))

    def on_keyup(self, key):
        """
        Key release event handler
        Key code does not matter. Always return to main menu
        :param key: any key pressed
        """
        if key == pygame.K_DOWN:
            if self.menu_pos < self.maxpos:
                self.audio.play_sound("arrow")
                self.menu_pos += 1
        elif key == pygame.K_UP:
            if self.menu_pos > 0:
                self.menu_pos -= 1
                self.audio.play_sound("arrow")
        elif key == pygame.K_RETURN:
            if self.menu_pos < 2:
                self.arena.config[self.labels[self.menu_pos]] = 1 if self.arena.config[self.labels[self.menu_pos]] == 0 else 0
                self.audio.play_sound("closing-tape")
            elif self.menu_pos == 2:
                # Keyboard settings
                self.parent.change_mode(SettingsModeId.KLAYOUT)
            elif self.menu_pos == 3:
                # Gamepad buttons settings
                self.parent.change_mode(SettingsModeId.GLAYOUT)
        elif key in (pygame.K_q, pygame.K_ESCAPE, pygame.K_LEFT):
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
                i = 0
                for elem in self.rectangles:
                    _, rect = elem
                    if rect.collidepoint(pos):
                        self.menu_pos = i
                        self.on_keyup(pygame.K_RETURN)
                    i += 1
        if button in (2, 3):
            self.arena.change_board(BoardType.MENU)
        elif button == 4:
            self.on_keyup(pygame.K_UP)
        elif button == 5:
            self.on_keyup(pygame.K_DOWN)
