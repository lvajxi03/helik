#!/usr/bin/env python3

"""
Init mode handler module
"""

from helik.modes.standard import Mode
from helik.htypes import GameMode


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
        self.data = self.game.data

    def activate(self):
        """
        Activate event handler
        """
        self.data['points'] = 0
        self.data['level'] = -1
        self.data['seconds'] = 0
        self.data['bullets-available'] = 20
        if self.arena.config['option'] == 0:
            self.data['lives'] = 0
        else:
            self.data['lives'] = 5 - self.arena.config['option'] + 1
        self.data['option'] = self.arena.config['option']
        self.game.explosions = []
        self.game.change_mode(GameMode.SELECTPLAYER)
