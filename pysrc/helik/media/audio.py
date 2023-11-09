#!/usr/bin/env python3

"""
Audio controller handler module
"""

import json
import pygame
from helik.htypes import SoundPlayState


class AudioController:
    """
    Audio controller handler class
    """
    def __init__(self, basepath):
        """
        Audio controller class constructor
        :param basepath: Path-like object - root of all resources
        """
        self.sounds = {}
        self.music_state = SoundPlayState.STOPPED
        bp = basepath.joinpath("sounds")
        fn = basepath.joinpath("sounds.json")
        with open(fn, encoding="utf-8") as f_handle:
            try:
                js = json.load(f_handle)
                for sound in js:
                    self.sounds[sound] = pygame.mixer.Sound(bp.joinpath(js[sound]))
            except IOError:
                pass
        self.music_channel = pygame.mixer.Channel(0)
        self.sfx_channel = pygame.mixer.Channel(1)

    def play_sound(self, sound: str):
        """
        Play SFX sound.
        Sound is played one time only
        :param sound: sound key name in sounds library
        """
        if sound in self.sounds:
            self.sfx_channel.play(self.sounds[sound])

    def play_music(self, music: str):
        """
        Play the music.
        Music is played infinitely.
        :param music: music key name in sounds library.
        """
        if music in self.sounds:
            self.stop_music()
            self.music_state = SoundPlayState.PLAYING
            self.music_channel.play(self.sounds[music], loops=-1)

    def stop_music(self):
        """
        Stop the music.
        """
        if self.music_state != SoundPlayState.STOPPED:
            self.music_channel.fadeout(100)
            self.music_state = SoundPlayState.STOPPED

    def pause_music(self):
        """
        Pause the music.
        """
        if self.music_state == SoundPlayState.PLAYING:
            self.music_channel.pause()
            self.music_state = SoundPlayState.PAUSED

    def unpause_music(self):
        """
        Unpause the music.
        """
        if self.music_state == SoundPlayState.PAUSED:
            self.music_channel.unpause()
            self.music_state = SoundPlayState.PLAYING
