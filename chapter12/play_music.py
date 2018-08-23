#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-03-18 21:59
# @Author  : hys
# @Site    : 
# @File    : play_music.py
# @Software: PyCharm
# @Desc     :
# @license : Copyright(C), Your Company
# @Contact : george.zw513@gmail.com
import pygame


class MusicPlayer:
    """游戏音乐播放器"""
    def __init__(self, music_name):
        """初始化音乐播放器"""
        self.music_name = music_name
        pygame.init()
        pygame.mixer.init()

    def play_music(self):
        pygame.display.set_mode([10, 10])
        pygame.time.delay(1000)
        pygame.mixer.music.load(self.music_name)
        # mp.play()
        # pygame.mixer.music.load(self.music_name)
        pygame.mixer.music.play()

    def stop_music(self):
        pygame.mixer.music.stop()


music1 = MusicPlayer("music\m_unknow.mp3")
music2 = MusicPlayer("music\mm.mp3")
music2.play_music()
pygame.time.delay(10000)
music1.play_music()
pygame.time.delay(10000)
print("延时10S")
music2.stop_music()
pygame.time.delay(10000)
print("延时20S")



