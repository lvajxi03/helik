#!/usr/bin/env python3

"""
Entry point for Helik package
"""

import sys
from helik.arena import Application


if __name__ == "__main__":
    vaq = False #  Validate And Quit
    app = Application()
    try:
        if sys.argv[1] == "-q":
            vaq = True
    except IndexError:
        pass
    app.run(validate_and_quit=vaq)
