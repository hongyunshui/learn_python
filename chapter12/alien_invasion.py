#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-03-17 11:58
# @Author  : hys
# @Site    : 
# @File    : alien_invasion.py
# @Software: PyCharm
# @Desc     :
# @license : Copyright(C), Your Company
# @Contact : george.zw513@gmail.com
import pygame
from chapter12.settings import Settings
from chapter12.ship import Ship
import chapter12.game_functions as gf  # 导入游戏功能模块
from pygame.sprite import Group
from chapter12.game_stats import GameStats
from chapter12.scoreboard import Scoreboard
from chapter12.button import Button
from chapter12.test_play_music import MusicPlayer


def run_game():
    """初始化屏幕并创建一个屏幕对象"""
    # 初始化pygame模块 （去掉之后游戏运行正常）
    pygame.init()
    # 获取游戏设置对象
    ai_settings = Settings()
    # 获得屏幕最佳颜色位数
    best_depth = pygame.display.mode_ok((ai_settings.screen_width, ai_settings.screen_height), pygame.FULLSCREEN)
    # 获取背景屏幕
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height), pygame.FULLSCREEN,
                                     best_depth)
    # 在屏幕标题栏显示名字“Alien Invasion”
    pygame.display.set_caption("Alien Invasion")
    # 创建play按钮
    play_button = Button(ai_settings, screen, "PLAY")
    # 创建一个用于存储游戏统计信息的实例
    stats = GameStats(ai_settings)
    # 创建记分牌
    sb = Scoreboard(ai_settings, screen, stats)
    # 创建一艘飞船
    ship = Ship(ai_settings, screen)
    # 创建一个用于存储子弹的编组
    bullets = Group()
    # 创建外星人编组
    aliens = Group()
    # 创建外星人群
    gf.create_fleet(ai_settings, screen, ship, aliens)
    # 播放背景音乐
    # pygame.mixer.music.load("music\m_unknow.mp3")
    # pygame.mixer.music.play()

    # 开始游戏的主循环
    while True:
        # 监视键盘和鼠标事件
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
        if stats.game_active:
            # 更新飞船信息
            ship.update()
            # 更新子弹状态
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            # print(len(bullets))  # 在终端显示子弹的数量
            # 更新外星人
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)
            pygame.time.delay(10)
        # 更新屏幕
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)


run_game()


