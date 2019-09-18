# -*- coding: utf-8 -*-
# @Time    : 2019/9/17 7:37
# @Author  : Feng Xiaoqing
# @FileName: static_func.py
# @Software: PyCharm
# @Function：
#----------------------------------- 
#静态方法：
# class Dog(object):
#
#     def __init__(self,name):
#         self.name = name
#
#     @staticmethod#实际上跟类没有什么关系了。
#     def eat(self):
#
#         print("%s is eating %s " % (self.name,"baozi"))
#
#
# d = Dog("xiawang")
# d.eat(d)


import os
# os.system()
# os.mkdir()

class Dog(object):
    '''这个类是描述狗这个对象的'''

    def __init__(self,name):
        self.name = name
        self.__food = None

    #@staticmethod #实际上跟类没什么关系了
    #@classmethod
    @property #attribute
    def eat(self):
        print("%s is eating %s" %(self.name,self.__food))
    @eat.setter
    def eat(self,food):
        print("set to food:",food)
        self.__food = food
    @eat.deleter
    def eat(self):
        del self.__food
        print("删完了")

    def talk(self):
        print("%s is talking"% self.name)

    def __call__(self, *args, **kwargs):
        print("running call",args,kwargs)

    def __str__(self):
        return "<obj:%s>" %self.name

#print(Dog.__dict__) #打印类里的所有属性，不包括实例属性
d = Dog("ChenRonghua")
print(d)
# print(d.__dict__) #打印所有实例属性，不包括类属性
# d(1,2,3,name=333)

#Dog("ChenRonghua")()
