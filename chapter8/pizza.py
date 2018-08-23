#!/usr/bin/env python
"""
-*- coding: utf-8 -*-
@Time    : 2018-03-15 8:31
@Author  : hys
@Site    : 
@File    : pizza.py
@Software: PyCharm
@Desc     :
@license : Copyright(C), Your Company
@Contact : george.zw513@gmail.com
"""


def mk_pizza(size, *toppings):
    """概述要制作的比萨"""
    print("\nMaking a " + str(size) +
          "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)


# make_pizza(9, "牛肉", "白面", "奶油")
