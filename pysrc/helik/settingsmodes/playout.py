#!/usr/bin/env python3

"""
Pad Layout settings mode
"""

from helik.settingsmodes import  SettingsMode
from helik.hdefs import ARENA_HEIGHT


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
