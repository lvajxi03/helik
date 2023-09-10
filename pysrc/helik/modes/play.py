#!/usr/bin/env python3

"""
Mode play handler module
"""


import pygame
from helik.modes.standard import Mode
from helik.game.objects import Movable
from helik.htypes import TimerType, GameType
from helik.hdefs import ARENA_HEIGHT

class ModePlay(Mode):
    """
    Mode play handle class
    """
    def __init__(self, parent):
        """
        Mode play class constructor
        """
        super().__init__(parent)
        self.last_movable = 0
        self.movables = []
        self.objects = []
        self.bullets_from = []
        self.bullets_to = []
        self.seconds = 0
        self.mspeed = 21

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
        self.last_movable = len(self.movables) - 1

    def activate(self):
        """
        Activate event handler
        """
        self.last_movable = 0
        self.create_movables()
        self.last_movable = len(self.movables) - 1
        pygame.time.set_timer(TimerType.COPTER, 10)
        pygame.time.set_timer(TimerType.MOVABLES, self.mspeed)
        pygame.time.set_timer(TimerType.SECONDS, 1000)

    def deactivate(self):
        pygame.time.set_timer(TimerType.MOVABLES, 0)
        pygame.time.set_timer(TimerType.COPTER, 0)
        pygame.time.set_timer(TimerType.SECONDS, 0)

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
                if not m.valid:
                    mlast = self.movables[self.last_movable]
                    m.r.x = mlast.r.x + mlast.r.w
                    m.valid = True
                    self.last_movable += 1
                    self.last_movable %= len(self.movables)
        elif timer == TimerType.SECONDS:
            self.seconds += 1
            if self.seconds % 10 == 0:
                self.mspeed -= 2
                if self.mspeed > 0:
                    pygame.time.set_timer(TimerType.MOVABLES, 0)
                    pygame.time.set_timer(TimerType.MOVABLES, self.mspeed)

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
        self.res_man.get("surfaces", "buffer").blit(self.res_man.get("surfaces", "status"), (0, ARENA_HEIGHT - 60))
        self.res_man.get("surfaces", "buffer").blit(self.res_man.get("images", "heart-b"), (10, ARENA_HEIGHT - 54))
        self.res_man.get("surfaces", "buffer").blit(self.res_man.get("images", "heart-b"), (70, ARENA_HEIGHT - 54))
        self.res_man.get("surfaces", "buffer").blit(self.res_man.get("images", "heart-b"), (130, ARENA_HEIGHT - 54))
        self.res_man.get("surfaces", "buffer").blit(self.res_man.get("digits", "0"), (200, ARENA_HEIGHT - 52))
        self.res_man.get("surfaces", "buffer").blit(self.res_man.get("digits", "1"), (235, ARENA_HEIGHT - 52))
        self.res_man.get("surfaces", "buffer").blit(self.res_man.get("digits", "2"), (270, ARENA_HEIGHT - 52))
        self.res_man.get("surfaces", "buffer").blit(self.res_man.get("digits", "3"), (305, ARENA_HEIGHT - 52))
        # Paint bottom objects
        x = 0
        for movable in self.movables:
            if movable.visible:
                movable.on_paint(self.res_man.get("surfaces", "buffer"))

        # TODO - remove obsolete paints
        self.game.plane.on_paint(self.res_man.get("surfaces", "buffer"))
        self.res_man.get("surfaces", "buffer").blit(
            self.res_man.get(
                "images", "bullet-2"), (300, 300))
        self.game.copter.on_paint()
