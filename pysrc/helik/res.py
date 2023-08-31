#!/usr/bin/env python3

"""
All the resources
"""

import pygame
from helik.hdefs import ARENA_WIDTH, ARENA_HEIGHT
from helik.htypes import BoardType
from helik.locale import locale


class ResourceManager:
    """
    Resource Manager class
    """
    def __init__(self, basepath):
        self.resources = {}
        self.create_resources(basepath)

    def create_resources(self, basepath):
        """
        Load all resources
        """
        self.resources = {
            "images": {
                "default-background": pygame.image.load(basepath.joinpath("back-default.jpg")),
                "helik-small-left": pygame.image.load(basepath.joinpath("copter-white-left.png")),
                "helik-small-right": pygame.image.load(basepath.joinpath("copter-white-right.png"))
            },
            "fonts": {
                "heading": pygame.font.Font(basepath.joinpath('ehs.ttf'), 164),
                "menu": pygame.font.Font(basepath.joinpath('ehs.ttf'), 48),
                "prepare": pygame.font.Font(basepath.joinpath('ehs.ttf'), 512)
            },
            "surfaces": {
                "screen": pygame.display.set_mode((ARENA_WIDTH, ARENA_HEIGHT), flags=pygame.SRCALPHA, depth=32,
                                                  vsync=1),
                "buffer": pygame.Surface((ARENA_WIDTH, ARENA_HEIGHT), pygame.SRCALPHA),
                "status": pygame.Surface((ARENA_WIDTH, 60), pygame.SRCALPHA)
            }
        }
        for ty in locale:
             for name in locale[ty]:
                if isinstance(locale[ty][name]["pl"], list):
                    locale[ty][name]["label"] = {
                        "pl": [],
                        "en": []}
                    for elem in locale[ty][name]["pl"]:
                        label = pygame.transform.rotate(
                            self.get(
                                "fonts",
                                locale[ty][name]["font"]).render(
                                    elem,
                                    True,
                                    pygame.Color(locale[ty][name]["color"])),
                            locale[ty][name]["rotate"])
                        rect = label.get_rect()
                        locale[ty][name]["label"]["pl"].append((label, rect))
                        label = pygame.transform.rotate(
                            self.get(
                                "fonts",
                                locale[ty][name]["font"]).render(
                                    elem,
                                    True,
                                    pygame.Color(locale[ty][name]["color"])),
                            locale[ty][name]["rotate"])
                        rect = label.get_rect()
                        locale[ty][name]["label"]["en"].append((label, rect))
                else:
                    locale[ty][name]["label"] = {}
                    label = pygame.transform.rotate(
                        self.get(
                            "fonts",
                            locale[ty][name]["font"]).render(
                                locale[ty][name]["pl"],
                                True,
                                pygame.Color(
                                    locale[ty][name]["color"])),
                        locale[ty][name]["rotate"])
                    rect = label.get_rect()
                    locale[ty][name]["label"]["pl"] = (label, rect)
                    label = pygame.transform.rotate(
                        self.get(
                            "fonts",
                            locale[ty][name]["font"]).render(
                                locale[ty][name]["en"],
                                True,
                                pygame.Color(
                                    locale[ty][name]["color"])),
                        locale[ty][name]["rotate"])
                    rect = label.get_rect()
                    locale[ty][name]["label"]["en"] = (label, rect)
        # Quirks and hacks:
        for l in ["1", "2", "3"]:
            label, rect = self.get_label(BoardType.GAME, l, "pl")
            rect = label.get_rect()
            rect.center = (ARENA_WIDTH//2, ARENA_HEIGHT//2)
            self.set_label(BoardType.GAME, l, "pl", (label, rect))
            self.set_label(BoardType.GAME, l, "en", (label, rect))

    def get(self, section: str, subsection: str):
        try:
            return self.resources[section][subsection]
        except KeyError:
            return None

    def get_label(self, board, name, lang):
        try:
            return locale[board][name]["label"][lang]
        except KeyError:
            return None

    def set_label(self, board, name, lang, newval):
        """
        set_label is necessary for quirks and hacks
        in `create_resources`
        :param board: board type
        :param name: label name
        :param lang: current lang
        :param newval: new tuple with label and its rect
        """
        try:
            locale[board][name]["label"][lang] = newval
        except KeyError:
            return None

    def set_alpha(self, board, name, lang, alpha):
        try:
            rec = locale[board][name]["label"][lang]
            if isinstance(rec, list):
                for elem in list:
                    lab, re = elem
                    lab.set_alpha(alpha)
            else:
                lab, re = rec
                lab.set_alpha(alpha)
        except KeyError:
            return None

    # That's all Folks!
