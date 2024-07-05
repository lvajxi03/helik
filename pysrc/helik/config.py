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
            "lastnick": "",
            "sound": 1,
            "music": 1
            }

    def read_config(self, fn: str):
        """
        Read app configuration from a file
        :param fn: filename
        :return: configuration dictionary
        """
        try:
            with open(fn, encoding="utf-8") as fh:
                data = json.load(fh)
                self.data.update(data)
                if not isinstance(self.data['hiscores'], list):
                    self.data['hiscores'] = []
                if len(self.data['hiscores']) == 0:
                    i = 0
                    for name in ["AAA", "BBB", "CCC", "DDD", "EEE", "FFF", "GGG", "HHH", "III", 'JJJ']:
                        self.data['hiscores'].append((name, i * 10 + 2))
                        i += 1
                self.data['hiscores'].sort(key=lambda a: a[1], reverse=True)
                self.data['hiscores'] = self.data['hiscores'][:10]
        except IOError:
            pass
        except json.decoder.JSONDecodeError:
            pass

    def read_default_config(self):
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
            with open(fn, "w", encoding="utf-8") as fh:
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
            else:
                _, p = self.data['hiscores'][-1]
                if p < points:
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
        self.data['hiscores'].sort(key=lambda a: a[1], reverse=True)
        self.data['hiscores'] = self.data['hiscores'][:10]