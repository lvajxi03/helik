#!/usr/bin/env python3

"""
New level mode handler module
"""


from helik.game.level import Level
from helik.htypes import GameMode, TimerType
from helik.hdefs import ARENA_WIDTH, ARENA_HEIGHT
from .standard import Mode


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
        if self.game.data['level'] < len(self.resman.levels) - 1:
            self.audio.play_sound("game-begin")
            self.game.data['level'] += 1
            self.game.level = Level(self.resman,
                                    self.game.data['level'],
                                    self.arena.config['option'])
            self.image = self.resman.level_planes[
                self.arena.config["lang"]][self.game.data['level']]
            r = self.image.get_rect()
            self.x = ARENA_WIDTH
            self.y = (ARENA_HEIGHT - r.h) // 2
            self.w = r.w
        else:
            self.game.change_mode(GameMode.GAMEOVER)

    def on_update(self, dt):
        """
        Update event handler
        :param dt: unused
        """
        self.x -= 3
        if self.x + self.w <= 0:
            self.game.change_mode(GameMode.PLAY)

    def on_paint(self):
        """
        Paint event handler
        """
        self.buffer.blit(self.resman.images["default-background"], (0, 0))
        if self.image:
            self.buffer.blit(self.image, (self.x, self.y))
