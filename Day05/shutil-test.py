#!/usr/bin/env python
#-*- coding:utf-8 _*-

"""
@author: Fengxiaoqing
@contact: fy88fy@163.com
@software: PyCharm
@file: shutil-test.py
@time: 2019/9/3 17:47
"""

import shutil
#
# f1 = open('os-test.py','w')
# f2 = open('2.txt','w')

# shutil.copyfile('os-test.py','1.txt')
# shutil.copytree('package_test','module_test')
shutil.make_archive('shutil_test.zip','zip','E:/fxqPython/Day05')
