#!/usr/bin/env python3

"""
New level mode handler module
"""


import pygame
from helik.modes.standard import Mode
from helik.game.level import Level
from helik.htypes import GameMode, TimerType
from helik.hdefs import ARENA_WIDTH, ARENA_HEIGHT


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
        self.image = None
        self.x = 0
        self.y = 0
        self.w = 0

    def activate(self):
        """
        Activate event handler
        """
        if self.game.data['level'] < 7:
            self.game.data['level'] += 1
            self.game.level = Level(self.res_man, self.game.data['level'])
            self.game.level.create_buildings()
            self.game.level.create_clouds()
            self.game.level.create_dircs()
            self.game.level.create_birds()
            self.image = self.res_man.plane_levels[self.arena.config["lang"]][self.game.data['level']]
            r = self.image.get_rect()
            self.x = (ARENA_WIDTH -r.w) // 2
            self.y = (ARENA_HEIGHT - r.h) // 2
            self.w = r.w
            pygame.time.set_timer(TimerType.THIRD, 2)
        else:
            self.game.change_mode(GameMode.GAMEOVER)

    def on_timer(self, timer):
        """
        Timer event handler
        """
        if timer == TimerType.THIRD:
            self.x -= 1
            if self.x + self.w <= 0:
                self.game.change_mode(GameMode.PLAY)

    def deactivate(self):
        """
        Deactivate event handler
        """
        pygame.time.set_timer(TimerType.THIRD, 0)

    def on_paint(self):
        """
        Paint event handler
        """
        self.buffer.blit(self.res_man.images["default-background"], (0, 0))
        self.buffer.blit(self.image, (self.x, self.y))
