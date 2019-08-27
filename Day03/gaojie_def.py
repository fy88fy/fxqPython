# -*- coding: utf-8 -*-
# @Time    : 2019/8/22 23:53
# @Author  : Feng Xiaoqing
# @FileName: gaojie_def.py
# @Software: PyCharm
# @Function：
#----------------------------------- 
def add(x, y, f):
    return f(x) + f(y)
res = add(3,-6,abs)
print(res)

res = add(3, -6, abs)
print(res)