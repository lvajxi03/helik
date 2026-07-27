#!/usr/bin/env python3

"""
KInput settings mode
Provides mode for keys input (interactive new key definition)
"""

import pygame
from helik.platform import keysallowed
from helik.hdefs import ARENA_WIDTH, ARENA_HEIGHT
from helik.platform import ButtonType, TimerType
from .standard import SettingsMode, SettingsModeId


class KbdInputSettingsMode(SettingsMode):
    """
    Keyboart input settings mode
    """
    blink: bool = False
    maxdef: int = 0
    defined: list = []

    def activate(self):
        pygame.time.set_timer(TimerType.SECOND, 250)
        self.blink = False
        self.maxdef = 0
        self.defined = []

    def on_paint(self):
        """
        Paint event handler
        """
        self.paint_default_bg()
        self.paint_default_title("settings")
        la = self.resman["settings"]["kinput-heading-shadow"]
        la.paint_at(self.buffer, 205, 45)
        la = self.resman["settings"]["kinput-heading"]
        la.paint_at(self.buffer, 200, 40)

        la = self.resman["settings"]["kinput-help-1"]
        la.paint_at(self.buffer, 200, 180)

        for counter, elem in enumerate(self.resman["settings"]["kinput-items-shadow"]):
            if counter < self.maxdef or (counter == self.maxdef and self.blink):
                elem.paint_at(self.buffer, 205, 285 + counter * 80)
                try:
                    self.buffer.blit(
                        self.resman.keylabels["shadows"][
                            self.arena.config[
                                "lang"]][self.defined[counter]],
                        (505, 285 + counter * 80))
                except IndexError:
                    pass

        for counter, elem in enumerate(self.resman["settings"]["kinput-items"]):
            if counter < self.maxdef or (counter == self.maxdef and self.blink):
                (elem
                 .paint_at(self.buffer, 200, 280 + counter * 80))
                try:
                    self.buffer.blit(
                        self.resman.keylabels["keys"][
                            self.arena.config["lang"]][
                            self.defined[counter]],
                        (500, 280 + counter * 80))
                except IndexError:
                    pass

        la = self.resman["settings"]["kinput-help-2"]
        la.paint_at(self.buffer, 200, 500)
        la = self.resman["settings"]["kinput-help-3"]
        la.paint_at(self.buffer, 200, 560)
        la = self.resman["settings"]["kinput-help-4"]
        la.paint_at(self.buffer, 200, 620)

        la = self.resman["settings"]["kinput-status"]
        la.paint_at(self.buffer, ARENA_WIDTH - la.w - 200, ARENA_HEIGHT - 55)

    def on_keyup(self, key):
        """
        Key release event handler
        Key code does not matter. Always return to main menu
        :param key: any key pressed
        """
        match key:
            case pygame.K_ESCAPE:
                self.parent.change_mode(SettingsModeId.KLAYOUT)
            case pygame.K_F2:
                # Restart defining keys
                self.activate()
            case pygame.K_F3:
                self.arena.toggle_lang()
            case pygame.K_RETURN:
                if len(self.defined) == 2:
                    self.arena.config["keys"]["jump"] = self.defined[0]
                    self.arena.config["keys"]["shoot"] = self.defined[1]
                    self.parent.change_mode(SettingsModeId.KLAYOUT)
            case _:
                if key in keysallowed and key not in self.defined:
                    self.defined.append(key)
                    self.maxdef += 1

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

    def on_joybuttonup(self, button):
        """
        Jou Button Up event handler
        :param button: button number
        """
        match button:
            case ButtonType.START:
                self.activate()
            case ButtonType.SELECT:
                if len(self.defined) == 2:
                    self.arena.config["keys"]["jump"] = self.defined[0]
                    self.arena.config["keys"]["shoot"] = self.defined[1]
                    self.parent.change_mode(SettingsModeId.KLAYOUT)

    def on_joyaxismotion(self, axis, value):
        """
        Joy Axis Motion event handler
        :param axis: axis number
        :poram value: axis value
        """
        if axis == 0:
            self.parent.change_mode(SettingsModeId.KLAYOUT)

    def on_timer(self, timer):
        """
        Timer handler
        """
        if timer == TimerType.SECOND:
            self.blink = not self.blink
