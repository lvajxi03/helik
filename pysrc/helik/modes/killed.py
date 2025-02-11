#!/usr/bin/env python3

"""
Mode killed handler module
"""


import pygame
from helik.hdefs import ARENA_HEIGHT
from .types import GameMode
from helik.platform import TimerType
from .standard import Mode


class ModeKilled(Mode):
    """
    Mode killed handle class
    """
    def __init__(self, parent):
        """
        Mode killed class constructor
        """
        super().__init__(parent)
        self.previous_y = 0

    def activate(self):
        """
        Activate event handler
        """
        self.audio.play_sfx("failed")
        self.previous_y = self.game.player.y
        pygame.time.set_timer(TimerType.FIRST, 11)

    def deactivate(self):
        """
        Deactivate event handler
        """
        pygame.time.set_timer(TimerType.SECOND, 0)

    def on_update(self, delta):
        """
        Update event handler
        :param delta: delta time between two frames
        """
        for explosion in self.game.explosions:
            explosion.on_update(delta)

    def on_timer(self, timer):
        """
        Timer event handler
        :param timer: timer type code
        """
        if timer == TimerType.FIRST:
            self.game.player.y += 3
            if self.game.player.y > ARENA_HEIGHT:
                if self.arena.config['option'] > 0:
                    if self.game.data['lives'] > 1:
                        self.game.data['lives'] -= 1
                        self.game.player.y = (ARENA_HEIGHT - self.game.player.h) // 2
                        self.game.level.rewind()
                        self.game.change_mode(GameMode.PLAY)
                    else:
                        self.game.change_mode(GameMode.GAMEOVER)
                else:
                    self.game.player.y = (ARENA_HEIGHT - self.game.player.h) // 2
                    self.game.level.rewind()
                    self.game.change_mode(GameMode.PLAY)

    def on_paint(self):
        """
        Paint event handler
        """
        self.game.modes[GameMode.PLAY].on_paint()
