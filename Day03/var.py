# -*- coding: utf-8 -*-
# @Time    : 2019/8/22 23:07
# @Author  : Feng Xiaoqing
# @FileName: var.py
# @Software: PyCharm
# @Function：
#----------------------------------- 

def change_name(name):
    global school  #可改全局变量,除了字符串和整数不能改
    school = "Tian jing"
    print("Before change",name,school)
    name = "FXQ" #局部变量，函数是变量的作用域
    age = '22'
    print("After change",name)

    names[0] = "fengxiaoqing"
    print(names)

name= "fxq"
school = "Qing Hua"

names = ["fxq","Jack","feng"]

change_name(name)
print(name,school,names)