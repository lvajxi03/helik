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
from helik.boards.menu import BoardMenu
from helik.res import create_resources

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
        self.screen = pygame.display.set_mode((ARENA_WIDTH, ARENA_HEIGHT), flags=pygame.SRCALPHA, depth=32, vsync=1)
        self.resources = create_resources(files('helik.resources'))

        self.buffer = pygame.Surface((ARENA_WIDTH, ARENA_HEIGHT), pygame.SRCALPHA)
        self.lang = "pl"
        pygame.display.set_caption(APPLICATION_TITLE)
        self.clock = pygame.time.Clock()
        self.running = True
        self.boards = {
            BoardType.WELCOME: BoardWelcome(self),
            BoardType.MENU: BoardMenu(self)
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
                elif event.type == pygame.KEYDOWN:
                    self.on_keydown(event.key)
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
        self.screen.blit(self.buffer, (0, 0))

    def on_keydown(self, key):
        """
        Keydown event handler
        :param key: key that was pressed
        """
        if key == pygame.K_q:
            self.running = False
        else:
            self.boards[self.board_id].on_keydown(key)

