# -*- coding: utf-8 -*-
# @Time    : 2019/9/18 7:08
# @Author  : Feng Xiaoqing
# @FileName: fanshe.py
# @Software: PyCharm
# @Function：
#-----------------------------------

def bulk(self):
    print("%s is yall....," %self.name)
class Dog(object):

    def __init__(self,name):
        self.name = name

    def eat(self,food):
        print("%s is eating %s"  % (self.name,food))

d = Dog("wangxiao")
choice = input(">>:").strip()

if hasattr(d,choice):
    # func = getattr(d,choice)
    # func("chengrong")

    delattr(d,choice)
else:
    setattr(d,choice,bulk)
    d.talk(d)

print(d.name)