# -*- coding: utf-8 -*-
# @Time    : 2019/8/29 7:44
# @Author  : Feng Xiaoqing
# @FileName: json_xuleihua.py
# @Software: PyCharm
# @Function：
#----------------------------------- 
import json

info = {
    'name': 'fxq',
    'age': 22,
}

f = open('info.txt','w')
f.write(json.dumps(info))
f.close()

#
# import pickle
#
# def sayhi():
#     print('hello')
#
# info = {
#     'name': 'fxq',
#     'age': 22,
#     'func':sayhi
# }
#
# f = open('info.txt','wb')
#
# # f.write(pickle.dumps(info))
# pickle.dump(info,f)
# f.close()