#!/usr/bin/env python
#-*- coding:utf-8 _*-

"""
@author: Fengxiaoqing
@contact: fy88fy@163.com
@software: PyCharm
@file: zhuangshiqi.py
@time: 2019/8/29 15:48
"""

import time
def main():
    def timer(func):
        def warrper():
            start_time = time.time()
            func()
            stop_time = time.time()
            print("\033[32mRun time is %s\033[0m" % (stop_time-start_time))
        return warrper

    @timer
    def test():
        time.sleep(2)
        print('hello')
    test()

if __name__ == "__main__":
    main()
