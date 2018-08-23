#!/usr/bin/env python
"""
-*- coding: utf-8 -*-
@Time    : 2018-03-15 10:09
@Author  : hys
@Site    : 
@File    : learn_class.py
@Software: PyCharm
@Desc     :
@license : Copyright(C), Your Company
@Contact : george.zw513@gmail.com
"""
# import chapter9.dog as dog # 如果不使用别名在调用时需要输入全部路径
import chapter9.dog
from chapter9.练习 import Users, Restaurant, IceCreamStand, Admin, Privileges, Die
my_dog = chapter9.dog.Dog("kk", 8)  # 如果不使用别名在调用时需要输入全部路径
print(my_dog.name + " " + str(my_dog.age))

hys = Users('zhao', 'hys', 9, 'F')
hys.describe_user()
hys.increment_login_attempts()
hys.increment_login_attempts()
hys.increment_login_attempts()
print("登陆次数是： ")
print(str(hys.login_attempts))
hys.reset_login_attempts()
print(hys.login_attempts)

ice_cream_stand = IceCreamStand("冰淇淋小店", "冷饮")
ice_cream_stand.describe_restaurant()
ice_cream_stand.flavors = ["老冰棍", "冰块", "西瓜味道", "菠萝味道"]
ice_cream_stand.display_ice_cream()

restaurant = Restaurant("餐馆", "中餐")
# print("就餐人数： " + str(restaurant.number_served))
# restaurant.number_served = 100
# print("就餐人数： " + str(restaurant.number_served))
# restaurant.set_number_served(900)
# print("就餐人数： " + str(restaurant.number_served))
restaurant.increment_number_served(150)
print("就餐人数： " + str(restaurant.number_served))

admin = Admin("zhao", "jianhong", 20, "F")
admin.show_privileges()

privileges = Privileges("k", "k", 30, "M")
privileges.privileges.describe_user()
privileges.privileges.show_privileges()

die = Die(20)
die.roll_die()


