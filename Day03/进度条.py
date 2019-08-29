#!/usr/bin/env python
#-*- coding:utf-8 _*-

"""
@author: Fengxiaoqing
@contact: fy88fy@163.com
@software: PyCharm
@file: 进度条.py
@time: 2019/8/8 21:30
"""
import sys,time

def main():
    for i in range(50):
        sys.stdout.write(">")
        sys.stdout.flush()
        time.sleep(0.1)
if __name__ == "__main__":
    main()
