#!/usr/bin/env python3

"""
Keyboard Layout settings mode
"""

import pygame
from helik.settingsmodes import SettingsMode
from helik.htypes import SettingsModeId


class KbdLayoutSettingsMode(SettingsMode):
    """
    Keyboard Layout settings mode class
    """
    def __init__(self, parent, arena):
        """
        Class constructor
        :param parent: Settings board handle
        :param arena: Arena handle
        """
        super().__init__(parent, arena)

    def on_paint(self):
        """
        Paint event handler
        """
        self.paint_default_bg()
        self.paint_default_title("settings")
        la, _ = self.resman.locale[self.arena.config["lang"]]["settings"]["klayout-heading-shadow"]
        self.buffer.blit(la, (205, 45))
        la, _ = self.resman.locale[self.arena.config["lang"]]["settings"]["klayout-heading"]
        self.buffer.blit(la, (200, 40))

        keys = ["jump", "shoot"]
        i = 0
        for elem in self.resman.locale[self.arena.config["lang"]]["settings"]["kinput-items-shadow"]:
            la, _ = elem
            self.buffer.blit(la, (205, 285 + i * 80))
            try:
                self.buffer.blit(self.resman.keylabels[
                                     "shadows"][
                                     self.arena.config["lang"]][self.arena.config["keys"][keys[i]]],
                                 (505, 285 + i * 80))
            except IndexError:
                pass
            i += 1

        i = 0
        for elem in self.resman.locale[self.arena.config["lang"]]["settings"]["kinput-items"]:
            la, _ = elem
            self.buffer.blit(la, (200, 280 + i * 80))
            try:
                self.buffer.blit(self.resman.keylabels[
                                     "keys"][
                                     self.arena.config["lang"]][self.arena.config["keys"][keys[i]]],
                                 (500, 280 + i * 80))
            except IndexError:
                pass
            i += 1


    def on_keyup(self, key):
        """
        Key release event handler
        Key code does not matter. Always return to main menu
        :param key: any key pressed
        """
        if key == pygame.K_F2:
            self.parent.change_mode(SettingsModeId.KINPUT)
        elif key in (pygame.K_q, pygame.K_ESCAPE, pygame.K_LEFT):
            self.parent.change_mode(SettingsModeId.MAIN)

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
                    self.arena.config['lang'] = lang
                    self.audio.play_sound("arrow")
        if button in (2, 3):
            self.parent.change_mode(SettingsModeId.MAIN)
        elif button == 4:
            self.on_keyup(pygame.K_UP)
        elif button == 5:
            self.on_keyup(pygame.K_DOWN)
