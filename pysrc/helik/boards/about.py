#!/usr/bin/env python3

"""
About board module
"""


import pygame
from helik.htypes import BoardType
from helik.boards.standard import Board
from helik.hdefs import ARENA_HEIGHT, ARENA_WIDTH

class BoardAbout(Board):
    """
    About board class
    """
    def __init__(self, parent):
        super().__init__(parent)

    def on_paint(self):
        """
        Paint event handler
        """
        self.res_man.get("surfaces", "buffer").blit(self.res_man.get("images", "default-background"), (0, 0))
#        pygame.draw.rect(self.res_man.get("surfaces", "status"), self.status_color, self.status)
        self.res_man.get("surfaces", "buffer").blit(self.res_man.get("surfaces", "status"), (0, ARENA_HEIGHT - 60))

    def activate(self):
        """
        """

    def deactivate(self):
        """
        """

    def on_keyup(self, key):
        """
        Key release event handler
        Key code does not matter. Always return to main menu
        :param key: any key pressed
        """
        self.parent.change_board(BoardType.MENU)
