#!/usr/bin/env python3

"""
App module
"""

import pygame
import random
from importlib.resources import files
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
from helik.res import ResourceManager

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
        self.lang = "pl"
        pygame.display.set_caption(APPLICATION_TITLE)
        self.clock = pygame.time.Clock()
        self.running = True
        self.boards = {
            BoardType.WELCOME: BoardWelcome(self),
            BoardType.MENU: BoardMenu(self),
            BoardType.ABOUT: BoardAbout(self),
            BoardType.HISCORES: BoardHiscores(self),
            BoardType.HELP: BoardHelp(self),
            BoardType.OPTIONS: BoardOptions(self),
            BoardType.SETTINGS: BoardSettings(self),
            BoardType.GAME: BoardGame(self)
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
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYUP:
                    self.on_keyup(event.key)
                elif event.type > pygame.USEREVENT:
                    self.on_timer(event.type)
            self.on_paint()
            pygame.display.update()
            self.clock.tick(60)

        # Eventually,
        pygame.quit()

    def on_timer(self, timer):
        self.boards[self.board_id].on_timer(timer)

    def on_paint(self):
        """
        Paint event handler
        """
        self.boards[self.board_id].on_paint()
        self.res_man.get("surfaces", "screen").blit(self.res_man.get("surfaces", "buffer"), (0, 0))

    def on_keyup(self, key):
        """
        Key release handler
        :param key: key code
        """
        self.boards[self.board_id].on_keyup(key)

