#!/usr/bin/env python3

"""
HeliK config module
"""

import json
import os


def read_config(fn: str) -> dict:
    """
    Read app configuration from a file
    :param fn: filename
    :return: configuration dictionary
    """
    data = {}
    try:
        with open(fn) as fh:
            data = json.load(fh)
            return data
    except IOError:
        pass
    return data


def read_default_config() -> dict:
    """
    Read default configuration from a file
    :return: configuration dictionary
    """
    data = {}
    fn = os.path.expanduser("~/.helikrc")
    return read_config(fn)


def save_config(fn: str, data: dict):
    """
    Save configuration to a file
    :param fn: filename
    :param data: configuration to save
    """
    try:
        with open(fn, "w") as fh:
            json.dump(fh, data)
    except IOError:
        pass


def save_default_config(data: dict):
    """
    Save configuration to a default file
    :param data: configuration to save
    """
    fn = os.path.expanduser("~/.helikrc")
    save_config(fn, data)
