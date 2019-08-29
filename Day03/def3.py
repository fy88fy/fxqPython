# -*- coding: utf-8 -*-
# @Time    : 2019/8/20 23:46
# @Author  : Feng Xiaoqing
# @FileName: def3.py
# @Software: PyCharm
# @Function：
#----------------------------------- 
def test1():
    print('in the test1')

def test2():
    print('in the test2')
    return 0

def test3():
    print('in the test3')
    return 1,'hello',['alex','haha',{'name': 'alex'}]

x = test1()
y = test2()
z = test3()
print(x)
print(y)
print(z)