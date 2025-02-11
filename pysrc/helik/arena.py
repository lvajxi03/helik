#!/usr/bin/env python3

"""
Arena module
"""

import random
from importlib.resources import files
import pygame
from helik.hdefs import APPLICATION_TITLE
from helik.boards import (BoardType, BoardWelcome, BoardAbout, BoardMenu, BoardOptions,
                          BoardHiscores, BoardHelp, BoardSettings, BoardGame, BoardNewScore, BoardQuit)
from helik.htypes import DirCType
from helik.res import ResourceManager
from helik.config import Config
from helik.media.audio import AudioController


class Application:
    """
    Helik application
    """
    def __init__(self):
        """
        Application initializer
        """
        random.seed()
        pygame.init()
        pygame.mixer.init()
        pygame.joystick.init()
        for i in range(pygame.joystick.get_count()):
            joystick = pygame.joystick.Joystick(i)
            joystick.init()
        self.resman = ResourceManager(files('helik.resources'))
        self.audio = AudioController(self, files('helik.resources'))
        pygame.display.set_caption(APPLICATION_TITLE)
        self.clock = pygame.time.Clock()
        self.running = True
        self.config = Config()
        self.config.read_default_config()
        self.boards = {
            BoardType.WELCOME: BoardWelcome(self),
            BoardType.MENU: BoardMenu(self),
            BoardType.ABOUT: BoardAbout(self),
            BoardType.HISCORES: BoardHiscores(self),
            BoardType.HELP: BoardHelp(self),
            BoardType.OPTIONS: BoardOptions(self),
            BoardType.SETTINGS: BoardSettings(self),
            BoardType.GAME: BoardGame(self),
            BoardType.NEWSCORE: BoardNewScore(self),
            BoardType.QUIT: BoardQuit(self)
            }
        self.board_id = BoardType.WELCOME
        self.dirc = DirCType.DOWN

    def change_board(self, newboard):
        """
        Change board to the other one.
        Will change only if the other one is different.
        Additional actions:
        * .deactivate() method called for the current board
        * .activate() method called for the new board
        :param newboard: other board id
        """
        if newboard != self.board_id:
            self.boards[self.board_id].deactivate()
            self.board_id = newboard
            self.boards[self.board_id].activate()

    def run(self, **kwargs):
        """
        Main application loop
        """
        vaq = kwargs.get("validate_and_quit", False)

        if vaq:
            self.boards[BoardType.QUIT].activate()
        else:
            # Activate initial board
            self.boards[self.board_id].activate()

        # webbrowser.open("mailto:marcin.bielewicz@gmail.com")
        # Main application loop
        for j in range(pygame.joystick.get_count()):
            pygame.joystick.Joystick(j)
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYUP:
                    self.on_keyup(event.key)
                elif event.type == pygame.MOUSEBUTTONUP:
                    self.on_mouseup(event.button, event.pos)
                elif event.type == pygame.JOYBUTTONUP:
                    self.on_joybuttonup(event.button)
                elif event.type == pygame.JOYAXISMOTION:
                    self.on_joyaxismotion(event.axis, event.value)
                elif event.type == pygame.JOYDEVICEADDED:
                    for j in range(pygame.joystick.get_count()):
                        joy = pygame.joystick.Joystick(j)
                        joy.init()
                elif event.type > pygame.USEREVENT:
                    self.on_timer(event.type)

            dt = self.clock.tick(1000)
            self.on_update(dt)
            self.on_paint()
            pygame.display.update()

        # Eventually,
        self.config.save_default_config()
        pygame.quit()

    def on_joybuttonup(self, button):
        """
        Delegate joystick button up event
        :param button: button number
        """
        self.boards[self.board_id].on_joybuttonup(button)

    def on_joyaxismotion(self, axis, value):
        """
        Delegate joystick axis motion event
        :param axis: axis number (0: X, 1: Y)
        :param value:
        """
        self.boards[self.board_id].on_joyaxismotion(axis, int(value))

    def on_mouseup(self, button, pos):
        """
        Delegate mouse button up event
        :param button: button number
        :param pos: cursor position
        """
        self.boards[self.board_id].on_mouseup(button, pos)

    def on_timer(self, timer):
        """
        Delegate timer event
        :param timer: timer identifier
        """
        self.boards[self.board_id].on_timer(timer)

    def on_paint(self):
        """
        Paint event handler
        """
        self.boards[self.board_id].on_paint()

    def on_keyup(self, key):
        """
        Key release handler
        :param key: key code
        """
        self.boards[self.board_id].on_keyup(key)

    def on_update(self, delta):
        """
        Update event handler
        :param delta: delta time from last frame
        """
        self.boards[self.board_id].on_update(delta)
