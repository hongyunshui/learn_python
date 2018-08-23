#!/usr/bin/env python
"""
-*- coding: utf-8 -*-
@Time    : 2018-03-11 21:52
@Author  : hys
@Site    : 
@File    : 练习.py
@Software: PyCharm
@Desc     :
@license : Copyright(C), Your Company
@Contact : george.zw513@gmail.com
"""
# 4-3 数到20 ：使用一个for 循环打印数字1~20（含）。
for number in range(1, 21):
    print(number)
# 4-4 一百万 ：创建一个列表，其中包含数字1~1 000 000，再使用一个for 循环将这些数字打印出来（如果输出的时间太长，按Ctrl + C停止输出，或关闭输出窗口）。
# numbers = [value for value in range(1, 1000001)]
numbers = []
for value in range(1, 1000000):
    numbers.append(value)
print("最大值")
print(max(numbers))
print("最小值")
print(min(numbers))
# for number in numbers:
#     print(number)
# 4-5 计算1~1 000 000的总和 ：创建一个列表，其中包含数字1~1 000 000，再使用min() 和max() 核实该列表确实是从1开始，到
# 1 000 000结束的。另外，对这个列表调用函数sum() ，看看Python将一百万个数字相加需要多长时间。
sum(numbers)
# 4-6 奇数 ：通过给函数range() 指定第三个参数来创建一个列表，其中包含1~20的奇数；再使用一个for 循环将这些数字都打印出来。
for value in range(1, 20, 2):
    print(value)
# 4-7 3的倍数 ：创建一个列表，其中包含3~30内能被3整除的数字；再使用一个for 循环将这个列表中的数字都打印出来。
numbers = [value for value in range(3, 30, 3)]
print("3~30能被3整出的数：")
for number in numbers:
    print(number)
# 4-8 立方 ：将同一个数字乘三次称为立方。例如，在Python中，2的立方用2**3 表示。请创建一个列表，其中包含前10个整数（即1~10）
# 的立方，再使用一个for 循环将这些立方数都打印出来。
numbers = [value ** 3 for value in range(1, 11)]
print(numbers)
# 4-9 立方解析 ：使用列表解析生成一个列表，其中包含前10个整数的立方。

# 动手试一试
# 4-10 切片 ：选择你在本章编写的一个程序，在末尾添加几行代码，以完成如下任务。
# 打印消息“The first three items in the list are:”，再使用切片来打印列表的前三个元素。
players = ["aa", "bb", "cc", "dd", "ee", "ff", "gg"]
print("the first items in the list are :")
print(players[:3])
# 打印消息“Three items from the middle of the list are:”，再使用切片来打印列表中间的三个元素。
print("中间三个元素是：")
print(players[2:5])
# 打印消息“The last three items in the list are:”，再使用切片来打印列表末尾的三个元素。
print("最后三个元素是：")
print(players[4:])
# 4-11 你的比萨和我的比萨 ：在你为完成练习4-1而编写的程序中，创建比萨列表的副本，并将其存储到变量friend_pizzas 中，再完成如
# 下任务。
# 在原来的比萨列表中添加一种比萨。
# 在列表friend_pizzas 中添加另一种比萨。
# 核实你有两个不同的列表。为此，打印消息“My favorite pizzas are:”，再使用一个for 循环来打印第一个列表；打印消息
# “My friend's favorite pizzas are:”，再使用一个for 循环来打印第二个列表。核实新增的比萨被添加到了正确的列表中。
# 4-12 使用多个循环 ：在本节中，为节省篇幅，程序foods.py的每个版本都没有使用for 循环来打印列表。请选择一个版本的foods.py，
# 在其中编写两个for 循环，将各个食品列表都打印出来。

# 动手试一试
# 4-13 自助餐 ：有一家自助式餐馆，只提供五种简单的食品。请想出五种简单的食品，并将其存储在一个元组中。
# 使用一个for 循环将该餐馆提供的五种食品都打印出来。
# 尝试修改其中的一个元素，核实Python确实会拒绝你这样做。
# 餐馆调整了菜单，替换了它提供的其中两种食品。请编写一个这样的代码块：给元组变量赋值，并使用一个for 循环将新元组的每个元素
# 都打印出来。
foods = ("馒头", "大米", "白菜", "花生", "白面")
for food in foods:
    print(food)
# foods[2] = "腊肉"
print(foods)
print(foods[3])
foods = (foods[0], foods[1], "大豆", "芹菜", foods[4])
print(foods)

del foods
# foods = (value for value in players)
print(foods)
