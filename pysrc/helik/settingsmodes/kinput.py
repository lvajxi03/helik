#!/usr/bin/env python3

from helik.settingsmodes.standard import SettingsMode


class KbdInputSettingsMode(SettingsMode):
    """
    Keyboart input settings mode
    """
    def __init__(self, parent, arena):
        """
        Class constructor
        :param parent: Settings board handle
        :param arena: Arena handle
        """
        super().__init__(parent, arena)
