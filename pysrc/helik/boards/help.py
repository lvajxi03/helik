#!/usr/bin/env python3

"""
Help board handler
"""


import pygame
from helik.htypes import BoardType
from helik.boards.standard import Board
from helik.hdefs import ARENA_HEIGHT, ARENA_WIDTH


class BoardHelp(Board):
    """
    Help board class
    """
    def __init__(self, parent):
        super().__init__(parent)

    def on_paint(self):
        """
        Paint event handler
        """
        self.res_man.get("surfaces", "buffer").blit(self.res_man.get("images", "default-background"), (0, 0))
        self.res_man.get("surfaces", "buffer").blit(self.res_man.get("surfaces", "status"), (0, ARENA_HEIGHT - 60))

    def activate(self):
        """
        """

    def deactivate(self):
        """
        """

    def on_keyup(self, key):
        """
        # TODO
        Key release event handler
        Key code does not matter. Always return to main menu
        :param key: any key pressed
        """
        self.parent.change_board(BoardType.MENU)