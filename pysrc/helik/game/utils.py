#!/usr/bin/env python3

"""
Game utility routines
"""

from helik.game.objects import BulletFrom, Copter

def make_bullet_from(c: Copter):
    """
    Make bullet-from utility routine
    :param c: Copter instance
    """
    w, h  = c.image.get_size()
    x, y = c.x + w, c.y + 30
    return BulletFrom(c.res_man.get("images", "bullet-2"), x, y)


def make_clouds(resman, level):
    """
    Create clouds
    :param resman: Resource Manager instance
    :param level: level index
    """
    clouds = []
    # TODO - index etc
    return clouds
