#!/usr/bin/env python
"""
-*- coding: utf-8 -*-
@Time    : 2018-02-11 15:33
@Author  : hys
@Site    : 
@File    : motorcycles.py
@Software: PyCharm
@Desc     :
@license : Copyright(C), Your Company
@Contact : george.zw513@gmail.com
"""
#3.2.1　修改列表元素
motorcycles = [ 'honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)
#3.2.2　在列表中添加元素
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
#1. 在列表末尾添加元素
motorcycles.append('ducati')
print(motorcycles)

工具 = []
工具.append('汽车')
工具.append('锤子')
工具.append('镰刀')
工具.append('计算机')
工具.append('蒸锅')
print(工具)
工具.insert(2, '水杯')

print(工具)
del 工具[-1]
print(工具)

#2. 使用方法pop() 删除元素

最后一个工具 = 工具.pop()
print(工具)
print(最后一个工具)

第二个工具 = 工具.pop(1)
print(工具)
print(第二个工具)

#不确定位置的情况下按值删除
工具.remove("汽车")
print(工具)
#当删除的值不在列表中时会报语法错误
#工具.remove("钉子")
print(工具)
