#!/usr/bin/env python3

"""
Standard game mode
"""

import pygame


class Mode:
    """
    Generic mode handler class
    """
    def __init__(self, game):
        self.game = game
        self.arena = self.game.parent
        self.res_man = self.arena.res_man

    def activate(self):
        """
        Activate event handler
        """

    def deactivate(self):
        """
        Deactivate event handler
        """

    def on_paint(self):
        """
        Paint event handler
        """

    def on_keyup(self, key):
        """
        Key release event handler
        :param key: key code
        """

    def on_timer(self, timer):
        """
        Timer event handler
        :param timer: timer type
        """
