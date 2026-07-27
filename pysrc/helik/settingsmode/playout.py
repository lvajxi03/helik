#!/usr/bin/env python3

"""
Pad Layout settings mode
"""

import pygame
from helik.platform import ButtonType, AxisType, AxisValue
from helik.datatypes import BoardType, HelpChapter
from helik.hdefs import ARENA_WIDTH, ARENA_HEIGHT
from .standard import SettingsMode, SettingsModeId


class PadLayoutSettingsMode(SettingsMode):
    """
    Pad Layout settings mode class
    """
    def on_paint(self):
        """
        Paint event handler
        """
        self.paint_default_bg()
        self.paint_default_title("settings")
        la = self.resman["settings"]["playout-heading-shadow"]
        la.paint_at(self.buffer, 205, 45)
        la = self.resman["settings"]["playout-heading"]
        la.paint_at(self.buffer, 200, 40)

        la = self.resman["settings"]["playout-help-2"]
        la.paint_at(self.buffer, 200, 180)

        buttons = ["jump", "shoot"]

        for counter, elem in enumerate(self.resman["settings"]["pinput-items-shadow"]):
            elem.paint_at(self.buffer, 205, 285 + counter * 80)
            try:
                self.buffer.blit(self.resman.button_labels[
                                     "shadows"][
                                     self.arena.config[
                                         "lang"]][
                                     self.arena.config[
                                         "buttons"][buttons[counter]]],
                                 (505, 285 + counter * 80))
            except IndexError:
                pass

        for counter, elem in enumerate(self.resman["settings"]["pinput-items"]):
            elem.paint_at(self.buffer, 200, 280 + counter * 80)
            try:
                self.buffer.blit(self.resman.button_labels[
                                     "buttons"][
                                     self.arena.config["lang"]][
                                     self.arena.config[
                                         "buttons"][buttons[counter]]],
                                 (500, 280 + counter * 80))
            except IndexError:
                pass

            la = self.resman["settings"]["playout-help-1"]
            la.paint_at(self.buffer, 200, 680)

            la = self.resman["settings"]["playout-status"]
            la.paint_at(self.buffer, ARENA_WIDTH - la.w - 200, ARENA_HEIGHT - 55)

    def on_joybuttonup(self, button):
        """
        JoyButtonUp event handler
        :param button: button number
        """
        match button:
            case ButtonType.START:
                self.parent.change_mode(SettingsModeId.GINPUT)
            case ButtonType.B:
                self.arena.toggle_lang()

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
                self.parent.change_mode(SettingsModeId.GINPUT)
            case pygame.K_F3:
                self.arena.toggle_lang()
            case pygame.K_ESCAPE:
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
