# -*- coding: utf-8 -*-
# @Time    : 2019/9/10 22:53
# @Author  : Feng Xiaoqing
# @FileName: dog.py
# @Software: PyCharm
# @Function：
#----------------------------------- 
class Dog():
    def __init__(self,name):
        self.name = name
        
    def bulk(self):
        print('%s wang wang wang !!!' % self.name)

dog = Dog('cheng')
dog.bulk()