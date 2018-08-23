#!/usr/bin/env python
"""
-*- coding: utf-8 -*-
@Time    : 2018-03-13 12:17
@Author  : hys
@Site    : 
@File    : 用户输入和while循环.py
@Software: PyCharm
@Desc     :
@license : Copyright(C), Your Company
@Contact : george.zw513@gmail.com
"""

# 7.1函数input() 的工作原理
name = input("please enter your name: ")
print("hello " + name)

prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nwhat's your name: "
name = input(prompt)
print("你好" + name)

# 7.1.2使用int() 来获取数值输入
height = input("请输入你的身高： ")
height = int(height)

if height >= 10:
    print("你可以乘坐过山车。")

# 7.2while 循环简介
# for 循环用于针对集合中的每个元素都一个代码块，而while 循环不断地运行，直到指定的条件不满足为止
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program.\n# "
message = ""
# while message != "退出":
#     message = input(prompt)
#     if message != "退出":
#         print(message)

# active = True
# while active:
#     message = input(prompt)
#     if message != "退出":
#         print(message)
#     else:
#         active = False

while True:
    message = input(prompt)
    if message != "退出":
        print(message)
    else:
        print("程序结束")
        break

# 7.2.5在循环中使用continue
current_number = 0
while current_number < 90:
    current_number += 1
    if current_number % 10 == 0:
        continue
    print(current_number)


