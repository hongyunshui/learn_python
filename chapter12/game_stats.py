#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-03-22 11:56
# @Author  : hys
# @Site    : 
# @File    : game_stats.py
# @Software: PyCharm
# @Desc     :
# @license : Copyright(C), Your Company
# @Contact : george.zw513@gmail.com


class GameStats:
    """跟踪统计游戏信息"""
    def __init__(self, ai_settings):
        """初始化统计信息"""
        self.ai_settings = ai_settings
        self.reset_stats()
        self.game_active = False
        # self.ships_left = self.ai_settings.ship_limit
        # self.score = 0
        # 在任何情况下都不应重置最高分
        self.high_score = 0

    def reset_stats(self):
        """初始化游戏运行期间可能变化的统计信息"""
        self.ships_left = self.ai_settings.ship_limit  # 剩余飞船数量
        self.score = 0  # 当前得分
        self.level = 1  # 游戏等级

