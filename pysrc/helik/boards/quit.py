#!/usr/bin/env python3

"""
Board quit handler module
"""

from helik.boards.standard import Board


class BoardQuit(Board):
    """
    Board quit handler class
    """
    def __init__(self, parent):
        """
        Board quit class constructor
        """
        super().__init__(parent)

    def activate(self):
        """
        Activate board event handler
        """
        self.arena.running = False
