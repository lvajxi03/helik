#!/usr/bin/env python3

"""
Count objects in lane(s)
"""

import sys
import json


def open_and_count(filename: str):
    """
    Open lane file and count objects.
    Remark: this routine counts only non-zero (free space) objects
    :param filename: name of lane layout file
    :return: none
    :output: lane names and objects count
    """
    with open(filename) as fh:
        try:
            js = json.load(fh)
            for lane in js["lanes"]:
                counter = 0
                for obj in lane["objects"]:
                    if obj[0] > 0:
                        counter += 1
                print(f"{lane['description']}: {counter}")
        except IOError as ioe:
            print(str(ioe))
        except json.JSONDecodeError as jde:
            print(str(jde))


if __name__ == "__main__":
    try:
        open_and_count(sys.argv[1])
    except IndexError:
        print(f"Usage: {sys.argv[0]} <level file>")