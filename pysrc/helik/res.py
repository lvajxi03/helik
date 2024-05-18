#!/usr/bin/env python3

"""
All the resources
"""

import sys
import json
import pygame
from helik.hdefs import ARENA_WIDTH, ARENA_HEIGHT, LEVELNO


class ResourceManager:
    """
    Resource Manager class
    """

    def __init__(self, basepath):
        """
        Create ResourceManager instance
        :param basepath: root directory of all resources
        """
        self.resources = {}
        self.images = {}
        self.digits = {}
        self.levels = []
        self.colors = {}
        self.surfaces = {}
        self.level_planes = {}
        self.surfaces = {
            "buffer": pygame.display.set_mode(
                (ARENA_WIDTH, ARENA_HEIGHT),
                flags=pygame.SRCALPHA | pygame.FULLSCREEN | pygame.NOFRAME,
                depth=32,
                vsync=1),
            "status": pygame.Surface((ARENA_WIDTH, 60), pygame.SRCALPHA)
        }
        self.rectangles = {
            "lang-rectangles": {
                "pl": pygame.Rect(ARENA_WIDTH - 154, ARENA_HEIGHT - 58, 75, 56),
                "en": pygame.Rect(ARENA_WIDTH - 77, ARENA_HEIGHT - 58, 75, 56)
            }
        }
        self.load_resources(basepath)

    def load_resources(self, basepath):
        """
        Load all resources
        :param basepath: root directory of all resources
        """
        self.load_images(basepath)
        self.load_digits(basepath)
        self.load_colors(basepath)
        self.load_level_planes(basepath)
        self.load_labels(basepath)
        self.load_levels(basepath)

    def load_digits(self, basepath):
        """
        Load digits -- surfaces to produce numbers
        :param basepath: root directory of all resources
        """
        pa = basepath.joinpath("images").joinpath("digits")
        for i in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            fn = f"{i}.png"
            self.digits[i] = pygame.image.load(pa.joinpath(fn))
        print(self.digits)

    def load_levels(self, basepath):
        """
        :param basepath: root directory of all resources
        Load levels data from resorces
        """
        pa = basepath.joinpath("levels")
        for i in range(LEVELNO):
            f_path = pa.joinpath(f"{i}.json")
            with open(f_path, encoding="utf-8") as f_handle:
                d = json.load(f_handle)
                self.levels.append(d)

    def load_labels(self, basepath):
        """
        Load labels from resources
        :param basepath: root directory of all resources
        """
        self.labels = {}
        pa = basepath.joinpath("images").joinpath("labels")
        f_path = pa.joinpath("labels.json")
        try:
            with open(f_path, encoding="utf-8") as f_handle:
                data = json.load(f_handle)
                for lang in data:
                    print(lang)
                    if lang not in self.labels:
                        self.labels[lang] = {}
                    values = data[lang]
                    for key in values:
                        value = values[key]
                        if type(value) is list:
                            self.labels[lang][key] = []
                            for elem in value:
                                img = pygame.image.load(pa.joinpath(lang).joinpath(key).joinpath(elem))
                                rect = img.get_rect()
                                self.labels[lang][key].append((img, rect))
                        elif type(value) is str:
                            img = pygame.image.load(pa.joinpath(lang).joinpath(value))
                            rect = img.get_rect()
                            self.labels[lang][key] = (img, rect)
                        elif type(value) is dict:
                            self.labels[lang][key] = {}
                            for elem in value:
                                img = pygame.image.load(pa.joinpath(lang).joinpath(key).joinpath(value[elem]))
                                rect = img.get_rect()
                                self.labels[lang][key][elem] = (img, rect)
        except IOError as ioe:
            print(str(ioe))
            sys.exit(1)

    def load_level_planes(self, basepath):
        self.level_planes = {}
        pa = basepath.joinpath("images").joinpath("level-planes")
        f_path = pa.joinpath("level-planes.json")
        try:
            with open(f_path, encoding="utf-8") as f_handle:
                data = json.load(f_handle)
                for key in data:
                    values = data[key]
                    if type(values) is list:
                        if key not in self.level_planes:
                            self.level_planes[key] = []
                        for value in values:
                            self.level_planes[key].append(pygame.image.load(pa.joinpath(key).joinpath(value)))
                    elif type(values) is str:
                        self.level_planes[key] = pygame.image.load(pa.joinpath(values))
        except IOError as ioe:
            print(str(ioe))

    def load_colors(self, basepath):
        f_name = basepath.joinpath("colors.json")
        try:
            with open(f_name, encoding="utf-8") as f_handle:
                data = json.load(f_handle)
                for name in data["colors"]:
                    r = data["colors"][name]
                    self.colors[name] = pygame.Color(r[0], r[1], r[2], r[3])
        except IOError:
            pass

    def load_images(self, basepath):
        """
        Load all the images
        """
        self.images = {}  # Clear existing images
        pa = basepath.joinpath("images")
        f_path = pa.joinpath("images.json")
        try:
            with open(f_path, encoding="utf-8") as f_handle:
                data = json.load(f_handle)
                for key in data:
                    value = data[key]
                    if type(value) is list:
                        self.images[key] = []
                        for elem in value:
                            self.images[key].append(pygame.image.load(pa.joinpath(key).joinpath(elem)))
                    elif type(value) is dict:
                        self.images[key] = {}
                        for elem in value:
                            self.images[key][elem] = pygame.image.load(pa.joinpath(key).joinpath(value[elem]))
                    elif type(value) is str:
                        self.images[key] = pygame.image.load(pa.joinpath(value))
        except IOError as ioe:
            print(str(ioe))

        # That's all Folks!
