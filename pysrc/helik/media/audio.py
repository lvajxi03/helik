#!/usr/bin/env python3

"""
Audio controller handler module
"""

import json
import enum
import pygame
from helik.htypes import SoundPlayState


@enum.unique
class SoundChannel(enum.IntEnum):
    """
    Sound channel numbers
    """
    BACKGROUND = 0
    MUSIC = 1
    SOUND = 2


class AudioController:
    """
    Audio controller handler class
    """
    states: list = []
    sounds: dict = {}
    channels: list = []
    arena = None

    def __init__(self, parent, basepath):
        """
        Audio controller class constructor
        :param parent: arena instance handle
        :param basepath: Path-like object - root of all resources
        """
        self.arena = parent
        bp = basepath.joinpath("sounds")
        fn = basepath.joinpath("sounds.json")
        with open(fn, encoding="utf-8") as f_handle:
            try:
                js = json.load(f_handle)
                for sound in js:
                    print(sound)
                    self.sounds[sound] = pygame.mixer.Sound(bp.joinpath(js[sound]))
            except IOError:
                pass
        for i in range(3):
            self.channels.append(pygame.mixer.Channel(i))
            self.states.append(SoundPlayState.STOPPED)

    def play(self, channel: int, sound: str, **kwargs):
        """
        Play Music
        :param channel: channel number
        :param sound: sound key in the music library
        :param kwargs: additional parameters, like:
            * loops - number of loops, -1 -> infinite loop
        """
        loops = kwargs.get("loops", 1)
        if self.arena.config["sound"] == 1:
            if sound in self.sounds:
                if self.states[channel] == SoundPlayState.PLAYING:
                    self.states[channel].fadeout(100)
                self.channels[channel].play(self.sounds[sound], loops=loops)
                self.states[channel] = SoundPlayState.PLAYING

    def play_sound(self, channel: int, sound: str):
        """
        Play SFX sound.
        Sound is played one time only
        :param channel: channel number
        :param sound: sound key in the music library
        """
        if self.arena.config["sound"] == 1:
            if sound in self.sounds:
                # Don't mark channel state here, as SFX sounds
                # be very short.
                self.channels[channel].play(self.sounds[sound])

    def stop(self, channel: int):
        """
        Stop the playback
        :param channel: channel number
        """
        if self.states[channel] != SoundPlayState.STOPPED:
            self.channels[channel].fadeout(100)
            self.states[channel] = SoundPlayState.STOPPED

    def pause(self, channel):
        """
        Pause the playback
        :param channel: channel number
        """
        if self.states[channel] == SoundPlayState.PLAYING:
            self.channels[channel].pause()
            self.states[channel] = SoundPlayState.PAUSED

    def unpause_music(self, channel: int):
        """
        Unpause the playback
        :param channel: channel number
        """
        if self.states[channel] == SoundPlayState.PAUSED:
            self.channels[channel].unpause()
            self.states[channel] = SoundPlayState.PLAYING

    def enable_background_music(self, sound: str):
        """
        Handy wrapper to enable background music
        :param sound: sound key in the music library
        """
        if self.arena.config["music"] == 1:
            if self.states[SoundChannel.BACKGROUND] == SoundPlayState.PAUSED:
                self.unpause_music(SoundChannel.BACKGROUND)
            elif self.states[SoundChannel.BACKGROUND] == SoundPlayState.STOPPED:
                self.play(SoundChannel.BACKGROUND, sound, loops=-1)

    def pause_background_music(self):
        """
        Handy wrapper to pause background music
        """
        self.pause(SoundChannel.BACKGROUND)

    def stop_background_music(self):
        """
        Handy wrapper to stop background music
        """
        self.stop(SoundChannel.BACKGROUND)

    def enable_music(self, sound: str):
        """
        Handy wrapper for enabling gameplay music
        :param sound: sound key in the music library
        """
        if self.arena.config["music"] == 1:
            if self.states[SoundChannel.MUSIC] == SoundPlayState.PAUSED:
                self.unpause_music(SoundChannel.MUSIC)
            elif self.states[SoundChannel.MUSIC] == SoundPlayState.STOPPED:
                self.play(SoundChannel.MUSIC, sound, loops=-1)

    def pause_music(self):
        """
        Handy wrapper to pause gameplay music
        """
        self.pause(SoundChannel.MUSIC)

    def stop_music(self):
        """
        Handy wrapper to stop gameplay music
        """
        self.stop(SoundChannel.MUSIC)

    def play_sfx(self, sound: str):
        """
        Handy wrapper to play sound in SFX channel
        :param sound: sound key in the music library
        """
        self.play_sound(SoundChannel.SOUND, sound)

    def play_music(self, sound: str):
        """
        Handy wrapper to play sound in music channel
        :param sound: sound key in the music library
        """
        self.play_sound(SoundChannel.SOUND, sound)
