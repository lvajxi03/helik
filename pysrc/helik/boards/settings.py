#!/usr/bin/env python3

"""
Settings board handler
"""
from helik.htypes import SettingsModeId
from helik.settingsmodes import (MainSettingsMode, KbdLayoutSettingsMode,
                                 KbdInputSettingsMode, PadLayoutSettingsMode,
                                 PadInputSettingsMode)
from .standard import Board


class BoardSettings(Board):
    """
    Settings board class.
    Deletage all operations to settings modes.
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

    def change_mode(self, mode):
        """
        Change settings mode
        :param mode: new mode
        """
        if mode != self.mode:
            self.modes[self.mode].deactivate()
            self.mode = mode
            self.modes[self.mode].activate()

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

    def on_timer(self, timer):
        """
        Timer handler
        """
        self.modes[self.mode].on_timer(timer)

    def on_joybuttonup(self, button):
        """
        JoyButtonUp event handler
        :param button: joystick button
        """
        self.modes[self.mode].on_joybuttonup(button)

    def on_joyaxismotion(self, axis, value):
        """
        JoyAxisMotion event handler
        :param axis: axis number
        :param value: axis value
        """
        self.modes[self.mode].on_joyaxismotion(axis, value)
