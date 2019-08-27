# -*- coding: utf-8 -*-
# @Time    : 2019/8/20 23:59
# @Author  : Feng Xiaoqing
# @FileName: def4.py
# @Software: PyCharm
# @Function：
#----------------------------------- 
def test(x,y):
    print(x)
    print(y)

test(1,2)
test(y=1,x=2)
print('#'*50)

def test1(x,y=2):
    print(x)
    print(y)

test1(1)
test1(y=1,x=2)

print('#'*50)
'''参数组'''
def test2(*args):
    print(args)

test2(1,3,33,33)

def test3(x,*args):
    print(x)
    print(args)

test3(1,234,'fxq','aaa')

print('#'*50)

def logger(source):
    print("from logger %s" % source)



def test4(name,age=18,*args,**kwargs):
    print(name)
    print(age)
    print(args)
    print(kwargs)
    logger(source)
test4('fxq',age = 22,sex = 'M',hobby = 'base')