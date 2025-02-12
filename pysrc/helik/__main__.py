#!/usr/bin/env python3

"""
Entry point for Helik package
"""

import sys
from .arena import Arena


if __name__ == "__main__":
    vaq = False  # Validate And Quit
    app = Arena()
    try:
        if sys.argv[1] == "-q":
            vaq = True
    except IndexError:
        pass
    app.run(validate_and_quit=vaq)
