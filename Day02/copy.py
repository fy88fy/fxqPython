#!/usr/bin/env python
#-*- coding:utf-8 _*-

"""
@author: Fengxiaoqing
@contact: fy88fy@163.com
@software: PyCharm
@file: copy.py
@time: 2019/7/31 10:57
"""
import copy

person = ['name',['saving',100]]
# #三种浅copy
# p1 = copy.copy(person)
# p2 = person[:]
# p3 = list(person)

#可以建立联合账号：
p1 = person[:]
p2 = person[:]

p1[0]='alex'
p2[0]='fengjie'

p1[1][1]=50

print(p1)
print(p2)