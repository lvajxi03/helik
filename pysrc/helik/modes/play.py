#!/usr/bin/env python3

"""
Mode play handler module
"""


import pygame
from helik.modes.standard import Mode
from helik.game.objects import Movable
from helik.htypes import TimerType, GameType
from helik.hdefs import ARENA_HEIGHT, ARENA_WIDTH
from helik.gfx import blitnumber
from helik.game.utils import make_bullet_from

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
        self.bullets = 20
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
        pygame.time.set_timer(TimerType.BULLETS, 5)

    def deactivate(self):
        pygame.time.set_timer(TimerType.MOVABLES, 0)
        pygame.time.set_timer(TimerType.COPTER, 0)
        pygame.time.set_timer(TimerType.SECONDS, 0)
        pygame.time.set_timer(TimerType.BULLETS, 0)

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
        elif timer == TimerType.BULLETS:
            for b in self.bullets_from:
                b.move(8)
                self.bullets_from = [x for x in self.bullets_from if x.valid]
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
        elif key == pygame.K_s:
            if self.bullets > 0:
                self.bullets_from.append(make_bullet_from(self.game.copter))
                self.bullets -= 1
        self.game.copter.on_keyup(key)

    def on_paint(self):
        """
        Paint event handler
        """
        self.buffer.blit(self.res_man.get("images", "default-background"), (0, 0))
        self.buffer.blit(self.res_man.get("surfaces", "status"), (0, ARENA_HEIGHT - 60))
        self.buffer.blit(self.res_man.get("images", "heart-b"), (10, ARENA_HEIGHT - 54))
        self.buffer.blit(self.res_man.get("images", "heart-b"), (70, ARENA_HEIGHT - 54))
        self.buffer.blit(self.res_man.get("images", "heart-b"), (130, ARENA_HEIGHT - 54))
        blitnumber(self.buffer, self.seconds, 5, self.res_man.get_section("digits"), (ARENA_WIDTH - 200, ARENA_HEIGHT - 54))
        self.buffer.blit(self.res_man.get("images", "bullets-indicator"), (350, ARENA_HEIGHT - 54))
        blitnumber(self.buffer, self.bullets, 3, self.res_man.get_section("digits"), (400, ARENA_HEIGHT - 54))
        # Paint bottom objects
        x = 0
        for movable in self.movables:
            if movable.visible:
                movable.on_paint(self.buffer)

        # TODO - remove obsolete paints
        self.game.plane.on_paint(self.buffer)


        for bullet in self.bullets_from:
            if bullet.visible:
                bullet.on_paint(self.buffer)
        self.game.copter.on_paint()
