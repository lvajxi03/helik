#!/usr/bin/env python3

"""
Mode play handler module
"""


import pygame
from helik.modes.standard import Mode


class ModePlay(Mode):
    """
    Mode play handle class
    """
    def __init__(self, parent):
        """
        Mode play class constructor
        """
        super().__init__(parent)
