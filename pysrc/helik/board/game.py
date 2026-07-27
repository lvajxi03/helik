#!/usr/bin/env python3

"""
Game board for HeliK
"""


from helik.game import Level
from helik.gamemode import (Mode, ModeInit, ModeKilled, ModePaused,
                            ModePlay, ModePrepare, ModeNewLevel, SelectPlayer, ModeGameOver)
from helik.gamemode import GameMode
from helik.media import SoundPlayState
from .standard import Board


class BoardGame(Board):
    """
    Game board class for HeliK
    """
    def __init__(self, parent):
        """
        Game board constructor
        """
        super().__init__(parent)
        self.mode = GameMode.NONE
        self.player = None
        self.data = {
            'points': 0,
            'level': -1,
            'option': 2,
            'seconds': 0,
            'bullets-available': 20,
            'lives': 5
        }
        self.music_state = SoundPlayState.STOPPED
        self.modes = {
            GameMode.NONE: Mode(self),
            GameMode.SELECTPLAYER: SelectPlayer(self),
            GameMode.INIT: ModeInit(self),
            GameMode.PREPARE: ModePrepare(self),
            GameMode.PLAY: ModePlay(self),
            GameMode.PAUSED: ModePaused(self),
            GameMode.KILLED: ModeKilled(self),
            GameMode.NEWLEVEL: ModeNewLevel(self),
            GameMode.GAMEOVER: ModeGameOver(self),
            }
        self.explosions = []

        self.level = None

    def new_level(self):
        """
        Initialize new level data
        """
        self.level = Level(self.resman, self.data['level'], self.arena.config["option"])

    def change_mode(self, newmode):
        """
        Change to new game mode.
        Mode is changed only if differs from current mode:
        1. Old mode runs its `deactivate` method
        2. Mode is changed
        3. New mode runs its `activate` method
        :param newmode: new mode
        """
        if newmode != self.mode:
            self.modes[self.mode].deactivate()
            self.mode = newmode
            self.modes[self.mode].activate()

    def activate(self, **kwargs):
        """
        Activate event handler
        :param kwargs: additional parameters, like help or previous board
        """
        self.change_mode(GameMode.INIT)

    def deactivate(self):
        """
        Deactivate event handler
        """
        self.music_state = SoundPlayState.STOPPED
        self.audio.stop_music()

    def on_paint(self):
        """
        Paint event handler
        """
        self.modes[self.mode].on_paint()

    def on_keyup(self, key):
        """
        Key release event handler
        :param key: key code
        """
        self.modes[self.mode].on_keyup(key)

    def on_timer(self, timer):
        """
        Timer event handler
        :param timer: timer identifier
        """
        self.modes[self.mode].on_timer(timer)

    def on_update(self, delta):
        """
        Update event handler
        :param delta: delta time from last frame
        """
        self.modes[self.mode].on_update(delta)

    def on_mouseup(self, button, pos):
        """
        Mouse up event handler
        :param button: button number
        :param pos: cursor position
        """
        self.modes[self.mode].on_mouseup(button, pos)

    def on_joybuttonup(self, button):
        """
        JoyButtonUp event handler
        :param button: button number
        """
        self.modes[self.mode].on_joybuttonup(button)

    def on_joyaxismotion(self, axis, value):
        """
        JoyAxisMotion event handler
        :param axis: axis number
        :param value: axis value
        """
        self.modes[self.mode].on_joyaxismotion(axis, value)
