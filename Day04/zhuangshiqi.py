# -*- coding: utf-8 -*-
# @Time    : 2019/8/26 23:18
# @Author  : Feng Xiaoqing
# @FileName: zhuangshiqi.py
# @Software: PyCharm
# @Function：
#----------------------------------- 

import time

def timmer(func):
    def warpper(*args,**kwargs):
        start_time = time.time()
        func()
        stop_time = time.time()
        print("The func run time is %s" % (stop_time-start_time))
    return warpper

@timmer
def test1():
    time.sleep(3)
    print("In the test1.")

test1()


