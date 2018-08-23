#!/usr/bin/env python
"""
-*- coding: utf-8 -*-
@Time    : 2018-03-05 14:13
@Author  : hys
@Site    :
@File    : opt_list.py
@Software: PyCharm
@Desc     :
@license : Copyright(C), Your Company
@Contact : george.zw513@gmail.com
"""
#4.1　遍历整个列表
magicians = ['alice', 'david', 'carolina', 'alice']
for magician in magicians:
    print(magician)
print(magicians)



for value in range(1,9):
    print(value)

numbers = list(range(1, 6))
print(numbers)


eventnumbers = list(range(1, 9, 2))
print(eventnumbers)

squares = []
for value in list(range(1, 5)):
    squares.append(value ** 2)
print(squares)

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print("列表中各个数字之和是：")
print(sum(digits))
print("列表中的最大数字是：")
print(max(digits))
print("列表中的最小值是：")
print(min(digits))


squares = [value ** 3 for value in range(1, 6)]
print("列表解析：")
print(squares)

#切片
players = ["a", "ab", "ccd", "asbcd"]
print(players[1:4])
print(players[:3])
print(players[1:])

for player in players[2:4]:
    print(player)

x = 3
print(players[:x])

pp = players
players.append("fffff")
print(pp)

ppp = players[:]
players.append("ddd")
print(players)
print(ppp)

