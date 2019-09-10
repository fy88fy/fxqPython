# -*- coding: utf-8 -*-
# @Time    : 2019/9/9 22:59
# @Author  : Feng Xiaoqing
# @FileName: class-test.py
# @Software: PyCharm
# @Function：
#-----------------------------------
'''装饰器'''
import  time
class foo1:
    def foo(func):
        def wrraper():
            start_time = time.time()
            func()
            stop_time = time.time()
            print("I am in foo ,Running time is %s" % (stop_time-start_time))
        return wrraper

    @ foo
    def test():
        time.sleep(3)
        print("hello in test program.")
        print("I want to be a \033[32m security progammer\033[0m or \033[32msecurity engineer\033[0m")

    test()
# foo=foo()
foo1