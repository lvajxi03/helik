#!/usr/bin/env python3

"""
Locale module for HeliK
"""

from helik.htypes import BoardType


locale = {
    BoardType.MENU: {
        "title": {
            "pl": "HeliK",
            "en": "HeliK"
            },
        "status": {
            "pl": "UZYJ KLAWISZY KURSORA I ENTER, ABY WYBRAC OPCJE LUB Q ABY WYJSC",
            "en": "USE CURSOR KEYS AND ENTER TO SELECT AN OPTON OR Q TO QUIT"
            },
        "menu": {
            "pl": ["NOWA GRA", "OPCJE", "NAJLEPSZE WYNIKI", "USTAWIENIA", "POMOC", "O PROGRAMIE", "WYJSCIE"],
            "en": ["NEW GAME", "OPTIONS", "HISCORES", "SETTINGS", "HELP", "ABOUT", "QUIT"]
            }
        },
    BoardType.ABOUT: {
        "title": {
            "pl": "O programie",
            "en": "About"
            },
        },
    BoardType.HELP: {
        },
    BoardType.HISCORES: {
        "title": {
            "pl": "NAJLEPSZE WYNIKI",
            "en": "HISCORES"
            }
        },
    BoardType.NEWSCORE: {
        },
    BoardType.OPTIONS: {
        },
    BoardType.SETTINGS: {
        },
    BoardType.GAME: {
        }
    }
