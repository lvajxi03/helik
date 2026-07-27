#!/usr/bin/env python3

"""
Testing lanes
"""

import pytest
from helik.game import Lane


@pytest.fixture
def make_data():
    return {
        'speed': 3,
        'bottom': 1
    }


def test_lane_1(make_data):
    l = None
    with pytest.raises(KeyError):
        l = Lane(make_data, None, -1)
    assert l is None
