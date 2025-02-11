#!/usr/bin/env python3

"""
Base classes for SettingsModes
"""

import enum


@enum.unique
class SettingsModeId(enum.IntEnum):
    """
    Settings board can have multiple modes:
    1. Main settings menu
    2. Keyboard layout
    3. Keyboard input
    4. Gamepad layout
    5. Gamepad input
    """
    MAIN = 0
    KLAYOUT = 1
    KINPUT = 2
    GLAYOUT = 3
    GINPUT = 4


class SettingsMode:
    """
    Base class of SettingsMode
    """
    def __init__(self, parent, arena):
        """
        Class constructor
        :param parent: Settings board handle
        :param arena: Main Arena handle
        """
        self.parent = parent
        self.arena = arena
        self.resman = self.arena.resman
        self.buffer = self.resman.surfaces["buffer"]
        self.images = self.resman.images
        self.audio = self.arena.audio

    def activate(self):
        """
        Mode activator
        """

    def deactivate(self):
        """
        Mode deactivator
        """

    def on_keyup(self, key):
        """
        Key release handler
        :param key: key code
        """

    def on_mouseup(self, button, pos):
        """
        Mouse up event handler
        :param button: button number
        :param pos: cursor position
        """

    def on_paint(self):
        """
        Paint handler
        """

    def on_timer(self, timer):
        """
        Timer handler
        """

    def on_update(self, delta):
        """
        Update event handler
        :param delta: delta time from last frame
        """

    def on_joybuttonup(self, button):
        """
        Joystick button up handler
        :param button: number of button released
        """

    def on_joyaxismotion(self, axis, value):
        """
        Joystick axis motion handler
        :param axis: axis number in use
        :param value: axis move value
        """

    def paint_default_bg(self):
        """
        Paint default background and items
        """
        self.parent.paint_default_bg()

    def paint_default_title(self, groupname):
        self.parent.paint_default_title(groupname)
