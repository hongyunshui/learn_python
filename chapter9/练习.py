#!/usr/bin/env python
"""
-*- coding: utf-8 -*-
@Time    : 2018-03-15 10:53
@Author  : hys
@Site    : 
@File    : 练习.py
@Software: PyCharm
@Desc     :
@license : Copyright(C), Your Company
@Contact : george.zw513@gmail.com
"""
from random import randint
# 动手试一试
# 9-1 餐馆 ：创建一个名为Restaurant 的类，其方法__init__() 设置两个属性：restaurant_name 和cuisine_type 。创建一个名
# 为describe_restaurant() 的方法和一个名为open_restaurant() 的方法，其中前者打印前述两项信息，而后者打印一条消息，指
# 出餐馆正在营业。根据这个类创建一个名为restaurant 的实例，分别打印其两个属性，再调用前述两个方法。


class Restaurant:
    """模拟餐馆的类"""
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print("餐馆的名字是： " + self.restaurant_name)
        print("餐馆的类型是： " + self.cuisine_type)

    def set_number_served(self, set_number):
        self.number_served = set_number

    def increment_number_served(self, increment_number):
        self.number_served += increment_number

    @staticmethod
    def open_restaurant():
        print("餐馆正在营业！")


# restaurant = Restaurant("HYS", "中式")
# print(restaurant.restaurant_name)
# print(restaurant.cuisine_type)
# restaurant.describe_restaurant()
# restaurant.open_restaurant()

# 9-2 三家餐馆 ：根据你为完成练习9-1而编写的类创建三个实例，并对每个实例调用方法describe_restaurant() 。
# restaurant1 = Restaurant("ZZ", "MDL")
# restaurant1.describe_restaurant()
# 9-3 用户 ：创建一个名为User 的类，其中包含属性first_name 和last_name ，还有用户简介通常会存储的其他几个属性。在类
# User 中定义一个名为describe_user() 的方法，它打印用户信息摘要；再定义一个名为greet_user() 的方法，它向用户发出个
# 性化的问候。创建多个表示不同用户的实例，并对每个实例都调用上述两个方法。


class Users:
    def __init__(self, first_name="", last_name="", age=0, sex=""):
        self.first_name = first_name
        self.last_name = last_name
        self.age = int(age)
        self.sex = sex
        self.login_attempts = 0

    def describe_user(self):
        fall_name = self.first_name.title() + self.last_name.title()
        print("用户姓名： " + fall_name)
        print("年龄： " + str(self.age))
        print("性别： " + self.sex)

    def greet_user(self):
        print("你好，" + self.first_name + self.last_name)

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


# hys = User("Zhao", "hys", , "F")

# 动手试一试
# 9-4 就餐人数 ：在为完成练习9-1而编写的程序中，添加一个名为number_served 的属性，并将其默认值设置为0。根据这个类创建一
# 个名为restaurant 的实例；打印有多少人在这家餐馆就餐过，然后修改这个值并再次打印它。
# 添加一个名为set_number_served() 的方法，它让你能够设置就餐人数。调用这个方法并向它传递一个值，然后再次打印这个值。
# 添加一个名为increment_number_served() 的方法，它让你能够将就餐人数递增。调用这个方法并向它传递一个这样的值：你认为这家
# 餐馆每天可能接待的就餐人数。
# 9-5 尝试登录次数 ：在为完成练习9-3而编写的User 类中，添加一个名为login_attempts 的属性。编写一个名为
# increment_login_attempts() 的方法，它将属性login_attempts 的值加1。再编写一个名为reset_login_attempts() 的方法，
# 它将属性login_attempts 的值重置为0。根据User 类创建一个实例，再调用方法increment_login_attempts() 多次。打印属性
# login_attempts 的值，确认它被正确地递增。然后，调用方法reset_login_attempts() ，并再次打印属性login_attempts 的值，
# 确认它被重置为0。

# 动手试一试
# 9-6 冰淇淋小店 ：冰淇淋小店是一种特殊的餐馆。编写一个名为IceCreamStand 的类，让它继承你为完成练习9-1或练习9-4而编写
# 的Restaurant 类。这两个版本的Restaurant 类都可以，挑选你更喜欢的那个即可。添加一个名为flavors 的属性，用于存储一个由
# 各种口味的冰淇淋组成的列表。编写一个显示这些冰淇淋的方法。创建一个IceCreamStand 实例，并调用这个方法。


class IceCreamStand(Restaurant):
    """冰淇淋小店"""
    def __init__(self, restaurant_name, cuisine_type):
        """初始化父类属性"""
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []

    def display_ice_cream(self):
        for ice_cream in self.flavors:
            print(ice_cream)

# 9-7 管理员 ：管理员是一种特殊的用户。编写一个名为Admin 的类，让它继承你为完成练习9-3或练习9-5而编写的User 类。添加
# 一个名为privileges 的属性，用于存储一个由字符串（如"can add post" 、"can delete post" 、"can ban user" 等）组成的列
# 表。编写一个名为show_privileges() 的方法，它显示管理员的权限。创建一个Admin 实例，并调用这个方法。


class Admin(Users):
    """模拟管理员"""
    def __init__(self, first_name, last_name, age, sex):
        super().__init__(first_name, last_name, age, sex)
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        print("管理员有如下权限： ")
        for privilege in self.privileges:
            print(privilege)


# 9-8 权限 ：编写一个名为Privileges 的类，它只有一个属性——privileges ，其中存储了练习9-7 所说的字符串列表。将方法
# show_privileges() 移到这个类中。在Admin 类中，将一个Privileges 实例用作其属性。创建一个Admin 实例，并使用方法
# show_privileges() 来显示其权限。


class Privileges:
    def __init__(self, first_name, last_name, age, sex):
        self.privileges = Admin(first_name, last_name, age, sex)


# 9-9 电瓶升级 ：在本节最后一个electric_car.py版本中，给Battery 类添加一个名为upgrade_battery() 的方法。这个方法检查
# 电瓶容量，如果它不是85，就将它设置为85。创建一辆电瓶容量为默认值的电动汽车，调用方法get_range() ，然后对电瓶进行升级，
# 并再次调用get_range() 。你会看到这辆汽车的续航里程增加了。

# 动手试一试
# 9-10 导入Restaurant 类 ：将最新的Restaurant 类存储在一个模块中。在另一个文件中，导入Restaurant 类，创建一个
# Restaurant 实例，并调用Restaurant 的一个方法，以确认import 语句正确无误。
# 9-11 导入Admin 类 ：以为完成练习9-8而做的工作为基础，将User 、Privileges 和Admin 类存储在一个模块中，再创建一
# 个文件，在其中创建一个Admin 实例并对其调用方法show_privileges() ，以确认一切都能正确地运行。
# 9-12 多个模块 ：将User 类存储在一个模块中，并将Privileges 和Admin 类存储在另一个模块中。再创建一个文件，在其中
# 创建一个Admin 实例，并对其调用方法show_privileges() ，以确认一切都依然能够正确地运行。

# 动手试一试
# 9-13 使用OrderedDict ：在练习6-4中，你使用了一个标准字典来表示词汇表。请使用OrderedDict 类来重写这个程序，并确认输
# 出的顺序与你在字典中添加键—值对的顺序一致。
# 9-14 骰子 ：模块random 包含以各种方式生成随机数的函数，其中的randint() 返回一个位于指定范围内的整数，例如，下面的代
# 码返回一个1~6内的整数：
# from random import randint
# x = randint(1, 6)
# 请创建一个Die 类，它包含一个名为sides 的属性，该属性的默认值为6。编写一个名为roll_die() 的方法，它打印位于1和骰子面数
# 之间的随机数。创建一个6面的骰子，再掷10次。 创建一个10面的骰子和一个20面的骰子，并将它们都掷10次。


class Die:
    def __init__(self, die_side=6):
        self.sides = die_side

    def roll_die(self):
        x = randint(1, self.sides)
        print("筛子的点数是： " + str(x))


# die = Die()
# die.roll_die()
# die.roll_die()

# 9-15 Python Module of the Week ：要了解Python标准库，一个很不错的资源是网站Python Module of the Week。
# 请访问http://pymotw.com/ 并查看其中的目录，在其中找一个你感兴趣的模块进行探索，或阅读模块collections 和random 的文档。


