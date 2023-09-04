#!/usr/bin/env python3

"""
Locale module for HeliK
"""

from helik.htypes import BoardType


locale = {
    BoardType.MENU: {
        "title": {
            "pl": "HeliK!",
            "en": "HeliK!",
            "font": "heading",
            "rotate": 90,
            "color": "#e0df4a"
        },
        "title_shadow": {
            "pl": "HeliK!",
            "en": "HeliK!",
            "font": "heading",
            "rotate": 90,
            "color": "#313131"
        },
        "status": {
            "pl": "UZYJ KLAWISZY KURSORA I ENTER, ABY WYBRAC OPCJE LUB Q ABY WYJSC",
            "en": "USE CURSOR KEYS AND ENTER TO SELECT AN OPTON OR Q TO QUIT",
            "font": "menu",
            "rotate": 0,
            "color": "#ffffff"
        },
        "menu": {
            "pl": ["NOWA GRA", "OPCJE", "NAJLEPSZE WYNIKI",
                   "USTAWIENIA", "POMOC", "O PROGRAMIE", "WYJSCIE"],
            "en": ["NEW GAME", "OPTIONS", "HISCORES", "SETTINGS",
                   "HELP", "ABOUT", "QUIT"],
            "font": "menu",
            "rotate": 0,
            "color": "#fefefe"
        }
    },
    BoardType.ABOUT: {
        "title": {
            "pl": "O programie",
            "en": "About",
            "font": "menu",
            "rotate": 0,
            "color": "#e0df4a"
            }
    },
    BoardType.HELP: {
        "title": {
            "pl": "Pomoc",
            "en": "Help",
            "font": "menu",
            "rotate": 0,
            "color": "#e0df4a"
        }
    },
    BoardType.HISCORES: {
        "title": {
            "pl": "NAJLEPSZE WYNIKI",
            "en": "HISCORES",
            "font": "menu",
            "rotate": 0,
            "color": "#e0df4a"
        }
    },
    BoardType.NEWSCORE: {
        "title": {
            "pl": "Nowy rekord",
            "en": "New Score",
            "font": "menu",
            "rotate": 0,
            "color": "#e0df4a"
        }
    },
    BoardType.OPTIONS: {
        "title": {
            "pl": "Opcje gry",
            "en": "Game Options",
            "font": "menu",
            "rotate": 0,
            "color": "#e0df4a"
        }
    },
    BoardType.SETTINGS: {
        "title": {
            "pl": "Ustawienia",
            "en": "Settings",
            "font": "menu",
            "rotate": 0,
            "color": "#e0df4a"
        }
    },
    BoardType.GAME: {
        "1": {
            "pl": "1",
            "en": "1",
            "font": "prepare",
            "rotate": 0,
            "color": "#e9df4a"
        },
        "2": {
            "pl": "2",
            "en": "2",
            "font": "prepare",
            "rotate": 0,
            "color": "#e9df4a"
        },
        "3": {
            "pl": "3",
            "en": "3",
            "font": "prepare",
            "rotate": 0,
            "color": "#e9df4a"
            },
        "paused": {
            "pl": "GRA WSTRZYMANA",
            "en": "GAME PAUSED",
            "font": "big-message",
            "color": "#e0df4a",
            "rotate": 0
        },
        "continue": {
            "pl": "NACISNIJ SPACJE BY KONTYNUOWAC",
            "en": "PRESS SPACE TO CONTINUE",
            "font": "menu",
            "color": "#ffffff",
            "rotate": 0
        }
    }
}
