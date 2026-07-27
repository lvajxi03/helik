#!/usr/bin/env python3

"""
Platform-related types
"""

import enum
import pygame


@enum.unique
class TimerType(enum.IntEnum):
    """
    TimerType enum
    There are only like 7-8 user events available,
    thus all the timers shall be reusable and have
    weird names
    """
    FIRST = pygame.USEREVENT + 1
    SECOND = pygame.USEREVENT + 2
    THIRD = pygame.USEREVENT + 3
    FOURTH = pygame.USEREVENT + 5
    FIFTH = pygame.USEREVENT + 6
