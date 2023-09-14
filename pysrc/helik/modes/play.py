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
        self.data = self.game.data
        # TODO: move to another mode?
        self.data.new_level(self.res_man, 0)

    def activate(self):
        """
        Activate event handler
        """
        pygame.time.set_timer(TimerType.COPTER, 10)
        pygame.time.set_timer(TimerType.MOVABLES, self.data['mspeed'])
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
            for m in self.data['movables']:
                m.move()
                if not m.valid:
                    mlast = self.data['movables'][self.data['last-movable']]
                    m.r.x = mlast.r.x + mlast.r.w
                    m.valid = True
                    self.data['last-movable'] += 1
                    self.data['last-movable'] %= len(self.data['movables'])
        elif timer == TimerType.BULLETS:
            for b in self.data['bullets-from']:
                b.move(8)
                self.data['bullets-from'] = [x for x in self.data['bullets-from'] if x.valid]
        elif timer == TimerType.SECONDS:
            self.data['seconds'] += 1
            if self.data['seconds'] % 10 == 0:
                self.data['mspeed'] -= 2
                if self.data['mspeed'] > 0:
                    pygame.time.set_timer(TimerType.MOVABLES, 0)
                    pygame.time.set_timer(TimerType.MOVABLES, self.data['mspeed'])

    def on_keyup(self, key):
        """
        Key release event handler
        :param key: key code
        """
        if key == pygame.K_ESCAPE:
            self.game.change_mode(GameType.PAUSED)
        elif key == pygame.K_s:
            if self.data['bullets-available'] > 0:
                self.data['bullets-from'].append(make_bullet_from(self.game.copter))
                self.data['bullets-available'] -= 1
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
        blitnumber(self.buffer, self.data['seconds'], 5, self.res_man.digits, (ARENA_WIDTH - 200, ARENA_HEIGHT - 54))
        self.buffer.blit(self.res_man.get("images", "bullets-indicator"), (340, ARENA_HEIGHT - 42))
        blitnumber(self.buffer, self.data['bullets-available'], 3, self.res_man.digits, (400, ARENA_HEIGHT - 54))
        # Paint bottom objects
        for movable in self.data['movables']:
            if movable.visible:
                movable.on_paint(self.buffer)

        # TODO - remove obsolete paints
        self.game.plane.on_paint(self.buffer)


        for bullet in self.data['bullets-from']:
            if bullet.visible:
                bullet.on_paint(self.buffer)
        self.game.copter.on_paint()
