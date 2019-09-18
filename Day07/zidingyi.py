# -*- coding: utf-8 -*-
# @Time    : 2019/9/18 8:04
# @Author  : Feng Xiaoqing
# @FileName: zidingyi.py
# @Software: PyCharm
# @Function：
#----------------------------------- 
class fxqException(Exception):
    def __init__(self, msg):
        self.message = msg

    # def __str__(self):
    #     return self.message

try:
    raise fxqException('我的异常')

except fxqException as e:
    print(e)