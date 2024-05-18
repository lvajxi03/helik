#!/usr/bin/env python3

"""
Lane module
"""

from helik.hdefs import ARENA_HEIGHT
from helik.htypes import GameObjectType
from helik.game.buildings import building_from_image
from helik.game.clouds import cloud_from_image
from helik.game.dirc import dirc_from_images
from helik.game.ammo import ammo_from_images
from helik.game.heart import heart_from_images


class Lane:
    """
    Game lane class
    """
    def __init__(self, data, resman, multiplier=1):
        """
        Create lane instance
        :param data: dict that describes lane data
        :param resman: Resource Manager instance
        :param multiplier: objects repeating factor
        """
        self.speed = data["speed"]
        self.bottom = data["bottom"] == 1
        self.objects = []

        if multiplier < 1:
            multiplier = 1
        x = 0
        # Create objects
        for i in range(multiplier):
            for ar in data["objects"]:
                try:
                    if ar[0] == GameObjectType.NONE:
                        x += ar[1]
                    elif ar[0] == GameObjectType.BUILDING:
                        # Create new building
                        im = resman.images["buildings"][ar[1]]
                        if self.bottom:
                            self.objects.append(building_from_image(im, x))
                        else:
                            self.objects.append(building_from_image(im, x, ar[2]))
                        w, h = im.get_size()
                        x += w
                    elif ar[0] == GameObjectType.CLOUD:
                        im = resman.images["clouds"][ar[1]]
                        w, _ = im.get_size()
                        if self.bottom:
                            self.objects.append(cloud_from_image(im, x, ARENA_HEIGHT - ar[2]))
                        else:
                            self.objects.append(cloud_from_image(im, x, ar[2]))
                        x += w
                    elif ar[0] == GameObjectType.DIRC:
                        ims = resman.images["dirc"]
                        w, _ = ims[0].get_size()
                        if self.bottom:
                            self.objects.append(dirc_from_images(ims, x, ARENA_HEIGHT - ar[2]))
                        else:
                            self.objects.append(dirc_from_images(ims, x, ar[2]))
                        x += w
                    elif ar[0] == GameObjectType.AMMO:
                        ims = resman.images["ammo"]
                        w, _ = ims[0].get_size()
                        if self.bottom:
                            self.objects.append(ammo_from_images(ims, x, ARENA_HEIGHT - ar[2]))
                        else:
                            self.objects.append(ammo_from_images(ims, x, ar[2]))
                    elif ar[0] == GameObjectType.HEART:
                        ims = resman.images["hearts"]
                        w, _ = ims[0].get_size()
                        if self.bottom:
                            self.objects.append(heart_from_images(ims, x, ARENA_HEIGHT - ar[2]))
                        else:
                            self.objects.append(heart_from_images(ims, x, ar[2]))
                    elif ar[0] == GameObjectType.BIRD:
                        pass
                except IndexError:
                    # Skip invalid and incomplete objects
                    pass
                except KeyError:
                    pass

    def __len__(self):
        return len(self.objects)

    def rewind(self, dx):
        """
        Rewind lane objects by a given distance
        :param dx: x-axis distance
        """
        for obj in self.objects:
            obj.x += dx

    def move(self):
        for obj in self.objects:
            obj.move(self.speed)

        self.objects = [x for x in self.objects if x.valid]

    def paint(self, canvas):
        """
        Paint the lane
        """
        for obj in self.objects:
            obj.on_paint(canvas)