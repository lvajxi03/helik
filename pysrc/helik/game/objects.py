#!/usr/bin/env python3

"""
Game objects
"""


import enum
import pygame
from helik.htypes import TimerType
from helik.hdefs import ARENA_WIDTH, ARENA_HEIGHT, STATUS_HEIGHT


class Copter:
    """
    Copter player class
    """
    def __init__(self, parent):
        self.game = parent
        self.res_man = self.game.arena.res_man
        self.buffer = self.game.buffer
        self.x = 200
        self.y = 200
        self.image = self.res_man.images["helik-small-right"]
        self.mask = pygame.mask.from_surface(self.image)


    def on_paint(self):
        """
        Paint event handler
        """
        self.buffer.blit(self.image, (self.x, self.y))

    def on_keyup(self, key):
        """
        Key release event handler
        :param key: key code
        """
        if key == pygame.K_SPACE:
            if self.y > 30:
                self.y -= 30

    def on_timer(self, timer):
        """
        Timer event handler
        """
        if timer == TimerType.COPTER:
            if self.y <= ARENA_HEIGHT-60:
                self.y += 1
            else:
                # TODO
                self.y = -30

    def collide(self, something):
        """
        Check if collided with something else
        :param something: any object to collide
        :return: True if collided, false otherwise
        """


class Movable:
    """
    Movable (buildings, etc) support class
    """
    def __init__(self, image, x):
        self.image =  image
        self.mask = pygame.mask.from_surface(image)
        self.r = image.get_rect()
        self.r.x = x
        self.r.y = ARENA_HEIGHT - self.r.h - STATUS_HEIGHT
        self.valid = True
        if self.r.x > ARENA_WIDTH:
            self.visible = False
        else:
            self.visible = True

    def move(self, speed=1):
        self.r.x -= speed
        if self.r.x + self.r.w < 0:
            self.valid = False
            self.visible = False
        else:
            self.valid = True
            self.visible = True

    def on_paint(self, canvas):
        """
        Paint event handler
        :param canvas: surface to blit into
        """
        if self.visible:
            canvas.blit(self.image, self.r)


        
class FlyingObject:
    """
    Flying object handler class
    """
    def __init__(self, image, x, y):
        self.image =  image
        self.mask = pygame.mask.from_surface(self.image)
        self.r = image.get_rect()
        self.r.x = x
        self.r.y = y
        self.base_y = y
        self.valid = True
        if self.r.x > ARENA_WIDTH:
            self.visible = False
        elif self.r.y < 0:
            self.visible = False
        else:
            self.visible = True

    def move(self, speed=1):
        """
        Move object according to its policy
        """
        # Generic move:
        self.r.x += speed
        if self.r.x + self.r.w < 0 or self.r.y + self.r.h < 0:
            self.valid = False
            self.visible = False

    def on_paint(self, canvas):
        """
        Generic paint method
        """
        if self.visible:
            canvas.blit(self.image, self.r)


class Plane(FlyingObject):
    """
    Plane handler class
    """
    def __init__(self, image, x, y):
        super().__init__(image, x, y)


class BulletFrom(FlyingObject):
    """
    BulletFrom handler class
    """
    def __init__(self, image, x, y):
        super().__init__(image, x, y)

    def move(self, speed=1):
        self.r.x += speed
        if self.r.x > ARENA_WIDTH:
            self.valid = False
            self.visible = False

class BulletTo(FlyingObject):
    """
    BulletTo handler class
    """
    def __init__(self, image, x, y):
        super().__init__(image, x, y)

class TNT(FlyingObject):
    """
    TNT handler class
    """
    def __init__(self, image, x, y):
        super().__init__(image, x, y)

    def move(self):
        """
        Move object according to its policy
        """
        self.r.x -= 1

class Cloud(FlyingObject):
    """
    Cloud class
    """
    def __init__(self,image, x, y):
        super().__init__(image, x, y)

    def move(self, speed=1):
        """
        Move cloud according to its policy
        """
        self.r.x -= speed
