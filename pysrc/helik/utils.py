#!/usr/bin/env python3

"""
Various utility routines
"""


from helik.htypes import BoardType

def menupos2board(menu_pos: int) -> BoardType:
    """
    Calculate board id from menu pos
    :param menu_pos: menu position number
    :return: board id
    """
    ids = [BoardType.GAME, BoardType.OPTIONS, BoardType.HISCORES,
           BoardType.SETTINGS, BoardType.HELP, BoardType.ABOUT,
           BoardType.QUIT]
    try:
        return ids[menu_pos]
    except IndexError:
        return BoardType.QUIT # Because, erm, why not? ;)
