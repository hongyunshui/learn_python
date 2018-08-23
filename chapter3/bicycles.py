#!/usr/bin/env python
"""
-*- coding: utf-8 -*-
@Time    : 2018-02-11 11:23
@Author  : hys
@Site    : 
@File    : bicycles.py
@Software: PyCharm
@Desc     :
@license : Copyright(C), Your Company
@Contact : george.zw513@gmail.com
"""
bicycles = [ 'trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
print('\t'+bicycles[0].title())

#3.1.2  索引从0而不是1开始

print("第二个元素是："+bicycles[1])
print("第三个元素是："+bicycles[2])

print("最后一个元素是：" + bicycles[-1])
print("倒数第二个元素是：" + bicycles[-2])
print("倒数第三个是：" + bicycles[-3])

#3.1.3  使用列表中的各个值
message = "my last bicycle is a " + bicycles[-1]
print(message)

friends_name = ['chang yan kai', 'gao xiao min ', 'wan xiao lin', 'wang xiao yang', 'deng yan pu ', 'zhao zhan long', 'song zhi zhong', 'gu xiao yao ', 'kang wei peng ', 'zhao shun long']
for name in friends_name:
    print(name.title() + "早上好")

通勤方式 = ["骑自行车", "骑摩托车", "自驾汽车", "乘公交车"]
print(通勤方式)

for 通勤 in 通勤方式 :
    print("我喜欢" + 通勤 + "去上班")
