#!/usr/bin/env python3

"""
App module
"""

import random
from importlib.resources import files
import pygame
from helik.hdefs import ARENA_WIDTH, ARENA_HEIGHT, APPLICATION_TITLE
from helik.htypes import BoardType
from helik.boards.welcome import BoardWelcome
from helik.boards.about import BoardAbout
from helik.boards.menu import BoardMenu
from helik.boards.options import BoardOptions
from helik.boards.hiscores import BoardHiscores
from helik.boards.help import BoardHelp
from helik.boards.settings import BoardSettings
from helik.boards.game import BoardGame
from helik.boards.quit import BoardQuit
from helik.res import ResourceManager
from helik.config import Config

class Application():
    """
    Helik application
    """
    def __init__(self):
        """
        Application initializer
        """
        random.seed()
        pygame.init()
        self.res_man = ResourceManager(files('helik.resources'))
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
            BoardType.QUIT: BoardQuit(self)
            }
        self.board_id = BoardType.WELCOME

    def change_board(self, newboard):
        if newboard != self.board_id:
            self.boards[self.board_id].deactivate()
            self.board_id = newboard
            self.boards[self.board_id].activate()

    def run(self):
        """
        Main application loop
        """
        # Activate initial board
        self.boards[self.board_id].activate()

        # Main application loop
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYUP:
                    self.on_keyup(event.key)
                elif event.type == pygame.MOUSEBUTTONUP:
                    self.on_mouseup(event.button, event.pos)
                elif event.type > pygame.USEREVENT:
                    self.on_timer(event.type)
            self.on_paint()
            pygame.display.flip()
            dt = self.clock.tick(60)
            self.on_update(dt)

        # Eventually,
        self.config.save_default_config()
        pygame.quit()

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
        b = pygame.transform.flip(self.res_man.surfaces["buffer"], False, True)
        self.res_man.surfaces["screen"].blit(b, (0, 0))

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
        self.boards[self.board_id].on_update(delta/20)
