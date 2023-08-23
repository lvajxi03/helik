#!/usr/bin/env python3

"""
All the resources
"""

import pygame
from helik.hdefs import ARENA_WIDTH, ARENA_HEIGHT


class ResourceManager:
    """
    Resource Manager class
    """
    def __init__(self, basepath):
        self.resources = {}
        self.create_resources(basepath)

    def create_resources(self, basepath):
        """
        Load all resources
        """
        self.resources = {
            "images": {
                "default-background": pygame.image.load(basepath.joinpath("back-default.jpg"))
            },
            'fonts': {
                "heading": pygame.font.Font(basepath.joinpath('ehs.ttf'), 164),
                "menu": pygame.font.Font(basepath.joinpath('ehs.ttf'), 48)
            },
            "surfaces": {
                "screen": pygame.display.set_mode((ARENA_WIDTH, ARENA_HEIGHT), flags=pygame.SRCALPHA, depth=32,
                                                  vsync=1),
                "buffer": pygame.Surface((ARENA_WIDTH, ARENA_HEIGHT), pygame.SRCALPHA),
                "status": pygame.Surface((ARENA_WIDTH, 60), pygame.SRCALPHA)
            }
        }

    def get(self, section: str, subsection: str):
        try:
            return self.resources[section][subsection]
        except KeyError:
            return None
    # That's all Folks!
