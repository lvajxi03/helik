#!/usr/bin/env python3

"""
Various keys definition
"""

import pygame

keysallowed = [pygame.K_F4, pygame.K_F5, pygame.K_F6, pygame.K_F7,
               pygame.K_F8, pygame.K_F9, pygame.K_F10, pygame.K_F11, pygame.K_F12,
               pygame.K_BACKSPACE, pygame.K_INSERT, pygame.K_DELETE, pygame.K_PAGEUP,
               pygame.K_PAGEDOWN, pygame.K_PAUSE, pygame.K_HOME, pygame.K_END,
               pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN,
               pygame.K_SPACE, pygame.K_w, pygame.K_e, pygame.K_r, pygame.K_t,
               pygame.K_y, pygame.K_u, pygame.K_i, pygame.K_o, pygame.K_p, pygame.K_a,
               pygame.K_s, pygame.K_d, pygame.K_f, pygame.K_g, pygame.K_h, pygame.K_i,
               pygame.K_j, pygame.K_k, pygame.K_l, pygame.K_z, pygame.K_x, pygame.K_c,
               pygame.K_v, pygame.K_b, pygame.K_n, pygame.K_m, pygame.K_BACKSLASH,
               pygame.K_SLASH, pygame.K_LEFTPAREN, pygame.K_RIGHTPAREN, pygame.K_LEFTBRACKET,
               pygame.K_RIGHTBRACKET, pygame.K_PLUS, pygame.K_MINUS, pygame.K_EQUALS,
               pygame.K_TAB, pygame.K_BACKQUOTE, pygame.K_QUOTE, pygame.K_QUOTEDBL,
               pygame.K_COMMA, pygame.K_SEMICOLON, pygame.K_QUESTION, pygame.K_GREATER]

keynames = {
    "pl": {
        pygame.K_F3: "F3",
        pygame.K_F4: "F4",
        pygame.K_F5: "F5",
        pygame.K_F6: "F6",
        pygame.K_F7: "F7",
        pygame.K_F8: "F8",
        pygame.K_F9: "F9",
        pygame.K_F10: "F10",
        pygame.K_F11: "F11",
        pygame.K_F12: "F12",
        pygame.K_BACKSPACE: "Backspace",
        pygame.K_INSERT: "Insert",
        pygame.K_DELETE: "Delete",
        pygame.K_PAGEUP: "PageUp",
        pygame.K_PAGEDOWN: "PageDown",
        pygame.K_PAUSE: "Pause",
        pygame.K_HOME: "Home",
        pygame.K_END: "End",
        pygame.K_LEFT: "←",
        pygame.K_RIGHT: "",
        pygame.K_UP: "",
        pygame.K_DOWN: "",
        pygame.K_SPACE: "Spacja",
        pygame.K_w: "W",
        pygame.K_e: "E",
        pygame.K_r: "R",
        pygame.K_t: "T",
        pygame.K_y: "Y",
        pygame.K_u: "U",
        pygame.K_i: "I",
        pygame.K_o: "O",
        pygame.K_p: "P",
        pygame.K_a: "A",
        pygame.K_s: "S",
        pygame.K_d: "D",
        pygame.K_f: "F",
        pygame.K_g: "G",
        pygame.K_h: "H",
        pygame.K_j: "J",
        pygame.K_k: "K",
        pygame.K_l: "L",
        pygame.K_z: "Z",
        pygame.K_x: "X",
        pygame.K_c: "C",
        pygame.K_v: "V",
        pygame.K_b: "B",
        pygame.K_n: "N",
        pygame.K_m: "M",
        pygame.K_BACKSLASH: "\\",
        pygame.K_SLASH: "/",
        pygame.K_LEFTPAREN: "(",
        pygame.K_RIGHTPAREN: ")",
        pygame.K_LEFTBRACKET: "[",
        pygame.K_RIGHTBRACKET: "]",
        pygame.K_PLUS: "+",
        pygame.K_MINUS: "-",
        pygame.K_EQUALS: "=",
        pygame.K_TAB: "Tabulator",
        pygame.K_BACKQUOTE: "`",
        pygame.K_QUOTE: "'",
        pygame.K_QUOTEDBL: "\"",
        pygame.K_COMMA: ",",
        pygame.K_SEMICOLON: ";",
        pygame.K_QUESTION: "?",
        pygame.K_GREATER: "<",
        pygame.K_LESS: "<"
    },
    "en": {
        pygame.K_F3: "F3",
        pygame.K_F4: "F4",
        pygame.K_F5: "F5",
        pygame.K_F6: "F6",
        pygame.K_F7: "F7",
        pygame.K_F8: "F8",
        pygame.K_F9: "F9",
        pygame.K_F10: "F10",
        pygame.K_F11: "F11",
        pygame.K_F12: "F12",
        pygame.K_BACKSPACE: "Backspace",
        pygame.K_INSERT: "Insert",
        pygame.K_DELETE: "Delete",
        pygame.K_PAGEUP: "PageUp",
        pygame.K_PAGEDOWN: "PageDown",
        pygame.K_PAUSE: "Pause",
        pygame.K_HOME: "Home",
        pygame.K_END: "End",
        pygame.K_LEFT: "←",
        pygame.K_RIGHT: "",
        pygame.K_UP: "",
        pygame.K_DOWN: "",
        pygame.K_SPACE: "Space",
        pygame.K_w: "W",
        pygame.K_e: "E",
        pygame.K_r: "R",
        pygame.K_t: "T",
        pygame.K_y: "Y",
        pygame.K_u: "U",
        pygame.K_i: "I",
        pygame.K_o: "O",
        pygame.K_p: "P",
        pygame.K_a: "A",
        pygame.K_s: "S",
        pygame.K_d: "D",
        pygame.K_f: "F",
        pygame.K_g: "G",
        pygame.K_h: "H",
        pygame.K_j: "J",
        pygame.K_k: "K",
        pygame.K_l: "L",
        pygame.K_z: "Z",
        pygame.K_x: "X",
        pygame.K_c: "C",
        pygame.K_v: "V",
        pygame.K_b: "B",
        pygame.K_n: "N",
        pygame.K_m: "M",
        pygame.K_BACKSLASH: "\\",
        pygame.K_SLASH: "/",
        pygame.K_LEFTPAREN: "(",
        pygame.K_RIGHTPAREN: ")",
        pygame.K_LEFTBRACKET: "[",
        pygame.K_RIGHTBRACKET: "]",
        pygame.K_PLUS: "+",
        pygame.K_MINUS: "-",
        pygame.K_EQUALS: "=",
        pygame.K_TAB: "Tab",
        pygame.K_BACKQUOTE: "`",
        pygame.K_QUOTE: "'",
        pygame.K_QUOTEDBL: "\"",
        pygame.K_COMMA: ",",
        pygame.K_SEMICOLON: ";",
        pygame.K_QUESTION: "?",
        pygame.K_GREATER: "<",
        pygame.K_LESS: "<"
    }
}


def render_keys_labels(misc: dict, fonts: dict, colors: dict) -> dict:
    """
    Render labels with all key names, in various langs
    :param misc:
    :param fonts: font data
    :param colors: colors data
    :return dict: rendered labels
    """
    data = {"shadows": {}, "keys": {}}
    # do the shadows:
    for lang in keynames:
        data["shadows"][lang] = {}
        for elem in keynames[lang]:
            if misc["keys-and-buttons"]["color"] in colors:
                color = colors[misc["keys-and-buttons-shadow"]["color"]]
            else:
                color = pygame.Color(misc["keys-and-buttons-shadow"]["color"])
            su = pygame.transform.rotate(
                fonts[misc["keys-and-buttons-shadow"]["font"]].render(
                    keynames[lang][elem],
                    True,
                    color),
                misc["keys-and-buttons-shadow"]["rotate"]
            )
            su.set_alpha(color.a)
            data["shadows"][lang][elem] = su
    # do the keys:
    for lang in keynames:
        data["keys"][lang] = {}
        for elem in keynames[lang]:
            if misc["keys-and-buttons"]["color"] in colors:
                color = colors[misc["keys-and-buttons"]["color"]]
            else:
                color = pygame.Color(misc["keys-and-buttons"]["color"])
            su = pygame.transform.rotate(
                fonts[misc["keys-and-buttons"]["font"]].render(
                    keynames[lang][elem],
                    True,
                    color),
                misc["keys-and-buttons"]["rotate"]
            )
            su.set_alpha(color.a)
            data["keys"][lang][elem] = su
    return data
