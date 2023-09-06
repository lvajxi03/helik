#!/usr/bin/env python3

"""
Mode play handler module
"""


import pygame
from helik.modes.standard import Mode
from helik.game.objects import Movable
from helik.htypes import TimerType, GameType


class ModePlay(Mode):
    """
    Mode play handle class
    """
    def __init__(self, parent):
        """
        Mode play class constructor
        """
        super().__init__(parent)
        self.movables = []

    def create_movables(self):
        """
        Create list of movables, according to a level
        """
        self.movables = []
        x = 0
        for index in self.res_man.get_index("levels", self.game.game_data['level']):
            im, re = self.res_man.bottom_objects[index]
            m = Movable(im, x)
            x += re.w
            self.movables.append(m)

    def activate(self):
        """
        Activate event handler
        """
        self.create_movables()
        pygame.time.set_timer(TimerType.COPTER, 10)
        pygame.time.set_timer(TimerType.MOVABLES, 1)

    def deactivate(self):
        pygame.time.set_timer(TimerType.MOVABLES, 0)
        pygame.time.set_timer(TimerType.COPTER, 0)

    def on_timer(self, timer):
        """
        Timer event handler
        :param timer: timer type code
        """
        if timer == TimerType.COPTER:
            self.game.copter.on_timer(timer)

        elif timer == TimerType.MOVABLES:
            for m in self.movables:
                m.move()
            m = self.movables[0]
            if not m.valid:
                last = self.movables[-1]
                m.r.x = last.r.x + last.r.w
                m.valid = True
                self.movables = self.movables[1:]
                self.movables.append(m)

    def on_keyup(self, key):
        """
        Key release event handler
        :param key: key code
        """
        if key == pygame.K_ESCAPE:
            self.game.change_mode(GameType.PAUSED)
        else:
            self.game.copter.on_keyup(key)

    def on_paint(self):
        """
        Paint event handler
        """
        self.res_man.get("surfaces", "buffer").blit(
            self.res_man.get(
                "images", "default-background"), (0, 0))
        # Paint bottom objects
        x = 0
        for movable in self.movables:
            if movable.valid:
                self.res_man.get("surfaces", "buffer").blit(movable.image, movable.r)

        self.game.plane.on_paint(self.res_man.get("surfaces", "buffer"))
        self.game.copter.on_paint()
