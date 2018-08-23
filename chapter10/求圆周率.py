#!/usr/bin/env python
"""
-*- coding: utf-8 -*-
@Time    : 2018-03-16 12:02
@Author  : hys
@Site    : 
@File    : 求圆周率.py
@Software: PyCharm
@Desc     :
@license : Copyright(C), Your Company
@Contact : george.zw513@gmail.com
"""
from random import random
from math import sqrt
from time import clock

darts = 500000000  # 循环次数
hits = 0  # 圆内的点
clock()  # 开始记时
for i in range(1, darts):
    x, y = random(), random()
    dis = sqrt(x**2 + y**2)
    if dis <= 1:
        hits += 1
pi = 4*hits/darts
print("圆周率 = " + str(pi))
print("运行时间是： " + str(clock()))
