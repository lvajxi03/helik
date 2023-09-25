#!/usr/bin/env python3

"""
Mode play handler module
"""


import pygame
from helik.modes.standard import Mode
from helik.game.level import Level
from helik.htypes import TimerType, GameType
from helik.hdefs import ARENA_HEIGHT, ARENA_WIDTH, STATUS_HEIGHT
from helik.gfx import blitnumber


class ModePlay(Mode):
    """
    Mode play handler class
    """
    def __init__(self, parent):
        """
        Mode play class constructor
        """
        super().__init__(parent)
        self.data = self.game.data

    def activate(self):
        """
        Activate event handler
        """
        pygame.time.set_timer(TimerType.SECONDS, 1000)

    def deactivate(self):
        pygame.time.set_timer(TimerType.SECONDS, 0)

    def on_update(self, delta):
        self.game.level.move(delta)
        self.game.copter.move(delta)

        # Bullet collisions
        for bullet in self.game.level.bullets:
            if bullet.valid:
                for cloud in self.game.level.clouds:
                    if cloud.valid:
                        if cloud.collide(bullet):
                            bullet.valid = False
                            bullet.visible = False
                            cloud.valid = False
                            cloud.visible = False
                            self.game.data['points'] += 1
                for building in self.game.level.buildings:
                    if building.valid:
                        if building.collide(bullet):
                            bullet.valid = False
                            bullet.visible = False
                            building.valid = False
                            building.visible = False
                            self.game.data['points'] += 1

        for cloud in self.game.level.clouds:
            if cloud.valid:
                col = cloud.collide(copter)

    def on_timer(self, timer):
        """
        Timer event handler
        :param timer: timer type code
        """
        if timer == TimerType.COPTER:
            self.game.copter.on_timer(timer)

        elif timer == TimerType.SECONDS:
            self.game.data['seconds'] += 1
            self.game.data['points'] += 10

    def on_keyup(self, key):
        """
        Key release event handler
        :param key: key code
        """
        if key == pygame.K_ESCAPE:
            self.game.change_mode(GameType.PAUSED)
        elif key == pygame.K_s:
            if self.data['bullets-available'] > 0:
                self.game.level.make_bullet(self.game.copter)
                self.data['bullets-available'] -= 1
        self.game.copter.on_keyup(key)

    def on_paint(self):
        """
        Paint event handler
        """
        self.buffer.blit(self.res_man.images["default-background"], (0, 0))
        self.buffer.blit(self.res_man.surfaces["status"], (0, ARENA_HEIGHT - 60))
        for i in range(self.game.data['lives']):
            self.buffer.blit(self.res_man.images["heart-b"], (10 + i * 60, ARENA_HEIGHT - 54))
        blitnumber(self.buffer, self.data['points'], 5, self.res_man.digits, (ARENA_WIDTH - 200, ARENA_HEIGHT - 54))
        self.buffer.blit(self.res_man.images["bullets-indicator"], (340, ARENA_HEIGHT - 42))
        blitnumber(self.buffer, self.data['bullets-available'], 3, self.res_man.digits, (400, ARENA_HEIGHT - 54))

        self.game.level.on_paint(self.buffer)

        self.game.copter.on_paint()

        pygame.draw.line(self.buffer, pygame.Color(255, 255, 255), (0, ARENA_HEIGHT - STATUS_HEIGHT), (ARENA_WIDTH, ARENA_HEIGHT - STATUS_HEIGHT), width=2)
