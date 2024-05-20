#!/usr/bin/env python3

"""
GameObject factories
"""

from helik.game.objects import GameObjectType
from helik.hdefs import ARENA_WIDTH, ARENA_HEIGHT
from helik.game.ammo import Ammo
from helik.game.birds import Bird
from helik.game.buildings import Building
from helik.game.clouds import Cloud
from helik.game.distance import Distance
from helik.game.dirc import DirC
from helik.game.heart import Heart


def upper_list_factory(data, game_option: int, images):
    """
    This factory creates objects relative to top
    :param data: whole level data dictionary
    :param game_option: level of difficulty
    :param images: all objects images
    """
    objects = []
    x = ARENA_WIDTH
    multiplier = int(data["multipliers"][game_option])
    for m in range(0, multiplier):
        for n in data["objects"]:
            if n[0] == 0:
                obj = Distance(x, n[1])
                objects.append(obj)
                x += n[1]
            elif n[0] == 1:
                image = images["buildings"][n[1]]
                obj = Building(x, )


def lower_list_factory():
    """
    This factory creates objects relative to bottom
    """
    pass

def distance_factory(arguments: list):
    """
    Factory to make a distance
    :param arguments: list of arguments (accepted: list with single argument, width)
    :return: Distance
    """


def building_factory(arguments: list):
    """
    Factory to make a building
    :param arguments: list of arguments (accepted: list with single argument, image number)
    """


def ammo_factory(arguments: list):
    """
    Factory to make an ammo
    :param arguments: list of arguments(accepted: list with single argument, y position)
    """


def heart_factory(arguments: list):
    """
    Factory to make a heart
    :param arguments: list of arguments(accepted: list with single argument, y position)
    """