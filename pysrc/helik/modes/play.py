#!/usr/bin/env python3

"""
Mode play handler module
"""


import pygame
from helik.modes.standard import Mode
from helik.htypes import TimerType, GameMode, SoundPlayState
from helik.hdefs import ARENA_HEIGHT, ARENA_WIDTH, STATUS_HEIGHT, SPEED
from helik.gfx import blitnumber
from helik.game.explosion import Explosion
from helik.game.player import PlayerDirection
from helik.htypes import GameObjectType


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
        self.speed = SPEED

    def activate(self):
        """
        Activate event handler
        """
        if self.audio.music_state == SoundPlayState.PAUSED:
            self.audio.unpause_music()
        elif self.game.music_state == SoundPlayState.STOPPED:
            self.audio.play_music("music-3")
        self.speed -=  self.arena.config['option']
        pygame.time.set_timer(TimerType.SECOND, 1000)
        pygame.time.set_timer(TimerType.FIRST, 250)
        # self.speed = 30 - 2 * self.data['option']
        pygame.time.set_timer(TimerType.THIRD, self.speed)
        pygame.time.set_timer(TimerType.FOURTH, int(self.speed * 1.5))

    def deactivate(self):
        """
        Deactivate event handler
        """
        self.audio.pause_music()
        pygame.time.set_timer(TimerType.SECOND, 0)
        pygame.time.set_timer(TimerType.FIRST, 0)
        pygame.time.set_timer(TimerType.THIRD, 0)
        pygame.time.set_timer(TimerType.FOURTH, 0)

    def game_update(self):
        """
        Game objects update
        """
        self.game.player.move(1)
        self.game.level.move()

        # Bullet collisions (buildings, birds)
        for bullet in self.game.level.bullets:
            if bullet.valid:
                for lane in self.game.level.lanes:
                    for obj in lane.objects:
                        # Buildings and birds:
                        if obj.go_type in [GameObjectType.BUILDING, GameObjectType.BIRD]:
                            col = obj.collide(bullet)
                            if col:
                                bullet.valid = False
                                bullet.visible = False
                                obj.valid = False
                                obj.visible = False
                                self.game.data["points"] += 1
                                x, y = col
                                ex = Explosion(self.resman.images["explosions"],
                                               x + obj.x,
                                               y + obj.y)
                                self.game.explosions.append(ex)

        # Regular collisions (buildings, clouds, birds)
        for lane in self.game.level.lanes:
            for obj in lane.objects:
                if obj.go_type in [GameObjectType.BUILDING, GameObjectType.BIRD, GameObjectType.CLOUD]:
                    if obj.valid:
                        col = obj.collide(self.game.player)
                        if col:
                            obj.valid = False
                            obj.visible = False
                            self.game.change_mode(GameMode.KILLED)
                elif obj.go_type == GameObjectType.DIRC:
                    if obj.collide(self.game.player):
                        obj.valid = False
                        obj.visible = False
                        self.game.player.toggle_direction()
                elif obj.go_type == GameObjectType.HEART:
                    if obj.collide(self.game.player):
                        obj.visible = False
                        obj.valid = False
                        if self.game.data['lives'] < 4:
                            self.game.data['lives'] += 1
                elif obj.go_type == GameObjectType.AMMO:
                    if obj.collide(self.game.player):
                        obj.visible = False
                        obj.valid = False
                        self.game.data['bullets-available'] += 1

        for ex in self.game.explosions:
            ex.on_update(0)

        self.game.explosions = [x for x in self.game.explosions if x.valid]
        self.game.level.bullets = [x for x in self.game.level.bullets if x.valid]

        if self.game.level.is_empty():
            self.game.change_mode(GameMode.NEWLEVEL)

        if (self.game.player.h + self.game.player.y >= ARENA_HEIGHT - STATUS_HEIGHT) or \
                (self.game.player.y < 0):
            ex = Explosion(self.resman.images["explosions"],
                           self.game.player.x + self.game.player.w // 2,
                           self.game.player.y + self.game.player.h)
            self.game.explosions.append(ex)
            self.game.change_mode(GameMode.KILLED)

    def on_timer(self, timer):
        """
        Timer event handler
        :param timer: timer type code
        """
        if timer == TimerType.SECOND:
            self.game.data['seconds'] += 1
            self.game.data['points'] += 10

        elif timer == TimerType.THIRD:
            self.game_update()
        elif timer == TimerType.FOURTH:
            pass

    def on_keyup(self, key):
        """
        Key release event handler
        :param key: key code
        """
        if key == pygame.K_ESCAPE:
            self.game.change_mode(GameMode.PAUSED)
        elif key == pygame.K_s:
            if self.data['bullets-available'] > 0:
                self.audio.play_sound("popup")
                self.game.level.make_bullet(self.game.player)
                self.data['bullets-available'] -= 1
        self.game.player.on_keyup(key)

    def on_mouseup(self, button, pos):
        """
        Mouse up event handler
        :param button: button number
        :param pos: cursor position
        """
        if button == 1:
            self.on_keyup(pygame.K_s)
        elif button == 4:
            self.on_keyup(pygame.K_SPACE)
        elif button == 2:
            self.on_keyup(pygame.K_ESCAPE)

    def on_paint(self):
        """
        Paint event handler
        """
        self.buffer.blit(self.resman.images["default-background"], (0, 0))
        self.buffer.blit(self.resman.surfaces["status"], (0, ARENA_HEIGHT - 60))
        lives = self.game.data['lives']
        missing = 5 - lives
        for i in range(lives):
            self.buffer.blit(self.resman.images["heart-yellow"], (10 + i * 60, ARENA_HEIGHT - 54))
        for i in range(missing):
            self.buffer.blit(
                self.resman.images["heart-gray"],
                (10 + 60 * lives + i * 60, ARENA_HEIGHT - 54))
        blitnumber(self.buffer, self.data['points'], 5,
                   self.resman.digits, (ARENA_WIDTH - 200, ARENA_HEIGHT - 54))
        self.buffer.blit(self.resman.images["bullets-indicator"],
                         (340, ARENA_HEIGHT - 42))
        blitnumber(self.buffer, self.data['bullets-available'],
                   3, self.resman.digits, (400, ARENA_HEIGHT - 54))

        if self.game.player.direction == PlayerDirection.DOWN:
            self.buffer.blit(self.resman.images["dirc"][4], (ARENA_WIDTH - 350, ARENA_HEIGHT - 54))
        else:
            self.buffer.blit(self.resman.images["dirc"][0], (ARENA_WIDTH - 350, ARENA_HEIGHT - 54))

        self.game.level.on_paint(self.buffer)
        self.game.player.on_paint()

        for explosion in self.game.explosions:
            if explosion.valid:
                explosion.on_paint(self.buffer)

        pygame.draw.line(self.buffer,
                         pygame.Color(255, 255, 255),
                         (0, ARENA_HEIGHT - STATUS_HEIGHT),
                         (ARENA_WIDTH, ARENA_HEIGHT - STATUS_HEIGHT), width=2)
