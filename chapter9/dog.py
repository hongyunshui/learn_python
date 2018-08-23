#!/usr/bin/env python
"""
-*- coding: utf-8 -*-
@Time    : 2018-03-15 10:33
@Author  : hys
@Site    : 
@File    : dog.py
@Software: PyCharm
@Desc     :
@license : Copyright(C), Your Company
@Contact : george.zw513@gmail.com
"""


class Dog:  # 类名之后不需要圆括号
    """一次模拟小狗的尝试"""
    def __init__(self, name, age):
        """初始化属性"""
        self.name = name
        self.age = age

    def sit(self):
        """模拟小狗被命令蹲下"""
        print(self.name.title() + " is now sitting")

    def roll_over(self):
        """模拟小狗打滚"""
        print(self.name.title() + " is rolled over")


# my_dog = Dog("jj", 9)
# print(my_dog.name + str(my_dog.age))
