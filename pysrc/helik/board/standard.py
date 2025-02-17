#!/usr/bin/env python3

"""
Standard board for Helik
"""

from helik.hdefs import ARENA_HEIGHT, STATUS_HEIGHT, ARENA_WIDTH


class Board:
    """
    Generic board class for Helik
    """
    def __init__(self, parent):
        """
        Class constructor
        """
        self.arena = parent
        self.resman = self.arena.resman
        self.buffer = self.resman.surfaces["buffer"]
        self.images = self.resman.images
        self.audio = self.arena.audio

    def activate(self, **kwargs):
        """
        Board activator
        :param kwargs: additional parameters, like help or previous board
        """

    def deactivate(self):
        """
        Board deactivator
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
        Default background and all labels paint method
        """
        self.buffer.blit(self.resman.images["default-background"], (0, 0))
        self.buffer.blit(self.resman.surfaces["status"], (0, ARENA_HEIGHT - STATUS_HEIGHT))

        # Lang flags
        self.buffer.blit(self.resman.images["flag-pl"],
                         self.resman.rectangles["lang-rectangles"]["pl"])
        self.buffer.blit(self.resman.images["flag-en"],
                         self.resman.rectangles["lang-rectangles"]["en"])

    def paint_default_title(self, groupname):
        """
        Paint default title
        :param groupname: Name of the group/board
        """
        la, _ = self.resman.locale[self.arena.config["lang"]][groupname]["title-shadow"]
        self.buffer.blit(la, (30, 30))
        la, _ = self.resman.locale[self.arena.config["lang"]][groupname]["title"]
        self.buffer.blit(la, (25, 25))

    def paint_default_status(self):
        la, re = self.resman.locale["common"]["common-status"]
        self.buffer.blit(la, (ARENA_WIDTH - re.width - 200, ARENA_HEIGHT - 55))
