#!/usr/bin/env python3

"""
Settings board handler
"""
import pygame
from helik.boards.standard import Board
from helik.hdefs import ARENA_WIDTH, ARENA_HEIGHT
from helik.htypes import BoardType, SettingsModeId
from helik.settingsmodes import (MainSettingsMode, KbdLayoutSettingsMode,
                                 KbdInputSettingsMode, PadLayoutSettingsMode,
                                 PadInputSettingsMode)


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
        self.mode = SettingsModeId.MAIN
        self.modes = {
            SettingsModeId.MAIN: MainSettingsMode(self, parent),
            SettingsModeId.KLAYOUT: KbdLayoutSettingsMode(self, parent),
            SettingsModeId.KINPUT: KbdInputSettingsMode(self, parent),
            SettingsModeId.GLAYOUT: PadLayoutSettingsMode(self, parent),
            SettingsModeId.GINPUT: PadInputSettingsMode(self, parent)
        }
        self.labels = ["sound", "music"]
        self.menu_pos = 0
        self.maxpos = 3
        self.rectangles = []
        self.rectangles_s = []
        self.create_rectangles()
        self.rect_pos = None
        self.rect_pos_t = None
        self.create_rectangles()

    def change_mode(self, mode):
        """
        Change settings mode
        :param mode: new mode
        """
        if mode != self.mode:
            self.modes[self.mode].deactivate()
            self.mode = mode
            self.modes[self.mode].activate()

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
        self.modes[self.mode].on_paint()

    def on_keyup(self, key):
        """
        Key release event handler
        Key code does not matter. Always return to main menu
        :param key: any key pressed
        """
        self.modes[self.mode].on_keyup(key)

    def on_mouseup(self, button, pos):
        """
        Mouse up event handler
        :param button: button number
        :param pos: cursor position
        """
        self.modes[self.mode].on_mouseup(button, pos)

    def activate(self):
        """
        Board activator
        """
        self.modes[self.mode].activate()
