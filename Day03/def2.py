
# -*- coding: utf-8 -*-
# @Time    : 2019/8/20 23:27
# @Author  : Feng Xiaoqing
# @FileName: def2.py
# @Software: PyCharm
# @Function：
#----------------------------------- 
import time
def logger():
    time_format = '%Y-%m-%d %X'
    time_current = time.strftime(time_format)
    with open('a.txt','a+') as f:
        f.write('%s end action\n ' % time_current )

def test1():
    print('in the test1')
    logger()


def test2():
    print('in the test2')
    logger()

def test3():
    print('in the test3')
    logger()
x = test1()
y = test2()
z = test3()