#!/usr/bin/env python3

"""
Standard Page module
"""

import pygame


class StaticPage:
    """
    Plain static page class definition
    """
    def __init__(self, layout: dict, resman):
        """
        Create StaticPage instance
        :param layout: page layout
        :param resman: resource manager instance
        """
        self.layers = []
        self.navigator = None
        for layer in self.layout["layers"]:
            for elem in layer:
                if elem == "image":


class StaticBook:
    """
    Group all the static pages together, plus navigator
    """
    def __init__(self):
        """
        Create StaticBook instance
        """
        self.pages = []
        self.current = 0

    def show(self):
        self.current = 0

    def prev(self):
        if self.current > 0:
            self.current -= 1

    def next(self):
        if self.current < len(self.pages) - 1:
            self.current += 1

    def append(self, page):
        self.pages.append(page)

    def on_keyup(self, key):
        if key == pygame.K_LEFT:
            self.prev()
        elif key == pygame.K_RIGHT:
            self.next()
