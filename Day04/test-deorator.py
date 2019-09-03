# -*- coding: utf-8 -*-
# @Time    : 2019/8/27 22:12
# @Author  : Feng Xiaoqing
# @FileName: test-deorator.py
# @Software: PyCharm
# @Function：
#----------------------------------- 

import  time
def timer(func):
    def wrapper(*args,**kwargs):
        start_time = time.time()
        func(*args,**kwargs)
        stop_time = time.time()
        print("The time is %s" % (stop_time-start_time))
        print("#"*50)
    return wrapper

@timer
def test1(name):
    time.sleep(2)
    print("in the test1...",name)

@timer
def test2(name):
    time.sleep(3)
    print("\033[32;2min the test2...\033[0m",name)

test1('122')
test2("111")