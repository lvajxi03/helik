#!/usr/bin/env python3

"""
Level viewer module
"""

import sys
from importlib.resources import files
import pygame
from helik.board import BoardViewer
from helik.media.audio import AudioController
from helik.platform import ResourceManager


class LevelViewer:
    """
    LevelViewer,
    Arena-like viewer
    """
    def __init__(self, levelfile: str):
        pygame.init()
        self.running = True
        self.clock = pygame.time.Clock()
        self.resman = ResourceManager(files('helik.resources'))
        self.audio = AudioController(self, files('helik.resources'))
        pygame.display.set_caption("HeliK Level Viewer")
        self.board = BoardViewer(self, levelfile)

    def run(self):
        """
        Run the event loop
        """
        self.board.activate()
        while self.running:
            for event in pygame.event.get():
                match event.type:
                    case pygame.QUIT:
                        self.running = False
                    case pygame.KEYUP:
                        self.on_keyup(event.key)
                    case pygame.MOUSEBUTTONUP:
                        self.on_mouseup(event.button, event.pos)
                    case _:
                        if event.type > pygame.USEREVENT:
                            self.on_timer(event.type)

            _ = self.clock.tick(1000)
            self.on_paint()
            pygame.display.update()

    def on_paint(self):
        """
        Paint event handler
        """
        self.board.on_paint()

    def on_keyup(self, key):
        """
        Key release handler
        :param key: key code
        """
        self.board.on_keyup(key)

    def on_mouseup(self, button, pos):
        """
        Delegate mouse button up event
        :param button: button number
        :param pos: cursor position
        """
        self.board.on_mouseup(button, pos)

    def on_timer(self, timer):
        """
        Delegate timer event
        :param timer: timer identifier
        """
        self.board.on_timer(timer)


if __name__ == "__main__":
    try:
        LevelViewer(sys.argv[1]).run()
    except IndexError:
        print("Usage:")
        print(f"{sys.argv[0]} <level-filename>")
        sys.exit(1)
