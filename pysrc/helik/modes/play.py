#!/usr/bin/env python3

"""
Mode play handler module
"""


import pygame
from helik.modes.standard import Mode
from helik.htypes import TimerType, GameMode
from helik.hdefs import ARENA_HEIGHT, ARENA_WIDTH, STATUS_HEIGHT
from helik.gfx import blitnumber
from helik.game.explosion import Explosion
from helik.game.player import PlayerDirection


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
        self.speed = 30

    def activate(self):
        """
        Activate event handler
        """
        pygame.time.set_timer(TimerType.SECOND, 1000)
        pygame.time.set_timer(TimerType.FIRST, 250)
        self.speed = 20 - self.data['level'] - 3 * self.data['option']
        pygame.time.set_timer(TimerType.THIRD, self.speed)
        pygame.time.set_timer(TimerType.FOURTH, 10)

    def deactivate(self):
        """
        Deactivate event handler
        """
        pygame.time.set_timer(TimerType.SECOND, 0)
        pygame.time.set_timer(TimerType.FIRST, 0)
        pygame.time.set_timer(TimerType.THIRD, 0)
        pygame.time.set_timer(TimerType.FOURTH, 0)

    def move_board(self):
        """
        Move board according to current speed
        """
        delta = 1
        self.game.level.move(delta)

        for explosion in self.game.explosions:
            explosion.on_update(delta)

    def on_update(self, delta):
        """
        Update event handler
        :param delta: delta time between two frames
        """
        self.game.player.move(delta)

        # Bullet collisions
        for bullet in self.game.level.bullets:
            if bullet.valid:
                for building in self.game.level.buildings:
                    if building.valid:
                        col = building.collide(bullet)
                        if col:
                            bullet.valid = False
                            bullet.visible = False
                            building.valid = False
                            building.visible = False
                            self.game.data['points'] += 1
                            x, y = col
                            self.game.explosions.append(
                                Explosion(
                                    self.res_man.explosions, x + building.x, y + building.y))
                for bird in self.game.level.birds:
                    if bird.valid:
                        col = bird.collide(bullet)
                        if col:
                            bird.valid = False
                            bird.visible = False
                            bullet.valid = False
                            bullet.visible = False
                            self.game.data['points'] += 1
                            x, y = col
                            self.game.explosions.append(
                                Explosion(
                                    self.res_man.explosions, x + bird.x, y + bird.y))

        # Cloud collisions
        for cloud in self.game.level.clouds:
            if cloud.valid:
                col = cloud.collide(self.game.player)
                if col:
                    cloud.valid = False
                    cloud.visible = False
                    x, y = col
                    self.game.explosions.append(
                        Explosion(
                            self.res_man.explosions, x + cloud.x, y + cloud.y))
                    self.game.change_mode(GameMode.KILLED)

        # Building collisions
        for building in self.game.level.buildings:
            if building.valid:
                col = building.collide(self.game.player)
                if col:
                    building.valid = False
                    building.visible = False
                    x, y = col
                    self.game.explosions.append(
                        Explosion(
                            self.res_man.explosions, x + building.x, y + building.y))
                    self.game.change_mode(GameMode.KILLED)

        # Dirc collisions
        for dirc in self.game.level.dircs:
            if dirc.valid:
                if dirc.collide(self.game.player):
                    dirc.valid = False
                    dirc.visible = False
                    self.game.player.toggle_direction()

        self.game.level.rotate()
        if self.game.level.is_empty():
            self.game.change_mode(GameMode.NEWLEVEL)

        # Birds collisions
        for bird in self.game.level.birds:
            if bird.valid:
                col = bird.collide(self.game.player)
                if col:
                    bird.valid = False
                    bird.visible = False
                    x, y = col
                    self.game.explosions.append(
                        Explosion(
                            self.res_man.explosions, x + bird.x, y + bird.y))
                    self.game.change_mode(GameMode.KILLED)

    def on_timer(self, timer):
        """
        Timer event handler
        :param timer: timer type code
        """
        if timer == TimerType.SECOND:
            self.game.data['seconds'] += 1
            self.game.data['points'] += 10
        elif timer == TimerType.FIRST:
            for dirc in self.game.level.dircs:
                dirc.next()
            for bird in self.game.level.birds:
                bird.next()
        elif timer == TimerType.THIRD:
            self.move_board()
        elif timer == TimerType.FOURTH:
            self.game.level.move_buildings()

    def on_keyup(self, key):
        """
        Key release event handler
        :param key: key code
        """
        if key == pygame.K_ESCAPE:
            self.game.change_mode(GameMode.PAUSED)
        elif key == pygame.K_s:
            if self.data['bullets-available'] > 0:
                self.game.level.make_bullet(self.game.player)
                self.data['bullets-available'] -= 1
        self.game.player.on_keyup(key)

    def on_paint(self):
        """
        Paint event handler
        """
        self.buffer.blit(self.res_man.images["default-background"], (0, 0))
        self.buffer.blit(self.res_man.surfaces["status"], (0, ARENA_HEIGHT - 60))
        lives = self.game.data['lives']
        missing = 5 - lives
        for i in range(lives):
            self.buffer.blit(self.res_man.images["heart-yellow"], (10 + i * 60, ARENA_HEIGHT - 54))
        for i in range(missing):
            self.buffer.blit(
                self.res_man.images["heart-gray"],
                (10 + 60 * lives + i * 60, ARENA_HEIGHT - 54))
        blitnumber(self.buffer, self.data['points'], 5,
                   self.res_man.digits, (ARENA_WIDTH - 200, ARENA_HEIGHT - 54))
        self.buffer.blit(self.res_man.images["bullets-indicator"],
                         (340, ARENA_HEIGHT - 42))
        blitnumber(self.buffer, self.data['bullets-available'],
                   3, self.res_man.digits, (400, ARENA_HEIGHT - 54))

        if self.game.player.direction == PlayerDirection.DOWN:
            self.buffer.blit(self.res_man.dircs[4], (ARENA_WIDTH - 350, ARENA_HEIGHT - 54))
        else:
            self.buffer.blit(self.res_man.dircs[0], (ARENA_WIDTH - 350, ARENA_HEIGHT - 54))

        self.game.level.on_paint(self.buffer)
        self.game.player.on_paint()

        for explosion in self.game.explosions:
            if explosion.valid:
                explosion.on_paint(self.buffer)

        pygame.draw.line(self.buffer,
                         pygame.Color(255, 255, 255),
                         (0, ARENA_HEIGHT - STATUS_HEIGHT),
                         (ARENA_WIDTH, ARENA_HEIGHT - STATUS_HEIGHT), width=2)
