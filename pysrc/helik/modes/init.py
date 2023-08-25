#!/usr/bin/env python3

"""
Init mode handler module
"""

from helik.modes.standard import Mode
from helik.htypes import GameType


class ModeInit(Mode):
    """
    Init mode handler class
    """
    def __init__(self, parent):
        """
        Init mode constructor
        :param parent: parent (game board) handle
        """
        super().__init__(parent)

    def activate(self):
        """
        Activate event handler
        """
        self.game.game_data['points'] = 0
        self.game.change_mode(GameType.PREPARE)

    def deactivate(self):
        """
        Deactivate event handler
        """
