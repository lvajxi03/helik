#!/usr/bin/env python3

"""
Audio types
"""

import enum


@enum.unique
class SoundPlayState(enum.IntEnum):
    """
    SoundPlayState enum
    Tells you what state is the particular sound object
    """
    STOPPED = 0
    PLAYING = 1
    PAUSED = 2
