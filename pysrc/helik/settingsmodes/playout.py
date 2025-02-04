#!/usr/bin/env python3

"""
Pad Layout settings mode
"""

import pygame
from .standard import SettingsMode
from helik.htypes import SettingsModeId
from helik.platform import ButtonType, AxisType, AxisValue
from helik.hdefs import ARENA_WIDTH, ARENA_HEIGHT


class PadLayoutSettingsMode(SettingsMode):
    """
    Pad Layout settings mode class
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
        la, _ = self.resman.locale[self.arena.config["lang"]]["settings"]["playout-heading-shadow"]
        self.buffer.blit(la, (205, 45))
        la, _ = self.resman.locale[self.arena.config["lang"]]["settings"]["playout-heading"]
        self.buffer.blit(la, (200, 40))

        la, _ = self.resman.locale[self.arena.config["lang"]]["settings"]["playout-help-2"]
        self.buffer.blit(la, (200, 180))

        buttons = ["jump", "shoot"]
        i = 0
        for elem in self.resman.locale[self.arena.config["lang"]]["settings"]["pinput-items-shadow"]:
            la, _ = elem
            self.buffer.blit(la, (205, 285 + i * 80))
            try:
                self.buffer.blit(self.resman.button_labels[
                                     "shadows"][
                                     self.arena.config["lang"]][self.arena.config["buttons"][buttons[i]]],
                                 (505, 285 + i * 80))
            except IndexError:
                pass
            i += 1

        i = 0
        for elem in self.resman.locale[self.arena.config["lang"]]["settings"]["pinput-items"]:
            la, _ = elem
            self.buffer.blit(la, (200, 280 + i * 80))
            try:
                self.buffer.blit(self.resman.button_labels[
                                     "buttons"][
                                     self.arena.config["lang"]][self.arena.config["buttons"][buttons[i]]],
                                 (500, 280 + i * 80))
            except IndexError:
                pass
            i += 1

            la, _ = self.resman.locale[self.arena.config["lang"]]["settings"]["playout-help-1"]
            self.buffer.blit(la, (200, 680))

            la, re = self.resman.locale[self.arena.config["lang"]]["settings"]["playout-status"]
            self.buffer.blit(la, (ARENA_WIDTH - re.width - 200, ARENA_HEIGHT - 55))

    def on_joybuttonup(self, button):
        """
        JoyButtonUp event handler
        :param button: button number
        """
        if button == ButtonType.START:
            self.parent.change_mode(SettingsModeId.GINPUT)

    def on_keyup(self, key):
        """
        Key release event handler
        Key code does not matter. Always return to main menu
        :param key: any key pressed
        """
        if key == pygame.K_F2:
            self.parent.change_mode(SettingsModeId.GINPUT)
        elif key in (pygame.K_q, pygame.K_ESCAPE, pygame.K_LEFT):
            self.parent.change_mode(SettingsModeId.MAIN)

    def on_joyaxismotion(self, axis, value):
        """
        Joy Axis Motion event handler
        :param axis: axis number
        :param value: axis value
        """
        if axis == AxisType.HORIZ and value == AxisValue.LOWER:
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
