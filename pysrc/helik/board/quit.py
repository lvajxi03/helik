#!/usr/bin/env python3

"""
Board quit handler module
"""

from .standard import Board


class BoardQuit(Board):
    """
    Board quit handler class
    """
    def activate(self, **kwargs):
        """
        Activate board event handler
        :param kwargs: additional parameters, like help or previous board
        """
        self.arena.running = False
