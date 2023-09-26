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
            "pl": ["NOWA GRA", "OPCJE GRY", "NAJLEPSI",
                   "USTAWIENIA", "POMOC", "O PROGRAMIE", "WYJSCIE"],
            "en": ["NEW GAME", "GAME OPTIONS", "HISCORES", "SETTINGS",
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
            "font": "heading-2",
            "rotate": 90,
            "color": "#e0df4a"
        },
        "title-shadow": {
            "pl": "O programie",
            "en": "About",
            "font": "heading-2",
            "rotate": 90,
            "color": "#313131"
        }
    },
    BoardType.HELP: {
        "title": {
            "pl": "Pomoc",
            "en": "Help",
            "font": "heading-2",
            "rotate": 90,
            "color": "#e0df4a"
        },
        "title-shadow": {
            "pl": "Pomoc",
            "en": "HELP",
            "font": "heading-2",
            "rotate": 90,
            "color": "#313131"
        }
    },
    BoardType.HISCORES: {
        "title": {
            "pl": "NAJLEPSI",
            "en": "HISCORES",
            "font": "heading-2",
            "rotate": 90,
            "color": "#e0df4a"
        },
        "title-shadow": {
            "pl": "NAJLEPSI",
            "en": "HISCORES",
            "font": "heading-2",
            "rotate": 90,
            "color": "#313131"
        },
        "empty": {
            "pl": "(niczego tu jeszcze nie ma)",
            "en": "(so far nothing to see here)",
            "font": "menu",
            "rotate": 0,
            "color": "#313131"
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
            "font": "heading-3",
            "rotate": 90,
            "color": "#e0df4a"
        },
        "title-shadow": {
            "pl": "Opcje gry",
            "en": "Game Options",
            "font": "heading-3",
            "rotate": 90,
            "color": "#313131"
        },
        "header": {
            "pl": "Wybierz tryb",
            "en": "Choose your mode",
            "font": "heading-3",
            "rotate": 0,
            "color": "#e0df4a"
        },
        "header-shadow": {
            "pl": "Wybierz tryb",
            "en": "Choose your mode",
            "font": "heading-3",
            "rotate": 0,
            "color": "#313131"
        },
        "options": {
            "pl": ["Treningowy", "Latwy", "Normalny", "Sredni", "Trudny", "Piekielny"],
            "en": ["Training", "Easy", "Normal", "Medium", "Hard", "Hell no!"],
            "font": "menu",
            "rotate": 0,
            "color": "#fefefe"
        }
    },
    BoardType.SETTINGS: {
        "title": {
            "pl": "Ustawienia",
            "en": "Settings",
            "font": "heading-2",
            "rotate": 90,
            "color": "#e0df4a"
        },
        "title-shadow": {
            "pl": "Ustawienia",
            "en": "Settings",
            "font": "heading-2",
            "rotate": 90,
            "color": "#313131"
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
        "paused-shadow": {
            "pl": "GRA WSTRZYMANA",
            "en": "GAME PAUSED",
            "font": "big-message",
            "color": "#313131",
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
