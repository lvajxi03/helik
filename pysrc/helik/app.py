#!/usr/bin/env python3

"""
App module
"""

import pygame
from helik.hdefs import ARENA_WIDTH, ARENA_HEIGHT, APPLICATION_TITLE
from helik.boards.menu import BoardMenu

class Application():
    """
    Helik application
    """
    def __init__(self):
        """
        Application initializer
        """
        pygame.init()
        self.screen = pygame.display.set_mode((ARENA_WIDTH, ARENA_HEIGHT))
        pygame.display.set_caption(APPLICATION_TITLE)
        self.clock = pygame.time.Clock()
        self.running = True
        self.menu = BoardMenu(self)

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
            pygame.display.flip()
            self.clock.tick(60)

        # Eventually,
        pygame.quit()

    def on_timer(self, timer):
        self.menu.on_timer(timer)

    def on_paint(self):
        """
        Paint event handler
        """
        self.menu.on_paint()

    def on_keydown(self, key):
        """
        Keydown event handler
        :param key: key that was pressed
        """
        if key == pygame.K_q:
            self.running = False
