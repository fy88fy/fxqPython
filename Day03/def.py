# -*- coding: utf-8 -*-
# @Time    : 2019/8/20 23:12
# @Author  : Feng Xiaoqing
# @FileName: def.py
# @Software: PyCharm
# @Function：
#----------------------------------- 

def func1():
    """定义函数"""
    print('in the func1')
    return 0

def func2():
    """定义过程"""
    print('in the func2')

x = func1()
y = func2()

print('from func1 return is %s ' % x)
print('from func2 return is %s ' % y)

