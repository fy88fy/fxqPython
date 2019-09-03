# -*- coding: utf-8 -*-
# @Time    : 2019/8/29 7:52
# @Author  : Feng Xiaoqing
# @FileName: json_fanxuleihua.py
# @Software: PyCharm
# @Function：
#----------------------------------- 
import json
f = open('info.txt','r')
data = json.loads(f.read())

print(data['age'])


# import pickle
# def sayhi():
#     print('hello1')
#
# f = open('info.txt','rb')
# # data = pickle.loads(f.read())
# data = pickle.load(f)
# print(data['func'](),data['name'])