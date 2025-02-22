#!/usr/bin/env python3

"""
Level viewer board
"""

import json
from helik.game import Level
from .standard import Board


class BoardViewer(Board):
    """
    Viewer Board
    """
    def __init__(self, parent, levelfile: str):
        super().__init__(parent)
        self.levelfile = levelfile
        self.level = None
        self.load()

    def load(self):
        """
        (re)Load level data
        """
        with open(self.levelfile, encoding='utf-8') as fh:
            try:
                data = json.load(fh)
                self.resman.levels[0] = data
                self.level = Level(self.resman, 0, 0)
            except IOError as ioe:
                print(ioe)

    def on_paint(self):
        """
        Paint event handler
        """
        self.paint_default_bg()
        self.level.on_paint(self.buffer)