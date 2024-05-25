#!/usr/bin/env python3

"""
NewScore board module
"""
import pygame
from helik.boards.standard import Board
from helik.hdefs import ARENA_WIDTH, ARENA_HEIGHT
from helik.htypes import BoardType


class BoardNewScore(Board):
    """
    NewScore board class
    """
    def __init__(self, parent):
        """
        Create NewScore object
        :param parent: parent object handle
        """
        super().__init__(parent)

    def on_paint(self):
        """
        Paint event handler
        """
        self.buffer.blit(self.resman.images["default-background"], (0, 0))
        self.buffer.blit(self.resman.surfaces["status"], (0, ARENA_HEIGHT - 60))

        l, r = self.resman.labels[self.arena.config['lang']]["control"]["keyboard"]
        r.x = (ARENA_WIDTH - r.w) // 2
        r.y = ARENA_HEIGHT // 4

        self.buffer.blit(l, r)

    def on_keyup(self, key):
        """
        Key release event handler
        Key code does not matter. Always return to main menu
        :param key: any key pressed
        """
        if key == pygame.K_ESCAPE:
            self.arena.change_board(BoardType.MENU)
