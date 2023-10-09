#!/usr/bin/env python3

"""
Graphics utilities
"""


def blitnumber(target, number: int, width: int, digits: dict, at):
    """
    Blit number on a surface (zero-leading)
    :param surface: target surface
    :param number: the number itself
    :param width: target width of a number
    :param digits: dict with digits mapping (to images)
    :param at: tuple with top-left coordinates of the number
    """
    s = str(number).rjust(width, '0')
    x, y = at
    for c in s:
        target.blit(digits[c], (x, y))
        x += 35


def blitnumber_s(target, number: int, width: int, digits: dict, at):
    """
    Blit number on a surface (space-leading)
    :param surface: target surface
    :param number: the number itself
    :param width: target width of a number
    :param digits: dict with digits mapping (to images)
    :param at: tuple with top-left coordinates of the number
    """
    s = str(number).rjust(width, ' ')
    x, y = at
    for c in s:
        if c != ' ':
            target.blit(digits[c], (x, y))
        x += 35


def blitstr(target, s: str, letters: dict, at):
    """
    Blit string on a surface
    :param surface: target surface
    :param s: the string itself
    :param letters: dict with letters mapping (to images)
    :param at: tuple with top-left coordinates of the string
    """
    x, y = at
    for c in s:
        if c !=' ':
            target.blit(letters[c], (x, y))
        x += 35
