#!/usr/bin/env python3

"""
Graphics utilities
"""


def blitnumber(target, number: int, width: int, digits: dict, at):
    """
    Blit number on a surface
    :param surface: target surface
    :param number: the number itself
    :param width: targed width of a number
    :param digits: dict with digits mapping (to images)
    """
    s = str(number).rjust(width, '0')
    x, y = at
    for c in s:
        target.blit(digits[c], (x, y))
        x += 35
    
