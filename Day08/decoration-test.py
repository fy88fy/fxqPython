# -*- coding: utf-8 -*-
# @Time    : 2019/9/26 23:05
# @Author  : Feng Xiaoqing
# @FileName: decoration-test.py
# @Software: PyCharm
# @Function：
#----------------------------------- 

# import time
# def timeer(func):
#
#     def wrapper(*args,**kwargs):
#         start_time = time.time()
#         func(*args,**kwargs)
#         stop_time = time.time()
#         print('The project has run : %s ' % (stop_time - start_time))
#     return wrapper
# @ timeer
# def test(name):
#     time.sleep(2)
#     print(name,"in the test.")
#
# name = 111
# t = test('aaa')
# t = test('bbb')


import  time

def timeer(func):
    def wrraper(*args,**kwargs):
        start_time = time.time()
        func(*args,**kwargs)
        stop_time = time.time()
        print("\033[32mRunning time :\033[0m%s " % (stop_time - start_time) )
    return wrraper

@ timeer
def Student(name):
    time.sleep(2)
    print("\033[32m%s\033[0m is running... " % name)

student = Student('fengxiaoqing')

