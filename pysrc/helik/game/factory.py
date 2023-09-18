#!/usr/bin/env python


"""
Game objects factory module
"""


from helik.game.objects import Building, Distance, Cloud


def make_buildings(resman, level: int):
    """
    Create buildings for given level
    :param resman: resource manager handle
    :param level: level index
    :return buildings list
    """
    buildings = []
    be = resman.levels[level]["buildings"]
    x = 0
    for b in be:
        if be[0] == -1:
            distance = Distance(x, be[2], be[1] == 1)
            buildings.append(distance)
            x += be[2]
        else:
            building = Building(self.resman.buildings[be[0], x))
            buildings.append(building)
            w, h = buildings.image.get_size()
            x += w
    return buildings
