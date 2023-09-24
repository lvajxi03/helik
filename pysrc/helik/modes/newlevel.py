#!/usr/bin/env python3

"""
New level mode handler module
"""


from helik.modes.standard import Mode
from helik.game.level import Level
from helik.htypes import GameType


class ModeNewLevel(Mode):
    """
    New level mode handler class
    """
    def __init__(self, parent):
        """
        New level mode class constructor
        """
        super().__init__(parent)
        self.data = self.game.data

    def activate(self):
        """
        Activate event handler
        """
        if self.game.data['level'] < 7:
            self.game.data['level'] += 1            
            self.game.level = Level(self.res_man, self.game.data['level'])
            self.game.level.create_buildings()
            self.game.level.create_clouds()
            self.game.change_mode(GameType.PLAY)
        else:
            self.game.change_mode(GameType.GAMEOVER)


    def deactivate(self):
        """
        Deactivate event handler
        """
        
