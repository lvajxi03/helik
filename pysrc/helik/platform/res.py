#!/usr/bin/env python3

"""
All the resources
"""
import json
import os
import pygame
from helik.hdefs import ARENA_WIDTH, ARENA_HEIGHT, LEVELNO, ALL_CHARS
from .keys import render_keys_labels
from .buttons import render_buttons_labels


characters = ['abcdefgh', 'ijklmnop', 'qrstuvwx', 'yz.-_012', '3456789#']


def load_images(basepath):
    """
    Load all the images
    :basepath: root of all resounrces
    :return: images dict
    """
    images = {}
    pa = basepath.joinpath("images")
    f_path = basepath.joinpath("images.json")
    try:
        with open(f_path, encoding="utf-8") as f_handle:
            data = json.load(f_handle)
            for key in data:
                value = data[key]
                if type(value) is list:
                    images[key] = []
                    for elem in value:
                        images[key].append(pygame.image.load(
                            pa.joinpath(key).joinpath(elem)).convert_alpha())
                elif type(value) is dict:
                    images[key] = {}
                    for elem in value:
                        images[key][elem] = pygame.image.load(
                            pa.joinpath(key).joinpath(value[elem])).convert_alpha()
                elif type(value) is str:
                    images[key] = pygame.image.load(pa.joinpath(value)).convert_alpha()
    except IOError as ioe:
        raise

    return images


def load_misc_data(basepath):
    """
    Load misc data from a JSON file
    :param basepath: root directory of all resources
    :return: misc data dict
    """
    f_name = basepath.joinpath("misc.json")
    misc = {}
    try:
        with open(f_name, encoding='utf-8') as f_handle:
            misc = json.load(f_handle)
    except IOError:
        pass
    return misc


def load_level_planes(basepath):
    """
    Load images that display leven planes.
    Level planes are images, but bound to lang
    (both images and locales)
    :param basepath: root of all resources
    :return: level planes dict
    """
    level_planes = {}
    pa = basepath.joinpath("images").joinpath("level_planes")
    f_path = pa.joinpath("level-planes.json")
    try:
        with open(f_path, encoding="utf-8") as f_handle:
            data = json.load(f_handle)
            for key in data:
                values = data[key]
                if type(values) is list:
                    if key not in level_planes:
                        level_planes[key] = []
                    for value in values:
                        level_planes[key].append(
                            pygame.image.load(pa.joinpath(key).joinpath(value)).convert_alpha())
                elif type(values) is str:
                    level_planes[key] = pygame.image.load(pa.joinpath(
                        values)).convert_alpha()
    except IOError as ioe:
        raise
    return level_planes


def create_letters(font, color):
    """
    Create letters for new hiscore board
    :param font: Pygame Font object
    :param color: Pygame color object
    :return: letters dictionary
    """
    letters = {}
    for letter in ALL_CHARS:
        su = font.render(
            letter,
            True,
            color)
        letters[letter] = su
    return letters


def load_levels(basepath) -> list:
    """
    Load levels data from resorces
    :param basepath: root directory of all resources
    :return: levels data list
    """
    levels = []
    pa = basepath.joinpath("levels")
    for i in range(LEVELNO):
        f_path = pa.joinpath(f"{i}.json")
        with open(f_path, encoding="utf-8") as f_handle:
            d = json.load(f_handle)
            levels.append(d)
    return levels


def load_colors(basepath) -> dict:
    """
    Load colors definitions
    :param basepath: root directory of all resources
    :return: colors data
    """
    colors = {}
    f_name = basepath.joinpath("colors.json")
    try:
        with open(f_name, encoding="utf-8") as f_handle:
            data = json.load(f_handle)
            for name in data["colors"]:
                r = data["colors"][name]
                colors[name] = pygame.Color(r[0], r[1], r[2], r[3])
    except IOError as ioe:
        raise
    return colors


def load_fonts(basepath) -> dict:
    """
    Load fonts data and create Font object from fonts.json
    :param basepath: root directory of all resources
    :return: font data dict
    """
    fonts = {}
    f_name = basepath.joinpath("fonts.json")
    try:
        with open(f_name, encoding="utf-8") as f_handle:
            data = json.load(f_handle)["fonts"]
            for name in data:
                dt = data[name]
                fonts[name] = pygame.font.Font(basepath.joinpath("fonts").joinpath(dt[0]),
                                                    dt[1])
    except IOError:
        pass
    return fonts


def read_labels(basepath) -> dict:
    """
    Recursively read labels data from fancy directory structures
    :param basepath: root directory of all resources
    :return: labels data
    """
    ret = {}
    objs = os.listdir(basepath)
    for obj in objs:
        fp = os.path.join(basepath, obj)
        if os.path.isdir(fp):
            ret[obj.lower()] = read_labels(fp)
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


def create_labels(fonts, colors, basepath):
    """
    Create labels.
    :param fonts: definition of fonts
    :param colors: definition of colors
    :param basepath: root directory of all resources
    :return: all labels
    """
    trav = basepath.joinpath("labels")
    content = read_labels(trav)
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
                if fd["color"] in colors:
                    color = colors[fd["color"]]
                else:
                    color = pygame.Color(fd["color"])
                if "label" in fd:
                    # Single label
                    su = pygame.transform.rotate(
                        fonts[fd["font"]].render(
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
                            fonts[fd["font"]].render(
                                fdx,
                                True,
                                color),
                            rotate)
                        su.set_alpha(color.a)
                        r = su.get_rect()
                        data[lang][group][label].append((su, r))
    try:
        # move "common/common" to single "common" only
        data["common"] = data["common"]["common"]
    except KeyError:
        pass

    return data


class ResourceManager:
    """
    Resource Manager class
    """
    def __init__(self, basepath):
        """
        Create ResourceManager instance
        :param basepath: root directory of all resources
        """
        self.misc = {}
        self.resources = {}
        self.fonts = {}
        self.colors = {}
        self.pages = {}
        self.levels = []
        self.images = {}
        self.surfaces = {}
        self.letters = {}
        self.level_planes = {}
        self.locale = {}
        self.keylabels = {}
        self.button_labels = {}
        self.surfaces = {
            "buffer": pygame.display.set_mode(
                (ARENA_WIDTH, ARENA_HEIGHT),
                    flags=pygame.FULLSCREEN | pygame.NOFRAME),
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

    def load_resources(self, basepath):
        """
        Load all resources
        :param basepath: root directory of all resources
        """
        self.fonts = load_fonts(basepath)
        self.colors = load_colors(basepath)
        self.misc = load_misc_data(basepath)
        self.images = load_images(basepath)
        self.locale = create_labels(self.fonts, self.colors, basepath)
        self.keylabels = render_keys_labels(self.misc, self.fonts, self.colors)
        self.button_labels = render_buttons_labels(self.misc, self.fonts, self.colors)
        self.level_planes = load_level_planes(basepath)
        self.levels = load_levels(basepath)
        self.letters = create_letters(self.fonts["screen-keyboard"], self.colors["snowy-white"])
        self.pages = read_labels(basepath.joinpath("pages"))

    # That's all Folks!
