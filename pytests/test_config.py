#!/usr/bin/env python3

"""
Testing helik.config
"""

import pytest
from pygame import K_ESCAPE, K_SPACE, K_s
from helik.config import Config
from helik.platform import ButtonType


@pytest.fixture
def get_config_0():
    return {"key1": "value1", "key2": "value2"}


@pytest.fixture
def get_config_1():
    return "UFO"


@pytest.fixture
def get_config_2():
    return {"key1": "value1", "hiscores": 3}


@pytest.fixture
def get_config_3():
    return {"keys": {"shoot": K_ESCAPE, "jump": K_ESCAPE}}


def test_config_1():
    c = Config()
    assert len(c["hiscores"]) == 0


def test_config_2():
    c = Config()
    c.fake_hiscores()
    assert len(c["hiscores"]) == 10


def test_config_3(mocker):
    mocker.patch("builtins.open", side_effect=IOError)
    c = Config()
    c.read_default_config()
    assert len(c["hiscores"]) == 10


def test_config_4(mocker):
    mocker.patch("builtins.open", side_effect=IOError)
    c = Config()
    c.read_default_config()
    c.append_hiscore("NICK", 1)
    _, p = c["hiscores"][9]
    assert p > 1


def test_config_5(mocker):
    mocker.patch("builtins.open", side_effect=IOError)
    c = Config()
    c.read_default_config()
    for i in range(10):
        c.append_hiscore("NICK", 1000)
    _, p = c["hiscores"][9]
    assert p == 1000


def test_config_6(mocker, get_config_0):
    mocker.patch("builtins.open")
    mocker.patch("json.loads", return_value=get_config_0)
    c = Config()
    c.read_default_config()
    assert len(c["hiscores"]) == 10


def test_config_7(mocker, get_config_1):
    mocker.patch("builtins.open")
    mocker.patch("json.loads", return_value=get_config_1)
    c = Config()
    with pytest.raises(ValueError):
        c.read_default_config()
        assert True


def test_config_8(mocker, get_config_2):
    mocker.patch("builtins.open")
    mocker.patch("json.loads", return_value=get_config_2)
    c = Config()
    c.read_default_config()
    assert len(c["hiscores"]) == 10


def test_config_9(mocker):
    mock_file = mocker.mock_open()
    mocker.patch("builtins.open", mock_file)
    mocker.return_value = "random string"
    c = Config()
    c.read_default_config()
    assert len(c["hiscores"]) == 10


def test_config_10(mocker, get_config_3):
    mock_file = mocker.mock_open()
    mocker.patch("builtins.open", mock_file)
    mocker.patch("json.loads", return_value=get_config_3)
    c = Config()
    c.read_default_config()
    assert c["keys"]["jump"] == K_SPACE
    assert c["keys"]["shoot"] == K_s


def test_config_11(mocker):
    mock_file = mocker.mock_open()
    mocker.patch("builtins.open", mock_file)
    c = Config()
    c.save_config("\\/\\/\\/\\/")


def test_config_12(mocker):
    mock_file = mocker.mock_open()
    mocker.patch("builtins.open", mock_file)
    c = Config()
    c.save_default_config()


