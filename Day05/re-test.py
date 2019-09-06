# -*- coding: utf-8 -*-
# @Time    : 2019/9/5 7:34
# @Author  : Feng Xiaoqing
# @FileName: re-test.py
# @Software: PyCharm
# @Function：
#----------------------------------- 
import re

# a = re.match('C.+','Chen123gFeng')#从头开始
# print(a)
# print(a.group())

# a = re.search('F[a-zA-Z]+','Chen123gFeng123affff')#从头开始
# print(a)
# print(a.group())

# a = re.search('#.*#','Chen#123gF#eng123affff')#从头开始
# print(a)
# print(a.group())
#
# a = re.search('aC?','aCCaChen#123gF#eng123aaffff')#从头开始
# print(a)
# print(a.group())


a = re.search('[0-9](3)','aCCaChen3123gF#eng123aaffff')#从头开始
print(a)
print(a.group())
