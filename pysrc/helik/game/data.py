#!/usr/bin/env python3

"""
Game data module
"""

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
            'mspeed': 30,
            'last-movable': 0
        }

    def new_level(self, resman, level: int):
        """
        Introduce new level
        :param resman: resource manager handle
        :param level: new level
        """
        self['level'] = level
        self['mspeed'] = 20 - 3* self['option'] - 2 * self['level']

    def score(self):
        self.points += 1  # TODO: ?
