#!/usr/bin/env python3

"""
All the resources
"""

import json
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
        self.images = {}
        self.digits = {}
        self.clouds = []
        self.levels = []
        self.colors = {}
        self.buildings = []
        self.fonts = {}
        self.surfaces = {}
        self.explosions = []
        self.dircs = []
        self.plane_levels = {"pl": [], "en": []}
        self.create_resources(basepath)

    def create_resources(self, basepath):
        """
        Load all resources
        """
        # Fonts
        f_name = basepath.joinpath("fonts.json")
        try:
            with open(f_name) as f_handle:
                self.fonts = json.load(f_handle)["fonts"]
                for name in self.fonts:
                    dt = self.fonts[name]
                    self.fonts[name] = pygame.font.Font(basepath.joinpath(dt[0]), dt[1])
        except IOError:
            pass
        f_name = basepath.joinpath("images.json")
        try:
            with open(f_name) as f_handle:
                data = json.load(f_handle)
                for name in data["general"]:
                    self.images[name] = pygame.image.load(basepath.joinpath(data["general"][name]))
                for name in data["digits"]:
                    self.digits[name] = pygame.image.load(basepath.joinpath(data["digits"][name]))
                for name in data["clouds"]:
                    self.clouds.append(pygame.image.load(basepath.joinpath(name)))
                for name in data["buildings"]:
                    self.buildings.append(pygame.image.load(basepath.joinpath(name)))
                for name in data["explosions"]:
                    self.explosions.append(pygame.image.load(basepath.joinpath(name)))
                for name in data["dirc"]:
                    self.dircs.append(pygame.image.load(basepath.joinpath(name)))
                for name in data["pl-plane-levels"]:
                    self.plane_levels["pl"].append(pygame.image.load(basepath.joinpath(name)))
                for name in data["en-plane-levels"]:
                    self.plane_levels["en"].append(pygame.image.load(basepath.joinpath(name)))
        except IOError as ioe:
            print(str(ioe))

        f_name = basepath.joinpath("colors.json")
        try:
            with open(f_name) as f_handle:
                data = json.load(f_handle)
                for name in data["colors"]:
                    r = data["colors"][name]
                    self.colors[name] = pygame.Color(r[0], r[1], r[2], r[3])
        except IOError:
            pass

        self.surfaces = {
            "buffer": pygame.display.set_mode((ARENA_WIDTH, ARENA_HEIGHT), flags=pygame.SRCALPHA, depth=32,
                                              vsync=1),
            "status": pygame.Surface((ARENA_WIDTH, 60), pygame.SRCALPHA)
        }
        self.resources = {
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
        f_name = basepath.joinpath("levels.json")
        try:
            with open(f_name) as f_handle:
                self.levels = json.load(f_handle)["levels"]
        except IOError:
            pass
        except KeyError:
            pass

        # Labels
        for ty in locale:
             for name in locale[ty]:
                if isinstance(locale[ty][name]["pl"], list):
                    locale[ty][name]["label"] = {
                        "pl": [],
                        "en": []}
                    for elem in locale[ty][name]["pl"]:
                        label = pygame.transform.rotate(
                            self.fonts[locale[ty][name]["font"]].render(
                                elem,
                                True,
                                pygame.Color(locale[ty][name]["color"])),
                            locale[ty][name]["rotate"])
                        pygame.image.save(label, f"{ty}-{name}-{elem}-pl.png")
                        rect = label.get_rect()
                        locale[ty][name]["label"]["pl"].append((label, rect))
                    for elem in locale[ty][name]["en"]:
                        label = pygame.transform.rotate(
                            self.fonts[locale[ty][name]["font"]].render(
                                elem,
                                True,
                                pygame.Color(locale[ty][name]["color"])),
                            locale[ty][name]["rotate"])
                        pygame.image.save(label, f"{ty}-{name}-{elem}-en.png")
                        rect = label.get_rect()
                        locale[ty][name]["label"]["en"].append((label, rect))
                else:
                    locale[ty][name]["label"] = {}
                    label = pygame.transform.rotate(
                        self.fonts[locale[ty][name]["font"]].render(
                            locale[ty][name]["pl"],
                            True,
                            pygame.Color(
                                locale[ty][name]["color"])),
                        locale[ty][name]["rotate"])
                    pygame.image.save(label, f"{ty}-{name}-pl.png")
                    rect = label.get_rect()
                    locale[ty][name]["label"]["pl"] = (label, rect)
                    label = pygame.transform.rotate(
                      self.fonts[locale[ty][name]["font"]].render(
                          locale[ty][name]["en"],
                          True,
                          pygame.Color(
                              locale[ty][name]["color"])),
                        locale[ty][name]["rotate"])
                    rect = label.get_rect()
                    locale[ty][name]["label"]["en"] = (label, rect)
                    pygame.image.save(label, f"{ty}-{name}-en.png")
        # Quirks and hacks:
        for l in ["1", "2", "3"]:
            label, rect = self.get_label(BoardType.GAME, l, "pl")
            pygame.image.save(label, f"{l}-pl.png")
            rect = label.get_rect()
            rect.center = (ARENA_WIDTH//2, ARENA_HEIGHT//2)
            self.set_label(BoardType.GAME, l, "pl", (label, rect))
            self.set_label(BoardType.GAME, l, "en", (label, rect))

        # Status:
        pygame.draw.rect(self.surfaces["status"],
                         self.colors["status-color"], (0, 0, ARENA_WIDTH, 60))

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
                for elem in rec:
                    lab, re = elem
                    lab.set_alpha(alpha)
            else:
                lab, re = rec
                lab.set_alpha(alpha)
        except KeyError:
            return None

    # That's all Folks!
