#!/usr/bin/env python3

"""
Standard game mode
"""


class Mode:
    """
    Generic mode handler class
    """
    def __init__(self, game):
        self.game = game
        self.arena = self.game.arena
        self.buffer = self.game.buffer
        self.res_man = self.arena.res_man
        self.images = self.res_man.images

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

    def on_update(self, delta):
        """
        Update event handler
        :param delta: delta time from last frame
        """
