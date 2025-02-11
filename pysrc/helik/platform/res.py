#!/usr/bin/env python3

"""
All the resources
"""
import json
import os
import pygame
from helik.hdefs import ARENA_WIDTH, ARENA_HEIGHT, LEVELNO, ALL_CHARS
from helik.platform import render_keys_labels, render_buttons_labels


characters = ['abcdefgh', 'ijklmnop', 'qrstuvwx', 'yz.-_012', '3456789#']


class ResourceManager:
    """
    Resource Manager class
    """
    misc: dict = {}
    resources: dict = {}
    fonts: dict = {}
    colors: dict = {}
    pages: dict = {}
    levels: list = []
    digits: dict = {}
    images: dict = {}
    surfaces = {}
    letters = {}
    level_planes = {}
    locale = {}
    keylabels: dict = {}
    button_labels: dict = {}

    def __init__(self, basepath):
        """
        Create ResourceManager instance
        :param basepath: root directory of all resources
        """
        self.surfaces = {
            "buffer": pygame.display.set_mode(
                (ARENA_WIDTH, ARENA_HEIGHT),
            ), # flags=pygame.FULLSCREEN | pygame.NOFRAME),
            "status": pygame.Surface((ARENA_WIDTH, 60), pygame.SRCALPHA)
        }
        self.rectangles = {
            "lang-rectangles": {
                "pl": pygame.Rect(ARENA_WIDTH - 154, ARENA_HEIGHT - 58, 75, 56),
                "en": pygame.Rect(ARENA_WIDTH - 77, ARENA_HEIGHT - 58, 75, 56)
            }
        }
        self.load_resources(basepath)

        pygame.draw.rect(self.surfaces["status"],
                         self.colors["status-color"], (0, 0, ARENA_WIDTH, 60))

    def load_misc_data(self, basepath):
        """
        Load misc data from a JSON file
        :param basepath: root directory of all resources
        """
        f_name = basepath.joinpath("misc.json")
        try:
            with open(f_name, encoding='utf-8') as f_handle:
                self.misc = json.load(f_handle)
        except IOError:
            pass

    def load_resources(self, basepath):
        """
        Load all resources
        :param basepath: root directory of all resources
        """
        self.load_fonts(basepath)
        self.load_colors(basepath)
        self.load_misc_data(basepath)
        self.load_images(basepath)
        self.load_digits(basepath)
        self.load_labels(basepath)
        self.keylabels = render_keys_labels(self.misc, self.fonts, self.colors)
        self.button_labels = render_buttons_labels(self.misc, self.fonts, self.colors)
        self.load_level_planes(basepath)
        self.load_levels(basepath)
        self.create_letters(self.fonts["screen-keyboard"], self.colors["snowy-white"])
        trav = basepath.joinpath("pages")
        self.pages = self.read_labels(trav)

    def load_fonts(self, basepath):
        """
        Load fonts data and create Font objects
        from fonts.json
        :param basepath: root directory of all resources
        """
        f_name = basepath.joinpath("fonts.json")
        try:
            with open(f_name, encoding="utf-8") as f_handle:
                data = json.load(f_handle)["fonts"]
                for name in data:
                    dt = data[name]
                    self.fonts[name] = pygame.font.Font(basepath.joinpath("fonts").joinpath(dt[0]),
                                                        dt[1])
        except IOError:
            pass

    def read_pages(self, basepath):
        """
        Recursively read pages data from fancy directory structures
        :param basepath: root directory of all resources
        """
        ret = {}
        objs = os.listdir(basepath)
        for obj in objs:
            fp = os.path.join(basepath, obj)
            if os.path.isdir(fp):
                ret[obj.lower()] = self.read_pages(fp)
            if os.path.isfile(fp):
                _, ex = os.path.splitext(fp)
                if ex.lower() == ".json":
                    try:
                        with open(fp, encoding='utf-8') as fh:
                            js = json.load(fh)
                            ret.update(js)
                    except IOError:
                        pass
        return ret

    def read_labels(self, basepath):
        """
        Recursively read labels data from fancy directory structures
        :param basepath: root directory of all resources
        """
        ret = {}
        objs = os.listdir(basepath)
        for obj in objs:
            fp = os.path.join(basepath, obj)
            if os.path.isdir(fp):
                ret[obj.lower()] = self.read_labels(fp)
            if os.path.isfile(fp):
                _, ex = os.path.splitext(obj)
                if ex.lower() == ".json":
                    try:
                        with open(fp, encoding='utf-8') as fh:
                            js = json.load(fh)
                            ret.update(js)
                    except IOError:
                        pass
        return ret

    def load_labels(self, basepath):
        """
        Load and create labels
        :param basepath: root directory of all resources
        """
        trav = basepath.joinpath("labels")
        content = self.read_labels(trav)
        data = {}
        # 1. Languages
        for lang in content:
            if lang not in data:
                data[lang] = {}
            for group in content[lang]:
                if group not in data[lang]:
                    data[lang][group] = {}
                for label in content[lang][group]:
                    # Font data
                    fd = content[lang][group][label]
                    rotate = 0
                    if "rotate" in fd:
                        rotate = int(fd["rotate"])
                    if fd["color"] in self.colors:
                        color = self.colors[fd["color"]]
                    else:
                        color = pygame.Color(fd["color"])
                    if "label" in fd:
                        # Single label
                        su = pygame.transform.rotate(
                            self.fonts[fd["font"]].render(
                                fd["label"],
                                True,
                                color),
                            rotate)
                        su.set_alpha(color.a)
                        r = su.get_rect()
                        data[lang][group][label] = (su, r)
                    elif "labels" in fd:
                        # List of labels
                        data[lang][group][label] = []
                        for fdx in fd["labels"]:
                            su = pygame.transform.rotate(
                                self.fonts[fd["font"]].render(
                                    fdx,
                                    True,
                                    color),
                                rotate)
                            su.set_alpha(color.a)
                            r = su.get_rect()
                            data[lang][group][label].append((su, r))
        self.locale = data

    def load_digits(self, basepath):
        """
        Load digits -- surfaces to produce numbers
        :param basepath: root directory of all resources
        """
        pa = basepath.joinpath("images").joinpath("digits")
        for i in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            fn = f"{i}.png"
            self.digits[i] = pygame.image.load(pa.joinpath(fn)).convert_alpha()

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

    def create_letters(self, font, color):
        """
        Create letters for new hiscore board
        :param font: Pygame Font object
        :param color: Pygame color object
        """
        self.letters = {}
        for letter in ALL_CHARS:
            su = font.render(
                letter,
                True,
                color)
            self.letters[letter] = su

    def load_level_planes(self, basepath):
        """
        Load images that display leven planes
        """
        self.level_planes = {}
        pa = basepath.joinpath("images").joinpath("level_planes")
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
                            self.level_planes[key].append(
                                pygame.image.load(pa.joinpath(key).joinpath(value)).convert_alpha())
                    elif type(values) is str:
                        self.level_planes[key] = pygame.image.load(pa.joinpath(
                            values)).convert_alpha()
        except IOError as ioe:
            print(ioe)

    def load_colors(self, basepath):
        """
        Load colors definitions
        """
        f_name = basepath.joinpath("colors.json")
        try:
            with open(f_name, encoding="utf-8") as f_handle:
                data = json.load(f_handle)
                for name in data["colors"]:
                    r = data["colors"][name]
                    self.colors[name] = pygame.Color(r[0], r[1], r[2], r[3])
        except IOError as ioe:
            print(ioe)

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
                            self.images[key].append(pygame.image.load(
                                pa.joinpath(key).joinpath(elem)).convert_alpha())
                    elif type(value) is dict:
                        self.images[key] = {}
                        for elem in value:
                            self.images[key][elem] = pygame.image.load(
                                pa.joinpath(key).joinpath(value[elem])).convert_alpha()
                    elif type(value) is str:
                        self.images[key] = pygame.image.load(pa.joinpath(value)).convert_alpha()
        except IOError as ioe:
            print(ioe)

    # That's all Folks!
