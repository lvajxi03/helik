#!/usr/bin/env python3

"""
Mode paused handler module
"""


import pygame
from helik.modes.standard import Mode


class ModePaused(Mode):
    """
    Mode paused handle class
    """
    def __init__(self, parent):
        """
        Mode paused class constructor
        """
        super().__init__(parent)
