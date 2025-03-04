#!/usr/bin/env python3

"""
Keyboard Layout settings mode
"""

import pygame
from helik.hdefs import ARENA_WIDTH, ARENA_HEIGHT
from helik.platform import ButtonType, AxisType, AxisValue
from helik.datatypes import BoardType, HelpChapter
from .standard import SettingsMode, SettingsModeId


class KbdLayoutSettingsMode(SettingsMode):
    """
    Keyboard Layout settings mode class
    """
    def on_paint(self):
        """
        Paint event handler
        """
        self.paint_default_bg()
        self.paint_default_title("settings")
        la, _ = self.resman["settings"]["klayout-heading-shadow"]
        self.buffer.blit(la, (205, 45))
        la, _ = self.resman["settings"]["klayout-heading"]
        self.buffer.blit(la, (200, 40))

        la, _ = self.resman["settings"]["klayout-help-2"]
        self.buffer.blit(la, (200, 180))

        keys = ["jump", "shoot"]
        i = 0
        for elem in self.resman["settings"]["kinput-items-shadow"]:
            la, _ = elem
            self.buffer.blit(la, (205, 285 + i * 80))
            try:
                self.buffer.blit(self.resman.keylabels[
                                     "shadows"][
                                     self.arena.config["lang"]][
                                     self.arena.config["keys"][keys[i]]],
                                 (505, 285 + i * 80))
            except IndexError:
                pass
            i += 1

        i = 0
        for elem in self.resman["settings"]["kinput-items"]:
            la, _ = elem
            self.buffer.blit(la, (200, 280 + i * 80))
            try:
                self.buffer.blit(self.resman.keylabels[
                                     "keys"][
                                     self.arena.config["lang"]][
                                     self.arena.config["keys"][keys[i]]],
                                 (500, 280 + i * 80))
            except IndexError:
                pass
            i += 1

            la, _ = self.resman["settings"]["klayout-help-1"]
            self.buffer.blit(la, (200, 680))

            la, re = self.resman["settings"]["klayout-status"]
            self.buffer.blit(la, (ARENA_WIDTH - re.width - 200, ARENA_HEIGHT - 55))

    def on_keyup(self, key):
        """
        Key release event handler
        Key code does not matter. Always return to main menu
        :param key: any key pressed
        """
        match key:
            case pygame.K_F1:
                self.parent.arena.change_board(
                    BoardType.HELP, help=HelpChapter.SETTINGS)
            case pygame.K_F2:
                self.parent.change_mode(SettingsModeId.KINPUT)
            case pygame.K_F3:
                self.arena.toggle_lang()
            case pygame.K_ESCAPE:
                self.parent.change_mode(SettingsModeId.MAIN)

    def on_joybuttonup(self, button):
        """
        Joy Button Up event handler
        :param button: button number
        """
        match button:
            case ButtonType.START:
                self.parent.change_mode(SettingsModeId.KINPUT)
            case ButtonType.B:
                self.arena.toggle_lang()

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
        match button:
            case 1:
                rects = self.resman.rectangles["lang-rectangles"]
                for lang in rects:
                    if rects[lang].collidepoint(pos):
                        self.arena.set_lang(lang)
                        self.audio.play_sfx("arrow")
            case 4:
                self.on_keyup(pygame.K_UP)
            case 5:
                self.on_keyup(pygame.K_DOWN)
