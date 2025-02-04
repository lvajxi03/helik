#!/usr/bin/env python3

"""
Platform buttons module
"""

import enum
import pygame


@enum.unique
class ButtonType(enum.IntEnum):
    """
    Common buttons definiton
    """
    X = 0
    A = 1
    B = 2
    Y = 3
    LEFT = 4
    RIGHT = 5
    SELECT = 8
    START = 9


buttons_allowed = [
    ButtonType.X,
    ButtonType.A,
    ButtonType.B,
    ButtonType.Y,
    ButtonType.LEFT,
    ButtonType.RIGHT]


button_names = {
    "pl": {
        ButtonType.X: "X",
        ButtonType.A: "A",
        ButtonType.B: "B",
        ButtonType.Y: "Y",
        ButtonType.LEFT: "Lewy",
        ButtonType.RIGHT: "Prawy"
    },
    "en": {
        ButtonType.X: "X",
        ButtonType.A: "A",
        ButtonType.B: "B",
        ButtonType.Y: "Y",
        ButtonType.LEFT: "Left",
        ButtonType.RIGHT: "Right"
    }
}


def render_buttons_labels(misc: dict, fonts: dict, colors: dict) -> dict:
    """
    Render labels with all key names, in various langs
    :param misc:
    :param fonts: font data
    :param colors: colors data
    :return dict: rendered labels
    """
    data = {"shadows": {}, "buttons": {}}
    # do the shadows:
    for lang in button_names:
        data["shadows"][lang] = {}
        for elem in button_names[lang]:
            if misc["keys-and-buttons"]["color"] in colors:
                color = colors[misc["keys-and-buttons-shadow"]["color"]]
            else:
                color = pygame.Color(misc["keys-and-buttons-shadow"]["color"])
            su = pygame.transform.rotate(
                fonts[misc["keys-and-buttons-shadow"]["font"]].render(
                    button_names[lang][elem],
                    True,
                    color),
                misc["keys-and-buttons-shadow"]["rotate"]
            )
            su.set_alpha(color.a)
            data["shadows"][lang][elem] = su
    # do the buttons:
    for lang in button_names:
        data["buttons"][lang] = {}
        for elem in button_names[lang]:
            if misc["keys-and-buttons"]["color"] in colors:
                color = colors[misc["keys-and-buttons"]["color"]]
            else:
                color = pygame.Color(misc["keys-and-buttons"]["color"])
            su = pygame.transform.rotate(
                fonts[misc["keys-and-buttons"]["font"]].render(
                    button_names[lang][elem],
                    True,
                    color),
                misc["keys-and-buttons"]["rotate"]
            )
            su.set_alpha(color.a)
            data["buttons"][lang][elem] = su
    return data
