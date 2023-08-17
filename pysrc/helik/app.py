#!/usr/bin/env python3

"""
App module
"""

import pygame
from helik.hdefs import ARENA_WIDTH, ARENA_HEIGHT


class Application():
    """
    Helik application
    """
    def __init__(self):
        """
        Application initializer
        """
        pygame.init()
        self.screen = pygame.display.set_mode((ARENA_WIDTH, ARENA_HEIGHT), pygame.FULLSCREEN)
        self.clock = pygame.time.Clock()
        self.running = True

    def run(self):
        """
        Main application loop
        """
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                keys = pygame.key.get_pressed()
                if keys[pygame.K_q]:
                    self.running = False
            self.screen.fill("purple")

            pygame.display.flip()

            self.clock.tick(60)

        # Eventually,
        pygame.quit()
