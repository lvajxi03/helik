#!/usr/bin/env/python3

import pygame
from helik.settingsmodes.standard import SettingsMode
from helik.htypes import SettingsModeId, TimerType
from helik.platform import ButtonType, buttons_allowed
from helik.hdefs import ARENA_WIDTH, ARENA_HEIGHT


class PadInputSettingsMode(SettingsMode):
    """
    Settings mode to configure pad input
    """
    blink: bool = False
    maxdef: int = 0
    defined: list = []

    def __init__(self, parent, arena):
        """
        Class constructor
        :param parent: Settings board handle
        :param arena: Arena handle
        """
        super().__init__(parent, arena)
        self.blink = False
        self.maxdef = 0
        self.defined = []

    def on_paint(self):
        """
        Paint event handler
        """
        self.paint_default_bg()
        self.paint_default_title("settings")
        la, _ = self.resman.locale[self.arena.config["lang"]]["settings"]["pinput-heading-shadow"]
        self.buffer.blit(la, (205, 45))
        la, _ = self.resman.locale[self.arena.config["lang"]]["settings"]["pinput-heading"]
        self.buffer.blit(la, (200, 40))
        la, _ = self.resman.locale[self.arena.config["lang"]]["settings"]["pinput-help-1"]
        self.buffer.blit(la, (200, 180))

        i = 0
        for elem in self.resman.locale[self.arena.config["lang"]]["settings"]["pinput-items-shadow"]:
            if i < self.maxdef or (i == self.maxdef and self.blink):
                la, _ = elem
                self.buffer.blit(la, (205, 285 + i * 80))
                try:
                    self.buffer.blit(self.resman.button_labels["shadows"][self.arena.config["lang"]][self.defined[i]],
                                     (505, 285 + i * 80))
                except IndexError:
                    pass
                i += 1

        i = 0
        for elem in self.resman.locale[self.arena.config["lang"]]["settings"]["pinput-items"]:
            if i < self.maxdef or (i == self.maxdef and self.blink):
                la, _ = elem
                self.buffer.blit(la, (200, 280 + i * 80))
                try:
                    self.buffer.blit(self.resman.button_labels["buttons"][self.arena.config["lang"]][self.defined[i]],
                                     (500, 280 + i * 80))
                except IndexError:
                    pass
                i += 1

        la, _ = self.resman.locale[self.arena.config["lang"]]["settings"]["pinput-help-2"]
        self.buffer.blit(la, (200, 500))
        la, _ = self.resman.locale[self.arena.config["lang"]]["settings"]["pinput-help-3"]
        self.buffer.blit(la, (200, 560))
        la, _ = self.resman.locale[self.arena.config["lang"]]["settings"]["pinput-help-4"]
        self.buffer.blit(la, (200, 620))

        la, re = self.resman.locale[self.arena.config["lang"]]["settings"]["pinput-status"]
        self.buffer.blit(la, (ARENA_WIDTH - re.width - 200, ARENA_HEIGHT - 55))

    def on_keyup(self, key):
        """
        Key release event handler
        Key code does not matter. Always return to main menu
        :param key: any key pressed
        """
        if key in (pygame.K_q, pygame.K_ESCAPE, pygame.K_LEFT):
            self.parent.change_mode(SettingsModeId.GLAYOUT)
        elif key == pygame.K_RETURN:
            if len(self.defined) == 2:
                self.arena.config["buttons"]["jump"] = self.defined[0]
                self.arena.config["buttons"]["shoot"] = self.defined[1]
                self.parent.change_mode(SettingsModeId.KLAYOUT)

    def on_joybuttonup(self, button):
        """
        JoyButtonUp event handler
        :param button: button number
        """
        if button == ButtonType.SELECT:
            if len(self.defined) == 2:
                self.arena.config["buttons"]["jump"] = self.defined[0]
                self.arena.config["buttons"]["shoot"] = self.defined[1]
                self.parent.change_mode(SettingsModeId.GLAYOUT)
        elif button == ButtonType.START:
            self.activate()
        elif button in buttons_allowed and button not in self.defined:
            self.defined.append(button)
            self.maxdef += 1

    def on_joyaxismotion(self, axis, value):
        """
        JoyAxisMotion event handler
        :param axis: axis number
        :param value: axis move value
        """
        if axis == 0:
            self.parent.change_mode(SettingsModeId.GLAYOUT)

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
            self.parent.change_mode(SettingsModeId.GLAYOUT)
        elif button == 4:
            self.on_keyup(pygame.K_UP)
        elif button == 5:
            self.on_keyup(pygame.K_DOWN)

    def activate(self):
        pygame.time.set_timer(TimerType.SECOND, 250)
        self.blink = False
        self.maxdef = 0
        self.defined = []

    def on_timer(self, timer):
        """
        Timer handler
        """
        if timer == TimerType.SECOND:
            self.blink = not self.blink
