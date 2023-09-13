#!/usr/bin/env python3

"""
Game data module
"""

from helik.game.objects import Movable


class GameData:
    """
    Main game data class
    """
    def __init__(self):
        """
        GameData class constructor
        """
        self.data = {}
        self.new_data()

    def __getitem__(self, key):
        try:
            return self.data[key]
        except:
            return None

    def __setitem__(self, key, value):
        self.data[key] = value

    def __delitem__(self, key):
        try:
            del self.data[key]
        except:
            pass

    def new_data(self):
        self.data = {
            'level': 0,
            'points': 0,
            'option': 1,
            'lives': 3,
            'movables': [],
            'objects': [],
            'bullets-from': [],
            'bullets-available': 20,
            'bullets-to': [],
            'seconds': 0,
            'mspeed': 20,
            'last-movable': 0
        }

    def new_level(self, resman, level: int):
        """
        Introduce new level
        :param resman: resource manager handle
        :param level: new level
        """
        self['level'] = level
        self['mspeed'] = 20 - self['option'] - self['level']
        self.create_movables(resman, level)

    def score(self):
        self.points += 1  # TODO: ?

    def create_movables(self, resman, level):
        """
        Create movables according to the level
        :param resman: resource manager handle
        :param level: level number
        """
        self.data['movables'] = []
        x = 0
        for index in resman.get_index("levels", level):
            im, re = resman.bottom_objects[index]
            m = Movable(im, x)
            x += re.w
            self.data['movables'].append(m)
        self.data['last-movable'] = len(self.data['movables']) - 1
