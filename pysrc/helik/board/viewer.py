#!/usr/bin/env python3

"""
Level viewer board
"""

import json
import pygame.time
from helik.game import Level
from helik.platform import TimerType
from .standard import Board


class BoardViewer(Board):
    """
    Viewer Board
    """
    def __init__(self, parent, levelfile: str):
        super().__init__(parent)
        self.levelfile = levelfile
        self.level = None
        self.load()
        self.running = False
        self.speed = 10

    def activate(self, **kwargs):
        """
        Activate event handler
        (most of the initial routines go here)
        :param kwargs: specific keyword arguments
        """
        self.load()
        self.level = Level(self.resman, 0, 0)
        self.running = True
        pygame.time.set_timer(TimerType.FIRST, self.speed)

    def load(self):
        """
        (re)Load level data
        """
        with open(self.levelfile, encoding='utf-8') as fh:
            try:
                data = json.load(fh)
                self.resman.levels[0] = data
                self.level = Level(self.resman, 0, 0)
            except IOError as ioe:
                print(ioe)

    def on_keyup(self, key):
        """
        Key up event handler
        :param key: released key
        """
        match key:
            case pygame.K_SPACE:
                if self.running:
                    self.running = False
                    pygame.time.set_timer(TimerType.FIRST, 0)
                else:
                    self.running = True
                    pygame.time.set_timer(TimerType.FIRST, self.speed)
            case pygame.K_s:
                if not self.running:
                    self.level.move()
            case pygame.K_r:
                self.activate()
            case pygame.K_UP:
                if self.speed > 2:
                    self.speed -= 1
                    pygame.time.set_timer(TimerType.FIRST, 0)
                    pygame.time.set_timer(TimerType.FIRST, self.speed)
            case pygame.K_DOWN:
                self.speed += 1
                pygame.time.set_timer(TimerType.FIRST, self.speed)

    def on_mouseup(self, button, pos):
        """
        Mouse up event handler
        :param button: mouse button number
        :param pos: mouse button pos (tuple)
        """
        if button == 1:
            if self.running:
                self.running = False
                pygame.time.set_timer(TimerType.FIRST, 0)
            else:
                self.running = True
                pygame.time.set_timer(TimerType.FIRST, self.speed)

    def on_paint(self):
        """
        Paint event handler
        """
        self.paint_default_bg()
        self.level.on_paint(self.buffer)

    def on_timer(self, timer):
        """
        Timer event handler
        :param timer: timer to handle
        """
        if  timer == TimerType.FIRST:
            self.level.move()
            if self.level.is_empty():
                self.activate()
