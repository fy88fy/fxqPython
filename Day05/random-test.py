#!/usr/bin/env python
#-*- coding:utf-8 _*-

"""
@author: Fengxiaoqing
@contact: fy88fy@163.com
@software: PyCharm
@file: random-test.py
@time: 2019/9/3 14:08
"""
#
# def checkcode():
#     import random
#     checkcode = ''
#
#     for i in range(5):
#         current = random.randint(0,5)
#         if current == i:
#             tmp = chr(random.randint(65,90))
#         else:
#             tmp = random.randint(0,9)
#         checkcode += str(tmp)
#     print(checkcode)
#
# checkcode()


def checkcode():
    import random
    checkcode=''

    for i in range(4):
        current = random.randint(1,4)
        if current == i:
            tmp = chr(random.randint(66,90))
        else:
            tmp = random.randint(0,9)
        checkcode += str(tmp)
    return checkcode
print(checkcode())