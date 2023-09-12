#!/usr/bin/env python3

"""
Game utility routines
"""

from helik.game.objects import BulletFrom, Copter

def make_bullet_from(c: Copter):
    w, h  = c.image.get_size()
    x, y = c.x + w, c.y + 30
    return BulletFrom(c.res_man.get("images", "bullet-2"), x, y)

