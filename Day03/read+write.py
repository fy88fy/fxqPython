#!/usr/bin/env python
#-*- coding:utf-8 _*-

"""
@author: Fengxiaoqing
@contact: fy88fy@163.com
@software: PyCharm
@file: read+write.py
@time: 2019/8/8 21:39
"""


def main():
    f = open('sing.txt','r+',encoding='utf-8')
    print(f.tell())
    print(f.read())
    print(f.tell())


if __name__ == "__main__":
    main()
