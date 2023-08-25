#!/usr/bin/env python3

"""
Mode killed handler module
"""


import pygame
from helik.modes.standard import Mode


class ModeKilled(Mode):
    """
    Mode killed handle class
    """
    def __init__(self, parent):
        """
        Mode killed class constructor
        """
        super().__init__(parent)
