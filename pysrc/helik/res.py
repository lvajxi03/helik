#!/usr/bin/env python3

"""
All the resources
"""

import pygame
from helik.hdefs import ARENA_WIDTH, ARENA_HEIGHT, STATUS_HEIGHT
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
                "helik-small-right": pygame.image.load(basepath.joinpath("copter-white-right.png")),
                "plane-small-left": pygame.image.load(basepath.joinpath("samolot.png")),
                "line-0": pygame.image.load(basepath.joinpath("line-0.png")),
                "wiezowiec-a": pygame.image.load(basepath.joinpath("wiezowiec-a.png")),
                "wiezowiec-b": pygame.image.load(basepath.joinpath("wiezowiec-b.png")),
                "fabryka-a": pygame.image.load(basepath.joinpath("fabryka-a.png")),
                "dom-a": pygame.image.load(basepath.joinpath("dom-a.png")),
                "bullet-1": pygame.image.load(basepath.joinpath("bullet-1.png")),
                "bullet-2": pygame.image.load(basepath.joinpath("bullet-2.png")),
                "flag-pl": pygame.image.load(basepath.joinpath("flag_pl.png")),
                "flag-en": pygame.image.load(basepath.joinpath("flag_en.png")),
                "heart-b": pygame.image.load(basepath.joinpath("heart-b.png"))
            },
            "digits": {
                "0": pygame.image.load(basepath.joinpath("0.png")),
                "1": pygame.image.load(basepath.joinpath("1.png")),
                "2": pygame.image.load(basepath.joinpath("2.png")),
                "3": pygame.image.load(basepath.joinpath("3.png")),
                "4": pygame.image.load(basepath.joinpath("4.png")),
                "5": pygame.image.load(basepath.joinpath("5.png")),
                "6": pygame.image.load(basepath.joinpath("6.png")),
                "7": pygame.image.load(basepath.joinpath("7.png")),
                "8": pygame.image.load(basepath.joinpath("8.png")),
                "9": pygame.image.load(basepath.joinpath("9.png")),
            },
            "colors": {
                "status-color": pygame.Color(128, 128, 128, 128),
            },
            "fonts": {
                "heading": pygame.font.Font(basepath.joinpath('ehs.ttf'), 164),
                "heading2": pygame.font.Font(basepath.joinpath('ehs.ttf'), 96),
                "big-message": pygame.font.Font(basepath.joinpath('ehs.ttf'), 128),
                "menu": pygame.font.Font(basepath.joinpath('ehs.ttf'), 48),
                "prepare": pygame.font.Font(basepath.joinpath('ehs.ttf'), 512)
            },
            "surfaces": {
                "buffer": pygame.display.set_mode((ARENA_WIDTH, ARENA_HEIGHT), flags=pygame.SRCALPHA, depth=32,
                                                  vsync=1),
                "status": pygame.Surface((ARENA_WIDTH, 60), pygame.SRCALPHA)
            },
            "lang-rectangles": {
                "pl": pygame.Rect(ARENA_WIDTH - 154, ARENA_HEIGHT - 58, 75, 56),
                "en": pygame.Rect(ARENA_WIDTH - 77, ARENA_HEIGHT - 58, 75, 56)
                },
            "levels": [
                [0, 0, 0, 1, 0, 1, 2, 1, 0, 1, 3, 1, 0, 2, 0, 1, 2],
                [0, 0, 1, 2, 3, 2, 1, 0, 1, 2, 3, 2, 1, 0, 1, 2, 3],
                [0, 1, 2, 3, 2, 1, 0, 1, 2, 3, 2, 1, 0, 1, 2, 3, 2],
                [1, 2, 3, 2, 1, 2, 2, 3, 3, 2, 2, 1, 1, 2, 2, 3, 2],
                [2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 3, 2, 2]
                ]
        }
        # Objects:
        # 1. Bottom objects
        self.bottom_objects = []
        for name in ["line-0", "wiezowiec-a", "wiezowiec-b", "fabryka-a", "dom-a"]:
            obj = self.resources["images"][name]
            rec = obj.get_rect()
            rec.y = ARENA_HEIGHT - STATUS_HEIGHT - rec.h
            self.bottom_objects.append((obj, rec))

        # Labels
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
                    for elem in locale[ty][name]["en"]:
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

        # Status:
        pygame.draw.rect(self.get("surfaces", "status"),
                         self.get("colors", "status-color"), (0, 0, ARENA_WIDTH, 60))

    def get(self, section: str, subsection: str):
        try:
            return self.resources[section][subsection]
        except KeyError:
            return None

    def get_index(self, section, index: int):
        try:
            return self.resources[section][index]
        except IndexError:
            return None

    def get_section(self, section: str):
        """
        Get all section data from resources
        :param section: section name
        :return section data (dict) or None
        """
        try:
            return self.resources[section]
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
            pass

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
