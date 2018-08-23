#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-03-22 17:10
# @Author  : hys
# @Site    : 
# @File    : scoreboard.py
# @Software: PyCharm
# @Desc     :
# @license : Copyright(C), Your Company
# @Contact : george.zw513@gmail.com
import pygame.font
from pygame.sprite import Group
from chapter12.ship import Ship


class Scoreboard:
    """显示得分信息的类"""
    def __init__(self, ai_settings, screen, stats):
        """初始化显示得分涉及的属性"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        # 显示得分信息时使用的字体设置
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 20)

        # 准备初始化得分图像
        self.prep_score()

        # 准备包含最高分和当前得分的图像
        self.prep_score()  # 当前得分
        self.prep_high_score()  # 最高分
        self.prep_level()  # 游戏等级
        self.prep_ships()  # 显示余下多少飞船

    def prep_score(self):
        """将得分转换为一副渲染的图像"""
        rounded_score = int(round(self.stats.score, -1))  # 将得分圆整为10
        score_str = "{:,}".format(rounded_score)  # 将得分转化为字符串类型，且每隔3位就用小数点隔开
        score_str = "current score:" + score_str
        # 将score_image渲染为图像
        self.score_image = self.font.render(score_str, True, self.text_color, self.ai_settings.bg_color)

        # 将得分放在屏幕右上角
        self.score_rect = self.score_image.get_rect()  # 获得得分矩形对象属性
        self.score_rect.right = self.screen_rect.right - 20  # 设置得分图像右边缘距离屏幕有边缘20个像素
        self.score_rect.top = 20  # 设置得分图像上边缘距离屏幕上边缘20个像素

    def prep_high_score(self):
        """将最高得分转换为渲染的图像"""
        high_score = int(round(self.stats.high_score, -1))  # 将最高得分圆整为10
        high_score_str = "{:,}".format(high_score)  # 把最高得分转化为字符串类型，且每隔3位就用小数点隔开
        high_score_str = "high score:" + high_score_str
        # 将high_score_str渲染为图像
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.ai_settings.bg_color)
        # 将最高分放在屏幕中央
        self.high_score_rect = self.high_score_image.get_rect()  # 获得最高分矩形对象属性
        self.high_score_rect.centerx = self.screen_rect.centerx  # 横坐标在屏幕中央
        self.high_score_rect.top = self.score_rect.top  # 纵坐标与得分一样

    def prep_level(self):
        """在屏幕上显示当前游戏等级"""
        # 将等级数渲染为图像
        self.level_image = self.font.render(str(self.stats.level), True, self.text_color, self.ai_settings.bg_color)
        self.level_rect = self.level_image.get_rect()  # 获得当前等级数对象属性
        self.level_rect.right = self.score_rect.right  # 当前等级横坐标在与当前得分横坐标一样
        self.level_rect.top = self.score_rect.bottom + 5  # 当前等级显示位置的纵坐标在当前得分位置向下20个像素

    def prep_ships(self):
        """显示余下多少飞船"""
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_settings, self.screen)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)

    def show_score(self):
        """在屏幕上显示得分、最高分、当前等级"""
        self.screen.blit(self.score_image, self.score_rect)  # 显示当前得分
        self.screen.blit(self.high_score_image, self.high_score_rect)  # 显示最高得分
        self.screen.blit(self.level_image, self.level_rect)  # 显示当前等级
        self.ships.draw(self.screen)



