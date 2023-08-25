#!/usr/bin/env python3

"""
Mode prepare handler module
"""


import pygame
from helik.modes.standard import Mode


class ModePrepare(Mode):
    """
    Mode prepare handle class
    """
    def __init__(self, parent):
        """
        Mode prepare class constructor
        """
        super().__init__(parent)
