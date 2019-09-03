# -*- coding: utf-8 -*-
# @Time    : 2019/9/3 7:11
# @Author  : Feng Xiaoqing
# @FileName: main.py
# @Software: PyCharm
# @Function：
#----------------------------------- 
# from test import sayhi
# def logger():
#     print("in logger")
#     sayhi()
#
# def search():
#     print("in search")
#     sayhi()
# logger()
# search()

# from test import sayhi as sayhi_test,name
# print(name)
# print(sayhi_test())


import os,sys

x = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(x)

import package_test