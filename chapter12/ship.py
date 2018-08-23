#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-03-17 17:24
# @Author  : hys
# @Site    : 
# @File    : ship.py
# @Software: PyCharm
# @Desc     :
# @license : Copyright(C), Your Company
# @Contact : george.zw513@gmail.com
import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    def __init__(self, ai_settings, screen):
        """初始化飞船并设置其初始位置"""
        super().__init__()  # 初始化sprite属性
        self.screen = screen
        # 加载飞船图像并获取其外部矩形
        self.ai_settings = ai_settings
        self.image = pygame.image.load("images\ship.bmp")
        # 获取飞船控制器属性
        self.rect = self.image.get_rect()
        # 获取背景屏幕控制器属性
        self.screen_rect = screen.get_rect()
        # 将每艘新飞船在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        # 在飞船的属性center中存储小数值
        self.center = float(self.rect.centerx)
        # 在飞船的属性bottom中存储小数值
        self.bottom = float(self.rect.bottom)
        # 飞船移动标志位
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """根据移动标志调整飞船的位置"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.bottom -= self.ai_settings.ship_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.bottom += self.ai_settings.ship_speed_factor
        # 根据self.center更新rect对象
        self.rect.centerx = self.center
        self.rect.bottom = self.bottom

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """让飞船在屏幕上居中"""
        self.center = self.screen_rect.centerx
        self.bottom = self.screen_rect.bottom

