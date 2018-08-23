#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-03-17 14:50
# @Author  : hys
# @Site    : 
# @File    : settings.py
# @Software: PyCharm
# @Desc     :
# @license : Copyright(C), Your Company
# @Contact : george.zw513@gmail.com


class Settings:
    """存储《外星人入侵》的所有设置的类"""

    def __init__(self):
        """初始化游戏的设置"""
        # 屏幕设置
        self.screen_width = 800  # 屏幕的宽度
        self.screen_height = 600  # 屏幕的高度
        self.bg_color = (0, 64, 128)  # 屏幕的颜色
        # 飞船设置
        self.ship_limit = 2  # 备用飞船数量
        self.ship_speed_factor = 2  # 飞船移动的速度
        # 子弹设置
        self.bullet_width = 3  # 子弹宽度
        self.bullet_height = 15  # 子弹高度
        self.bullet_speed_factor = 1  # 子弹速度
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 50  # 屏幕上最多可以发射的子弹
        # 外星人设置
        self.alien_speed_factor = 1  # 外星人左右移动的速度
        self.fleet_drop_speed = 80  # 外星人撞到屏幕后向下移动的速度
        # fleet_direction 为1 表示向右移动，为-1 表示向左移动
        self.alien_points = 8  # 记分
        self.fleet_direction = 1
        # 以什么样的速度加快游戏节奏
        self.speedup_scale = 1.1
        # 外星人点数的提高速度
        self.score_scale = 1.5
        # 初始化游戏相关设置
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """初始化随游戏进行而变化的设置"""
        self.ship_speed_factor = 2  # 飞船移动的速度
        self.bullet_speed_factor = 3  # 子弹速度
        self.alien_speed_factor = 1  # 外星人左右移动的速度
        self.fleet_drop_speed = 1  # 外星人撞到屏幕后向下移动的速度
        self.fleet_direction = 1  # fleet_direction 为1 表示向右移动，为-1 表示向左移动
        self.alien_points = 9  # 记分

    def increase_speed(self):
        """提高速度设置"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
        print("当前每个外星人点数值是： " + str(self.alien_points))
        # self.fleet_drop_speed *= self.speedup_scale



