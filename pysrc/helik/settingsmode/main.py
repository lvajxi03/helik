#!/usr/bin/env python3

"""
Main Settings mode
"""

import pygame
from helik.hdefs import ARENA_HEIGHT, ARENA_WIDTH
from helik.platform import AxisValue, AxisType, ButtonType
from helik.datatypes import BoardType, HelpChapter
from .standard import SettingsMode, SettingsModeId


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

        for counter, elem in enumerate(self.resman["settings"]["items"]):
            elem.move(400, 100 + counter * 80)
            elem.r.w = 750 - elem.x
            self.rectangles.append(elem)

        for counter, elem in enumerate(self.resman["settings"]["items-shadow"]):
            elem.move(405, 105 + counter * 80)
            elem.r.w = 750 - elem.x
            self.rectangles_s.append(elem)

        self.recalculate_pos()

    def recalculate_pos(self):
        """
        Re-calculate current selection rectangle
        """
        self.rect_pos = self.rectangles[self.menu_pos].r
        self.rect_pos = self.rect_pos.inflate(40, 40)

    def on_paint(self):
        """
        Paint event handler
        """
        self.paint_default_bg()
        self.paint_default_title("settings")

        la = self.resman["settings-status"]
        la.paint_at(self.buffer, ARENA_WIDTH - la.w - 200, ARENA_HEIGHT - 55)

        for re in self.rectangles_s:
            re.paint(self.buffer)
        for re in self.rectangles:
            re.paint(self.buffer)

        self.rect_pos_t = self.rect_pos.move(5, 5)
        pygame.draw.rect(self.buffer, pygame.Color(16, 16, 16),
                         self.rect_pos_t, width=5, border_radius=20)
        pygame.draw.rect(self.buffer, pygame.Color(207, 229, 32),
                         self.rect_pos, width=5, border_radius=20)

        if self.arena.config["sound"] == 1:
            la = self.resman["settings"]["checked-shadow"]
            la.paint_at(self.buffer, 705, 100)
            la = self.resman["settings"]["checked"]
            la.paint_at(self.buffer, 700, 95)
        else:
            la = self.resman["settings"]["unchecked-shadow"]
            la.paint_at(self.buffer, 705, 100)
            la = self.resman["settings"]["unchecked"]
            la.paint_at(self.buffer, 700, 95)

        if self.arena.config["music"] == 1:
            la = self.resman["settings"]["checked-shadow"]
            la.paint_at(self.buffer, 705, 175)
            la = self.resman["settings"]["checked"]
            la.paint_at(self.buffer, 700, 170)
        else:
            la = self.resman["settings"]["unchecked-shadow"]
            la.paint_at(self.buffer, 705, 175)
            la = self.resman["settings"]["unchecked"]
            la.paint_at(self.buffer, 700, 170)

        for i in range(2):
            la = self.resman["settings"]["grip-shadow"]
            la.paint_at(self.buffer, 705, 260 + i * 80)
            la = self.resman["settings"]["grip"]
            la.paint_at(self.buffer, 700, 255 + i * 80)

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
            case pygame.K_F3:
                self.parent.arena.toggle_lang()
                self.create_rectangles()
            case pygame.K_DOWN:
                if self.menu_pos < self.maxpos:
                    self.audio.play_sfx("poom")
                    self.menu_pos += 1
            case pygame.K_UP:
                if self.menu_pos > 0:
                    self.menu_pos -= 1
                    self.audio.play_sfx("poom")
            case pygame.K_RETURN:
                self.audio.play_sfx("closing-tape")
                match self.menu_pos:
                    case 0:
                        self.arena.config["sound"] = 0 if self.arena.config["sound"] == 1 else 1
                    case 1:
                        if self.arena.config["music"] == 1:
                            self.arena.config["music"] = 0
                            self.arena.audio.stop_music()
                            self.arena.audio.stop_background_music()
                        else:
                            self.arena.config["music"] = 1
                            self.arena.audio.enable_background_music("background-music")
                    case 2:
                        # Keyboard settings
                        self.parent.change_mode(SettingsModeId.KLAYOUT)
                    case 3:
                        # Gamepad buttons settings
                        self.parent.change_mode(SettingsModeId.GLAYOUT)
            case pygame.K_ESCAPE:
                self.audio.play_sfx("closing-tape")
                self.arena.change_board(BoardType.MENU)
        self.recalculate_pos()

    def on_mouseup(self, button, pos):
        """
        Mouse up event handler
        :param button: button number
        :param pos: cursor position
        """
        ch_lang = False
        match button:
            case 1:
                rects = self.resman.rectangles["lang-rectangles"]
                for lang in rects:
                    if rects[lang].collidepoint(pos):
                        self.arena.set_lang(lang)
                        ch_lang = True
                        self.audio.play_sfx("poom")
                        self.create_rectangles()
                if not ch_lang:
                    for counter, elem in enumerate(self.rectangles):
                        if elem.r.collidepoint(pos):
                            self.menu_pos = counter
                            self.on_keyup(pygame.K_RETURN)
            case 4:
                self.on_keyup(pygame.K_UP)
            case 5:
                self.on_keyup(pygame.K_DOWN)

    def on_joyaxismotion(self, axis, value):
        """
        JoyAxisMotion event handler
        :param axis: axis number
        :param value: axis value
        """
        if axis == AxisType.HORIZ and value == AxisValue.LOWER:
            self.arena.change_board(BoardType.MENU)
        elif axis == AxisType.VERT:
            if value == 1:
                self.on_keyup(pygame.K_DOWN)
            elif value == -1:
                self.on_keyup(pygame.K_UP)

    def on_joybuttonup(self, button):
        match button:
            case ButtonType.SELECT:
                self.on_keyup(pygame.K_RETURN)
            case ButtonType.B:
                self.arena.toggle_lang()
                self.create_rectangles()

    def activate(self):
        """
        Activate mode event
        """
        self.create_rectangles()
