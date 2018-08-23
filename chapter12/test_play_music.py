#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-03-19 0:25
# @Author  : hys
# @Site    : 
# @File    : test_play_music.py
# @Software: PyCharm
# @Desc     :
# @license : Copyright(C), Your Company
# @Contact : george.zw513@gmail.com
import pygame


class MusicPlayer:
    def __init__(self, screen, music_name):
        self.screen = screen
        self.music_name = music_name

    def play_music(self):
        pygame.mixer.music.load(self.music_name)
        pygame.mixer.music.play()

    @staticmethod
    def stop_music():
        pygame.mixer.music.stop()
