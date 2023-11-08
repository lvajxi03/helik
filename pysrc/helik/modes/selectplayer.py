#!/usr/bin/env python3

"""
SelectPlayer handler module
"""

import pygame
from helik.modes.standard import Mode
from helik.htypes import BoardType, GameMode
from helik.game.player import Player
from helik.hdefs import ARENA_WIDTH, ARENA_HEIGHT


class SelectPlayer(Mode):
    """
    SelectPlayer handler class
    """
    def __init__(self, parent):
        """
        Class constructor
        """
        super().__init__(parent)
        self.viewpos = 0
        self.rects = []
        self.view_x = 0
        self.view_y = 0
        self.vehicles = [self.images["vehicles"][0],
                       self.images["vehicles"][2],
                       self.images["vehicles"][4]]
        x = ARENA_WIDTH // 4
        for image in self.vehicles:
            r = image.get_rect()
            r.center = (x, ARENA_HEIGHT // 2)
            x += ARENA_WIDTH // 4
            self.rects.append(r)

    def activate(self):
        """
        Activate event handler
        """

    def deactivate(self):
        """
        Deactivate event handler
        """

    def on_paint(self):
        """
        Paint event handler
        """
        self.buffer.blit(self.res_man.images["default-background"], (0, 0))
        for i in range(len(self.rects)):
            self.buffer.blit(self.vehicles[i], self.rects[i])
        r = self.images["viewport"].get_rect()
        r.center = ((self.viewpos + 1) * ARENA_WIDTH // 4, ARENA_HEIGHT // 2)
        self.buffer.blit(self.images["viewport"], r)

    def on_keyup(self, key):
        """
        Key release event handler
        :param key: key code
        """
        if key == pygame.K_LEFT:
            if self.viewpos > 0:
                self.viewpos -= 1
                self.res_man.play("arrow")
        elif key == pygame.K_RIGHT:
            if self.viewpos < len(self.images["vehicles"]) - 1:
                self.viewpos += 1
                self.res_man.play("arrow")
        elif key == pygame.K_RETURN:
            self.game.player = Player(self.game, self.viewpos)
            self.game.change_mode(GameMode.PREPARE)
        elif key == pygame.K_ESCAPE:
            self.arena.change_board(BoardType.MENU)
        elif key == pygame.K_q:
            self.arena.change_board(BoardType.MENU)