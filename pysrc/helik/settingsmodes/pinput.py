#!/usr/bin/env/python3

from helik.settingsmodes.standard import SettingsMode


class PadInputSettingsMode(SettingsMode):
    """
    Settings mode to configure pad input
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
