# -*- coding: utf-8 -*-
# @Time    : 2019/8/22 23:33
# @Author  : Feng Xiaoqing
# @FileName: digui.py
# @Software: PyCharm
# @Function：
#----------------------------------- 

def calc(n):
    print(n)
    if int(n/2) >0 :
        return calc(int(n/2))
    print("---->>>",n)

calc(100)