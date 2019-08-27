# -*- coding: utf-8 -*-
# @Time    : 2019/8/27 0:10
# @Author  : Feng Xiaoqing
# @FileName: gaojie-def.py
# @Software: PyCharm
# @Function：
#----------------------------------- 


import time
def timer(func):
    def deco(*args,**kwargs):
        star_time = time.time()
        func(*args,**kwargs)
        stop_time = time.time()
        print("%s" % (stop_time - star_time))
        return func
    return deco

@timer
def test1():
    time.sleep(3)
    print("in the test1")

@timer
def test2(name):
    time.sleep(2)
    print("in test2",name)

test1()
test2("fxq")



