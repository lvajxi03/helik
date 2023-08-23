#!/usr/bin/env python3

"""
All the resources
"""

import pygame


def create_resources(basepath):
    """
    Load all resources
    """
    resources = {
        "images": {
            "default-background": pygame.image.load(basepath.joinpath("back-default.jpg")).convert_alpha()
        }
    }
    # That's all Folks!
    return resources
