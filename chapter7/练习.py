#!/usr/bin/env python
"""
-*- coding: utf-8 -*-
@Time    : 2018-03-13 14:33
@Author  : hys
@Site    : 
@File    : 练习.py
@Software: PyCharm
@Desc     :
@license : Copyright(C), Your Company
@Contact : george.zw513@gmail.com
"""
# 动手试一试
# 7-1 汽车租赁 ：编写一个程序，询问用户要租赁什么样的汽车，并打印一条消息，如“Let me see if I can find you a Subaru”。
car = input("请输入你想租赁的汽车型号： ")
print("请稍等，我们正在查询是否有" + car + "汽车可以租赁...")
# 7-2 餐馆订位 ：编写一个程序，询问用户有多少人用餐。如果超过8人，就打印一条消息，指出没有空桌；否则指出有空桌。
number = input("请输入您要用餐的人数： ")
number = int(number)
if number > 8:
    print("抱歉，暂时没有合适的空位。")
else:
    print("有合适的桌位，请就坐。")
# 7-3 10的整数倍 ：让用户输入一个数字，并指出这个数字是否是10的整数倍。
number = input("请输入一个数字： ")
number = int(number)
if number % 10 == 0:
    print(str(number) + " 是10的整数倍")
else:
    print(str(number) + " 不是10的整数倍")

# 7-4 比萨配料 ：编写一个循环，提示用户输入一系列的比萨配料，并在用户输入'quit' 时结束循环。每当用户输入一种配料后，都打印
# 一条消息，说我们会在比萨中添加这种配料。
pizzas = ["苹果"]
while True:
    a = input("请输入配料： ")
    if a == "quit":
        break
    pizzas.append(a)
    print(a + "已添加！")
print("请验证您的披萨配料：")
print(pizzas)
# 7-5 电影票 ：有家电影院根据观众的年龄收取不同的票价：不到3岁的观众免费；3~12岁的观众为10美元；超过12岁的观众为15美元。
# 请编写一个循环，在其中询问用户的年龄，并指出其票价。
# while True:
#     age = int(input("请输入你的年龄： "))
#     if age == 0:
#         break
#     elif age < 3:
#         print("你的电影票免费")
#     elif age < 12:
#         print("你的电影票费用为10美元。")
#     else:
#         print("你的电影票费用为15美元。")

# 7-6 三个出口 ：以另一种方式完成练习7-4或练习7-5，在程序中采取如下所有做法。
# 在while 循环中使用条件测试来结束循环。
# 使用变量active 来控制循环结束的时机。
# 使用break 语句在用户输入'quit' 时退出循环。
active = True
while active:
    age = input("请输入你的年龄： ")
    if age == "quit":
        active = False
        continue
    age = int(age)
    if age < 3:
        print("你的电影票免费")
    elif age < 12:
        print("你的电影票费用为10美元。")
    else:
        print("你的电影票费用为15美元。")
# 7-7 无限循环 ：编写一个没完没了的循环，并运行它（要结束该循环，可按Ctrl +C，也可关闭显示输出的窗口）。
