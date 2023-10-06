#!/usr/bin/env python3

"""
HeliK config module
"""

import json
import os


class Config:
    """
    Configuration handler module
    """
    def __init__(self):
        self.data = {
            "lang": "en",
            "option": 1,
            "hiscores": [],
            "lastnick": ""
            }

    def read_config(self, fn: str) -> dict:
        """
        Read app configuration from a file
        :param fn: filename
        :return: configuration dictionary
        """
        try:
            with open(fn) as fh:
                data = json.load(fh)
                self.data.update(data)
                if not isinstance(self.data['hiscores'], list):
                    self.data['hiscores'] = []
        except IOError:
            pass
        except json.decoder.JSONDecodeError:
            pass

    def read_default_config(self) -> dict:
        """
        Read default configuration from a file
        :return: configuration dictionary
        """
        fn = os.path.expanduser("~/.helikrc")
        self.read_config(fn)

    def save_config(self, fn: str):
        """
        Save configuration to a file
        :param fn: filename
        """
        try:
            with open(fn, "w") as fh:
                json.dump(self.data, fh)
        except IOError:
            pass

    def save_default_config(self):
        """
        Save configuration to a default file
        """
        fn = os.path.expanduser("~/.helikrc")
        self.save_config(fn)

    def __getitem__(self, key):
        """
        Get operator overload
        :param key: dict key
        """
        try:
            return self.data[key]
        except KeyError:
            return None

    def __setitem__(self, key, value):
        """
        Set operator overload
        :param key: dict key
        :param value: associated value
        """
        self.data[key] = value

    def is_hiscore(self, points: int):
        """
        Check if this score is hiscore
        :param points:
        :return True if hiscore, false otherwise
        """
        try:
            if len(self.data['hiscores']) < 10:
                return True
            last = self.data['hiscores'][-1]
            if last[1] < points:
                return True
        except KeyError:
            pass
        return False

    def append_hiscore(self, nick: str, points: int):
        """
        Append hiscore to a list
        :param nick: new winners' name
        :param points: new winners' points
        """
        self.data['hiscores'].append((nick, points))

