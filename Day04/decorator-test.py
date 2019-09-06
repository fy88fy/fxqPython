#!/usr/bin/env python
#-*- coding:utf-8 _*-

"""
@author: Fengxiaoqing
@contact: fy88fy@163.com
@software: PyCharm
@file: decorator-test.py
@time: 2019/9/2 10:15
"""

import time
def main():
    a = 65
    def timer(func):
        def wrapper():
            start_time = time.time()
            func()
            stop_time = time.time()

            print("Project run time is %s" % (stop_time - start_time))
            print(a)
        return wrapper

    @timer
    def test():
        time.sleep(3)

        print("Hello!")

    test()



if __name__ == "__main__":
    main()
